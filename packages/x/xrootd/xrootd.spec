#
# spec file for package xrootd
#
# Copyright (c) 2023 SUSE LLC
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


# SECTION Multiflavour definitions
%define pname xrootd
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "python"
%bcond_without python3
%define psuffix -python
%else
%bcond_with python3
%define psuffix %{nil}
%endif
# /SECTION

%define __builder ninja
%define skip_python2 1
%define plugver 5
%bcond_with    ceph
%bcond_without libc_semaphore

Name:           %{pname}%{psuffix}
Version:        5.5.5
Release:        0
Summary:        An eXtended Root Daemon
License:        LGPL-3.0-or-later
Group:          System/Daemons
URL:            http://xrootd.org/
Source0:        http://xrootd.org/download/v%{version}/xrootd-%{version}.tar.gz
Source1:        xrootd-user.conf
Source100:      xrootd-rpmlintrc
# PATCH0 [Python] Modernize build system https://github.com/xrootd/xrootd/pull/2025; patch rebased for current version
Patch0:         xrootd-modernize-python-builds.patch
# PATCH-FEATURE-OPENSUSE Hardening patches
Patch100:       harden_cmsd@.service.patch
Patch101:       harden_frm_purged@.service.patch
Patch102:       harden_frm_xfrd@.service.patch
Patch103:       harden_xrootd@.service.patch
BuildRequires:  ca-certificates
BuildRequires:  cmake >= 3.0
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  graphviz-gd
BuildRequires:  graphviz-gnome
BuildRequires:  ncurses-devel
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  readline-devel
BuildRequires:  swig
BuildRequires:  systemd-rpm-macros
BuildRequires:  sysuser-tools
BuildRequires:  pkgconfig(fuse)
BuildRequires:  pkgconfig(krb5)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(zlib)
%if %{with libc_semaphore}
BuildRequires:  glibc-devel >= 2.21
%else
BuildRequires:  glibc-devel
%endif
%if %{with ceph}
BuildRequires:  librados-devel
BuildRequires:  libradosstriper-devel
%endif
BuildRequires:  pkgconfig(libtirpc)
%if %{with python3}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  xrootd-client-devel  = %{version}
BuildRequires:  xrootd-libs-devel    = %{version}
BuildRequires:  xrootd-private-devel = %{version}
BuildRequires:  xrootd-server-devel  = %{version}
%define python_subpackage_only 1
%python_subpackages
%endif

%description
The XROOTD project gives access to data repositories.
The typical usage is to give access to file-based ones. It is
based on a scalable architecture, a communication protocol, and
a set of plugins and tools based on those. The ability to
configure it and to make it scale (for size and performance)
allows the deployment of data access clusters of virtually any
size, which can include sophisticated features, like
authentication/authorization, integrations with other systems,
WAN data distribution, etc.

The XRootD software framework is a generic suite for data access,
which can serve natively any kind of data, organized as a
hierarchical filesystem-like namespace, based on the concept
of a directory.

%package        ceph
Summary:        Ceph back-end plug-in for XRootD
Group:          System/Filesystems
Requires:       %{pname}-server = %{version}

%description    ceph
The XROOTD project gives access to data repositories.
The typical usage is to give access to file-based ones.

This package contains Ceph storage back-end plug-in for the
XRootD server.

%package        ceph-devel
Summary:        Ceph back-end plug-in for XRootD
Group:          Development/Libraries/C and C++
Requires:       %{pname}-ceph = %{version}
Requires:       %{pname}-server = %{version}

%description    ceph-devel
The XROOTD project gives access to data repositories.
The typical usage is to give access to file-based ones.

This package contains header files and development libraries
for XRootD Ceph storage back-end plug-in development.

%package        client
Summary:        XRootD command line client tools
Group:          Productivity/Clustering/Computing
Requires:       %{pname}-client-libs = %{version}
Requires:       %{pname}-libs        = %{version}
Provides:       %{pname}-cl          = %{version}
Obsoletes:      %{pname}-cl          < %{version}

%description    client
The XROOTD project gives access to data repositories.
The typical usage is to give access to file-based ones.

This package contains the command line tools used to
communicate with XRootD servers.

%package        client-libs
Summary:        Libraries used by XRootD clients
Group:          System/Libraries
Requires:       %{pname}-libs = %{version}

%description    client-libs
The XROOTD project gives access to data repositories.
The typical usage is to give access to file-based ones.

