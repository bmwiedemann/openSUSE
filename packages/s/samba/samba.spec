#
# spec file for package samba
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%{!?py3_soflags:  %global py3_soflags cpython-%{python3_version_nodots}m}
%{!?py3_soflags_dash:   %global py3_soflags_dash %(echo %{py3_soflags} | sed "s/_/-/g")}

#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

%{!?_tmpfilesdir:%global _tmpfilesdir /usr/lib/tmpfiles.d}

# mscat only builds with libgnutls >= 3.5.6 and libtasn1 >= 3.8 both
# of which are unavailable prior to SLE15sp1 and Leap15.1. Excluding
# these requires libtasn1 be bundled in older versions (otherwise
# configure fails), but mscat still can't build due to the libgnutls
# dependency.
%if 0%{?sle_version} <= 120300
%define with_mscat 0
%else
%if 0%{?suse_version} < 1500
%define with_mscat 0
%else
%define with_mscat 1
%endif
%endif

%if 0%{?suse_version} > 1140 && 0%{?suse_version} != 1315
%define         build_ctdb_pmda 1
%endif
%if 0%{?suse_version} > 1320 || 0%{?sle_version} > 120200
%ifarch aarch64 x86_64
%define         build_ceph 1
%endif
%endif

%define talloc_version 2.3.1
%define tevent_version 0.10.2
%define tdb_version    1.4.3
%define ldb_version    2.1.4

%global with_mitkrb5 1
%global with_dc 0
%if 0%{?suse_version} > 1320
%ifnarch ppc
%global with_dc 1
%endif
%endif

Name:           samba
BuildRequires:  autoconf
BuildRequires:  cups-devel
BuildRequires:  cyrus-sasl-devel
BuildRequires:  e2fsprogs-devel
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  patch
BuildRequires:  perl-Parse-Yapp
%if 0%{?suse_version} > 1300
BuildRequires:  libarchive-devel
%endif
%if 0%{?suse_version} > 1210
BuildRequires:  gamin-devel
%else
BuildRequires:  fam-devel
%endif
BuildRequires:  libacl-devel
BuildRequires:  libattr-devel
%if 0%{?suse_version} > 1100
BuildRequires:  libuuid-devel
%endif
BuildRequires:  cracklib-devel
BuildRequires:  gdbm-devel
BuildRequires:  keyutils-devel
BuildRequires:  libnscd-devel
%if 0%{?suse_version} >= 1330
BuildRequires:  libnsl-devel
%endif
BuildRequires:  libopenssl-devel
BuildRequires:  zlib-devel
%if 0%{?suse_version} >= 1330
BuildRequires:  libtirpc-devel
%endif
BuildRequires:  ncurses-devel
BuildRequires:  openldap2-devel
BuildRequires:  pam-devel
BuildRequires:  popt-devel
BuildRequires:  python3-devel
BuildRequires:  python3-xml
BuildRequires:  readline-devel
%if 0%{?suse_version} >= 1330
BuildRequires:  rpcgen
%endif
%if 0%{?suse_version} > 1110
BuildRequires:  fdupes
%endif
%define pkgconfig_req pkg-config
BuildRequires:  %{pkgconfig_req}
BuildRequires:  libldb-devel >= %{ldb_version}
BuildRequires:  libtalloc-devel >= %{talloc_version}
BuildRequires:  libtdb-devel >= %{tdb_version}
BuildRequires:  libtevent-devel >= %{tevent_version}
BuildRequires:  python3-ldb-devel >= %{ldb_version}
BuildRequires:  python3-talloc-devel
BuildRequires:  python3-tdb
BuildRequires:  python3-tevent
# to generate the man pages
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  libxslt
%if 0%{?suse_version} > 1210
BuildRequires:  dbus-1-devel
BuildRequires:  libxslt-tools
%endif
%if 0%{?suse_version} > 1220
BuildRequires:  libavahi-devel
# To only BuildRequire systemd-rpm-macros leads to broken binaries
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(systemd)
%endif
%if 0%{?build_ctdb_pmda}
BuildRequires:  libpcp-devel
%endif
%if 0%{?build_ceph}
BuildRequires:  libcephfs-devel
BuildRequires:  librados-devel
%endif
%if %{with_dc}
BuildRequires:  gpgme-devel
BuildRequires:  krb5-devel >= 1.15.1
BuildRequires:  krb5-server >= 1.15.1
BuildRequires:  libgnutls-devel >= 3.4.7
BuildRequires:  libjansson-devel
BuildRequires:  python3-gpgme
%else
BuildRequires:  krb5-devel
BuildRequires:  libgnutls-devel >= 3.2.0
%endif
%if %{with_mscat}
BuildRequires:  libgnutls-devel >= 3.5.6
BuildRequires:  libtasn1-devel >= 3.8
%endif

%define libsmbclient_name libsmbclient0
%define libnetapi_name libnetapi0
%define libwbclient_name libwbclient0
%if 0%{?suse_version} > 1140
%define	build_make_smp_mflags %{?_smp_mflags}
%else
%define	build_make_smp_mflags %{?jobs:-j%jobs}
%endif
Version:        4.13.0+git.138.ff2d5480c67
Release:        0
Url:            https://www.samba.org/
Obsoletes:      samba-32bit < %{version}
Obsoletes:      samba-gplv3 < %{version}
Recommends:     cron
Recommends:     logrotate
Summary:        A SMB/CIFS File, Print, and Authentication Server
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Samba
Source:         samba-%{version}.tar.bz2
Source4:        baselibs.conf
Source100:      samba-client-rpmlintrc
Requires(pre):  /usr/bin/getent
Requires(pre):  /usr/sbin/groupadd
Requires:       system-user-nobody
Requires:       coreutils
Requires:       grep
%if 0%{?suse_version} > 1220
Requires:       %{fillup_prereq}
%endif
Requires:       samba-client >= %{version}
# Choose some features / extra packages here
############################################
%if 0%{?suse_version} > 1120
%define cifs_init_script cifs
%else
%define cifs_init_script smbfs
%endif
# Define some global directories
################################
%define	DOCDIR %{_defaultdocdir}/samba
%define	DOCBOOKDIR %{_defaultdocdir}/samba/docbook
%define	LOGDIR %{_localstatedir}/log/samba
%define	LOCKDIR %{_localstatedir}/lib/samba
%define	CONFIGDIR %{_sysconfdir}/samba
%define	INITDIR %{_sysconfdir}/init.d
%if 0%{?suse_version} > 1220
%define	PIDDIR /run/samba
%else
%define	PIDDIR %{_localstatedir}/run/samba
%endif
%define	NET_CFGDIR network
%define	auth_modules auth_unix,auth_wbc,auth_server,auth_netlogond,auth_script,auth_samba4
%define	idmap_modules idmap_ad,idmap_adex,idmap_hash,idmap_ldap,idmap_rfc2307,idmap_rid,idmap_tdb2
%define	pdb_modules pdb_tdbsam,pdb_ldap,pdb_ads,pdb_smbpasswd,pdb_wbc_sam,pdb_samba4
%define	vfs_modules vfs_cacheprime,vfs_readahead
%define	VENDOR SUSE
%if 0%{?suse_version} > 1120
%define cups_lib_dir %{_prefix}/lib/cups
%else
%define cups_lib_dir %{_libdir}/cups
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Samba is a suite of programs that allows SMB/CIFS clients to use the
Unix file space, printers, and authentication subsystem.

The package named samba contains all programs that are needed to act as
a server.  The binaries expect the configuration file to be found in
/etc/samba/smb.conf

For a more detailed description of Samba, check the samba-doc package
or the Samba.org Web page at https://www.Samba.org/

Please check https://en.openSUSE.org/Samba for general information on
Samba as part of SUSE Linux Enterprise or openSUSE products, links to
binary packages of the most current Samba version, and a bug reporting
how to.



%package client
Summary:        Samba Client Utilities
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Samba
Provides:       smbfs
Obsoletes:      samba-client-gplv2 < %{version}
Obsoletes:      samba-gplv3-client < %{version}
%if 0%{?suse_version} < 1221
Requires:       %{?insserv_prereq}
Requires:       /sbin/chkconfig
%endif
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Requires:       coreutils
%{?systemd_requires}
Requires:       cifs-utils

%description client
Samba is a suite of programs that allows SMB/CIFS clients to use the
Unix file space, printers, and authentication subsystem.

The package named samba-client contains all programs that are needed to
act as a Samba client. The binaries expect the configuration file to
be found in /etc/samba/smb.conf

For a more detailed description of Samba, check the samba-doc package
or the Samba.org Web page at https://www.Samba.org/

Please check https://en.openSUSE.org/Samba for general information on
Samba as part of SUSE Linux Enterprise or openSUSE products, links to
binary packages of the most current Samba version, and a bug reporting
how to.



%package core-devel
Summary:        Development files shared by Samba subpackages
License:        GPL-3.0-or-later
Group:          Development/Libraries/C and C++
Conflicts:      samba-devel

%description core-devel
This package contains the libraries and header files needed to
develop programs which make use of Samba.

%package doc
Summary:        Samba Documentation
License:        GPL-3.0-or-later
Group:          Documentation/Other
Requires:       coreutils
Requires:       findutils
Obsoletes:      samba-doc-gplv2 < %{version}
Obsoletes:      samba-gplv3-doc < %{version}
%if 0%{?suse_version} > 1110
BuildArch:      noarch
%endif

%description doc
This package contains all the Samba documentation as it is not part of
the man pages.

%package libs
Summary:        Samba libraries
License:        GPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       krb5
%if 0%{?suse_version} > 1210 && 0%{?suse_version} < 1315
Requires:       libfam0-gamin
%endif
Requires:       samba-libs-python3 = %{version}

%description libs
The samba-libs package contains the libraries needed by programs that
link against the SMB, RPC and other protocols provided by the Samba suite.

%package libs-python3
Summary:        Python3 dependencies of samba-libs
License:        GPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       python3

%description libs-python3
Dependencies of samba-libs that require python3.

%package python3
Summary:        Samba Python3 libraries
License:        GPL-3.0-or-later
Group:          Development/Libraries/Python
Requires:       %{name} = %{version}
Requires:       python3-ldb
Requires:       python3-talloc
Requires:       python3-tdb
Requires:       python3-tevent
Requires:       libsamba-policy0-python3 = %{version}

%description python3
The samba-python3 package contains the Python libraries needed by programs
that use SMB, RPC and other Samba provided protocols in Python3 programs.

%package test
Summary:        Testing tools for Samba servers and clients
License:        GPL-3.0-or-later
Group:          Applications/System
Requires:       samba = %{version}
Requires:       samba-winbind = %{version}

%description test
samba-test provides testing tools for both the server and client
packages of Samba.



%package winbind
Summary:        Winbind Daemon and Tool
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Samba
Obsoletes:      samba-gplv3-winbind < %{version}
Provides:       samba-client:/usr/sbin/winbindd
Requires:       pam-config
Recommends:     cron
Recommends:     logrotate
Recommends:     /usr/sbin/nscd
%if 0%{?suse_version} < 1221
Requires:       %{?insserv_prereq}
%endif
Requires(pre):  /usr/sbin/groupadd
Requires:       coreutils
Requires:       samba-client >= %{version}
Requires:       libtevent-util0 >= %{version}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description winbind
This is the winbind-daemon and the wbinfo-tool.



%package -n ctdb
Summary:        Clustered TDB
License:        GPL-3.0-or-later
Group:          System/Daemons
Requires(pre):  %{?fillup_prereq}
%if 0%{?suse_version} > 1220
BuildRequires:  systemd-rpm-macros
# bnc886095: The CTDB resource agent could be split out into a separate rpm,
# with corresponding ctdb and tdb-tools requirements. Until then, just add the
# tdb-tools requirement to ctdb.
Requires:       tdb-tools
%else
Requires(pre):  %{insserv_prereq}
%endif
Requires(pre): coreutils
Requires(pre): /bin/mktemp
Requires(pre): /usr/bin/killall
Requires(pre): sed

%description -n ctdb
ctdb is the clustered database used by Samba

%package -n ctdb-pcp-pmda
Summary:        Performance Co-Pilot (PCP) monitoring agent
License:        GPL-3.0-or-later
Group:          System/Monitoring

%description -n ctdb-pcp-pmda
The CTDB Performance Co-Pilot (PCP) monitoring agent allows remote PCP
clients to view and capture detailed real-time performance metrics for
one or more cluster nodes.

%package -n ctdb-tests
Summary:        CTDB clustered database test suite
License:        GPL-3.0-or-later
Group:          Development/Tools

%description -n ctdb-tests
Test suite for clustered database (CTDB).


%package -n libdcerpc-binding0
Summary:        Some samba library
License:        GPL-3.0-or-later
Group:          System/Libraries

%description -n libdcerpc-binding0
This subpackage contains utility functions to handle DCE/RPC binding
strings.

%package -n libdcerpc-samr0
Summary:        Security Account Manager (SAM) Remote Protocol library
License:        GPL-3.0-or-later
Group:          System/Libraries

%description -n libdcerpc-samr0
This subpackage contains NDR marshallers for the SAMR protocol.


