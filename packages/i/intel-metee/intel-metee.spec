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

%define SONAME libmetee6_0_2_0

Name:           intel-metee
Version:        6.0.2
Release:        0
Summary:        Library to access CSE/CSME/GSC firmware via a MEI interface
License:        Apache-2.0
URL:            https://github.com/intel/metee
Source:         https://github.com/intel/metee/archive/refs/tags/%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake

%description
ME TEE Library is a C library to access CSE/CSME/GSC firmware via a
MEI interface. The MEI TEE API simplifies connection and
communication with the MEI device and firmware status registers
retrieval.

%package -n %{SONAME}
Summary:        Library to access CSE/CSME/GSC firmware via a MEI interface

%description -n %{SONAME}
ME TEE Library is a C library to access CSE/CSME/GSC [Converged
Security (and Management) Engine, Graphic System Controller] firmware
via a MEI interface. The MEI TEE API simplifies connection and
communication with the MEI device and firmware status registers
retrieval.

%package devel
Summary:        Headers for the intel-metee library
Requires:       %{SONAME} = %{version}

%description devel
Development package for the libmeete library.

%prep
%autosetup -p1 -n metee-%{version}

%build
CFLAGS=-Wno-builtin-macro-redefined \
%cmake
%cmake_build

%install
%cmake_install

%ldconfig_scriptlets -n %{SONAME}

%files -n %{SONAME}
%license COPYING
%doc CHANGELOG.md README.md
%{_libdir}/libmetee.so.%{version}.0

%files devel
%{_libdir}/libmetee.so
%{_includedir}/metee.h

%changelog

