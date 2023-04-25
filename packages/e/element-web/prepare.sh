#!/bin/bash

set -ex

oldwd="$(pwd)"
tmpdir="$(mktemp -d)"

version=$(grep "Version:" element-web.spec | awk '{print $2}')
osc rm --force element-web-*.tar.gz || :
wget -c https://github.com/vector-im/element-web/archive/v${version}.tar.gz -O element-web-${version}.tar.gz
wget https://meet.element.io/libs/external_api.min.js -O jitsi_external_api.min.js
osc add element-web-*.tar.gz

#zypper install yarn cargo gcc-c++ sqlcipher-devel libsecret-devel


rm -rf "element-web-${version}"
wget -c https://github.com/vector-im/element-web/archive/v${version}.tar.gz -O element-web-${version}.tar.gz
tar xzvf element-web-${version}.tar.gz
cd element-web-${version}

changes=$(grep "^=============" -B10000 -m2 CHANGELOG.md | head -n -3 | tail -n +4)

echo 'yarn-offline-mirror "./npm-packages-offline-cache"' > .yarnrc
yarn cache clean
rm -rf node_modules/
yarn install --pure-lockfile --ignore-engines || : # this will download tha packages into the offline cache

# download some additional dependencie that slips through this earlier method
cd ./npm-packages-offline-cache/
#wget -O matrix-analytics-events-0.0.1.tgz $(grep -m1 -A2 "@matrix.org/analytics-events" ../yarn.lock | grep resolved | awk '{print $NF}' | tr -d '"')
#mkdir package
#tar xvf matrix-analytics-events-0.0.1.tgz --strip-components=1 -C package/
#tar czf matrix-analytics-events-0.0.1.tgz package/
#rm -r package

# fill sentry-cli cache with mock binaries for all architecutres
cd sentry-cli
sentry_cli_version=$(ls ../@sentry-cli-*.tgz | sed -e 's/.*cli-//' -e 's/.tgz//')
for arch in i686 x86_64 aarch64 armv7 riscv64 ppc64 ppc64le s390x; do
	url="https://downloads.sentry-cdn.com/sentry-cli/${sentry_cli_version}/sentry-cli-Linux-${arch}"
	filehash=$(echo -n "$url" | md5sum | cut -c1-6)
	target="${filehash}-sentry-cli-Linux-${arch/_/-}"
	#wget -O "$target" "$url"
	echo '#!/bin/bash' > "$target"
	echo '' >> "$target"
	echo "echo ${sentry_cli_version}" >> "$target"
	chmod +x "$target"
done
cd ..


cd ..

tar czf npm-packages-offline-cache.tar.gz ./npm-packages-offline-cache
cp npm-packages-offline-cache.tar.gz "$oldwd/"
cd "$oldwd"
echo rm -rf "$tmpdir"
echo -e "\n\nDONE creating npm dependency offline cache file 'npm-packages-offline-cache.tar.gz'"


read -p "Write changes?"
osc vc -m "Version ${version}\n${changes}" element-web.changes

#DIST_VERSION=$version ./scripts/package.sh
#
#cp "dist/element-${version}.tar.gz" "$oldwd/"
#cd "$oldwd"
#rm -rf "$tmpdir"
#echo -e "\n\nDONE creating output file 'element-${version}.tar.gz'"