%package -n libdcerpc-samr-devel
Summary:        Development files for the SAMR protocol library
License:        GPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       libdcerpc-samr0 = %{version}

%description -n libdcerpc-samr-devel
This subpackage contains libraries and header files for developing
applications that want to make use of libdcerpc-samr.



%package -n libdcerpc0
Summary:        Distributed Computing Environment Remote Procedure Calls library
License:        GPL-3.0-or-later
Group:          System/Libraries

%description -n libdcerpc0
DCE/RPC, short for "Distributed Computing Environment / Remote
Procedure Calls", is the remote procedure call system developed for
the Distributed Computing Environment (DCE). This system allows
programmers to write distributed software as if it were all working
on the same computer, without having to worry about the underlying
network code.



%package -n libdcerpc-devel
Summary:        Development files for the DCE/RPC library
License:        GPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       libdcerpc-binding0 = %{version}
Requires:       libdcerpc0 = %{version}
Requires:       samba-core-devel = %{version}

%description -n libdcerpc-devel
DCE/RPC, short for "Distributed Computing Environment / Remote
Procedure Calls", is the remote procedure call system developed for
the Distributed Computing Environment (DCE). This system allows
programmers to write distributed software as if it were all working
on the same computer, without having to worry about the underlying
network code.

This subpackage contains libraries and header files for developing
applications that want to make use of libdcerpc.



%package -n libndr-krb5pac0
Summary:        NDR marshallers for the KRB5 PAC formats
License:        GPL-3.0-or-later
Group:          System/Libraries

%description -n libndr-krb5pac0
This subpackage contains NDR marshallers for the Kerberos Privilege
Attribute Certificate Data Structure (PAC).


%package -n libndr-krb5pac-devel
Summary:        Development files for the ndr-krb5pac library
License:        GPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       libndr-krb5pac0 = %{version}
Requires:       samba-core-devel = %{version}

%description -n libndr-krb5pac-devel
This subpackage contains libraries and header files for developing
applications that want to make use of libndr-krb5pac.



%package -n libndr-nbt0
Summary:        NDR marshallers for NBT formats
License:        GPL-3.0-or-later
Group:          System/Libraries

%description -n libndr-nbt0
This subpackage contains NDR marshallers for the NetBIOS protocol.



%package -n libndr-nbt-devel
Summary:        Development files for the ndr-nbt library
License:        GPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       libndr-nbt0 = %{version}
Requires:       samba-core-devel = %{version}

%description -n libndr-nbt-devel
This subpackage contains libraries and header files for developing
applications that want to make use of libndr-nbt.



%package -n libndr-standard0
Summary:        NDR marshallers for the standard set of DCE/RPC interfaces
License:        GPL-3.0-or-later
Group:          System/Libraries

%description -n libndr-standard0
This subpackage contains NDR encoders/decoders for the set of standard
DCE/RPC interfaces found on Windows and Samba servers.



%package -n libndr-standard-devel
Summary:        Development files for the libndr-standard library
License:        GPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       libndr-standard0 = %{version}
Requires:       samba-core-devel = %{version}

%description -n libndr-standard-devel
This subpackage contains libraries and header files for developing
applications that want to make use of libndr-standard.



%package -n libndr1
Summary:        Network Data Representation library
License:        GPL-3.0-or-later
Group:          System/Libraries
Provides:       libndr0
Obsoletes:      libndr0

%description -n libndr1
Network Data Representation (NDR) is an implementation of the
presentation layer in the OSI model.



%package -n libndr-devel
Summary:        Development files for the Network Data Representation library
License:        GPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       libndr1 = %{version}
Requires:       samba-core-devel = %{version}

%description -n libndr-devel
Network Data Representation (NDR) is an implementation of the
presentation layer in the OSI model.

This subpackage contains libraries and header files for developing
applications that want to make use of libndr.



%package -n libsamba-credentials0
Summary:        Samba credential management library
License:        GPL-3.0-or-later
Group:          System/Libraries

%description -n libsamba-credentials0
This subpackage contains libraries for credentials management.


%package -n libsamba-credentials-devel
Summary:        Development files for the Samba credential management library
License:        GPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       libsamba-credentials0 = %{version}

%description -n libsamba-credentials-devel
This subpackage contains libraries and header files for developing
applications that want to make use of libsamba-credentials.



%package -n libsamba-errors0
Summary:        Samba errors handling library
License:        GPL-3.0-or-later
Group:          System/Libraries

%description -n libsamba-errors0
This subpackage contains libraries to handle and translate NT error codes.


%package -n libsamba-errors-devel
Summary:        Development files for the Samba errors handling library
License:        GPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       libsamba-errors0 = %{version}

%description -n libsamba-errors-devel
This subpackage contains libraries and header files for developing
applications that want to make use of libsamba-errors.



%package -n libsamba-hostconfig0
Summary:        Host-wide Samba configuration library
License:        GPL-3.0-or-later
Group:          System/Libraries

%description -n libsamba-hostconfig0
This subpackage contains libraries for accessing the samba host-specific
configuration files.


%package -n libsamba-hostconfig-devel
Summary:        Development files for the host-wide Samba configuration library
License:        GPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       libsamba-hostconfig0 = %{version}
Requires:       samba-core-devel = %{version}

%description -n libsamba-hostconfig-devel
This subpackage contains libraries and header files for developing
applications that want to make use of libsamba-hostconfig.



%package -n libsamba-passdb0
Summary:        Samba3 password database library
License:        GPL-3.0-or-later
Group:          System/Libraries
Obsoletes:      libpdb0 < %{version}

%description -n libsamba-passdb0
This subpackage contains libraries to interface the password database.


%package -n libsamba-passdb-devel
Summary:        Development files for the Samba3 password database library
License:        GPL-3.0-or-later
Group:          Development/Libraries/C and C++
Provides:       libpdb-devel
Obsoletes:      libpdb-devel
Requires:       libndr-standard-devel = %{version}
Requires:       libsamba-passdb0 = %{version}
Requires:       libtevent-devel

%description -n libsamba-passdb-devel
This subpackage contains libraries and header files for developing
applications that want to make use of libsamba-passdb.


%package -n libsamba-policy0-python3
Summary:        Active Directory Group Policy library
License:        GPL-3.0-or-later
Group:          System/Libraries

%description -n libsamba-policy0-python3
This subpackage contains the python3 library for policy management.

%package -n libsamba-policy-devel
Summary:        Development files for the Samba AD Group Policy library
License:        GPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       libsamba-policy-python3-devel = %{version}

%description -n libsamba-policy-devel
This subpackage contains libraries and header files for developing
applications that want to make use of libsamba-policy.

%package -n libsamba-policy-python3-devel
Summary:        Development files for the Samba AD Group Policy library
License:        GPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       libsamba-policy0-python3 = %{version}

%description -n libsamba-policy-python3-devel
This subpackage contains libraries and header files for developing
applications that want to make use of libsamba-policy.

%package -n libsamba-util0
Summary:        Samba utility function library
License:        GPL-3.0-or-later
Group:          System/Libraries

%description -n libsamba-util0
This subpackage contains generic data structures and functions used
within Samba.



%package -n libsamba-util-devel
Summary:        Development files for the Samba utility function library
License:        GPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       libsamba-util0 = %{version}
Requires:       samba-core-devel = %{version}

%description -n libsamba-util-devel
This subpackage contains libraries and header files for developing
applications that want to make use of libsamba-util.



%package -n libsamdb0
Summary:        Samba's SAM database library
License:        GPL-3.0-or-later
Group:          System/Libraries

%description -n libsamdb0
This subpackage contains libraries for accessing the SAM database.



%package -n libsamdb-devel
Summary:        Development files for Samba's SAM database library
License:        GPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       libsamdb0 = %{version}

%description -n libsamdb-devel
This subpackage contains libraries and header files for developing
applications that want to make use of libsamdb.



%package -n libsmbconf0
Summary:        Samba3 configuration library
License:        GPL-3.0-or-later
Group:          System/Libraries

%description -n libsmbconf0
libsmbconf is a library to read or, based on the backend, modify the
Samba configuration.



%package -n libsmbconf-devel
Summary:        Development files for the Samba3 configuration library
License:        GPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       libsmbconf0 = %{version}

%description -n libsmbconf-devel
libsmbconf is a library to read or, based on the backend, modify the
Samba configuration.

This subpackage contains libraries and header files for developing
applications that want to make use of libsmbconf.



%package -n libsmbldap2
Summary:        Samba LDAP protocol helper function library
License:        GPL-3.0-or-later
Group:          System/Libraries

%description -n libsmbldap2
libsmbldap contains LDAP protocol helper functions for Samba.



%package -n libsmbldap-devel
Summary:        Development files for the smbldap library
License:        GPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       libsmbldap2 = %{version}
Requires:       libtalloc-devel
Requires:       libtevent-devel
Requires:       openldap2-devel

%description -n libsmbldap-devel
libsmbldap contains LDAP protocol helper functions for Samba.

This subpackage contains libraries and header files for developing
applications that want to make use of libsmbldap.



%package -n libtevent-util0
Summary:        Samba tevent <-> system status code conversion utility library
License:        GPL-3.0-or-later
Group:          System/Libraries

%description -n libtevent-util0
The libtevent-util library contains functions to convert tevent error
codes to platform-specific (errno, NTSTATUS, WERROR) ones.



%package -n libtevent-util-devel
Summary:        Development files for the Samba tevent utility library
License:        GPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       libtevent-devel
Requires:       libtevent-util0 = %{version}
Requires:       samba-core-devel = %{version}

%description -n libtevent-util-devel
The libtevent-util library contains functions to convert tevent error
codes to platform-specific (errno, NTSTATUS, WERROR) ones.

This subpackage contains libraries and header files for developing
applications that want to make use of libtevent-util.



%package -n %{libsmbclient_name}
Obsoletes:      libsmbclient < %{version}
Summary:        Samba Client Library
License:        GPL-3.0-or-later
Group:          System/Libraries

%description -n %{libsmbclient_name}
This package includes the libsmbclient library.

libsmbclient is provided by the libsmbclient0 package.



%package -n libsmbclient-devel
Summary:        Libraries and Header Files to Develop Programs with smbclient Support
License:        GPL-3.0-or-later
Group:          Development/Libraries/C and C++
BuildRequires:  %{pkgconfig_req}
Requires:       %{libsmbclient_name} = %{version}
Requires:       krb5-devel

%description -n libsmbclient-devel
This package contains the static libraries and header files needed to
develop programs which make use of the smbclient programming interface.



%package -n %{libnetapi_name}
Summary:        Samba netapi Library
License:        GPL-3.0-or-later
Group:          System/Libraries

%description -n %{libnetapi_name}
This package includes the netapi library.



%package -n libnetapi-devel
Summary:        Libraries and Header Files to Develop Programs with netapi Support
License:        GPL-3.0-or-later
Group:          Development/Libraries/C and C++
BuildRequires:  %{pkgconfig_req}
Requires:       %{libnetapi_name} = %{version}

%description -n libnetapi-devel
This package contains the static libraries and header files needed to
develop programs which make use of the netapi programming interface.



%package -n %{libwbclient_name}
Summary:        Samba libwbclient Library
License:        LGPL-3.0-or-later
Group:          System/Libraries

%description -n %{libwbclient_name}
This package includes the wbclient library.



%package -n libwbclient-devel
Summary:        Libraries and Header Files to Develop Programs with wbclient Support
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
BuildRequires:  %{pkgconfig_req}
Requires:       %{libwbclient_name} = %{version}

%description -n libwbclient-devel
This package contains the static libraries and header files needed to
develop programs which make use of the wbclient programming interface.

%package ceph
Summary:        Ceph specific add-ons for Samba
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Samba
Requires:       samba = %{version}

%description ceph
The Ceph VFS module for Samba allows shares to be backed by the Ceph
distributed file system. A Ceph CTDB lock helper binary is included so
that RADOS locks can be used for CTDB split-brain avoidance.

%package ad-dc
Summary:        Samba Active Directory-compatible Domain Controller
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Samba
Requires:       samba = %{version}
Requires:       samba-dsdb-modules = %{version}
Recommends:     krb5-server >= 1.15.1
Requires:       samba-python3 = %{version}
Recommends:     samba-winbind = %{version}
Recommends:     tdb-tools >= %{tdb_version}
Provides:       samba-kdc = %{version}
Obsoletes:      samba-kdc < %{version}

%description ad-dc
This package contains the Active Directory-compatible Domain Controller

%package dsdb-modules
Summary:        Samba LDB modules
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Samba
Requires:       libldb2 >= %{ldb_version}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description dsdb-modules
This package contains plugins which add Active Directory features to the
LDB library.

%prep
%setup -n samba-%{version} -q
# vendor-files (config, scripts, tools)
install -m 0644 -p packaging/SuSE/docu/rfc3454.txt source4/heimdal/lib/wind/
# Create and add vendor suffix
if test "%{_project}" != "openSUSE:Factory"; then
	vendor_tag_release=$( grep -m 1 ^Release: %{_sourcedir}/samba.spec | \
		while read tag release; do \
			echo -n "${release:+${release}-}"; \
		done)
else
	vendor_tag_release=""
