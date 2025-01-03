#
# spec file for package libunicode
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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
%define mayor   6
%define lname   libunicode%{ver}_%{mayor}
%define sover   %{ver}.%{mayor}
%define force_gcc_version 13
Name:           libunicode
Version:        0.6.0
Release:        0
Summary:        Modern C++20 Unicode library
License:        Apache-2.0
URL:            https://github.com/contour-terminal/libunicode
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  c++_compiler
BuildRequires:  cmake
BuildRequires:  unicode-ucd >= 16.0.0
BuildRequires:  cmake(Catch2) >= 3.3.0
BuildRequires:  cmake(range-v3)
%if 0%{?suse_version} < 1600
BuildRequires:  gcc%{?force_gcc_version}
BuildRequires:  gcc%{?force_gcc_version}-c++
%endif
ExclusiveArch:  x86_64 aarch64

%description

The goal of libunicode library is to bring painless unicode support to C++ with
simple and easy to understand APIs. The API naming conventions are chosen to
look familiar to those using the C++ standard libary.

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
	-DLIBUNICODE_UCD_DIR=%{_datadir}/unicode/ucd \
	%{nil}
%cmake_build

%install
%cmake_install

#check
#ctest

%ldconfig_scriptlets -n %{lname}

%files -n %{lname}
%license LICENSE
%doc README.md Changelog.md
%{_libdir}/%{name}*.so.%{sover}*

%files devel
%license LICENSE
%{_includedir}/%{name}
%{_libdir}/cmake/%{name}
%{_libdir}/%{name}*.so

%files tools
%license LICENSE
%{_bindir}/unicode-query

%changelog
