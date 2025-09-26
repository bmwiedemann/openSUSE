#
# spec file for package intel-metee
#
# Copyright (c) 2025 SUSE LLC
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

Name:           igsc
Version:        1.0.0
Release:        0
Summary:        Intel Graphics System Controller Firmware Update Utility
License:        Apache-2.0
URL:            https://github.com/intel/igsc
Source:         https://github.com/intel/igsc/archive/refs/tags/V%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  intel-metee-devel 
BuildRequires:  systemd-devel

%description
Intel Graphics System Controller (igsc) Firmware Update Utility and
library.

%package devel
Summary:        Headers and cmake files for the igsc library

%description devel
Headers and cmake files for the igsc library.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%ldconfig_scriptlets

%files
%{_bindir}/igsc
%{_libdir}/libigsc.so.1*

%files devel
%{_includedir}/igsc_lib.h
%{_libdir}/cmake/igsc/
%{_libdir}/libigsc.so

%changelog

