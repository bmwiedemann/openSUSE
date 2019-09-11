#
# spec file for package flann
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


%define sover   1_9
Name:           flann
Version:        1.9.1
Release:        0
Summary:        Fast Library for Approximate Nearest Neighbors
License:        BSD-3-Clause
Group:          Productivity/Scientific/Other
Url:            https://www.cs.ubc.ca/research/flann/
Source0:        https://github.com/mariusmuja/flann/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         0001-src-cpp-fix-cmake-3.11-build.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  googletest-devel
BuildRequires:  hdf5-devel
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(zlib)

%description
FLANN is a library for performing fast approximate nearest neighbor 
searches in high dimensional spaces.

%package -n     lib%{name}%{sover}
Summary:        C++ library for %{name}
Group:          System/Libraries
Provides:       lib%{name}_cpp%{sover} = %{version}

%description -n lib%{name}%{sover}
FLANN is a library for performing fast approximate nearest neighbor 
searches in high dimensional spaces.

This package contains the shared library.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{sover} = %{version}

%description    devel
Fast Library for Approximate Nearest Neighbors.

This package contains the header files and libraries needed to develop
application that use %{name}.

%prep
%setup -q
%patch0 -p1

%build
%cmake \
    -DFLANN_LIB_INSTALL_DIR="%{_lib}" \
    -DBUILD_MATLAB_BINDINGS=OFF \
    -DBUILD_PYTHON_BINDINGS=OFF \
    -DBUILD_EXAMPLES=OFF \
    -DBUILD_DOC=OFF

%make_jobs 

%install
%cmake_install

find %{buildroot} -type f -name \*.a -delete -print

%post -n lib%{name}%{sover} -p /sbin/ldconfig
%postun -n lib%{name}%{sover} -p /sbin/ldconfig

%files -n lib%{name}%{sover}
%doc ChangeLog
%license COPYING
%{_libdir}/lib%{name}*so.*

%files devel
%{_includedir}/%{name}/
%{_libdir}/lib%{name}*so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
