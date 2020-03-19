#
# spec file for package fedfs-utils
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


%define libname libnfsjunct0
#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
Name:           fedfs-utils
Version:        0.10.7
Release:        0
Summary:        Utilities for mounting and managing FedFS
License:        GPL-2.0-only
URL:            http://wiki.linux-nfs.org/wiki/index.php/FedFsUtilsProject
# http://git.linux-nfs.org/?p=cel/fedfs-utils.git;a=summary
Source:         %{name}-%{version}.tar.gz
Source1:        sysconfig.fedfs
Patch0:         fedfs-utils-no-sunrpc.diff
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  libtool
BuildRequires:  openldap2-devel
BuildRequires:  pkgconfig
BuildRequires:  python-base
BuildRequires:  python-rpm-macros
BuildRequires:  rpcsvc-proto-devel
BuildRequires:  shadow
BuildRequires:  pkgconfig(krb5)
BuildRequires:  pkgconfig(libattr)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libconfig)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libidn)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(libtirpc)
BuildRequires:  pkgconfig(liburiparser)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(uuid)

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

%package common
Summary:        Common files for FedFS
BuildArch:      noarch

%description common
This package contains files common to all of the fedfs packages.

%package client
Summary:        Utilities for mounting FedFS domains
Requires:       %{name}-common = %{version}-%{release}
Requires:       nfs-client

%description client
This package contains the tools needed to mount a FedFS domain and act
as a client.

%package nsdbparams
Summary:        FedFS nsdbparams utility
Requires:       %{name}-common = %{version}-%{release}

%description nsdbparams
This package contains the nsdbparams utility, which is needed by both
the fedfs-server and fedfs-admin packages.

%package devel
Summary:        Development files and libraries for the nfs-plugin
Requires:       %{libname} = %{version}-%{release}
Requires:       %{name}-common = %{version}-%{release}

%description devel
This package contains the development files and libraries for the nfs-plugin.

%package -n %{libname}
Summary:        Runtime libraries for the nfs-plugin

%description -n %{libname}
This package contains runtime libraries for the nfs-plugin.

%package server
Summary:        Utilities for serving FedFS domains
Requires:       %{libname} = %{version}-%{release}
Requires:       %{name}-common = %{version}-%{release}
Requires:       %{name}-nsdbparams = %{version}-%{release}
Requires:       nfs-kernel-server

%description server
This package contains the tools needed to act as a FedFS server.

%package admin
Summary:        Utilities for administering FedFS domains
Requires:       %{name}-common = %{version}-%{release}
Requires:       %{name}-nsdbparams = %{version}-%{release}

%description admin
This package contains the tools needed to manage a FedFS domain.

%prep
%setup -q
%patch0

# disable -Werror
sed -i -e 's:-Werror\ ::g' configure.ac

%build
autoreconf -fvi
%define _sharedstatedir %{_localstatedir}/lib
%configure \
  --sysconfdir=%{_sysconfdir}/fedfs \
  --disable-static
%make_build

%install
%make_install
%fdupes %{buildroot}%{python2_sitelib}
mkdir -p %{buildroot}%{_sharedstatedir}/fedfs
install -Dm 644 contrib/init/rpcfedfsd.service %{buildroot}%{_unitdir}/rpcfedfsd.service
install -Dm 644 %{SOURCE1} %{buildroot}%{_fillupdir}/sysconfig.fedfs
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcrpcfedfsd
find %{buildroot} -type f -name "*.la" -delete -print

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

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files common
%license COPYING
%doc README ChangeLog doc/ldap/fedfs.schema doc/ldap/fedfs-schema.ldif
%{_mandir}/man7/fedfs.7%{?ext_man}

%files client
/sbin/mount.fedfs
%{_sbindir}/fedfs-map-nfs4
%{_mandir}/man8/mount.fedfs.8%{?ext_man}
%{_mandir}/man8/fedfs-map-nfs4.8%{?ext_man}

%files nsdbparams
%{_sbindir}/nsdbparams
%{_mandir}/man8/nsdbparams.8%{?ext_man}
%{_mandir}/man7/nsdb-parameters.7%{?ext_man}

%files devel
%{_includedir}/nfs-plugin.h
%{_libdir}/libnfsjunct.so

%files -n %{libname}
%{_libdir}/libnfsjunct.so.*

%files server
%dir %{_sharedstatedir}/fedfs
%{_sbindir}/nfsref
%{_sbindir}/rpc.fedfsd
%{_sbindir}/rcrpcfedfsd
%dir %{_sysconfdir}/fedfs
%config %{_sysconfdir}/fedfs/access.conf
%{_mandir}/man8/rpc.fedfsd.8%{?ext_man}
%{_mandir}/man8/nfsref.8%{?ext_man}
%{_unitdir}/rpcfedfsd.service
%{_fillupdir}/sysconfig.fedfs

%files admin
%{_bindir}/fedfs-domainroot
%{_bindir}/nsdb-jumpstart
%{python2_sitelib}/PyFedfs/
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
%{_mandir}/man8/fedfs-create-junction.8%{?ext_man}
%{_mandir}/man8/fedfs-create-replication.8%{?ext_man}
%{_mandir}/man8/fedfs-delete-junction.8%{?ext_man}
%{_mandir}/man8/fedfs-delete-replication.8%{?ext_man}
%{_mandir}/man8/fedfs-get-limited-nsdb-params.8%{?ext_man}
%{_mandir}/man8/fedfs-get-nsdb-params.8%{?ext_man}
%{_mandir}/man8/fedfs-lookup-junction.8%{?ext_man}
%{_mandir}/man8/fedfs-lookup-replication.8%{?ext_man}
%{_mandir}/man8/fedfs-null.8%{?ext_man}
%{_mandir}/man8/fedfs-set-nsdb-params.8%{?ext_man}
%{_mandir}/man8/fedfs-domainroot.8%{?ext_man}
%{_mandir}/man8/nsdb-*

%changelog
