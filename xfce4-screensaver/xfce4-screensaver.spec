#
# spec file for package xfce4-screensaver
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


%bcond_with git
Name:           xfce4-screensaver
Version:        0.1.8
Release:        0
Summary:        Screensaver and locker for Xfce
License:        GPL-2.0-only
Group:          System/GUI/XFCE
URL:            https://git.xfce.org/apps/xfce4-screensaver/about/
# PATCH-FIX-OPENSUSE xfce4-screensaver_pam_fix_opensuse.patch maurizio.galli@gmail.com -- PAM fix for openSUSE
Patch0:         xfce4-screensaver_pam_fix_opensuse.patch
Source:         https://archive.xfce.org/src/apps/xfce4-screensaver/0.1/%{name}-%{version}.tar.bz2
BuildRequires:  intltool
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig
BuildRequires:  xfce4-session
BuildRequires:  xfconf
BuildRequires:  xscreensaver-data
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(garcon-1)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libwnck-3.0)
BuildRequires:  pkgconfig(libxfce4ui-2)
BuildRequires:  pkgconfig(libxfce4util-1.0)
BuildRequires:  pkgconfig(libxklavier)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xscrnsaver)
%if %{with git}
BuildRequires:  xfce4-dev-tools
%endif
Requires:       xfconf
Recommends:     %{name}-lang
Recommends:     xscreensaver-data

%description
xfce4-screensaver is a screen saver and locker that integrates with the Xfce desktop.
This software is not ready for production machines yet. Please use with caution.

Add xfce4-screensaver-command -l to xflock4 script for it to work properly.

%lang_package

%prep
%autosetup -p1

%build
%if %{with git}
NOCONFIGURE=1 ./autogen.sh
%configure \
    --enable-maintainer-mode \
    --with-systemd     \
    --enable-pam       \
    --enable-locking   \
    --with-console-kit \
    --with-pam-auth-type=common
%else
%configure  \
    --with-systemd     \
    --enable-pam       \
    --enable-locking   \
    --with-console-kit \
    --with-pam-auth-type=common
%endif

%make_build

%install
%make_install
%find_lang %{name}

%files -f  %{name}.lang
%license COPYING COPYING.LGPL COPYING.LIB
%doc README.md NEWS TODO ChangeLog
%dir %{_sysconfdir}/xdg/menus
%dir %{_prefix}/lib/xfce4-screensaver
%dir %{_datadir}/applications/screensavers
%dir %{_datadir}/desktop-directories
%config %{_sysconfdir}/xdg/autostart/xfce4-screensaver.desktop
%config %{_sysconfdir}/xdg/menus/xfce4-screensavers.menu
%config %{_sysconfdir}/pam.d/xfce4-screensaver
%{_bindir}/xfce4-screensaver
%{_bindir}/xfce4-screensaver-command
%{_bindir}/xfce4-screensaver-configure
%{_bindir}/xfce4-screensaver-preferences
%{_prefix}/lib/xfce4-screensaver-dialog
%{_prefix}/lib/xfce4-screensaver-gl-helper
%{_prefix}/lib/xfce4-screensaver/floaters
%{_prefix}/lib/%{name}/popsquares
%{_prefix}/lib/%{name}/slideshow
%{_datadir}/applications/screensavers/xfce-floaters.desktop
%{_datadir}/applications/xfce4-screensaver-preferences.desktop
%{_datadir}/applications/screensavers/xfce-personal-slideshow.desktop
%{_datadir}/applications/screensavers/xfce-popsquares.desktop
%{_datadir}/dbus-1/services/org.xfce.ScreenSaver.service
%{_datadir}/desktop-directories/xfce4-screensaver.directory
%{_mandir}/man1/xfce4-screensaver-command.1%{?ext_man}
%{_mandir}/man1/xfce4-screensaver-preferences.1%{?ext_man}
%{_mandir}/man1/xfce4-screensaver.1%{?ext_man}
%{_datadir}/pixmaps/xfce-logo-white.svg

%changelog