fi
# ensure Git commit portion of version string is retained
vendor_tag=$(echo -n %{version} | sed "s/.*+git/git/"; \
	echo -n "${vendor_tag_release}" )
# Create product suffix
test 0%{?centos_version} -gt 0 && product_version=%{?centos_version}
test 0%{?fedora_version} -gt 0 && product_version=%{?fedora_version}
test 0%{?mandriva_version} -gt 0 && product_version=%{?mandriva_version}
test 0%{?rhel_version} -gt 0 && product_version=%{?rhel_version}
test 0%{?suse_version} -gt 0 && product_version=%{?suse_version}
major_version=$((${product_version}/100))
minor_version=$((${product_version}/10))
minor_version="${minor_version#$major_version}"
product_version="${major_version}.${minor_version}"
case "%{suse_version}" in
	1010) product_suffix="-SLE_10" ;;
	1110) product_suffix="-SLE_11" ;;
	1315) product_suffix="-SLE_12" ;;
	*) product_suffix="-oS${product_version}" ;;
esac
# Add the build architecture
test "%{_build_arch}" != "" && \
	product_suffix="${product_suffix}-%{_build_arch}"
# Set SAMBA_VERSION_VENDOR_SUFFIX in the VERSION file
mv VERSION VERSION.orig
sed -e "s/^SAMBA_VERSION_VENDOR_SUFFIX=$/SAMBA_VERSION_VENDOR_SUFFIX=${vendor_tag}%{VENDOR}${product_suffix}/" VERSION.orig >VERSION

%build
if command -v ncurses6-config &> /dev/null; then
	export NCURSES_CONFIG="$(command -v ncurses6-config)"
fi

export CFLAGS="%{optflags} -D_GNU_SOURCE -D_LARGEFILE64_SOURCE -DIDMAP_RID_SUPPORT_TRUSTED_DOMAINS -I/usr/include/tirpc"
%if 0%{?suse_version} >= 1330
export LDFLAGS="-ltirpc"
%endif
%if 0%{?suse_version} < 1141
%{?suse_update_config:%{suse_update_config -f}}
%endif
%if 0%{?suse_version} < 1111
bundled_libraries_extra="libarchive"
%endif
%if ! 0%{?with_mscat}
bundled_libraries_extra+=",libtasn1"
%endif
CONFIGURE_OPTIONS="\
	--prefix=%{_prefix} \
	--localstatedir=%{_localstatedir} \
	--sysconfdir=%{_sysconfdir} \
	--libdir=%{_libdir} \
	--libexecdir=%{_libdir} \
	--with-cachedir=%{LOCKDIR} \
	--with-lockdir=%{LOCKDIR}/lock \
	--with-logfilebase=%{LOGDIR} \
	--with-modulesdir=%{_libdir}/samba \
	--disable-rpath \
	--disable-rpath-install \
	--enable-debug \
%if 0%{?build_ctdb_pmda}
	--enable-pmda \
%endif
	--enable-fhs \
	--with-cluster-support \
	--with-socketpath=%{_localstatedir}/lib/ctdb/ctdb.socket \
%if 0%{?build_ceph}
	--enable-ceph-reclock \
%endif
	--with-pam \
	--with-pammodulesdir=/%{_lib}/security \
	--with-piddir=%{PIDDIR} \
	--with-relro \
%if 0%{?suse_version} > 1220
	--enable-avahi \
	--with-systemd \
%endif
	--with-shared-modules=%{auth_modules},%{vfs_modules},%{pdb_modules},%{idmap_modules} \
%if %with_mitkrb5
	--with-system-mitkrb5 \
%endif
%if ! %{with_dc}
	--without-ad-dc \
	--without-json \
	--without-gpgme \
%else
%if %{with_mitkrb5}
	--with-experimental-mit-ad-dc \
%endif
%endif
	--bundled-libraries=NONE,socket_wrapper,cmocka,${bundled_libraries_extra} \
"
./configure ${CONFIGURE_OPTIONS}
make %{build_make_smp_mflags} \
	all

pushd docs-xml
autoconf && ./configure
XML_CATALOG_FILES="file:///etc/xml/catalog file://$(pwd)/build/catalog.xml" make htmlman
popd

pushd ctdb
XML_CATALOG_FILES="file:///etc/xml/catalog file://$(pwd)/build/catalog.xml" make manpages
popd

%install
install -d -m 0755 -p \
	%{buildroot}/%{_sysconfdir}/{pam.d,xinetd.d,logrotate.d} \
	%{buildroot}/%{_sysconfdir}/openldap/schema \
	%{buildroot}/%{_sysconfdir}/sysconfig/%{NET_CFGDIR}/{if-{down,up}.d,scripts} \
%if 0%{?suse_version} <= 1500
	%{buildroot}/%{_sysconfdir}/sysconfig/SuSEfirewall2.d/services \
%endif
	%{buildroot}/%{_sysconfdir}/security \
	%{buildroot}/%{_sysconfdir}/slp.reg.d \
	%{buildroot}/%{CONFIGDIR} \
%if 0%{?suse_version} > 1220
	%{buildroot}/%{_unitdir} \
%else
	%{buildroot}/%{INITDIR} \
%endif
	%{buildroot}/%{_lib}/security \
	%{buildroot}/sbin \
	%{buildroot}/%{_includedir} \
	%{buildroot}/%{_libdir}/pkgconfig \
	%{buildroot}/%{_libdir}/python/lib-dynload \
	%{buildroot}/%{_libdir}/samba/{config,vfs,rpc,auth,charset,idmap} \
	%{buildroot}/%{_datadir}/omc/svcinfo.d \
	%{buildroot}/%{_datadir}/samba/{LDAP,templates} \
	%{buildroot}/%{_localstatedir}/adm \
	%{buildroot}/%{_localstatedir}/lib/ctdb/persistent \
	%{buildroot}/%{LOCKDIR}/{drivers/{WIN40,W32X86,W32MIPS,W32ALPHA,W32PPC,IA64,x64},netlogon,lock/msg.lock,printing,private/msg.sock,profiles,winbindd_privileged} \
	%{buildroot}/%{LOGDIR} \
	%{buildroot}/%{PIDDIR} \
	%{buildroot}/%{_fillupdir} \
	%{buildroot}/%{_var}/cache/krb5rcache \
	%{buildroot}/%{_var}/log/ctdb \
	%{buildroot}/%{DOCDIR} \
	%{buildroot}/%{DOCBOOKDIR} \
	%{buildroot}/%{_datadir}/susehelp/meta/Administration/System

make install \
	DESTDIR=%{buildroot} \
	CONFIGDIR=%{CONFIGDIR}

# debug symbols are created and installed if the files are excluded only
%if ! %{with_dc}
rm \
	%{buildroot}/%{_libdir}/samba/ldb/ildap.so \
	%{buildroot}/%{_libdir}/samba/ldb/ldbsamba_extensions.so \
	%{buildroot}/%{_mandir}/man8/samba.8* \
	%{buildroot}/%{_mandir}/man8/samba-tool.8* \
	%{buildroot}/%{_mandir}/man8/samba_downgrade_db.8*
%endif

