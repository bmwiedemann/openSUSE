#!/bin/sh
set -eu
tmpdir=$(mktemp -d)
trap 'rm -rf ${tmpdir}' EXIT

sourcedir="$(realpath "$(dirname "$0")")"
script="${sourcedir}/kiwi_metainfo_helper"

cd "$tmpdir"

# Setup environment

mkdir -p "${tmpdir}/repos/"
cp "${sourcedir}/sles-release-15.4-150400.32.2.x86_64.rpm" "${tmpdir}/repos/"

# Mock "date"
export PATH="${tmpdir}:$PATH"
cat >"${tmpdir}/date" <<'EOF'
#!/bin/sh
exec /usr/bin/date -d "2018-10-30T09:19:02.074934628Z" "$@"
EOF
chmod a+x "${tmpdir}/date"

cat >.data <<EOF
DISTURL="obs://build.opensuse.org/openSUSE:Factory/images/0f40c57dd619e1dff9e512949b6bca09-opensuse-tumbleweed-image:docker"
RELEASE=4.2
RECIPEFILE=_service:foobar:Dockerfile
BUILD_ARCH=aarch64:aarch64_ilp32:armv8l
EOF
export BUILD_DIST=.dist

cat >Dockerfile <<EOF
DISTURL=%DISTURL%
SOURCEURL=%SOURCEURL%
RELEASE=%RELEASE%
BUILDTIME=%BUILDTIME%
ARCH=%ARCH%
OS_VERSION=%OS_VERSION%
OS_VERSION_NO_DASH=%OS_VERSION_NO_DASH%
OS_VERSION_ID=%OS_VERSION_ID%
OS_VERSION_ID_SP=%OS_VERSION_ID_SP%
OS_PRETTY_NAME=%OS_PRETTY_NAME%
OS_VENDOR=%OS_VENDOR%
OS_PRETTY_NAME_DASHED=%OS_PRETTY_NAME_DASHED%
OS_PRETTY_NAME_BEFORE_PAREN=%OS_PRETTY_NAME_BEFORE_PAREN%
OS_PRETTY_NAME_BEFORE_PAREN_DASHED=%OS_PRETTY_NAME_BEFORE_PAREN_DASHED%
EOF

bash "${script}"

diff -u Dockerfile - <<EOF
DISTURL=obs://build.opensuse.org/openSUSE:Factory/images/0f40c57dd619e1dff9e512949b6bca09-opensuse-tumbleweed-image:docker
SOURCEURL=https://build.opensuse.org/package/show/openSUSE:Factory/opensuse-tumbleweed-image?rev=0f40c57dd619e1dff9e512949b6bca09
RELEASE=4.2
BUILDTIME=2018-10-30T09:19:02.074934628Z
ARCH=aarch64
OS_VERSION=15-SP4
OS_VERSION_NO_DASH=15 SP4
OS_VERSION_ID=15.4
OS_VERSION_ID_SP=15.4
OS_PRETTY_NAME=SUSE Linux Enterprise Server 15 SP4
OS_VENDOR=SUSE
OS_PRETTY_NAME_DASHED=SUSE-Linux-Enterprise-Server-15-SP4
OS_PRETTY_NAME_BEFORE_PAREN=SUSE Linux Enterprise Server 15 SP4
OS_PRETTY_NAME_BEFORE_PAREN_DASHED=SUSE-Linux-Enterprise-Server-15-SP4
EOF

# Now with a build.suse.de DISTURL
cat >.data <<EOF
DISTURL="obs://build.suse.de/SUSE:SLE-15-SP3:Update:CR/images/5f0a221b7877396cbf977205e64690d2-sles15-image"
RELEASE=4.2
RECIPEFILE=_service:foobar:Dockerfile
BUILD_ARCH=aarch64:aarch64_ilp32:armv8l
EOF

cat >Dockerfile <<EOF
DISTURL=%DISTURL%
SOURCEURL=%SOURCEURL%
EOF

bash "${script}"

diff -u Dockerfile - <<EOF
DISTURL=obs://build.suse.de/SUSE:SLE-15-SP3:Update:CR/images/5f0a221b7877396cbf977205e64690d2-sles15-image
SOURCEURL=https://sources.suse.com/SUSE:SLE-15-SP3:Update:CR/sles15-image/5f0a221b7877396cbf977205e64690d2/
EOF

