#
# spec file for package fedfs-utils
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

Name:           fedfs-utils
Url:            http://wiki.linux-nfs.org/wiki/index.php/FedFsUtilsProject
Version:        0.10.7
Release:        0
Summary:        Utilities for mounting and managing FedFS
License:        GPL-2.0
Group:          Productivity/Networking/System
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  krb5-devel
BuildRequires:  libattr-devel
BuildRequires:  libcap-devel
BuildRequires:  libconfig-devel
BuildRequires:  libidn-devel
BuildRequires:  libopenssl-devel
BuildRequires:  libtirpc-devel
BuildRequires:  libtool
BuildRequires:  liburiparser-devel
BuildRequires:  libuuid-devel
BuildRequires:  libxml2-devel
BuildRequires:  openldap2-devel
BuildRequires:  python
BuildRequires:  rpcsvc-proto-devel
BuildRequires:  shadow
BuildRequires:  sqlite-devel

Source:         %{name}-%{version}.tar.gz
Source1:        sysconfig.fedfs
Patch:          fedfs-utils-no-sunrpc.diff

%description
RFC 5716 introduces the Federated File System (FedFS, for short). FedFS
is an extensible standardized mechanism by which system administrators
construct a coherent namespace across multiple file servers using file
system referrals.

A file system referral is like a symbolic link to another file system
share, but it is not visible to applications. It behaves like an
automounted directory where a new file system mount is done when an
application first accesses that directory. The arguments of the mount
operation are controlled by information returned by the file server.

Today, file system referral mechanisms exist in several network file
system protocols. FedFS provides its namespace features by leveraging
referral mechanisms already built in to network file system protocols.
Thus no change to file system protocols or clients is required.

Currently, the Linux FedFS implementation supports only NFS version 4
referrals. More on NFS version 4 referrals can be found in RFC 3530.
FedFS may support other network file system protocols in the future.

%prep
%setup -q -n %{name}-%{version}
%patch -p0

%build
./autogen.sh
%define _sharedstatedir /var/lib
%configure --sysconfdir=/etc/fedfs
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
%fdupes %{buildroot}%{python_sitelib}
mkdir -p %{buildroot}%{_sharedstatedir}/fedfs
mkdir -p %{buildroot}%{_unitdir}
install -m 644 contrib/init/rpcfedfsd.service %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_fillupdir}
install -m 644 %{S:1} %{buildroot}%{_fillupdir}/sysconfig.fedfs
ln -s %{_sbindir}/service $RPM_BUILD_ROOT%{_sbindir}/rcrpcfedfsd

# Don't package static libs to encourage use of shared library.
rm -f %{buildroot}%{_libdir}/libnfsjunct.a
rm -f %{buildroot}%{_libdir}/libnfsjunct.la

%package common
Summary:        Common files for FedFS
Group:          Productivity/Networking/System
BuildArch:      noarch

%description common
This package contains files common to all of the fedfs packages.

RFC 5716 introduces the Federated File System (FedFS, for short). FedFS
is an extensible standardized mechanism by which system administrators
construct a coherent namespace across multiple file servers using file
system referrals.

A file system referral is like a symbolic link to another file system
share, but it is not visible to applications. It behaves like an
automounted directory where a new file system mount is done when an
application first accesses that directory. The arguments of the mount
operation are controlled by information returned by the file server.

Today, file system referral mechanisms exist in several network file
system protocols. FedFS provides its namespace features by leveraging
referral mechanisms already built in to network file system protocols.
Thus no change to file system protocols or clients is required.

Currently, the Linux FedFS implementation supports only NFS version 4
referrals. More on NFS version 4 referrals can be found in RFC 3530.
FedFS may support other network file system protocols in the future.

%files common
%defattr(-,root,root)
%doc COPYING README ChangeLog doc/ldap/fedfs.schema doc/ldap/fedfs-schema.ldif
%{_mandir}/man7/fedfs.7.*

%package client
Summary:        Utilities for mounting FedFS domains
Group:          Productivity/Networking/System
Requires:       %{name}-common = %{version}-%{release}
Requires:       nfs-client

%description client
This package contains the tools needed to mount a FedFS domain and act
as a client.

RFC 5716 introduces the Federated File System (FedFS, for short). FedFS
is an extensible standardized mechanism by which system administrators
construct a coherent namespace across multiple file servers using file
system referrals.

A file system referral is like a symbolic link to another file system
share, but it is not visible to applications. It behaves like an
automounted directory where a new file system mount is done when an
application first accesses that directory. The arguments of the mount
operation are controlled by information returned by the file server.

