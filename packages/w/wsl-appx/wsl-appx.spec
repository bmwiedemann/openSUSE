#
# spec file for package wsl-appx
#
# Copyright (c) 2021 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#
# needssslcertforbuild


# needsappxsslcertforbuild

Name:           wsl-appx
Version:        1
Release:        0
Summary:        SUSE on Windows application
License:        MIT
Group:          Productivity/Other
URL:            https://gitlab.suse.de/cbosdonnat/wsl-app
Source0:        AppxManifest.xml
Source1:        openSUSE.tar.gz
Source2:        sle.tar.gz
BuildRequires:  WSL-DistroLauncher
BuildRequires:  WSL-DistroLauncher-debug
BuildRequires:  fb-util-for-appx
BuildRequires:  mingw64-filesystem
%if 0%{?is_opensuse}
BuildRequires:  openSUSE-release
%else
BuildRequires:  sles-release
%endif
BuildRequires:  openssl(cli)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Windows Store application providing SLES or openSUSE.

%prep
%setup -Tc -a1 -a2
%if 0%{?is_opensuse}
ln -s openSUSE files
%else
ln -s sle files
%endif

os_release_file="/usr/lib/os-release"
if [ -e "/etc/os-release" ]; then
	os_release_file="/etc/os-release"
fi

# This is dirty. The CN of the AppxManifest needs to match the
# signing certificate's CN. In OBS the CN is the project name. The
# project itself may not have a cert so we can't use %_project. So
# we abuse %vendor which is the project with the key.
#PROJECT="%vendor"
#PROJECT="${PROJECT##*/}"
#OBS="%vendor"
#OBS="${OBS#*//}"
#OBS="${OBS%/*}"
#PUBLISHER="E=$PROJECT@$OBS, CN=$PROJECT OBS Project"
if [ -e "%{_sourcedir}/_projectcert.crt" ]; then
	# mangle value so Windows accepts it
	PUBLISHER=`openssl x509 -subject -in "%{_sourcedir}/_projectcert.crt" -noout -nameopt RFC2253 |sed -e 's/^subject=//;s/emailAddress/E/g;s/,/, /g'`
else
	PUBLISHER="nobody"
fi

# Evaluate os-release file as bash variable assignments
source "$os_release_file"

# PRETTY_NAME on SLE frequently has release label in parentheses as suffix.
# The Microsoft Store rejects this spelling for not matching the display name.
# Trim PRETTY_NAME from space, open paren to end of string:
# SUSE Linux Enterprise Server 15 SP3 (Snapshot 16) -> SUSE Linux Enterprise Server 15 SP3
PRETTY_NAME="${PRETTY_NAME// (*/}"
APPID="${PRETTY_NAME//[^[:alnum:]]/}"
IDENTITYAPPID="${PRETTY_NAME//[^[:alnum:]\.]/}"
LAUNCHERNAME="${PRETTY_NAME//[^[:alnum:].]/-}.exe"

# FIX bsc#1179874 Error in parsing the WSL appx package
# PRETTY_NAME in SLES development snapshots can exceed 40 characters allowed in ShortName appx schema field
# Define SHORT_NAME as first 35 characters of PRETTY_NAME and use in AppManifest.xml template
# Length 35 discards development snapshot/beta/rc qualifier cleanly:
# 'SUSE Linux Enterprise Server 15 SP3 (Snapshot11)' -> 'SUSE Linux Enterprise Server 15 SP3'
SHORT_NAME="${PRETTY_NAME::35}"

# RELEASE is used for digits of the appx version submitted to the MS Store.
# To remove the circular dependency on kiwi opensuse-wsl-image or suse-wsl-image,
# set RELEASE here to be an easily matched string of integer digits.
# Substitute these digits with an actual release number during kiwi
# image build using OBS source services.
RELEASE="0.0"
ARCH="%_arch"
case "$ARCH" in
	x86_64) ARCH="x64" ;;
	aarch64) ARCH="arm64" ;;
esac
# This has to be "SUSE" right now as per requirements from the
# way the store is set up
PUBLISHER_DISPLAY_NAME="SUSE"
# an appx version needs to match this pattern:
# '(0|[1-9][0-9]{0,3}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])(\.(0|[1-9][0-9]{0,3}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])){3}'
# found in the error log if you don't set the proper version.
# for actual store submission there are more rules:
# https://docs.microsoft.com/en-us/windows/uwp/publish/package-version-numbering
# So we need to mangle the versions in a creative way
# Summarized, the digits of the four segments are limited to the following ranges:
# 0-65535, 0-65535, 0-65535, 0
# Where the fourth segment is reserved for the MS Store use.
if [ "$ID" = "opensuse-tumbleweed" ]; then
	# Concatenate VERSION_ID year and day to consume only one segment 0-65535 e.g. 20210524 -> 21144
	# Retain RELEASE version number in the two remaining segments 0-65535.0-65535
	# Example: VERSION_ID="20210524" date --date=$VERSION_ID +"%y%j" -> 21144
	VERSION=`printf "%d.%d.%d.0" "$(date --date=$VERSION_ID +"%y%j")" "${RELEASE%.*}" "${RELEASE#*.}"`
else
	RELEASE="${RELEASE/lp???./}"
	# Concatenate digits of VERSION_ID to consume only one segment 0-65535 e.g. 15.3 -> 153
	# Retain RELEASE version number in the two remaining segments 0-65535.0-65535
	VERSION=`printf "%d.%d.%d.0" "${VERSION_ID//\./}" "${RELEASE%.*}" "${RELEASE#*.}"`
fi

for i in PRETTY_NAME APPID IDENTITYAPPID ARCH PUBLISHER PUBLISHER_DISPLAY_NAME VERSION LAUNCHERNAME SHORT_NAME; do
	eval echo "\"$i='\$$i'\""
done > .settings

cd files
sed -e "s/@PRETTY_NAME@/${PRETTY_NAME}/g;s/@APPID@/$APPID/g;s/@IDENTITYAPPID@/$IDENTITYAPPID/g;s/@PUBLISHER@/$PUBLISHER/g;s/@PUBLISHER_DISPLAY_NAME@/$PUBLISHER_DISPLAY_NAME/g;s/@VERSION@/${VERSION}/g;s/@LAUNCHERNAME@/$LAUNCHERNAME/g;s/@SHORT_NAME@/$SHORT_NAME/g;s/@ARCH@/$ARCH/g" \
	< %{SOURCE0} > AppxManifest.xml
cat AppxManifest.xml

# Get the binary
cp %{_mingw64_bindir}/DistroLauncher.exe "$LAUNCHERNAME"

# TODO So far .pri files are generated by VS and added to the source
# it would be way better to have them generated here with an opensource tool

%build

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/{Assets,images}

# Be explicit about what is copied to metadata and where
# Errors about missing contents are useful for debugging
install -D -m 0644 files/Assets/*.png $RPM_BUILD_ROOT%{_datadir}/%{name}/Assets/
install -D -m 0644 files/images/*.ico $RPM_BUILD_ROOT%{_datadir}/%{name}/images/
install -D -m 0644 files/*.pri $RPM_BUILD_ROOT%{_datadir}/%{name}
install -D -m 0644 files/*.xml $RPM_BUILD_ROOT%{_datadir}/%{name}
install -D -m 0755 files/*.exe $RPM_BUILD_ROOT%{_datadir}/%{name}

%files
%{_datadir}/%{name}

%changelog
