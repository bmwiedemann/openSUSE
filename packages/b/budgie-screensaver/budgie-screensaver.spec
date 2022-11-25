#
# spec file for package budgie-screensaver
#
# Copyright (c) 2022 SUSE LLC
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


%if 0%{?suse_version} < 1550
%define _distconfdir %{_sysconfdir}
%endif
%if 0%{?usrmerged}
%define chkpwd %{_sbindir}/unix2_chkpwd
%else
%define chkpwd /sbin/unix2_chkpwd
%endif
Name:           budgie-screensaver
Version:        5.1.0+0
Release:        0
Summary:        Fork of GNOME Screensaver for Budgie 10
License:        GPL-2.0-or-later
Group:          System/GUI/Other
URL:            https://github.com/BuddiesOfBudgie/budgie-screensaver
Source0:        %{name}-%{version}.tar.xz
Patch0:         gnome-screensaver-suse-pam.patch
BuildRequires:  intltool
BuildRequires:  meson
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
Requires:       procps
%if 0%{?suse_version} < 1550
BuildRequires:  pkgconfig(xxf86misc)
%endif

%description
Fork of GNOME Screensaver for Budgie 10

%lang_package

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
mkdir -p %{buildroot}%{_sysconfdir}/xdg/autostart
cp %{buildroot}%{_datadir}/applications/budgie-screensaver.desktop %{buildroot}%{_sysconfdir}/xdg/autostart/budgie-desktop-screensaver.desktop
%find_lang budgie-screensaver

%files
%license LICENSE
%config(noreplace) %{_sysconfdir}/pam.d/budgie-screensaver
%{_bindir}/budgie-screensaver
%{_bindir}/budgie-screensaver-command
%{_libexecdir}/budgie-screensaver-dialog
%{_datadir}/applications/budgie-screensaver.desktop
%{_sysconfdir}/xdg/autostart/budgie-desktop-screensaver.desktop
%{_mandir}/man1/budgie-screensaver-command.1%{?ext_man}
%{_mandir}/man1/budgie-screensaver.1%{?ext_man}

%files lang -f budgie-screensaver.lang

%changelog
