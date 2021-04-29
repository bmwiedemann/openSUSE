#
# spec file for package libSavitar
#
# Copyright (c) 2021 SUSE LLC
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


%define sover 0
Name:           libSavitar
%define sversion        4.9
Version:        4.9.0
Release:        0
Summary:        C++ implementation of 3mf loading with SIP python bindings
License:        LGPL-3.0-only
Group:          Development/Libraries/C and C++
URL:            https://github.com/Ultimaker/libSavitar
Source:         https://github.com/Ultimaker/libSavitar/archive/%{sversion}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE -- Use system libraries instead of embedded ones.
Patch0:         use-system-libs.patch
# PATCH-FIX-OPENSUSE - use Qt5 sip import name, taken from Fedora
Patch1:         libSavitar-3.5.1-PyQt5.sip.patch
BuildRequires:  cmake >= 2.8.12
BuildRequires:  gmock
BuildRequires:  gtest
BuildRequires:  pugixml-devel >= 1.8
BuildRequires:  python3-sip-devel < 5
%if 0%{?suse_version} >= 1550
BuildRequires:  python3-qt5-sip
%else
BuildRequires:  python3-sip
%endif

%description
libSavitar is a C++ implementation of 3mf loading with SIP python bindings.

%package -n %{name}%{sover}
Summary:        3D printer control software
Group:          System/Libraries
Provides:       python3-Savitar = %version
%if 0%{?suse_version} >= 1550
# The PyQt5.sip module. NOT a requirement on (Py)Qt5
Requires:       python3-qt5-sip
%else
# python3-sip provides PyQt5.sip in older distributions only
Requires:       python3-sip
%endif

%description -n %{name}%{sover}
libSavitar is a C++ implementation of 3mf loading with SIP python bindings.

%package devel
Summary:        Header files for libSavitar
Group:          Development/Libraries/C and C++
Requires:       %{name}%{sover} = %{version}
Requires:       python3-sip-devel < 5

%description devel
Development package for libSavitar.

%prep
%autosetup -p1 -n %{name}-%{sversion}

%build
%cmake -DUSE_SYSTEM_LIBS=TRUE \
       -DBUILD_TESTS=TRUE \
       -DLIB_SUFFIX=64
%cmake_build

%install
%cmake_install

%check
cd build
export LD_LIBRARY_PATH=$PWD
# we don't use "make test" to get the output on failure
/usr/bin/ctest --force-new-ctest-process --output-on-failure

%post   -n %{name}%{sover} -p /sbin/ldconfig
%postun -n %{name}%{sover} -p /sbin/ldconfig

%files devel
%{_includedir}/Savitar/
%{_libdir}/cmake/Savitar/
%{_libdir}/libSavitar.so

%files -n %{name}%{sover}
%license LICENSE
%doc README.md
%{_libdir}/libSavitar.so.*
%{python3_sitearch}/Savitar.so

%changelog
