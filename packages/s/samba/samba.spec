#
# spec file for package samba
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


%if 0%{?sle_version} == 120500 && !0%{?is_opensuse}
# If building for 12 SP5 we have to manually define the macros for python3.6,
# the python-rpm-macros package provides the macros for python3.4
%define cpython3_soabi   %(python3.6 -c "import sysconfig; print(sysconfig.get_config_var('SOABI'))")
%define py3_soflags      %{cpython3_soabi}
%define py3_soflags_dash %(echo %{py3_soflags} | sed "s/_/-/g")
%define py3_incdir       %(python3.6 -c "import sysconfig as s; print(s.get_path('include'))")
%define python3_sitearch %{_libdir}/python3.6/site-packages
%else
%{!?py3_soflags:  %global py3_soflags cpython-%{python3_version_nodots}m}
%{!?py3_soflags_dash:   %global py3_soflags_dash %(echo %{py3_soflags} | sed "s/_/-/g")}
%endif

%{!?_fillupdir:%global _fillupdir /var/adm/fillup-templates}
%{!?_tmpfilesdir:%global _tmpfilesdir /usr/lib/tmpfiles.d}
%{!?_pam_moduledir:%global _pam_moduledir /%{_lib}/security}
%{!?_pam_confdir:%global _pam_confdir %{_sysconfdir}/pam.d}
%{!?_pam_secconfdir:%global _pam_secconfdir %{_sysconfdir}/security}

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

%define talloc_version 2.3.3
%define tevent_version 0.11.0
%define tdb_version    1.4.4
%define ldb_version    2.4.1

# This table represents the possible combinations of build macros.
# They are defined only if not already defined in the build service
# project configuration:
# https://openbuildservice.org/help/manuals/obs-user-guide/cha.obs.prjconfig.html#sec.prjconfig.macros
#
#                    %with_dc  %with_mit_dc  %with_mitkrb5
#---------------------------------------------------------
#           Heimdal      1         0              0
#  With DC
#           MIT          1         1              1
#---------------------------------------------------------
#           MIT          0         0              1
#  No DC
#           Heimdal      0         0              0
#---------------------------------------------------------
%if 0%{?sle_version} == 120500 && !0%{?is_opensuse}
%define with_mitkrb5 1
%define with_mit_dc 0
%define with_dc 0
%else
%{!?with_mitkrb5: %define with_mitkrb5 1}
%{!?with_mit_dc: %define with_mit_dc 1}
%{!?with_dc: %define with_dc 1}
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
%if 0%{?sle_version} == 120500 && !0%{?is_opensuse}
BuildRequires:  python36-devel
BuildRequires:  python36-xml
%else
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Markdown
BuildRequires:  python3-devel
BuildRequires:  python3-dnspython
BuildRequires:  python3-xml
%endif
BuildRequires:  readline-devel
%if 0%{?suse_version} >= 1330
BuildRequires:  rpcgen
%endif
%if 0%{?suse_version} > 1110
BuildRequires:  fdupes
%endif
%define pkgconfig_req pkg-config
BuildRequires:  %{pkgconfig_req}
%if 0%{?sle_version} != 120500 || 0%{?is_opensuse}
# Build with embedded libraries only in SLE 12 SP5, jsc#SLE-23330
BuildRequires:  libldb-devel >= %{ldb_version}
BuildRequires:  libtalloc-devel >= %{talloc_version}
BuildRequires:  libtdb-devel >= %{tdb_version}
BuildRequires:  libtevent-devel >= %{tevent_version}
BuildRequires:  python3-ldb-devel >= %{ldb_version}
BuildRequires:  python3-talloc-devel
BuildRequires:  python3-tdb
BuildRequires:  python3-tevent
%endif
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
BuildRequires:  libgnutls-devel >= 3.4.7
%if %{with_dc}
BuildRequires:  gpgme-devel
BuildRequires:  libjansson-devel
%if 0%{?sle_version} == 120500 && !0%{?is_opensuse}
BuildRequires:  python36-gpgme
%else
BuildRequires:  python3-gpgme
%endif
%if %{with_mit_dc}
BuildRequires:  krb5-devel >= 1.15.1
BuildRequires:  krb5-server >= 1.15.1
%endif
%else
BuildRequires:  krb5-devel
%endif
%if ! %{with_mitkrb5}
BuildRequires:  bison
BuildRequires:  flex
%endif
%if %{with_mscat}
BuildRequires:  libgnutls-devel >= 3.5.6
BuildRequires:  libtasn1-devel >= 3.8
%endif
%if 0%{?sle_version} > 150200 || 0%{?suse_version} > 1500
# liburing not yet available for all Factory architectures
%ifnarch ppc armv6l armv7l
BuildRequires:  liburing-devel
%endif
%endif

%if 0%{?suse_version} > 1140
%define	build_make_smp_mflags %{?_smp_mflags}
%else
%define	build_make_smp_mflags %{?jobs:-j%jobs}
%endif
Version:        4.15.5+git.328.f1f29505d84
Release:        0
URL:            https://www.samba.org/
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
Requires:       /usr/bin/grep
Requires:       coreutils
%if 0%{?sle_version} > 120500
Requires:       system-user-nobody
%endif
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
Requires(postun):/sbin/ldconfig
Recommends:     cifs-utils
Requires:       coreutils

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

