#
# spec file for package tog-pegasus
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


%if 0%{?suse_version} > 1140 || 0%{?fedora_version} > 14
%define has_systemd 1
%else
%define has_systemd 0
%endif

%{?!PEGASUS_BUILD_TEST_RPM:     %global PEGASUS_BUILD_TEST_RPM        1}
# do "rpmbuild --define 'PEGASUS_BUILD_TEST_RPM 1'" to build test RPM.

%global srcname pegasus
%global major_ver 2.14
%global pegasus_gid 65
%global pegasus_uid 66

%if 0%{?suse_version} > 1310
%define rundir /run
%else
%define rundir /var/run
%endif

Name:           tog-pegasus
Version:        %{major_ver}.1
Release:        0
%if 0%{?suse_version}
%else
%endif
Summary:        OpenPegasus WBEM Services for Linux
License:        MIT
Group:          System/Daemons

URL:            http://www.openpegasus.org
Source0:        https://collaboration.opengroup.org/pegasus/documents/32572/pegasus-%{version}.tar.gz
#  1: Description of security enhacements
Source1:        README.SUSE.Security
#  2: Description of SUSE setup
Source2:        README.SUSE
#  3: Description of SSL settings
Source3:        README.SUSE.SSL
#  4: /etc/tmpfiles.d configuration file
Source4:        tog-pegasus.tmpfiles
#  5: systemd service file for RedHat/Fedora
Source5:        tog-pegasus.service
#  6: This file controls access to the Pegasus services by users with the PAM pam_access module
Source6:        access.conf
#  7: Simple Redhat/Fedora wrapper for Pegasus's cimprovagt - because of confining providers in SELinux 
Source7:        cimprovagt-wrapper.sh
#  8: Example wrapper confining Operating System Provider from sblim-cmpi-base package
Source8:        cmpiOSBase_OperatingSystemProvider-cimprovagt.example
#  9: DMTF CIM schema
Source9:        cim_schema_2.38.0Experimental-MOFs.zip
# 10: Fedora/RHEL script for adding self-signed certificates to the local CA
#     trust store
Source10:       generate-certs
# 11: SUSE script for adding self-signed certificates to the local CA
#     trust store
Source11:       generate-certs.SUSE
# 12: systemd service file for SUSE (> 1310)
Source12:       tog-pegasus.service.SUSE
# 13: Simple SUSE wrapper for Pegasus's cimprovagt - because of confining providers in SELinux 
Source13:       cimprovagt-wrapper.sh.SUSE

#  1: http://cvs.rdg.opengroup.org/bugzilla/show_bug.cgi?id=5011
#     Removing insecure -rpath
Patch1:         pegasus-2.9.0-no-rpath.patch
#  2: Adding -fPIE
Patch2:         pegasus-2.7.0-PIE.patch
#  3: http://cvs.rdg.opengroup.org/bugzilla/show_bug.cgi?id=5016
#     Configuration variables
Patch3:         pegasus-2.9.0-redhat-config.patch
#  4: don't see how http://cvs.rdg.opengroup.org/bugzilla/show_bug.cgi?id=5099 fixed it
#     Changing provider dir to the directory we use
Patch4:         pegasus-2.9.0-cmpi-provider-lib.patch
#  5: http://cvs.rdg.opengroup.org/bugzilla/show_bug.cgi?id=5010
#     We distinguish between local and remote user and behave adequately (will be upstream once)
Patch5:         pegasus-2.9.0-local-or-remote-auth.patch
#  6: http://cvs.rdg.opengroup.org/bugzilla/show_bug.cgi?id=5012
#     Modifies pam rules to use access cofiguration file and local/remote differences
Patch61:        pegasus-SUSE-pam-wbem.patch
Patch62:        pegasus-2.5.1-pam-wbem.patch
#  9: Adds cimuser binary to admin commands
Patch9:         pegasus-2.6.0-cimuser.patch
# 12: Removes snmp tests, which we don't want to perform
Patch12:        pegasus-2.7.0-no_snmp_tests.patch
# 13: Changes to make package compile on sparc
Patch13:        pegasus-2.9.0-sparc.patch
# 16: Fixes "getpagesize" build error
Patch16:        pegasus-2.9.1-getpagesize.patch
# 19: Don't strip binaries, add -g flag
Patch19:        pegasus-2.10.0-dont-strip.patch
# 20: use posix locks on sparc arches
Patch20:        pegasus-2.10.0-sparc-posix-lock.patch
# 22: Fix CMPI enumGetNext function to change CMPI Data state from default CMPI_nullValue
#     to CMPI_goodValue when it finds and returns next instance correctly
Patch22:        pegasus-2.12.0-null_value.patch
# 24: bz#883030, getPropertyAt() returns Null instead of empty array
Patch24:        pegasus-2.12.0-empty_arrays.patch
# 25: allow experimental schema registration with cimmofl during build
Patch25:        pegasus-2.12.0-cimmofl-allow-experimental.patch
# 26: use external schema and add missing includes there
Patch26:        pegasus-2.12.0-schema-version-and-includes.patch
# 29: bz#1049314, allow unprivileged users to subscribe to indications by default
Patch29:        pegasus-2.13.0-enable-subscriptions-for-nonprivileged-users.patch
# 33: fixes build with gcc5
Patch33:        pegasus-2.13.0-gcc5-build.patch
# 34: fixes various build problemss
Patch34:        pegasus-2.14.1-build-fixes.patch
# 35: fixes compiler warnings
Patch35:        pegasus-2.14.1-fix-compiler-warnings.patch
# 36: 'STACK_OF' undefined
Patch36:        pegasus-2.14.1-openssl.patch
# 37: OpenSSL 1.1 changes
Patch37:        pegasus-2.14.1-openssl-1.1.patch

