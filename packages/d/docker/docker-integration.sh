#!/bin/bash
# docker-integration: run Docker's integration tests
# Copyright (C) 2024 SUSE LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

set -Eeuo pipefail

TESTDIR=/usr/src/docker-test
TEST_SRCDIR="$TESTDIR/src"
TEST_BINDIR="$TESTDIR/bin"

TMPROOT="$(mktemp --tmpdir -d docker-integration-tmpdir.XXXXXX)"
TMPDIR="$TMPROOT/tmp"
DEST="$TMPROOT/dest"

mkdir -p "$TMPDIR" "$TEST_BINDIR" "$DEST"
chmod 1777 "$TMPDIR"
chmod 777 "$TMPROOT"

function usage() {
	cat >&2 <<-EOF
	docker-integration.sh [-Av] [-r TestName] [-t timeout] [<test-suites>...]

	Arguments:
	  -A
	         Run all tests (do not fail on first suite failure).
	  -v
	         Run tests in verbose mode (go test -v).
	  -r
	         Only run tests that match the given regular expression (go test -run).
	  -t <timeout=$timeout>
	         Set the per-suite timeout to <timeout> (go test -timeout).
	  <test-suites>...
	         Only run the given test suites in /usr/src/docker-test. The
	         default is to run all test suites

	Examples:

	  Run the build and network integration tests with a 60 minute timeout:

	    ./docker-integration.sh -t 60m integration/build integration/network

	  Run all of the tests in verbose mode with a 6 hour timeout:

	    ./docker-integration.sh -Av -t 360m

	This script is maintained by openSUSE in the Virtualization:containers
	project, and is only intended to be used by openSUSE developers.
	EOF
	exit "${1:-1}"
}

fail_fast=1
verbose=
filter=
timeout=20m
while getopts "Ahr:t:v" opt; do
	case "$opt" in
	A)
		fail_fast=
		;;
	v)
		verbose=1
		;;
	r)
		filter="$OPTARG"
		;;
	t)
		timeout="$OPTARG"
		;;
	h)
		usage 0
		;;
	:)
		echo "Missing argument: -$OPTARG" >&2
		usage 1
		;;
	\?)
		echo "Invalid option: -$OPTARG" >&2
		usage 1
		;;
	esac
done

pushd "$TEST_SRCDIR"

if [ "$OPTIND" -le "$#" ]; then
	SUITES=("${@:$OPTIND:$(($#+1))}")
else
	readarray -t SUITES <<<"$(find . -type f -name test.main -printf "%h\n")"
fi
echo "Planning to run suites {${SUITES[@]}}."

# Download the frozen images.
if ! [ -d /docker-frozen-images ]; then
	# TODO: Get the hashes from /usr/src/docker-test/Dockerfile...
	contrib/download-frozen-image-v2.sh "$TMPDIR/docker-frozen-images" \
		busybox:latest@sha256:95cf004f559831017cdf4628aaf1bb30133677be8702a8c5f2994629f637a209 \
		busybox:glibc@sha256:1f81263701cddf6402afe9f33fca0266d9fff379e59b1748f33d3072da71ee85 \
		debian:bookworm-slim@sha256:2bc5c236e9b262645a323e9088dfa3bb1ecb16cc75811daf40a23a824d665be9 \
		hello-world:latest@sha256:d58e752213a51785838f9eed2b7a498ffa1cb3aa7f946dda11af39286c3db9a9 \
		arm32v7/hello-world:latest@sha256:50b8560ad574c779908da71f7ce370c0a2471c098d44d1c8f6b513c5a55eeeb1
	sudo cp -r "$TMPDIR/docker-frozen-images" /
fi

# Create binaries in $TEST_BINDIR.
if ! [ -e "$TEST_BINDIR/docker-basic-plugin" ]; then
	(
		pushd "$TEST_SRCDIR/testutil/fixtures/plugin/basic"

		go mod init docker-basic-plugin
		go build -o "$TEST_BINDIR/docker-basic-plugin" .
	)
fi
if ! [ -e "$TEST_BINDIR/registry-v2" ]; then
	# The v2.x tags of Docker registry don't use go.mod, and pre-date the move
	# to github.com/distribution, so we need to create a fake GOPATH with the
	# old github.com/docker/distribution import path.
	(
		export GOPATH="$(mktemp -d -p "$TMPROOT" distribution-build-gopath.XXXXXX)"
		pushd "$GOPATH"

		git clone \
			--depth=1 --branch=v2.8.3 \
			https://github.com/distribution/distribution.git \
			src/github.com/docker/distribution

		pushd src/github.com/docker/distribution

		GO111MODULE=off go build -o "$TEST_BINDIR/registry-v2" ./cmd/registry
	)
fi
if ! [ -e "$TEST_BINDIR/ctr" ]; then
	containerd-ctr --help >/dev/null
	ln -sf "$(which containerd-ctr)" "$TEST_BINDIR/ctr"
fi
if ! [ -e "$TEST_BINDIR/docker" ]; then
	# The integration-cli tests require a Docker 17.06.2 client (from 2017).
	# This is mainly because the tests are all based on the specific output the
	# client gives, and some tests fail on modern client versions.
	(
		export GOPATH="$(mktemp -d -p "$TMPROOT" distribution-build-gopath.XXXXXX)"
		pushd "$GOPATH"

		# This tag also comes from the time when this was called
		# github.com/docker/docker-ce-packaging, so we need to work around this
		# by moving the cli component into the right path...
		git clone \
			--depth=1 --branch=v17.06.2-ce \
			https://github.com/docker/cli.git \
			src/github.com/docker/docker-ce-packaging
		mv \
			src/github.com/docker/docker-ce-packaging/components/cli \
			src/github.com/docker/cli

		pushd src/github.com/docker/cli
		GO111MODULE=off go build -o "$TEST_BINDIR/docker" ./cmd/docker
	)
