#
# spec file for package xdg-desktop-portal
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


Name:           xdg-desktop-portal
Version:        1.18.2
Release:        0
Summary:        A portal frontend service for Flatpak
License:        LGPL-2.1-or-later
Group:          System/Libraries
URL:            https://github.com/flatpak/xdg-desktop-portal
Source0:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  docutils
BuildRequires:  meson >= 0.58
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  xmlto
BuildRequires:  pkgconfig(flatpak)
BuildRequires:  pkgconfig(fuse3)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libgeoclue-2.0) >= 2.5.2
BuildRequires:  pkgconfig(libpipewire-0.3) >= 0.2.90
BuildRequires:  pkgconfig(libportal)
BuildRequires:  pkgconfig(libsystemd)
# Break cycle: we buildrequire flatpak, and flatpak has a requires on xdg-desktop-portal
#!BuildIgnore:  xdg-desktop-portal
# xdg-dfesktop-portal calls out to fusermount3 (in $PATH) (boo#1197567)
# document-portal/document-portal-fuse.c: char *umount_argv[] = { "fusermount3", "-u", "-z", (char *) path, NULL };
Requires:       %{_bindir}/fusermount3

%description
A portal frontend service for Flatpak and possibly other desktop containment frameworks.

xdg-desktop-portal works by exposing a series of D-Bus interfaces known as portals under
a well-known name (org.freedesktop.portal.Desktop) and object path (/org/freedesktop/portal/desktop).

The portal interfaces include APIs for file access, opening URIs, printing and others.

%package devel
Summary:        A portal frontend service for Flatpak -- Development files
Group:          Development/Languages/C and C++
Requires:       %{name} = %{version}

%description devel
A portal frontend service for Flatpak and possibly other desktop containment frameworks.

xdg-desktop-portal works by exposing a series of D-Bus interfaces known as portals under
a well-known name (org.freedesktop.portal.Desktop) and object path (/org/freedesktop/portal/desktop).

This package contains convenience files for developers.

%lang_package

%prep
%autosetup -p1

%build
%meson \
	-Dpytest=disabled \
	%{nil}
%meson_build

%install
%meson_install

# own the packaging directories
install -d %{buildroot}%{_datadir}/xdg-desktop-portal

%find_lang %{name} %{?no_lang_C}

%post
%systemd_user_post %{name}.service xdg-document-portal.service xdg-permission-store.service

%preun
%systemd_user_preun %{name}.service xdg-document-portal.service xdg-permission-store.service

%files
%license COPYING
%dir %{_datadir}/dbus-1
%dir %{_datadir}/dbus-1/interfaces
%dir %{_datadir}/dbus-1/services
%{_datadir}/dbus-1/interfaces/*.xml
%{_datadir}/dbus-1/services/org.freedesktop.impl.portal.PermissionStore.service
%{_datadir}/dbus-1/services/org.freedesktop.portal.Desktop.service
%{_datadir}/dbus-1/services/org.freedesktop.portal.Documents.service
%dir %{_datadir}/%{name}
%{_libexecdir}/%{name}
%{_libexecdir}/xdg-desktop-portal-validate-icon
%{_libexecdir}/xdg-document-portal
%{_libexecdir}/xdg-permission-store
%{_libexecdir}/xdg-desktop-portal-rewrite-launchers
%{_userunitdir}/%{name}.service
%{_userunitdir}/xdg-document-portal.service
%{_userunitdir}/xdg-permission-store.service
%{_userunitdir}/xdg-desktop-portal-rewrite-launchers.service
%{_mandir}/man5/portals.conf.5%{?ext_man}

%files devel
%doc %{_datadir}/doc/%{name}/
%if %{pkg_vcmp meson < 0.62.0 }
%{_libdir}/pkgconfig/%{name}.pc
%else
%{_datadir}/pkgconfig/%{name}.pc
%endif

%files lang -f %{name}.lang

%changelog
