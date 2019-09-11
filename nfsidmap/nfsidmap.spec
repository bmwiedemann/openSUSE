#
# spec file for package nfsidmap
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           nfsidmap
Version:        0.27
Release:        0
Summary:        NFSv4 ID Mapping Library
License:        BSD-3-Clause
Group:          Productivity/Networking/NFS
URL:            http://nfs.sourceforge.net
Source0:        https://fedorapeople.org/~steved/libnfsidmap/%{version}/libnfsidmap-%{version}.tar.bz2
Source1:        nfsv4.schema
Patch0:         fix-prototype.patch
Patch1:         libnfsidmap-export-symbols.patch
Patch3:         0002-nss_gss_princ_to_ids-and-nss_gss_princ_to_grouplist-.patch
BuildRequires:  libtool
BuildRequires:  openldap2-devel
BuildRequires:  pkgconfig
BuildRequires:  tcpd-devel

%description
In NFSv4, identities of users are conveyed by names rather than user ID
and group ID. Both the NFS server and client code in the kernel need to
translate these to numeric IDs.

%package devel
Summary:        NFSv4 ID Mapping Library development libraries
Group:          Development/Libraries/C and C++
Requires:       nfsidmap = %{version}

%description devel
In NFSv4, identities of users are conveyed by names rather than user ID
and group ID. Both the NFS server and client code in the kernel need to
translate these to numeric IDs.

%prep
%setup -q -n libnfsidmap-%{version}
%patch0 -p1
%patch1 -p1
%patch3 -p1
cp %{SOURCE1} .

%build
autoreconf -fiv
export CFLAGS="%{optflags} -DLDAP_DEPRECATED -DENABLE_LDAP"
%configure \
  --disable-static \
  --with-pluginpath=%{_libdir}/libnfsidmap
make %{?_smp_mflags}

%check
make %{?_smp_mflags} check

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc README nfsv4.schema
%{_libdir}/libnfsidmap/
%{_libdir}/libnfsidmap.so.0*
%{_mandir}/man?/*

%files devel
%{_libdir}/libnfsidmap.so
%{_includedir}/*.h
%{_libdir}/pkgconfig/libnfsidmap.pc

%changelog
