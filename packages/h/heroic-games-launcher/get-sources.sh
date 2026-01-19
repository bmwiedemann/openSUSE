#!/usr/bin/sh

set -e

if [[ -z "$1" ]]; then
echo "Please enter the version you want to update to";
exit 1;
fi

REPO_DIR="HeroicGamesLauncher"
VERSION="$1"

echo "++++++++++++++++++++++++++++++++++++++++++++++"
echo "patching service file and downloading sources"
echo "++++++++++++++++++++++++++++++++++++++++++++++"

sed -i -e 's|<param name="revision">refs/tags/v.*|<param name="revision">refs/tags/v'${VERSION}'</param>|g' _service
osc service runall

if [ -f "pnpm-offline-store.tar.gz" ]; then rm pnpm-offline-store.tar.gz; fi

echo "+++++++++++++++++++++++++++++++++++++++++++++++++++"
echo "Config package.json to force download dependencies"
echo "+++++++++++++++++++++++++++++++++++++++++++++++++++"

cd "$REPO_DIR"

# Forcing the download of required npm dependencies
ESBUILD_VERSION="0.25.3"
ROLLUP_VERSION="4.52.5"
SWC_VERSION="1.11.24"
UNDICI_V7_FIXED="7.18.0"

jq --indent 2 \
  --arg esbuild_ver "$ESBUILD_VERSION" \
  --arg rollup_ver "$ROLLUP_VERSION" \
  --arg swc_ver "$SWC_VERSION" \
  --arg undici_v7 "$UNDICI_V7_FIXED" \
'
  .
  | .dependencies += (
      .devDependencies
      | with_entries(select(.key != "electron" and .key != "electron-builder"))
    )

  | .devDependencies = {
      "electron": .devDependencies["electron"],
      "electron-builder": .devDependencies["electron-builder"]
    }

  | .packageManager = "pnpm@>=10.17.1"

  | .scripts.build = "electron-vite build"
  | .scripts["dist:linux"] =
      "pnpm run build && electron-builder --linux --dir -c.electronDist=/usr/lib64/electron/ -c.electronVersion=$(cat /usr/lib64/electron/version)"

  | .build.executableName = "heroic"
  | .build.files = [
      "build/**/*",
      "dist/**/*",
      "node_modules/**/*",
      "!**/*.map",
      "!node_modules/@esbuild/**/*"
    ]

  | .devDependencies |= with_entries(
      select(.key != "electron" and .key != "react-devtools")
    )

  | .peerDependencies.electron = "^25.9.3"

  # ARM64 native binaries
  | .devDependencies |= del(."@esbuild/linux-arm64")
  | .dependencies |= del(
      ."@rollup/rollup-linux-arm64-gnu",
      ."@swc/core-linux-arm64-gnu"
    )

  | .devDependencies["@esbuild/linux-arm64"] = $esbuild_ver
  | .dependencies["@rollup/rollup-linux-arm64-gnu"] = $rollup_ver
  | .dependencies["@swc/core-linux-arm64-gnu"] = $swc_ver

  # === CVE-2026-22036: undici fix (runtime enforced) ===
  | .dependencies = (.dependencies // {})
  | .dependencies.undici = $undici_v7
  | .devDependencies |= del(.undici)

  | .pnpm.overrides = (
      (.pnpm.overrides // {})
      + {
          "undici": $undici_v7,
          "undici-types": "6.21.0"
        }
    )

  # === CVE-2026-22029: react-router / remix-run/router fix ===
  | .pnpm.overrides = (
      (.pnpm.overrides // {})
      + {
          "@remix-run/router": "^1.23.2",
          "react-router": "^7.12.0",
          "react-router-dom": "^7.12.0"
        }
    )
' package.json > package.json.new && mv package.json.new package.json

echo "++++++++++++++++++++++++++++++++++++++++++++++"
echo "Cleanup Step"
echo "++++++++++++++++++++++++++++++++++++++++++++++"

rm -rf node_modules .pnpm-store package-lock.json
mkdir .pnpm-store

echo "++++++++++++++++++++++++++++++++++++++++++++++"
echo "Downloading pnpm modules and packing all"
echo "++++++++++++++++++++++++++++++++++++++++++++++"

pnpm config set store-dir .pnpm-store
pnpm install --lockfile-only --force --ignore-scripts

##npm install --package-lock-only --legacy-peer-deps --strict-peer-dependencies --no-frozen-lockfile  --ignore-scripts
pnpm install --ignore-scripts

tar cJf ../pnpm-offline-store.tar.xz .pnpm-store node_modules package.json pnpm-lock.yaml

echo "++++++++++++++++++++++++++++++++++++++++++++++"
echo "Done! Have fun building and testing"
echo "++++++++++++++++++++++++++++++++++++++++++++++"
