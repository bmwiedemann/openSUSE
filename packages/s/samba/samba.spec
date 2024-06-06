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


%{!?py3_soflags:  %global py3_soflags cpython-%{python3_version_nodots}m}
%{!?py3_soflags_dash:   %global py3_soflags_dash %(echo %{py3_soflags} | sed "s/_/-/g")}

%{!?_fillupdir:%global _fillupdir /var/adm/fillup-templates}
%{!?_tmpfilesdir:%global _tmpfilesdir /usr/lib/tmpfiles.d}
%{!?_pam_moduledir:%global _pam_moduledir /%{_lib}/security}
%if 0%{?suse_version} > 1500
%{!?_pam_vendordir:%global _pam_vendordir %{_prefix}/lib/pam.d}
%global samba_pamdir %_pam_vendordir
%else
%{!?_pam_confdir:%global _pam_confdir %{_sysconfdir}/pam.d}
%global samba_pamdir %_pam_confdir
%endif
%{!?_pam_secconfdir:%global _pam_secconfdir %{_sysconfdir}/security}

%define with_mscat 1
%define build_ctdb_pmda 1

%ifarch aarch64 x86_64
%define build_ceph 1
%endif

%define talloc_version 2.4.2
%define tevent_version 0.16.1
%define tdb_version    1.4.10
%define ldb_version    2.9.0

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
%{!?with_mitkrb5: %define with_mitkrb5 1}
%{!?with_mit_dc: %define with_mit_dc 1}
# if factory/tw default with_dc to 1 (if not already defined in project config)
%if 0%{?suse_version} > 1500
%{!?with_dc: %define with_dc 1}
%else
%{!?with_dc: %define with_dc 0}
%endif

# Define whether smbd is built with SMB1 disabled
%{!?without_smb1_server: %define without_smb1_server 1}

Name:           samba
BuildRequires:  autoconf
BuildRequires:  cups-devel
BuildRequires:  cyrus-sasl-devel
BuildRequires:  e2fsprogs-devel
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  patch
BuildRequires:  perl-Parse-Yapp
BuildRequires:  libarchive-devel
BuildRequires:  libacl-devel
BuildRequires:  libattr-devel
BuildRequires:  libuuid-devel
BuildRequires:  cracklib-devel
BuildRequires:  gdbm-devel
BuildRequires:  keyutils-devel
BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  libnscd-devel
BuildRequires:  libopenssl-devel
BuildRequires:  zlib-devel
BuildRequires:  libtirpc-devel
BuildRequires:  ncurses-devel
BuildRequires:  openldap2-devel
BuildRequires:  pam-devel
BuildRequires:  popt-devel
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Markdown
BuildRequires:  python3-devel
BuildRequires:  python3-dnspython
BuildRequires:  python3-xml
BuildRequires:  readline-devel
BuildRequires:  rpcgen
BuildRequires:  fdupes
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
BuildRequires:  dbus-1-devel
BuildRequires:  libxslt-tools
BuildRequires:  libavahi-devel
# To only BuildRequire systemd-rpm-macros leads to broken binaries
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(systemd)
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
BuildRequires:  python3-gpg
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
BuildRequires:  perl-JSON
%endif
%if %{with_mscat}
BuildRequires:  libgnutls-devel >= 3.5.6
BuildRequires:  libtasn1-devel >= 3.8
%if 0%{?suse_version} > 1500
BuildRequires:  libtasn1-tools
%endif
%endif
# liburing not yet available for all Factory architectures
%ifnarch ppc armv6l armv7l
BuildRequires:  liburing-devel
%endif
BuildRequires:  sysuser-tools

Version:        4.20.1+git.339.cf6e153bb2
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
Requires:       /usr/bin/grep
Requires:       coreutils
Requires:       system-user-nobody
Requires:       %{fillup_prereq}
Requires:       samba-client >= %{version}
Requires:       sysuser-shadow
Provides:       group(ntadmin)

%{?systemd_ordering}
%sysusers_requires

