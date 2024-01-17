#
# spec file for package flann
#
# Copyright (c) 2022 SUSE LLC
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
Version:        1.9.2
Release:        0
Summary:        Fast Library for Approximate Nearest Neighbors
License:        BSD-3-Clause
Group:          Productivity/Scientific/Other
URL:            https://www.cs.ubc.ca/research/flann/
Source:         https://github.com/tkircher/flann/releases/download/%version/flann-%version.tar.xz
# PATCH-FIX-UPSTREAM
Patch0:         https://github.com/tkircher/flann/commit/c9572a40574c18a79e50b6a8c0043a8cafed6e69.patch#/fix_lz4_linkage.patch
# PATCH-FIX-UPSTREAM
Patch1:         0001-Cleanup-library-build-make-static-library-optional.patch
# PATCH-FIX-UPSTREAM
Patch2:         0001-Fix-LZ4_LDFLAGS-format-for-pkgconfig-file.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  googletest-devel
BuildRequires:  hdf5-devel
BuildRequires:  liblz4-devel
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(zlib)

%description
FLANN is a library for performing approximate nearest neighbor
searches in high dimensional spaces.

%package -n     lib%{name}%{sover}
Summary:        Fast Library for Approximate Nearest Neighbors
Group:          System/Libraries
Provides:       lib%{name}_cpp%{sover} = %{version}

%description -n lib%{name}%{sover}
FLANN is a library for performing approximate nearest neighbor
searches in high dimensional spaces.

This package contains the shared library.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{sover} = %{version}
Requires:       liblz4-devel

%description    devel
Fast Library for Approximate Nearest Neighbors.

This package contains the header files and libraries needed to develop
application that use %{name}.

%prep
%autosetup -p1
# Correct install path for CMake config
sed -i -e 's@\(set(config_install_dir\).*)@\1 "%{_libdir}/cmake/flann")@' CMakeLists.txt

%build
%cmake \
    -DFLANN_LIB_INSTALL_DIR="%{_lib}" \
    -DBUILD_MATLAB_BINDINGS=OFF \
    -DBUILD_PYTHON_BINDINGS=OFF \
    -DBUILD_EXAMPLES=OFF \
    -DBUILD_DOC=OFF

%cmake_build

%install
%cmake_install

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
%{_libdir}/cmake/flann

%changelog
