#
# spec file for package verdict
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


%define libname libverdict1_4

Name:           verdict
Version:        1.4.1
Release:        0
Summary:        Compute quality functions of 2 and 3-dimensional regions
License:        BSD-3-Clause
URL:            https://github.com/sandialabs/verdict
Source:         https://github.com/sandialabs/verdict/archive/refs/tags/%{version}.tar.gz#/verdict-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gtest

%description
Verdict is a library for evaluating the geometric qualities of regions of space.

%package -n %{libname}
Summary:        Verdict library for evaluating the geometric qualities of regions of space
Group:          System/Libraries

%description -n %{libname}
Verdict is a library for evaluating the geometric qualities of regions of space.

%package devel
Summary:        Verdict header files
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
This package contains the header files and cmake config files.

%prep
%setup

%build
%cmake \
  -DCMAKE_SKIP_RPATH:BOOL=OFF \
  -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON \
  -DVERDICT_ENABLE_TESTING:BOOL=ON \
  -DCMAKE_INSTALL_DOCDIR=%{_docdir} \
  %{nil}
%cmake_build

%install
%cmake_install
rm -vrf %{buildroot}/%{_docdir}

%check
%ifarch %{ix86}
# https://github.com/sandialabs/verdict/issues/3
export GTEST_FILTER=:-verdict.hex_test3_flat
%endif
%ctest

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license LICENSE
%{_libdir}/lib*so.*

%files devel
%doc README.md
%{_includedir}/verdict*.h
%{_libdir}/lib*so
%{_libdir}/cmake/verdict

%changelog