# Define some global directories
################################
%define	DOCDIR %{_defaultdocdir}/samba
%define	DOCBOOKDIR %{_defaultdocdir}/samba/docbook
%define	LOGDIR %{_localstatedir}/log/samba
%define	LOCKDIR %{_localstatedir}/lib/samba
%define	CONFIGDIR %{_sysconfdir}/samba
%define	INITDIR %{_sysconfdir}/init.d
%define	PIDDIR /run/samba
%define	auth_modules auth_unix,auth_wbc,auth_server,auth_netlogond,auth_script,auth_samba4
%define	idmap_modules idmap_ad,idmap_adex,idmap_hash,idmap_ldap,idmap_rfc2307,idmap_rid,idmap_tdb2
%define	pdb_modules pdb_tdbsam,pdb_ldapsam,pdb_smbpasswd,pdb_samba_dsdb
%define	vfs_modules vfs_cacheprime,vfs_readahead
%define	VENDOR SUSE
%define cups_lib_dir %{_prefix}/lib/cups
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
BuildArch:      noarch

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
Provides:       group(winbind)
Requires:       pam-config
Recommends:     /usr/sbin/nscd
Recommends:     cron
Recommends:     logrotate
Requires:       coreutils
Requires:       samba-client = %{version}
Requires:       samba-winbind-libs = %{version}
Recommends:     samba-gpupdate = %{version}
Requires:       sysuser-shadow

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
BuildRequires:  systemd-rpm-macros
# bnc886095: The CTDB resource agent could be split out into a separate rpm,
# with corresponding ctdb and tdb-tools requirements. Until then, just add the
# tdb-tools requirement to ctdb.
Requires:       tdb-tools
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
%if %{with_mit_dc}
Requires:       python3-Markdown
%endif

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
Recommends:     python3-dnspython
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
# The ldb modules provided by this package check their own version matches
# the libldb2 version. It the version do not match (e.g. libldb2 version
# is updated and samba-dsdb-modules is not rebuilt against it) programs using
# libldb2 won't start. The requires_eq macro will require the libldb2 version
# available at build time without having to manually maintain the global
# ldb_version variable in this spec file (bsc#1118508, bsc#1199362)
%requires_eq libldb2
Requires:       samba-ldb-ldap = %{version}
Requires(post): /sbin/ldconfig
Requires(postun):/sbin/ldconfig

%description dsdb-modules
This package contains plugins which add Active Directory features to the
LDB library.

%prep
%setup -n samba-%{version} -q
# Create and add vendor suffix
if test "%{_project}" != "openSUSE:Factory"; then
	vendor_tag_release="%{release}"
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
export LDFLAGS="-ltirpc"
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
	--enable-avahi \
	--with-systemd \
	--with-systemddir=%{_unitdir} \
	--systemd-install-services \
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
%if 0%{?suse_version} > 1500
%if %{without_smb1_server}
	--without-smb1-server \
%endif
%endif
"

./configure ${CONFIGURE_OPTIONS}
make %{?_smp_mflags}

pushd docs-xml
autoconf && ./configure
XML_CATALOG_FILES="file:///etc/xml/catalog file://$(pwd)/build/catalog.xml" make htmlman
popd

pushd ctdb
XML_CATALOG_FILES="file:///etc/xml/catalog file://$(pwd)/build/catalog.xml" make %{?_smp_mflags} manpages
popd

%sysusers_generate_pre packaging/SuSE/systemd/sysusers.samba-winbind winbind samba-winbind.conf
%sysusers_generate_pre packaging/SuSE/systemd/sysusers.samba samba samba.conf

%install

install -d -m 0755 -p \
	%{buildroot}/%samba_pamdir

install -d -m 0755 -p \
	%{buildroot}/%{_sysconfdir}/{xinetd.d,logrotate.d} \
	%{buildroot}/%{_sysconfdir}/openldap/schema \
	%{buildroot}/%{_sysconfdir}/security \
	%{buildroot}/%{CONFIGDIR} \
	%{buildroot}/%{_unitdir} \
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

make %{?_smp_mflags} install \
	DESTDIR=%{buildroot} \
	CONFIGDIR=%{CONFIGDIR}

# debug symbols are created and installed if the files are excluded only
%if ! %{with_dc}
rm \
	%{buildroot}/%{_mandir}/man8/samba.8* \
	%{buildroot}/%{_mandir}/man8/samba_downgrade_db.8* \
	%{buildroot}/%{_unitdir}/samba-ad-dc.service
%endif

