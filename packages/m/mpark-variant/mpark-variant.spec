#
# spec file for package mpark-variant
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           mpark-variant
Version:        1.4.0+20210816.23cb94f
Release:        0
Summary:        C++17 std::variant for C++11/14/17
License:        BSL-1.0
Group:          Development/Libraries/C and C++
URL:            https://github.com/mpark/variant
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  ninja

%description
MPark.Variant is an implementation of C++17 std::variant for C++11/14/17.

%package devel
Summary:        Development files for %{name}
Provides:       %{name}-static = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
MPark.Variant is an implementation of C++17 std::variant for C++11/14/17.

%prep
%autosetup -p1
sed -i 's@lib/@%{_libdir}/@g' CMakeLists.txt

%build
%cmake -G Ninja \
-DCMAKE_BUILD_TYPE=Release \

%ninja_build

%install
cd build
%ninja_install

%files devel
%doc README.md
%license LICENSE.md
%{_includedir}/mpark
%{_libdir}/cmake/mpark_variant

%changelog
