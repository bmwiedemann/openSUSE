#
# spec file for package xrootd
#
# Copyright (c) 2021 SUSE LLC
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


%bcond_with    ceph

%if 0%{?sle_version} < 150000 && !0%{?is_opensuse}
%bcond_with    libc_semaphore
%else
%bcond_without libc_semaphore
%endif

%define __builder ninja

Name:           xrootd
Version:        4.12.8
Release:        0
%define plugver 4
Summary:        An eXtended Root Daemon
License:        LGPL-3.0-or-later
Group:          System/Daemons
URL:            http://xrootd.org/
Source0:        https://github.com/xrootd/xrootd/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source100:      xrootd-rpmlintrc
Patch0:	harden_cmsd@.service.patch
Patch1:	harden_frm_purged@.service.patch
Patch2:	harden_frm_xfrd@.service.patch
Patch3:	harden_xrootd@.service.patch
BuildRequires:  cmake >= 2.8
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  graphviz-gd
BuildRequires:  graphviz-gnome
BuildRequires:  ncurses-devel
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  readline-devel
BuildRequires:  swig
BuildRequires:  systemd
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
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
%if 0%{?suse_version} >= 1500
BuildRequires:  pkgconfig(libtirpc)
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
Requires:       %{name}-server = %{version}

%description    ceph
The XROOTD project gives access to data repositories.
The typical usage is to give access to file-based ones.

This package contains Ceph storage back-end plug-in for the
XRootD server.

%package        ceph-devel
Summary:        Ceph back-end plug-in for XRootD
Group:          Development/Libraries/C and C++
Requires:       %{name}-ceph = %{version}
Requires:       %{name}-server = %{version}

%description    ceph-devel
The XROOTD project gives access to data repositories.
The typical usage is to give access to file-based ones.

This package contains header files and development libraries
for XRootD Ceph storage back-end plug-in development.

%package        client
Summary:        XRootD command line client tools
Group:          Productivity/Clustering/Computing
Requires:       %{name}-client-libs = %{version}
Requires:       %{name}-libs = %{version}
Provides:       %{name}-cl = %{version}
Obsoletes:      %{name}-cl < %{version}

%description    client
The XROOTD project gives access to data repositories.
The typical usage is to give access to file-based ones.

This package contains the command line tools used to
communicate with XRootD servers.

%package        client-libs
Summary:        Libraries used by XRootD clients
Group:          System/Libraries
Requires:       %{name}-libs = %{version}

%description    client-libs
The XROOTD project gives access to data repositories.
The typical usage is to give access to file-based ones.

This package contains libraries used by XRootD clients.

%package        client-devel
Summary:        Development files for XRootD clients
Group:          Development/Libraries/C and C++
Requires:       %{name}-client-libs = %{version}
Requires:       %{name}-libs-devel = %{version}
Provides:       %{name}-cl-devel = %{version}
Obsoletes:      %{name}-cl-devel < %{version}
Recommends:     %{name}-client = %{version}

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
Requires:       %{name}-client = %{version}
Requires:       %{name}-libs = %{version}
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
Requires:       %{name}-libs = %{version}

%description    libs-devel
The XROOTD project gives access to data repositories.
The typical usage is to give access to file-based ones.

This package contains header files and development libraries
for XRootD development.

%package        private-devel
Summary:        Private XRootD development files
Group:          Development/Libraries/C and C++
Requires:       %{name}-libs = %{version}

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
Requires:       %{name}-client-libs = %{version}
Requires:       %{name}-libs = %{version}
Requires:       %{name}-server-libs = %{version}
Recommends:     logrotate

%description    server
The XROOTD project gives access to data repositories.
The typical usage is to give access to file-based ones.

The XRootD (eXtended Root Daemon) server binaries.

%package        server-libs
Summary:        Libraries used by XRootD servers
Group:          System/Daemons
Requires:       %{name}-client-libs = %{version}
Requires:       %{name}-libs = %{version}
Requires:       logrotate
Requires:       systemd
Requires(pre):  systemd
Requires(preun):systemd
Requires(post): systemd
Requires(postun):systemd

%description    server-libs
The XROOTD project gives access to data repositories.
The typical usage is to give access to file-based ones.

This package contains libraries used by XRootD servers.

%package        server-devel
Summary:        Development files for XRootD servers
Group:          Development/Libraries/C and C++
Requires:       %{name}-client-devel = %{version}
Requires:       %{name}-libs-devel = %{version}
Requires:       %{name}-server-libs = %{version}
Recommends:     %{name}-server = %{version}

%description    server-devel
The XROOTD project gives access to data repositories.
The typical usage is to give access to file-based ones.

This package contains header files and development libraries
for XRootD server development.

%package     -n python3-%{name}
Summary:        Python 3 bindings for XRootD
Group:          Development/Libraries/Python
Requires:       %{name}-client-libs = %{version}

%description -n python3-xrootd
The XROOTD project gives access to data repositories.
The typical usage is to give access to file-based ones.

This package provides the python 3 bindings for XRootD.

%prep
%autosetup -p1

