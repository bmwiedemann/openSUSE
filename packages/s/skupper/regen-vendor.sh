#!/bin/bash
# Regenerate vendor.tar.gz for the skupper OBS package.
#
# Plain `go mod vendor` (what `osc service manualrun go_modules` runs)
# fails on the 2.2.x branch: some tests/integration/kube/controller/*_test.go
# files import internal/fixtures, which exists on main only. So exactly those
# files are moved aside first, then vendored, packed, and moved back. The
# remaining suite_test.go still pulls test-only deps (e.g. envtest) into
# vendor/, which the build does not use but keeps the tree reproducible.
# Everything happens in a throwaway clone, so shipped sources are untouched.
#
# Usage: ./regen-vendor.sh [revision]   # default: 2.2.4 (see _service)
set -euo pipefail

REV="${1:-2.2.4}"
URL="https://github.com/skupperproject/skupper"
# In-module import path whose directory the branch does not ship.
MISSING="internal/fixtures"

WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT

git clone --quiet "$URL" "$WORK/skupper"
git -C "$WORK/skupper" checkout --quiet "$REV"

SRC="$WORK/skupper"
mapfile -t BROKEN < <(grep -rl "$MISSING" --include='*_test.go' "$SRC/tests" || true)
[ "${#BROKEN[@]}" -gt 0 ] || { echo "no test files importing $MISSING, nothing to set aside"; exit 1; }
mkdir "$WORK/aside"
for f in "${BROKEN[@]}"; do
	mv "$f" "$WORK/aside/"
done

(
	cd "$SRC"
	go mod vendor
)
tar -C "$SRC" -czf "$WORK/vendor.tar.gz" vendor
for f in "${BROKEN[@]}"; do
	mv "$WORK/aside/$(basename "$f")" "$f"
done

cp "$WORK/vendor.tar.gz" ./vendor.tar.gz
echo "wrote ./vendor.tar.gz from $URL@$REV"
