#
# spec file for package utfcpp
#
# Copyright (c) 2025 SUSE LLC
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


Name:           utfcpp
Version:        4.0.8
Release:        0
Summary:        A library for handling UTF-8 encoded strings
License:        BSL-1.0
URL:            https://github.com/nemtrif/utfcpp
Source:         %{name}-%{version}.tar.xz
Patch0:         utfcpp-4.0.5-cmake-location.patch
BuildRequires:  c++_compiler
BuildRequires:  cmake >= 3.14
BuildArch:      noarch

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
%cmake_build

%install
%cmake_install

%check
%ctest

%files devel
%license LICENSE
%doc README.md
%{_includedir}/utf8cpp
%{_datadir}/cmake/utf8cpp

%changelog