# CTDB
install -m 0644 packaging/SuSE/config/sysconfig.ctdb %{buildroot}/%{_fillupdir}
%if 0%{?suse_version} > 1220
install -m 0755 ctdb/config/ctdb.service %{buildroot}%{_unitdir}/ctdb.service
ln -s service %{buildroot}/%{_sbindir}/rcctdb
# create tmpfile conf
install -d -m 0755 %{buildroot}/%{_tmpfilesdir}
echo "d /run/ctdbd 0755 root root" >%{buildroot}/%{_tmpfilesdir}/ctdb.conf
%else
install -m 0755 ctdb/config/ctdb.init %{buildroot}/%{INITDIR}/ctdb
ln -s %{_sysconfdir}/init.d/ctdb %{buildroot}/%{_sbindir}/rcctdb
%endif
mkdir %{buildroot}/%{_defaultdocdir}/ctdb
for file in README COPYING doc/examples doc/*.html doc/readonlyrecords.txt doc/recovery-process.txt ; do
	cp -a ctdb/${file} %{buildroot}/%{_defaultdocdir}/ctdb
done
touch %{buildroot}/%{_sysconfdir}/ctdb/nodes
# sudo can be used by statd-callout, but is not needed
rm %{buildroot}/%{_sysconfdir}/sudoers.d/ctdb
# install the config_migrate.sh script to move to new 4.9+ ctdb configuration
install -m 0744 ctdb/doc/examples/config_migrate.sh %{buildroot}/%{_sysconfdir}/ctdb/config_migrate.sh

# utility scripts
scripts="creategroup mksmbpasswd.sh"
install -d -m 0755 examples/scripts
for i in $scripts; do
	install -m 0755 "source3/script/${i}" examples/scripts/${i}
done
# configuration files
pushd packaging/SuSE/
echo "# smb.conf is the main Samba configuration file. You find a full commented" >config/smb.conf
echo "# version at %{DOCDIR}/examples/smb.conf.%{VENDOR} if the" >>config/smb.conf
echo "# samba-doc package is installed." >>config/smb.conf
grep -v "\(^#\|^;\|^$\)" config/smb.conf.vendor >>config/smb.conf
install -p -m 0644 config/smb.conf.vendor ../../examples/smb.conf.%{VENDOR}
for file in smb.conf lmhosts smbusers smbpasswd smbusers; do
	install -m 0644 "config/${file}" %{buildroot}/%{CONFIGDIR}/${file}
done
%if 0%{?suse_version} < 1221
	install -m 0644 -p config/cifstab %{buildroot}/%{CONFIGDIR}/%{cifs_init_script}tab
%endif
section_names=$( sed -ne 's/^\[\(.*\)\]$/\1/p' config/smb.conf)
for section in $section_names; do
%if 0%{?suse_version} < 1211
	LD_LIBRARY_PATH=../source3/bin/ \
%endif
	../source3/bin/testparm -s --section-name "${section}" config/smb.conf >"%{buildroot}/%{_datadir}/samba/templates/default-${section}" || :
done
for file in config/templates/*; do
	cp -a "${file}" "%{buildroot}/%{_datadir}/samba/templates/"
done
# start scripts
scriptSuffix=""
if test 0%{?suse_version} -lt 901; then
	scriptSuffix="-900"
elif test 0%{?suse_version} -lt 1011; then
	scriptSuffix="-1010"
elif test 0%{?suse_version} -lt 1111; then
	scriptSuffix="-1110"
elif test 0%{?suse_version} -lt 1131; then
	scriptSuffix="-1130"
fi
startScripts="smb nmb winbind"
%if 0%{?suse_version} < 1221
	startScripts="${startScripts} %{cifs_init_script}"
%endif
%if 0%{?suse_version} > 1220
for srv_name in nmb smb winbind; do
	install -m 0644 -p systemd/${srv_name}.service %{buildroot}/%{_unitdir}
	ln -s service %{buildroot}/%{_sbindir}/rc${srv_name}
done
%if %{with_dc}
	install -m 0644 -p systemd/samba-ad-dc.service %{buildroot}/%{_unitdir}
	ln -s service %{buildroot}/%{_sbindir}/rcsamba-ad-dc
%endif
install -m 0644 systemd/sysconfig.* %{buildroot}%{_fillupdir}
install -m 0644 -p ../systemd/samba.conf.tmp %{buildroot}/%{_tmpfilesdir}/samba.conf
%else
for script in ${startScripts}; do
	install -m 0755 "init/${script}${scriptSuffix}" \
		"%{buildroot}/%{INITDIR}/${script}"
	ln -s "%{INITDIR}/${script}" "%{buildroot}/%{_sbindir}/rc${script}"
done
%endif
for script in ${startScripts}; do
	SERVICE_NAME=$( echo "${script}" | tr [:lower:] [:upper:])
	sed \
		-e "s#__SERVICE_NAME#${SERVICE_NAME}#g" \
		-e "s#__SERVICE_SCRIPT_NAME#${script}#g" \
			init/template.xml \
			>"%{buildroot}/%{_datadir}/omc/svcinfo.d/${script}.xml"
done
install -m 0755 tools/nmbstatus %{buildroot}/%{_bindir}/nmbstatus
pod2man tools/nmbstatus >%{buildroot}/%{_mandir}/man1/nmbstatus.1
install -m 0755 tools/update-apparmor-samba-profile \
	%{buildroot}/%{_datadir}/samba/
# PDF generator
install -p -m 0755 tools/smbprngenpdf %{buildroot}/%{_bindir}/smbprngenpdf
install -m 0644 config/samba.reg %{buildroot}/%{_sysconfdir}/slp.reg.d/samba.reg
install -m 0644 config/samba.pamd-common %{buildroot}/%{_sysconfdir}/pam.d/samba
install -m 0644 config/dhcp.conf %{buildroot}/%{_fillupdir}/samba-client-dhcp.conf
install -m 0644 config/sysconfig.dhcp-samba-client %{buildroot}/%{_fillupdir}/sysconfig.dhcp-samba-client
for script in samba-winbindd; do
	install -m 0755 "tools/${script}" "%{buildroot}/%{_sysconfdir}/sysconfig/%{NET_CFGDIR}/scripts/${script}"
done
%if 0%{?suse_version} < 1221
	touch %{buildroot}/var/run/%{cifs_init_script}
%if 0%{?suse_version} < 1121
	sed -e 's/cifs/smbfs/g' tools/cifs >%{buildroot}/%{_sysconfdir}/sysconfig/%{NET_CFGDIR}/scripts/%{cifs_init_script}
	touch --reference=tools/cifs %{buildroot}/%{_sysconfdir}/sysconfig/%{NET_CFGDIR}/scripts/%{cifs_init_script}
%else
	install -m 0755 -p tools/cifs %{buildroot}/%{_sysconfdir}/sysconfig/%{NET_CFGDIR}/scripts/%{cifs_init_script}
%endif
%endif
# Create ghosts for the symlinks
for script in 55-samba-winbindd; do
	touch %{buildroot}/%{_sysconfdir}/sysconfig/%{NET_CFGDIR}/if-{down,up}.d/${script}
done
%if 0%{?suse_version} < 1221
	touch %{buildroot}/%{_sysconfdir}/sysconfig/%{NET_CFGDIR}/if-{down,up}.d/21-%{cifs_init_script}
%endif
%if 0%{?suse_version} <= 1500
# Install SuSEfirewall2 config files
install -m 0644 config/sysconfig.firewall.netbios-server \
	%{buildroot}%{_sysconfdir}/sysconfig/SuSEfirewall2.d/services/netbios-server
install -m 0644 config/sysconfig.firewall.samba-server \
	%{buildroot}%{_sysconfdir}/sysconfig/SuSEfirewall2.d/services/samba-server
%if 0%{?suse_version} > 1100
install -m 0644 config/sysconfig.firewall.samba-client \
	%{buildroot}%{_sysconfdir}/sysconfig/SuSEfirewall2.d/services/samba-client
%endif
%endif
# Add logrotate settings for nmbd and smbd only on systems newer than 8.1.
	LOGROTATE_FILES="samba samba-winbind"
for file in ${LOGROTATE_FILES}; do
	install -m 0644 logrotate/${file} %{buildroot}/%{_sysconfdir}/logrotate.d/${file}
	rm -f "%{_builddir}/samba-%{version}/filelist-${file}"
	touch "%{_builddir}/samba-%{version}/filelist-${file}"
	echo "%config(noreplace) %{_sysconfdir}/logrotate.d/${file}" >>%{_builddir}/samba-%{version}/filelist-${file}
done
install -m 0644 docu/README.SUSE %{buildroot}/%{DOCDIR}/
# SUSEhelp files
install -m 0644 docu/Samba.desktop %{buildroot}/%{_datadir}/susehelp/meta/Administration/System/Samba.desktop
install -d -m 0755 -p ../../docs/htmldocs
install -m 0644 docu/manpages.html ../../docs/htmldocs/manpages.html
install -m 0644 ../../docs-xml/output/htmldocs/manpages/* ../../docs/htmldocs/
popd
# winbind stuff
install -m 0644 examples/pam_winbind/pam_winbind.conf %{buildroot}/%{_sysconfdir}/security/pam_winbind.conf
# install nsswitch-headers (for squid, etc. #FIXME)
install -d -m 0755 \
	%{buildroot}/%{_includedir}/samba/nsswitch \
	%{buildroot}/%{_includedir}/samba/winbindd
for file in winbind_client.h winbind_nss_config.h winbind_nss_linux.h; do
	install -m 0644 "nsswitch/${file}" %{buildroot}/%{_includedir}/samba/nsswitch/${file}
done
for file in winbindd.h winbindd_proto.h; do
	install -m 0644 "source3/winbindd/${file}" %{buildroot}/%{_includedir}/samba/winbindd/${file}
done
# cups SMB support
mkdir	-p %{buildroot}/%{cups_lib_dir}/backend/
touch %{buildroot}/%{cups_lib_dir}/backend/smb
mv COPYING README.md WHATSNEW.txt %{buildroot}/%{DOCDIR}/
cp -a docs/* %{buildroot}/%{DOCDIR}
rmdir "%{buildroot}/%{DOCBOOKDIR}"
cp -a examples/ %{buildroot}/%{DOCDIR}
# finally build filelist-samba-doc
for file in $( find %{buildroot}%{DOCDIR} -maxdepth 1); do
	# exclude %{DOCDIR}, README, and docbook
	case "${file#%{buildroot}}" in
		%{DOCDIR}|%{DOCDIR}/README.%{VENDOR}|%{DOCDIR}/docbook) continue ;;
	esac
	echo "%doc ${file#%{buildroot}}" >>"%{_builddir}/samba-%{version}/filelist-samba-doc"
done
for file in $( find %{buildroot}%{_libdir}/samba/vfs/ -mindepth 1 ); do
	# if built we don't want ceph VFS modules in the base package
	case "${file#%{buildroot}}" in
		%{_libdir}/samba/vfs/ceph.so) continue ;;
		%{_libdir}/samba/vfs/ceph_snapshots.so) continue ;;
	esac
	echo "${file#%{buildroot}}" >>%{_builddir}/samba-%{version}/filelist-samba
done
# only package Man pages for VFS modules that we ship
for file in %{buildroot}%{_mandir}/man8/vfs_*; do
	case "${file#%{buildroot}}" in
		%{_mandir}/man8/vfs_ceph.8)
%if 0%{?build_ceph} == 0
			rm ${file}
%endif
			continue
			;;
		%{_mandir}/man8/vfs_ceph_snapshots.8)
%if 0%{?build_ceph} == 0
			rm ${file}
%endif
			continue
			;;
		%{_mandir}/man8/vfs_glusterfs.8)
			rm ${file}
			continue
			;;
		%{_mandir}/man8/vfs_gpfs.8)
			rm ${file}
			continue
			;;
		%{_mandir}/man8/vfs_tsmsm.8)
			rm ${file}
			continue
			;;
	esac
	# wildcard suffix to account for subsequent gzip
	echo "${file#%{buildroot}}*" >>%{_builddir}/samba-%{version}/filelist-samba
done
# copy the schema
install -m 0644 examples/LDAP/samba.schema %{buildroot}/%{_sysconfdir}/openldap/schema/samba3.schema
install -m 0644 examples/LDAP/samba-nds.schema %{buildroot}/%{_datadir}/samba/LDAP/samba-nds.schema
# Clean up installed doc if we have a noarch doc package
%if 0%{?suse_version} < 1120
while read file; do
	rm -r "%{buildroot}/${file#%* }"
done <"%{_builddir}/samba-%{version}/filelist-samba-doc"
for file in %{_datadir}/susehelp; do
	rm -r "%{buildroot}/${file}"
done
pushd "%{buildroot}/%{DOCDIR}"
for file in $( find . -mindepth 1 -maxdepth 1);do
	test "${file}" = "./README.%{VENDOR}" && continue
	rm -r "${file}"
done
popd
%endif
# Hardlink duplicate files
%if 0%{?suse_version} > 1110
%fdupes %{buildroot}
%endif

%pre
getent group ntadmin >/dev/null || groupadd -g 71 -o -r ntadmin
%if 0%{?suse_version} > 1220
%service_add_pre nmb.service smb.service
%endif

%if %{with_dc}
%pre ad-dc
%service_add_pre samba-ad-dc.service
%endif

%preun
%if 0%{?suse_version} > 1220
%service_del_preun nmb.service smb.service
%else
%{?stop_on_removal:%{stop_on_removal smb nmb}}
%endif

%if %{with_dc}
%preun ad-dc
%service_del_preun samba-ad-dc.service
%endif

%post
%if 0%{?suse_version} > 1220

# bsc#1088574; bsc#1071090; bsc#1065551
if [ -f %{_unitdir}/smb.service ] && \
   grep -qE '^ExecStart=.*smbd.*foreground.*no-process-group' %{_unitdir}/smb.service && \
   [ -f %{_sysconfdir}/sysconfig/samba ] && \
   grep -q -- '-D' %{_sysconfdir}/sysconfig/samba
then
    echo using foreground execution for samba systemd units
    echo overwriting samba sysconfig to remove daemon related flags...
    sed -i 's/-D *//g' %{_sysconfdir}/sysconfig/samba
    sed -i 's/-F *//g' %{_sysconfdir}/sysconfig/samba    
fi

%service_add_post nmb.service smb.service
%{_bindir}/systemd-tmpfiles --create %{_tmpfilesdir}/samba.conf
%fillup_only
%endif

%postun
%if 0%{?suse_version} > 1220
%service_del_postun nmb.service smb.service
%else
%{?restart_on_update:%{restart_on_update nmb smb}}
%{?insserv_cleanup:%{insserv_cleanup}}
%endif

%pre client
%if 0%{?suse_version} < 1221
# non SUSE + 11.3 an newer, update, no cifstab, but smbfstab
if [ ! 0%{?suse_version} -lt 1121 -a \
	${1:-0} -gt 1 -a \
	! -e /etc/samba/cifstab -a \
	-f /etc/samba/smbfstab ]; then
	cp -a /etc/samba/smbfstab /var/adm/backup/etc_samba_smbfstab-move
	chkconfig -c smbfs && >/var/adm/backup/etc_samba_smbfs-enabled || :
fi
%endif

%preun client
%{?stop_on_removal:%{stop_on_removal %cifs_init_script}}

%post client
/sbin/ldconfig
%if 0%{?suse_version} < 1221
if [ ${1:-0} -eq 1 ]; then
%if 0%{?suse_version} < 1131
# Only insserv cifs if we're not in update mode.
%{?insserv_force_if_yast:%{insserv_force_if_yast %{cifs_init_script}}}
%endif
	ln -fs %{_sysconfdir}/sysconfig/%{NET_CFGDIR}/scripts/%{cifs_init_script} %{_sysconfdir}/sysconfig/%{NET_CFGDIR}/if-down.d/21-%{cifs_init_script}
	ln -fs %{_sysconfdir}/sysconfig/%{NET_CFGDIR}/scripts/%{cifs_init_script} %{_sysconfdir}/sysconfig/%{NET_CFGDIR}/if-up.d/21-%{cifs_init_script}
else
	for if_case in if-down.d if-up.d; do
		test -h %{_sysconfdir}/sysconfig/%{NET_CFGDIR}/${if_case}/%{cifs_init_script} || \
			continue
		rm -f %{_sysconfdir}/sysconfig/%{NET_CFGDIR}/${if_case}/%{cifs_init_script}
		ln -fs %{_sysconfdir}/sysconfig/%{NET_CFGDIR}/scripts/%{cifs_init_script} %{_sysconfdir}/sysconfig/%{NET_CFGDIR}/${if_case}/21-%{cifs_init_script}
	done
fi
%endif
for fn in MACHINE.SID idmap2.tdb idmap_test.tdb netlogon_creds_cli.tdb passdb.tdb secrets.tdb smbpasswd; do
	test ! -e %{LOCKDIR}/private/$fn && test -e %{CONFIGDIR}/$fn && \
		mv %{CONFIGDIR}/$fn %{LOCKDIR}/private/
done
for fn in brlock.tdb connections.tdb dbwrap_watchers.tdb gencache_notrans.tdb g_lock.tdb leases.tdb locking.tdb mutex.tdb names.tdb printer_list.tdb serverid.tdb smbXsrv_client_global.tdb smbXsrv_open_global.tdb smbXsrv_session_global.tdb smbXsrv_tcon_global.tdb smbXsrv_version_global.tdb srv_fss.tdb; do
	test ! -e %{LOCKDIR}/lock/$fn && test -e %{LOCKDIR}/$fn && \
		mv %{LOCKDIR}/$fn %{LOCKDIR}/lock/
done
%if 0%{?suse_version} < 1221
if [ ${1:-0} -gt 1 -a -f /var/adm/backup/etc_samba_smbfstab-move ]; then
	test -f /etc/samba/cifstab && \
		mv /etc/samba/cifstab /etc/samba/cifstab.rpmnew
	mv /var/adm/backup/etc_samba_smbfstab-move /etc/samba/cifstab
	if [ -f /var/adm/backup/etc_samba_smbfs-enabled ]; then
		chkconfig -a cifs >/dev/null
		rm /var/adm/backup/etc_samba_smbfs-enabled
	fi
fi
%endif
if ! test -e %{_bindir}/get_printing_ticket; then
	ln -fs %{_bindir}/smbspool %{cups_lib_dir}/backend/smb
fi
%{?fillup_only:%{fillup_only -nsd dhcp samba-client network}}

%postun client
/sbin/ldconfig
%if 0%{?suse_version} < 1221
%{?insserv_cleanup:%{insserv_cleanup}}
%endif

