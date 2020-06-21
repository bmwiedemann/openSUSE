#
# spec file for package libserf
#
# Copyright (c) 2020 SUSE LLC
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
Version:        1.3.9
Release:        0
Summary:        High-Performance Asynchronous HTTP Client Library
License:        Apache-2.0
Group:          System/Libraries
URL:            https://serf.apache.org/
Source:         https://dist.apache.org/repos/dist/dev/serf/serf-%{version}.tar.bz2
Source2:        https://dist.apache.org/repos/dist/dev/serf/serf-%{version}.tar.bz2.asc
Source3:        https://people.apache.org/keys/group/serf.asc#/%{name}.keyring
# PATCH-FIX-UPSTREAM libserf-python3.patch
# https://github.com/apache/serf/commit/d4de5a672d8c03b82ba70c1b737926bcf078f761
Patch0:         libserf-python3.patch
# PATCH-FIX-UPSTREAM libserf-python3-2.patch
# http://svn.apache.org/viewvc?view=revision&revision=1814604
Patch1:         libserf-python3-2.patch
BuildRequires:  gcc
BuildRequires:  glibc-devel
BuildRequires:  libapr-util1-devel >= %{minimum_apr_version}
BuildRequires:  libapr1-devel >= %{minimum_apr_version}
BuildRequires:  libexpat-devel
BuildRequires:  libopenssl-devel
BuildRequires:  openldap2-devel
BuildRequires:  pkgconfig
BuildRequires:  scons >= 2.3
BuildRequires:  zlib-devel
%if %{with gssapi}
BuildRequires:  krb5-devel
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
Requires:       libapr-util1-devel >= %{minimum_apr_version}
Requires:       libapr1-devel >= %{minimum_apr_version}
Requires:       libexpat-devel
Requires:       libopenssl-devel
Requires:       libserf-%{major}-%{major} = %{version}
Requires:       openldap2-devel
Requires:       zlib-devel
%if %{with gssapi}
Requires:       krb5-devel
%endif

%description -n libserf-devel
The serf library is a C-based HTTP client library built upon the Apache
Portable Runtime (APR) library. It multiplexes connections, running the
read/write communication asynchronously. Memory copies and transformations are
kept to a minimum to provide high performance operation.

%prep
%setup -q -n "serf-%{version}"
%patch0 -p1
%patch1 -p1

%build
scons \
	PREFIX=%{_prefix} \
	LIBDIR=%{_libdir} \
	APR=%{_prefix} \
	OPENSSL=%{_prefix} \
	ZLIB=%{_prefix} \
%if %{with gssapi}
	GSSAPI=$(krb5-config --prefix) \
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
%{_includedir}/serf-%{major}
%{_libdir}/libserf-%{major}.so
%{_libdir}/pkgconfig/serf-%{major}.pc

%changelog
