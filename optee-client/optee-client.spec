#
# spec file for package optee-client
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define libname libteec1
Name:           optee-client
Version:        3.5.0
Release:        0
Summary:        A Trusted Execution Environment client
License:        BSD-2-Clause
Group:          System/Boot
URL:            https://github.com/OP-TEE/optee_client
Source:         https://github.com/OP-TEE/optee_client/archive/%{version}.tar.gz#/optee_client-%{version}.tar.gz
BuildRequires:  cmake

%description
This component provides the TEE Client API as defined by the
GlobalPlatform TEE standard. For a general overview of OP-TEE, the
Open Platform Trusted Execution Environment, see the Notice.md file.

%package -n %{libname}
Summary:        Library implementing TEE Client API
Group:          System/Libraries

%description -n %{libname}
This component provides the TEE Client API as defined by the
GlobalPlatform TEE standard. For a general overview of OP-TEE, the
Open Platform Trusted Execution Environment, see the Notice.md file.

%package devel
Summary:        Files for Developing with libtee
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
This component provides the TEE Client API as defined by the GlobalPlatform
TEE standard. For a general overview of OP-TEE, please see the Notice.md file.

This package contains the libvisio development files.

%prep
%setup -q -n optee_client-%{version}

sed -i \
    -e "s:-Werror ::g" \
    CMakeLists.txt

%build
%cmake
make %{?_smp_mflags} V=1

%install
%cmake_install

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files
%license LICENSE
%doc README.md
%{_sbindir}/tee-supplicant

%files devel
%{_includedir}/*.h
%{_libdir}/libteec.so

%files -n %{libname}
%{_libdir}/libteec.so.*

%changelog
