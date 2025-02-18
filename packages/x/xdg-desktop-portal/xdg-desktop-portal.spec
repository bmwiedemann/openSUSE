#
# spec file for package xdg-desktop-portal
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2024 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "docs"
%bcond_without  docs
%define psuffix -devel-docs
%else
%bcond_with     docs
%endif

%define oname xdg-desktop-portal

Name:           %{oname}%{?psuffix}
Version:        1.19.4
Release:        0
%if "%{flavor}" == ""
Summary:        A portal frontend service for Flatpak
Group:          System/Libraries
%else
Summary:        Development documentation for xdg-desktop-portal
Group:          Documentation/HTML
Supplements:    (%{oname}-devel and patterns-base-documentation)
%endif
License:        LGPL-2.1-or-later
URL:            https://github.com/flatpak/xdg-desktop-portal
Source0:        %{url}/releases/download/%{version}/%{oname}-%{version}.tar.xz

BuildRequires:  docutils
BuildRequires:  meson >= 0.58
BuildRequires:  pkgconfig

%if %{with docs}
BuildRequires:  python3-Sphinx
BuildRequires:  python3-furo
BuildRequires:  python3-sphinxcontrib-copybutton
BuildRequires:  python3-sphinxext-opengraph
%endif
BuildRequires:  gstreamer-plugins-good
BuildRequires:  gstreamer-utils
BuildRequires:  systemd-rpm-macros
BuildRequires:  xmlto
BuildRequires:  pkgconfig(flatpak)
BuildRequires:  pkgconfig(fuse3)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libgeoclue-2.0) >= 2.5.2
BuildRequires:  pkgconfig(libpipewire-0.3) >= 0.2.90
BuildRequires:  pkgconfig(libportal) >= 0.9.0
BuildRequires:  pkgconfig(libsystemd)
# Break cycle: we buildrequire flatpak, and flatpak has a requires on xdg-desktop-portal
#!BuildIgnore:  xdg-desktop-portal
# xdg-desktop-portal calls out to fusermount3 (in $PATH) (boo#1197567)
# document-portal/document-portal-fuse.c: char *umount_argv[] = { "fusermount3", "-u", "-z", (char *) path, NULL };
Requires:       %{_bindir}/fusermount3

%if "%{flavor}" == ""
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

%else

%description
A portal frontend service for Flatpak and possibly other desktop containment frameworks.

xdg-desktop-portal works by exposing a series of D-Bus interfaces known as portals under
a well-known name (org.freedesktop.portal.Desktop) and object path (/org/freedesktop/portal/desktop).

This package contains convenience documentation for developers.
%endif

%lang_package

%prep
%autosetup -p1 -n %{oname}-%{version}

%build
%meson %{!?with_docs:-Ddocumentation=disabled} \
	-Dtests=disabled \
	%{nil}
%meson_build

%install
%meson_install

# own the packaging directories
install -d %{buildroot}%{_datadir}/xdg-desktop-portal/portals
%if %{with docs}
rm -fr %{buildroot}/%{_datadir}/{dbus-1,%{oname},locale,pkgconfig} %buildroot%{_userunitdir} %{buildroot}%{_mandir} %{buildroot}/%{_libdir} %{buildroot}/%{_libexecdir} %{_vpath_builddir}/doc/html/.doctrees
%else
%find_lang %{oname} %{?no_lang_C}
%endif

%if "%{flavor}" == ""
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
%dir %{_datadir}/%{name}/portals
%{_libexecdir}/%{name}
%{_libexecdir}/xdg-desktop-portal-validate-icon
%{_libexecdir}/xdg-desktop-portal-validate-sound
%{_libexecdir}/xdg-document-portal
%{_libexecdir}/xdg-permission-store
%{_libexecdir}/xdg-desktop-portal-rewrite-launchers
%{_userunitdir}/%{name}.service
%{_userunitdir}/xdg-document-portal.service
%{_userunitdir}/xdg-permission-store.service
%{_userunitdir}/xdg-desktop-portal-rewrite-launchers.service
%{_mandir}/man5/portals.conf.5%{?ext_man}

%files devel
%license COPYING
%if %{pkg_vcmp meson < 0.62.0 }
%{_libdir}/pkgconfig/%{name}.pc
%else
%{_datadir}/pkgconfig/%{name}.pc
%endif

%files lang -f %{name}.lang
%license COPYING

%else

%files
%doc %{_vpath_builddir}/doc/html
%endif

%changelog
