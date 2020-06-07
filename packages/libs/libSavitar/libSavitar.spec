#
# spec file for package libSavitar
#
# Copyright (c) 2020 SUSE LLC
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
Version:        4.6.1
Release:        0
Summary:        C++ implementation of 3mf loading with SIP python bindings
License:        LGPL-3.0-only
Group:          Development/Libraries/C and C++
URL:            https://github.com/Ultimaker/libSavitar
Source0:        %{name}-%{version}.tar.xz
# PATCH-FIX-OPENSUSE -- Use system libraries instead of embedded ones.
Patch0:         use-system-libs.patch
# PATCH-FIX-OPENSUSE - use Qt5 sip import name, taken from Fedora
Patch1:         libSavitar-3.5.1-PyQt5.sip.patch
BuildRequires:  cmake >= 2.8.12
BuildRequires:  gmock
BuildRequires:  gtest
BuildRequires:  pugixml-devel >= 1.8
BuildRequires:  python3-sip-devel

%description
libSavitar is a C++ implementation of 3mf loading with SIP python bindings.

%package -n %{name}%{sover}
Summary:        3D printer control software
Group:          System/Libraries
Provides:       python3-Savitar = %version

%description -n %{name}%{sover}
libSavitar is a C++ implementation of 3mf loading with SIP python bindings.

%package devel
Summary:        Header files for libSavitar
Group:          Development/Libraries/C and C++
Requires:       %{name}%{sover} = %{version}
Requires:       python3-sip-devel

%description devel
Development package for libSavitar.

%prep
%autosetup -p1

%build
%cmake -DUSE_SYSTEM_LIBS=TRUE \
       -DBUILD_TESTS=TRUE \
       -DLIB_SUFFIX=64
make %{?_smp_mflags}

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
