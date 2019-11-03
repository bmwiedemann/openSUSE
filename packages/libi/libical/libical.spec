#
# spec file for package libical
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


%global flavor @BUILD_FLAVOR@%{nil}
%define sonum   3
%if "%{flavor}" == "glib"
%define name_ext -glib
%bcond_without glib
%else
%define name_ext %{nil}
%bcond_with glib
%endif
Name:           libical%{name_ext}
Version:        3.0.6
Release:        0
%if %{without glib}
Summary:        An Implementation of Basic iCAL Protocols
License:        MPL-2.0 OR LGPL-2.1-only
Group:          Development/Libraries/C and C++
%else
Summary:        GObject wrapper for libical library
License:        MPL-2.0 OR LGPL-2.1-only
Group:          Development/Libraries/C and C++
%endif
URL:            https://github.com/libical/libical
Source:         https://github.com/libical/libical/releases/download/v%{version}/libical-%{version}.tar.gz
Source2:        baselibs.conf
Source3:        libical-rpmlintrc
Patch1:         0001-vcc.y-factor-out-hexdigit-conversion.patch
Patch2:         0002-vcc.y-fix-infinite-loop-with-lower-case-hex-digits.patch
Patch3:         0003-vcc.y-fix-infinite-loop-with-non-hex-digits.patch
Patch4:         0004-vobject.c-vCard-Unicode-reading-support.patch
Patch5:         0005-vcc.y-do-not-ignore-field-separator-in-QUOTED-PRINTA.patch
BuildRequires:  cmake >= 3.1
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(icu-i18n)
%if %{with glib}
BuildRequires:  gtk-doc
BuildRequires:  vala
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(libical)
BuildRequires:  pkgconfig(libxml-2.0)
%endif

%if %{without glib}
%description -n libical
Libical is an implementation of the IETF's iCalendar
calendaring and scheduling protocols (RFC 2445, 2446, and 2447). It
parses iCal components and provides a C API for manipulating the
component properties, parameters, and subcomponents.
%else
%description -n libical-glib
This package provides a GObject wrapper for libical library with support
for GObject Introspection.
%endif

%package -n libical%{sonum}
Summary:        An Implementation of Basic iCAL Protocols
Group:          System/Libraries
Provides:       libical = %{version}
Obsoletes:      libical < %{version}

%description -n libical%{sonum}
Libical is an implementation of the IETF's iCalendar
calendaring and scheduling protocols (RFC 2445, 2446, and 2447). It
parses iCal components and provides a C API for manipulating the
component properties, parameters, and subcomponents.

%package -n libical-devel
Summary:        Development files for libical, an implementation of basic iCAL protocols
Group:          Development/Libraries/C and C++
Requires:       libical%{sonum} = %{version}
# Typelib should be required, but might create a build cycle
# Requires:      typelib-1_0-libical%%{sonum} = %%{version}

%description -n libical-devel
Libical is an implementation of the IETF's iCalendar
Calendaring and Scheduling protocols. (RFC 2445, 2446, and 2447). It
parses iCal components and provides a C API for manipulating the
component properties, parameters, and subcomponents.

%package -n libical-doc
Summary:        Example source code for programs to use libical
Group:          Documentation/Other
BuildArch:      noarch

%description -n libical-doc
Libical is an implementation of the IETF's iCalendar
calendaring and scheduling protocols (RFC 2445, 2446, and 2447). It
parses iCal components and provides a C API for manipulating the
component properties, parameters, and subcomponents.

%package -n libical-glib%{sonum}
Summary:        GObject wrapper for libical library
Group:          System/Libraries
Provides:       libical-glib = %{version}
Obsoletes:      libical-glib < %{version}

%description -n libical-glib%{sonum}
This package provides a GObject wrapper for libical library with support
for GObject Introspection.

