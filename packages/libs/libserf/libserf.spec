#
# spec file for package libserf
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


# version 1.2.0 requires apr 1.3.0 or later for apr_socket_addr_get
%define minimum_apr_version 1.3.0
%define major	1
%define minor	3
%define SHLIBVER %{major}.%{minor}.0
%bcond_without	gssapi
Name:           libserf
Version:        1.3.10
Release:        0
Summary:        High-Performance Asynchronous HTTP Client Library
License:        Apache-2.0
Group:          System/Libraries
URL:            https://serf.apache.org/
Source:         https://www.apache.org/dist/serf/serf-%{version}.tar.bz2
Source2:        https://www.apache.org/dist/serf/serf-%{version}.tar.bz2.asc
Source3:        https://www.apache.org/dist/serf/KEYS#/%{name}.keyring
BuildRequires:  pkgconfig
BuildRequires:  scons >= 2.3
BuildRequires:  pkgconfig(apr-1) >= %{minimum_apr_version}
BuildRequires:  pkgconfig(apr-util-1) >= %{minimum_apr_version}
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(zlib)
%if %{with gssapi}
BuildRequires:  pkgconfig(krb5-gssapi)
%endif

%description
The serf library is a C-based HTTP client library built upon the Apache
Portable Runtime (APR) library. It multiplexes connections, running the
read/write communication asynchronously. Memory copies and transformations are
kept to a minimum to provide high performance operation.

%package -n libserf-%{major}-%{major}
Summary:        High-Performance Asynchronous HTTP Client Library
Group:          Development/Libraries/C and C++

%description -n libserf-%{major}-%{major}
The serf library is a C-based HTTP client library built upon the Apache
Portable Runtime (APR) library. It multiplexes connections, running the
read/write communication asynchronously. Memory copies and transformations are
kept to a minimum to provide high performance operation.

%package -n libserf-devel
Summary:        High-Performance Asynchronous HTTP Client Library
Group:          Development/Libraries/C and C++
Requires:       libserf-%{major}-%{major} = %{version}

%description -n libserf-devel
The serf library is a C-based HTTP client library built upon the Apache
Portable Runtime (APR) library. It multiplexes connections, running the
read/write communication asynchronously. Memory copies and transformations are
kept to a minimum to provide high performance operation.

%prep
%autosetup -p1 -n "serf-%{version}"

%build
scons \
	PREFIX=%{_prefix} \
	LIBDIR=%{_libdir} \
	APR=%{_prefix} \
	OPENSSL=%{_prefix} \
	ZLIB=%{_prefix} \
%if %{with gssapi}
	GSSAPI=$(which krb5-config) \
%endif
	DEBUG=yes \
	CFLAGS="%{optflags}" \
	APR_STATIC=no \
	%{?_smp_mflags}

%install
scons install --install-sandbox=%{buildroot}
rm -f "%{buildroot}%{_libdir}"/lib*.a

%post   -n libserf-%{major}-%{major} -p /sbin/ldconfig
%postun -n libserf-%{major}-%{major} -p /sbin/ldconfig

%files -n libserf-%{major}-%{major}
%license LICENSE
%doc CHANGES NOTICE README
%doc design-guide.txt
%{_libdir}/libserf-%{major}.so.%{major}
%{_libdir}/libserf-%{major}.so.%{SHLIBVER}

%files -n libserf-devel
%license LICENSE
%{_includedir}/serf-%{major}
%{_libdir}/libserf-%{major}.so
%{_libdir}/pkgconfig/serf-%{major}.pc

%changelog
