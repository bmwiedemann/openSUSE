#
# spec file for package libgweather4
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


Name:           libgweather4
Version:        4.2.0
Release:        0
Summary:        Library to get online weather information
License:        GPL-2.0-or-later
Group:          Development/Libraries/GNOME
URL:            https://wiki.gnome.org/Projects/LibGWeather
Source0:        https://download.gnome.org/sources/libgweather/4.2/libgweather-%{version}.tar.xz

BuildRequires:  gobject-introspection-devel
BuildRequires:  intltool
BuildRequires:  meson >= 0.50.0
BuildRequires:  pkgconfig
BuildRequires:  python3-gobject
BuildRequires:  pkgconfig(geocode-glib-2.0)
BuildRequires:  pkgconfig(gi-docgen)
BuildRequires:  pkgconfig(gio-2.0) >= 2.68.0
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(libxml-2.0) >= 2.6.0
BuildRequires:  pkgconfig(vapigen)

%description
This is a library to download weather information from online sources.

%package -n gweather4-data
Summary:        Auxiliary schema data for libgweather
Group:          Development/Libraries/GNOME
Requires:       libgweather-4-0 = %{version}
Provides:       %{name} = %{version}

%description -n gweather4-data
This is a library to download weather information from online sources.
This package provides the architecture independent files.

%package devel
Summary:        Development files for libgweather, a weather info retrieval library
Group:          Development/Libraries/GNOME
Requires:       libgweather-4-0 = %{version}
Requires:       typelib-1_0-GWeather-4_0 = %{version}

%description devel
This is a library to download weather information from online sources.
This package provides the development files.

%package -n libgweather-4-0
Summary:        Library to get online weather information
Group:          Development/Libraries/GNOME
Requires:       gweather4-data >= %{version}

%description -n libgweather-4-0
This is a library to download weather information from online sources.

%package -n typelib-1_0-GWeather-4_0
Summary:        Introspection bindings for libgweather
Group:          System/Libraries

%description -n typelib-1_0-GWeather-4_0
This is a library to download weather information from online sources.

This package provides the GObject Introspection bindings for the
libgweather library.

%lang_package

%prep
%autosetup -p1 -n libgweather-%{version}

%build
%meson \
	-D enable_vala=true \
	-D gtk_doc=true \
	-D soup2=false \
	%{nil}
%meson_build

%install
%meson_install

%find_lang libgweather-4.0 %{?no_lang_C}
%find_lang libgweather-4.0-locations libgweather-4.0.lang %{?no_lang_C}

%ldconfig_scriptlets -n libgweather-4-0

%files -n gweather4-data
%{_datadir}/glib-2.0/schemas/org.gnome.GWeather4.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.GWeather4.gschema.xml
%{_datadir}/libgweather-4/
%dir %{_libdir}/libgweather-4
%{_libdir}/libgweather-4/Locations.bin

%files -n libgweather-4-0
%license COPYING
%{_libdir}/*.so.*

%files -n typelib-1_0-GWeather-4_0
%{_libdir}/girepository-1.0/GWeather-4.0.typelib

%files devel
%doc README.md NEWS
%{_datadir}/doc/libgweather-4.0/
%{_includedir}/libgweather-4.0
%{_libdir}/*.so
%{_libdir}/pkgconfig/gweather4.pc
%{_datadir}/gir-1.0/GWeather-4.0.gir
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/gweather4.deps
%{_datadir}/vala/vapi/gweather4.vapi

%files lang -f libgweather-4.0.lang

%changelog
