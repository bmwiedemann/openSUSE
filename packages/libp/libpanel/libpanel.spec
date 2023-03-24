#
# spec file for package libpanel
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


%define libname %{name}1-1

Name:           libpanel
Version:        1.2.0
Release:        0
Summary:        IDE paneling library for GTK
License:        LGPL-3.0-or-later
URL:            https://gitlab.gnome.org/GNOME/libpanel
Source:         https://download.gnome.org/sources/%{name}/1.2/%{name}-%{version}.tar.xz

BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(vapigen)

%description
A collection of GTK widgets for IDE-like applications targeting
GNOME using GTK and libadwaita.

%package -n     %{libname}
Summary:        Shared library files for %{name}
Provides:       %{name} = %{version}

%description -n %{libname}
The %{libname} package contains shared libraries %{name}.

%package -n     typelib-1_0-Panel-1
Summary:        Typelib files for %{name}

%description -n typelib-1_0-Panel-1
Package contains typelib files for use with %{name}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{libname} = %{version}
Requires:       typelib-1_0-Panel-1 = %{version}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%lang_package

%prep
%autosetup -p1

%build
%meson \
	-D docs=disabled \
	%{nil}
%meson_build

%install
%meson_install
%find_lang %{name}

%ldconfig_scriptlets -n %{libname}

%files -n %{libname}
%license COPYING
%{_libdir}/%{name}-1.so.*

%files -n typelib-1_0-Panel-1
%{_libdir}/girepository-1.0/Panel-1.typelib

%files devel
%doc AUTHORS NEWS README.md
%{_includedir}/libpanel-1/
%{_libdir}/libpanel-1.so
%{_libdir}/pkgconfig/libpanel-1.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Panel-1.gir
%{_datadir}/icons/hicolor/scalable/actions/panel-*-symbolic.svg
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/libpanel-1.deps
%{_datadir}/vala/vapi/libpanel-1.vapi

%files lang -f %{name}.lang

%changelog
