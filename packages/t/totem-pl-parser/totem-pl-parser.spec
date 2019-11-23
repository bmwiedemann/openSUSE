#
# spec file for package totem-pl-parser
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define sover   18

Name:           totem-pl-parser
Version:        3.26.4
Release:        0
Summary:        A GObject-based library to parse playlist formats
License:        LGPL-2.0-or-later AND GPL-2.0-or-later
Group:          Productivity/Multimedia/Video/Players
URL:            http://www.gnome.org/projects/totem/
#Source0:       http://download.gnome.org/sources/totem-pl-parser/3.26/%%{name}-%%{version}.tar.xz
Source:         %{name}-%{version}.tar.xz

BuildRequires:  gtk-doc
BuildRequires:  intltool
BuildRequires:  libgcrypt-devel
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  translation-update-upstream
BuildRequires:  pkgconfig(glib-2.0) >= 2.31.0
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(libarchive) >= 3.0
BuildRequires:  pkgconfig(libquvi-0.9) >= 0.9.1
BuildRequires:  pkgconfig(libxml-2.0)
Requires:       libquvi-scripts
Recommends:     %{name}-lang

%description
totem-pl-parser is a GObject-based library to parse a host of
playlist formats, to save them too.

%package -n libtotem-plparser%{sover}
Summary:        A GObject-based library to parse playlist formats
# Main package contains libexec files needed for full functionality
Group:          System/Libraries
Requires:       %{name} >= %{version}

%description -n libtotem-plparser%{sover}
totem-pl-parser is a GObject-based library to parse a host of
playlist formats, to save them too.

%package -n typelib-1_0-TotemPlParser-1_0
Summary:        Introspection bindings for the Totem playlist parser library
# Main package contains libexec files needed for full functionality
Group:          System/Libraries
Requires:       %{name} >= %{version}

%description -n typelib-1_0-TotemPlParser-1_0
totem-pl-parser is a GObject-based library to parse a host of
playlist formats, to save them too.

This package provides the GObject Introspection bindings for the
totem-pl-parser library.

%package -n libtotem-plparser-mini%{sover}
Summary:        Mini version of the Totem playlist parser library
# Main package contains libexec files needed for full functionality
Group:          System/Libraries
Requires:       %{name} >= %{version}

%description -n libtotem-plparser-mini%{sover}
totem-pl-parser is a GObject-based library to parse a host of
playlist formats, to save them too.

%package devel
Summary:        Development files for the Totem playlist parser library
Group:          Development/Libraries/GNOME
Requires:       libtotem-plparser%{sover} = %{version}
Requires:       libtotem-plparser-mini%{sover} = %{version}
Requires:       typelib-1_0-TotemPlParser-1_0 = %{version}

%description devel
totem-pl-parser is a GObject-based library to parse a host of
playlist formats, to save them too.

%lang_package

%prep
%autosetup
translation-update-upstream

%build
%meson \
        -D enable-quvi=yes \
        -D enable-libarchive=yes \
        -D enable-libgcrypt=yes \
        -D enable-gtk-doc=true \
        %{nil}
%meson_build

%install
%meson_install
%find_lang %{name}

%post   -n libtotem-plparser%{sover} -p /sbin/ldconfig
%postun -n libtotem-plparser%{sover} -p /sbin/ldconfig

%post   -n libtotem-plparser-mini%{sover} -p /sbin/ldconfig
%postun -n libtotem-plparser-mini%{sover} -p /sbin/ldconfig

%files
%dir %{_libexecdir}/totem-pl-parser/
%{_libexecdir}/totem-pl-parser/99-totem-pl-parser-videosite

%files -n libtotem-plparser%{sover}
%license COPYING.LIB
%{_libdir}/libtotem-plparser.so.*

%files -n typelib-1_0-TotemPlParser-1_0
%{_libdir}/girepository-1.0/TotemPlParser-1.0.typelib

%files -n libtotem-plparser-mini%{sover}
%{_libdir}/libtotem-plparser-mini.so.*

%files devel
%{_includedir}/totem-pl-parser/
%{_libdir}/libtotem-plparser.so
%{_libdir}/libtotem-plparser-mini.so
%{_libdir}/pkgconfig/totem-plparser.pc
%{_libdir}/pkgconfig/totem-plparser-mini.pc
%{_datadir}/gir-1.0/*.gir
%doc %{_datadir}/gtk-doc/html/totem-pl-parser/

%files lang -f %{name}.lang

%changelog
