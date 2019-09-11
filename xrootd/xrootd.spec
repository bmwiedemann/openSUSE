#
# spec file for package xrootd
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

Name:           xrootd
Version:        3.3.6
Release:        0
Summary:        An eXtended Root Daemon (xrootd)
License:        LGPL-3.0-or-later
Group:          System/Daemons
Url:            http://xrootd.org/
Source0:        http://xrootd.org/download/v%{version}/xrootd-%{version}.tar.gz
Source1:        xrootd
Source2:        cmsd
Source3:        frm_xfrd
Source4:        frm_purged
# PATCH-FIX-OPENSUSE xrootd-gcc6-fix.patch bnc#985167 -- fixes build with gcc6, patch included in upstream version 4.3.0
Patch0:         xrootd-gcc6-fix.patch
# FATCH-FIX-OPENSUSE xrootd-gcc8-fix.patch -- fixes build with gcc8
Patch1:         xrootd-gcc8-fix.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  cmake >= 2.8
BuildRequires:  fdupes
BuildRequires:  fuse-devel
BuildRequires:  gcc-c++
BuildRequires:  glibc-devel
BuildRequires:  krb5-devel
BuildRequires:  libxml2-devel
BuildRequires:  ncurses-devel
BuildRequires:  openssl-devel
BuildRequires:  readline-devel
BuildRequires:  swig
BuildRequires:  zlib-devel
%if 0%{?suse_version} >= 1500
BuildRequires:  libtirpc-devel
%endif

%description
The eXtended Root Daemon

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1
%patch1 -p1

%build
mkdir build
cd build
# openssl version of leap 15 is not supported by xrootd 3
%if 0%{?suse_version} < 1500
	cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_BUILD_TYPE=RelWithDebInfo ../
%else
	cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_BUILD_TYPE=RelWithDebInfo  -DENABLE_CRYPTO=FALSE ../
%endif
make %{?_smp_mflags}