# CTDB
install -m 0644 packaging/SuSE/config/sysconfig.ctdb %{buildroot}/%{_fillupdir}
ln -s service %{buildroot}/%{_sbindir}/rcctdb
# create tmpfile conf
install -d -m 0755 %{buildroot}/%{_tmpfilesdir}
echo "d /run/ctdbd 0755 root root" >%{buildroot}/%{_tmpfilesdir}/ctdb.conf
mkdir %{buildroot}/%{_defaultdocdir}/ctdb
for file in README COPYING doc/examples doc/*.html doc/readonlyrecords.txt ; do
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
section_names=$( sed -ne 's/^\[\(.*\)\]$/\1/p' config/smb.conf)
for section in $section_names; do
	../source3/bin/testparm -s --section-name "${section}" config/smb.conf >"%{buildroot}/%{_datadir}/samba/templates/default-${section}" || :
done
for file in config/templates/*; do
	cp -a "${file}" "%{buildroot}/%{_datadir}/samba/templates/"
done
# start scripts
startScripts="smb nmb winbind"
for srv_name in ${startScripts}; do
	ln -s service %{buildroot}/%{_sbindir}/rc${srv_name}
done
%if %{with_dc}
	ln -s service %{buildroot}/%{_sbindir}/rcsamba-ad-dc
	install -m 0644 systemd/sysconfig.samba-ad-dc %{buildroot}%{_fillupdir}
	# Drop-in file for named to allow r/w access to dlz dir (bsc#1201689)
	install -d -m 0755 -p %{buildroot}%{_unitdir}/named.service.d
	install -m 0644 systemd/named-override.conf %{buildroot}%{_unitdir}/named.service.d/26-samba-dlz.conf
%endif
rm %{buildroot}/%{_sysconfdir}/sysconfig/samba
install -m 0644 systemd/sysconfig.samba %{buildroot}%{_fillupdir}
install -m 0644 systemd/sysconfig.samba-winbind %{buildroot}%{_fillupdir}
install -m 0644 -Dp systemd/sysusers.samba %{buildroot}%{_sysusersdir}/samba.conf
install -m 0644 -Dp systemd/sysusers.samba-winbind %{buildroot}%{_sysusersdir}/samba-winbind.conf
install -m 0644 -p ../systemd/samba.conf.tmp %{buildroot}/%{_tmpfilesdir}/samba.conf

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
install -m 0644 config/samba.pamd-common %{buildroot}/%samba_pamdir/samba
install -m 0644 config/dhcp.conf %{buildroot}/%{_fillupdir}/samba-client-dhcp.conf
install -m 0644 config/sysconfig.dhcp-samba-client %{buildroot}/%{_fillupdir}/sysconfig.dhcp-samba-client

# Add logrotate settings for nmbd and smbd only on systems newer than 8.1.
%if 0%{?suse_version} > 1500
mkdir -p %{buildroot}%{_distconfdir}/logrotate.d
%endif
LOGROTATE_FILES="samba samba-winbind"
for file in ${LOGROTATE_FILES}; do
	rm -f "%{_builddir}/samba-%{version}/filelist-${file}"
	touch "%{_builddir}/samba-%{version}/filelist-${file}"
%if 0%{?suse_version} > 1500
        install -m 0644 logrotate/${file} %{buildroot}/%{_distconfdir}/logrotate.d/${file}
        echo "%{_distconfdir}/logrotate.d/${file}" >>%{_builddir}/samba-%{version}/filelist-${file}
%else
        install -m 0644 logrotate/${file} %{buildroot}/%{_sysconfdir}/logrotate.d/${file}
	echo "%config(noreplace) %{_sysconfdir}/logrotate.d/${file}" >>%{_builddir}/samba-%{version}/filelist-${file}
%endif
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
# Hardlink duplicate files
%fdupes %{buildroot}

%pre -f samba.pre
%service_add_pre nmb.service smb.service samba-bgqd.service
%if 0%{?suse_version} > 1500
# Prepare for migration to /usr/etc; save any old .rpmsave
for i in logrotate.d/samba pam.d/samba; do
   test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i}.rpmsave.old ||:
done
%endif

%if 0%{?suse_version} > 1500
%posttrans
# Migration to /usr/etc, restore just created .rpmsave
for i in logrotate.d/samba pam.d/samba; do
   test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i} ||:
done
%endif

%if %{with_dc}
%pre ad-dc
%service_add_pre samba-ad-dc.service
%endif

%preun
%service_del_preun nmb.service smb.service samba-bgqd.service

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

%service_add_post nmb.service smb.service samba-bgqd.service
%tmpfiles_create samba.conf
%fillup_only

%postun
%service_del_postun nmb.service smb.service samba-bgqd.service

%post client
/sbin/ldconfig
for fn in MACHINE.SID idmap2.tdb idmap_test.tdb netlogon_creds_cli.tdb passdb.tdb secrets.tdb smbpasswd; do
	test ! -e %{LOCKDIR}/private/$fn && test -e %{CONFIGDIR}/$fn && \
		mv %{CONFIGDIR}/$fn %{LOCKDIR}/private/
done
for fn in brlock.tdb connections.tdb dbwrap_watchers.tdb gencache_notrans.tdb g_lock.tdb leases.tdb locking.tdb mutex.tdb names.tdb printer_list.tdb serverid.tdb smbXsrv_client_global.tdb smbXsrv_open_global.tdb smbXsrv_session_global.tdb smbXsrv_tcon_global.tdb smbXsrv_version_global.tdb srv_fss.tdb; do
	test ! -e %{LOCKDIR}/lock/$fn && test -e %{LOCKDIR}/$fn && \
		mv %{LOCKDIR}/$fn %{LOCKDIR}/lock/
done
if ! test -e %{_bindir}/get_printing_ticket; then
	ln -fs %{_bindir}/smbspool %{cups_lib_dir}/backend/smb
fi
%{?fillup_only:%{fillup_only -nsd dhcp samba-client network}}

%postun client
/sbin/ldconfig

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

%pre winbind -f winbind.pre
%service_add_pre winbind.service
%if 0%{?suse_version} > 1500
# Prepare for migration to /usr/etc; save any old .rpmsave
for i in logrotate.d/samba-winbind ; do
   test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i}.rpmsave.old ||:
done
%endif

%if 0%{?suse_version} > 1500
%posttrans winbind
# Migration to /usr/etc, restore just created .rpmsave
for i in logrotate.d/samba-winbind ; do
   test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i} ||:
done
%endif

%post winbind
/sbin/ldconfig
%service_add_post winbind.service
%tmpfiles_create samba.conf
%{fillup_only -ans samba winbind}

%preun winbind
%service_del_preun winbind.service

%postun winbind
/sbin/ldconfig
if [ $1 -eq 0 ]; then
%{_sbindir}/pam-config --delete --winbind
if [ -x %{_sbindir}/nscd ]; then
	%{_sbindir}/nscd -i passwd
	%{_sbindir}/nscd -i group
fi
fi
%service_del_postun winbind.service

%pre -n ctdb
%service_add_pre ctdb.service
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
%service_del_preun ctdb.service
exit 0

%post -n ctdb
%{fillup_only -n ctdb}
%service_add_post ctdb.service
%tmpfiles_create ctdb.conf

%postun -n ctdb
%service_del_postun ctdb.service
exit 0

%files -f filelist-samba
%defattr(-,root,root)
%{_unitdir}/nmb.service
%{_unitdir}/smb.service
%{_unitdir}/samba-bgqd.service
%ghost %{CONFIGDIR}/smbpasswd
%config(noreplace) %{CONFIGDIR}/smbusers
%if 0%{?suse_version} > 1500
%samba_pamdir/samba
%else
%config %samba_pamdir/samba
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
%{_libdir}/samba/rpcd_classic
%{_libdir}/samba/rpcd_epmapper
%{_libdir}/samba/rpcd_fsrvp
%{_libdir}/samba/rpcd_lsad
%{_libdir}/samba/rpcd_mdssvc
%{_libdir}/samba/rpcd_spoolss
%{_libdir}/samba/rpcd_winreg
%{_libdir}/samba/rpcd_witness
%{_libdir}/samba/samba-bgqd
%{_libdir}/samba/samba-dcerpcd
%attr(0644,root,root) %{_datadir}/omc/svcinfo.d/nmb.xml
%attr(0644,root,root) %{_datadir}/omc/svcinfo.d/smb.xml
%dir %{_datadir}/samba
%{_datadir}/samba/update-apparmor-samba-profile
%{_mandir}/man1/smbstatus.1.*
%{_mandir}/man1/wspsearch.1.*
%{_mandir}/man5/smbpasswd.5.*
%{_mandir}/man8/nmbd.8.*
%{_mandir}/man8/smbd.8.*
%{_mandir}/man8/samba-bgqd.8.*
%{_mandir}/man8/samba-dcerpcd.8.*
%{_fillupdir}/sysconfig.samba
%{_sysusersdir}/samba.conf

%files client
%defattr(-,root,root)
%dir %{CONFIGDIR}
%config(noreplace) %{CONFIGDIR}/lmhosts
%config(noreplace) %{CONFIGDIR}/smb.conf
%dir %{_sysconfdir}/openldap
%dir %{_sysconfdir}/openldap/schema
%attr(0444,root,root) %config %{_sysconfdir}/openldap/schema/samba3.schema
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
%{_bindir}/samba-log-parser
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
%{_bindir}/wspsearch
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
%{_mandir}/man1/samba-log-parser.1.*
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
%dir %{_tmpfilesdir}
%{_tmpfilesdir}/samba.conf
%if %{with_mscat}
%{_bindir}/dumpmscat
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
%_includedir/samba-4.0/gen_ndr/claims.h
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
%_includedir/samba-4.0/smb3posix.h
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
%{_libdir}/samba/libCHARSET3-private-samba.so
%{_libdir}/samba/libMESSAGING-private-samba.so
%{_libdir}/samba/libMESSAGING-SEND-private-samba.so
%{_libdir}/samba/libaddns-private-samba.so
%{_libdir}/samba/libads-private-samba.so
%{_libdir}/samba/libasn1util-private-samba.so
%{_libdir}/samba/libauth-private-samba.so
%if %{with_dc}
%{_libdir}/samba/libauthn-policy-util-private-samba.so
%endif
%{_libdir}/samba/libauthkrb5-private-samba.so
%{_libdir}/samba/libcli-cldap-private-samba.so
%{_libdir}/samba/libcli-ldap-private-samba.so
%{_libdir}/samba/libcli-ldap-common-private-samba.so
%{_libdir}/samba/libcli-nbt-private-samba.so
%{_libdir}/samba/libcli-smb-common-private-samba.so
%{_libdir}/samba/libcli-spoolss-private-samba.so
%{_libdir}/samba/libcliauth-private-samba.so
%{_libdir}/samba/libclidns-private-samba.so
%{_libdir}/samba/libcluster-private-samba.so
%{_libdir}/samba/libcmdline-contexts-private-samba.so
%{_libdir}/samba/libcmdline-private-samba.so
%{_libdir}/samba/libcommon-auth-private-samba.so
%{_libdir}/samba/libdbwrap-private-samba.so
%{_libdir}/samba/libdcerpc-pkt-auth-private-samba.so
%{_libdir}/samba/libdcerpc-samba-private-samba.so
%{_libdir}/samba/libdcerpc-samba4-private-samba.so
%{_libdir}/samba/libevents-private-samba.so
%{_libdir}/samba/libflag-mapping-private-samba.so
%{_libdir}/samba/libgenrand-private-samba.so
%{_libdir}/samba/libgensec-private-samba.so
%{_libdir}/samba/libgpo-private-samba.so
%{_libdir}/samba/libgse-private-samba.so
%{_libdir}/samba/libhttp-private-samba.so
%{_libdir}/samba/libinterfaces-private-samba.so
%{_libdir}/samba/libiov-buf-private-samba.so
%{_libdir}/samba/libkrb5samba-private-samba.so
%{_libdir}/samba/libldbsamba-private-samba.so
%{_libdir}/samba/liblibcli-lsa3-private-samba.so
%{_libdir}/samba/liblibcli-netlogon3-private-samba.so
%{_libdir}/samba/liblibsmb-private-samba.so
%{_libdir}/samba/libstable-sort-private-samba.so
%{_libdir}/libtevent-util.so.*
%{_libdir}/samba/libmessages-dgm-private-samba.so
%{_libdir}/samba/libmessages-util-private-samba.so
%{_libdir}/samba/libmsghdr-private-samba.so
%{_libdir}/samba/libmsrpc3-private-samba.so
%{_libdir}/samba/libndr-samba4-private-samba.so
%{_libdir}/samba/libndr-samba-private-samba.so
%{_libdir}/samba/libnet-keytab-private-samba.so
%{_libdir}/samba/libnetif-private-samba.so
%{_libdir}/samba/libnpa-tstream-private-samba.so
%{_libdir}/samba/libprinting-migrate-private-samba.so
%{_libdir}/samba/libregistry-private-samba.so
%{_libdir}/samba/libreplace-private-samba.so
%{_libdir}/samba/libsamba-cluster-support-private-samba.so
%{_libdir}/samba/libsamba-debug-private-samba.so
%{_libdir}/samba/libsamba-security-private-samba.so
%{_libdir}/samba/libsamba-sockets-private-samba.so
%{_libdir}/samba/libsamba3-util-private-samba.so
%{_libdir}/samba/libsamba-modules-private-samba.so
%{_libdir}/samba/libsamdb-common-private-samba.so
%{_libdir}/samba/libsmb-transport-private-samba.so
%{_libdir}/samba/libsmbclient-raw-private-samba.so
%{_libdir}/samba/libsmbd-base-private-samba.so
%{_libdir}/samba/libsmbd-shim-private-samba.so
%{_libdir}/samba/libsmbldaphelper-private-samba.so
%{_libdir}/samba/libsecrets3-private-samba.so
%{_libdir}/samba/libserver-id-db-private-samba.so
%{_libdir}/samba/libserver-role-private-samba.so
%{_libdir}/samba/libsocket-blocking-private-samba.so
%{_libdir}/samba/libsys-rw-private-samba.so
%{_libdir}/samba/libtalloc-report-printf-private-samba.so
%{_libdir}/samba/libtdb-wrap-private-samba.so
%{_libdir}/samba/libtime-basic-private-samba.so
%{_libdir}/samba/libtrusts-util-private-samba.so
%{_libdir}/samba/libutil-reg-private-samba.so
%{_libdir}/samba/libutil-setid-private-samba.so
%{_libdir}/samba/libutil-tdb-private-samba.so
%if %{with_mscat}
%{_libdir}/samba/libmscat-private-samba.so
%endif
%if %{with_dc}
%{_libdir}/samba/libdfs-server-ad-private-samba.so
%endif
%dir %{_libdir}/samba/pdb
%{_libdir}/samba/pdb/ldapsam.so
%{_libdir}/samba/pdb/smbpasswd.so
%{_libdir}/samba/pdb/tdbsam.so

%files libs
%defattr(-,root,root)
%{_libdir}/libdcerpc-samr.so.*
%dir %{_libdir}/samba
%{_libdir}/samba/libLIBWBCLIENT-OLD-private-samba.so
%{_libdir}/samba/libauth4-private-samba.so
%{_libdir}/samba/libauth-unix-token-private-samba.so
%{_libdir}/samba/libdnsserver-common-private-samba.so
%{_libdir}/samba/libgpext-private-samba.so
%{_libdir}/samba/libposix-eadb-private-samba.so
%{_libdir}/samba/libprinter-driver-private-samba.so
%{_libdir}/samba/libshares-private-samba.so
%{_libdir}/samba/libsmbpasswdparser-private-samba.so
%{_libdir}/samba/libtalloc-report-private-samba.so
%{_libdir}/samba/libtorture-private-samba.so
%{_libdir}/samba/libxattr-tdb-private-samba.so
%{_libdir}/samba/libcmocka-private-samba.so
%{_libdir}/samba/libREG-FULL-private-samba.so
%{_libdir}/samba/libRPC-SERVER-LOOP-private-samba.so
%{_libdir}/samba/libRPC-WORKER-private-samba.so
%{_libdir}/samba/libdsdb-module-private-samba.so
%if ! %{with_mitkrb5}
%{_libdir}/samba/libasn1-private-samba.so
%{_libdir}/samba/libcom-err-private-samba.so
%{_libdir}/samba/libgss-preauth-private-samba.so
%{_libdir}/samba/libgssapi-private-samba.so
%{_libdir}/samba/libhcrypto-private-samba.so
%{_libdir}/samba/libhdb-private-samba.so
%{_libdir}/samba/libheimbase-private-samba.so
%{_libdir}/samba/libheimntlm-private-samba.so
%{_libdir}/samba/libhx509-private-samba.so
%{_libdir}/samba/libkdc-private-samba.so
%{_libdir}/samba/libkrb5-private-samba.so
%{_libdir}/samba/libroken-private-samba.so
%{_libdir}/samba/libwind-private-samba.so
%endif

%files libs-python3
%{_libdir}/samba/libsamba-net.%{py3_soflags_dash}-private-samba.so
%{_libdir}/samba/libsamba-python.%{py3_soflags_dash}-private-samba.so

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
%{_bindir}/mdsearch
%{_mandir}/man1/gentest.1.*
%{_mandir}/man1/locktest.1.*
%{_mandir}/man1/masktest.1.*
%{_mandir}/man1/ndrdump.1.*
%{_mandir}/man1/mdsearch.1.*

%files winbind-libs
%defattr(-,root,root)
%{_pam_moduledir}/pam_winbind.so
%{_libdir}/libnss_winbind.so.*
%{_libdir}/samba/libidmap-private-samba.so
%{_libdir}/samba/libnss-info-private-samba.so
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
%{_unitdir}/winbind.service
%{_sysusersdir}/samba-winbind.conf
%{_bindir}/ntlm_auth
%{_bindir}/wbinfo
%{_sbindir}/rcwinbind
%{_sbindir}/winbindd
%{_mandir}/man1/ntlm_auth.1.*
%{_mandir}/man1/wbinfo.1.*
%{_mandir}/man8/winbindd.8.*
%attr(0644,root,root) %{_datadir}/omc/svcinfo.d/winbind.xml
%attr(0750,root,winbind) %dir %{LOCKDIR}/winbindd_privileged
%{_fillupdir}/sysconfig.samba-winbind
%attr(0770,root,root) %{_var}/cache/krb5rcache

%files doc -f filelist-samba-doc
%defattr(-,root,root)
%dir %{DOCDIR}
%doc %{_datadir}/susehelp

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
%attr(644,root,root) %{_unitdir}/ctdb.service
%dir %{_tmpfilesdir}
%{_tmpfilesdir}/ctdb.conf
%ghost %dir /run/ctdbd
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
%{_sbindir}/rcctdb
%{_bindir}/ctdb
%{_bindir}/ctdb_diagnostics
%{_bindir}/ltdbtool
%{_bindir}/onnode
%{_bindir}/ping_pong
%dir %{_libdir}/ctdb
%{_libdir}/ctdb/ctdb-config
%{_libdir}/samba/libctdb-event-client-private-samba.so
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
%ghost %dir /run/ctdb
%{_mandir}/man1/ctdb.1.gz
%{_mandir}/man1/ctdbd.1.gz
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
%dir %{_unitdir}/named.service.d
%{_unitdir}/named.service.d/26-samba-dlz.conf
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
%{_datadir}/samba/setup/ad-schema/AD_DS_Attributes__Windows_Server_v1803.ldf
%{_datadir}/samba/setup/ad-schema/AD_DS_Attributes_Windows_Server_v1903.ldf
%{_datadir}/samba/setup/ad-schema/AD_DS_Classes__Windows_Server_2012_R2.ldf
%{_datadir}/samba/setup/ad-schema/AD_DS_Classes__Windows_Server_2016.ldf
%{_datadir}/samba/setup/ad-schema/AD_DS_Classes__Windows_Server_v1803.ldf
%{_datadir}/samba/setup/ad-schema/AD_DS_Classes_Windows_Server_v1903.ldf
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
%{_datadir}/samba/admx/GNOME_Settings.admx
%dir %{_datadir}/samba/admx/en-US
%{_datadir}/samba/admx/en-US/samba.adml
%{_datadir}/samba/admx/en-US/GNOME_Settings.adml
%dir %{_datadir}/samba/admx/ru-RU
%{_datadir}/samba/admx/ru-RU/GNOME_Settings.adml
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
%{_libdir}/samba/libad-claims-private-samba.so
%{_libdir}/samba/libdb-glue-private-samba.so
%{_libdir}/samba/libdsdb-garbage-collect-tombstones-private-samba.so
%{_libdir}/samba/libscavenge-dns-records-private-samba.so
%{_libdir}/samba/libprocess-model-private-samba.so
%{_libdir}/samba/libservice-private-samba.so
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
%{_libdir}/samba/pdb/samba_dsdb.so
%if %{with_mit_dc}
%{_libdir}/krb5/plugins/kdb/samba.so
%else
%{_libdir}/samba/libHDB-SAMBA4-private-samba.so
%endif
%dir %{_libdir}/samba/bind9
%{_libdir}/samba/bind9/dlz_bind9_10.so
%{_libdir}/samba/bind9/dlz_bind9_11.so
%{_libdir}/samba/bind9/dlz_bind9_12.so
%{_libdir}/samba/bind9/dlz_bind9_14.so
%{_libdir}/samba/bind9/dlz_bind9_16.so
%{_libdir}/samba/bind9/dlz_bind9_18.so
%dir %{_libdir}/samba/gensec
%{_libdir}/samba/gensec/krb5.so
%{_libdir}/samba/libdlz-bind9-for-torture-private-samba.so
%{_libdir}/samba/libpac-private-samba.so

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
