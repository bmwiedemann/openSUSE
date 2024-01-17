#
# spec file for package deepin-icon-theme
#
# Copyright (c) 2022 SUSE LLC
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


%define name1 deepin-launcher
%define deepin_launcher_version %(rpm -q --queryformat '%%{VERSION}' deepin-launcher)

Name:           deepin-icon-theme
Version:        2021.11.24
Release:        0
Summary:        Icons Theme
License:        GPL-3.0-or-later
Group:          System/GUI/Other
URL:            https://github.com/linuxdeepin/deepin-icon-themels
Source0:        https://github.com/linuxdeepin/deepin-icon-theme/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  deepin-launcher
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  xcursorgen
BuildArch:      noarch

%description
Icons for the Deepin Desktop Environment.

%package vintage
Summary:        Vintage icon theme for Deepin
Group:          System/GUI/Other

%description vintage
Vintage icons for the Deepin Desktop Environment.

%package -n deepin-launcher-branding-upstream
Summary:        Upstream branding for deepin-launcher
Group:          System/GUI/Other
Version:        %{deepin_launcher_version}
Release:        0
Requires:       %{name1} = %{version}
Provides:       %{name1}-branding = %{version}
Conflicts:      otherproviders(%{name1}-branding)
Supplements:    packageand(deepin-launcher:branding-upstream)

%description -n deepin-launcher-branding-upstream
Upstream branding for deepin-launcher icon.

%prep
%autosetup -p1
sed -i 's/python/python3/g' Makefile
# https://github.com/linuxdeepin/deepin-icon-theme/pull/30
find . -path ./tools -prune -false -o -type f -exec chmod 0644 \{\} +

%build
make check-perm
%make_build

%install
%make_install
%fdupes %{buildroot}%{_datadir}/icons/bloom*
%fdupes %{buildroot}%{_datadir}/icons/Vintage

%files
%doc CHANGELOG.md
%license LICENSE
%{_datadir}/icons/bloom
%{_datadir}/icons/bloom-*
%exclude %{_datadir}/icons/bloom/places/*/deepin-launcher.svg
%exclude %{_datadir}/icons/bloom-*/places/*/deepin-launcher.svg

%files vintage
%license LICENSE
%{_datadir}/icons/Vintage

%files -n deepin-launcher-branding-upstream
%license LICENSE
%{_datadir}/icons/bloom/places/*/deepin-launcher.svg
%{_datadir}/icons/bloom-*/places/*/deepin-launcher.svg

%changelog