%package devel
Summary:        Development files shared by Samba subpackages
License:        GPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       samba-client-libs
Requires:       samba-libs
Requires:       samba-winbind-libs
%if %{with_dc}
Requires:       samba-ad-dc-libs
%if %{with_mit_dc}
Requires:       pkgconfig(krb5)
%endif
%endif
Provides:       samba-core-devel = %{version}
Obsoletes:      samba-core-devel < %{version}
Provides:       libwbclient0-devel = %{version}
Obsoletes:      libwbclient0-devel < %{version}
Provides:       libdcerpc-samr-devel = %{version}
Obsoletes:      libdcerpc-samr-devel < %{version}
Provides:       libdcerpc-devel = %{version}
Obsoletes:      libdcerpc-devel < %{version}
Provides:       libndr-krb5pac-devel = %{version}
Obsoletes:      libndr-krb5pac-devel < %{version}
Provides:       libndr-nbt-devel = %{version}
Obsoletes:      libndr-nbt-devel < %{version}
Provides:       libndr-standard-devel = %{version}
Obsoletes:      libndr-standard-devel < %{version}
Provides:       libndr-devel = %{version}
Obsoletes:      libndr-devel < %{version}
Provides:       libsamba-credentials-devel = %{version}
Obsoletes:      libsamba-credentials-devel < %{version}
Provides:       libsamba-errors-devel = %{version}
Obsoletes:      libsamba-errors-devel < %{version}
Provides:       libsamba-hostconfig-devel = %{version}
Obsoletes:      libsamba-hostconfig-devel < %{version}
Provides:       libsamba-passdb-devel = %{version}
Obsoletes:      libsamba-passdb-devel < %{version}
Provides:       libsamba-util-devel = %{version}
Obsoletes:      libsamba-util-devel < %{version}
Provides:       libsamdb-devel = %{version}
Obsoletes:      libsamdb-devel < %{version}
Provides:       libsmbconf-devel = %{version}
Obsoletes:      libsmbconf-devel < %{version}
Provides:       libsmbldap-devel = %{version}
Obsoletes:      libsmbldap-devel < %{version}
Provides:       libtevent-util-devel = %{version}
Obsoletes:      libtevent-util-devel < %{version}
Provides:       libsmbclient-devel = %{version}
Obsoletes:      libsmbclient-devel < %{version}
Provides:       libnetapi-devel = %{version}
Obsoletes:      libnetapi-devel < %{version}
Provides:       libwbclient-devel = %{version}
Obsoletes:      libwbclient-devel < %{version}

%description devel
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

%package client-libs
Summary:        Samba client libraries
License:        GPL-3.0-or-later
Group:          Development/Libraries/C and C++
Provides:       libsmbclient0 = %{version}
Obsoletes:      libsmbclient0 < %{version}
Provides:       libndr2 = %{version}
Obsoletes:      libndr0 < %{version}
Obsoletes:      libndr1 < %{version}
Obsoletes:      libndr2 < %{version}
Provides:       libsmbldap2 = %{version}
Obsoletes:      libsmbldap0 < %{version}
Obsoletes:      libsmbldap2 < %{version}
Provides:       libsamba-credentials1 = %{version}
Obsoletes:      libsamba-credentials0 < %{version}
Obsoletes:      libsamba-credentials1 < %{version}
Provides:       libdcerpc-binding0 = %{version}
Obsoletes:      libdcerpc-binding0 < %{version}
Provides:       libndr-krb5pac0 = %{version}
Obsoletes:      libndr-krb5pac0 < %{version}
Provides:       libndr-nbt0 = %{version}
Obsoletes:      libndr-nbt0 < %{version}
Provides:       libndr-standard0 = %{version}
Obsoletes:      libndr-standard0 < %{version}
Provides:       libsamba-util0 = %{version}
Obsoletes:      libsamba-util0 < %{version}
Provides:       libsamba-errors0 = %{version}
Obsoletes:      libsamba-errors0 < %{version}
Provides:       libsamba-hostconfig0 = %{version}
Obsoletes:      libsamba-hostconfig0 < %{version}
Provides:       libtevent-util0 = %{version}
Obsoletes:      libtevent-util0 < %{version}
Provides:       libnetapi0 = %{version}
Obsoletes:      libnetapi0 < %{version}
Provides:       libsamba-passdb0 = %{version}
Obsoletes:      libsamba-passdb0 < %{version}
Provides:       libsamdb0 = %{version}
Obsoletes:      libsamdb0 < %{version}
Provides:       libwbclient0 = %{version}
Obsoletes:      libwbclient0 < %{version}
Provides:       libsmbconf0 = %{version}
Obsoletes:      libsmbconf0 < %{version}
Provides:       libdcerpc0 = %{version}
Obsoletes:      libdcerpc0 < %{version}

%description client-libs
The samba-libs package contains the libraries needed by samba client
programs.

%package libs
Summary:        Samba libraries
License:        GPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       samba-client-libs = %{version}
Recommends:     samba-libs-python3 = %{version}
Provides:       libdcerpc-samr0 = %{version}
Obsoletes:      libdcerpc-samr0 < %{version}

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
Requires:       libsamba-policy0-python3 = %{version}
Requires:       python3-ldb
Requires:       python3-talloc
Requires:       python3-tdb
Requires:       python3-tevent

%description python3
The samba-python3 package contains the Python libraries needed by programs
that use SMB, RPC and other Samba provided protocols in Python3 programs.

%package gpupdate
Summary:        Samba Group Policy
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Samba
Requires:       cepces
Requires:       certmonger
Requires:       samba-ldb-ldap = %{version}
Requires:       samba-python3 = %{version}
Requires:       sscep

%description gpupdate
The samba-gpupdate package provides the samba-gpupdate tool for applying
Group Policies on a Samba client.

%package ldb-ldap
Summary:        Samba Ldb Ldap Modules
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Samba

%description ldb-ldap
samba-ldb-ldap contains the ldb ldap module required by samba-tool and
samba-gpupdate.

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
Recommends:     /usr/sbin/nscd
Recommends:     cron
Recommends:     logrotate
%if 0%{?suse_version} < 1221
Requires:       %{?insserv_prereq}
%endif
Requires(pre):  /usr/sbin/groupadd
Requires:       coreutils
Requires:       samba-winbind-libs = %{version}
Recommends:     samba-gpupdate = %{version}

Requires(post): /sbin/ldconfig
Requires(postun):/sbin/ldconfig

%description winbind
This is the winbind-daemon and the wbinfo-tool.

%package winbind-libs
Summary:        Winbind Daemon libraries
License:        GPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       samba-client-libs = %{version}

Requires(post): /sbin/ldconfig
Requires(postun):/sbin/ldconfig

%description winbind-libs
This package contains the libraries required by the Winbind daemon.

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
Requires(pre):  coreutils
Requires(pre):  /bin/mktemp
Requires(pre):  /usr/bin/killall
Requires(pre):  /usr/bin/sed
Provides:       ctdb-tests = %{version}
Obsoletes:      ctdb-tests <= %{version}

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