%post   -n libdcerpc-binding0 -p /sbin/ldconfig
%postun -n libdcerpc-binding0 -p /sbin/ldconfig
%post   -n libdcerpc-samr0 -p /sbin/ldconfig
%postun -n libdcerpc-samr0 -p /sbin/ldconfig
%post   -n libdcerpc0 -p /sbin/ldconfig
%postun -n libdcerpc0 -p /sbin/ldconfig
%post   -n libndr-krb5pac0 -p /sbin/ldconfig
%postun -n libndr-krb5pac0 -p /sbin/ldconfig
%post   -n libndr-nbt0 -p /sbin/ldconfig
%postun -n libndr-nbt0 -p /sbin/ldconfig
%post   -n libndr-standard0 -p /sbin/ldconfig
%postun -n libndr-standard0 -p /sbin/ldconfig
%post   -n libndr1 -p /sbin/ldconfig
%postun -n libndr1 -p /sbin/ldconfig
%post -n %{libnetapi_name} -p /sbin/ldconfig
%postun -n %{libnetapi_name} -p /sbin/ldconfig
%post   -n libsamba-credentials0 -p /sbin/ldconfig
%postun -n libsamba-credentials0 -p /sbin/ldconfig
%post   -n libsamba-errors0 -p /sbin/ldconfig
%postun -n libsamba-errors0 -p /sbin/ldconfig
%post   -n libsamba-hostconfig0 -p /sbin/ldconfig
%postun -n libsamba-hostconfig0 -p /sbin/ldconfig
%post   -n libsamba-passdb0 -p /sbin/ldconfig
%postun -n libsamba-passdb0 -p /sbin/ldconfig
%post   -n libsamba-policy0-python3 -p /sbin/ldconfig
%postun -n libsamba-policy0-python3 -p /sbin/ldconfig
%post   -n libsamba-util0 -p /sbin/ldconfig
%postun -n libsamba-util0 -p /sbin/ldconfig
%post   -n libsamdb0 -p /sbin/ldconfig
%postun -n libsamdb0 -p /sbin/ldconfig
%post   -n libsmbconf0 -p /sbin/ldconfig
%postun -n libsmbconf0 -p /sbin/ldconfig
%post   -n libsmbldap2 -p /sbin/ldconfig
%postun -n libsmbldap2 -p /sbin/ldconfig
%post   -n libtevent-util0 -p /sbin/ldconfig
%postun -n libtevent-util0 -p /sbin/ldconfig
%post -n %{libwbclient_name} -p /sbin/ldconfig
%postun -n %{libwbclient_name} -p /sbin/ldconfig
%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig
%post test -p /sbin/ldconfig
%postun test -p /sbin/ldconfig

%if %{with_dc}
%post ad-dc
/sbin/ldconfig
%service_add_post samba-ad-dc.service

%postun ad-dc
/sbin/ldconfig
%service_del_postun samba-ad-dc.service
%endif

%post dsdb-modules
ln -sf %{_libdir}/samba/ldb %{_libdir}/ldb/samba
/sbin/ldconfig

%postun dsdb-modules -p /sbin/ldconfig

%pre winbind
# we need this group for squid (ntlmauth)
# read access to /var/lib/samba/winbindd_privileged
getent group winbind >/dev/null || groupadd -r winbind
%if 0%{?suse_version} > 1220
%service_add_pre winbind.service
%endif

%post winbind
/sbin/ldconfig
if test ${1:-0} -eq 1; then
	ln -fs %{_sysconfdir}/sysconfig/%{NET_CFGDIR}/scripts/samba-winbindd %{_sysconfdir}/sysconfig/%{NET_CFGDIR}/if-down.d/55-samba-winbindd
	ln -fs %{_sysconfdir}/sysconfig/%{NET_CFGDIR}/scripts/samba-winbindd %{_sysconfdir}/sysconfig/%{NET_CFGDIR}/if-up.d/55-samba-winbindd
else
	for if_case in if-down.d if-up.d; do
		test -h %{_sysconfdir}/sysconfig/%{NET_CFGDIR}/${if_case}/samba-winbindd || \
			continue
		rm -f %{_sysconfdir}/sysconfig/%{NET_CFGDIR}/${if_case}/samba-winbindd
		ln -fs %{_sysconfdir}/sysconfig/%{NET_CFGDIR}/scripts/samba-winbindd %{_sysconfdir}/sysconfig/%{NET_CFGDIR}/${if_case}/55-samba-winbindd
	done
fi
%if 0%{?suse_version} > 1220
%service_add_post winbind.service
%{_bindir}/systemd-tmpfiles --create %{_tmpfilesdir}/samba.conf
%{fillup_only -ans samba winbind}
%endif

%preun winbind
%if 0%{?suse_version} > 1220
%service_del_preun winbind.service
%else
%{?stop_on_removal:%{stop_on_removal winbind}}
%endif

%postun winbind
/sbin/ldconfig
if [ $1 -eq 0 ]; then
%{_sbindir}/pam-config --delete --winbind
if [ -x %{_sbindir}/nscd ]; then
	%{_sbindir}/nscd -i passwd
	%{_sbindir}/nscd -i group
fi
fi
%if 0%{?suse_version} > 1220
%service_del_postun winbind.service
%else
%{?restart_on_update:%{restart_on_update winbind}}
%{?insserv_cleanup:%{insserv_cleanup}}
%endif

%pre -n ctdb
%if 0%{?suse_version} > 1220
%service_add_pre ctdb.service
%endif
if [ -e %{_sysconfdir}/sysconfig/ctdb ] ; then
    grep CTDB_LOGGING %{_sysconfdir}/sysconfig/ctdb >/dev/null 2>&1 ||
    	sed -i s/CTDB_LOGFILE=/CTDB_LOGGING=file:/g %{_sysconfdir}/sysconfig/ctdb
fi
if [ ! -f %{_sysconfdir}/ctdb/config_migrate.sh ] ; then
    echo "* CTDB Configuration has been redesigned"
    echo ""
    echo "  - Daemon and tool options are now specified in a new ctdb.conf"
    echo "    Samba-style configuration file.  For details, see ctdb.conf(5)."
    echo ""
    echo "  - The event script configuration is no longer specified in the top-level"
    echo "    configuration file.  It can now be specified per event script."
    echo "    For example, the configuration options for the 50.samba event script"
    echo "    can be placed alongside the event script in a file called"
    echo "    50.samba.options.  Script options can also be specified in a new"
    echo "    script.options file.  For details, see ctdb-script.options(5)."
    echo ""
    echo "  - Options that affect CTDB startup should be configured in the"
    echo "    distribution-specific configuration file.  For details, see"
    echo "    ctdb.sysconfig(5)."
    echo ""
    echo "  - Tunable settings are now loaded from ctdb.tunables.  Using"
    echo "    CTDB_SET_TunableVariable=<value> in the main configuration file is"
    echo "    no longer supported.  For details, see ctdb-tunables(7)."
    echo ""
    echo "  An example script to migrate legacy configurations to the new"
    echo "  style is available in %{_sysconfdir}/ctdb/config_migrate.sh."
fi

%preun -n ctdb
%if 0%{?suse_version} > 1220
%service_del_preun ctdb.service
%endif
exit 0

%post -n ctdb
%if 0%{?suse_version} > 1220
%{fillup_only -n ctdb}
%service_add_post ctdb.service
%{_bindir}/systemd-tmpfiles --create %{_tmpfilesdir}/ctdb.conf || :
%else
%{fillup_and_insserv -n ctdb}
%endif

%postun -n ctdb
%if 0%{?suse_version} > 1220
%service_del_postun ctdb.service
%else
%{insserv_cleanup}
%endif
exit 0

%post -n %{libsmbclient_name} -p /sbin/ldconfig
%postun -n %{libsmbclient_name} -p /sbin/ldconfig

%files -f filelist-samba
%defattr(-,root,root)
%if 0%{?suse_version} < 1221
%attr(0754,root,root) %config %{INITDIR}/nmb
%attr(0754,root,root) %config %{INITDIR}/smb
%else
%{_unitdir}/nmb.service
%{_unitdir}/smb.service
%endif
%if 0%{?suse_version} < 1111
%attr(0600,root,root) %config(noreplace) %{CONFIGDIR}/smbpasswd
%else
%ghost %{CONFIGDIR}/smbpasswd
%endif
%config(noreplace) %{CONFIGDIR}/smbusers
%config %{_sysconfdir}/pam.d/samba
%{_sysconfdir}/slp.reg.d
%if 0%{?suse_version} <= 1500
%{_sysconfdir}/sysconfig/SuSEfirewall2.d/services/netbios-server
%{_sysconfdir}/sysconfig/SuSEfirewall2.d/services/samba-server
%endif
%dir %{_libdir}/samba
%dir %{_libdir}/samba/vfs
%dir %{_libdir}/samba/ldb
%{_libdir}/samba/auth
%{_libdir}/samba/config
%{_libdir}/samba/rpc
%attr(0775,root,ntadmin) %{LOCKDIR}/drivers
%dir %{LOCKDIR}/lock/msg.lock
%{LOCKDIR}/netlogon
%attr(0770,root,users) %dir %{LOCKDIR}/profiles
%{_bindir}/smbstatus
%{_sbindir}/nmbd
%{_sbindir}/rcnmb
%{_sbindir}/rcsmb
%{_sbindir}/smbd
%if 0%{?suse_version} < 1100
%dir %{_datadir}/omc
%dir %{_datadir}/omc/svcinfo.d
%endif
%attr(0644,root,root) %{_datadir}/omc/svcinfo.d/nmb.xml
%attr(0644,root,root) %{_datadir}/omc/svcinfo.d/smb.xml
%dir %{_datadir}/samba
%{_datadir}/samba/update-apparmor-samba-profile
%{_mandir}/man1/smbstatus.1.*
%{_mandir}/man5/smbpasswd.5.*
%{_mandir}/man8/nmbd.8.*
%{_mandir}/man8/smbd.8.*
%if 0%{?suse_version} > 1220
%{_fillupdir}/sysconfig.samba
%endif

%files client
%defattr(-,root,root)
%if 0%{?suse_version} < 1221
%attr(0754,root,root) %config %{INITDIR}/%{cifs_init_script}
%attr(0600,root,root) %config(noreplace) %{CONFIGDIR}/%{cifs_init_script}tab
%ghost %{_sysconfdir}/sysconfig/%{NET_CFGDIR}/if-down.d/21-%{cifs_init_script}
%ghost %{_sysconfdir}/sysconfig/%{NET_CFGDIR}/if-up.d/21-%{cifs_init_script}
%{_sysconfdir}/sysconfig/%{NET_CFGDIR}/scripts/%{cifs_init_script}
%{_sbindir}/rc%{cifs_init_script}
%if 0%{?suse_version} < 1100
%dir %{_datadir}/omc
%dir %{_datadir}/omc/svcinfo.d
%endif
%attr(0644,root,root) %{_datadir}/omc/svcinfo.d/%{cifs_init_script}.xml
%ghost %{_localstatedir}/run/%{cifs_init_script}
%endif
%dir %{CONFIGDIR}
%config(noreplace) %{CONFIGDIR}/lmhosts
%config(noreplace) %{CONFIGDIR}/smb.conf
%dir %{_sysconfdir}/openldap
%dir %{_sysconfdir}/openldap/schema
%attr(0444,root,root) %config %{_sysconfdir}/openldap/schema/samba3.schema
%if 0%{?suse_version} <= 1500 && 0%{?suse_version} > 1100
%{_sysconfdir}/sysconfig/SuSEfirewall2.d/services/samba-client
%endif
%{_bindir}/cifsdd
%{_bindir}/dbwrap_tool
%{_sbindir}/eventlogadm
%{_bindir}/findsmb
%{_bindir}/net
%{_bindir}/nmblookup
%{_bindir}/oLschema2ldif
%{_bindir}/regdiff
%{_bindir}/samba-regedit
%{_bindir}/regpatch
%{_bindir}/regshell
%{_bindir}/regtree
%{_bindir}/nmbstatus
%{_bindir}/pdbedit
%{_bindir}/profiles
%{_bindir}/rpcclient
%{_bindir}/sharesec
%{_bindir}/smbcacls
%{_bindir}/smbclient
%{_bindir}/smbcontrol
%{_bindir}/smbcquotas
%{_bindir}/smbget
%{_bindir}/smbpasswd
%{_bindir}/smbprngenpdf
%{_bindir}/smbspool
%{_bindir}/smbtar
%{_bindir}/smbtree
%{_bindir}/testparm
%{_bindir}/mvxattr
%dir %{cups_lib_dir}
%dir %{cups_lib_dir}/backend
%ghost %{cups_lib_dir}/backend/smb
%{_libdir}/libnss_wins.so.*
%dir %{_libdir}/samba
%{_libdir}/samba/charset
%{_libdir}/samba/smbspool_krb5_wrapper
%{_mandir}/man1/dbwrap_tool.1.*
%{_mandir}/man1/findsmb.1.*
%{_mandir}/man1/log2pcap.1.*
%{_mandir}/man1/nmblookup.1.*
%{_mandir}/man1/nmbstatus.1.*
%{_mandir}/man1/oLschema2ldif.1.*
%{_mandir}/man1/profiles.1.*
%{_mandir}/man1/regdiff.1.*
%{_mandir}/man1/regpatch.1.*
%{_mandir}/man1/regshell.1.*
%{_mandir}/man1/regtree.1.*
%{_mandir}/man1/rpcclient.1.*
%{_mandir}/man1/sharesec.1.*
%{_mandir}/man1/smbcacls.1.*
%{_mandir}/man1/smbcontrol.1.*
%{_mandir}/man1/smbclient.1.*
%{_mandir}/man1/smbcquotas.1.*
%{_mandir}/man1/smbget.1.*
%{_mandir}/man1/smbtar.1.*
%{_mandir}/man1/smbtree.1.*
%{_mandir}/man1/testparm.1.*
%{_mandir}/man1/mvxattr.1.*
%{_mandir}/man5/lmhosts.5.*
%{_mandir}/man5/smb.conf.5.*
%{_mandir}/man5/smbgetrc.5.*
%{_mandir}/man7/samba.7.*
%{_mandir}/man8/cifsdd.8.*
%{_mandir}/man8/eventlogadm.8.*
%{_mandir}/man8/net.8.*
%{_mandir}/man8/pdbedit.8.*
%{_mandir}/man8/samba-regedit.8.*
%{_mandir}/man8/smbpasswd.8.*
%{_mandir}/man8/smbspool.8.*
%{_mandir}/man8/smbspool_krb5_wrapper.8.*
%dir %{_datadir}/samba
%dir %{_datadir}/samba/LDAP
%config %{_datadir}/samba/LDAP/samba-nds.schema
%{_datadir}/samba/templates
%dir %{DOCDIR}
%doc %{DOCDIR}/README.%{VENDOR}
%{_fillupdir}/samba-client-dhcp.conf
%{_fillupdir}/sysconfig.dhcp-samba-client
%dir %{LOCKDIR}
%dir %{LOCKDIR}/lock
%dir %{LOCKDIR}/private
%attr(0700,root,root) %dir %{LOCKDIR}/private/msg.sock
%attr(0750,root,root) %dir %{LOGDIR}
%ghost %dir %{PIDDIR}
%if 0%{?suse_version} > 1220
%dir %{_tmpfilesdir}
%{_tmpfilesdir}/samba.conf
%endif
%if %{with_mscat}
%{_bindir}/dumpmscat
%endif

