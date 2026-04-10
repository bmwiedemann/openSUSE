#
# spec file for package yaml-cpp
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define library_name libyaml-cpp0_9
Name:           yaml-cpp
Version:        0.9.0
Release:        0
Summary:        YAML parser and emitter in C++
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/jbeder/yaml-cpp/
Source:         https://github.com/jbeder/yaml-cpp/archive/%{name}-%{version}.tar.gz
Source98:       baselibs.conf
BuildRequires:  cmake >= 3.5
BuildRequires:  pkgconfig
BuildRequires:  sed
%if %{?suse_version} >= 1330
BuildRequires:  gcc
BuildRequires:  gcc-c++
%else
BuildRequires:  gcc6
BuildRequires:  gcc6-c++
%endif

%description
A YAML parser and emitter in C++ matching the YAML 1.2 spec.

%package -n %{library_name}
Summary:        YAML parser and emitter in C++
Group:          Development/Libraries/C and C++

%description -n %{library_name}
A YAML parser and emitter in C++ matching the YAML 1.2 spec.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{library_name} = %{version}

%description devel
Development files for %{name} library.

%prep
%autosetup -p1 -n %{name}-%{name}-%{version}

%build
export CC=gcc
export CXX=g++
%if 0%{?suse_version} < 1330
export CC=gcc-6
export CXX=g++-6
%endif
%cmake \
    -DYAML_BUILD_SHARED_LIBS:BOOL=ON \
    -DYAML_CPP_BUILD_TESTS:BOOL=OFF \
    -DCMAKE_C_COMPILER=$CC             \
    -DCMAKE_CXX_COMPILER=$CXX

make %{?_smp_mflags}

%install
%cmake_install

%check
%ctest

%ldconfig_scriptlets -n %{library_name}

%files -n %{library_name}
%license LICENSE
%{_libdir}/libyaml-cpp.so.*

%files devel
%{_libdir}/pkgconfig/yaml-cpp.pc
%{_libdir}/cmake/%{name}/
%{_includedir}/yaml-cpp/
%{_libdir}/libyaml-cpp.so

%changelog
