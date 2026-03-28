#
# spec file for package sanlock
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "python"
%global pprefix python-
%define oldpython python
%bcond_without python
%bcond_without python2
%else
%global pprefix %{nil}
%bcond_with python
%bcond_with python2
%endif

#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
%define pname   sanlock
Name:           %{pprefix}%{pname}
Version:        5.0.0
Release:        0
%if ! %{with python}
Summary:        A shared disk lock manager
License:        GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/Base
%else
Summary:        Python bindings for the sanlock library
License:        GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/Base
%endif
URL:            https://pagure.io/sanlock
Source0:        %{pname}-%{version}.tar.xz
Source1:        sysconfig.sanlock
Source2:        sysconfig.wdmd
# Upstream patches
# SUSE patches
Patch100:       sanlock-SCHED_RESET_ON_FORK-undefined.patch
Patch101:       sanlock-python-prefix.patch
Patch102:       suse-systemd.patch
Patch103:       suse-no-date-time.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  device-mapper-devel
BuildRequires:  libaio-devel
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(blkid)
BuildRequires:  pkgconfig(uuid)
%if ! %{with python}
Requires(pre):  %fillup_prereq
Requires(pre):  shadow
Provides:       group(sanlock)
Provides:       user(sanlock)
Recommends:     logrotate
%{?systemd_requires}
%if 0%{?suse_version} >= 1500
Requires(pre):  group(disk)
%endif
%else
BuildRequires:  %{pname}-devel = %{version}
Provides:       sanlock-python
%if "%{python_flavor}" == "python2"
Provides:       %{oldpython}-%{pname}
%endif
%endif
%python_subpackages

%description
sanlock uses disk paxos to manage leases on shared storage.
Hosts connected to a common SAN can use this to synchronize their
access to the shared disks.
%if %{with python}
This package provides a module that permits applications written in
the Python programming language to use the interface supplied by the
sanlock library.
%endif

%package        -n libsanlock1
Summary:        A shared disk lock manager library
Group:          Development/Libraries/C and C++
Provides:       sanlock-lib = %{version}

%description    -n libsanlock1
The runtime libraries for sanlock, a shared disk lock manager.
Hosts connected to a common SAN can use this to synchronize their
access to the shared disks.

%package        -n %{pname}-devel
Summary:        Development files for %{pname}
Group:          Development/Libraries/C and C++
Requires:       libsanlock1 = %{version}-%{release}

%description    -n %{pname}-devel
The %{pname}-devel package contains libraries and header files for
developing applications that use %{pname}.

%package        -n fence-sanlock
Summary:        Fence agent using sanlock and wdmd
Group:          System/Base
Requires:       sanlock = %{version}-%{release}

%description    -n fence-sanlock
Fence agent and daemon for using sanlock and wdmd as a cluster fence agent.

%package -n     sanlk-reset
Summary:        Host reset daemon and client using sanlock
Group:          System/Base
Requires:       libsanlock1 = %{version}-%{release}
Requires:       sanlock = %{version}-%{release}

%description -n sanlk-reset
The reset daemon and client for sanlock.
A cooperating host running the daemon can be reset by a host
running the client, so long as both maintain access to a
common sanlock lockspace.

%prep
%setup -q -n %{pname}-%{version}
%patch -P 100
%patch -P 101
%patch -P 102 -p1
%patch -P 103 -p1

%build
%if ! %{with python}
# upstream does not require configure
# upstream does not support _smp_mflags
CFLAGS="%{optflags}" make -j1 -C wdmd
CFLAGS="%{optflags}" make -j1 -C src
%else
pushd python
CFLAGS="%{optflags} -fno-strict-aliasing" %pyproject_wheel
popd
%endif

%install
%if ! %{with python}
%make_install LIBDIR=%{_libdir} -C src
%make_install LIBDIR=%{_libdir} -C wdmd

install -D -m 644 src/sanlock.conf %{buildroot}/%{_sysconfdir}/sanlock/sanlock.conf
install -D -m 644 %{SOURCE1} %{buildroot}/%{_fillupdir}/sysconfig.sanlock
install -D -m 644 %{SOURCE2} %{buildroot}/%{_fillupdir}/sysconfig.wdmd

install -D -m 644 init.d/sanlock.service %{buildroot}/%{_unitdir}/sanlock.service
ln -s service %{buildroot}%{_sbindir}/rcsanlock
install -D -m 644 init.d/wdmd.service %{buildroot}/%{_unitdir}/wdmd.service
ln -s service %{buildroot}%{_sbindir}/rcwdmd

install -Dm 0644 src/logrotate.sanlock \
	%{buildroot}%{_sysconfdir}/logrotate.d/sanlock

install -Dd -m 0755 %{buildroot}%{_sysconfdir}/wdmd.d
%else
pushd python
%pyproject_install
popd
%endif

%if ! %{with python}
%pre -n %{pname}
getent group sanlock > /dev/null || groupadd \
	-g 179 sanlock
getent passwd sanlock > /dev/null || useradd \
	-u 179 -c "sanlock" -s /sbin/nologin -r \
	-g 179 -G disk -d %{_localstatedir}/run/sanlock sanlock

%service_add_pre wdmd.service
%service_add_pre sanlock.service

%post -n %{pname}
%service_add_post wdmd.service sanlock.service

%fillup_only -n wdmd
%fillup_only -n sanlock

%post -n libsanlock1 -p /sbin/ldconfig

%preun -n %{pname}
%service_del_preun wdmd.service sanlock.service

%postun -n %{pname}
%service_del_postun wdmd.service sanlock.service

%postun -n libsanlock1 -p /sbin/ldconfig

%files -n %{pname}
%dir %attr(0700, root, root) %{_sysconfdir}/wdmd.d/
%dir %attr(0700, root, root) %{_sysconfdir}/sanlock/
%config(noreplace) %{_sysconfdir}/sanlock/sanlock.conf
%{_sbindir}/rcsanlock
%{_fillupdir}/sysconfig.sanlock
%{_sbindir}/rcwdmd
%{_fillupdir}/sysconfig.wdmd
%{_unitdir}/sanlock.service
%{_unitdir}/wdmd.service
%{_sbindir}/sanlock
%{_sbindir}/wdmd
%{_mandir}/man8/wdmd*
%{_mandir}/man8/sanlock*
%config(noreplace) %{_sysconfdir}/logrotate.d/sanlock

%files -n libsanlock1
%{_libdir}/libsanlock.so.*
%{_libdir}/libsanlock_client.so.*
%{_libdir}/libwdmd.so.*

%files -n %{pname}-devel
%{_libdir}/libwdmd.so
%{_includedir}/wdmd.h
%{_libdir}/libsanlock.so
%{_libdir}/libsanlock_client.so
%{_includedir}/sanlock.h
%{_includedir}/sanlock_rv.h
%{_includedir}/sanlock_admin.h
%{_includedir}/sanlock_resource.h
%{_includedir}/sanlock_direct.h
%{_libdir}/pkgconfig/libsanlock.pc
%{_libdir}/pkgconfig/libsanlock_client.pc

%else

%files %{python_files}
%{python_sitearch}/sanlock*.so
%{python_sitearch}/sanlock_python-%{version}.dist-info
%endif

%changelog
