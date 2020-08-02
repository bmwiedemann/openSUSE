#
# spec file for package easyloggingpp
#
# Copyright (c) 2019 SUSE LLC
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


Name:           easyloggingpp
Version:        9.96.7
Release:        0
Summary:        Single header C++ logging library
License:        MIT
URL:            https://github.com/muflihun/easyloggingpp
Source0:        https://github.com/muflihun/easyloggingpp/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig

%description
Single header C++ logging library. It is thread-aware and type safe,
it provides ability to write logs in a customized format, and support
for logging classes, third-party libraries, STL and third-party
containers.

%package devel
Summary:        Single header C++ logging library

%description devel
Single header C++ logging library. It is thread-aware and type safe,
it provides ability to write logs in a customized format, and support
for logging classes, third-party libraries, STL and third-party
containers.

%prep
%autosetup -p1

%build
%cmake

%install
%cmake_install

%files devel
%doc CHANGELOG.md README.md
%license LICENSE
%{_includedir}/easylogging++.cc
%{_includedir}/easylogging++.h
%{_datadir}/pkgconfig/%{name}.pc

%changelog