%package ceph
Summary:        Ceph specific add-ons for Samba
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Samba
Requires:       samba = %{version}

%description ceph
The Ceph VFS module for Samba allows shares to be backed by the Ceph
distributed file system. A Ceph CTDB lock helper binary is included so
that RADOS locks can be used for CTDB split-brain avoidance.

%package -n samba-tool
Summary:        Main Samba administration tool
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Samba
Requires:       samba = %{version}
Requires:       samba-ldb-ldap = %{version}
Requires:       samba-python3 = %{version}

%description -n samba-tool
The package contains samba-tool, the main tool for Samba Administration.

%package ad-dc
Summary:        Samba Active Directory-compatible Domain Controller
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Samba
Requires:       samba = %{version}
Requires:       samba-dsdb-modules = %{version}
%if %{with_mit_dc}
Recommends:     krb5-server >= 1.15.1
%endif
Requires:       samba-python3 = %{version}
Requires:       samba-tool = %{version}
Recommends:     samba-winbind = %{version}
Recommends:     tdb-tools >= %{tdb_version}
Provides:       samba-kdc = %{version}
Obsoletes:      samba-kdc < %{version}

%description ad-dc
This package contains the Active Directory-compatible Domain Controller

%package ad-dc-libs
Summary:        Samba Active Directory Domain Controller libraries
License:        GPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       samba-client-libs = %{version}
Requires:       samba-libs = %{version}

%description ad-dc-libs
This package contains the Active Directory-compatible Domain Controller
libraries.

%package dsdb-modules
Summary:        Samba LDB modules
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Samba
Requires:       libldb2 >= %{ldb_version}
Requires:       samba-ldb-ldap = %{version}
Requires(post): /sbin/ldconfig
Requires(postun):/sbin/ldconfig

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
%if 0%{?sle_version} == 120500 && !0%{?is_opensuse}
# Build with embedded libraries only in SLE 12 SP5, jsc#SLE-23330
bundled_libraries_extra+=",talloc,pytalloc,tdb,pytdb,tevent,pytevent,ldb,pyldb"
bundled_libraries_extra+=",pytalloc-util.%{py3_soflags}"
bundled_libraries_extra+=",pyldb-util.%{py3_soflags}"
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
	--with-profiling-data \
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
	--with-pammodulesdir=%_pam_moduledir\
	--with-piddir=%{PIDDIR} \
	--with-relro \
%if 0%{?suse_version} > 1220
	--enable-avahi \
	--with-systemd \
	--with-systemddir=%{_unitdir} \
	--systemd-install-services \
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
%if %{with_dc} && %{with_mit_dc}
	--with-experimental-mit-ad-dc \
%endif
%endif
	--bundled-libraries=NONE,socket_wrapper,cmocka,${bundled_libraries_extra} \
	--without-fam \
"

%if 0%{?sle_version} == 120500 && !0%{?is_opensuse}
PYTHON=/usr/bin/python3.6 ./configure ${CONFIGURE_OPTIONS}
PYTHON=/usr/bin/python3.6 make %{?_smp_mflags}
%else
./configure ${CONFIGURE_OPTIONS}
make %{?_smp_mflags}
%endif

pushd docs-xml
autoconf && ./configure
XML_CATALOG_FILES="file:///etc/xml/catalog file://$(pwd)/build/catalog.xml" make htmlman
popd

pushd ctdb
%if 0%{?sle_version} == 120500 && !0%{?is_opensuse}
PYTHON=/usr/bin/python3.6 XML_CATALOG_FILES="file:///etc/xml/catalog file://$(pwd)/build/catalog.xml" make %{?_smp_mflags} manpages
%else
XML_CATALOG_FILES="file:///etc/xml/catalog file://$(pwd)/build/catalog.xml" make %{?_smp_mflags} manpages
%endif
popd

%install
install -d -m 0755 -p \
	%{buildroot}/%_pam_confdir \
	%{buildroot}/%{_sysconfdir}/{xinetd.d,logrotate.d} \
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

%if 0%{?sle_version} == 120500 && !0%{?is_opensuse}
PYTHON=/usr/bin/python3.6 make %{?_smp_mflags} install \
	DESTDIR=%{buildroot} \
	CONFIGDIR=%{CONFIGDIR}
%else
make %{?_smp_mflags} install \
	DESTDIR=%{buildroot} \
	CONFIGDIR=%{CONFIGDIR}
%endif

%if 0%{?sle_version} == 120500 && !0%{?is_opensuse}
# Build with embedded libraries only in SLE 12 SP5, jsc#SLE-23330
# Move the ldb and tdb tools to libdir to do not interfere with
# system-wide tools provided by libldb1 and libtdb1 system packages

install -d -m 0755 %{buildroot}/%{_libdir}/samba/bin
mv %{buildroot}/%{_bindir}/ldbadd \
   %{buildroot}/%{_bindir}/ldbdel \
   %{buildroot}/%{_bindir}/ldbedit \
   %{buildroot}/%{_bindir}/ldbmodify \
   %{buildroot}/%{_bindir}/ldbrename \
   %{buildroot}/%{_bindir}/ldbsearch \
   %{buildroot}/%{_bindir}/tdbbackup \
   %{buildroot}/%{_bindir}/tdbdump \
   %{buildroot}/%{_bindir}/tdbrestore \
   %{buildroot}/%{_bindir}/tdbtool \
   %{buildroot}/%{_libdir}/samba/bin

install -d -m 0755 %{buildroot}/%{_libdir}/samba/man/man1
install -d -m 0755 %{buildroot}/%{_libdir}/samba/man/man3
install -d -m 0755 %{buildroot}/%{_libdir}/samba/man/man8
mv %{buildroot}/%{_mandir}/man1/ldbadd.1 \
   %{buildroot}/%{_mandir}/man1/ldbdel.1 \
   %{buildroot}/%{_mandir}/man1/ldbedit.1 \
   %{buildroot}/%{_mandir}/man1/ldbmodify.1 \
   %{buildroot}/%{_mandir}/man1/ldbrename.1 \
   %{buildroot}/%{_mandir}/man1/ldbsearch.1 \
   %{buildroot}/%{_libdir}/samba/man/man1/