fi

# Create an unprivilegeduser account for tests.
if ! ( grep unprivilegeduser /etc/passwd &>/dev/null ); then
	useradd --create-home --gid docker unprivilegeduser
fi

# Disable SUSE secrets for tests, as some tests (TestDiff from
# integration/container) will fail if we have secrets injected.
[ -e /etc/docker/suse-secrets-enable ] && \
	mv -nv /etc/docker/suse-secrets-enable{,-DISABLED}
sudo systemctl restart docker

# Make sure docker-buildx is disabled.
[ -e /usr/lib/docker/cli-plugins/docker-buildx ] && \
	mv -nv /usr/lib/docker/cli-plugins/docker-buildx{,-DISABLED}

# Disable any daemon configurations.
[ -e /etc/docker/daemon.json ] && \
	mv -nv /etc/docker/daemon.json{,.DISABLED}

set -x

# In order for< gotest.tools/v3/assert> to parse the source and give us useful
# error messages, we have to create a fake source directory that points at
# $TEST_SRCDIR. This path is replaced with %{docker_builddir} during the
# docker.spec build.
__DOCKER_BUILDIR="@@docker_builddir@@"
DOCKER_BUILDDIR="${DOCKER_BUILDDIR:-$__DOCKER_BUILDIR}"
sudo rm -rvf "$DOCKER_BUILDDIR"
sudo mkdir -p "$(dirname "$DOCKER_BUILDDIR")"
sudo ln -svf "$TEST_SRCDIR" "$DOCKER_BUILDDIR"

# Clean up any old containers/images/networks/volumes before running the tests.
# We need to do this *BEFORE* we set PATH, as the outdated $TEST_BINDIR/docker
# doesn't support some of these commands.
docker container prune -f
docker image prune -af
#docker buildx prune -af
docker network prune -f
docker volume prune -af
[ -z "$(docker plugin ls -q)" ] || docker plugin ls -q | xargs docker plugin rm -f
docker system prune -af

export DOCKERFILE="$TEST_SRCDIR/Dockerfile"
export TMPDIR="$TMPDIR"
export TEMP="$TMPDIR"
export HOME="$TMPDIR/fake-home"
export DEST="$TEST_SRCDIR/bundles"
export ABS_DEST="$DEST"
export PATH="$TEST_BINDIR:$PATH"

export TZ=UTC
export DOCKER_INTEGRATION_DAEMON_DEST="$ABS_DEST"
export DOCKER_HOST=unix:///run/docker.sock
export DOCKER_GRAPHDRIVER=overlay2
export DOCKER_USERLANDPROXY=true
export DOCKER_REMAP_ROOT="${DOCKER_REMAP_ROOT:-}"
export DOCKER_TMPDIR="$TMPDIR"
export DOCKER_SUSE_SECRETS_ENABLE=0

set +x

# Make sure that we have a dummy "destination" directory for tests.
rm -rf "$DOCKER_INTEGRATION_DAEMON_DEST"
mkdir -p "$DOCKER_INTEGRATION_DAEMON_DEST"

# Install the emptyfs images.
sh ./hack/make/.build-empty-images

ls -la "$TMPROOT"

success=0
failed_suites=()
for suite_name in "${SUITES[@]}"; do
	suite_name="${suite_name#*./}"
	pushd "$TEST_SRCDIR/$suite_name"

	test_flags=()
	[ -n "$verbose" ] && test_flags+=("-test.v")
	[ -n "$filter" ] && test_flags+=("-test.run" "$filter")

	if [[ "$suite_name" == "integration-cli" ]]; then
		# We need to disable docker-buildx for the integration-cli tests
		# because otherwise the "docker build" command will use the wrong
		# builder and the output won't match what the tests expect.
		timeout=360m
	fi
	test_flags+=("-test.timeout" "$timeout")

	echo "Running suite $suite_name (${test_flags[@]}) [success=$success fail=${#failed_suites[@]}]"

	set -x +e
	sudo -E HOME="$HOME" TMPDIR="$TMPDIR" PATH="$PATH" \
		./test.main "${test_flags[@]}"
	err="$?"
	if (( $err != 0 )); then
		[ -z "$fail_fast" ] || exit "$err"
		failed_suites+=("$suite_name")
	else
		(( success++ ))
	fi
	set +x -e

	popd
done

[ -e /usr/lib/docker/cli-plugins/docker-buildx-DISABLED ] && \
	mv -nv /usr/lib/docker/cli-plugins/docker-buildx{-DISABLED,}

[ -e /etc/docker/suse-secrets-enable-DISABLED ] && \
	mv -nv /etc/docker/suse-secrets-enable{-DISABLED,}

[ -e /etc/docker/daemon.json.DISABLED ] && \
	mv -nv /etc/docker/daemon.json{.DISABLED,}

echo "Suite results: $success success(es) ${#failed_suites[@]} failure(s)."
if (( ${#failed_suites[@]} > 0 )); then
	echo "Failed suites:"
	printf " - %s\n" "${failed_suites[@]}"
	exit 1
fi
