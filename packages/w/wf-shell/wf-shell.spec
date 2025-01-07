#
# spec file for package wf-shell
#
# Copyright (c) 2023 SUSE LLC
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

%define major_ver 0.9
%define minor_ver 0
Name:           wf-shell
Version:        %{major_ver}.%{minor_ver}
Release:        0
Summary:        A GTK3-based panel for wayfire
License:        MIT
URL:            https://wayfire.org/
Source0:        https://github.com/WayfireWM/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/WayfireWM/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz.sha256sum
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libboost_filesystem-devel
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(dbusmenu-gtk3-0.4)
BuildRequires:  pkgconfig(gtk-layer-shell-0)
BuildRequires:  pkgconfig(gtkmm-3.0)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(wayfire)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wf-config) >= %{major_ver}
BuildRequires:  pkgconfig(wlroots) >= 0.17.0

%description
wf-shell is a repository which contains the various components needed to built a fully functional DE based around wayfire. Currently it has only a GTK-based panel and background client.

%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}

%description devel
Development libraries for %{name}

%prep
echo "`grep %{name}-%{version}.tar.xz %{SOURCE1} | grep -Eo '^[0-9a-f]+'`  %{SOURCE0}" | sha256sum -c
%autosetup

%build
%meson
%meson_build

%install
%meson_install
install -D -m 0644 wf-shell.ini.example %{buildroot}%{_datadir}/wayfire/wf-shell.ini.example
%fdupes %{buildroot}%{_prefix}

%check
%meson_test

%files
%{_bindir}/wf-*
%{_bindir}/wayland-logout
%{_datadir}/wayfire/
%{_datadir}/wayfire/wf-shell.ini.example
%dir %{_datadir}/icons/hicolor/160x160
%dir %{_datadir}/icons/hicolor/160x160/apps
%{_datadir}/icons/*/*/*/*.png
%{_datadir}/icons/*/*/*/*.svg
%{_mandir}/man1/wayland-logout.1%{?ext_man}

%files devel
%{_libdir}/pkgconfig/wf-shell.pc

%changelog