mv %{buildroot}/%{_mandir}/man3/ldb.3 \
   %{buildroot}/%{_mandir}/man3/talloc.3 \
   %{buildroot}/%{_libdir}/samba/man/man3/
mv %{buildroot}/%{_mandir}/man8/tdbbackup.8 \
   %{buildroot}/%{_mandir}/man8/tdbdump.8 \
   %{buildroot}/%{_mandir}/man8/tdbrestore.8 \
   %{buildroot}/%{_mandir}/man8/tdbtool.8 \
   %{buildroot}/%{_libdir}/samba/man/man8/
%endif

# debug symbols are created and installed if the files are excluded only
%if ! %{with_dc}
rm \
	%{buildroot}/%{_mandir}/man8/samba.8* \
	%{buildroot}/%{_mandir}/man8/samba_downgrade_db.8* \
	%{buildroot}/%{_unitdir}/samba-ad-dc.service \
	%{buildroot}/%{_libdir}/samba/libdsdb-module-samba4.so
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
	ln -s service %{buildroot}/%{_sbindir}/rc${srv_name}
done
%if %{with_dc}
	ln -s service %{buildroot}/%{_sbindir}/rcsamba-ad-dc
	install -m 0644 systemd/sysconfig.samba-ad-dc %{buildroot}%{_fillupdir}
%endif
rm %{buildroot}/%{_sysconfdir}/sysconfig/samba
install -m 0644 systemd/sysconfig.samba %{buildroot}%{_fillupdir}
install -m 0644 systemd/sysconfig.samba-winbind %{buildroot}%{_fillupdir}
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
install -m 0644 config/samba.pamd-common %{buildroot}/%_pam_confdir/samba
install -m 0644 config/dhcp.conf %{buildroot}/%{_fillupdir}/samba-client-dhcp.conf
install -m 0644 config/sysconfig.dhcp-samba-client %{buildroot}/%{_fillupdir}/sysconfig.dhcp-samba-client

# Network scripts
%if 0%{?suse_version} <= 1500
NETWORK_SCRIPTS="samba-winbindd dhcpcd-hook-samba dhcpcd-hook-samba-functions"
%else
NETWORK_SCRIPTS="samba-winbindd"
%endif
for script in ${NETWORK_SCRIPTS}; do
	install -m 0755 "tools/${script}" "%{buildroot}/%{_sysconfdir}/sysconfig/%{NET_CFGDIR}/scripts/${script}"
done

# Create ghosts for the symlinks
%if 0%{?suse_version} <= 1500
NETWORK_LINKS="55-samba-winbindd 21-dhcpcd-hook-samba"
%else
NETWORK_LINKS="55-samba-winbindd"
%endif
for script in ${NETWORK_LINKS}; do
	touch %{buildroot}/%{_sysconfdir}/sysconfig/%{NET_CFGDIR}/if-{down,up}.d/${script}
done

# Install SuSEfirewall2 config files
%if 0%{?suse_version} <= 1500
install -m 0644 config/sysconfig.firewall.netbios-server \
	%{buildroot}%{_sysconfdir}/sysconfig/SuSEfirewall2.d/services/netbios-server
install -m 0644 config/sysconfig.firewall.samba-server \
	%{buildroot}%{_sysconfdir}/sysconfig/SuSEfirewall2.d/services/samba-server
install -m 0644 config/sysconfig.firewall.samba-client \
	%{buildroot}%{_sysconfdir}/sysconfig/SuSEfirewall2.d/services/samba-client
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
install -m 0644 examples/pam_winbind/pam_winbind.conf %{buildroot}/%_pam_secconfdir/pam_winbind.conf
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
if testparm -s  2>&1 | grep "server schannel ="  | grep -E "Auto|No"
then
    echo "CVE-2020-1472(ZeroLogon):"
    echo "Please configure 'server schannel = yes'"
    echo "See https://bugzilla.samba.org/show_bug.cgi?id=14497"
fi
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
%tmpfiles_create samba.conf
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
%if 0%{?suse_version} < 1221
%{?stop_on_removal:%{stop_on_removal %cifs_init_script}}
%endif

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

%post   -n libsamba-policy0-python3 -p /sbin/ldconfig
%postun -n libsamba-policy0-python3 -p /sbin/ldconfig
%post client-libs -p /sbin/ldconfig
%postun client-libs -p /sbin/ldconfig
%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig
%post ad-dc-libs -p /sbin/ldconfig
%postun ad-dc-libs -p /sbin/ldconfig
%post winbind-libs -p /sbin/ldconfig
%postun winbind-libs -p /sbin/ldconfig
%post test -p /sbin/ldconfig
%postun test -p /sbin/ldconfig

%if %{with_dc}
%post ad-dc
/sbin/ldconfig
%service_add_post samba-ad-dc.service
%{fillup_only -ans samba ad-dc}

%postun ad-dc
/sbin/ldconfig
%service_del_postun samba-ad-dc.service
%endif

