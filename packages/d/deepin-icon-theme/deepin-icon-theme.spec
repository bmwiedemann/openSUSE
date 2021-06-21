#
# spec file for package deepin-icon-theme
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

%define name1 deepin-launcher
%define deepin_launcher_version %(rpm -q --queryformat '%%{VERSION}' deepin-launcher)

Name:           deepin-icon-theme
Version:        2021.03.12
Release:        0
Summary:        Icons Theme
Group:          System/GUI/Other
License:        GPL-3.0+
URL:            https://github.com/linuxdeepin/deepin-icon-theme
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM deepin-icon-theme_fix-makefile.patch -- https://github.com/linuxdeepin/deepin-icon-theme/pull/23
Patch0:         0001-fix-Makefile-s-install-target.patch
# PATCH-FIX-UPSTREAM 0001-Fix-broken-symlinks.patch -- https://github.com/linuxdeepin/deepin-icon-theme/pull/41
Patch1:         0001-Fix-broken-symlinks.patch
# PATCH-FIX-UPSTREAM 0001-fix-fix-litian.patch
Patch2:         0001-fix-fix-litian.patch
# PATCH-FIX-UPSTREAM 0002-fix-soft-link-error.patch
Patch3:         0002-fix-soft-link-error.patch
BuildRequires:  deepin-launcher
BuildRequires:  hicolor-icon-theme
BuildRequires:  xcursorgen
BuildRequires:  fdupes
BuildArch:      noarch

%description
Icons for the Deepin Desktop Environment.

%package vintage
Summary:        Vintage icon theme for Deepin

%description vintage
Vintage icons for the Deepin Desktop Environment.

%package -n deepin-launcher-branding-upstream
Summary:        Upstream branding for deepin-launcher
Version:        %{deepin_launcher_version}
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
