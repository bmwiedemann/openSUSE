#
# spec file for package wcm
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

%define major_ver 0.9
%define minor_ver 0
Name:           wcm
Version:        %{major_ver}.%{minor_ver}
Release:        0
Summary:        Wayfire Config Manager
License:        MIT
Url:            https://wayfire.org/
Source0:        https://github.com/WayfireWM/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/WayfireWM/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz.sha256sum
BuildRequires:  meson
BuildRequires:  gcc-c++
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(wayfire)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  pkgconfig(wf-config) >= %{major_ver}
BuildRequires:  pkgconfig(wf-shell) >= %{major_ver}
BuildRequires:  pkgconfig(gtkmm-3.0)
BuildRequires:  pkgconfig(xkbregistry)
BuildRequires:  pkgconfig(wlroots) >= 0.17.0
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
Requires:       wayfire >= %{major_ver}
Requires:       wdisplays >= %{major_ver}

%description
Wayfire Config Manager https://wayfire.org/.

%prep
echo "`grep %{name}-%{version}.tar.xz %{SOURCE1} | grep -Eo '^[0-9a-f]+'`  %{SOURCE0}" | sha256sum -c
%autosetup -p1

%build
# Disable including wdisplays.  It's already packaged in Factory, added Requires: for the distro package
%meson -Denable_wdisplays=false
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license LICENSE
%{_bindir}/%{name}
%dnl %{_bindir}/wdisplays
%{_datadir}/wayfire/icons
%{_datadir}/icons/hicolor/*
%{_datadir}/applications/*.desktop

%changelog

