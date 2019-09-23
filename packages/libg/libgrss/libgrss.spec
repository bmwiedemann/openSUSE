#
# spec file for package libgrss
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           libgrss
Version:        0.7.0
Release:        0
Summary:        Library for management of RSS/Atom/Pie feeds
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://wiki.gnome.org/Projects/Libgrss
Source:         http://download.gnome.org/sources/libgrss/0.7/%{name}-%{version}.tar.xz
BuildRequires:  intltool >= 0.40.6
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gobject-2.0) >= 2.30.2
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(libsoup-2.4) >= 2.48.0
BuildRequires:  pkgconfig(libxml-2.0) >= 2.9.2

%description
LibGRSS is a library for management of RSS/Atom/Pie feeds.

%package -n libgrss0
Summary:        Library for management of RSS/Atom/Pie feeds
Group:          System/Libraries

%description -n libgrss0
LibGRSS is a library for management of RSS/Atom/Pie feeds.

%package -n typelib-1_0-Grss-0_7
Summary:        Introspection bindings for libgrss, a RSS/Atom/Pie feed management library
Group:          System/Libraries

%description -n typelib-1_0-Grss-0_7
LibGRSS is a library for management of RSS/Atom/Pie feeds.
This package provides the GObject Introspection bindings for the
libgrss library.

%package devel
Summary:        Development files for libgrss, a RSS/Atom/Pie feed management library
Group:          Development/Libraries/GNOME
Requires:       libgrss0 = %{version}

%description devel
LibGRSS is a library for management of RSS/Atom/Pie feeds.
This package provides the headers for it.

%prep
%setup -q

%build
%configure \
    --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libgrss0 -p /sbin/ldconfig
%postun -n libgrss0 -p /sbin/ldconfig

%files -n libgrss0
%license COPYING
%doc NEWS README
%{_libdir}/libgrss.so.*

%files -n typelib-1_0-Grss-0_7
%{_libdir}/girepository-1.0/Grss-0.7.typelib

%files devel
%doc %{_datadir}/gtk-doc/html/libgrss/
%{_datadir}/gir-1.0/Grss-0.7.gir
%{_includedir}/libgrss/
%{_libdir}/libgrss.so
%{_libdir}/pkgconfig/libgrss.pc

%changelog