BuildRequires:  bash
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  grep
BuildRequires:  openssl
BuildRequires:  openssl-devel
BuildRequires:  pam-devel
BuildRequires:  procps
BuildRequires:  procps
BuildRequires:  sed
%if 0%{?suse_version}
BuildRequires:  cim-schema
BuildRequires:  unzip
%if 0%{?suse_version} > 1010
BuildRequires:  fdupes
%endif
%else
BuildRequires:  libstdc++
%endif
BuildRequires:  make
BuildRequires:  net-snmp-devel
BuildRequires:  openslp-devel
BuildRequires:  openssl-devel
BuildRequires:  pam-devel
%if 0%{?has_systemd}
BuildRequires:  pkgconfig(systemd)
%if 0%{?suse_version}
%{?systemd_ordering}
%else
BuildRequires:  systemd-units
Requires:       net-snmp-libs
%endif
%endif
%if 0%{?suse_version}
Requires:       %{name}-libs = %{version}-%{release}
%else
Requires:       %{name}-libs = %{version}-%{release}
%endif
Requires:       openssl
%if 0%{?suse_version} > 1130
Requires:       ca-certificates
BuildRequires:  ca-certificates
# for restorecon(8)
BuildRequires:  policycoreutils
Requires:       policycoreutils
%endif
Provides:       cim-server = 1
Requires(post): /sbin/ldconfig
%if 0%{?suse_version}
Requires(post):  /usr/sbin/groupadd
%endif

%description
OpenPegasus WBEM Services for Linux enables management solutions that deliver
increased control of enterprise resources. WBEM is a platform and resource
independent DMTF standard that defines a common information model and
communication protocol for monitoring and controlling resources from diverse
sources.

%package devel
Summary:        The OpenPegasus Software Development Kit
Group:          Development/Tools
%if 0%{?suse_version}
Requires:       libpegclient1
Requires:       libpegcommon1
Requires:       libpegexportserver1
Requires:       libpeglistener1
Requires:       tog-pegasus-libs = %{version}-%{release}
%else
Requires:       tog-pegasus >= %{version}-%{release}
%endif
Provides:       tog-pegasus-sdk = %{version}
Obsoletes:      tog-pegasus-sdk < %{version}
%if 0%{?suse_version}
Provides:       tog-pegasus-devel-internal
# because of /usr/lib64/libcmpiCppImpl.so
Conflicts:      sblim-cmpi-c++-devel
%endif

%description devel
The OpenPegasus WBEM Services for Linux SDK is the developer's kit for the
OpenPegasus WBEM Services for Linux release. It provides Linux C++ developers
with the WBEM files required to build WBEM Clients and Providers. It also
supports C provider developers via the CMPI interface.

%package libs
Summary:        The OpenPegasus Libraries
# because of /usr/lib64/libcmpiCppImpl.so.*
Group:          System/Libraries
Conflicts:      libcmpiCppImpl0
Requires(pre):  /usr/sbin/useradd
Requires(pre):  /usr/sbin/groupadd
Requires(post): /sbin/ldconfig

%description libs
The OpenPegasus libraries.

%if %{PEGASUS_BUILD_TEST_RPM}
%package test
Summary:        The OpenPegasus Tests
Group:          Development/Debug
Requires:       tog-pegasus >= %{version}-%{release}, make

%description test
The OpenPegasus WBEM tests for the OpenPegasus %{version} Linux rpm.
%endif

%if 0%{?suse_version}
%package -n libpegclient1
Summary:        Client library for tog-pegasus
Group:          System/Libraries

%description -n libpegclient1
This is a dependency of tog-pegasus and other associated packages.

%package -n libpegcommon1
Summary:        Common library for tog-pegasus
Group:          System/Libraries

%description -n libpegcommon1
This is a dependency of tog-pegasus and other associated packages.

%package -n libpeglistener1
Summary:        Listener library for tog-pegasus
Group:          System/Libraries

%description -n libpeglistener1
This is a dependency of tog-pegasus and other associated packages.

%package -n libpegexportserver1
Summary:        Exportserver library for tog-pegasus
Group:          System/Libraries

%description -n libpegexportserver1
This is a dependency of tog-pegasus and other associated packages.

%endif

