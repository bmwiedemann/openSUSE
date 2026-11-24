#!/bin/sh
#
# Regenerate node_modules.tar.gz, the archive of npm tarballs that the spec
# unpacks for the UI build.
#
# The node_modules source service (obs-service-node_modules) writes its
# tarballs into a node_modules/ directory. osc cannot commit a directory to a
# Subversion based package: "osc addremove" skips directories and "osc add"
# only offers to pack one into a .obscpio container. So the directory is
# packed here as an ordinary tar source instead.
#
# The service downloads every platform build of every optional dependency -
# 333 MiB of darwin, win32, musl and riscv64 binaries for esbuild, rolldown,
# tailwindcss and lightningcss, although the package builds for x86_64 and
# aarch64 only. The entries are dropped here before packing, using the os, cpu
# and libc fields that package-lock.json carries for them; npm treats those
# dependencies as optional, so a build root without them installs fine.
#
# On a version bump, refresh the input first:
#
#   tar -xOf llama-swap-<VERSION>.tar.gz \
#       llama-swap-<VERSION>/ui/package-lock.json > ui-package-lock.json
#   osc service manualrun go_modules   # regenerates vendor.tar.gz
#   ./update-npm-deps.sh -f
#
# usage: ./update-npm-deps.sh [-f]     -f re-downloads, even if node_modules/
#                                          is there already
#
set -eu

cd "$(dirname "$0")"

if [ ! -d node_modules ] || [ "${1:-}" = "-f" ]; then
    rm -rf node_modules
    osc service manualrun node_modules
fi

python3 - <<'PY'
import json, os, sys

LOCKFILE = "ui-package-lock.json"
# the architectures ExclusiveArch allows, and the C library they use
OS, CPU, LIBC = {"linux"}, {"x64", "arm64"}, {"glibc"}

def tarball_name(package, version):
    name = package.split("node_modules/")[-1].replace("/", "-")
    return f"{name}-{version}.tgz"

def keep(entry):
    for key, allowed in (("os", OS), ("cpu", CPU), ("libc", LIBC)):
        if values := entry.get(key):
            if not set(values) & allowed:
                return False
    return True

lock = json.load(open(LOCKFILE))
os.chdir("node_modules")

dropped = []
for package, entry in lock["packages"].items():
    if not package or not entry.get("resolved", "").startswith("http"):
        continue
    if not keep(entry):
        dropped.append(tarball_name(package, entry["version"]))

missing = [name for name in dropped if not os.path.exists(name)]
if missing:
    # a lockfile that does not match the downloaded directory: rather fail than
    # ship an archive that is quietly incomplete
    sys.exit(f"{LOCKFILE} does not match node_modules/: no such file "
             f"{missing[0]} (run ./update-npm-deps.sh -f?)")

for name in dropped:
    os.remove(name)
print(f"dropped {len(dropped)} dependencies for other platforms")
PY

tar -czf node_modules.tar.gz node_modules
rm -rf node_modules

# npm tarballs are compressed already, so this is roughly the size of the
# dependencies that remain
printf 'node_modules.tar.gz: %s\n' "$(du -h -d0 node_modules.tar.gz | cut -f1)"
