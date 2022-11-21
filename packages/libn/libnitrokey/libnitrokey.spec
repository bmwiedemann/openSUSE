#
# spec file for package libnitrokey
#
# Copyright (c) 2022 SUSE LLC
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


%if 0%{?suse_version} == 1315
%define force_gcc_version 7
%endif
%define lib_name %{name}3

Name:           libnitrokey
Version:        3.8
Release:        0
Summary:        Communicate with Nitrokey stick devices in a clean and easy manner
License:        LGPL-3.0-only
Group:          Development/Libraries/C and C++
URL:            https://github.com/Nitrokey/libnitrokey
Source:         https://github.com/Nitrokey/libnitrokey/releases/download/v%{version}/libnitrokey-v%{version}.tar.gz
Source1:        https://github.com/Nitrokey/libnitrokey/releases/download/v%{version}/libnitrokey-v%{version}.tar.gz.sig
BuildRequires:  cmake
BuildRequires:  gcc%{?force_gcc_version}-c++ >= 5
%if 0%{?force_gcc_version}
#!BuildIgnore:  libgcc_s1
%endif
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  pkgconfig(hidapi-libusb)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(udev)

%description
Libnitrokey is a project to communicate with Nitrokey Pro and Storage devices
in a clean and easy manner.

%package -n %{lib_name}
Summary:        Shared library for libnitrokey
Group:          Development/Libraries/C and C++
Requires:       %{name}-udev >= %{version}

%description -n %{lib_name}
Libnitrokey is a project to communicate with Nitrokey Pro and Storage devices
in a clean and easy manner.

This package holds the shared library.

%package udev
Summary:        udev rules for libnitrokey
Group:          Development/Libraries/C and C++
BuildArch:      noarch

%description udev
Libnitrokey is a project to communicate with Nitrokey Pro and Storage devices
in a clean and easy manner.

This package holds the udev rules.

%package devel
Summary:        Development files for libnitrokey
Group:          Development/Libraries/C and C++
Requires:       %{lib_name} = %{version}

%description devel
Libnitrokey is a project to communicate with Nitrokey Pro and Storage devices
in a clean and easy manner.

This package holds the development files.

%prep
%setup -q -n %{name}-v%{version}

%build
%if 0%{?force_gcc_version}
export CC="gcc-%{?force_gcc_version}"
export CXX="g++-%{?force_gcc_version}"
%endif
%cmake
make %{?_smp_mflags} CXX=g++

%install
%cmake_install

%post   -n %{lib_name} -p /sbin/ldconfig
%postun -n %{lib_name} -p /sbin/ldconfig

%files udev
%{_prefix}/lib/udev/rules.d/41-nitrokey.rules

%files devel
%{_includedir}/libnitrokey/
%{_libdir}/libnitrokey.so
%{_libdir}/pkgconfig/libnitrokey-1.pc

%files -n %{lib_name}
%{_libdir}/libnitrokey.so.*

%changelog
