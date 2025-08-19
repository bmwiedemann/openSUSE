#
# spec file for package xfce4-screensaver
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%bcond_without wayland

Name:           xfce4-screensaver
Version:        4.20.1
Release:        0
Summary:        Screensaver and locker for Xfce
License:        GPL-2.0-only
Group:          System/GUI/XFCE
URL:            https://docs.xfce.org/apps/xfce4-screensaver/start
Source:         https://archive.xfce.org/src/apps/xfce4-screensaver/4.20/%{name}-%{version}.tar.xz
# PATCH-FIX-OPENSUSE 0001-relax_versions.diff -- Allow build for Leap with its ancient but sufficient X11 packages.
Patch01:        0001-relax_versions.diff
BuildRequires:  gettext >= 0.19.8
BuildRequires:  meson >= 0.60.0
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  xfce4-session
BuildRequires:  xfconf >= 4.18.0
BuildRequires:  xscreensaver-data
BuildRequires:  pkgconfig(dbus-1) >= 0.30
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(garcon-1) >= 4.18.0
BuildRequires:  pkgconfig(garcon-gtk3-1) >= 4.18.0
BuildRequires:  pkgconfig(gdk-wayland-3.0) >= 3.24.0
BuildRequires:  pkgconfig(gdk-x11-3.0) >= 3.24.0
BuildRequires:  pkgconfig(gio-2.0) >= 2.50.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.50.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.24.0
BuildRequires:  pkgconfig(gtk+-x11-3.0) >= 3.24.0
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libwnck-3.0) >= 3.20
BuildRequires:  pkgconfig(libxfce4ui-2) >= 4.18.4
BuildRequires:  pkgconfig(libxfce4util-1.0) >= 4.18.0
BuildRequires:  pkgconfig(libxfce4windowing-0) >= 4.19.2
BuildRequires:  pkgconfig(libxfconf-0) >= 4.18.0
BuildRequires:  pkgconfig(libxklavier) >= 5.2
BuildRequires:  pkgconfig(x11) >= 1.6.7
BuildRequires:  pkgconfig(xext) >= 1.0.0
BuildRequires:  pkgconfig(xscrnsaver) >= 1.2.2
%if %{with wayland}
BuildRequires:  pkgconfig(libwlembed-0)
BuildRequires:  pkgconfig(libwlembed-gtk3-0)
BuildRequires:  pkgconfig(wayland-protocols)
%endif
Requires:       xfconf
Recommends:     %{name}-lang
Conflicts:      xscreensaver

%description
xfce4-screensaver is a screen saver and locker that integrates with the Xfce desktop.
This software is not ready for production machines yet. Please use with caution.

Add xfce4-screensaver-command -l to xflock4 script for it to work properly.

%lang_package

%prep
%autosetup -p1

%build
%meson	\
    -Dauthentication-scheme=pam	\
    -Dpam-auth-type=common	\
    -Dsession-manager=systemd	\
    -Dx11=enabled		\
%if %{with wayland}
    -Dwayland=enabled		\
%endif
    -Ddocs=disabled
%meson_build

%install
%meson_install
%find_lang %{name}
%if 0%{?suse_version} > 1500
mkdir -p %{buildroot}%{_pam_vendordir}
mv %{buildroot}%{_sysconfdir}/pam.d/xfce4-screensaver %{buildroot}%{_pam_vendordir}
%endif

%if 0%{?suse_version} > 1500
%pre
# Prepare for migration to /usr/lib; save any old .rpmsave
for i in pam.d/xfce4-screensaver ; do
     test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i}.rpmsave.old ||:
done

%posttrans
# Migration to /usr/lib, restore just created .rpmsave
for i in pam.d/xfce4-screensaver ; do
     test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i} ||:
done
%endif

%files -f  %{name}.lang
%license COPYING COPYING.LGPL COPYING.LIB
%doc README.md NEWS
%dir %{_sysconfdir}/xdg/menus
%dir %{_datadir}/applications/screensavers
%dir %{_datadir}/desktop-directories
%dir %{_datadir}/icons/hicolor
%dir %{_libexecdir}/xfce4-screensaver/
%config %{_sysconfdir}/xdg/autostart/xfce4-screensaver.desktop
%config %{_sysconfdir}/xdg/menus/xfce4-screensavers.menu
%if 0%{?suse_version} > 1500
%{_pam_vendordir}/xfce4-screensaver
%else
%config %{_sysconfdir}/pam.d/xfce4-screensaver
%endif
%{_bindir}/xfce4-screensaver
%{_bindir}/xfce4-screensaver-command
%{_bindir}/xfce4-screensaver-preferences
%{_datadir}/applications/screensavers/xfce-floaters.desktop
%{_datadir}/applications/xfce4-screensaver-preferences.desktop
%{_datadir}/applications/screensavers/xfce-personal-slideshow.desktop
%{_datadir}/applications/screensavers/xfce-popsquares.desktop
%{_datadir}/dbus-1/services/org.xfce.ScreenSaver.service
%{_datadir}/desktop-directories/xfce4-screensaver.directory
%{_libexecdir}/xfce4-screensaver-*
%{_libexecdir}/xfce4-screensaver/*
%{_mandir}/man1/xfce4-screensaver-command.1%{?ext_man}
%{_mandir}/man1/xfce4-screensaver-preferences.1%{?ext_man}
%{_mandir}/man1/xfce4-screensaver.1%{?ext_man}
%{_datadir}/pixmaps/xfce-logo-white.svg
%{_datadir}/icons/hicolor/*

%changelog
