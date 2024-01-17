#
# spec file for package libkmip
#
# Copyright (c) 2021 SUSE LLC
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


Name:           libkmip
Version:        0.2.0
Release:        0
Summary:        ISO C11 implementation of the Key Management Interoperability Protocol
License:        Apache-2.0 OR BSD-3-Clause
Group:          Productivity/Security
URL:            https://github.com/OpenKMIP/libkmip
Source:         https://github.com/OpenKMIP/libkmip/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  libopenssl-devel

%description
libkmip is an ISO C11 implementation of the Key Management
Interoperability Protocol (KMIP), an OASIS communication standard
for the management of objects stored and maintained by key
management systems.

%package -n libkmip0
Summary:        ISO C11 implementation of the Key Management Interoperability Protocol
Group:          System/Libraries

%description -n libkmip0
libkmip is an ISO C11 implementation of the Key Management
Interoperability Protocol (KMIP), an OASIS communication standard
for the management of objects stored and maintained by key
management systems. KMIP defines how key management operations
and operation data should be encoded and communicated, between
client and server applications. Supported operations include
creating, retrieving, and destroying keys. Supported object types
include symmetric and asymmetric encryption keys.

For more information on KMIP, check out the OASIS KMIP Technical
Committee and the OASIS KMIP Documentation.

This package contains the shared library.

%package devel
Summary:        Header files for the Key Management Interoperability Protocol library
Group:          Development/Languages/C and C++
Requires:       libkmip0 = %{version}

%description devel
libkmip is an ISO C11 implementation of the Key Management
Interoperability Protocol (KMIP), an OASIS communication standard
for the management of objects stored and maintained by key
management systems.

This package contains the development headers and libraries.

%package tools
Summary:        Tools for the Key Management Interoperability Protocol
Group:          Development/Languages/C and C++

%description tools
libkmip is an ISO C11 implementation of the Key Management
Interoperability Protocol (KMIP), an OASIS communication standard
for the management of objects stored and maintained by key
management systems. KMIP defines how key management operations
and operation data should be encoded and communicated, between
client and server applications. Supported operations include
creating, retrieving, and destroying keys. Supported object types
include symmetric and asymmetric encryption keys.

This package contains various tools.

%prep
%autosetup -p1

%build
%make_build CFLAGS="%{optflags} -std=c11"

%install
%make_install PREFIX="%{_prefix}"

if [ "lib" != "%_lib" ]; 
then
	mv %{buildroot}/%{_prefix}/lib %{buildroot}/%{_libdir}
fi
rm %{buildroot}/%{_libdir}/libkmip.a
mv %{buildroot}/%{_bindir}/kmip %{buildroot}/%{_libdir}/kmip/
rm -rf %{buildroot}/%{_prefix}/src

%post -n libkmip0 -p /sbin/ldconfig
%postun -n libkmip0 -p /sbin/ldconfig

%files -n libkmip0
%license LICENSE LICENSE.APACHE LICENSE.BSD
%{_libdir}/libkmip.so.0*

%files devel
%license LICENSE LICENSE.APACHE LICENSE.BSD
%dir %{_includedir}/kmip
%{_includedir}/kmip/*
%{_libdir}/libkmip.so

%files tools
%license LICENSE LICENSE.APACHE LICENSE.BSD
%dir /%{_libdir}/kmip
%{_libdir}/kmip/*
%doc %{_datadir}/doc/kmip

%changelog