This package contains libraries used by XRootD clients.

%package        client-devel
Summary:        Development files for XRootD clients
Group:          Development/Libraries/C and C++
Requires:       %{pname}-client-libs = %{version}
Requires:       %{pname}-libs-devel  = %{version}
Recommends:     %{pname}-client      = %{version}
Provides:       %{pname}-cl-devel    = %{version}
Obsoletes:      %{pname}-cl-devel    < %{version}

%description    client-devel
The XROOTD project gives access to data repositories.
The typical usage is to give access to file-based ones.

This package contains header files and development libraries
for XRootD client development

%package        doc
Summary:        Developer documentation for the XRootD libraries
Group:          Documentation/Other
BuildArch:      noarch

%description    doc
The XROOTD project gives access to data repositories.
The typical usage is to give access to file-based ones.

This package contains the API documentation of the XRootD
libraries.

%package        fuse
Summary:        FUSE-based XRootD filesystem mount
Group:          System/Filesystems
Requires:       %{pname}-client = %{version}
Requires:       %{pname}-libs = %{version}
Requires:       fuse

%description    fuse
The XROOTD project gives access to data repositories.
The typical usage is to give access to file-based ones.

This package contains the FUSE (file system in user space)
XRootD mount tool.

%package        libs
Summary:        XRootD core libraries
Group:          System/Libraries
%if %{with libc_semaphore}
Requires:       glibc >= 2.21
%endif

%description    libs
The XROOTD project gives access to data repositories.
The typical usage is to give access to file-based ones.

This package contains libraries used by the XRootD servers and
clients.

%package        libs-devel
Summary:        Development files for XRootD core libraries
Group:          Development/Libraries/C and C++
Requires:       %{pname}-libs = %{version}

%description    libs-devel
The XROOTD project gives access to data repositories.
The typical usage is to give access to file-based ones.

This package contains header files and development libraries
for XRootD development.

%package        private-devel
Summary:        Private XRootD development files
Group:          Development/Libraries/C and C++
Requires:       %{pname}-libs = %{version}
Requires:       %{pname}-server-libs = %{version}

%description    private-devel
The XROOTD project gives access to data repositories.
The typical usage is to give access to file-based ones.

This package contains some private XRootD headers and development
libraries. The use of these fikles is strongly discouraged.
Backwards compatibility between versions is not guaranteed for
them.

%package        server
Summary:        XRootD (eXtended Root Daemon) server
Group:          System/Daemons
Requires:       %{pname}-client-libs = %{version}
Requires:       %{pname}-libs        = %{version}
Requires:       %{pname}-server-libs = %{version}
Recommends:     logrotate
%sysusers_requires

%description    server
The XROOTD project gives access to data repositories.
The typical usage is to give access to file-based ones.

The XRootD (eXtended Root Daemon) server binaries.

%package        server-libs
Summary:        Libraries used by XRootD servers
Group:          System/Daemons
Requires:       %{pname}-client-libs = %{version}
Requires:       %{pname}-libs = %{version}
Requires:       logrotate
Requires:       systemd
Requires(post): systemd
Requires(postun):systemd
Requires(pre):  systemd
Requires(preun):systemd

%description    server-libs
The XROOTD project gives access to data repositories.
The typical usage is to give access to file-based ones.

This package contains libraries used by XRootD servers.

%package        server-devel
Summary:        Development files for XRootD servers
Group:          Development/Libraries/C and C++
Requires:       %{pname}-client-devel = %{version}
Requires:       %{pname}-libs-devel   = %{version}
Requires:       %{pname}-server-libs  = %{version}
Recommends:     %{pname}-server       = %{version}

%description    server-devel
The XROOTD project gives access to data repositories.
The typical usage is to give access to file-based ones.

This package contains header files and development libraries
for XRootD server development.

%package -n python-xrootd
Summary:        Python bindings for xrootd

%description -n python-xrootd
This package provides python3 bindings for xrootd.

%prep
%autosetup -p1 -n %{pname}-%{version}

%build
%if %{with python3}
# Create a version file so that python packages get the right version info;
# this should not be needed when tagged version 5.6 is packaged
echo %{version} > VERSION