%package -n libical-glib-devel
Summary:        Development files for building against libical-glib
Group:          Development/Libraries/C and C++
Requires:       libical-glib%{sonum} = %{version}
Requires:       typelib-1_0-ICal-3_0 = %{version}
Requires:       typelib-1_0-ICalGLib-3_0 = %{version}

%description -n libical-glib-devel
Development files for building against libical-glib%{sonum}

%package -n libical-glib-doc
Summary:        Documentation files for libical-glib%{sonum}
Group:          Documentation/Other
BuildArch:      noarch

%description -n libical-glib-doc
Documentation files for %{name}%{sonum}

%package -n typelib-1_0-ICal-3_0
Summary:        Introspection bindings for libical
Group:          Development/Libraries/C and C++

%description -n typelib-1_0-ICal-3_0
This package provides the gobject-introspection bindings for libical.

%package -n typelib-1_0-ICalGLib-3_0
Summary:        Introspection bindings for the libical glib bindings.
Group:          Development/Libraries/C and C++

%description -n typelib-1_0-ICalGLib-3_0
This package provides the gobject-introspection bindings for libical-glib.

%prep
%autosetup -p1 -n libical-%{version}

%build
%cmake \
  -DICAL_ALLOW_EMPTY_PROPERTIES=true \
%if %{with glib}
  -DICAL_GLIB=true \
  -DGOBJECT_INTROSPECTION=true \
  -DICAL_GLIB_VAPI=true \
%else
  -DICAL_GLIB=false \
%endif
  -DSHARED_ONLY=true
make -j1

%install
%cmake_install
rm examples/CMakeLists.txt
%if %{with glib}
rm -r %{buildroot}%{_includedir}/libical/
rm -r %{buildroot}%{_libdir}/cmake/LibIcal
rm %{buildroot}%{_libdir}/libical.so*
rm %{buildroot}%{_libdir}/libical_cxx.so*
rm %{buildroot}%{_libdir}/libicalss.so*
rm %{buildroot}%{_libdir}/libicalss_cxx.so*
rm %{buildroot}%{_libdir}/libicalvcal.so*
rm %{buildroot}%{_libdir}/pkgconfig/libical.pc
%endif

%if %{without glib}
%post -n %{name}%{sonum} -p /sbin/ldconfig
%postun -n %{name}%{sonum} -p /sbin/ldconfig
%else
%post -n %{name} -p /sbin/ldconfig
%postun -n %{name} -p /sbin/ldconfig
%endif

%if %{without glib}
%files -n %{name}%{sonum}
%license COPYING
%doc AUTHORS ReadMe.txt ReleaseNotes.txt TEST THANKS TODO
%{_libdir}/libical.so.*
%{_libdir}/libical_cxx.so.*
%{_libdir}/libicalss.so.*
%{_libdir}/libicalss_cxx.so.*
%{_libdir}/libicalvcal.so.*

%files devel
%{_libdir}/libical.so
%{_libdir}/libical_cxx.so
%{_libdir}/libicalss.so
%{_libdir}/libicalss_cxx.so
%{_libdir}/libicalvcal.so
%{_libdir}/pkgconfig/libical.pc
%{_libdir}/cmake/LibIcal/
%{_includedir}/libical/

%files doc
%doc doc/*.txt
%doc examples/
%else
%files -n %{name}%{sonum}
%{_libdir}/libical-glib.so.*

%files devel
%{_libdir}/libical-glib.so
%{_libdir}/pkgconfig/libical-glib.pc
%{_includedir}/libical-glib/
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/libical-glib.vapi
# This should really be in libical-devel
%{_datadir}/gir-1.0/ICal-3.0.gir
%{_datadir}/gir-1.0/ICalGLib-3.0.gir

%files doc
%{_datadir}/gtk-doc/html/libical-glib

%files -n typelib-1_0-ICal-3_0
%{_libdir}/girepository-1.0/ICal-3.0.typelib

%files -n typelib-1_0-ICalGLib-3_0
%{_libdir}/girepository-1.0/ICalGLib-3.0.typelib
%endif

%changelog
