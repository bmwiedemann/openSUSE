#
# spec file for package utfcpp
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


Name:           utfcpp
Version:        3.1.1
Release:        0
Summary:        A library for handling UTF-8 encoded strings
License:        BSL-1.0
URL:            https://github.com/nemtrif/utfcpp
Source:         https://github.com/nemtrif/utfcpp/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE utfcpp-use_system_gtest.patch aloisio@gmx.com -- use system-supplied googletest
Patch0:         utfcpp-use_system_gtest.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  googletest-devel

%description
A C++ library for handling UTF-8 encoded strings.

%package devel
Summary:        A library for handling UTF-8 encoded strings

%description devel
A C++ library for handling UTF-8 encoded strings.

%prep
%autosetup -p1

%build
%cmake

%install
%cmake_install

%check
make -C build test

%files devel
%license LICENSE
%doc README.md
%dir %{_includedir}/utf8cpp
%{_includedir}/utf8cpp/utf8.h
%dir %{_includedir}/utf8cpp/utf8
%{_includedir}/utf8cpp/utf8/checked.h
%{_includedir}/utf8cpp/utf8/core.h
%{_includedir}/utf8cpp/utf8/cpp11.h
%{_includedir}/utf8cpp/utf8/unchecked.h
%dir %{_libdir}/cmake/utf8cpp
%{_libdir}/cmake/utf8cpp/utf8cppConfig.cmake

%changelog
