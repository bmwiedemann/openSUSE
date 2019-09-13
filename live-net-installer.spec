#
# spec file for package live-net-installer
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%ifarch aarch64
%define base_url http://download.opensuse.org/ports/aarch64
%else
%define base_url http://download.opensuse.org
%endif

Name:           live-net-installer
Version:        1.0
Release:        0
Summary:        Makes the installation available from a running system
License:        BSD-3-Clause
Group:          System/YaST
Url:            https://build.opensuse.org/package/show/openSUSE:Factory:Live/live-net-installer
Source1:        start-install.sh
Source2:        installation.desktop
Source3:        COPYING
Source4:        extend
Source5:        upgrade.desktop
BuildRequires:  coreutils
BuildRequires:  yast2-installation
Requires:       util-linux
Requires:       xdg-utils
Requires:       yast2-installation

%description
This package contains files that allow starting the installer from a
running (live) system.

%prep
%setup -q -T -c
cp %{SOURCE3} .

URL=
%if 0%{?is_opensuse}
# Tumbleweed?
%if 0%{?suse_version} >= 1550 && !0%{?sle_version}
URL="%{base_url}/tumbleweed/repo/oss"
%endif

# Leap?
%if 0%{?sle_version}
leap="$(expr %{?sle_version} / 100)"
leap_min="$(expr ${leap} % 100)" || true # leap_min can be 0, which causes expr to exit(1)
leap_maj="$(expr ${leap} / 100)"
URL="%{base_url}/distribution/leap/${leap_maj}.${leap_min}/repo/oss"
%endif
%endif

if [ -z "$URL" ]; then
	echo "Building for unknown distro - no repository specified."
    exit 1
fi
sed -i"" "s=@URL@=${URL}=" %{SOURCE1}

%build

%install
install -Dm 755 %{SOURCE1} %{buildroot}%{_sbindir}/start-install.sh
install -Dm 644 %{SOURCE2} %{buildroot}%{_datadir}/applications/installation.desktop
install -Dm 644 %{SOURCE5} %{buildroot}%{_datadir}/applications/upgrade.desktop
install -Dm 755 %{SOURCE4} %{buildroot}/bin/extend

%files
%license COPYING
/bin/extend
%{_sbindir}/start-install.sh
%{_datadir}/applications/installation.desktop
%{_datadir}/applications/upgrade.desktop

%changelog