Today, file system referral mechanisms exist in several network file
system protocols. FedFS provides its namespace features by leveraging
referral mechanisms already built in to network file system protocols.
Thus no change to file system protocols or clients is required.

Currently, the Linux FedFS implementation supports only NFS version 4
referrals. More on NFS version 4 referrals can be found in RFC 3530.
FedFS may support other network file system protocols in the future.

%files client
%defattr(-,root,root)
/sbin/mount.fedfs
%{_sbindir}/fedfs-map-nfs4
%{_mandir}/man8/mount.fedfs.8.*
%{_mandir}/man8/fedfs-map-nfs4.8.*

%package nsdbparams
Summary:        FedFS nsdbparams utility
Group:          Productivity/Networking/System
Requires:       %{name}-common = %{version}-%{release}

%description nsdbparams
This package contains the nsdbparams utility, which is needed by both
the fedfs-server and fedfs-admin packages.

RFC 5716 introduces the Federated File System (FedFS, for short). FedFS
is an extensible standardized mechanism by which system administrators
construct a coherent namespace across multiple file servers using file
system referrals.

A file system referral is like a symbolic link to another file system
share, but it is not visible to applications. It behaves like an
automounted directory where a new file system mount is done when an
application first accesses that directory. The arguments of the mount
operation are controlled by information returned by the file server.

Today, file system referral mechanisms exist in several network file
system protocols. FedFS provides its namespace features by leveraging
referral mechanisms already built in to network file system protocols.
Thus no change to file system protocols or clients is required.

Currently, the Linux FedFS implementation supports only NFS version 4
referrals. More on NFS version 4 referrals can be found in RFC 3530.
FedFS may support other network file system protocols in the future.

%files nsdbparams
%defattr(-,root,root)
%{_sbindir}/nsdbparams
%{_mandir}/man8/nsdbparams.8.*
%{_mandir}/man7/nsdb-parameters.7.*

%package devel
Summary:        Development files and libraries for the nfs-plugin
Group:          Development/Libraries/C and C++
Requires:       %{name}-common = %{version}-%{release}
Requires:       libnfsjunct0%{?_isa} = %{version}-%{release}

%description devel
This package contains the development files and libraries for the nfs-plugin.

RFC 5716 introduces the Federated File System (FedFS, for short). FedFS
is an extensible standardized mechanism by which system administrators
construct a coherent namespace across multiple file servers using file
system referrals.

A file system referral is like a symbolic link to another file system
share, but it is not visible to applications. It behaves like an
automounted directory where a new file system mount is done when an
application first accesses that directory. The arguments of the mount
operation are controlled by information returned by the file server.

Today, file system referral mechanisms exist in several network file
system protocols. FedFS provides its namespace features by leveraging
referral mechanisms already built in to network file system protocols.
Thus no change to file system protocols or clients is required.

Currently, the Linux FedFS implementation supports only NFS version 4
referrals. More on NFS version 4 referrals can be found in RFC 3530.
FedFS may support other network file system protocols in the future.

%files devel
%defattr(-,root,root)
%{_includedir}/nfs-plugin.h
%{_libdir}/libnfsjunct.so

%package -n libnfsjunct0
Summary:        Runtime libraries for the nfs-plugin
Group:          Productivity/Networking/System

%description -n libnfsjunct0
This package contains runtime libraries for the nfs-plugin.

RFC 5716 introduces the Federated File System (FedFS, for short). FedFS
is an extensible standardized mechanism by which system administrators
construct a coherent namespace across multiple file servers using file
system referrals.

A file system referral is like a symbolic link to another file system
share, but it is not visible to applications. It behaves like an
automounted directory where a new file system mount is done when an
application first accesses that directory. The arguments of the mount
operation are controlled by information returned by the file server.

Today, file system referral mechanisms exist in several network file
system protocols. FedFS provides its namespace features by leveraging
referral mechanisms already built in to network file system protocols.
Thus no change to file system protocols or clients is required.

Currently, the Linux FedFS implementation supports only NFS version 4
referrals. More on NFS version 4 referrals can be found in RFC 3530.
FedFS may support other network file system protocols in the future.

%post -n libnfsjunct0 -p /sbin/ldconfig

%postun -n libnfsjunct0 -p /sbin/ldconfig

%files -n libnfsjunct0
%defattr(-,root,root)
# We need to include this in the lib package because it is
# dlopen()ed by the junction support code in nfs-utils.
%{_libdir}/libnfsjunct.so.*

%package server
Summary:        Utilities for serving FedFS domains
Group:          Productivity/Networking/System
Requires:       %{name}-common = %{version}-%{release}
Requires:       %{name}-nsdbparams%{?_isa} = %{version}-%{release}
Requires:       libnfsjunct0%{?_isa} = %{version}-%{release}
Requires:       nfs-kernel-server

