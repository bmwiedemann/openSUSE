#
# spec file for package libmfx-gen
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


%global sover 1_2
Name:           libmfx-gen
%define lname   libmfx-gen%{sover}
Version:        24.1.5
Release:        0
Summary:        Intel oneVPL GPU Runtime
License:        MIT
Group:          Development/Languages/C and C++
URL:            https://github.com/oneapi-src/oneVPL-intel-gpu
Source0:        https://github.com/intel/vpl-gpu-rt/archive/refs/tags/intel-onevpl-%{version}.tar.gz
Source1:        supplements.inc
Source2:        generate-supplements.sh
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libva)
ExclusiveArch:  x86_64

%description
Intel oneVPL GPU Runtime is a Runtime implementation of oneVPL
API for Intel Gen GPUs: Runtime provides access to
hardware-accelerated video decode, encode and filtering.

%package -n %lname
Summary:        Intel oneVPL GPU Runtime
Group:          System/Libraries
%include %{S:1}

%description -n %lname
Intel oneVPL GPU Runtime is a Runtime implementation of oneVPL
API for Intel Gen GPUs: Runtime provides access to
hardware-accelerated video decode, encode and filtering.

%package devel
Summary:        Development files for Intel oneVPL GPU Runtime
Group:          Development/Languages/C and C++
Requires:       %lname = %version

%description devel
This package contains the development headers and pkgconfig files for
the Intel oneVPL GPU Runtime.

%prep
%autosetup -p1 -n vpl-gpu-rt-intel-onevpl-%{version}

%build
mkdir -p build
pushd build
cmake -DCMAKE_INSTALL_PREFIX="%{_prefix}" ..
make %{?_smp_mflags}
popd

%install
pushd build
%make_install
popd

%ldconfig_scriptlets -n %lname

%files
%doc README.md

%files -n %lname
%license LICENSE
%{_libdir}/libmfx-gen.so.1*
%dir %{_libdir}/libmfx-gen
%{_libdir}/libmfx-gen/enctools.so

%files devel
%{_libdir}/libmfx-gen.so
%{_libdir}/pkgconfig/libmfx-gen.pc

%changelog