%ifarch ia64
%global PEGASUS_HARDWARE_PLATFORM LINUX_IA64_GNU
%endif
%ifarch x86_64
%global PEGASUS_HARDWARE_PLATFORM LINUX_X86_64_GNU
%endif
%ifarch ppc
%global PEGASUS_HARDWARE_PLATFORM LINUX_PPC_GNU
%endif
%ifarch ppc64
%global PEGASUS_HARDWARE_PLATFORM LINUX_PPC64_GNU
%endif
%ifarch ppc64le
%global PEGASUS_HARDWARE_PLATFORM LINUX_PPC64_GNU
%endif
%ifarch s390
%global PEGASUS_HARDWARE_PLATFORM LINUX_ZSERIES_GNU
%endif
%ifarch s390x
%global PEGASUS_HARDWARE_PLATFORM LINUX_ZSERIES64_GNU
%endif
%ifarch sparcv9
%global PEGASUS_HARDWARE_PLATFORM LINUX_SPARCV9_GNU
%endif
%ifarch sparc64
%global PEGASUS_HARDWARE_PLATFORM LINUX_SPARC64_GNU
%endif
%ifarch %{ix86}
%global PEGASUS_HARDWARE_PLATFORM LINUX_IX86_GNU
%endif
%ifarch %{arm}
%global PEGASUS_HARDWARE_PLATFORM LINUX_XSCALE_GNU
%endif
%ifarch aarch64
%global PEGASUS_HARDWARE_PLATFORM LINUX_AARCH64_GNU
%endif

%global PEGASUS_ARCH_LIB %{_lib}
%global OPENSSL_HOME /usr
%global OPENSSL_BIN /usr/bin
%global PEGASUS_PEM_DIR /etc/Pegasus
%global PEGASUS_SSL_CERT_FILE server.pem
%global PEGASUS_SSL_KEY_FILE file.pem
%global PEGASUS_SSL_TRUSTSTORE client.pem
%global PAM_CONFIG_DIR /etc/pam.d
%global PEGASUS_CONFIG_DIR /etc/Pegasus
%global PEGASUS_VARDATA_DIR /var/lib/Pegasus
%global PEGASUS_VARDATA_CACHE_DIR /var/lib/Pegasus/cache
%global PEGASUS_LOCAL_DOMAIN_SOCKET_PATH %{rundir}/tog-pegasus/socket/cimxml.socket
%global PEGASUS_CIMSERVER_START_FILE %{rundir}/tog-pegasus/cimserver.pid
%global PEGASUS_TRACE_FILE_PATH /var/lib/Pegasus/cache/trace/cimserver.trc
%global PEGASUS_CIMSERVER_START_LOCK_FILE %{rundir}/tog-pegasus/cimserver_start.lock
%global PEGASUS_REPOSITORY_DIR /var/lib/Pegasus/repository
%global PEGASUS_PREV_REPOSITORY_DIR_NAME prev_repository
%global PEGASUS_REPOSITORY_PARENT_DIR /var/lib/Pegasus
%global PEGASUS_PREV_REPOSITORY_DIR /var/lib/PegasusXXX/prev_repository
%global PEGASUS_SBIN_DIR /usr/sbin
%global PEGASUS_DOC_DIR /usr/share/doc/%{name}-%{version}

%global PEGASUS_RPM_ROOT "%{_builddir}/%{srcname}"
%global PEGASUS_RPM_HOME %PEGASUS_RPM_ROOT/build
%global PEGASUS_INSTALL_LOG /var/lib/Pegasus/log/install.log

%prep
%setup -q -n %{srcname}
# convert DMTF schema for Pegasus
export PEGASUS_ROOT=%PEGASUS_RPM_ROOT
yes | mak/CreateDmtfSchema 238 %{SOURCE9} cim_schema_2.38.0
%patch1 -p1 -b .no-rpath
%patch2 -p1 -b .PIE
%patch3 -p1 -b .redhat-config
%patch4 -p1 -b .cmpi-provider-lib

%if 0%{?suse_version}
%patch61 -p1 -b .pam-wbem
%else
%patch62 -p1 -b .pam-wbem
%endif

%patch9 -p1 -b .cimuser
%patch12 -p1 -b .no_snmp_tests
%patch5 -p1 -b .local-or-remote-auth
%patch13 -p1 -b .sparc
%patch16 -p1 -b .getpagesize
%patch19 -p1 -b .dont-strip
%patch20 -p1 -b .sparc-locks
%patch22 -p1 -b .null_value
%patch24 -p1 -b .empty_arrays
%patch25 -p1 -b .cimmofl-allow-experimental
%patch26 -p1 -b .schema-version-and-includes
%patch29 -p1 -b .enable-subscriptions-for-nonprivileged-users
%patch33 -p1 -b .gcc5-build
%patch34 -p1 -b .build-fixes
%patch35 -p1 -b .compiler-warnings
%patch36 -p1 -b .openssl
%patch37 -p1 -b .openssl1.1

%build
cp -fp %SOURCE1 doc
cp -fp %SOURCE3 doc
cp -fp %SOURCE6 rpm
cp -fp %SOURCE8 doc

