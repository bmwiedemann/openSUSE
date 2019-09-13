#
# spec file for package libmodman
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2010 Dominique Leuenberger, Amsterdam, The Netherlands.
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


%if 0%{?build_snapshot}
%define _sourcename %{name}
%else
%define _sourcename %{name}-%{version}
%endif
Name:           libmodman
Version:        2.0.1
Release:        0
Summary:        A Module Management Library
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Source:         http://libmodman.googlecode.com/files/%{_sourcename}.tar.bz2
# Script used for automatic update of snapshot packages
Source98:       update-from-svn.sh
Source99:       baselibs.conf
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel

%description
The Module Loading library offers the choice to use prelinked libraries
from your application out of a pool.

%package -n libmodman1
Summary:        A Module Management Library
Group:          System/Libraries

%description -n libmodman1
The Module Loading library offers the choice to use prelinked libraries
from your application out of a pool.

%package devel
Summary:        Development files for libmodman, a module management library
Group:          Development/Languages/C and C++
Requires:       libmodman1 = %{version}

%description devel
The Module Loading library offers the choice to use prelinked libraries
from your application out of a pool.

This package is needed to develop applications using libmodman.

%prep
%setup -q -n %{_sourcename}
mkdir build

%build
export CXXFLAGS="%{optflags}"
%if 0%{?windows}
export CXXFLAGS="${CXXFLAGS} -fno-stack-protector -static-libgcc -static"
%endif

cd build
# FIXME: you should use %%cmake macros
cmake \
%if 0%{?windows}
  -DCMAKE_TOOLCHAIN_FILE=../cmake/mingw32.cmake \
  -DBUILD_TESTING=False \
%endif
  -DCMAKE_INSTALL_PREFIX=%{_prefix} \
  -DLIB_INSTALL_DIR=%{_libdir} \
  -DSHARE_INSTALL_PREFIX=%{_datadir} \
  -DINCLUDE_INSTALL_DIR=%{_includedir} \
..
make %{?_smp_mflags} VERBOSE=1

%install
cd build
%make_install

%check
cd build
make %{?_smp_mflags} test

%post -n libmodman1 -p /sbin/ldconfig
%postun -n libmodman1 -p /sbin/ldconfig

%files -n libmodman1
%if !0%{?windows}
%{_libdir}/libmodman.so.*
%else
%{_libdir}/libmodman.dll
%endif

%files devel
%if !0%{?windows}
%{_includedir}/libmodman
%{_libdir}/libmodman.so
%{_libdir}/pkgconfig/libmodman-2.0.pc
%{_datadir}/cmake/Modules/Findlibmodman.cmake
%else
%{_libdir}/libmodman.dll.a
%{_includedir}/libmodman
%endif

%changelog
