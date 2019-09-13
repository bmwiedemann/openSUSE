#
# spec file for package gflags
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           gflags
Version:        2.2.1
Release:        0
Summary:        Library for commandline flag processing
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://github.com/gflags/gflags
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
Requires:       libgflags2 = %{version}

%description
The gflags package contains a library that implements commandline
flags processing. As such, it is a replacement for getopt(). It has
increased flexibility, including built-in support for C++ types like
string, and the ability to define flags in the source file in which
they're used.

%package -n libgflags2
Summary:        Library for commandline flag processing
Group:          System/Libraries

%description -n libgflags2
The gflags package contains a library that implements commandline
flags processing. As such, it is a replacement for getopt(). It has
increased flexibility, including built-in support for C++ types like
string, and the ability to define flags in the source file in which
they're used.

%package devel
Summary:        Development files for gflags library
Group:          Development/Libraries/C and C++
Requires:       libgflags2 = %{version}

%description devel
This package contains headers and build system meta files.

%package devel-static
Summary:        Statically linked development libraries for gflags
Group:          Development/Libraries/C and C++
Requires:       %{name}-devel = %{version}

%description devel-static
This package contains the static libraries for gflags.

%prep
%setup -q

%build
CFLAGS="%{optflags} -pthread"
CXXFLAGS="%{optflags} -pthread"
export CFLAGS CXXFLAGS

%cmake \
	-DBUILD_STATIC_LIBS:BOOL=ON \
	-DBUILD_TESTING:BOOL=ON \
	-DCMAKE_BUILD_TYPE=Release

make %{?_smp_mflags} VERBOSE=1

%install
%cmake_install

# Installs a file on $HOME, remove it
rm -rf %{buildroot}/home/

%check
export LD_LIBRARY_PATH=`pwd`/build/lib
%ctest

%post -n libgflags2 -p /sbin/ldconfig
%postun -n libgflags2 -p /sbin/ldconfig

%files
%license COPYING.txt
%doc AUTHORS.txt ChangeLog.txt README.md
%{_bindir}/%{name}_completions.sh

%files -n libgflags2
%license COPYING.txt
%{_libdir}/libgflags.so.*
%{_libdir}/libgflags_nothreads.so.*

%files devel
%{_includedir}/%{name}/
%{_libdir}/libgflags.so
%{_libdir}/libgflags_nothreads.so
%{_libdir}/cmake/%{name}/
%{_libdir}/pkgconfig/%{name}.pc

%files devel-static
%{_libdir}/libgflags.a
%{_libdir}/libgflags_nothreads.a

%changelog