export PEGASUS_ROOT=%PEGASUS_RPM_ROOT
export PEGASUS_HOME=%PEGASUS_RPM_HOME
export PEGASUS_PLATFORM=%PEGASUS_HARDWARE_PLATFORM
export PEGASUS_ARCH_LIB=%PEGASUS_ARCH_LIB
export PEGASUS_ENVVAR_FILE=$PEGASUS_ROOT/env_var_Linux.status

export OPENSSL_HOME=%OPENSSL_HOME
export OPENSSL_BIN=%OPENSSL_BIN
export LD_LIBRARY_PATH=$PEGASUS_HOME/lib
export PATH=$PEGASUS_HOME/bin:$PATH

export PEGASUS_EXTRA_C_FLAGS="%{optflags} -fPIC -g -Wall -Wno-unused -fno-strict-aliasing"
export PEGASUS_EXTRA_CXX_FLAGS="$PEGASUS_EXTRA_C_FLAGS"
export PEGASUS_EXTRA_LINK_FLAGS="%{optflags}"
export PEGASUS_EXTRA_PROGRAM_LINK_FLAGS="-g -pie -Wl,-z,relro,-z,now,-z,nodlopen,-z,noexecstack"
export SYS_INCLUDES=-I/usr/kerberos/include

make %{?_smp_mflags} -f ${PEGASUS_ROOT}/Makefile.Release create_ProductVersionFile
make %{?_smp_mflags} -f ${PEGASUS_ROOT}/Makefile.Release create_CommonProductDirectoriesInclude
make %{?_smp_mflags} -f ${PEGASUS_ROOT}/Makefile.Release create_ConfigProductDirectoriesInclude
make %{?_smp_mflags} -f ${PEGASUS_ROOT}/Makefile.Release all
make %{?_smp_mflags} -f ${PEGASUS_ROOT}/Makefile.Release repository

%install
export PEGASUS_ROOT=%PEGASUS_RPM_ROOT
export PEGASUS_HOME=%PEGASUS_RPM_HOME
export PEGASUS_PLATFORM=%PEGASUS_HARDWARE_PLATFORM
export PEGASUS_ARCH_LIB=%PEGASUS_ARCH_LIB
export PEGASUS_ENVVAR_FILE=$PEGASUS_ROOT/env_var_Linux.status

export OPENSSL_BIN=%OPENSSL_BIN
export LD_LIBRARY_PATH=$PEGASUS_HOME/lib
export PATH=$PEGASUS_HOME/bin:$PATH

export PEGASUS_STAGING_DIR="%{buildroot}"
%if %{PEGASUS_BUILD_TEST_RPM}
make -f $PEGASUS_ROOT/Makefile.Release stage \
    PEGASUS_STAGING_DIR=$PEGASUS_STAGING_DIR \
    PEGASUS_BUILD_TEST_RPM=%{PEGASUS_BUILD_TEST_RPM}
%else
make -f $PEGASUS_ROOT/Makefile.Release stage \
    PEGASUS_STAGING_DIR=$PEGASUS_STAGING_DIR
%endif

mkdir -p "%{buildroot}/%{_tmpfilesdir}"
install -p -D -m 644 %{SOURCE4} "%{buildroot}/%{_tmpfilesdir}/tog-pegasus.conf"

# Install script to generate SSL certificates at startup
mkdir -p "%{buildroot}/%{_datadir}/Pegasus/scripts"
%if 0%{?suse_version}
install -p -m 755 %{SOURCE11} "%{buildroot}/%{_datadir}/Pegasus/scripts/generate-certs"
%else
install -p -m 755 %{SOURCE10} "%{buildroot}/%{_datadir}/Pegasus/scripts/generate-certs"
%endif

