#
# spec file for package libunicode
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

 
%define ver     0
%define mayor   4
%define lname   libunicode%{ver}_%{mayor}
%define sover   %{ver}.%{mayor}
%define force_gcc_version 13
Name:           libunicode
Version:        0.4.0
Release:        0
Summary:        Modern C++17 Unicode library
License:        Apache-2.0
URL:            https://github.com/contour-terminal/libunicode
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         libunicode-fix-catch-in-cmake.patch 
BuildRequires:  ccache
BuildRequires:  cmake
BuildRequires:  fmt-devel
%if 0%{?suse_version} < 1600
BuildRequires:  gcc%{?force_gcc_version}
BuildRequires:  gcc%{?force_gcc_version}-c++
%else
BuildRequires:  gcc-c++
%endif
BuildRequires:  range-v3-devel
BuildRequires:  unicode-ucd
BuildRequires:  cmake(Catch2) >= 3.3.0
ExclusiveArch:  x86_64 aarch64

%description
The goal of libunicode library is to bring painless unicode support to C++
with simple and easy to understand APIs. The API naming conventions are chosen
to look familiar to those using the C++ standard libary.

%package -n     %{lname}
Summary:        Library files for %{name}
%description -n %{lname}

The %{name} package contains libraries files for applications
that use %{name}

%package        devel
Summary:        Development files for %{name}
Requires:       %{lname} = %{version}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        tools
Summary:        Tools for %{name}
Requires:       %{lname} = %{version}

%description    tools
The %{name}-tools package contains tools about %{name}.

%prep
%autosetup -p1

%build
%if 0%{?suse_version} < 1600
export CC="gcc-%{?force_gcc_version}"
export CXX="g++-%{?force_gcc_version}"
%endif
%cmake \
%if 0%{?suse_version} < 1600
    -DLIBUNICODE_TESTING=OFF \
%endif
    -DLIBUNICODE_UCD_DIR=%{_datadir}/unicode/ucd
%cmake_build

%install
%cmake_install

#check
#ctest

%ldconfig_scriptlets -n %lname

%files -n %{lname}
%license LICENSE
%doc README.md Changelog.md
%{_libdir}/%{name}*.so.%{sover}*

%files devel
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%dir %{_libdir}/cmake/%{name}
%{_libdir}/cmake/%{name}/*.cmake
%{_libdir}/%{name}*.so

%files tools
%{_bindir}/unicode-query

%changelog
