#!/usr/bin/bash
#
# Script to update etcd configuration
# Intended to be run after updating sources
# Author: Elisei Roca
#------------------------------------------

set -euo pipefail
#set -x

DRY_RUN=0
REBUILD_IMAGE=0
NEW_CONF=".update-etcd-conf.new"
RPM_CACHE=".update-etcd-conf-latest.rpm"


while [ "$#" -gt 0 ]; do
  case $1 in
    --clean|-c)
      echo "Clean $NEW_CONF and $RPM_CACHE"
      rm -f "$NEW_CONF" "$RPM_CACHE"
      exit 0
      ;;
    --dry-run|-d)
      DRY_RUN=1
      ;;
    --rebuild|-r)
      REBUILD_IMAGE=1
      ;;
    --help|-h)
      echo "Usage: $0 [--clean|-c] [--dry-run|-d] [--rebuild|-r]"
      echo "  --clean,     -c : remove $NEW_CONF and $RPM_CACHE"
      echo "  --dry-run,   -d : create '$NEW_CONF' instead of updating etcd.conf"
      echo "  --rebuild,   -r : rebuild the RPM and container image"
      exit 0
      ;;
    *)
      echo "Unknown argument: $1" >&2
      exit 1
      ;;
  esac
  shift
done

BODY_TMP=$(mktemp "./.etcd-conf-update.body.XXXXXX")
HELP_TMP=$(mktemp "./.etcd-conf-update.help.XXXXXX")
OSC_LOG=$(mktemp "./.etcd-conf-update.osc.XXXXXX")
TEMP_FILES="$HELP_TMP $BODY_TMP $OSC_LOG"
cleanup() {
  rm -f $TEMP_FILES
}
trap cleanup EXIT

if [ "$REBUILD_IMAGE" -eq 1 ] || [ ! -f "$RPM_CACHE" ]; then
  rm -f "$RPM_CACHE"
  echo 'osc build --local-package --no-service'
  osc build --local-package --no-service --clean | tee "$OSC_LOG"
  RPM_PATH=$(tail -n10 "$OSC_LOG" | grep -Eo '/[^ ]*/etcd-[^ ]*\.rpm' | tail -1)
  [ -z "$RPM_PATH" ] || [ ! -f "$RPM_PATH" ] && { echo '| No etcd RPM found after osc build |'; exit 1; }
  cp -v "$RPM_PATH" "$RPM_CACHE"
  echo "Copied newly built RPM to: $RPM_CACHE"
else
  echo "Using cached RPM: $RPM_CACHE"
fi


if [ "$REBUILD_IMAGE" -eq 1 ] || ! podman image exists etcd-oscrpm; then
  podman build . -t etcd-oscrpm -f - <<EOF
FROM registry.opensuse.org/opensuse/tumbleweed:latest
COPY $RPM_CACHE /tmp/etcd.rpm
RUN old /etc/zypp/repos.d/*.repo
RUN zypper -n install --allow-unsigned-rpm /tmp/etcd.rpm
EOF
fi


ETCD_VERSION=$(podman run --rm etcd-oscrpm etcd --version 2>/dev/null | awk '/^etcd Version:/ {print $3}')
[ -z "$ETCD_VERSION" ] && { echo "Failed to extract etcd version from container"; exit 1; }
echo "Version: $ETCD_VERSION"

if ! podman run --rm etcd-oscrpm etcd --help > "$HELP_TMP" 2>/dev/null; then
  echo "Error: Failed to run etcd --help in container" >&2
  exit 1
fi
[ -s "$HELP_TMP" ] || { echo "Error: etcd --help output is empty" >&2; exit 1; }


HEADER_CONTENT='# Please also read README.security for this package.

# Environment variables: every flag has a corresponding environment variable that has the
# same name but is prefixed with ETCD_ and formatted in all caps and snake case.
# For example, --some-flag would be ETCD_SOME_FLAG.

# Caution: If you mix-and-match configuration options, then the following rules apply.
# * Command-line flags take precedence over environment variables.
# * If you provide a configuration file all command-line flags and environment variables are ignored.

# Set commandline options example: ETCD_OPTIONS="--feature-gates=StopGRPCServiceOnDefrag=true"
# ETCD_OPTIONS=""'


awk '
  /^[[:space:]]*--[A-Za-z0-9-]+/ {
    match($0, "^[[:space:]]*--([A-Za-z0-9-]+)([[:space:]]+\x27([^\x27]*)\x27|[[:space:]]+([^[:space:]]+))?", arr)
    var = arr[1]
    gsub("-", "_", var)
    var = toupper(var)
    if (arr[3] != "") val = arr[3]
    else if (arr[4] != "") val = arr[4]
    else val = ""
    print "# ETCD_" var "=\"" val "\""
    next
  }
  /^[[:space:]]*$/ { print ""; next }
  { sub(/^[[:space:]]*/, "", $0); print "# " $0 }
' "$HELP_TMP" > "$BODY_TMP"

echo "$HEADER_CONTENT" > "$NEW_CONF"
cat "$BODY_TMP" >> "$NEW_CONF"


# Uncomment default configuration options
for line in ETCD_NAME ETCD_DATA_DIR ETCD_LISTEN_CLIENT_URLS ETCD_ADVERTISE_CLIENT_URLS; do
  sed -i "/# $line=/s/^# //" "$NEW_CONF"
done


# Modify ETCD_DATA_DIR to default value
sed -i 's|^ETCD_DATA_DIR=.*$|ETCD_DATA_DIR="/var/lib/etcd/default.etcd"|' "$NEW_CONF"


if [ "$DRY_RUN" -eq 0 ]; then
  mv "$NEW_CONF" etcd.conf
  echo "Updated etcd.conf"
else
  echo "Dry run: created $NEW_CONF"
fi
