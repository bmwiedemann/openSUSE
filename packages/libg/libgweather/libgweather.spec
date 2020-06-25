#
# spec file for package libgweather
#
# Copyright (c) 2020 SUSE LLC
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


Name:           libgweather
Version:        3.36.1
Release:        0
Summary:        Library to get online weather information
License:        GPL-2.0-or-later
Group:          Development/Libraries/GNOME
URL:            https://wiki.gnome.org/Projects/LibGWeather
Source0:        https://download.gnome.org/sources/libgweather/3.36/%{name}-%{version}.tar.xz
Source99:       baselibs.conf

BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  intltool
BuildRequires:  meson >= 0.50.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(geocode-glib-1.0)
BuildRequires:  pkgconfig(gio-2.0) >= 2.44.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.13.5
BuildRequires:  pkgconfig(libsoup-2.4) >= 2.44.0
BuildRequires:  pkgconfig(libxml-2.0) >= 2.6.0
BuildRequires:  pkgconfig(vapigen)

%description
This is a library to download weather information from online sources.

%package -n gweather-data
Summary:        Auxiliary schema data for libgweather
Group:          Development/Libraries/GNOME
Requires:       libgweather-3-16 = %{version}
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}
Provides:       libgweather-data = %{version}
Obsoletes:      libgweather-data < %{version}
BuildArch:      noarch

%description -n gweather-data
This is a library to download weather information from online sources.
This package provides the architecture independent files.

%package devel
Summary:        Development files for libgweather, a weather info retrieval library
Group:          Development/Libraries/GNOME
Requires:       libgweather-3-16 = %{version}
Requires:       typelib-1_0-GWeather-3_0 = %{version}

%description devel
This is a library to download weather information from online sources.
This package provides the development files.

%package -n libgweather-3-16
Summary:        Library to get online weather information
Group:          Development/Libraries/GNOME
Requires:       gweather-data >= %{version}

%description -n libgweather-3-16
This is a library to download weather information from online sources.

%package -n typelib-1_0-GWeather-3_0
Summary:        Introspection bindings for libgweather
Group:          System/Libraries

%description -n typelib-1_0-GWeather-3_0
This is a library to download weather information from online sources.

This package provides the GObject Introspection bindings for the
libgweather library.

%lang_package

%prep
%autosetup -p1

%build
%meson \
	-Dglade_catalog=false \
	-Denable_vala=true \
	-Dgtk_doc=true \
	%{nil}
%meson_build

%install
%meson_install

%find_lang libgweather-3.0 %{?no_lang_C}
%find_lang libgweather-locations libgweather-3.0.lang %{?no_lang_C}

%post -n libgweather-3-16 -p /sbin/ldconfig
%postun -n libgweather-3-16 -p /sbin/ldconfig

%files -n gweather-data
%{_datadir}/glib-2.0/schemas/org.gnome.GWeather.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.GWeather.gschema.xml
%{_datadir}/libgweather/

%files -n libgweather-3-16
%license COPYING
%{_libdir}/*.so.*

%files -n typelib-1_0-GWeather-3_0
%{_libdir}/girepository-1.0/GWeather-3.0.typelib

%files devel
%doc AUTHORS HACKING MAINTAINERS README README.md NEWS
%doc %{_datadir}/gtk-doc/html/libgweather
%{_includedir}/libgweather-3.0
%{_libdir}/*.so
%{_libdir}/pkgconfig/gweather-3.0.pc
%{_datadir}/gir-1.0/GWeather-3.0.gir
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/gweather-3.0.deps
%{_datadir}/vala/vapi/gweather-3.0.vapi

%files lang -f %{name}-3.0.lang

%changelog
