#!/bin/bash
#
# Script for launching the Docker integration tests
# XXX: We currently only support running integration-cli.
#

set -Eeuo pipefail

DOCKER_DIR=/usr/src/docker
SCRIPTS_DIR="$DOCKER_DIR/hack"
VERSION="$(cat "$DOCKER_DIR/VERSION")"

# working dirs
FROZEN_IMAGES_DIR="/tmp/docker-frozen-images"
FROZEN_IMAGES_LINK=/docker-frozen-images

readarray -t TESTS < <(find "$DOCKER_DIR/integration-cli" -type f -executable -name 'tests.main')
CHECK_TIMEOUT="${CHECK_TIMEOUT:-15m}"
TEST_TIMEOUT="${TEST_TIMEOUT:-0}"
TEST_ARGS=("-check.v" "-check.timeout=${CHECK_TIMEOUT}" "-test.timeout=${TEST_TIMEOUT}")
TEST_SELECT=
TEST_LOG=/tmp/docker-tests.log
KEEPBUNDLE="${KEEPBUNDLE:-}"

# the config file for Docker
CFG_DOCKER=/etc/docker/daemon.json

################################################################################

log()   { echo ">>> $@" ; }
warn()  { log "WARNING: $@" ; }
error() { log "ERROR: $@" ; }
abort() { log "FATAL: $@" ; exit 1 ; }
usage() { echo "$USAGE" ; }
abort_usage() { usage ; abort "$@" ; }

bundle() {
	local bundle="$1"; shift
	log "Making bundle: $(basename "$bundle") (in $PWD)"
	local oldFlags="$-"
	set +Eeu
	source "$SCRIPTS_DIR/make/$bundle" "$@"
	set "-$oldFlags"
}

save_backup() {
	for x in $@ ; do
		if [ ! -f "$x" ] ; then
			touch "$x.nbak"
		elif [ -f "$x.bak" ] ; then
			warn "$x.bak already exists: no backup will be done"
		else
			cp -f "$x" "$x.bak"
		fi
	done
}

restore_backup() {
	for x in $@ ; do
		if [ -f "$x.nbak" ] ; then
			rm -f "$x.nbak"
		elif [ -f "$x.bak" ] ; then
			mv -f "$x.bak" "$x"
		fi
	done
}

require_go()  { go version  >/dev/null 2>&1 ; }
require_git() { git version >/dev/null 2>&1 ; }

################################################################################

[ "${#TESTS[@]}" -gt 0 ] || abort "integration tests executable not found in $DOCKER_DIR"
[ "$EUID" -eq 0 ]        || abort "this script must be run as root"
[ -n "$VERSION" ]        || abort "could not obtain version"

if [ "$#" -gt 0 ] ; then
	# run only some specific tests
	TEST_ARGS+=( "-check.f=$(echo $@ | tr ' ' '|')" )
fi

# tests require this user and group
/usr/sbin/groupadd -r docker >/dev/null 2>&1 || /bin/true
/usr/sbin/useradd --create-home --gid docker unprivilegeduser >/dev/null 2>&1 || /bin/true

export DOCKER_TEST_HOST="tcp://127.0.0.1:2375"
export PATH="/usr/local/bin:$PATH"
export TZ=utc

export DOCKER_GRAPHDRIVER="${DOCKER_GRAPHDRIVER:-vfs}"
export DOCKER_USERLANDPROXY="${DOCKER_USERLANDPROXY:-true}"
export DOCKER_STORAGE_OPTS="${DOCKER_STORAGE_OPTS:-}"
export DOCKER_REMAP_ROOT="${DOCKER_REMAP_ROOT:-}" # "default" uses dockremap

# Example usage: DOCKER_STORAGE_OPTS="dm.basesize=20G,dm.loopdatasize=200G".
storage_opts=()
if [ -n "$DOCKER_STORAGE_OPTS" ]; then
	IFS=','
	for i in ${DOCKER_STORAGE_OPTS}; do
		storage_opts+=("$i")
	done
	unset IFS
fi

# deal with remapping
save_backup /etc/subuid /etc/subgid
echo "dockremap:500000:65536"  >/etc/subuid
echo "dockremap:500000:65536"  >/etc/subgid
groupadd dockremap             >/dev/null 2>&1 || /bin/true
useradd -g dockremap dockremap >/dev/null 2>&1 || /bin/true