%description server
This package contains the tools needed to act as a FedFS server.

RFC 5716 introduces the Federated File System (FedFS, for short). FedFS
is an extensible standardized mechanism by which system administrators
construct a coherent namespace across multiple file servers using file
system referrals.

A file system referral is like a symbolic link to another file system
share, but it is not visible to applications. It behaves like an
automounted directory where a new file system mount is done when an
application first accesses that directory. The arguments of the mount
operation are controlled by information returned by the file server.

Today, file system referral mechanisms exist in several network file
system protocols. FedFS provides its namespace features by leveraging
referral mechanisms already built in to network file system protocols.
Thus no change to file system protocols or clients is required.

Currently, the Linux FedFS implementation supports only NFS version 4
referrals. More on NFS version 4 referrals can be found in RFC 3530.
FedFS may support other network file system protocols in the future.

%pre server
getent group fedfs >/dev/null || groupadd -r fedfs
getent passwd fedfs >/dev/null || \
    useradd -r -g fedfs -d %{_sharedstatedir}/fedfs -s /sbin/nologin \
    -c "FedFS Server User" fedfs
%service_add_pre rpcfedfsd.service
exit 0

%post server
%{fillup_only -an fedfs}
%service_add_post rpcfedfsd.service

%preun server
%service_del_preun rpcfedfsd.service

%postun server
%service_del_postun rpcfedfsd.service

%files server
%defattr(-,root,root)
%dir %{_sharedstatedir}/fedfs
%{_sbindir}/nfsref
%{_sbindir}/rpc.fedfsd
%{_sbindir}/rcrpcfedfsd
%dir /etc/fedfs
%config /etc/fedfs/access.conf
%{_mandir}/man8/rpc.fedfsd.8.*
%{_mandir}/man8/nfsref.8.*
%{_unitdir}/rpcfedfsd.service
%{_fillupdir}/sysconfig.fedfs

%package admin
Summary:        Utilities for administering FedFS domains
Group:          Productivity/Networking/System
Requires:       %{name}-common = %{version}-%{release}
Requires:       %{name}-nsdbparams%{?_isa} = %{version}-%{release}

%description admin
This package contains the tools needed to manage a FedFS domain.

RFC 5716 introduces the Federated File System (FedFS, for short). FedFS
is an extensible standardized mechanism by which system administrators
construct a coherent namespace across multiple file servers using file
system referrals.

A file system referral is like a symbolic link to another file system
share, but it is not visible to applications. It behaves like an
automounted directory where a new file system mount is done when an
application first accesses that directory. The arguments of the mount
operation are controlled by information returned by the file server.

Today, file system referral mechanisms exist in several network file
system protocols. FedFS provides its namespace features by leveraging
referral mechanisms already built in to network file system protocols.
Thus no change to file system protocols or clients is required.

Currently, the Linux FedFS implementation supports only NFS version 4
referrals. More on NFS version 4 referrals can be found in RFC 3530.
FedFS may support other network file system protocols in the future.

%files admin
%defattr(-,root,root)
%{_bindir}/fedfs-domainroot
%{_bindir}/nsdb-jumpstart
%{python_sitelib}/PyFedfs/
%{_sbindir}/fedfs-create-junction
%{_sbindir}/fedfs-create-replication
%{_sbindir}/fedfs-delete-junction
%{_sbindir}/fedfs-delete-replication
%{_sbindir}/fedfs-get-limited-nsdb-params
%{_sbindir}/fedfs-get-nsdb-params
%{_sbindir}/fedfs-lookup-junction
%{_sbindir}/fedfs-lookup-replication
%{_sbindir}/fedfs-null
%{_sbindir}/fedfs-set-nsdb-params
%{_sbindir}/nsdb-*
%{_mandir}/man8/fedfs-create-junction.8.*
%{_mandir}/man8/fedfs-create-replication.8.*
%{_mandir}/man8/fedfs-delete-junction.8.*
%{_mandir}/man8/fedfs-delete-replication.8.*
%{_mandir}/man8/fedfs-get-limited-nsdb-params.8.*
%{_mandir}/man8/fedfs-get-nsdb-params.8.*
%{_mandir}/man8/fedfs-lookup-junction.8.*
%{_mandir}/man8/fedfs-lookup-replication.8.*
%{_mandir}/man8/fedfs-null.8.*
%{_mandir}/man8/fedfs-set-nsdb-params.8.*
%{_mandir}/man8/fedfs-domainroot.8.*
%{_mandir}/man8/nsdb-*

%changelog