%build
%cmake \
   -DBUILD_PYTHON:BOOL=ON \
   -DPYTHON_EXECUTABLE:PATH=`which python3` \
   -DPYTHON_LIBRARY:PATH=%{_libdir} \
   -DPYTHON_INCLUDE_DIR:PATH=`python3 -c "from sysconfig import get_path;print(get_path('include'))"` \
   -DENABLE_CEPH:BOOL=%{with ceph} \
   -DUSE_LIBC_SEMAPHORE:BOOL=%{with libc_semaphore}

%cmake_build

cd ..
doxygen Doxyfile

%install
%cmake_install
rm -rf %{buildroot}%{_sysconfdir}/%{name}/*

mkdir -p %{buildroot}%{_var}/log/%{name}
mkdir -p %{buildroot}%{_var}/spool/%{name}

install -Dm 0644 -t %{buildroot}%{_sysconfdir}/%{name}/ packaging/common/*.cfg
install -Dm 0644 -t %{buildroot}%{_unitdir} packaging/common/{cmsd,frm_purged,frm_xfrd,xrootd}@.service
install -Dm 0644 -t %{buildroot}%{_unitdir} packaging/common/{xrdhttp,xrootd}@.socket
install -Dm 0644 packaging/rhel/xrootd.tmpfiles %{buildroot}%{_tmpfilesdir}/%{name}.conf
install -Dm 0644 packaging/common/client.conf %{buildroot}%{_sysconfdir}/%{name}/client.conf
install -p -Dm 0644 packaging/common/xrootd.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/xrootd
install -Dm 0644 packaging/common/client-plugin.conf.example %{buildroot}%{_sysconfdir}/xrootd/client.plugins.d/client-plugin.conf.example

install -Dm 644 README %{buildroot}%{_docdir}/%{name}/README
cp -pr doxydoc/html %{buildroot}%{_docdir}/%{name}/

chmod -x %{buildroot}%{_datadir}/%{name}/utils/XrdCmsNotify.pm

sed -i 's|/usr/bin/env bash|%{_bindir}/bash|' %{buildroot}%{_bindir}/xrootd-config
sed -i 's|/usr/bin/env perl|%{_bindir}/perl|' %{buildroot}%{_datadir}/%{name}/utils/XrdOlbMonPerf
sed -i 's|/usr/bin/env perl|%{_bindir}/perl|' %{buildroot}%{_datadir}/%{name}/utils/netchk

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

%pre server
getent group xrootd >/dev/null || groupadd -r xrootd
getent passwd xrootd >/dev/null || \
       useradd -r -g xrootd -c "XRootD runtime user" \
       -s /sbin/nologin -d %{_localstatedir}/spool/xrootd xrootd
%service_add_pre cmsd@.service frm_purged@.service frm_xfrd@.service xrootd@.service xrdhttp@.socket xrootd@.socket

%post server
%tmpfiles_create %{_tmpfilesdir}/%{name}.conf
%service_add_post cmsd@.service frm_purged@.service frm_xfrd@.service xrootd@.service xrdhttp@.socket xrootd@.socket

%preun server
%service_del_preun cmsd@.service frm_purged@.service frm_xfrd@.service xrootd@.service xrdhttp@.socket xrootd@.socket

%postun server
%service_del_postun cmsd@.service frm_purged@.service frm_xfrd@.service xrootd@.service xrdhttp@.socket xrootd@.socket

%files client
%license COPYING.LGPL LICENSE
%{_bindir}/xprep
%{_bindir}/xrd
%{_bindir}/xrdadler32
%{_bindir}/xrdcopy
%{_bindir}/xrdcp
%{_bindir}/xrdcp-old
%{_bindir}/xrdfs
%{_bindir}/xrdgsiproxy
%{_bindir}/xrdstagetool
%{_mandir}/man1/xprep.1%{?ext_man}
%{_mandir}/man1/xrd.1%{?ext_man}
%{_mandir}/man1/xrdadler32.1%{?ext_man}
%{_mandir}/man1/xrdcopy.1%{?ext_man}
%{_mandir}/man1/xrdcp.1%{?ext_man}
%{_mandir}/man1/xrdcp-old.1%{?ext_man}
%{_mandir}/man1/xrdfs.1%{?ext_man}
%{_mandir}/man1/xrdgsiproxy.1%{?ext_man}
%{_mandir}/man1/xrdstagetool.1%{?ext_man}

%files client-libs
%license COPYING.LGPL LICENSE
%{_libdir}/libXrdCl.so.*
%{_libdir}/libXrdClient.so.*
%{_libdir}/libXrdFfs.so.*
%{_libdir}/libXrdPosix.so.*
%{_libdir}/libXrdPosixPreload.so.*
# This lib may be used for LD_PRELOAD so the .so link needs to be included
%{_libdir}/libXrdPosixPreload.so
%dir %{_sysconfdir}/%{name}/
%dir %{_sysconfdir}/%{name}/client.plugins.d/
%config %{_sysconfdir}/%{name}/client.plugins.d/client-plugin.conf.example
%config(noreplace) %{_sysconfdir}/%{name}/client.conf

%files client-devel
%license COPYING.LGPL LICENSE
%{_bindir}/xrdgsitest
%{_mandir}/man1/xrdgsitest.1%{?ext_man}
%{_libdir}/libXrdCl.so
%{_libdir}/libXrdClient*.so
%{_libdir}/libXrdFfs.so
%{_libdir}/libXrdPosix.so
%dir %{_includedir}/%{name}/
%{_includedir}/%{name}/XrdCl/
%{_includedir}/%{name}/XrdClient/
%{_includedir}/%{name}/XrdPosix/

%files doc
%license COPYING.LGPL LICENSE
%{_docdir}/%{name}/

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
%dir %{_includedir}/%{name}/
%{_includedir}/%{name}/XrdVersion.hh
%{_includedir}/%{name}/XProtocol/
%{_includedir}/%{name}/Xrd/
%{_includedir}/%{name}/XrdCks/
%{_includedir}/%{name}/XrdNet/
%{_includedir}/%{name}/XrdOuc/
%{_includedir}/%{name}/XrdOfs/
%{_includedir}/%{name}/XrdSec/
%{_includedir}/%{name}/XrdSys/
%{_includedir}/%{name}/XrdXml/

%files private-devel
%license COPYING.LGPL LICENSE
%{_libdir}/libXrdSsiLib.so
%{_libdir}/libXrdSsiShMap.so
%dir %{_includedir}/%{name}/
%{_includedir}/%{name}/private/

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
%{_mandir}/man8/cmsd.8*
%{_mandir}/man8/frm_admin.8*
%{_mandir}/man8/frm_purged.8*
%{_mandir}/man8/frm_xfragent.8*
%{_mandir}/man8/frm_xfrd.8*
%{_mandir}/man8/mpxstats.8*
%{_mandir}/man8/xrdpfc_print.8*
%{_mandir}/man8/xrdpwdadmin.8*
%{_mandir}/man8/xrdsssadmin.8*
%{_mandir}/man8/xrootd.8*
%{_mandir}/man1/xrdmapc.1*
%{_datadir}/%{name}/
%{_unitdir}/cmsd@.service
%{_unitdir}/frm_purged@.service
%{_unitdir}/frm_xfrd@.service
%{_unitdir}/xrootd@.service
%{_unitdir}/xrdhttp@.socket
%{_unitdir}/xrootd@.socket
%{_tmpfilesdir}/%{name}.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%dir %{_sysconfdir}/%{name}/
%attr(-,xrootd,xrootd) %config(noreplace) %{_sysconfdir}/%{name}/xrootd-clustered.cfg
%attr(-,xrootd,xrootd) %config(noreplace) %{_sysconfdir}/%{name}/xrootd-standalone.cfg
%attr(-,xrootd,xrootd) %config(noreplace) %{_sysconfdir}/%{name}/xrootd-filecache-clustered.cfg
%attr(-,xrootd,xrootd) %config(noreplace) %{_sysconfdir}/%{name}/xrootd-filecache-standalone.cfg
%attr(-,xrootd,xrootd) %config(noreplace) %{_sysconfdir}/%{name}/xrootd-http.cfg
%attr(-,xrootd,xrootd) %dir %{_var}/log/%{name}
%attr(-,xrootd,xrootd) %dir %{_var}/spool/%{name}
# %%ghost %%dir %%{_var}/run/%%{name}

%files server-libs
%license COPYING.LGPL LICENSE
%{_libdir}/libXrdServer.so.*
%{_libdir}/libXrdSsiLib.so.*
%{_libdir}/libXrdSsiShMap.so.*
%{_libdir}/libXrdBlacklistDecision-%{plugver}.so
%{_libdir}/libXrdBwm-%{plugver}.so
%{_libdir}/libXrdFileCache-%{plugver}.so
%{_libdir}/libXrdHttp-%{plugver}.so
%{_libdir}/libXrdN2No2p-%{plugver}.so
%{_libdir}/libXrdOssSIgpfsT-%{plugver}.so
%{_libdir}/libXrdPss-%{plugver}.so
%{_libdir}/libXrdSsi-%{plugver}.so
%{_libdir}/libXrdSsiLog-%{plugver}.so
%{_libdir}/libXrdThrottle-%{plugver}.so
%{_libdir}/libXrdXrootd-%{plugver}.so

%files server-devel
%license COPYING.LGPL LICENSE
%{_libdir}/libXrdServer.so
%dir %{_includedir}/%{name}/
%{_includedir}/%{name}/XrdAcc/
%{_includedir}/%{name}/XrdCms/
%{_includedir}/%{name}/XrdFileCache/
%{_includedir}/%{name}/XrdHttp/
%{_includedir}/%{name}/XrdOss/
%{_includedir}/%{name}/XrdSfs/
%{_includedir}/%{name}/XrdXrootd/

%files -n python3-%{name}
%license COPYING.LGPL LICENSE
%{python3_sitearch}/XRootD/
%{python3_sitearch}/pyxrootd/
%{python3_sitearch}/xrootd-v%{version}-*.egg-info

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

%changelog