# make sure Docker is stopped, set our config file and then start again
save_backup "$CFG_DOCKER"
cat <<CFG_DOCKER_EOF >"$CFG_DOCKER"
{
	"log-level": "debug",
	"log-driver": "json-file",
	"log-opts": {
		"max-size": "50m",
		"max-file": "5"
	},
	"userns-remap": "$DOCKER_REMAP_ROOT",
	"hosts": [
		"tcp://127.0.0.1:2375"
	],
	"storage-driver": "$DOCKER_GRAPHDRIVER",
	"storage-opts": [
		$(printf '"%s",' "${storage_opts[@]}" | sed 's/"",//g;$s/,$//')
	],
	"userland-proxy": $DOCKER_USERLANDPROXY
}
CFG_DOCKER_EOF
systemctl restart docker.service

cleanup() {
	log "Restoring configuration files..."
	restore_backup /etc/subuid /etc/subgid "$CFG_DOCKER"
	rm -f "$FROZEN_IMAGES_LINK"

	log "Removing images and containers..."
	export DOCKER_HOST="$DOCKER_TEST_HOST"
	docker ps -aq    | xargs docker rm  -f &>/dev/null || :
	docker images -q | xargs docker rmi -f &>/dev/null || :

	log "Restarting the Docker service in a pristine state..."
	systemctl restart docker.service
}
trap cleanup EXIT

cd "$DOCKER_DIR"

export MAKEDIR="$SCRIPTS_DIR/make"
export DOCKER_HOST="$DOCKER_TEST_HOST"

# Clean up all images on the host -- this is key to avoid test run failures.
log "Cleaning the environment..."
docker ps -aq    | xargs docker rm  -f &>/dev/null || :
docker images -q | xargs docker rmi -f &>/dev/null || :

log "Preparing the environment..."
bundle .integration-daemon-setup

# XXX: Really this should be sourced from the Dockerfile but this is good
#      enough for now. This comes from the Docker 18.09.1-ce Dockerfile.
log "Downlading frozen images..."
mkdir -p "$FROZEN_IMAGES_DIR"
ln -sf "$FROZEN_IMAGES_DIR" "$FROZEN_IMAGES_LINK"
"$DOCKER_DIR/contrib/download-frozen-image-v2.sh" "$FROZEN_IMAGES_DIR" \
	buildpack-deps:jessie@sha256:dd86dced7c9cd2a724e779730f0a53f93b7ef42228d4344b25ce9a42a1486251 \
	busybox:latest@sha256:bbc3a03235220b170ba48a157dd097dd1379299370e1ed99ce976df0355d24f0 \
	busybox:glibc@sha256:0b55a30394294ab23b9afd58fab94e61a923f5834fba7ddbae7f8e0c11ba85e6 \
	debian:jessie@sha256:287a20c5f73087ab406e6b364833e3fb7b3ae63ca0eb3486555dc27ed32c6e60 \
	hello-world:latest@sha256:be0cd392e45be79ffeffa6b05338b98ebb16c87b255f48e297ec7f98e123905c

# The code within integration-cli which handles building *-test images doesn't
# appear to work within our setup, not to mention we don't want to Require: a
# bunch of build tools so we just use the provided Dockerfile and
# buildpack-deps.
tar -cC "$FROZEN_IMAGES_DIR" . | docker load
for dir in "$DOCKER_DIR"/contrib/*-test
do
	log "Building *-test images ($dir)..."
	docker build -t "$(basename "$dir")" "$dir"
done

# For some reason, dockerd appears to put the containerd.sock in the wrong
# place under systemd. So we just manually add a symlink for it.
[ -e "/var/run/docker/containerd/containerd.sock" ] || \
	ln -s docker-containerd.sock /var/run/docker/containerd/containerd.sock

# And there appears to be an issue with daemon.json as a configuration format,
# so we need to hide our generated configuration. The original will be restored
# in cleanup().
rm -f "$CFG_DOCKER"

# Run all of our tests.
rm -f "$TEST_LOG"
for TEST in "${TESTS[@]}"
do
	cd "$(dirname "$TEST")"
	log "Running integration test ($TEST)..." | tee -a "$TEST_LOG"
	"$TEST" "${TEST_ARGS[@]}" 2>&1 | tee -a "$TEST_LOG" || :
done

export -n DOCKER_HOST
