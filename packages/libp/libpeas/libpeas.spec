#
# spec file for package libpeas
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


%bcond_with lua51
%bcond_without python3
Name:           libpeas
Version:        1.36.0
Release:        0
Summary:        GObject-based Plugin Engine
License:        LGPL-2.1-or-later
Group:          Development/Libraries/GNOME
URL:            https://wiki.gnome.org/Projects/Libpeas
Source0:        https://download.gnome.org/sources/libpeas/1.36/%{name}-%{version}.tar.xz

BuildRequires:  fdupes
BuildRequires:  gettext
BuildRequires:  meson >= 0.50.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gi-docgen)
BuildRequires:  pkgconfig(gio-2.0) >= 2.44.0
BuildRequires:  pkgconfig(gladeui-2.0)
BuildRequires:  pkgconfig(gobject-2.0) >= 2.44.0
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 1.39.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.0.0
BuildRequires:  pkgconfig(pygobject-3.0) >= 3.0.0
%if %{with python3}
BuildRequires:  pkgconfig(python3) >= 3.2.0
%endif
%if %{with lua51}
BuildRequires:  lua51-devel >= 5.1.0
BuildRequires:  pkgconfig(luajit) >= 2.0
%endif

%description
libpeas is a gobject-based plugin engine, and is targetted at giving
every application the chance to assume its own extensibility.

%package -n libpeas-1_0-0
Summary:        GObject-based Plugin Engine
# We provide %%{name} to make the lang package installable
Group:          System/Libraries
Recommends:     %{name}-loader-python3
Provides:       %{name} = %{version}
# The gjs loader is officially no longer supported upstream (removed from git).
# With gjs moving to mozjs-24, it also fails building; so we follow upstream.
Obsoletes:      %{name}-loader-gjs <= %{version}
# Stop packaging the demo sub-package
Obsoletes:      %{name}-demo <= %{version}

%description -n libpeas-1_0-0
libpeas is a gobject-based plugin engine, and is targetted at giving
every application the chance to assume its own extensibility.

%package -n typelib-1_0-Peas-1_0
Summary:        Introspection bindings for libpeas, a GObject-based plugin engine
Group:          System/Libraries

%description -n typelib-1_0-Peas-1_0
libpeas is a gobject-based plugin engine, and is targetted at giving
every application the chance to assume its own extensibility.

This package provides the GObject Introspection bindings for the libpeas
library.

%package -n libpeas-gtk-1_0-0
Summary:        GObject-based Plugin Engine
Group:          System/Libraries

%description -n libpeas-gtk-1_0-0
libpeas is a gobject-based plugin engine, and is targetted at giving
every application the chance to assume its own extensibility.

%package -n typelib-1_0-PeasGtk-1_0
Summary:        Introspection bindings for the libpeas-gtk library
Group:          System/Libraries

%description -n typelib-1_0-PeasGtk-1_0
libpeas is a gobject-based plugin engine, and is targetted at giving
every application the chance to assume its own extensibility.

This package provides the GObject Introspection bindings for the
libpeas-gtk library.

%package loader-python3
Summary:        Python3 runtime loader for libpeas
Group:          System/Libraries
Supplements:    (libpeas-1_0-0 and python3)

%description loader-python3
libpeas is a gobject-based plugin engine, and is targetted at giving
every application the chance to assume its own extensibility.

This package contains the python3 loader.

%if %{with lua51}
%package loader-lua51
Summary:        Lua 5.1 runtime loader for libpeas
Group:          System/Libraries
Supplements:    packageand(libpeas-1_0-0:lua51)

%description loader-lua51
libpeas is a gobject-based plugin engine, and is targetted at giving
every application the chance to assume its own extensibility.

This package contains the LUA 5.1 loader.
%endif

%package -n glade-catalog-libpeas
Summary:        Glade catalog for libpeas, a GObject-based plugin engine
Group:          Development/Tools/GUI Builders
Requires:       glade
Requires:       libpeas-gtk-1_0-0 = %{version}
Supplements:    (glade and %{name}-devel)
BuildArch:      noarch

%description -n glade-catalog-libpeas
libpeas is a gobject-based plugin engine, and is targetted at giving
every application the chance to assume its own extensibility.

This package provides a catalog for Glade, to allow the use the libpeas
widgets in Glade.

%package devel
Summary:        Development files for libpeas, a GObject-based plugin engine
Group:          Development/Languages/C and C++
Requires:       libpeas-1_0-0 = %{version}
Requires:       libpeas-gtk-1_0-0 = %{version}
Requires:       typelib-1_0-Peas-1_0 = %{version}
Requires:       typelib-1_0-PeasGtk-1_0 = %{version}

%description devel
libpeas is a gobject-based plugin engine, and is targetted at giving
every application the chance to assume its own extensibility.

%lang_package

%prep
%autosetup -p1

%build
%meson \
	-Dgtk_doc=true \
	-Ddemos=false \
%if !%{with lua51}
	-Dlua51=false \
%endif
%if %{with python2}
	-Dpython2=true \
%endif
	%{nil}
%meson_build

%install
%meson_install
%find_lang %{name}-1.0 %{?no_lang_C}
%fdupes -s %{buildroot}%{_datadir}/doc/

%ldconfig_scriptlets -n libpeas-1_0-0
%ldconfig_scriptlets -n libpeas-gtk-1_0-0

%files -n libpeas-1_0-0
%license COPYING
%doc AUTHORS README
%{_libdir}/libpeas-1.0.so.*
%dir %{_libdir}/libpeas-1.0
%dir %{_libdir}/libpeas-1.0/loaders

%files -n typelib-1_0-Peas-1_0
%{_libdir}/girepository-1.0/Peas-1.0.typelib

%files -n libpeas-gtk-1_0-0
%{_libdir}/libpeas-gtk-1.0.so.*
# The icon is the default icon shown for loaded plugins without own definition.
%{_datadir}/icons/hicolor/*/actions/libpeas-plugin.*

%files -n typelib-1_0-PeasGtk-1_0
%{_libdir}/girepository-1.0/PeasGtk-1.0.typelib

%if %{with python3}
%files loader-python3
%{_libdir}/libpeas-1.0/loaders/libpython3loader.so
%endif

%if %{with lua51}
%files loader-lua51
%{_libdir}/libpeas-1.0/loaders/liblua51loader.so
%endif

%files -n glade-catalog-libpeas
%{_datadir}/glade/catalogs/libpeas-gtk.xml

%files devel
%{_datadir}/doc/libpeas-1.0
%{_datadir}/doc/libpeas-gtk-1.0
%{_includedir}/libpeas-1.0/
%{_libdir}/libpeas-1.0.so
%{_libdir}/libpeas-gtk-1.0.so
%{_libdir}/pkgconfig/libpeas-1.0.pc
%{_libdir}/pkgconfig/libpeas-gtk-1.0.pc
%{_datadir}/gir-1.0/Peas-1.0.gir
%{_datadir}/gir-1.0/PeasGtk-1.0.gir

%files lang -f %{name}-1.0.lang

%changelog