%post dsdb-modules
rm -f %{_libdir}/ldb/samba
ln -sf %{_libdir}/samba/ldb %{_libdir}/ldb2/modules/ldb/samba
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
%tmpfiles_create samba.conf
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
%tmpfiles_create ctdb.conf
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
%config %_pam_confdir/samba
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
%{_libdir}/samba/samba-bgqd
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
%{_mandir}/man8/samba-bgqd.8.*
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
%if 0%{?suse_version} <= 1500
%ghost %{_sysconfdir}/sysconfig/%{NET_CFGDIR}/if-down.d/21-dhcpcd-hook-samba
%ghost %{_sysconfdir}/sysconfig/%{NET_CFGDIR}/if-up.d/21-dhcpcd-hook-samba
%{_sysconfdir}/sysconfig/%{NET_CFGDIR}/scripts/dhcpcd-hook-samba
%{_sysconfdir}/sysconfig/%{NET_CFGDIR}/scripts/dhcpcd-hook-samba-functions
%{_sysconfdir}/sysconfig/SuSEfirewall2.d/services/samba-client
%endif
%{_bindir}/cifsdd
%{_bindir}/dbwrap_tool
%{_sbindir}/eventlogadm
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
%if 0%{?sle_version} == 120500 && !0%{?is_opensuse}
# Build with embedded libraries for SLE 12 SP5, jsc#SLE-23330
%dir %{_libdir}/samba/bin/
%{_libdir}/samba/bin/ldbadd
%{_libdir}/samba/bin/ldbdel
%{_libdir}/samba/bin/ldbedit
%{_libdir}/samba/bin/ldbmodify
%{_libdir}/samba/bin/ldbrename
%{_libdir}/samba/bin/ldbsearch
%{_libdir}/samba/bin/tdbbackup
%{_libdir}/samba/bin/tdbdump
%{_libdir}/samba/bin/tdbrestore
%{_libdir}/samba/bin/tdbtool
%dir %{_libdir}/samba/man
%dir %{_libdir}/samba/man/man1
%{_libdir}/samba/man/man1/ldbadd.1*
%{_libdir}/samba/man/man1/ldbdel.1*
%{_libdir}/samba/man/man1/ldbedit.1*
%{_libdir}/samba/man/man1/ldbmodify.1*
%{_libdir}/samba/man/man1/ldbrename.1*
%{_libdir}/samba/man/man1/ldbsearch.1*
%dir %{_libdir}/samba/man/man3
%{_libdir}/samba/man/man3/ldb.3*
%{_libdir}/samba/man/man3/talloc.3*
%dir %{_libdir}/samba/man/man8
%{_libdir}/samba/man/man8/tdbbackup.8*
%{_libdir}/samba/man/man8/tdbdump.8*
%{_libdir}/samba/man/man8/tdbrestore.8*
%{_libdir}/samba/man/man8/tdbtool.8*
%endif

%files devel
%defattr(-,root,root)
%{_includedir}/samba
%dir %_includedir/samba-4.0/
%_includedir/samba-4.0/charset.h
%_includedir/samba-4.0/rpc_common.h
%_includedir/samba-4.0/dcesrv_core.h
%_includedir/samba-4.0/credentials.h
%_includedir/samba-4.0/ndr.h
%_includedir/samba-4.0/smbldap.h
%_includedir/samba-4.0/smb_ldap.h
%_includedir/samba-4.0/param.h
%_includedir/samba-4.0/ldb_wrap.h
%_includedir/samba-4.0/smbconf.h
%_includedir/samba-4.0/dcerpc.h
%_includedir/samba-4.0/wbclient.h
%_includedir/samba-4.0/lookup_sid.h
%_includedir/samba-4.0/machine_sid.h
%_includedir/samba-4.0/passdb.h
%_includedir/samba-4.0/netapi.h
%_includedir/samba-4.0/libsmbclient.h
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
%_includedir/samba-4.0/gen_ndr/misc.h
%_includedir/samba-4.0/gen_ndr/ndr_misc.h
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
%_includedir/samba-4.0/gen_ndr/samr.h
%_includedir/samba-4.0/gen_ndr/ndr_samr.h
%_includedir/samba-4.0/gen_ndr/lsa.h
%_includedir/samba-4.0/gen_ndr/netlogon.h
%_includedir/samba-4.0/gen_ndr/atsvc.h
%_includedir/samba-4.0/gen_ndr/ndr_atsvc.h
%_includedir/samba-4.0/gen_ndr/ndr_svcctl.h
%_includedir/samba-4.0/gen_ndr/svcctl.h
%_includedir/samba-4.0/gen_ndr/ndr_samr_c.h
%_includedir/samba-4.0/gen_ndr/nbt.h
%_includedir/samba-4.0/gen_ndr/ndr_nbt.h
%_includedir/samba-4.0/gen_ndr/krb5pac.h
%_includedir/samba-4.0/gen_ndr/ndr_krb5pac.h
%_includedir/samba-4.0/ndr/ndr_krb5pac.h
%dir %_includedir/samba-4.0/ndr/
%_includedir/samba-4.0/ndr/ndr_dcerpc.h
%_includedir/samba-4.0/ndr/ndr_drsblobs.h
%_includedir/samba-4.0/ndr/ndr_drsuapi.h
%_includedir/samba-4.0/ndr/ndr_svcctl.h
%_includedir/samba-4.0/ndr/ndr_nbt.h
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
%_includedir/samba-4.0/util/attr.h
%_includedir/samba-4.0/util/blocking.h
%_includedir/samba-4.0/util/data_blob.h
%_includedir/samba-4.0/util/debug.h
%_includedir/samba-4.0/util/discard.h
%_includedir/samba-4.0/util/fault.h
%_includedir/samba-4.0/util/signal.h
%_includedir/samba-4.0/util/substitute.h
%_includedir/samba-4.0/util/time.h
%_includedir/samba-4.0/util/tevent_ntstatus.h
%_includedir/samba-4.0/util/tevent_unix.h
%_includedir/samba-4.0/util/tevent_werror.h
%{_libdir}/libnss_winbind.so
%{_libdir}/libnss_wins.so
%{_libdir}/libsamba-credentials.so
%{_libdir}/pkgconfig/samba-credentials.pc
%{_libdir}/libndr.so
%{_libdir}/pkgconfig/ndr.pc
%{_libdir}/libsmbldap.so
%{_libdir}/libsamba-util.so
%{_libdir}/pkgconfig/samba-util.pc
%{_libdir}/libsamba-errors.so
%{_libdir}/libsamba-hostconfig.so
%{_libdir}/pkgconfig/samba-hostconfig.pc
%{_libdir}/libtevent-util.so
%{_libdir}/libndr-standard.so
%{_libdir}/pkgconfig/ndr_standard.pc
%{_libdir}/libsmbconf.so
%{_libdir}/libdcerpc.so
%{_libdir}/libdcerpc-binding.so
%{_libdir}/pkgconfig/dcerpc.pc
%{_libdir}/libdcerpc-server-core.so
%{_libdir}/libdcerpc-samr.so
%{_libdir}/pkgconfig/dcerpc_samr.pc
%{_libdir}/libndr-nbt.so
%{_libdir}/pkgconfig/ndr_nbt.pc
%{_libdir}/libsamdb.so
%{_libdir}/pkgconfig/samdb.pc
%{_libdir}/libwbclient.so
%{_libdir}/pkgconfig/wbclient.pc
%{_libdir}/libndr-krb5pac.so
%{_libdir}/pkgconfig/ndr_krb5pac.pc
%{_libdir}/libsamba-passdb.so
%{_libdir}/libnetapi.so
%{_libdir}/pkgconfig/netapi.pc
%{_libdir}/libsmbclient.so
%{_libdir}/pkgconfig/smbclient.pc
%{_mandir}/man7/libsmbclient.7.*
%if %{with_dc}
%{_includedir}/samba-4.0/dcerpc_server.h
%{_libdir}/libdcerpc-server.so
%{_libdir}/pkgconfig/dcerpc_server.pc
%endif

