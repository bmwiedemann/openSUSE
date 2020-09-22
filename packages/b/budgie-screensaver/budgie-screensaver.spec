#
# spec file for package budgie-screensaver
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2020 Callum Farmer <callumjfarmer13@gmail.com>
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

Name:           budgie-screensaver
Version:        20190923
Release:        0
Summary:        Fork of GNOME Screensaver for Budgie 10
License:        GPL-2.0-or-later
Group:          System/GUI/Other
URL:            https://github.com/getsolus/budgie-screensaver
Source:         %{name}-%{version}.tar.xz
# PATCH-FIX-OPENSUSE remove-old-automake-macros.patch
Patch:          remove-old-automake-macros.patch
# PATCH-FEATURE-OPENSUSE gnome-screensaver-suse-pam.patch
Patch1:          gnome-screensaver-suse-pam.patch
# PATCH-FIX-UPSTREAM gnome-screensaver-helper.patch bgo#640647 fcrozat@novell.com -- Put back helper authentication, removed by upstream
Patch2:         gnome-screensaver-helper.patch
# PATCH-FEATURE-OPENSUSE gnome-screensaver-xvkbd-on-lock.patch rodrigo@novell.com -- Run xvkbd when locking the screen
Patch3:         gnome-screensaver-xvkbd-on-lock.patch
# PATCH-FIX-UPSTREAM gnome-screensaver-multihead-unlock.patch bnc#444157 bgo#455118 rodrigo@novell.com
Patch4:        gnome-screensaver-multihead-unlock.patch
Patch5:         gnome-desktop-3.36.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pam-devel
BuildRequires:  pkgconfig(libgnomekbdui)
BuildRequires:  libXScrnSaver-devel
BuildRequires:  libXext-devel
BuildRequires:  libXxf86vm-devel
BuildRequires:  pkgconfig(libsystemd)
Requires:       /sbin/unix2_chkpwd

%lang_package

%description
Fork of GNOME Screensaver for Budgie 10

%prep
%setup -q
%patch -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
if pkg-config --atleast-version 3.36 gnome-desktop-3.0; then
%patch5 -p1
fi

%build
touch ./config.rpath
touch ./ABOUT-NLS
mkdir m4
intltoolize --copy --force --automake
autoreconf -fiv
%configure\
	--libexecdir=%{_libexecdir}/gnome-screensaver\
	--with-pam-prefix=%{_sysconfdir}\
	--enable-authentication-scheme=helper\
	--with-passwd-helper="/sbin/unix2_chkpwd"\
	--with-console-kit\
	--with-systemd\
	--disable-docbook-docs
%make_build

%install
%make_install
%find_lang gnome-screensaver

%files
%license COPYING
%config(noreplace) %{_sysconfdir}/pam.d/gnome-screensaver
%{_bindir}/*
%{_libexecdir}/gnome-screensaver
%{_datadir}/applications/gnome-screensaver.desktop
%{_datadir}/dbus-1/services/org.gnome.ScreenSaver.service
%{_mandir}/man1/*

%files lang -f gnome-screensaver.lang

%changelog
