#!/bin/bash

set -ex

oldwd="$(pwd)"
tmpdir="$(mktemp -d)"

#zypper install yarn cargo gcc-c++ sqlcipher-devel libsecret-devel

version=$(grep "Version:" element-desktop.spec | awk '{print $2}')
osc rm -f element-web-*.tar.gz
osc rm -f element-desktop-*.tar.gz
wget -c https://github.com/vector-im/element-desktop/archive/v${version}.tar.gz -O element-desktop-${version}.tar.gz
wget -c https://github.com/vector-im/element-web/archive/v${version}.tar.gz -O element-web-${version}.tar.gz
osc add -f element-web-*.tar.gz
osc add -f element-desktop-*.tar.gz
cp element-desktop.spec "$tmpdir/"
cd "$tmpdir"

rm -rf "element-desktop-${version}"
wget -c https://github.com/vector-im/element-desktop/archive/v${version}.tar.gz -O element-desktop-${version}.tar.gz
tar xzvf element-desktop-${version}.tar.gz
cd element-desktop-${version}

changes=$(grep "^=============" -B10000 -m2 CHANGELOG.md | head -n -3 | tail -n +4)

echo 'yarn-offline-mirror "./npm-packages-offline-cache"' > .yarnrc
yarn cache clean
rm -rf node_modules/
yarn install --pure-lockfile || : # this will download tha packages into the offline cache

export PATH="$PATH:node_modules/.bin"
yarn run hak check
yarn run hak fetch

# prefetch cargo crates
pushd .hak/matrix-seshat/x86_64-unknown-linux-gnu/build
cargo vendor
mkdir -p .cargo
cat > .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF
popd

patch -p0 <<EOF
--- .hak/keytar/x86_64-unknown-linux-gnu/build/node_modules/node-gyp/gyp/pylib/gyp/input.py	2023-06-15 12:09:05.127000000 +0200
+++ .hak/keytar/x86_64-unknown-linux-gnu/build/node_modules/node-gyp/gyp/pylib/gyp/input.py	2023-06-15 13:34:18.969088855 +0200
@@ -1190,7 +1190,7 @@
         else:
             ast_code = compile(cond_expr_expanded, "<string>", "eval")
             cached_conditions_asts[cond_expr_expanded] = ast_code
-        env = {"__builtins__": {}, "v": StrictVersion}
+        env = {"__builtins__": {"openssl_fips": ""}, "v": StrictVersion}
         if eval(ast_code, env, variables):
             return true_dict
         return false_dict
EOF

tar czf npm-packages-offline-cache.tar.gz ./npm-packages-offline-cache
tar czf hak.tar.gz ./.hak
cp -v npm-packages-offline-cache.tar.gz hak.tar.gz "$oldwd/"

cd "$oldwd"
echo rm -rf "$tmpdir"
echo -e "\n\nDONE creating npm dependency offline cache file 'npm-packages-offline-cache.tar.gz'"


read -p "Write changes?"
osc vc -m "Version ${version}\n${changes}" element-desktop.changes