%files client-libs
%{_libdir}/libdcerpc-binding.so.*
%{_libdir}/libdcerpc-server-core.so.*
%{_libdir}/libdcerpc.so.*
%{_libdir}/libndr-krb5pac.so.*
%{_libdir}/libndr-nbt.so.*
%{_libdir}/libndr-standard.so.*
%{_libdir}/libndr.so.*
%{_libdir}/libnetapi.so.*
%{_libdir}/libsamba-credentials.so.*
%{_libdir}/libsamba-errors.so.*
%{_libdir}/libsamba-hostconfig.so.*
%{_libdir}/libsamba-passdb.so.*
%{_libdir}/libsamba-util.so.*
%{_libdir}/libsamdb.so.*
%{_libdir}/libsmbclient.so.*
%{_libdir}/libsmbconf.so.*
%{_libdir}/libsmbldap.so.*
%{_libdir}/libwbclient.so.*
%{_libdir}/samba/libCHARSET3-samba4.so
%{_libdir}/samba/libMESSAGING-samba4.so
%{_libdir}/samba/libMESSAGING-SEND-samba4.so
%{_libdir}/samba/libaddns-samba4.so
%{_libdir}/samba/libads-samba4.so
%{_libdir}/samba/libasn1util-samba4.so
%{_libdir}/samba/libauth-samba4.so
%{_libdir}/samba/libauthkrb5-samba4.so
%{_libdir}/samba/libcli-cldap-samba4.so
%{_libdir}/samba/libcli-ldap-samba4.so
%{_libdir}/samba/libcli-ldap-common-samba4.so
%{_libdir}/samba/libcli-nbt-samba4.so
%{_libdir}/samba/libcli-smb-common-samba4.so
%{_libdir}/samba/libcli-spoolss-samba4.so
%{_libdir}/samba/libcliauth-samba4.so
%{_libdir}/samba/libclidns-samba4.so
%{_libdir}/samba/libcmdline-contexts-samba4.so
%{_libdir}/samba/libcmdline-samba4.so
%{_libdir}/samba/libcommon-auth-samba4.so
%{_libdir}/samba/libdbwrap-samba4.so
%{_libdir}/samba/libdcerpc-pkt-auth-samba4.so
%{_libdir}/samba/libdcerpc-samba-samba4.so
%{_libdir}/samba/libdcerpc-samba4.so
%{_libdir}/samba/libevents-samba4.so
%{_libdir}/samba/libflag-mapping-samba4.so
%{_libdir}/samba/libgenrand-samba4.so
%{_libdir}/samba/libgensec-samba4.so
%{_libdir}/samba/libgpo-samba4.so
%{_libdir}/samba/libgse-samba4.so
%{_libdir}/samba/libhttp-samba4.so
%{_libdir}/samba/libinterfaces-samba4.so
%{_libdir}/samba/libiov-buf-samba4.so
%{_libdir}/samba/libkrb5samba-samba4.so
%{_libdir}/samba/libldbsamba-samba4.so
%{_libdir}/samba/liblibcli-lsa3-samba4.so
%{_libdir}/samba/liblibcli-netlogon3-samba4.so
%{_libdir}/samba/liblibsmb-samba4.so
%{_libdir}/libtevent-util.so.*
%{_libdir}/samba/libmessages-dgm-samba4.so
%{_libdir}/samba/libmessages-util-samba4.so
%{_libdir}/samba/libmsghdr-samba4.so
%{_libdir}/samba/libmsrpc3-samba4.so
%{_libdir}/samba/libndr-samba4.so
%{_libdir}/samba/libndr-samba-samba4.so
%{_libdir}/samba/libnet-keytab-samba4.so
%{_libdir}/samba/libnetif-samba4.so
%{_libdir}/samba/libnpa-tstream-samba4.so
%{_libdir}/samba/libprinting-migrate-samba4.so
%{_libdir}/samba/libregistry-samba4.so
%{_libdir}/samba/libreplace-samba4.so
%{_libdir}/samba/libsamba-cluster-support-samba4.so
%{_libdir}/samba/libsamba-debug-samba4.so
%{_libdir}/samba/libsamba-security-samba4.so
%{_libdir}/samba/libsamba-sockets-samba4.so
%{_libdir}/samba/libsamba3-util-samba4.so
%{_libdir}/samba/libsamba-modules-samba4.so
%{_libdir}/samba/libsamdb-common-samba4.so
%{_libdir}/samba/libsmb-transport-samba4.so
%{_libdir}/samba/libsmbclient-raw-samba4.so
%{_libdir}/samba/libsmbd-base-samba4.so
%{_libdir}/samba/libsmbd-shim-samba4.so
%{_libdir}/samba/libsmbldaphelper-samba4.so
%{_libdir}/samba/libsecrets3-samba4.so
%{_libdir}/samba/libserver-id-db-samba4.so
%{_libdir}/samba/libserver-role-samba4.so
%{_libdir}/samba/libsocket-blocking-samba4.so
%{_libdir}/samba/libsys-rw-samba4.so
%{_libdir}/samba/libtalloc-report-printf-samba4.so
%{_libdir}/samba/libtdb-wrap-samba4.so
%{_libdir}/samba/libtime-basic-samba4.so
%{_libdir}/samba/libtrusts-util-samba4.so
%{_libdir}/samba/libutil-reg-samba4.so
%{_libdir}/samba/libutil-setid-samba4.so
%{_libdir}/samba/libutil-tdb-samba4.so
%{_libdir}/samba/libwinbind-client-samba4.so
%if 0%{?sle_version} == 120500 && !0%{?is_opensuse}
# Build with embedded libraries for SLE 12 SP5, jsc#SLE-23330
%{_libdir}/samba/libtalloc.so.*
%{_libdir}/samba/libtdb.so.*
%{_libdir}/samba/libtevent.so.*
%{_libdir}/samba/libldb.so.*
%{_libdir}/samba/libldb-cmdline-samba4.so
%{_libdir}/samba/libldb-key-value-samba4.so
%{_libdir}/samba/libldb-tdb-err-map-samba4.so
%{_libdir}/samba/libldb-tdb-int-samba4.so
%{_libdir}/samba/ldb/asq.so
%{_libdir}/samba/ldb/ldb.so
%{_libdir}/samba/ldb/paged_searches.so
%{_libdir}/samba/ldb/rdn_name.so
%{_libdir}/samba/ldb/sample.so
%{_libdir}/samba/ldb/server_sort.so
%{_libdir}/samba/ldb/skel.so
%{_libdir}/samba/ldb/tdb.so
%{_libdir}/samba/libpyldb-util.%{py3_soflags_dash}.so.*
%{_libdir}/samba/libpytalloc-util.%{py3_soflags_dash}.so.*
%endif
%if %{with_mscat}
%{_libdir}/samba/libmscat-samba4.so
%endif
%if %{with_dc}
%{_libdir}/samba/libdfs-server-ad-samba4.so
%endif