%files core-devel
%defattr(-,root,root)
%{_includedir}/samba
%dir %_includedir/samba-4.0/
%_includedir/samba-4.0/charset.h
%_includedir/samba-4.0/dcesrv_core.h
%if %{with_dc}
%_includedir/samba-4.0/dcerpc_server.h
%endif
%dir %_includedir/samba-4.0/core/
%_includedir/samba-4.0/core/doserr.h
%_includedir/samba-4.0/core/error.h
%_includedir/samba-4.0/core/ntstatus.h
%_includedir/samba-4.0/core/ntstatus_gen.h
%_includedir/samba-4.0/core/hresult.h
%_includedir/samba-4.0/core/werror.h
%_includedir/samba-4.0/core/werror_gen.h
%_includedir/samba-4.0/domain_credentials.h
%dir %_includedir/samba-4.0/gen_ndr/
%_includedir/samba-4.0/gen_ndr/auth.h
%_includedir/samba-4.0/gen_ndr/dcerpc.h
%_includedir/samba-4.0/gen_ndr/drsblobs.h
%_includedir/samba-4.0/gen_ndr/drsuapi.h
%_includedir/samba-4.0/gen_ndr/ndr_dcerpc.h
%_includedir/samba-4.0/gen_ndr/ndr_drsblobs.h
%_includedir/samba-4.0/gen_ndr/ndr_drsuapi.h
%_includedir/samba-4.0/gen_ndr/ndr_svcctl_c.h
%_includedir/samba-4.0/gen_ndr/security.h
%_includedir/samba-4.0/gen_ndr/server_id.h
%_includedir/samba-4.0/ldb_wrap.h
%dir %_includedir/samba-4.0/ndr/
%_includedir/samba-4.0/ndr/ndr_dcerpc.h
%_includedir/samba-4.0/ndr/ndr_drsblobs.h
%_includedir/samba-4.0/ndr/ndr_drsuapi.h
%_includedir/samba-4.0/ndr/ndr_svcctl.h
%_includedir/samba-4.0/rpc_common.h
%dir %_includedir/samba-4.0/samba/
%_includedir/samba-4.0/samba/session.h
%_includedir/samba-4.0/samba/version.h
%_includedir/samba-4.0/share.h
%_includedir/samba-4.0/smb2_lease_struct.h
%_includedir/samba-4.0/tdr.h
%_includedir/samba-4.0/tsocket.h
%_includedir/samba-4.0/tsocket_internal.h
%dir %_includedir/samba-4.0/util/
%_includedir/samba-4.0/util/genrand.h
%_includedir/samba-4.0/util/idtree.h
%_includedir/samba-4.0/util/idtree_random.h
%_includedir/samba-4.0/util/tfork.h
%_includedir/samba-4.0/util_ldb.h
%{_libdir}/libnss_winbind.so
%{_libdir}/libnss_wins.so

%files libs
%defattr(-,root,root)
%dir %{_libdir}/samba
%{_libdir}/samba/libCHARSET3-samba4.so
%{_libdir}/samba/libLIBWBCLIENT-OLD-samba4.so
%{_libdir}/samba/libMESSAGING-samba4.so
%{_libdir}/samba/libMESSAGING-SEND-samba4.so
%{_libdir}/samba/libaddns-samba4.so
%{_libdir}/samba/libads-samba4.so
%{_libdir}/samba/libasn1util-samba4.so
%{_libdir}/samba/libauth-samba4.so
%{_libdir}/samba/libauth4-samba4.so
%{_libdir}/samba/libauth-unix-token-samba4.so
%{_libdir}/samba/libauthkrb5-samba4.so
%{_libdir}/samba/libcli-ldap-common-samba4.so
%{_libdir}/samba/libcli-ldap-samba4.so
%{_libdir}/samba/libcli-nbt-samba4.so
%{_libdir}/samba/libcli-cldap-samba4.so
%{_libdir}/samba/libcli-smb-common-samba4.so
%{_libdir}/samba/libcli-spoolss-samba4.so
%{_libdir}/samba/libcliauth-samba4.so
%{_libdir}/samba/libcluster-samba4.so
%{_libdir}/samba/libcmdline-contexts-samba4.so
%{_libdir}/samba/libcmdline-credentials-samba4.so
%{_libdir}/samba/libdbwrap-samba4.so
%{_libdir}/samba/libdcerpc-samba-samba4.so
%{_libdir}/samba/libdcerpc-samba4.so
%{_libdir}/libdcerpc-server-core.so.0
%{_libdir}/libdcerpc-server-core.so.0.0.1
%if %{with_dc}
%{_libdir}/samba/libdb-glue-samba4.so
%{_libdir}/samba/libdfs-server-ad-samba4.so
%{_libdir}/samba/libdnsserver-common-samba4.so
%endif
%{_libdir}/samba/libdsdb-module-samba4.so
%if %{with_dc}
%{_libdir}/samba/libdsdb-garbage-collect-tombstones-samba4.so
%endif
%{_libdir}/samba/libevents-samba4.so
%{_libdir}/samba/libflag-mapping-samba4.so
%{_libdir}/samba/libgenrand-samba4.so
%{_libdir}/samba/libgensec-samba4.so
%{_libdir}/samba/libgpext-samba4.so
%{_libdir}/samba/libgpo-samba4.so
%{_libdir}/samba/libgse-samba4.so
%{_libdir}/samba/libhttp-samba4.so
%{_libdir}/samba/libidmap-samba4.so
%{_libdir}/samba/libinterfaces-samba4.so
%{_libdir}/samba/libiov-buf-samba4.so
%{_libdir}/samba/libkrb5samba-samba4.so
%{_libdir}/samba/libldbsamba-samba4.so
%{_libdir}/samba/liblibcli-lsa3-samba4.so
%{_libdir}/samba/liblibcli-netlogon3-samba4.so
%{_libdir}/samba/liblibsmb-samba4.so
%{_libdir}/samba/libmessages-dgm-samba4.so
%{_libdir}/samba/libmessages-util-samba4.so
%{_libdir}/samba/libmsghdr-samba4.so
%{_libdir}/samba/libmsrpc3-samba4.so
%{_libdir}/samba/libndr-samba-samba4.so
%{_libdir}/samba/libndr-samba4.so
%{_libdir}/samba/libnet-keytab-samba4.so
%{_libdir}/samba/libnetif-samba4.so
%{_libdir}/samba/libnpa-tstream-samba4.so
%{_libdir}/samba/libnss-info-samba4.so
%{_libdir}/samba/libpopt-samba3-cmdline-samba4.so
%{_libdir}/samba/libpopt-samba3-samba4.so
%{_libdir}/samba/libposix-eadb-samba4.so
%{_libdir}/samba/libprinter-driver-samba4.so
%{_libdir}/samba/libprinting-migrate-samba4.so
%{_libdir}/samba/libregistry-samba4.so
%{_libdir}/samba/libreplace-samba4.so
%{_libdir}/samba/libsamba-cluster-support-samba4.so
%{_libdir}/samba/libsamba-debug-samba4.so
%{_libdir}/samba/libsamba-modules-samba4.so
%{_libdir}/samba/libsamba-security-samba4.so
%{_libdir}/samba/libsamba-sockets-samba4.so
%{_libdir}/samba/libsamba3-util-samba4.so
%{_libdir}/samba/libsamdb-common-samba4.so
%{_libdir}/samba/libsecrets3-samba4.so
%{_libdir}/samba/libserver-id-db-samba4.so
%{_libdir}/samba/libserver-role-samba4.so
%{_libdir}/samba/libshares-samba4.so
%{_libdir}/samba/libsmb-transport-samba4.so
%{_libdir}/samba/libsmbclient-raw-samba4.so
%{_libdir}/samba/libsmbd-base-samba4.so
%{_libdir}/samba/libsmbd-conn-samba4.so
%{_libdir}/samba/libsmbd-shim-samba4.so
%{_libdir}/samba/libsmbldaphelper-samba4.so
%{_libdir}/samba/libsmbpasswdparser-samba4.so
%{_libdir}/samba/libsocket-blocking-samba4.so
%{_libdir}/samba/libsys-rw-samba4.so
%{_libdir}/samba/libtalloc-report-samba4.so
%{_libdir}/samba/libtalloc-report-printf-samba4.so
%{_libdir}/samba/libtdb-wrap-samba4.so
%{_libdir}/samba/libtime-basic-samba4.so
%{_libdir}/samba/libtorture-samba4.so
%{_libdir}/samba/libtrusts-util-samba4.so
%{_libdir}/samba/libutil-cmdline-samba4.so
%{_libdir}/samba/libutil-reg-samba4.so
%{_libdir}/samba/libutil-setid-samba4.so
%{_libdir}/samba/libutil-tdb-samba4.so
%{_libdir}/samba/libwinbind-client-samba4.so
%{_libdir}/samba/libxattr-tdb-samba4.so
%{_libdir}/samba/libcmocka-samba4.so
%{_libdir}/samba/libcommon-auth-samba4.so
%if %{with_dc}
%{_libdir}/samba/libscavenge-dns-records-samba4.so
%endif
%dir %{_libdir}/samba/pdb
%{_libdir}/samba/pdb/ldapsam.so
%{_libdir}/samba/pdb/smbpasswd.so
%{_libdir}/samba/pdb/tdbsam.so
%{_libdir}/samba/libclidns-samba4.so
%if %{with_mscat}
%{_libdir}/samba/libmscat-samba4.so
%endif

%files libs-python3
%{_libdir}/samba/libsamba-net.%{py3_soflags_dash}-samba4.so
%{_libdir}/samba/libsamba-python.%{py3_soflags_dash}-samba4.so

