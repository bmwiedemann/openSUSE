#
# spec file for package libpeas2
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


%define         prj_version 2
%define         so_version 0
%define         glib_version 2.86
%bcond_without  gtkdoc
%bcond_without  gibind
%bcond_without  gjs
%bcond_with     lua51
%bcond_without  python3
%bcond_without  vapi

Name:           libpeas2
Version:        2.2.1
Release:        0
Summary:        GObject-based Plugin Engine version 2
License:        LGPL-2.1-or-later
URL:            https://wiki.gnome.org/Projects/Libpeas
Source0:        libpeas-%{version}.tar.zst

BuildRequires:  c++_compiler
BuildRequires:  c_compiler
BuildRequires:  fdupes
BuildRequires:  gettext-devel
BuildRequires:  meson >= 0.62.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gio-2.0) >= %{glib_version}
BuildRequires:  pkgconfig(girepository-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= %{glib_version}
BuildRequires:  pkgconfig(gmodule-2.0) >= %{glib_version}
BuildRequires:  pkgconfig(gobject-2.0) >= %{glib_version}
BuildRequires:  pkgconfig(pygobject-3.0) >= 3.2.0
%if %{with gibind}
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 1.39.0
%endif
%if %{with gjs}
BuildRequires:  pkgconfig(gjs-1.0) >= 1.77.1
BuildRequires:  pkgconfig(mozjs-140)
%endif
%if %{with gtkdoc}
BuildRequires:  pkgconfig(gi-docgen) >= 2021.7
%endif
%if %{with python3}
BuildRequires:  pkgconfig(python3) >= 3.2.0
%endif
%if %{with lua51}
BuildRequires:  lua51-lgi >= 0.9.0
BuildRequires:  pkgconfig(lua5.1) >= 5.1.0
BuildRequires:  pkgconfig(luajit) >= 2.0
%endif
%if %{with vapi}
# The vapigen binary is required
BuildRequires:  vala
%endif

%description
libpeas is a gobject-based plugin engine, and is targetted at giving
every application the chance to assume its own extensibility.

%package -n libpeas-%{prj_version}-%{so_version}
Summary:        GObject-based Plugin Engine
%if %{with gjs}
Recommends:     libpeas-loader-gjs
%endif
%if %{with lua51}
Recommends:     libpeas-loader-lua51
%endif
%if %{with python3}
Recommends:     libpeas-loader-python
%endif
# Provide "libpeas2" to make the lang package installable
Provides:       %{name} = %{version}

%description -n libpeas-%{prj_version}-%{so_version}
libpeas is a gobject-based plugin engine, and is targetted at giving
every application the chance to assume its own extensibility.

%package -n typelib-1_0-Peas-%{prj_version}
Summary:        Introspection bindings for libpeas, a GObject-based plugin engine

%description -n typelib-1_0-Peas-%{prj_version}
libpeas is a gobject-based plugin engine, and is targetted at giving
every application the chance to assume its own extensibility.

This package provides the GObject Introspection bindings for the libpeas
library.

%package devel
Summary:        Development files for libpeas, a GObject-based plugin engine
Requires:       libpeas-%{prj_version}-%{so_version} = %{version}
Requires:       typelib-1_0-Peas-%{prj_version} = %{version}

%description devel
libpeas is a gobject-based plugin engine, and is targetted at giving
every application the chance to assume its own extensibility.

%if %{with lua51}
%package loader-lua51
Summary:        Lua 5.1 runtime loader for libpeas
Supplements:    (libpeas-%{prj_version}-%{so_version} and lua51)

%description loader-lua51
libpeas is a gobject-based plugin engine, and is targetted at giving
every application the chance to assume its own extensibility.

This package contains the LUA 5.1 loader.
%endif

%if %{with gjs}
%package loader-gjs
Summary:        GJS runtime loader for libpeas
Supplements:    (libpeas-%{prj_version}-%{so_version} and gjs)

%description loader-gjs
libpeas is a gobject-based plugin engine, and is targetted at giving
every application the chance to assume its own extensibility.

This package contains the GJS loader.
%endif

%if %{with python3}
%package loader-python
Summary:        Python3 runtime loader for libpeas
Supplements:    (libpeas-%{prj_version}-%{so_version} and python3-base)

%description loader-python
libpeas is a gobject-based plugin engine, and is targetted at giving
every application the chance to assume its own extensibility.

This package contains the Python loader.
%endif

%lang_package

%prep
%autosetup -p1 -n libpeas-%{version}

%build
%meson \
    -Dgjs=%{?with_gjs:true}%{!?with_gjs:false} \
    -Dgtk_doc=%{?with_gtkdoc:true}%{!?with_gtkdoc:false} \
    -Dintrospection=%{?with_gibind:true}%{!?with_gibind:false} \
    -Dlua51=%{?with_lua51:true}%{!?with_lua51:false} \
    -Dpython3=%{?with_python3:true}%{!?with_python3:false} \
    -Dvapi=%{?with_vapi:true}%{!?with_vapi:false}

%meson_build

%install
%meson_install
%find_lang libpeas-%{prj_version} %{?no_lang_C}
%fdupes -s %{buildroot}%{_datadir}/doc/

%ldconfig_scriptlets -n libpeas-%{prj_version}-%{so_version}

%files -n libpeas-%{prj_version}-%{so_version}
%license COPYING
%doc AUTHORS README.md
%{_libdir}/libpeas-%{prj_version}.so.*
%dir %{_libdir}/libpeas-%{prj_version}
%dir %{_libdir}/libpeas-%{prj_version}/loaders

%files -n typelib-1_0-Peas-%{prj_version}
%{_libdir}/girepository-1.0/Peas-%{prj_version}.typelib

%if %{with gjs}
%files loader-gjs
%{_libdir}/libpeas-%{prj_version}/loaders/libgjsloader.so
%endif

%if %{with lua51}
%files loader-lua51
%{_libdir}/libpeas-%{prj_version}/loaders/liblua51loader.so
%endif

%if %{with python3}
%files loader-python
%{_libdir}/libpeas-%{prj_version}/loaders/libpythonloader.so
%endif

%files devel
%{_datadir}/doc/libpeas-%{prj_version}
%{_includedir}/libpeas-%{prj_version}/
%{_libdir}/libpeas-%{prj_version}.so
%{_libdir}/pkgconfig/libpeas-%{prj_version}.pc
%{_datadir}/gir-1.0/Peas-%{prj_version}.gir
%if %{with vapi}
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/libpeas-%{prj_version}.deps
%{_datadir}/vala/vapi/libpeas-%{prj_version}.vapi
%endif

%files lang -f libpeas-%{prj_version}.lang

%changelog