%files libs
%defattr(-,root,root)
%{_libdir}/libdcerpc-samr.so.*
%dir %{_libdir}/samba
%{_libdir}/samba/libLIBWBCLIENT-OLD-samba4.so
%{_libdir}/samba/libauth4-samba4.so
%{_libdir}/samba/libauth-unix-token-samba4.so
%{_libdir}/samba/libcluster-samba4.so
%{_libdir}/samba/libdnsserver-common-samba4.so
%{_libdir}/samba/libgpext-samba4.so
%{_libdir}/samba/libposix-eadb-samba4.so
%{_libdir}/samba/libprinter-driver-samba4.so
%{_libdir}/samba/libshares-samba4.so
%{_libdir}/samba/libsmbpasswdparser-samba4.so
%{_libdir}/samba/libtalloc-report-samba4.so
%{_libdir}/samba/libtorture-samba4.so
%{_libdir}/samba/libxattr-tdb-samba4.so
%{_libdir}/samba/libcmocka-samba4.so
%dir %{_libdir}/samba/pdb
%{_libdir}/samba/pdb/ldapsam.so
%{_libdir}/samba/pdb/smbpasswd.so
%{_libdir}/samba/pdb/tdbsam.so
%if ! %{with_mitkrb5}
%{_libdir}/samba/libasn1-samba4.so.*
%{_libdir}/samba/libcom_err-samba4.so.*
%{_libdir}/samba/libgssapi-samba4.so.*
%{_libdir}/samba/libhcrypto-samba4.so.*
%{_libdir}/samba/libhdb-samba4.so.*
%{_libdir}/samba/libheimbase-samba4.so.*
%{_libdir}/samba/libheimntlm-samba4.so.*
%{_libdir}/samba/libhx509-samba4.so.*
%{_libdir}/samba/libkdc-samba4.so.*
%{_libdir}/samba/libkrb5-samba4.so.*
%{_libdir}/samba/libroken-samba4.so.*
%{_libdir}/samba/libwind-samba4.so.*
%endif

%files libs-python3
%{_libdir}/samba/libsamba-net.%{py3_soflags_dash}-samba4.so
%{_libdir}/samba/libsamba-python.%{py3_soflags_dash}-samba4.so

