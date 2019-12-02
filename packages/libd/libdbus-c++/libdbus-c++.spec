#
# spec file for package libdbus
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

%if "%{flavor}" == "glib"
%bcond_with    docs
%bcond_without glib
%global psuffix -glib
%endif

%if "%{flavor}" == "docs"
%bcond_without docs
%bcond_with    glib
%global psuffix -api-docs
%endif

%if "%{flavor}" == ""
%bcond_with docs
%bcond_with glib
%endif

%define sname libdbus-c++

%define _rev e3455d20fc0b6e00bce7668fbd9b165fdc8a7040
%define sover 1

Name:           libdbus-c++%{?psuffix}
Version:        0.9.1+git20170322
Release:        0
Summary:        C++ Interface for DBus
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            http://dbus-cplusplus.sourceforge.net/index.html
#Source0:        http://sourceforge.net/projects/dbus-cplusplus/files/dbus-c%%2B%%2B/%%{version}/%%{name}-%%{version}.tar.gz
Source0:        https://github.com/andreas-volz/dbus-cplusplus/archive/%{_rev}.tar.gz#/%{sname}-%{version}.tar.gz
Source1:        baselibs.conf
# PATCH-FIX-UPSTREAM libdbus-c++-noreturn.patch davejplater@gmail.com -- Fix no return from function
Patch0:         libdbus-c++-noreturn.patch
# PATCH-FIX-UPSTREAM libdbus-c++-pthread.patch davejplater@gmail.com -- Get ffado to build with libdbus-c++
Patch1:         libdbus-c++-pthread.patch
# PATCH-FIX-UPSTREAM libdbus-c++-glibmm-2.43.patch dimstar@opensuse.org -- Fix build with glibmm2 2.43.x+
Patch4:         libdbus-c++-glibmm-2.43.patch
# PATCH-FIX-UPSTREAM libdbus-c++-gcc7.patch davejplater@gmail.com -- Fix gcc7 build errors
Patch5:         libdbus-c++-gcc7.patch
# PATCH_FIX_OPENSUSE libdbus-c++-sover.patch davejplater@gmail.com -- Prevent errors due to symbol incompatability.
Patch6:         libdbus-c++-sover.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  dos2unix
BuildRequires:  gcc-c++
%if %{with docs}
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  graphviz-gnome
%endif
%if %{with glib}
BuildRequires:  gtkmm2-devel
BuildRequires:  pkgconfig(dbus-glib-1)
%endif
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(dbus-1)
# ecore
BuildRequires:  libexpat-devel
%if "%{flavor}" == "docs"
BuildArch:      noarch
%endif

%description
DBus-c++ provides a C++ API for D-BUS. The library has
a glib and an ecore mainloop integration. It also offers an
optional own main loop.

%package -n libdbus-c++%{?psuffix}-1-%{sover}
Summary:        C++ Interface for D-Bus
Group:          System/Libraries

%description -n libdbus-c++%{?psuffix}-1-%{sover}
DBus-c++ provides a C++ API for D-BUS. The library has
a glib and an ecore mainloop integration. It also offers an
optional own main loop.

%package devel
Summary:        Development files for libdbus-c++
Group:          Development/Libraries/C and C++
Requires:       libdbus-c++%{?psuffix}-1-%{sover} = %{version}
Recommends:     libdbus-c++-api-docs
Conflicts:      libdbus-c++-devel < %{version}-%{release}
%if 0%{?suse_version} <= 1500
%if %{with glib}
Requires:       libdbus-c++-devel = %{version}-%{release}
%endif
%endif

%description devel
DBus-c++ provides a C++ API for D-BUS. The library has
a glib and an ecore mainloop integration. It also offers an
optional own main loop.
This subpackage contains the files needed for building against
libdbus-c++.

%prep
%setup -q -n dbus-cplusplus-%{_rev}
%patch0
%patch1
%patch4 -p1
%patch5
%patch6

%build
export SOVER="%{sover}:0:0"
export LDFLAGS="$LDFLAGS -lexpat -lpthread -pie"
export CFLAGS="%{optflags} -fPIC"
export CXXFLAGS="%{optflags} --std=c++11 -fPIC"
./bootstrap
%configure \
        --disable-ecore \
        --enable-static=no \
%if %{without glib}
        --disable-glib \
%endif
%if %{with docs}
        --enable-doxygen-docs \
%else
        --disable-doxygen-docs \
        --enable-tests \
        --enable-examples
%endif

%if "%{flavor}" == "docs"
make %{?_smp_mflags} -C doc
%else
make %{?_smp_mflags}
%endif

%install
%if "%{flavor}" == "docs"
%fdupes -s doc/

%else
%make_install
dos2unix -k AUTHORS
rm -f %{buildroot}%{_libdir}/*.la

# Remove files packaged in the base flavor
%if "%{flavor}" == "glib"
rm %{buildroot}%{_bindir}/*
rm -Rf %{buildroot}%{_includedir}
rm -Rf %{buildroot}%{_libdir}/libdbus-c++-1.so*
rm -Rf %{buildroot}%{_libdir}/pkgconfig/dbus-c++-1.pc
%endif
%endif

%post -n libdbus-c++%{?psuffix}-1-%{sover} -p /sbin/ldconfig
%postun -n libdbus-c++%{?psuffix}-1-%{sover} -p /sbin/ldconfig

%if "%{flavor}" == "docs"
%files
%doc doc/html doc/img
%else

%files -n libdbus-c++%{?psuffix}-1-%{sover}
%{_libdir}/libdbus-c++%{?psuffix}-1.so.%{sover}*

%files devel
%if "%{flavor}" == ""
%license COPYING
%doc AUTHORS README TODO
%{_bindir}/dbusxx-xml2cpp
%{_bindir}/dbusxx-introspect
%{_includedir}/dbus-c++-1
%endif

%{_libdir}/libdbus-c++%{?psuffix}-1.so
%{_libdir}/pkgconfig/*%{?psuffix}*.pc
%endif

%changelog
