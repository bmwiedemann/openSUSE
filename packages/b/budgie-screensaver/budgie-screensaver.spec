#
# spec file for package budgie-screensaver
#
# Copyright (c) 2021 SUSE LLC
# Copyright (c) 2021 Callum Farmer <gmbr3@opensuse.org>
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


%if 0%{?usrmerged}
%define chkpwd %{_sbindir}/unix2_chkpwd
%else
%define chkpwd /sbin/unix2_chkpwd
%endif
Name:           budgie-screensaver
Version:        20210412
Release:        0
Summary:        Fork of GNOME Screensaver for Budgie 10
License:        GPL-2.0-or-later
Group:          System/GUI/Other
URL:            https://github.com/getsolus/budgie-screensaver
Source0:        %{name}-%{version}.tar.xz
# PATCH-FIX-OPENSUSE remove-old-automake-macros.patch
Patch0:         remove-old-automake-macros.patch
# PATCH-FEATURE-OPENSUSE gnome-screensaver-suse-pam.patch
Patch1:         gnome-screensaver-suse-pam.patch
# PATCH-FIX-UPSTREAM gnome-screensaver-helper.patch bgo#640647 fcrozat@novell.com -- Put back helper authentication, removed by upstream
Patch2:         gnome-screensaver-helper.patch
# PATCH-FEATURE-OPENSUSE gnome-screensaver-xvkbd-on-lock.patch rodrigo@novell.com -- Run xvkbd when locking the screen
Patch3:         gnome-screensaver-xvkbd-on-lock.patch
# PATCH-FIX-UPSTREAM gnome-screensaver-multihead-unlock.patch bnc#444157 bgo#455118 rodrigo@novell.com
Patch4:         gnome-screensaver-multihead-unlock.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gnome-common
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libgnomekbdui)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xscrnsaver)
BuildRequires:  pkgconfig(xxf86vm)
Requires:       pam
%if 0%{?suse_version} < 1550
BuildRequires:  pkgconfig(xxf86misc)
%endif

%description
Fork of GNOME Screensaver for Budgie 10

%lang_package

%prep
%autosetup -p1

%build
export AUTOPOINT='intltoolize --copy --automake'
touch ./ABOUT-NLS
mkdir m4
mkdir build-aux
touch build-aux/config.rpath
autoreconf -fiv
%configure\
	--libexecdir=%{_libexecdir}/gnome-screensaver\
	--with-pam-prefix=%{_sysconfdir}\
	--enable-authentication-scheme=helper\
	--with-passwd-helper="%{chkpwd}"\
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
%{_datadir}/dbus-1/services/us.getsol.budgie-screensaver.service
%{_mandir}/man1/*

%files lang -f gnome-screensaver.lang

%changelog
