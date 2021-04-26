#
# spec file for package deepin-icon-theme
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%define name1 deepin-launcher
%define deepin_launcher_version %(rpm -q --queryformat '%%{VERSION}' deepin-launcher)

Name:           deepin-icon-theme
Version:        2020.09.25
Release:        0
Summary:        Icons Theme
License:        GPL-3.0+
URL:            https://github.com/linuxdeepin/deepin-icon-theme
Source0:        https://github.com/linuxdeepin/deepin-icon-theme/archive/%{version}/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM deepin-icon-theme_fix-makefile.patch hillwood@opensuse.org - fix makefile
Patch0:         deepin-icon-theme_fix-makefile.patch
Group:          System/GUI/Other
BuildArch:      noarch
BuildRequires:  deepin-launcher
BuildRequires:  hicolor-icon-theme
BuildRequires:  xcursorgen
BuildRequires:  fdupes
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Icons for the Deepin Desktop Environment.

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
%setup -q
%patch0 -p1
sed -i 's/python/python3/g' Makefile

%build
make check-perm
%make_build

%install
make install-icons DESTDIR=%{buildroot}
make install-cursors DESTDIR=%{buildroot}

rm %{buildroot}%{_datadir}/icons/bloom/actions/24/draw-triangle1.svg
ln -sf %{_datadir}/icons/bloom/status/20/arrow-left.svg %{buildroot}%{_datadir}/icons/bloom/actions/24/draw-triangle1.svg
rm %{buildroot}%{_datadir}/icons/bloom/actions/24/draw-triangle2.svg
ln -sf %{_datadir}/icons/bloom/status/20/arrow-right.svg %{buildroot}%{_datadir}/icons/bloom/actions/24/draw-triangle2.svg
rm %{buildroot}%{_datadir}/icons/bloom/actions/24/draw-triangle3.svg
ln -sf %{_datadir}/icons/bloom/status/20/arrow-up.svg %{buildroot}%{_datadir}/icons/bloom/actions/24/draw-triangle3.svg
rm %{buildroot}%{_datadir}/icons/bloom/actions/24/draw-triangle4.svg
ln -sf %{_datadir}/icons/bloom/status/20/arrow-down.svg %{buildroot}%{_datadir}/icons/bloom/actions/24/draw-triangle4.svg
rm %{buildroot}%{_datadir}/icons/bloom/actions/24/edit-delete-shred.svg
# ln -sf %{_datadir}/icons/bloom/status/20/trash-empty.svg %{buildroot}%{_datadir}/icons/bloom/actions/24/edit-delete-shred.svg
rm %{buildroot}%{_datadir}/icons/bloom/actions/24/itmages-remove.svg
# ln -sf %{_datadir}/icons/bloom/status/20/trash-empty.svg %{buildroot}%{_datadir}/icons/bloom/actions/24/itmages-remove.svg

%fdupes %{buildroot}

%files
%defattr(-,root,root,-)
%doc CHANGELOG.md
%license LICENSE
%{_datadir}/icons/bloom
%{_datadir}/icons/bloom-*
%exclude %{_datadir}/icons/bloom/places/*/deepin-launcher.svg
%exclude %{_datadir}/icons/bloom-*/places/*/deepin-launcher.svg

%files -n deepin-launcher-branding-upstream
%defattr(-,root,root,-)
%license LICENSE
%{_datadir}/icons/bloom/places/*/deepin-launcher.svg
%{_datadir}/icons/bloom-*/places/*/deepin-launcher.svg

%changelog
