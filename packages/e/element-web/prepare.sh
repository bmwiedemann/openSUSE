#!/bin/bash 

set -ex

oldwd="$(pwd)"

# cleanup old stuff
find -maxdepth 1 -type d -name 'element-web-*' | xargs rm -r

version=$(grep "Version:" element-web.spec | awk '{print $2}')
last_packaged_version=$(osc cat devel:languages:nodejs/element-web/element-web.spec | grep "^Version:" | awk '{print $NF}')

osc rm --force element-web-*.tar.gz || :
wget -c https://github.com/vector-im/element-web/archive/v${version}.tar.gz -O element-web-${version}.tar.gz
wget https://meet.element.io/libs/external_api.min.js -O jitsi_external_api.min.js
osc add element-web-*.tar.gz

#zypper install yarn cargo gcc-c++ sqlcipher-devel libsecret-devel

rm -rf "element-web-${version}"
tar xzvf element-web-${version}.tar.gz
cd element-web-${version}
changes=$(grep "^Changes in \[$last_packaged_version\]" -B10000 CHANGELOG.md |  head -n -2 | sed -e '/^==*$/d' -e 's/Changes in \[\([^\[]*\)\].*/- Version \1/' -e 's/Changes in \[\([^\[]*\)\].*/- Version \1/' -e 's/^\([^-].*\)$/  \1/')

echo 'yarn-offline-mirror "./npm-packages-offline-cache"' > .yarnrc
yarn cache clean
rm -rf node_modules/
yarn install --pure-lockfile --ignore-engines || : # this will download tha packages into the offline cache

# download some additional dependencie that slips through this earlier method
cd ./npm-packages-offline-cache/

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
echo -e "\n\nDONE creating npm dependency offline cache file 'npm-packages-offline-cache.tar.gz'"

read -p "Write changes?"
osc vc -m "${changes}" element-web.changes
