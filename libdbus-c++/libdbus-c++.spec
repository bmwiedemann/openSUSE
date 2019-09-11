#
# spec file for package libdbus-c++
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define _rev e3455d20fc0b6e00bce7668fbd9b165fdc8a7040
%define sover 1
# Html documentation build causes cycles
%define buildoc 0

Name:           libdbus-c++
Version:        0.9.1+git20170322
Release:        0
Summary:        C++ Interface for DBus
License:        LGPL-2.1+
Group:          Development/Libraries/C and C++
Url:            http://dbus-cplusplus.sourceforge.net/index.html
#Source0:        http://sourceforge.net/projects/dbus-cplusplus/files/dbus-c%%2B%%2B/%%{version}/%%{name}-%%{version}.tar.gz
Source0:        https://github.com/andreas-volz/dbus-cplusplus/archive/%{_rev}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
# PATCH-FIX-UPSTREAM libdbus-c++-noreturn.patch davejplater@gmail.com -- Fix no return from function
Patch0:         libdbus-c++-noreturn.patch
# PATCH-FIX-UPSTREAM libdbus-c++-pthread.patch davejplater@gmail.com -- Get ffado to build with libdbus-c++
Patch1:         libdbus-c++-pthread.patch
# PATCH-FIX-OPENSUSE libdbus-c++-nodocdatetime.patch davejplater@gmail.com -- No current date / time allowed in docs?
Patch2:         libdbus-c++-nodocdatetime.patch
# PATCH-FIX-UPSTREAM libdbus-c++-glibmm-2.43.patch dimstar@opensuse.org -- Fix build with glibmm2 2.43.x+
Patch4:         libdbus-c++-glibmm-2.43.patch
# PATCH-FIX-UPSTREAM libdbus-c++-gcc7.patch davejplater@gmail.com -- Fix gcc7 build errors
Patch5:         libdbus-c++-gcc7.patch
# PATCH_FIX_OPENSUSE libdbus-c++-sover.patch davejplater@gmail.com -- Prevent errors due to symbol incompatability.
Patch6:         libdbus-c++-sover.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  gcc-c++
%if %{buildoc} == 1
BuildRequires:  doxygen
BuildRequires:  graphviz-gnome
%endif
BuildRequires:  gtkmm2-devel
BuildRequires:  libexpat-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dbus-glib-1)
# ecore
BuildRequires:  libexpat-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
DBus-c++ provides a C++ API for D-BUS. The library has
a glib and an ecore mainloop integration. It also offers an
optional own main loop.

%package -n libdbus-c++-1-%{sover}
Summary:        C++ Interface for D-Bus
Group:          System/Libraries

%description -n libdbus-c++-1-%{sover}
DBus-c++ provides a C++ API for D-BUS. The library has
a glib and an ecore mainloop integration. It also offers an
optional own main loop. The libdbus-c++ library.

%package -n libdbus-c++-glib-1-%{sover}
Summary:        Glib integration for libdbus-c++
Group:          System/Libraries

%description -n libdbus-c++-glib-1-%{sover}
DBus-c++ provides a C++ API for D-BUS. The library has
a glib and an ecore mainloop integration. It also offers an
optional own main loop. The glib libdbus-c++ library.

%package devel
Summary:        Development files for libdbus-c++
Group:          Development/Libraries/C and C++
Requires:       libdbus-c++-1-%{sover} = %{version}
Requires:       libdbus-c++-glib-1-%{sover} = %{version}

%description devel
DBus-c++ provides a C++ API for D-BUS. The library has
a glib and an ecore mainloop integration. It also offers an
optional own main loop.
This subpackage contains the files needed for building against
libdbus-c++.

%prep
%setup -q -n dbus-cplusplus-%{_rev}
#-n dbus-cplusplus-%%{_rev}
%patch0
%patch1
%patch2
%patch4 -p1
%patch5
%patch6

%build
export SOVER="%{sover}:0:0"
#%%{sover}
# --enable-doxygen-docs  -fpermissive
./bootstrap
#./autogen.sh
%if 1 == 0
%define gcc_version 7
export CC=gcc-7
export CPP=cpp-7
export CXX=g++-7
%endif
export LDFLAGS="$LDFLAGS -lexpat -lpthread"
%if 0%{?gcc_version} > 5
export CXXFLAGS="%{optflags} --std=c++11 -fPIC -Werror=date-time"
%else
export CXXFLAGS="%{optflags} --std=c++11 -fPIC"
%endif
%configure --disable-ecore --enable-static=no \
%if %{buildoc} == 1
	   --enable-doxygen-docs \
%else
           --disable-doxygen-docs \
%endif
           --enable-tests \
	   --enable-examples
make %{?_smp_mflags}

%install
%make_install
dos2unix -k AUTHORS
rm -f %{buildroot}%{_libdir}/*.la
%if %{buildoc} == 1
%fdupes -s doc/
%endif

%post -n libdbus-c++-glib-1-%{sover} -p /sbin/ldconfig

%postun -n libdbus-c++-glib-1-%{sover} -p /sbin/ldconfig

%post -n libdbus-c++-1-%{sover} -p /sbin/ldconfig

%postun -n libdbus-c++-1-%{sover} -p /sbin/ldconfig

%files -n libdbus-c++-1-%{sover}
%defattr(755,root,root)
%{_libdir}/libdbus-c++-1.so.%{sover}
%{_libdir}/libdbus-c++-1.so.%{sover}.0.0

%files -n libdbus-c++-glib-1-%{sover}
%defattr(755,root,root)
%{_libdir}/libdbus-c++-glib-1.so.%{sover}
%{_libdir}/libdbus-c++-glib-1.so.%{sover}.0.0

# TODO: Separate the two lib's devel packages. There's only one set of headers though.
# FIXME: Every html file contains date and time, must be fixed before docs are included.
# FIXME: Add this to %%doc when fixed "doc/html doc/img" maybe a separate doc package.

%files devel
%defattr(-,root,root)
%if %{buildoc} == 1
%doc AUTHORS COPYING README TODO doc/html doc/img
%else
%doc AUTHORS COPYING README TODO
%endif

%{_bindir}/dbusxx-xml2cpp
%{_bindir}/dbusxx-introspect
%{_libdir}/libdbus-c++-1.so
%{_libdir}/libdbus-c++-glib-1.so
%{_includedir}/dbus-c++-1
%{_libdir}/pkgconfig/*.pc
# doc/html doc/img

%changelog
