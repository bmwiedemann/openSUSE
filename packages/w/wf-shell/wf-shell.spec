#
# spec file for package wf-shell
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           wf-shell
Version:        0.11.0
Release:        0
Summary:        A GTK4-based panel for wayfire
License:        MIT
URL:            https://wayfire.org/
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libboost_filesystem-devel
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(dbusmenu-glib-0.4)
BuildRequires:  pkgconfig(ddcutil)
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(gtk4-layer-shell-0)
BuildRequires:  pkgconfig(gtkmm-4.0)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(pam)
BuildRequires:  pkgconfig(wayfire)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wf-config)
BuildRequires:  pkgconfig(wireplumber-0.5)
BuildRequires:  pkgconfig(wlroots-0.20)
BuildRequires:  pkgconfig(xkbregistry)
BuildRequires:  pkgconfig(yyjson)

%description
wf-shell is a repository which contains the various components needed to built a fully functional DE based around wayfire. Currently it has only a GTK-based panel and background client.

%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}

%description devel
Development libraries for %{name}

%prep
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
%{_sysconfdir}/pam.d/wf-locker
%dir %{_sysconfdir}/xdg/xdg-desktop-portal-wlr
%{_sysconfdir}/xdg/xdg-desktop-portal-wlr/wayfire
%{_datadir}/applications/wf-locker-pin.desktop
%{_datadir}/wayfire/wf-shell.ini.example
%{_datadir}/wf-shell/
%dir %{_datadir}/icons/hicolor/160x160
%dir %{_datadir}/icons/hicolor/160x160/apps
%{_datadir}/icons/*/*/*/*.png
%{_datadir}/icons/*/*/*/*.svg
%{_mandir}/man1/wayland-logout.1%{?ext_man}

%files devel
%{_libdir}/pkgconfig/wf-shell.pc

%changelog