# cmake cannot inherit the right includedirs when running python builds; specify manually
export CFLAGS="%{optflags} -I%{_includedir}/%{pname} -I%{_includedir}/%{pname}/private"
export CXXFLAGS=${CFLAGS}
# https://github.com/xrootd/xrootd/issues/2032
%ifarch %ix86
export LDFLAGS+=" -Wno-error=odr"
%endif
%pyproject_wheel

%else

%sysusers_generate_pre %{SOURCE1} %{pname} xrootd-user.conf
%cmake \
   -DBUILD_PYTHON:BOOL=OFF \
   -DENABLE_CEPH:BOOL=%{with ceph} \
   -DUSE_LIBC_SEMAPHORE:BOOL=%{with libc_semaphore}

%cmake_build
doxygen ../Doxyfile
%endif

%install
%if %{with python3}

%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}/

%else

%cmake_install
test -e doxydoc/html && cp -pr doxydoc/html %{buildroot}%{_docdir}/%{pname}/

rm -rf %{buildroot}%{_sysconfdir}/%{pname}/*

mkdir -p %{buildroot}%{_var}/log/%{pname}
mkdir -p %{buildroot}%{_var}/spool/%{pname}

install -Dm 0644 -t %{buildroot}%{_sysconfdir}/%{pname}/ packaging/common/*.cfg
install -Dm 0644 -t %{buildroot}%{_unitdir} packaging/common/{cmsd,frm_purged,frm_xfrd,xrootd}@.service
install -Dm 0644 -t %{buildroot}%{_unitdir} packaging/common/{xrdhttp,xrootd}@.socket
install -Dm 0644 packaging/rhel/xrootd.tmpfiles %{buildroot}%{_tmpfilesdir}/%{pname}.conf
install -Dm 0644 packaging/common/client.conf %{buildroot}%{_sysconfdir}/%{pname}/client.conf
install -p -Dm 0644 packaging/common/xrootd.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/xrootd-server
install -Dm 0644 packaging/common/client-plugin.conf.example %{buildroot}%{_sysconfdir}/xrootd/client.plugins.d/client-plugin.conf.example

install -Dm 644 README %{buildroot}%{_docdir}/%{pname}/README

chmod -x %{buildroot}%{_datadir}/%{pname}/utils/XrdCmsNotify.pm

sed -i 's|/usr/bin/env bash|%{_bindir}/bash|' %{buildroot}%{_bindir}/xrootd-config
sed -i 's|/usr/bin/env perl|%{_bindir}/perl|' %{buildroot}%{_datadir}/%{pname}/utils/XrdOlbMonPerf
sed -i 's|/usr/bin/env perl|%{_bindir}/perl|' %{buildroot}%{_datadir}/%{pname}/utils/netchk

mkdir -p %{buildroot}%{_sysusersdir}
install -m 0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/

%fdupes %{buildroot}%{_prefix}

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig
%post client-libs -p /sbin/ldconfig
%postun client-libs -p /sbin/ldconfig
%post server-libs -p /sbin/ldconfig
%postun server-libs -p /sbin/ldconfig

%if %{with ceph}
%post ceph -p /sbin/ldconfig
%postun ceph -p /sbin/ldconfig
%endif

%pre server -f %{pname}.pre
%service_add_pre cmsd@.service frm_purged@.service frm_xfrd@.service xrootd@.service xrdhttp@.socket xrootd@.socket

%post server
%tmpfiles_create %{_tmpfilesdir}/%{pname}.conf
%service_add_post cmsd@.service frm_purged@.service frm_xfrd@.service xrootd@.service xrdhttp@.socket xrootd@.socket

%preun server
%service_del_preun cmsd@.service frm_purged@.service frm_xfrd@.service xrootd@.service xrdhttp@.socket xrootd@.socket

%postun server
%service_del_postun cmsd@.service frm_purged@.service frm_xfrd@.service xrootd@.service xrdhttp@.socket xrootd@.socket
%endif

%if %{without python3}
%files client
%license COPYING.LGPL LICENSE
%{_bindir}/xrdadler32
%{_bindir}/xrdcopy
%{_bindir}/xrdcks
%{_bindir}/xrdcp
%{_bindir}/xrdcrc32c
%{_bindir}/xrdfs
%{_bindir}/xrdgsiproxy
%{_bindir}/xrdpinls
%{_bindir}/xrdreplay
%{_mandir}/man1/xrdadler32.1%{?ext_man}
%{_mandir}/man1/xrdcopy.1%{?ext_man}
%{_mandir}/man1/xrdcp.1%{?ext_man}
%{_mandir}/man1/xrdfs.1%{?ext_man}
%{_mandir}/man1/xrdgsiproxy.1%{?ext_man}

%files client-libs
%license COPYING.LGPL LICENSE
%{_libdir}/libXrdCl.so.*
%{_libdir}/libXrdFfs.so.*
%{_libdir}/libXrdPosix.so.*
%{_libdir}/libXrdPosixPreload.so.*
# This lib may be used for LD_PRELOAD so the .so link needs to be included
%{_libdir}/libXrdPosixPreload.so
%dir %{_sysconfdir}/%{pname}/
%dir %{_sysconfdir}/%{pname}/client.plugins.d/
%config %{_sysconfdir}/%{pname}/client.plugins.d/client-plugin.conf.example
%config(noreplace) %{_sysconfdir}/%{pname}/client.conf

%files client-devel
%license COPYING.LGPL LICENSE
%{_bindir}/xrdgsitest
%{_mandir}/man1/xrdgsitest.1%{?ext_man}
%{_libdir}/libXrdCl.so
%{_libdir}/libXrdFfs.so
%{_libdir}/libXrdPosix.so
%dir %{_includedir}/%{pname}/
%{_includedir}/%{pname}/XrdCl/
%{_includedir}/%{pname}/XrdPosix/

%files doc
%license COPYING.LGPL LICENSE
%{_docdir}/%{pname}/

%files fuse
%license COPYING.LGPL LICENSE
%{_bindir}/xrootdfs
%{_mandir}/man1/xrootdfs.1%{?ext_man}

%files libs
%license COPYING.LGPL LICENSE
%{_libdir}/libXrdAppUtils.so.*
%{_libdir}/libXrdCrypto.so.*
%{_libdir}/libXrdCryptoLite.so.*
%{_libdir}/libXrdHttpUtils.so.*
%{_libdir}/libXrdUtils.so.*
%{_libdir}/libXrdXml.so.*
%{_libdir}/libXrdClProxyPlugin-%{plugver}.so
%{_libdir}/libXrdSec*-%{plugver}.so
%{_libdir}/libXrdCksCalczcrc32-%{plugver}.so
%{_libdir}/libXrdCryptossl-%{plugver}.so
%{_libdir}/libXrdCmsRedirectLocal-%{plugver}.so

%files libs-devel
%license COPYING.LGPL LICENSE
%{_bindir}/xrootd-config
%{_libdir}/libXrdAppUtils.so
%{_libdir}/libXrdCrypto.so
%{_libdir}/libXrdCryptoLite.so
%{_libdir}/libXrdHttpUtils.so
%{_libdir}/libXrdUtils.so
%{_libdir}/libXrdXml.so
%dir %{_includedir}/%{pname}/
%{_includedir}/%{pname}/XrdVersion.hh
%{_includedir}/%{pname}/XProtocol/
%{_includedir}/%{pname}/Xrd/
%{_includedir}/%{pname}/XrdCks/
%{_includedir}/%{pname}/XrdNet/
%{_includedir}/%{pname}/XrdOuc/
%{_includedir}/%{pname}/XrdOfs/
%{_includedir}/%{pname}/XrdSec/
%{_includedir}/%{pname}/XrdSys/
%{_includedir}/%{pname}/XrdXml/

%files private-devel
%license COPYING.LGPL LICENSE
%{_libdir}/libXrdSsiLib.so
%{_libdir}/libXrdSsiShMap.so
%dir %{_includedir}/%{pname}/
%{_includedir}/%{pname}/private/

%files server
%license COPYING.LGPL LICENSE
%{_bindir}/cconfig
%{_bindir}/cmsd
%{_bindir}/frm_admin
%{_bindir}/frm_purged
%{_bindir}/frm_xfragent
%{_bindir}/frm_xfrd
%{_bindir}/mpxstats
%{_bindir}/wait41
%{_bindir}/xrdacctest
%{_bindir}/xrdmapc
%{_bindir}/xrdpfc_print
%{_bindir}/xrdpwdadmin
%{_bindir}/xrdsssadmin
%{_bindir}/xrootd
%{_datadir}/%{pname}/
%{_mandir}/man8/cmsd.8%{?ext_man}
%{_mandir}/man8/frm_admin.8%{?ext_man}
%{_mandir}/man8/frm_purged.8%{?ext_man}
%{_mandir}/man8/frm_xfragent.8%{?ext_man}
%{_mandir}/man8/frm_xfrd.8%{?ext_man}
%{_mandir}/man8/mpxstats.8%{?ext_man}
%{_mandir}/man8/xrdpfc_print.8%{?ext_man}
%{_mandir}/man8/xrdpwdadmin.8%{?ext_man}
%{_mandir}/man8/xrdsssadmin.8%{?ext_man}
%{_mandir}/man8/xrootd.8%{?ext_man}
%{_mandir}/man1/xrdmapc.1%{?ext_man}
%{_sysusersdir}/%{pname}-user.conf
%{_tmpfilesdir}/%{pname}.conf
%{_unitdir}/cmsd@.service
%{_unitdir}/frm_purged@.service
%{_unitdir}/frm_xfrd@.service
%{_unitdir}/xrootd@.service
%{_unitdir}/xrdhttp@.socket
%{_unitdir}/xrootd@.socket
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}-server
%dir %{_sysconfdir}/%{pname}/
%attr(-,xrootd,xrootd) %config(noreplace) %{_sysconfdir}/%{pname}/xrootd-clustered.cfg
%attr(-,xrootd,xrootd) %config(noreplace) %{_sysconfdir}/%{pname}/xrootd-standalone.cfg
%attr(-,xrootd,xrootd) %config(noreplace) %{_sysconfdir}/%{pname}/xrootd-filecache-clustered.cfg
%attr(-,xrootd,xrootd) %config(noreplace) %{_sysconfdir}/%{pname}/xrootd-filecache-standalone.cfg
%attr(-,xrootd,xrootd) %config(noreplace) %{_sysconfdir}/%{pname}/xrootd-http.cfg
%attr(-,xrootd,xrootd) %dir %{_var}/log/%{pname}
%attr(-,xrootd,xrootd) %dir %{_var}/spool/%{pname}
%ghost %dir /run/%{pname}

%files server-libs
%license COPYING.LGPL LICENSE
%{_libdir}/libXrdClRecorder-%{plugver}.so
%{_libdir}/libXrdServer.so.*
%{_libdir}/libXrdSsiLib.so.*
%{_libdir}/libXrdSsiShMap.so.*
%{_libdir}/libXrdBlacklistDecision-%{plugver}.so
%{_libdir}/libXrdBwm-%{plugver}.so
%{_libdir}/libXrdFileCache-%{plugver}.so
%{_libdir}/libXrdHttp-%{plugver}.so
%{_libdir}/libXrdN2No2p-%{plugver}.so
%{_libdir}/libXrdOfsPrepGPI-%{plugver}.so
%{_libdir}/libXrdOssCsi-%{plugver}.so
%{_libdir}/libXrdOssSIgpfsT-%{plugver}.so
%{_libdir}/libXrdPfc-%{plugver}.so
%{_libdir}/libXrdPss-%{plugver}.so
%{_libdir}/libXrdSsi-%{plugver}.so
%{_libdir}/libXrdSsiLog-%{plugver}.so
%{_libdir}/libXrdThrottle-%{plugver}.so
%{_libdir}/libXrdXrootd-%{plugver}.so

%files server-devel
%license COPYING.LGPL LICENSE
%{_libdir}/libXrdServer.so
%dir %{_includedir}/%{pname}/
%{_includedir}/%{pname}/XrdAcc/
%{_includedir}/%{pname}/XrdCms/
%{_includedir}/%{pname}/XrdHttp/
%{_includedir}/%{pname}/XrdOss/
%{_includedir}/%{pname}/XrdPfc/
%{_includedir}/%{pname}/XrdSfs/
%{_includedir}/%{pname}/XrdXrootd/
%if %{with ceph}
%files ceph
%license COPYING.LGPL LICENSE
%{_libdir}/libXrdCeph-%{plugver}.so
%{_libdir}/libXrdCephXattr-%{plugver}.so
%{_libdir}/libXrdCephPosix.so.*

%files ceph-devel
%license COPYING.LGPL LICENSE
%{_libdir}/libXrdCephPosix.so
%endif

%else

%files %{python_files xrootd}
%license COPYING.LGPL LICENSE
%{python_sitearch}/XRootD/
%{python_sitearch}/pyxrootd/
%{python_sitearch}/xrootd-*info/
%endif

%changelog
