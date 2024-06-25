#
# spec file for package optee-client
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


%define libname libteec2
%define libname2 libckteec0
%define libname3 libseteec0
%define libname4 libteeacl0
Name:           optee-client
Version:        4.2.0
Release:        0
Summary:        A Trusted Execution Environment client
License:        BSD-2-Clause
Group:          System/Boot
URL:            https://github.com/OP-TEE/optee_client
Source:         https://github.com/OP-TEE/optee_client/archive/%{version}.tar.gz#/optee_client-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  libuuid-devel

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

%package -n %{libname2}
Summary:        Library implementing the PKCS11 API
Group:          System/Libraries

%description -n %{libname2}
This component provides the PKCS11 API using the PKCS11 trusted
application executing in OP-TEE.For a general overview of OP-TEE, the
Open Platform Trusted Execution Environment, see the Notice.md file.

%package -n %{libname3}
Summary:        Library implementing the Secure Element control
Group:          System/Libraries

%description -n %{libname3}
When a Secure Element -supported by OP-TEE- enables SCP03, the
encryption keys could have been derived from the HUK and therefore not
known to the normal world.

In such circumstances, APDU frames will need to be routed to the
secure world for encryption before sending them to the SE and then
decrypted when processing the response.

Secure Elements supporting SCP03 are shipped with predefined keys
stored in persistent memory and documented in their data sheets.

This library provides an interface to enable SCP03 using those
non-secure keys. It also provides an interface to rotate these default
keys and derive board unique new ones before enabling the SCP03
session.

%package -n %{libname4}
Summary:        ACL helper library
Group:          System/Libraries

%description -n %{libname4}
Helper library libteeacl containing functions that can be used to
generate the hashed UUID of the user or group. These can then be
configured to PKCS11 tokens provided by libckteec for Access Control
List (ACL) based access.

%package devel
Summary:        Files for Developing with libtee
Group:          Development/Libraries/C and C++
Requires:       %{libname2} = %{version}
Requires:       %{libname3} = %{version}
Requires:       %{libname4} = %{version}
Requires:       %{libname} = %{version}

%description devel
This component provides the TEE Client API as defined by the GlobalPlatform
TEE standard. For a general overview of OP-TEE, please see the Notice.md file.

This package contains the libvisio development files.

%prep
%autosetup -p1 -n optee_client-%{version}

%build
%cmake
make %{?_smp_mflags} V=1

%install
%cmake_install

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%post -n %{libname2} -p /sbin/ldconfig
%postun -n %{libname2} -p /sbin/ldconfig

%post -n %{libname3} -p /sbin/ldconfig
%postun -n %{libname3} -p /sbin/ldconfig

%post -n %{libname4} -p /sbin/ldconfig
%postun -n %{libname4} -p /sbin/ldconfig

%files
%license LICENSE
%doc README.md
%{_sbindir}/tee-supplicant

%files devel
%{_includedir}/*.h
%{_libdir}/libteec.so
%{_libdir}/libckteec.so
%{_libdir}/libseteec.so
%{_libdir}/libteeacl.so
%{_libdir}/pkgconfig/teec.pc
%{_libdir}/pkgconfig/teeacl.pc

%files -n %{libname}
%{_libdir}/libteec.so.*

%files -n %{libname2}
%{_libdir}/libckteec.so.*

%files -n %{libname3}
%{_libdir}/libseteec.so.*

%files -n %{libname4}
%{_libdir}/libteeacl.so.*

%changelog