%files python3
%defattr(-,root,root)
%{python3_sitearch}/*

%files gpupdate
%defattr(-,root,root)
%{_sbindir}/samba-gpupdate
%{_mandir}/man8/samba-gpupdate.8.gz

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
%{_bindir}/mdsearch
%{_mandir}/man1/gentest.1.*
%{_mandir}/man1/locktest.1.*
%{_mandir}/man1/masktest.1.*
%{_mandir}/man1/ndrdump.1.*
%{_mandir}/man1/vfstest.1.*
%{_mandir}/man1/mdsearch.1.*

%files winbind-libs
%defattr(-,root,root)
%{_pam_moduledir}/pam_winbind.so
%{_libdir}/libnss_winbind.so.*
%{_libdir}/samba/libidmap-samba4.so
%{_libdir}/samba/libnss-info-samba4.so
%dir %{_libdir}/samba/idmap
%{_libdir}/samba/idmap/ad.so
%{_libdir}/samba/idmap/autorid.so
%{_libdir}/samba/idmap/hash.so
%{_libdir}/samba/idmap/ldap.so
%{_libdir}/samba/idmap/rfc2307.so
%{_libdir}/samba/idmap/rid.so
%{_libdir}/samba/idmap/script.so
%{_libdir}/samba/idmap/tdb2.so
%dir %{_libdir}/samba/nss_info
%{_libdir}/samba/nss_info/rfc2307.so
%{_libdir}/samba/nss_info/hash.so
%{_libdir}/samba/nss_info/sfu.so
%{_libdir}/samba/nss_info/sfu20.so
%dir %{_libdir}/samba/krb5
%{_libdir}/samba/krb5/async_dns_krb5_locator.so
%{_libdir}/samba/krb5/winbind_krb5_locator.so
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
%{_mandir}/man5/pam_winbind.conf.5.*
%{_mandir}/man8/pam_winbind.8.*
%{_mandir}/man8/winbind_krb5_locator.8.*
%if %{with_mitkrb5}
%{_libdir}/samba/krb5/winbind_krb5_localauth.so
%{_mandir}/man8/winbind_krb5_localauth.8.*
%endif

%files winbind -f filelist-samba-winbind
%defattr(-,root,root)
%config(noreplace) %_pam_secconfdir/pam_winbind.conf
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
%{_mandir}/man1/ntlm_auth.1.*
%{_mandir}/man1/wbinfo.1.*
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
%dir %{_datadir}/ctdb
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
%{_libdir}/ctdb/tdb_mutex_check
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

%files -n samba-tool
%{_bindir}/samba-tool
%{_mandir}/man8/samba-tool.8.*

%if %{with_dc}
%files ad-dc
%{_fillupdir}/sysconfig.samba-ad-dc
%{_unitdir}/samba-ad-dc.service
%{_sbindir}/samba
%{_sbindir}/samba_dnsupdate
%{_sbindir}/samba_kcc
%{_sbindir}/samba_spnupdate
%{_sbindir}/samba_upgradedns
%{_sbindir}/samba_downgrade_db
%{_sbindir}/rcsamba-ad-dc
%dir %{_datadir}/samba/setup
%{_datadir}/samba/setup/aggregate_schema.ldif
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
%{_datadir}/samba/setup/extended-rights.ldif
%{_datadir}/samba/setup/provision_self_join_modify_schema.ldif
%dir %{_datadir}/samba/setup/ad-schema
%{_datadir}/samba/setup/ad-schema/MS-AD_Schema_2K8_Attributes.txt
%{_datadir}/samba/setup/ad-schema/MS-AD_Schema_2K8_Classes.txt
%{_datadir}/samba/setup/ad-schema/MS-AD_Schema_2K8_R2_Attributes.txt
%{_datadir}/samba/setup/ad-schema/MS-AD_Schema_2K8_R2_Classes.txt
%{_datadir}/samba/setup/ad-schema/AD_DS_Attributes__Windows_Server_2012_R2.ldf
%{_datadir}/samba/setup/ad-schema/AD_DS_Attributes__Windows_Server_2016.ldf
%{_datadir}/samba/setup/ad-schema/AD_DS_Classes__Windows_Server_2012_R2.ldf
%{_datadir}/samba/setup/ad-schema/AD_DS_Classes__Windows_Server_2016.ldf
%{_datadir}/samba/setup/ad-schema/Attributes_for_AD_DS__Windows_Server_2008_R2.ldf
%{_datadir}/samba/setup/ad-schema/Attributes_for_AD_DS__Windows_Server_2012.ldf
%{_datadir}/samba/setup/ad-schema/Classes_for_AD_DS__Windows_Server_2008_R2.ldf
%{_datadir}/samba/setup/ad-schema/Classes_for_AD_DS__Windows_Server_2012.ldf
%{_datadir}/samba/setup/ad-schema/licence.txt
%dir %{_datadir}/samba/setup/adprep
%{_datadir}/samba/setup/adprep/fix-forest-rev.ldf
%dir %{_datadir}/samba/setup/adprep/WindowsServerDocs
%{_datadir}/samba/setup/adprep/WindowsServerDocs/Forest-Wide-Updates.md
%{_datadir}/samba/setup/adprep/WindowsServerDocs/Sch49.ldf.diff
%{_datadir}/samba/setup/adprep/WindowsServerDocs/Sch50.ldf.diff
%{_datadir}/samba/setup/adprep/WindowsServerDocs/Sch51.ldf.diff
%{_datadir}/samba/setup/adprep/WindowsServerDocs/Sch57.ldf.diff
%{_datadir}/samba/setup/adprep/WindowsServerDocs/Sch59.ldf.diff
%{_datadir}/samba/setup/adprep/WindowsServerDocs/Schema-Updates.md
%dir %{_datadir}/samba/setup/display-specifiers
%{_datadir}/samba/setup/display-specifiers/DisplaySpecifiers-Win2k0.txt
%{_datadir}/samba/setup/display-specifiers/DisplaySpecifiers-Win2k3.txt
%{_datadir}/samba/setup/display-specifiers/DisplaySpecifiers-Win2k3R2.txt
%{_datadir}/samba/setup/display-specifiers/DisplaySpecifiers-Win2k8.txt
%{_datadir}/samba/setup/display-specifiers/DisplaySpecifiers-Win2k8R2.txt
%dir %{_datadir}/samba/admx
%{_datadir}/samba/admx/samba.admx
%{_datadir}/samba/admx/en-US
%{_datadir}/samba/admx/en-US/samba.adml
%{_mandir}/man8/samba.8.*
%{_mandir}/man8/samba_downgrade_db.8.*
%endif

%files ldb-ldap
%defattr(-,root,root)
%{_libdir}/samba/ldb/ildap.so
%{_libdir}/samba/ldb/ldbsamba_extensions.so

%if %{with_dc}
%files ad-dc-libs
%defattr(-,root,root)
%{_libdir}/samba/libdb-glue-samba4.so
%{_libdir}/samba/libdsdb-module-samba4.so
%{_libdir}/samba/libdsdb-garbage-collect-tombstones-samba4.so
%{_libdir}/samba/libscavenge-dns-records-samba4.so
%{_libdir}/samba/libprocess-model-samba4.so
%{_libdir}/samba/libservice-samba4.so
%dir %{_libdir}/samba/process_model
%{_libdir}/samba/process_model/standard.so
%{_libdir}/samba/process_model/prefork.so
%dir %{_libdir}/samba/service
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
%{_libdir}/libdcerpc-server.so.*
%if %{with_mit_dc}
%{_libdir}/krb5/plugins/kdb/samba.so
%else
%{_libdir}/samba/libHDB-SAMBA4-samba4.so
%endif
%dir %{_libdir}/samba/bind9
%{_libdir}/samba/bind9/dlz_bind9_10.so
%{_libdir}/samba/bind9/dlz_bind9_11.so
%{_libdir}/samba/bind9/dlz_bind9_12.so
%{_libdir}/samba/bind9/dlz_bind9_14.so
%{_libdir}/samba/bind9/dlz_bind9_16.so
%dir %{_libdir}/samba/gensec
%{_libdir}/samba/gensec/krb5.so
%{_libdir}/samba/libdlz-bind9-for-torture-samba4.so
%{_libdir}/samba/libpac-samba4.so

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
%{_libdir}/samba/ldb/instancetype.so
%{_libdir}/samba/ldb/lazy_commit.so
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
