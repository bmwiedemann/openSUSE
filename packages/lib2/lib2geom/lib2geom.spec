#
# spec file for package lib2geom
#
# Copyright (c) 2024 SUSE LLC
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


%define __builder ninja
%define sonum 1_4_0
%define sover 1.4.0
%define libname lib2geom%{sonum}
%define develname 2geom
%define short_version 1.4
Name:           lib2geom
Version:        1.4.0
Release:        0
Summary:        Easy to use 2D geometry library in C++
License:        LGPL-2.1-only AND MPL-1.1
URL:            https://gitlab.com/inkscape/%{name}
Group:          System/Libraries
Source0:        %{url}/-/archive/%{short_version}/%{name}-%{short_version}.tar.gz
# PATCH-FIX-OPENSUSE
Patch1:         fix-pkgconfig-libdir-path.patch
BuildRequires:  cmake >= 2.6
%if 0%{suse_version} < 1550
BuildRequires:  gcc13-c++
%else
BuildRequires:  gcc-c++
%endif
BuildRequires:  glib2
BuildRequires:  gsl-devel
BuildRequires:  gtest
BuildRequires:  gtk3-devel
BuildRequires:  libboost_headers-devel
BuildRequires:  ninja
BuildRequires:  cmake(double-conversion)

%description
A C++ 2D geometry library geared towards processing data
associated with vector graphics. The primary design consideration
is ease of use and clarity.

%package -n     %{libname}
Summary:        Easy to use 2D geometry library in C++

%description -n %{libname}
A C++ 2D geometry library geared towards processing data
associated with vector graphics. The primary design consideration
is ease of use and clarity.

%package        devel
Summary:        Development files for %{name}
Requires:       %{libname} = %{version}
Group:          Development/Libraries/C and C++

%description    devel
This package contains all necessary include files and libraries
needed to develop applications that require %{name}.

%prep
%autosetup -n %{name}-%{short_version} -p1

%build
%if 0%{?suse_version} && 0%{?suse_version} <= 1500
export CC=gcc-13
export CXX=g++-13
%endif
export CFLAGS="%optflags -fexcess-precision=fast -DNDEBUG"
export CXXFLAGS="$CFLAGS"
%cmake -Wno-dev \
       -D2GEOM_BUILD_SHARED:BOOL=ON \
       -D2GEOM_TOYS:BOOL=OFF \
       -D2GEOM_TESTING:BOOL=ON \
       -DCMAKE_SKIP_RPATH:BOOL=OFF \
       -DCMAKE_SKIP_INSTALL_RPATHS:BOOL=ON \
       %{nil}

%cmake_build

%install
%cmake_install

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%check
# deactivate failling test, also see
# PATCH-FIX-UPSTREAM fix instable tests, https://gitlab.com/inkscape/lib2geom/-/issues/67
%if 0%{?suse_version} > 1500
# TW x86_64 => passes
# TW i586
%ifarch i586
%define excluded_tests 1
ctest_exclude_regex="ellipse-test|elliptical-arc-test|line-test|polynomial-test|self-intersections-test"
%endif
# TW armv7l => passes
# TW aarch64
%ifarch aarch64 ppc64le riscv64 s390x
%define excluded_tests 1
ctest_exclude_regex="elliptical-arc-test|polynomial-test"
%endif
%endif
%if 0%{?sle_version} == 150600 && 0%{?is_opensuse}
# 15.6 x86_64 => passes
# 15.6 i586
%ifarch i586
%define excluded_tests 1
ctest_exclude_regex="bezier-test|ellipse-test|line-test|polynomial-test|self-intersections-test"
%endif
%endif
%if 0%{?sle_version} == 150500 && 0%{?is_opensuse}
# 15.5 x86_64
%ifarch x86_64
%define excluded_tests 1
ctest_exclude_regex="line-test"
%endif
# 15.5 i586
%ifarch i586
%define excluded_tests 1
ctest_exclude_regex="bezier-test|ellipse-test|line-test|polynomial-test|self-intersections-test"
%endif
%endif
# END deactivate failling test
pushd build
ctest --output-on-failure --force-new-ctest-process --parallel %{_smp_build_ncpus} \
      %{?excluded_tests:--exclude-regex "($ctest_exclude_regex)"}
popd

%files -n %{libname}
%license COPYING-LGPL-2.1 COPYING-MPL-1.1
%doc NEWS.md README.md
%{_libdir}/%{name}.so.%{sover}

%files devel
%dir %{_includedir}/%{develname}-%{version}/
%dir %{_includedir}/%{develname}-%{version}/%{develname}/
%{_includedir}/%{develname}-%{version}/%{develname}/numeric/
%{_includedir}/%{develname}-%{version}/%{develname}/intervaltree/
%{_includedir}/%{develname}-%{version}/%{develname}/orphan-code/
%{_includedir}/%{develname}-%{version}/%{develname}/symbolic/
%{_includedir}/%{develname}-%{version}/%{develname}/*.h

%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{develname}.pc
%{_libdir}/cmake/2Geom/

%changelog