# Test _multibuild
cat >.data <<EOF
DISTURL="obs://build.opensuse.org/openSUSE:Factory/images/0f40c57dd619e1dff9e512949b6bca09-opensuse-tumbleweed-image:docker"
RELEASE=4.2
RELEASE=4.2
RECIPEFILE=_service:foobar:Dockerfile.FLAVOR
BUILD_ARCH=aarch64:aarch64_ilp32:armv8l
EOF
export BUILD_DIST=.dist

cat >Dockerfile.FLAVOR <<EOF
RELEASE=%RELEASE%
EOF

bash "${script}"

diff -u Dockerfile.FLAVOR - <<EOF
RELEASE=4.2
EOF

# Test _multibuild when not a Dockerfile
cat >.data <<EOF
DISTURL="obs://build.opensuse.org/openSUSE:Factory/images/0f40c57dd619e1dff9e512949b6bca09-opensuse-tumbleweed-image:docker"
RELEASE=4.2
RELEASE=4.2
RECIPEFILE=_service:foobar:NotADockerfile
BUILD_ARCH=aarch64:aarch64_ilp32:armv8l
EOF
export BUILD_DIST=.dist

cat >NotADockerfile <<EOF
RELEASE=%RELEASE%
EOF

bash "${script}"

diff -u NotADockerfile - <<EOF
RELEASE=%RELEASE%
EOF

# Now test without build data (osc chroot build) and that without %OS_*% it doesn't need a release RPM
rm -r ./.data ./repos/

cat >Dockerfile <<EOF
DISTURL=%DISTURL%
SOURCEURL=%SOURCEURL%
RELEASE=%RELEASE%
BUILDTIME=%BUILDTIME%
ARCH=%ARCH%
EOF

bash "${script}"

diff -u Dockerfile - <<EOF
DISTURL=local
SOURCEURL=https://local/package/show/local/local?rev=local
RELEASE=0
BUILDTIME=2018-10-30T09:19:02.074934628Z
ARCH=noarch
EOF

# test base container annotations
cat >Dockerfile - <<EOF
BASE_REFNAME=%BASE_REFNAME%
BASE_DIGEST=%BASE_DIGEST%
EOF

mkdir -p containers
cat >containers/annotation - <<EOF
<annotation>
  <repo url="obsrepositories:/"/>
  <binaryid>491e4873e01f1a58464ea33970a08a3219062ec1bb9a4c5a1bd014d0d596beab</binaryid>
  <registry_refname>registry.suse.com/bci/bci-base:15.6</registry_refname>
  <registry_digest>sha256:cee5bd9e5a186dc1cca01e523f588f4c19c6c45abaa47139f7c021c289cb4c04</registry_digest>
  <registry_fatdigest>sha256:887c83266ee8ae4a83c215974a814abbb2007f0a445a67fac7079e922e846133</registry_fatdigest>
  <version>cee5bd9e5a186dc1cca01e523f588f4c19c6c45abaa47139f7c021c289cb4c04</version>
  <release>0</release>
  <binaryarch>noarch</binaryarch>
  <hdrmd5>05cb99d4617ee49ed6419f72cc8fcf6e</hdrmd5>
</annotation>
EOF

bash "${script}"

diff -u Dockerfile - <<EOF
BASE_REFNAME=registry.suse.com/bci/bci-base:15.6
BASE_DIGEST=sha256:cee5bd9e5a186dc1cca01e523f588f4c19c6c45abaa47139f7c021c289cb4c04
EOF
rm -r containers/annotation

# test processing .kiwi and config.sh in Kiwi builds
cat >.data <<EOF
RELEASE=42
DISTURL="obs://build.opensuse.org/openSUSE:Factory/test/0f40c57dd619e1dff9e512949b6bca09-test"
RECIPEFILE=_service:foobar:test.kiwi
BUILD_ARCH=aarch64:aarch64_ilp32:armv8l
EOF
export BUILD_DIST=.dist

cat >test.kiwi - <<EOF
<?xml version="1.0" encoding="utf-8"?>
<image schemaversion="8.0" name="test" displayname="Test (Build %RELEASE%)">
</image>
EOF

cat >config.sh - <<EOF
echo "Build: %RELEASE%" > /var/log/build
EOF

bash "${script}"

diff -u test.kiwi - <<EOF
<?xml version="1.0" encoding="utf-8"?>
<image schemaversion="8.0" name="test" displayname="Test (Build 42)">
</image>
EOF

diff -u config.sh - <<EOF
echo "Build: 42" > /var/log/build
EOF

rm test.kiwi config.sh