# remove SysV initscript, install .service file
rm -f "%{buildroot}/etc/init.d/tog-pegasus"
mkdir -p "%{buildroot}/%{_unitdir}"
%if 0%{?suse_version} > 1310
install -p -m 644 %{SOURCE12} "%{buildroot}/%{_unitdir}/%{name}.service"
%else
install -p -m 644 %{SOURCE5} "%{buildroot}/%{_unitdir}/tog-pegasus.service"
%endif
# cimserver_planned.conf is on the right place since 2.9.2 (update - not in 2.10.0)
#mv "%{buildroot}/var/lib/Pegasus/cimserver_planned.conf" "%{buildroot}/etc/Pegasus/cimserver_planned.conf"
mkdir -p "%{buildroot}/%{_docdir}/%{name}"
mv "%{buildroot}/%{_datadir}/doc/%{name}-%{major_ver}"/* "%{buildroot}/%{_docdir}/%{name}"
rm -rf "%{buildroot}/%{_datadir}/doc/%{name}-%{major_ver}"
# create symlink for libcmpiCppImpl
pushd "%{buildroot}/%{_libdir}"
ln -s libcmpiCppImpl.so.1 libcmpiCppImpl.so
# and libpeglistener
ln -s libpeglistener.so.1 libpeglistener.so
popd
mkdir -p "%{buildroot}/%{_libexecdir}/pegasus"
mv "%{buildroot}/%{_sbindir}/cimprovagt" "%{buildroot}/%{_libexecdir}/pegasus"
%if 0%{?suse_version}
install -p -m 0755 %{SOURCE13} "%{buildroot}/%{_sbindir}/cimprovagt"
%else
install -p -m 0755 %{SOURCE7} "%{buildroot}/%{_sbindir}/cimprovagt"
%endif
# install Platform_LINUX_XSCALE_GNU.h because of lmiwbem on arm
install -m 644 src/Pegasus/Common/Platform_LINUX_XSCALE_GNU.h "%{buildroot}/%{_includedir}/Pegasus/Common"
# install UintArgs.h because of cimple
install -m 644 src/Pegasus/Common/UintArgs.h "%{buildroot}/%{_includedir}/Pegasus/Common"
# install CIMEnumerationContext.h because of cimple
install -m 644 src/Pegasus/Client/CIMEnumerationContext.h "%{buildroot}/%{_includedir}/Pegasus/Client"
# install Linkage.h and CIMListener.h because of lmiwbem (CIMListener class)
mkdir -p "%{buildroot}/%{_includedir}/Pegasus/Listener"
install -m 644 src/Pegasus/Listener/Linkage.h "%{buildroot}/%{_includedir}/Pegasus/Listener"
install -m 644 src/Pegasus/Listener/CIMListener.h "%{buildroot}/%{_includedir}/Pegasus/Listener"
%if 0%{?suse_version}
# install files because of cimple (brevity and cimple-pegasus-adapter)
install -m 644 src/Pegasus/Common/ArrayImpl.h "%{buildroot}/%{_includedir}/Pegasus/Common"
install -m 644 src/Pegasus/Common/ArrayInternal.h "%{buildroot}/%{_includedir}/Pegasus/Common"
install -m 644 src/Pegasus/Common/ArrayRep.h "%{buildroot}/%{_includedir}/Pegasus/Common"
install -m 644 src/Pegasus/Common/AtomicInt.h "%{buildroot}/%{_includedir}/Pegasus/Common"
install -m 644 src/Pegasus/Common/Buffer.h "%{buildroot}/%{_includedir}/Pegasus/Common"
install -m 644 src/Pegasus/Common/CommonUTF.h "%{buildroot}/%{_includedir}/Pegasus/Common"
install -m 644 src/Pegasus/Common/InternalException.h "%{buildroot}/%{_includedir}/Pegasus/Common"
install -m 644 src/Pegasus/Common/Linkable.h "%{buildroot}/%{_includedir}/Pegasus/Common"
install -m 644 src/Pegasus/Common/Magic.h "%{buildroot}/%{_includedir}/Pegasus/Common"
install -m 644 src/Pegasus/Common/Memory.h "%{buildroot}/%{_includedir}/Pegasus/Common"
install -m 644 src/Pegasus/Common/Message.h "%{buildroot}/%{_includedir}/Pegasus/Common"
install -m 644 src/Pegasus/Common/Mutex.h "%{buildroot}/%{_includedir}/Pegasus/Common"
install -m 644 src/Pegasus/Common/PegasusAssert.h "%{buildroot}/%{_includedir}/Pegasus/Common"
install -m 644 src/Pegasus/Common/Stack.h "%{buildroot}/%{_includedir}/Pegasus/Common"
install -m 644 src/Pegasus/Common/StringConversion.h "%{buildroot}/%{_includedir}/Pegasus/Common"
install -m 644 src/Pegasus/Common/StrLit.h "%{buildroot}/%{_includedir}/Pegasus/Common"
install -m 644 src/Pegasus/Common/Threads.h "%{buildroot}/%{_includedir}/Pegasus/Common"
install -m 644 src/Pegasus/Common/XmlGenerator.h "%{buildroot}/%{_includedir}/Pegasus/Common"
install -m 644 src/Pegasus/Common/XmlParser.h "%{buildroot}/%{_includedir}/Pegasus/Common"
install -m 644 src/Pegasus/Common/XmlWriter.h "%{buildroot}/%{_includedir}/Pegasus/Common"
%endif

%if 0%{?suse_version}
# Fedora does this in %post :-/

# Create Symbolic Links for SDK Libraries
#
pushd "%{buildroot}/%{_libdir}"
ln -sf libpegclient.so.1 libpegclient.so
ln -sf libpegcommon.so.1 libpegcommon.so
ln -sf libpegprovider.so.1 libpegprovider.so
ln -sf libpegconfig.so.1 libpegconfig.so
ln -sf libpegprm.so.1 libpegprm.so
ln -sf libpegprovidermanager.so.1 libpegprovidermanager.so
ln -sf libDefaultProviderManager.so.1 libDefaultProviderManager.so
ln -sf libCIMxmlIndicationHandler.so.1 libCIMxmlIndicationHandler.so
ln -sf libsnmpIndicationHandler.so.1 libsnmpIndicationHandler.so
popd

# Create Symbolic Links for Packaged Provider Libraries
#
pushd "%{buildroot}/%{_libdir}/Pegasus/providers"
ln -sf libComputerSystemProvider.so.1 libComputerSystemProvider.so
ln -sf libOSProvider.so.1 libOSProvider.so
ln -sf libProcessProvider.so.1 libProcessProvider.so
popd

# Create Symbolic Links for Packaged Provider Managers
#
pushd "%{buildroot}/%{_libdir}/Pegasus/providerManagers/"
ln -sf libCMPIProviderManager.so.1 libCMPIProviderManager.so
popd

# no binaries below /usr/share
mv "%{buildroot}/%{_datadir}/Pegasus/test" "%{buildroot}/%{_libdir}/Pegasus"
%if 0%{?suse_version} > 1010
%fdupes -s %{buildroot}/%{_bindir}
%fdupes -s %{buildroot}/var/lib/Pegasus
%endif
ln -sf %{_sbindir}/service "%{buildroot}/%{_sbindir}/rc%{name}"
%endif

%check
# run unit tests
export LD_LIBRARY_PATH="%{buildroot}/%{_libdir}"
%if 0%{?suse_version}
cd "%{buildroot}/%{_libdir}/Pegasus/test"
%else
cd "%{buildroot}/%{_datadir}/Pegasus/test"
%endif
make prestarttests
# strip time and PID from logs to create reproducible results
perl -i -pe 's/^\d{10,}s-\d{1,6}us: //; s/ \[\d+:\d{10,}:/ [/' *.trace.0

%files
%defattr(0640, root, pegasus, 0750)
%verify(not md5 size mtime mode group) /var/lib/Pegasus/repository
%defattr(0644, root, pegasus, 0755)
/usr/share/Pegasus/mof
%dir /usr/share/Pegasus
%defattr(0755, root, pegasus, 0750)
/usr/share/Pegasus/scripts
%defattr(0640, root, pegasus, 0750)
%dir /var/lib/Pegasus
/var/lib/Pegasus/cache
%if 0%{?suse_version}
/var/lib/Pegasus/repository
%endif
%dir /var/lib/Pegasus/log
%defattr(0640, root, pegasus, 0750)
%dir /etc/Pegasus
%{_tmpfilesdir}/tog-pegasus.conf
%if 0%{?suse_version} == 0
%ghost %dir %{rundir}/%{name}
%ghost %attr(0640, root, pegasus) %{rundir}/%{name}/cimserver.pid
%ghost %attr(0640, root, pegasus) %{rundir}/%{name}/cimserver_start.lock
%ghost %attr(1640,root,pegasus) %{rundir}/%{name}/cimxml.socket
%endif
%attr(0644, root, pegasus) %{_unitdir}/tog-pegasus.service
%defattr(0640, root, pegasus, 0750)
%ghost %attr(0640, root, pegasus) %config(noreplace) /etc/Pegasus/cimserver_current.conf
%ghost %config(noreplace) /etc/Pegasus/cimserver_planned.conf
%config(noreplace) /etc/Pegasus/access.conf
%config(noreplace) /etc/pam.d/wbem
%ghost /etc/Pegasus/ssl.cnf
%ghost /etc/Pegasus/client.pem
%ghost /etc/Pegasus/server.pem
%ghost /etc/Pegasus/file.pem
%ghost /etc/Pegasus/ca.crt
%ghost /etc/Pegasus/ca.srl
%ghost /etc/Pegasus/client.srl
%ghost /etc/Pegasus/ssl-ca.cnf
%ghost /etc/Pegasus/ssl-service.cnf
%if 0%{?suse_version}
%ghost /etc/pki/trust/anchors/localhost-pegasus.pem
%else
%ghost /etc/pki/ca-trust/source/anchors/localhost-pegasus.pem
%endif
%ghost %attr(0640, root, pegasus) /etc/Pegasus/cimserver_trust
%ghost %attr(0640, root, pegasus) /etc/Pegasus/indication_trust
%ghost %attr(0640, root, pegasus) /etc/Pegasus/crl
%ghost %verify(not md5 size mtime) /var/lib/Pegasus/log/install.log
%ghost %attr(0640, root, pegasus) %verify(not md5 size mtime) /var/lib/Pegasus/cache/trace/cimserver.trc
%defattr(0755, root, pegasus, 0755)
/usr/sbin/*
/usr/bin/*
%dir %{_libexecdir}/pegasus/
%{_libexecdir}/pegasus/
%defattr(0644, root, pegasus, 0755)
/usr/share/man/man8/*
/usr/share/man/man1/*
%doc doc/license.txt doc/Admin_Guide_Release.pdf
%doc OpenPegasusNOTICE.txt
%doc doc/PegasusSSLGuidelines.htm doc/SecurityGuidelinesForDevelopers.html
%doc doc/README.SUSE.Security src/Clients/repupgrade/doc/repupgrade.html
%doc doc/README.SUSE.SSL doc/cmpiOSBase_OperatingSystemProvider-cimprovagt.example

%files devel
%defattr(0644,root,pegasus,0755)
%{_libdir}/*.so
/usr/share/Pegasus/samples
/usr/include/Pegasus
/usr/share/Pegasus/html

%files libs
%defattr(0755, root, pegasus, 0750)
%{_libdir}/*.so.*
%if 0%{?suse_version}
%exclude %{_libdir}/libpegclient.so.1
%exclude %{_libdir}/libpegslp_client.so.1
%exclude %{_libdir}/libpegcommon.so.1
%exclude %{_libdir}/libpegexportserver.so.1
%exclude %{_libdir}/libpeglistener.so.1
%endif
%dir %{_libdir}/Pegasus
%{_libdir}/Pegasus/providers
%{_libdir}/Pegasus/providerManagers
%exclude %{_libexecdir}/pegasus
%exclude /usr/lib/systemd
%exclude %{_tmpfilesdir}
%if 0%{?suse_version}
%exclude %{_libdir}/Pegasus/test
%endif

%if 0%{?suse_version}
%files -n libpegclient1
%defattr(-,root,root,-)
%{_libdir}/libpegclient.so.1
%{_libdir}/libpegslp_client.so.1

%files -n libpegcommon1
%defattr(-,root,root,-)
%{_libdir}/libpegcommon.so.1

%files -n libpeglistener1
%defattr(-,root,root,-)
%{_libdir}/libpeglistener.so.1

%files -n libpegexportserver1
%defattr(-,root,root,-)
%{_libdir}/libpegexportserver.so.1
%endif

%if %{PEGASUS_BUILD_TEST_RPM}
%files test
%defattr(0644,root,pegasus,0755)
%if 0%{?suse_version}
%dir %{_libdir}/Pegasus/test
%{_libdir}/Pegasus/test/log.trace.0
%{_libdir}/Pegasus/test/testtracer4.trace.0
%{_libdir}/Pegasus/test/Makefile
%{_libdir}/Pegasus/test/mak
%dir %{_libdir}/Pegasus/test/tmp
%ghost %{_libdir}/Pegasus/test/tmp/procIdFile
%ghost %{_libdir}/Pegasus/test/tmp/trapLogFile
%ghost %{_libdir}/Pegasus/test/tmp/IndicationStressTestLog
%ghost %{_libdir}/Pegasus/test/tmp/oldIndicationStressTestLog
%verify(not md5 size mtime) /var/lib/Pegasus/testrepository
%defattr(0750,root,pegasus,0755)
%{_libdir}/Pegasus/test/bin
%{_libdir}/Pegasus/test/%PEGASUS_ARCH_LIB
%else
%dir /usr/share/Pegasus/test
/usr/share/Pegasus/test/log.trace.0
/usr/share/Pegasus/test/testtracer4.trace.0
/usr/share/Pegasus/test/Makefile
/usr/share/Pegasus/test/mak
%dir /usr/share/Pegasus/test/tmp
%ghost /usr/share/Pegasus/test/tmp/procIdFile
%ghost /usr/share/Pegasus/test/tmp/trapLogFile
%ghost /usr/share/Pegasus/test/tmp/IndicationStressTestLog
%ghost /usr/share/Pegasus/test/tmp/oldIndicationStressTestLog
%verify(not md5 size mtime) /var/lib/Pegasus/testrepository
%defattr(0750,root,pegasus,0755)
/usr/share/Pegasus/test/bin
/usr/share/Pegasus/test/%PEGASUS_ARCH_LIB
%endif
%endif

%pre
%if 0%{?suse_version}
if [ -f /var/lib/systemd/migrated/%{name} ]; then
%service_add_pre %{name}.service
fi
%endif
if [ $1 -gt 1 ]; then
   if [ -d /var/lib/Pegasus/repository ]; then
        if [ -d /var/lib/Pegasus/prev_repository ]; then
           rm -rf /var/lib/Pegasus/prev_repository
        fi;
        mv /var/lib/Pegasus/repository /var/lib/Pegasus/prev_repository;
   fi
fi
:;

%post
install -d -m 1750 -o root -g pegasus %{rundir}/%{name}
%if 0%{?suse_version}
getent group wbem >/dev/null || /usr/sbin/groupadd -r wbem
%service_add_post %{name}.service
%else
restorecon %{rundir}/%{name}
/sbin/ldconfig;
%systemd_post tog-pegasus.service
%endif
if [ $1 -ge 1 ]; then
   echo `date` >>  /var/lib/Pegasus/log/install.log 2>&1 || :;
   if [ $1 -gt 1 ]; then
      if [ -d /var/lib/Pegasus/prev_repository ]; then
        echo "prev_repository exists, running repupgrade" >>  /var/lib/Pegasus/log/install.log 2>&1 || :;
        mkdir -p /var/lib/Pegasus/repository
         ls /var/lib/Pegasus >>  /var/lib/Pegasus/log/install.log 2>&1 || :;
      #  The user's old repository was moved to /var/lib/Pegasus/prev_repository, which 
      #  now must be upgraded to the new repository in /var/lib/Pegasus/repository:
         /usr/sbin/repupgrade 2>> /var/lib/Pegasus/log/install.log || :;
         echo "repupgrade done" >>  /var/lib/Pegasus/log/install.log 2>&1 || :;
         ls /var/lib/Pegasus >>  /var/lib/Pegasus/log/install.log 2>&1 || :;
      fi;
      /bin/systemctl try-restart tog-pegasus.service >/dev/null 2>&1 || :;
   fi;
fi
:;

%preun
%if 0%{?suse_version}
%service_del_preun %{name}.service
%else
%systemd_preun stop tog-pegasus.service
%endif
if [ $1 -eq 0 ]; then                  
   # Package removal, not upgrade     
   rm -rf %{rundir}/%{name}
fi
:;

%postun
/sbin/ldconfig
%if 0%{?suse_version}
%service_del_postun %{name}.service
%else
%systemd_postun_with_restart tog-pegasus.service
%endif

%preun devel
if [ $1 -eq 0 ] ; then
   make --directory /usr/share/Pegasus/samples -s clean >/dev/null 2>&1 || :;
fi
:;

%pre libs
if [ $1 -eq 1 ]; then
#  first install: create the 'pegasus' user and group:
	getent group pegasus >/dev/null || \
		/usr/sbin/groupadd -g %{pegasus_gid} -f -r pegasus
	getent passwd pegasus >/dev/null || \
		/usr/sbin/useradd -u %{pegasus_uid} -r -N -M -g pegasus \
		-s /sbin/nologin -d /var/lib/Pegasus \
		-c "tog-pegasus OpenPegasus WBEM/CIM services" pegasus
fi

%if 0%{?suse_version}
%post libs -p /sbin/ldconfig
%else
%post libs
if [ $1 -eq 1 ]; then
   # Create Symbolic Links for SDK Libraries
   #
   ln -sf libpegclient.so.1 /usr/%PEGASUS_ARCH_LIB/libpegclient.so
   ln -sf libpegcommon.so.1 /usr/%PEGASUS_ARCH_LIB/libpegcommon.so
   ln -sf libpegprovider.so.1 /usr/%PEGASUS_ARCH_LIB/libpegprovider.so
   ln -sf libDefaultProviderManager.so.1 /usr/%PEGASUS_ARCH_LIB/libDefaultProviderManager.so
   ln -sf libCIMxmlIndicationHandler.so.1 /usr/%PEGASUS_ARCH_LIB/libCIMxmlIndicationHandler.so
   ln -sf libsnmpIndicationHandler.so.1 /usr/%PEGASUS_ARCH_LIB/libsnmpIndicationHandler.so

   # Create Symbolic Links for Packaged Provider Libraries
   #
   ln -sf libComputerSystemProvider.so.1 /usr/%PEGASUS_ARCH_LIB/Pegasus/providers/libComputerSystemProvider.so
   ln -sf libOSProvider.so.1 /usr/%PEGASUS_ARCH_LIB/Pegasus/providers/libOSProvider.so
   ln -sf libProcessProvider.so.1 /usr/%PEGASUS_ARCH_LIB/Pegasus/providers/libProcessProvider.so

   # Create Symbolic Links for Packaged Provider Managers
   #
   ln -sf libCMPIProviderManager.so.1 /usr/%PEGASUS_ARCH_LIB/Pegasus/providerManagers/libCMPIProviderManager.so

   # Change ownership of Symbolic Links to the 'pegasus' group
   #
   /bin/chgrp -h pegasus /usr/%{_lib}/libpegclient.so
   /bin/chgrp -h pegasus /usr/%{_lib}/libpegcommon.so 
   /bin/chgrp -h pegasus /usr/%{_lib}/libpegprovider.so
   /bin/chgrp -h pegasus /usr/%{_lib}/libDefaultProviderManager.so
   /bin/chgrp -h pegasus /usr/%{_lib}/libCIMxmlIndicationHandler.so
   /bin/chgrp -h pegasus /usr/%{_lib}/libsnmpIndicationHandler.so
   /bin/chgrp -h pegasus /usr/%{_lib}/Pegasus/providers/libComputerSystemProvider.so
   /bin/chgrp -h pegasus /usr/%{_lib}/Pegasus/providers/libOSProvider.so
   /bin/chgrp -h pegasus /usr/%{_lib}/Pegasus/providers/libProcessProvider.so
   /bin/chgrp -h pegasus /usr/%{_lib}/Pegasus/providerManagers/libCMPIProviderManager.so
fi
:;
/sbin/ldconfig
%endif

%postun libs -p /sbin/ldconfig

%post test -p /sbin/ldconfig

%postun test -p /sbin/ldconfig

%if 0%{?suse_version}
%post -n libpegclient1 -p /sbin/ldconfig
%postun -n libpegclient1 -p /sbin/ldconfig

%post -n libpegcommon1 -p /sbin/ldconfig
%postun -n libpegcommon1 -p /sbin/ldconfig

%post -n libpeglistener1 -p /sbin/ldconfig
%postun -n libpeglistener1 -p /sbin/ldconfig

%post -n libpegexportserver1 -p /sbin/ldconfig
%postun -n libpegexportserver1 -p /sbin/ldconfig
%endif

%changelog