%install
cd build
rm -rf $RPM_BUILD_ROOT
make %{?_smp_mflags} install DESTDIR=$RPM_BUILD_ROOT
cd ..
rm -rf $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/*

mkdir -p $RPM_BUILD_ROOT%{_var}/log/%{name}
mkdir -p $RPM_BUILD_ROOT%{_var}/run/%{name}
mkdir -p $RPM_BUILD_ROOT%{_var}/spool/%{name}
mkdir -p $RPM_BUILD_ROOT%{_fillupdir}/
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_initrddir}
mkdir -p $RPM_BUILD_ROOT%{_sbindir}

install -m 644 packaging/rhel/xrootd.sysconfig $RPM_BUILD_ROOT%{_fillupdir}/sysconfig.%{name}
install -m 755 %{SOURCE2} $RPM_BUILD_ROOT%{_initrddir}/cmsd
install -m 755 %{SOURCE4} $RPM_BUILD_ROOT%{_initrddir}/frm_purged
install -m 755 %{SOURCE3} $RPM_BUILD_ROOT%{_initrddir}/frm_xfrd
install -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{_initrddir}/xrootd
install -m 755 packaging/rhel/xrootd.functions $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/xrootd.functions
install -m 644 packaging/common/xrootd-clustered.cfg $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/xrootd-clustered.cfg
install -m 644 packaging/common/xrootd-standalone.cfg $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/xrootd-standalone.cfg

ln -sf %{_initrddir}/xrootd $RPM_BUILD_ROOT%{_sbindir}/rcxrootd
ln -sf %{_initrddir}/cmsd $RPM_BUILD_ROOT%{_sbindir}/rccmsd
ln -sf %{_initrddir}/frm_purged $RPM_BUILD_ROOT%{_sbindir}/rcfrm_purged
ln -sf %{_initrddir}/frm_xfrd $RPM_BUILD_ROOT%{_sbindir}/rcfrm_xfrd

chmod -x $RPM_BUILD_ROOT%{_datadir}/%{name}/utils/XrdCmsNotify.pm
chmod -x $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/xrootd.functions

# Perl module
mkdir -p $RPM_BUILD_ROOT%{perl_vendorarch}/auto/XrdClientAdmin
mv $RPM_BUILD_ROOT/%{_libdir}/XrdClientAdmin.pm \
 $RPM_BUILD_ROOT%{perl_vendorarch}
mv $RPM_BUILD_ROOT/%{_libdir}/XrdClientAdmin.so* \
 $RPM_BUILD_ROOT%{perl_vendorarch}/auto/XrdClientAdmin

%fdupes $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%package cl
Summary:        The new XRootD client
Group:          Productivity/Clustering/Computing
Requires:       %{name}-libs = %{version}-%{release}

%description cl
The new XRootD client software.

%files cl
%defattr(-,root,root,-)
%{_libdir}/libXrdCl.so.*
%{_bindir}/xrdcopy
%{_bindir}/xrdfs
%doc %{_mandir}/man1/xrdcopy.1.gz
%doc %{_mandir}/man1/xrdfs.1.gz

%post cl -p /sbin/ldconfig
%postun cl -p /sbin/ldconfig

%package cl-devel
Summary:        Headers for compiling against xrootd-cl
Group:          Development/Libraries/Other
Requires:       %{name}-cl = %{version}-%{release}
Requires:       %{name}-client = %{version}-%{release}
Requires:       %{name}-libs = %{version}-%{release}
Requires:       %{name}-libs-devel = %{version}-%{release}

%description cl-devel
Headers for compiling against xrootd-cl

%files cl-devel
%defattr(-,root,root,-)
%{_includedir}/%{name}/XrdCl
%{_libdir}/libXrdCl.so

%package -n perl-xrood-client-admin
Summary:        XRootD client administration Perl module
Group:          Development/Libraries/Other
Requires:       %{name}-client = %{version}-%{release}
%if 0%{?suse_version} < 1140
Requires:       perl = %{perl_version}
%else
%{perl_requires}
%{?libperl_requires}
%endif

%description -n perl-xrood-client-admin
This package contains a swig generated xrootd client administration
Perl module.

%files -n perl-xrood-client-admin
%defattr(-,root,root,-)
%{perl_vendorarch}/XrdClientAdmin.pm
%dir %{perl_vendorarch}/auto/XrdClientAdmin/
%{perl_vendorarch}/auto/XrdClientAdmin/XrdClientAdmin.so

%package client
Summary:        XRootD client
Group:          Productivity/Clustering/Computing
Requires:       %{name}-libs = %{version}-%{release}

%description client
The XRootD client software.
%files client
%defattr(-,root,root,-)
%{_libdir}/libXrdClient.so.*
%{_libdir}/libXrdPosix.so.*
%{_libdir}/libXrdPosixPreload.so.*
%{_libdir}/libXrdFfs.so.*
%{_bindir}/xprep
%{_bindir}/xrd
%{_bindir}/xrdcp
%{_bindir}/xrdcp-old
%{_bindir}/xrdstagetool
%{_bindir}/xrdadler32
%doc %{_mandir}/man1/xprep.1.gz
%doc %{_mandir}/man1/xrd.1.gz
%doc %{_mandir}/man1/xrdadler32.1.gz
%doc %{_mandir}/man1/xrdcp.1.gz
%doc %{_mandir}/man1/xrdcp-old.1.gz
%doc %{_mandir}/man1/xrdstagetool.1.gz
%if 0%{?suse_version} < 1500
%{_bindir}/xrdgsiproxy
%doc %{_mandir}/man1/xrdgsiproxy.1.gz
%endif

%post client -p /sbin/ldconfig
%postun client -p /sbin/ldconfig

%package client-devel
Summary:        XRootD-client development files
Group:          Development/Libraries/Other
Requires:       %{name}-client = %{version}-%{release}
Requires:       %{name}-libs = %{version}-%{release}
Requires:       %{name}-libs-devel = %{version}-%{release}

%description client-devel
Headers for compiling against xrootd-client
%files client-devel
%defattr(-,root,root,-)
%{_libdir}/libXrdClient*.so
%{_libdir}/libXrdPosix.so
%{_libdir}/libXrdPosixPreload.so
%{_libdir}/libXrdFfs.so
%{_includedir}/%{name}/XrdClient
%{_includedir}/%{name}/XrdPosix

%package fuse
Summary:        XRootD filesystem
Group:          System/Filesystems
Requires:       %{name}-client = %{version}-%{release}
Requires:       %{name}-libs   = %{version}-%{release}
Requires:       fuse

%description fuse
Fuse driver for xrootd
%files fuse
%defattr(-,root,root,-)
%{_bindir}/xrootdfs
%doc %{_mandir}/man1/xrootdfs.1.gz
%attr(-,daemon,daemon) %dir %{_sysconfdir}/%{name}/

%package server
Summary:        XRootD server
Group:          System/Daemons
Requires:       %{name}-client = %{version}-%{release}
Requires:       %{name}-libs = %{version}-%{release}
Requires(pre): %insserv_prereq %fillup_prereq

%description server
The XRootD server
%files server
%defattr(-,root,root,-)
%{_bindir}/cconfig
%{_bindir}/cmsd
%{_bindir}/cns_ssi
%{_bindir}/frm_admin
%{_bindir}/frm_purged
%{_bindir}/frm_xfragent
%{_bindir}/frm_xfrd
%{_bindir}/mpxstats
%{_bindir}/wait41
%{_bindir}/XrdCnsd
%{_bindir}/xrdpwdadmin
%{_bindir}/xrdsssadmin
%{_bindir}/xrootd
%{_libdir}/libXrdBwm.so.*
%{_libdir}/libXrdPss*.so.*
%{_libdir}/libXrdOfs*.so.*
%{_libdir}/libXrdServer.so.*
%{_libdir}/libXrdXrootd.so.*
%doc %{_mandir}/man8/*
%{_fillupdir}/sysconfig.%{name}
%config(noreplace) %{_sysconfdir}/%{name}/xrootd-clustered.cfg
%config(noreplace) %{_sysconfdir}/%{name}/xrootd-standalone.cfg
%ghost%attr(-,daemon,daemon) %dir %{_var}/log/%{name}
%attr(-,daemon,daemon) %dir %{_var}/spool/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/utils
%{_initrddir}/cmsd
%{_initrddir}/frm_xfrd
%{_initrddir}/frm_purged
%{_initrddir}/xrootd
%config %{_sysconfdir}/%{name}/xrootd.functions
%{_sbindir}/rcxrootd
%{_sbindir}/rccmsd
%{_sbindir}/rcfrm_xfrd
%{_sbindir}/rcfrm_purged

%post server
/sbin/ldconfig || exit 1
%{fillup_and_insserv -n xrootd xrootd}
%restart_on_update xrootd
%fillup_and_insserv cmsd
%restart_on_update cmsd
%fillup_and_insserv frm_purged
%restart_on_update frm_purged
%fillup_and_insserv frm_xfrd
%restart_on_update frm_xfrd
%preun server
%stop_on_removal xrootd
%stop_on_removal cmsd
%stop_on_removal frm_purged
%stop_on_removal frm_xfrd
%postun server
/sbin/ldconfig || exit 1
%insserv_cleanup xrootd
%restart_on_update xrootd
%insserv_cleanup cmsd
%restart_on_update cmsd
%insserv_cleanup frm_purged
%restart_on_update frm_purged
%insserv_cleanup frm_xfrd
%restart_on_update frm xfrd

%package server-devel
Summary:        XRootD-server development files
Group:          Development/Libraries/Other
Requires:       %{name}-client = %{version}-%{release}
Requires:       %{name}-client-devel = %{version}-%{release}
Requires:       %{name}-libs = %{version}-%{release}
Requires:       %{name}-libs-devel = %{version}-%{release}
Requires:       %{name}-server = %{version}-%{release}

%description server-devel
Headers for compiling against xrootd-server
%files server-devel
%defattr(-,root,root,-)
%{_libdir}/libXrdBwm.so
%{_libdir}/libXrdPss*.so
%{_libdir}/libXrdOfs*.so
%{_libdir}/libXrdServer.so
%{_libdir}/libXrdXrootd.so
%{_includedir}/%{name}/XrdAcc
%{_includedir}/%{name}/XrdCms
%{_includedir}/%{name}/XrdOss
%{_includedir}/%{name}/XrdSfs
%{_includedir}/%{name}/XrdXrootd

%package libs
Summary:        XRootD core libraries
Group:          System/Libraries

%description libs
The XRootD core libraries
%files libs
%defattr(-,root,root,-)
%{_libdir}/libXrdSec*.so.*
%{_libdir}/libXrdCrypto*.so.*
%{_libdir}/libXrdUtils.so.*
%{_libdir}/libXrdCksCalc*.so.*
%{_libdir}/libXrdMain.so.*
%{_libdir}/libXrdAppUtils.so.*
%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%package libs-devel
Summary:        XRootD-lib development files
Group:          Development/Libraries/Other
Requires:       %{name}-libs = %{version}-%{release}

%description libs-devel
Headers for compiling against xrootd-libs
%files libs-devel
%defattr(-,root,root,-)
%dir %{_includedir}/%{name}
%{_libdir}/libXrdSec*.so
%{_libdir}/libXrdCrypto*.so
%{_libdir}/libXrdUtils.so
%{_libdir}/libXrdMain.so
%{_libdir}/libXrdCksCalc*.so
%{_libdir}/libXrdAppUtils.so
%{_includedir}/%{name}/XrdVersion.hh
%{_includedir}/%{name}/XrdVersionPlugin.hh
%{_includedir}/%{name}/XrdSec
%{_includedir}/%{name}/XrdNet
%{_includedir}/%{name}/XrdOuc
%{_includedir}/%{name}/XrdSys
%{_includedir}/%{name}/Xrd
%{_includedir}/%{name}/XProtocol
%{_includedir}/%{name}/XrdCks

%package private-devel
Summary:        Transitional package holding some private headers
Group:          Development/Libraries/Other
Requires:       %{name}-libs = %{version}-%{release}

%description private-devel
Transitional package holding some private headers

%files private-devel
%defattr(-,root,root,-)
%dir %{_includedir}/%{name}/private/
%dir %{_includedir}/%{name}/private/Xrd/
%{_includedir}/%{name}/private/Xrd/XrdPoll.hh
%dir %{_includedir}/%{name}/private/XrdClient/
%{_includedir}/%{name}/private/XrdClient/XrdClientInputBuffer.hh
%{_includedir}/%{name}/private/XrdClient/XrdClientLogConnection.hh
%{_includedir}/%{name}/private/XrdClient/XrdClientMessage.hh
%{_includedir}/%{name}/private/XrdClient/XrdClientPhyConnection.hh
%{_includedir}/%{name}/private/XrdClient/XrdClientSock.hh
%{_includedir}/%{name}/private/XrdClient/XrdClientConn.hh
%{_includedir}/%{name}/private/XrdClient/XrdClientConnMgr.hh
%{_includedir}/%{name}/private/XrdClient/XrdClientDebug.hh
%{_includedir}/%{name}/private/XrdClient/XrdClientReadCache.hh
%dir %{_includedir}/%{name}/private/XrdOfs/
%{_includedir}/%{name}/private/XrdOfs/XrdOfs.hh
%{_includedir}/%{name}/private/XrdOfs/XrdOfsEvr.hh
%{_includedir}/%{name}/private/XrdOfs/XrdOfsHandle.hh
%{_includedir}/%{name}/private/XrdOfs/XrdOfsTrace.hh
%dir %{_includedir}/%{name}/private/XrdSys/
%{_includedir}/%{name}/private/XrdSys/XrdSysPriv.hh
%dir %{_includedir}/%{name}/private/XrdNet/
%{_includedir}/%{name}/private/XrdNet/XrdNetBuffer.hh
%{_includedir}/%{name}/private/XrdNet/XrdNetPeer.hh
%dir %{_includedir}/%{name}/private/XrdOss/
%{_includedir}/%{name}/private/XrdOss/XrdOssApi.hh
%{_includedir}/%{name}/private/XrdOss/XrdOssConfig.hh
%{_includedir}/%{name}/private/XrdOss/XrdOssError.hh
%dir %{_includedir}/%{name}/private/XrdOuc/
%{_includedir}/%{name}/private/XrdOuc/XrdOucExport.hh
%{_includedir}/%{name}/private/XrdOuc/XrdOucPList.hh

%changelog
