#!/usr/bin/sh

set -euo pipefail

if [[ -z "${1:-}" ]]; then
  echo "Usage: $0 <version>"
  exit 1
fi

REPO_DIR="HeroicGamesLauncher"
VERSION="$1"

echo "++++++++++++++++++++++++++++++++++++++++++++++"
echo "patching service file and downloading sources"
echo "++++++++++++++++++++++++++++++++++++++++++++++"

sed -i -E 's|(<param name="revision">).*?(</param>)|\1v'"${VERSION}"'\2|' _service
osc service mr obs_scm
osc service mr set_version

if [ -f "pnpm-offline-store.tar.gz" ]; then rm pnpm-offline-store.tar.gz; fi

echo "+++++++++++++++++++++++++++++++++++++++++++++++++++"
echo "Config package.json to force download dependencies"
echo "+++++++++++++++++++++++++++++++++++++++++++++++++++"

cd "$REPO_DIR"

# Forcing the download of required npm dependencies
ESBUILD_VERSION="0.25.12"
SWC_VERSION="1.11.24"

jq --indent 2 \
  --arg swc_ver "$SWC_VERSION" \
'
.
| del(.packageManager)
| del(.build.shrinkwrapIgnoreDev)

| .dependencies["ajv"] = "^8.17.1"
| .dependencies["ajv-formats"] = "^2.1.1"
| .dependencies["builder-util-runtime"] = "^9.2.4"

| .dependencies = (.dependencies // {})
| .devDependencies = (.devDependencies // {})
| .optionalDependencies = (.optionalDependencies // {})

| .scripts.build = "electron-vite build"

| .scripts["dist:linux"] = "pnpm run build && electron-builder --linux --dir -c.electronDist=/usr/lib64/electron/ -c.electronVersion=$(cat /usr/lib64/electron/version)"

| .build.executableName = "heroic"

| .build.npmRebuild = false
| .build.nodeGypRebuild = false
| .build.asarUnpack = ["build/bin/**/*"]

| .build.files = [
    "build/**/*",
    "dist/**/*",
    "node_modules/**/*",
    "!**/*.map"
  ]

# ==========================================================
# Use system electron only
# Keep upstream ecosystem intact
# ==========================================================
| .devDependencies.electron = "^41.1.1"

| .devDependencies["electron-builder"] = "^26.8.2"

# ==========================================================
# Multi-arch esbuild support
# DO NOT REMOVE esbuild
# This is what fixes aarch64
# ==========================================================
| .optionalDependencies["@esbuild/linux-x64"] = "0.25.12"
| .optionalDependencies["@esbuild/linux-arm64"] = "0.25.12"

# ==========================================================
# Multi-arch rollup native binaries
# ==========================================================
| .optionalDependencies["@rollup/rollup-linux-x64-gnu"] = "4.52.5"
| .optionalDependencies["@rollup/rollup-linux-arm64-gnu"] = "4.52.5"

# ==========================================================
# Multi-arch swc native binaries
# ==========================================================
| .optionalDependencies["@swc/core-linux-x64-gnu"] = "1.11.24"
| .optionalDependencies["@swc/core-linux-arm64-gnu"] = "1.11.24"

# ==========================================================
# Security / compatibility overrides
# ==========================================================
| .overrides = (
    (.overrides // {})
    + {
        "undici": "7.24.7",
        "undici-types": "7.24.7",
        "@tootallnate/once": "3.0.1",
        "simple-git": "3.32.3",
        "fast-xml-parser": "5.5.7",
        "@xmldom/xmldom": "0.8.12",
        "find-up": "5.0.0",
        "shell-quote": "1.9.0",
        "ws@^7.0.0": "7.5.11",
        "ws@^8.0.0": "8.21.0"
      }
  )
' package.json > temp.json && mv temp.json package.json

echo "++++++++++++++++++++++++++++++++++++++++++++++"
echo "Cleanup Step"
echo "++++++++++++++++++++++++++++++++++++++++++++++"

rm -rf node_modules .pnpm-store package-lock.json
mkdir .pnpm-store

echo "++++++++++++++++++++++++++++++++++++++++++++++"
echo "Downloading pnpm modules and packing all"
echo "++++++++++++++++++++++++++++++++++++++++++++++"

pnpm config set store-dir .pnpm-store
pnpm install --ignore-scripts --no-frozen-lockfile

tar cJf ../pnpm-offline-store.tar.gz .pnpm-store node_modules package.json pnpm-lock.yaml

echo "++++++++++++++++++++++++++++++++++++++++++++++"
echo "Done! Have fun building and testing"
echo "++++++++++++++++++++++++++++++++++++++++++++++"