%files python3
%defattr(-,root,root)
%{python3_sitearch}/*

%files test
%defattr(-,root,root)
%{_bindir}/gentest
%{_bindir}/locktest
%{_bindir}/masktest
%{_bindir}/ndrdump
%{_bindir}/smbtorture
%{_mandir}/man1/smbtorture.1.*
%{_mandir}/man7/traffic_learner.7.*
%{_mandir}/man7/traffic_replay.7.*
%{_bindir}/vfstest
%{_bindir}/mdfind
%{_mandir}/man1/gentest.1.*
%{_mandir}/man1/locktest.1.*
%{_mandir}/man1/masktest.1.*
%{_mandir}/man1/ndrdump.1.*
%{_mandir}/man1/vfstest.1.*
%{_mandir}/man1/mdfind.1.*

%files winbind -f filelist-samba-winbind
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/security/pam_winbind.conf
%if 0%{?suse_version} < 1221
%attr(0754,root,root) %config %{INITDIR}/winbind
%else
%{_unitdir}/winbind.service
%endif
%ghost %{_sysconfdir}/sysconfig/%{NET_CFGDIR}/if-down.d/55-samba-winbindd
%ghost %{_sysconfdir}/sysconfig/%{NET_CFGDIR}/if-up.d/55-samba-winbindd
%{_sysconfdir}/sysconfig/%{NET_CFGDIR}/scripts/samba-winbindd
%{_bindir}/ntlm_auth
%{_bindir}/wbinfo
%{_sbindir}/rcwinbind
%{_sbindir}/winbindd
%{_sbindir}/samba-gpupdate
/%{_lib}/security/pam_winbind.so
%{_libdir}/libnss_winbind.so.*
%{_libdir}/samba/idmap
%{_libdir}/samba/nss_info
%dir %{_libdir}/samba/krb5
%{_libdir}/samba/krb5/winbind_krb5_locator.so
%{_libdir}/samba/krb5/winbind_krb5_localauth.so
%{_mandir}/man1/ntlm_auth.1.*
%{_mandir}/man1/wbinfo.1.*
%{_mandir}/man8/winbind_krb5_localauth.8.*
%{_mandir}/man8/winbind_krb5_locator.8.*
%{_mandir}/man5/pam_winbind.conf.5.*
%{_mandir}/man8/samba-gpupdate.8.gz
%{_mandir}/man8/idmap_ad.8.*
%{_mandir}/man8/idmap_autorid.8.*
%{_mandir}/man8/idmap_hash.8.*
%{_mandir}/man8/idmap_ldap.8.*
%{_mandir}/man8/idmap_nss.8.*
%{_mandir}/man8/idmap_rfc2307.8.*
%{_mandir}/man8/idmap_rid.8.*
%{_mandir}/man8/idmap_script.8.*
%{_mandir}/man8/idmap_tdb.8.*
%{_mandir}/man8/idmap_tdb2.8.*
%{_mandir}/man8/pam_winbind.8.*
%{_mandir}/man8/winbindd.8.*
%if 0%{?suse_version} < 1100
%dir %{_datadir}/omc
%dir %{_datadir}/omc/svcinfo.d
%endif
%attr(0644,root,root) %{_datadir}/omc/svcinfo.d/winbind.xml
%attr(0750,root,winbind) %dir %{LOCKDIR}/winbindd_privileged
%if 0%{?suse_version} > 1220
%{_fillupdir}/sysconfig.samba-winbind
%endif
%attr(0770,root,root) %{_var}/cache/krb5rcache
%if 0%{?suse_version} > 1110

%files doc -f filelist-samba-doc
%defattr(-,root,root)
%dir %{DOCDIR}
%doc %{_datadir}/susehelp
%endif

%files -n ctdb
%defattr(-,root,root)
%dir %{_sysconfdir}/ctdb
%{_fillupdir}/sysconfig.ctdb
%{_sysconfdir}/ctdb/notify.sh
%{_sysconfdir}/ctdb/ctdb-crash-cleanup.sh
%{_sysconfdir}/ctdb/debug-hung-script.sh
%{_sysconfdir}/ctdb/debug_locks.sh
%{_sysconfdir}/ctdb/functions
%{_sysconfdir}/ctdb/nfs-linux-kernel-callout
%ghost %{_sysconfdir}/ctdb/nodes
%{_sysconfdir}/ctdb/statd-callout
%if 0%{?suse_version} > 1220
%attr(644,root,root) %{_unitdir}/ctdb.service
%dir %{_tmpfilesdir}
%{_tmpfilesdir}/ctdb.conf
%ghost %dir /run/ctdbd
%else
%attr(755,root,root) %{INITDIR}/ctdb
%endif
%dir %{_datadir}/ctdb/events
%dir %{_datadir}/ctdb/events/legacy
%{_datadir}/ctdb/events/legacy/*
%dir %{_sysconfdir}/ctdb/events
%dir %{_sysconfdir}/ctdb/events/notification
%{_sysconfdir}/ctdb/events/notification/README
%dir %{_sysconfdir}/ctdb/nfs-checks.d
%config %{_sysconfdir}/ctdb/nfs-checks.d/00.portmapper.check
%config %{_sysconfdir}/ctdb/nfs-checks.d/10.status.check
%config %{_sysconfdir}/ctdb/nfs-checks.d/20.nfs.check
%config %{_sysconfdir}/ctdb/nfs-checks.d/30.nlockmgr.check
%config %{_sysconfdir}/ctdb/nfs-checks.d/40.mountd.check
%config %{_sysconfdir}/ctdb/nfs-checks.d/50.rquotad.check
%{_sysconfdir}/ctdb/nfs-checks.d/README
%{_sbindir}/ctdbd
%{_sbindir}/ctdbd_wrapper
%{_sbindir}/rcctdb
%{_bindir}/ctdb
%{_bindir}/ctdb_diagnostics
%{_bindir}/ctdb_run_cluster_tests
%{_bindir}/ctdb_run_tests
%{_bindir}/ltdbtool
%{_bindir}/onnode
%{_bindir}/ping_pong
%dir %{_libdir}/ctdb
%{_libdir}/ctdb/ctdb-config
%{_libdir}/samba/libctdb-event-client-samba4.so
%{_libdir}/ctdb/ctdb-event
%{_libdir}/ctdb/ctdb-eventd
%{_libdir}/ctdb/ctdb-path
%{_libdir}/ctdb/ctdb_lock_helper
%{_libdir}/ctdb/ctdb_natgw
%{_libdir}/ctdb/ctdb_recovery_helper
%{_libdir}/ctdb/ctdb_takeover_helper
%{_libdir}/ctdb/smnotify
%{_libdir}/ctdb/ctdb_killtcp
%{_libdir}/ctdb/ctdb_lvs
%{_libdir}/ctdb/ctdb_mutex_fcntl_helper
%dir %{_localstatedir}/lib/ctdb
%dir %{_localstatedir}/lib/ctdb/persistent
%dir %{_localstatedir}/log/ctdb
%if 0%{?suse_version} > 1220
%ghost %dir /run/ctdb
%else
%ghost %dir %{_localstatedir}/run/ctdb
%endif
%{_mandir}/man1/ctdb.1.gz
%{_mandir}/man1/ctdbd.1.gz
%{_mandir}/man1/ctdbd_wrapper.1.gz
%{_mandir}/man1/ctdb_diagnostics.1.gz
%{_mandir}/man1/ltdbtool.1.gz
%{_mandir}/man1/onnode.1.gz
%{_mandir}/man1/ping_pong.1.gz
%{_mandir}/man5/ctdb.conf.5.*
%{_mandir}/man5/ctdb-script.options.5.*
%{_mandir}/man5/ctdb.sysconfig.5.*
%{_mandir}/man7/ctdb-statistics.7.*
%{_mandir}/man7/ctdb-tunables.7.*
%{_mandir}/man7/ctdb.7.*
%doc %{_defaultdocdir}/ctdb
%{_sysconfdir}/ctdb/config_migrate.sh
%{_bindir}/ctdb_local_daemons

%if 0%{?build_ctdb_pmda}
%files -n ctdb-pcp-pmda
%defattr(-,root,root)
%dir %{_localstatedir}/lib/pcp
%dir %{_localstatedir}/lib/pcp/pmdas
%dir %{_localstatedir}/lib/pcp/pmdas/ctdb
%{_localstatedir}/lib/pcp/pmdas/ctdb/Install
%{_localstatedir}/lib/pcp/pmdas/ctdb/README
%{_localstatedir}/lib/pcp/pmdas/ctdb/Remove
%{_localstatedir}/lib/pcp/pmdas/ctdb/domain.h
%{_localstatedir}/lib/pcp/pmdas/ctdb/help
%{_localstatedir}/lib/pcp/pmdas/ctdb/pmdactdb
%{_localstatedir}/lib/pcp/pmdas/ctdb/pmns
%endif

%files -n ctdb-tests
%defattr(-,root,root)
%dir %{_libdir}/ctdb
%{_libdir}/ctdb/tests/
%dir %{_datadir}/ctdb
%{_datadir}/ctdb/tests

%files -n libdcerpc-binding0
%defattr(-,root,root)
%_libdir/libdcerpc-binding.so.0*

%files -n libdcerpc-samr0
%defattr(-,root,root)
%_libdir/libdcerpc-samr.so.0*

%files -n libdcerpc-samr-devel
%defattr(-,root,root)
%dir %_includedir/samba-4.0/
%dir %_includedir/samba-4.0/gen_ndr/
%_includedir/samba-4.0/gen_ndr/ndr_samr_c.h
%_libdir/libdcerpc-samr.so
%_libdir/pkgconfig/dcerpc_samr.pc

%files -n libdcerpc0
%defattr(-,root,root)
%_libdir/libdcerpc.so.0*

%files -n libdcerpc-devel
%defattr(-,root,root)
%dir %_includedir/samba-4.0/
%_includedir/samba-4.0/dcerpc.h
%dir %_includedir/samba-4.0/gen_ndr/
%_libdir/libdcerpc.so
%_libdir/libdcerpc-binding.so
%_libdir/pkgconfig/dcerpc.pc
%_libdir/libdcerpc-server-core.so
%if %{with_dc}
%_libdir/libdcerpc-server.so
%_libdir/pkgconfig/dcerpc_server.pc
%endif
%files -n libndr-krb5pac0
%defattr(-,root,root)
%_libdir/libndr-krb5pac.so.0*

%files -n libndr-krb5pac-devel
%defattr(-,root,root)
%dir %_includedir/samba-4.0/
%dir %_includedir/samba-4.0/gen_ndr/
%_includedir/samba-4.0/gen_ndr/krb5pac.h
%_includedir/samba-4.0/gen_ndr/ndr_krb5pac.h
%_includedir/samba-4.0/ndr/ndr_krb5pac.h
%_libdir/libndr-krb5pac.so
%_libdir/pkgconfig/ndr_krb5pac.pc

%files -n libndr-nbt0
%defattr(-,root,root)
%_libdir/libndr-nbt.so.0*

%files -n libndr-nbt-devel
%defattr(-,root,root)
%dir %_includedir/samba-4.0/
%dir %_includedir/samba-4.0/gen_ndr/
%_includedir/samba-4.0/gen_ndr/nbt.h
%_includedir/samba-4.0/gen_ndr/ndr_nbt.h
%dir %_includedir/samba-4.0/ndr/
%_includedir/samba-4.0/ndr/ndr_nbt.h
%_libdir/libndr-nbt.so
%_libdir/pkgconfig/ndr_nbt.pc

%files -n libndr-standard0
%defattr(-,root,root)
%_libdir/libndr-standard.so.0*

%files -n libndr-standard-devel
%defattr(-,root,root)
%dir %_includedir/samba-4.0/
%dir %_includedir/samba-4.0/gen_ndr/
%_includedir/samba-4.0/gen_ndr/samr.h
%_includedir/samba-4.0/gen_ndr/ndr_samr.h
%_includedir/samba-4.0/gen_ndr/lsa.h
%_includedir/samba-4.0/gen_ndr/netlogon.h
%_includedir/samba-4.0/gen_ndr/atsvc.h
%_includedir/samba-4.0/gen_ndr/ndr_atsvc.h
%_includedir/samba-4.0/gen_ndr/ndr_svcctl.h
%_includedir/samba-4.0/gen_ndr/svcctl.h
%_libdir/libndr-standard.so
%_libdir/pkgconfig/ndr_standard.pc

%files -n libndr1
%defattr(-,root,root)
%_libdir/libndr.so.1*

%files -n libndr-devel
%defattr(-,root,root)
%dir %_includedir/samba-4.0/
%dir %_includedir/samba-4.0/gen_ndr/
%_includedir/samba-4.0/gen_ndr/misc.h
%_includedir/samba-4.0/gen_ndr/ndr_misc.h
%_includedir/samba-4.0/ndr.h
%_libdir/libndr.so
%_libdir/pkgconfig/ndr.pc

%files -n %{libnetapi_name}
%defattr(-,root,root)
%{_libdir}/libnetapi.so.*

%files -n libnetapi-devel
%defattr(-,root,root)
%dir %_includedir/samba-4.0/
%{_includedir}/samba-4.0/netapi.h
%{_libdir}/libnetapi.so
%{_libdir}/pkgconfig/netapi.pc

%files -n libsamba-credentials0
%defattr(-,root,root)
%_libdir/libsamba-credentials.so.0*

%files -n libsamba-credentials-devel
%defattr(-,root,root)
%dir %_includedir/samba-4.0/
%_includedir/samba-4.0/credentials.h
%_libdir/libsamba-credentials.so
%_libdir/pkgconfig/samba-credentials.pc

%files -n libsamba-errors0
%defattr(-,root,root)
%_libdir/libsamba-errors.so.*

%files -n libsamba-errors-devel
%defattr(-,root,root)
%_libdir/libsamba-errors.so

%files -n libsamba-hostconfig0
%defattr(-,root,root)
%_libdir/libsamba-hostconfig.so.0*

%files -n libsamba-hostconfig-devel
%defattr(-,root,root)
%dir %_includedir/samba-4.0/
%_includedir/samba-4.0/param.h
%_libdir/libsamba-hostconfig.so
%_libdir/pkgconfig/samba-hostconfig.pc

%files -n libsamba-passdb0
%defattr(-,root,root)
%_libdir/libsamba-passdb.so.0*

%files -n libsamba-passdb-devel
%defattr(-,root,root)
%dir %_includedir/samba-4.0/
%_includedir/samba-4.0/lookup_sid.h
%_includedir/samba-4.0/machine_sid.h
%_includedir/samba-4.0/passdb.h
%_libdir/libsamba-passdb.so

%files -n libsamba-policy0-python3
%defattr(-,root,root)
%_libdir/libsamba-policy.%{py3_soflags_dash}.so.0*

%files -n libsamba-policy-devel
%defattr(-,root,root)
%dir %_includedir/samba-4.0/
%_includedir/samba-4.0/policy.h

%files -n libsamba-policy-python3-devel
%defattr(-,root,root)
%_libdir/libsamba-policy.%{py3_soflags_dash}.so
%_libdir/pkgconfig/samba-policy.%{py3_soflags}.pc

%files -n libsamba-util0
%defattr(-,root,root)
%_libdir/libsamba-util.so.0*

%files -n libsamba-util-devel
%defattr(-,root,root)
%dir %_includedir/samba-4.0/
%dir %_includedir/samba-4.0/util/
%_includedir/samba-4.0/util/attr.h
%_includedir/samba-4.0/util/blocking.h
%_includedir/samba-4.0/util/data_blob.h
%_includedir/samba-4.0/util/debug.h
%_includedir/samba-4.0/util/discard.h
%_includedir/samba-4.0/util/fault.h
%_includedir/samba-4.0/util/signal.h
%_includedir/samba-4.0/util/string_wrappers.h
%_includedir/samba-4.0/util/substitute.h
%_includedir/samba-4.0/util/time.h
%_libdir/libsamba-util.so
%_libdir/pkgconfig/samba-util.pc

%files -n libsamdb0
%defattr(-,root,root)
%_libdir/libsamdb.so.0*

%files -n libsamdb-devel
%defattr(-,root,root)
%_libdir/libsamdb.so
%_libdir/pkgconfig/samdb.pc

%files -n %{libsmbclient_name}
%defattr(-,root,root)
%{_libdir}/libsmbclient.so.*

%files -n libsmbclient-devel
%defattr(-,root,root)
%dir %_includedir/samba-4.0/
%{_includedir}/samba-4.0/libsmbclient.h
%{_libdir}/libsmbclient.so
%{_libdir}/pkgconfig/smbclient.pc
%{_mandir}/man7/libsmbclient.7.*

%files -n libsmbconf0
%defattr(-,root,root)
%_libdir/libsmbconf.so.0*

%files -n libsmbconf-devel
%defattr(-,root,root)
%dir %_includedir/samba-4.0/
%_includedir/samba-4.0/smbconf.h
%_libdir/libsmbconf.so

%files -n libsmbldap2
%defattr(-,root,root)
%_libdir/libsmbldap.so.2*

%files -n libsmbldap-devel
%defattr(-,root,root)
%dir %_includedir/samba-4.0/
%_includedir/samba-4.0/smbldap.h
%_includedir/samba-4.0/smb_ldap.h
%_libdir/libsmbldap.so

%files -n libtevent-util0
%defattr(-,root,root)
%_libdir/libtevent-util.so.0*

%files -n libtevent-util-devel
%defattr(-,root,root)
%dir %_includedir/samba-4.0/
%dir %_includedir/samba-4.0/util/
%_includedir/samba-4.0/util/tevent_ntstatus.h
%_includedir/samba-4.0/util/tevent_unix.h
%_includedir/samba-4.0/util/tevent_werror.h
%_libdir/libtevent-util.so

%files -n %{libwbclient_name}
%defattr(-,root,root)
%{_libdir}/libwbclient.so.*

%files -n libwbclient-devel
%defattr(-,root,root)
%dir %_includedir/samba-4.0/
%{_includedir}/samba-4.0/wbclient.h
%{_libdir}/libwbclient.so
%{_libdir}/pkgconfig/wbclient.pc

%if 0%{?build_ceph}
%files ceph
%defattr(-,root,root)
%{_mandir}/man8/vfs_ceph.8.*
%{_libdir}/samba/vfs/ceph.so
%{_mandir}/man8/vfs_ceph_snapshots.8.*
%{_libdir}/samba/vfs/ceph_snapshots.so
%{_mandir}/man7/ctdb_mutex_ceph_rados_helper.7.*
%{_libdir}/ctdb/ctdb_mutex_ceph_rados_helper
%endif

%if %{with_dc}
%files ad-dc
%{_unitdir}/samba-ad-dc.service
%{_bindir}/samba-tool
%{_sbindir}/samba
%{_sbindir}/samba_dnsupdate
%{_sbindir}/samba_kcc
%{_sbindir}/samba_spnupdate
%{_sbindir}/samba_upgradedns
%{_sbindir}/samba_downgrade_db
%{_sbindir}/rcsamba-ad-dc
%{_libdir}/krb5/plugins/kdb/samba.so
%{_libdir}/libdcerpc-server.so.0
%{_libdir}/libdcerpc-server.so.0.0.1
%{_libdir}/samba/bind9
%{_libdir}/samba/bind9/dlz_bind9.so
%{_libdir}/samba/bind9/dlz_bind9_10.so
%{_libdir}/samba/bind9/dlz_bind9_11.so
%{_libdir}/samba/bind9/dlz_bind9_9.so
%{_libdir}/samba/gensec
%{_libdir}/samba/gensec/krb5.so
%{_libdir}/samba/libdlz-bind9-for-torture-samba4.so
%{_libdir}/samba/libpac-samba4.so
%{_libdir}/samba/libprocess-model-samba4.so
%{_libdir}/samba/libservice-samba4.so
%{_libdir}/samba/process_model
%{_libdir}/samba/process_model/standard.so
%{_libdir}/samba/service
%{_libdir}/samba/service/cldap.so
%{_libdir}/samba/service/dcerpc.so
%{_libdir}/samba/service/dns.so
%{_libdir}/samba/service/dns_update.so
%{_libdir}/samba/service/drepl.so
%{_libdir}/samba/service/kcc.so
%{_libdir}/samba/service/kdc.so
%{_libdir}/samba/service/ldap.so
%{_libdir}/samba/service/nbtd.so
%{_libdir}/samba/service/ntp_signd.so
%{_libdir}/samba/service/s3fs.so
%{_libdir}/samba/service/winbindd.so
%{_libdir}/samba/service/wrepl.so
%{_datadir}/samba/setup
%{_datadir}/samba/setup/ad-schema
%{_datadir}/samba/setup/ad-schema/MS-AD_Schema_2K8_Attributes.txt
%{_datadir}/samba/setup/ad-schema/MS-AD_Schema_2K8_Classes.txt
%{_datadir}/samba/setup/ad-schema/MS-AD_Schema_2K8_R2_Attributes.txt
%{_datadir}/samba/setup/ad-schema/MS-AD_Schema_2K8_R2_Classes.txt
%{_datadir}/samba/setup/ad-schema/licence.txt
%{_datadir}/samba/setup/aggregate_schema.ldif
%{_datadir}/samba/setup/display-specifiers
%{_datadir}/samba/setup/display-specifiers/DisplaySpecifiers-Win2k0.txt
%{_datadir}/samba/setup/display-specifiers/DisplaySpecifiers-Win2k3.txt
%{_datadir}/samba/setup/display-specifiers/DisplaySpecifiers-Win2k3R2.txt
%{_datadir}/samba/setup/display-specifiers/DisplaySpecifiers-Win2k8.txt
%{_datadir}/samba/setup/display-specifiers/DisplaySpecifiers-Win2k8R2.txt
%{_datadir}/samba/setup/dns_update_list
%{_datadir}/samba/setup/idmap_init.ldif
%{_datadir}/samba/setup/krb5.conf
%{_datadir}/samba/setup/named.conf
%{_datadir}/samba/setup/named.conf.dlz
%{_datadir}/samba/setup/named.conf.update
%{_datadir}/samba/setup/named.txt
%{_datadir}/samba/setup/prefixMap.txt
%{_datadir}/samba/setup/provision.ldif
%{_datadir}/samba/setup/provision.reg
%{_datadir}/samba/setup/provision.zone
%{_datadir}/samba/setup/provision_basedn.ldif
%{_datadir}/samba/setup/provision_basedn_modify.ldif
%{_datadir}/samba/setup/provision_basedn_options.ldif
%{_datadir}/samba/setup/provision_basedn_references.ldif
%{_datadir}/samba/setup/provision_computers_add.ldif
%{_datadir}/samba/setup/provision_computers_modify.ldif
%{_datadir}/samba/setup/provision_configuration.ldif
%{_datadir}/samba/setup/provision_configuration_basedn.ldif
%{_datadir}/samba/setup/provision_configuration_modify.ldif
%{_datadir}/samba/setup/provision_configuration_references.ldif
%{_datadir}/samba/setup/provision_dns_accounts_add.ldif
%{_datadir}/samba/setup/provision_dns_add_samba.ldif
%{_datadir}/samba/setup/provision_dnszones_add.ldif
%{_datadir}/samba/setup/provision_dnszones_modify.ldif
%{_datadir}/samba/setup/provision_dnszones_partitions.ldif
%{_datadir}/samba/setup/provision_group_policy.ldif
%{_datadir}/samba/setup/provision_init.ldif
%{_datadir}/samba/setup/provision_partitions.ldif
%{_datadir}/samba/setup/provision_privilege.ldif
%{_datadir}/samba/setup/provision_rootdse_add.ldif
%{_datadir}/samba/setup/provision_rootdse_modify.ldif
%{_datadir}/samba/setup/provision_schema_basedn.ldif
%{_datadir}/samba/setup/provision_schema_basedn_modify.ldif
%{_datadir}/samba/setup/provision_self_join.ldif
%{_datadir}/samba/setup/provision_self_join_config.ldif
%{_datadir}/samba/setup/provision_self_join_modify.ldif
%{_datadir}/samba/setup/provision_self_join_modify_config.ldif
%{_datadir}/samba/setup/provision_users.ldif
%{_datadir}/samba/setup/provision_users_add.ldif
%{_datadir}/samba/setup/provision_users_modify.ldif
%{_datadir}/samba/setup/provision_well_known_sec_princ.ldif
%{_datadir}/samba/setup/schema_samba4.ldif
%{_datadir}/samba/setup/secrets.ldif
%{_datadir}/samba/setup/secrets_dns.ldif
%{_datadir}/samba/setup/secrets_init.ldif
%{_datadir}/samba/setup/share.ldif
%{_datadir}/samba/setup/spn_update_list
%{_datadir}/samba/setup/ypServ30.ldif
%{_datadir}/samba/admx
%{_datadir}/samba/admx/samba.admx
%{_datadir}/samba/admx/en-US
%{_datadir}/samba/admx/en-US/samba.adml
%{_mandir}/man8/samba.8.*
%{_mandir}/man8/samba-tool.8.*
%{_mandir}/man8/samba_downgrade_db.8.*

%files dsdb-modules
%defattr(-,root,root)
%{_libdir}/samba/ldb/acl.so
%{_libdir}/samba/ldb/aclread.so
%{_libdir}/samba/ldb/anr.so
%{_libdir}/samba/ldb/descriptor.so
%{_libdir}/samba/ldb/dirsync.so
%{_libdir}/samba/ldb/dns_notify.so
%{_libdir}/samba/ldb/dsdb_notification.so
%{_libdir}/samba/ldb/encrypted_secrets.so
%{_libdir}/samba/ldb/extended_dn_in.so
%{_libdir}/samba/ldb/extended_dn_out.so
%{_libdir}/samba/ldb/extended_dn_store.so
%{_libdir}/samba/ldb/ildap.so
%{_libdir}/samba/ldb/instancetype.so
%{_libdir}/samba/ldb/lazy_commit.so
%{_libdir}/samba/ldb/ldbsamba_extensions.so
%{_libdir}/samba/ldb/linked_attributes.so
%{_libdir}/samba/ldb/new_partition.so
%{_libdir}/samba/ldb/objectclass.so
%{_libdir}/samba/ldb/objectclass_attrs.so
%{_libdir}/samba/ldb/objectguid.so
%{_libdir}/samba/ldb/operational.so
%{_libdir}/samba/ldb/partition.so
%{_libdir}/samba/ldb/password_hash.so
%{_libdir}/samba/ldb/ranged_results.so
%{_libdir}/samba/ldb/repl_meta_data.so
%{_libdir}/samba/ldb/resolve_oids.so
%{_libdir}/samba/ldb/rootdse.so
%{_libdir}/samba/ldb/samba3sam.so
%{_libdir}/samba/ldb/samba3sid.so
%{_libdir}/samba/ldb/samba_dsdb.so
%{_libdir}/samba/ldb/samba_secrets.so
%{_libdir}/samba/ldb/samldb.so
%{_libdir}/samba/ldb/schema_data.so
%{_libdir}/samba/ldb/schema_load.so
%{_libdir}/samba/ldb/secrets_tdb_sync.so
%{_libdir}/samba/ldb/show_deleted.so
%{_libdir}/samba/ldb/subtree_delete.so
%{_libdir}/samba/ldb/subtree_rename.so
%{_libdir}/samba/ldb/tombstone_reanimate.so
%{_libdir}/samba/ldb/unique_object_sids.so
%{_libdir}/samba/ldb/update_keytab.so
%{_libdir}/samba/ldb/vlv.so
%{_libdir}/samba/ldb/wins_ldb.so
%{_libdir}/samba/ldb/audit_log.so
%{_libdir}/samba/ldb/group_audit_log.so
%{_libdir}/samba/ldb/paged_results.so
%{_libdir}/samba/ldb/count_attrs.so
%endif

%changelog
