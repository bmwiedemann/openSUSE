#
# spec file for package sanlock
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


%define with_fence_sanlockd 0
%define with_sanlk_reset    0
%if 0%{?suse_version} > 1320
%define with_fence_sanlockd 1
%define with_sanlk_reset    1
%endif
#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
%bcond_without python2
Name:           sanlock
Version:        3.8.0
Release:        0
Summary:        A shared disk lock manager
License:        GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/Base
Url:            https://pagure.io/sanlock
Source0:        %{name}-%{version}.tar.gz
Source1:        sysconfig.sanlock
Source2:        sysconfig.wdmd
Source3:        fence_sanlockd.init
# Upstream patches
# SUSE patches
Patch100:       sanlock-SCHED_RESET_ON_FORK-undefined.patch
Patch101:       sanlock-python-prefix.patch
Patch102:       suse-systemd.patch
Patch103:       suse-no-date-time.patch
Patch104:       sanlock-lto-disable-fpie.patch
BuildRequires:  %{python_module devel}
BuildRequires:  libaio-devel
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(blkid)
Requires(pre):  %fillup_prereq
Requires(pre):  shadow
Recommends:     logrotate
%{?systemd_requires}
%if 0%{?suse_version} >= 1500
Requires(pre):  group(disk)
%endif

%description
sanlock uses disk paxos to manage leases on shared storage.
Hosts connected to a common SAN can use this to synchronize their
access to the shared disks.

%package        -n libsanlock1
Summary:        A shared disk lock manager library
Group:          Development/Libraries/C and C++
Provides:       sanlock-lib = %{version}

%description    -n libsanlock1
The runtime libraries for sanlock, a shared disk lock manager.
Hosts connected to a common SAN can use this to synchronize their
access to the shared disks.

%package        -n python2-%{name}
Summary:        Python bindings for the sanlock library
Group:          Development/Libraries/Python
Requires:       libsanlock1 = %{version}-%{release}
Provides:       python-%{name}
Provides:       sanlock-python

%description    -n python2-%{name}
A module that permits applications written in the Python programming
language to use the interface supplied by the sanlock library.

%package        -n python3-%{name}
Summary:        Python bindings for the sanlock library
Group:          Development/Libraries/Python
Requires:       libsanlock1 = %{version}-%{release}

%description    -n python3-%{name}
A module that permits applications written in the Python programming
language to use the interface supplied by the sanlock library.


%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       libsanlock1 = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

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
%setup -q
%patch100
%patch101
%patch102 -p1
%patch103 -p1
%patch104 -p1

%build
# upstream does not require configure
# upstream does not support _smp_mflags
CFLAGS="%{optflags}" make -j1 -C wdmd
CFLAGS="%{optflags}" make -j1 -C src
pushd python
CFLAGS="%{optflags} -fno-strict-aliasing" %python_build
popd
%if %{with_fence_sanlockd}
CFLAGS="%{optflags}" make -j1 -C fence_sanlock
%endif
%if %{with_sanlk_reset}
CFLAGS="%{optflags}" make -j1 -C reset
%endif

%install
%make_install LIBDIR=%{_libdir} -C src
%make_install LIBDIR=%{_libdir} -C wdmd
pushd python
%python_install
popd
%if %{with_fence_sanlockd}
%make_install LIBDIR=%{_libdir} -C fence_sanlock
%endif
%if %{with_sanlk_reset}
%make_install LIBDIR=%{_libdir} -C reset
%endif

install -D -m 644 src/sanlock.conf %{buildroot}/%{_sysconfdir}/sanlock/sanlock.conf
install -D -m 644 %{SOURCE1} %{buildroot}/%{_fillupdir}/sysconfig.sanlock
install -D -m 644 %{SOURCE2} %{buildroot}/%{_fillupdir}/sysconfig.wdmd

install -D -m 644 init.d/sanlock.service %{buildroot}/%{_unitdir}/sanlock.service
ln -s service %{buildroot}%{_sbindir}/rcsanlock
install -D -m 644 init.d/wdmd.service %{buildroot}/%{_unitdir}/wdmd.service
ln -s service %{buildroot}%{_sbindir}/rcwdmd
%if %{with_fence_sanlockd}
install -D -m 0755 %{SOURCE3} %{buildroot}%{_prefix}/lib/systemd/systemd-fence_sanlockd
install -D -m 0644 init.d/fence_sanlockd.service %{buildroot}/%{_unitdir}/fence_sanlockd.service
ln -s service %{buildroot}%{_sbindir}/rcfence_sanlockd
%endif
%if %{with_sanlk_reset}
install -D -m 0644 init.d/sanlk-resetd.service %{buildroot}/%{_unitdir}/sanlk-resetd.service
ln -s service %{buildroot}%{_sbindir}/rcsanlk-resetd
%endif

install -Dm 0644 src/logrotate.sanlock \
	%{buildroot}%{_sysconfdir}/logrotate.d/sanlock

install -Dd -m 0755 %{buildroot}%{_sysconfdir}/wdmd.d

%pre
getent group sanlock > /dev/null || groupadd \
	-g 179 sanlock
getent passwd sanlock > /dev/null || useradd \
	-u 179 -c "sanlock" -s /sbin/nologin -r \
	-g 179 -G disk -d %{_localstatedir}/run/sanlock sanlock

%service_add_pre wdmd.service
%service_add_pre sanlock.service

%pre -n fence-sanlock
%service_add_pre fence_sanlockd.service

%pre -n sanlk-reset
%service_add_pre sanlk-resetd.service

%post
%service_add_post wdmd.service sanlock.service

%fillup_only -n wdmd
%fillup_only -n sanlock

%post -n libsanlock1 -p /sbin/ldconfig

%if %{with_fence_sanlockd}
%post -n fence-sanlock
%service_add_post fence_sanlockd.service
%endif

%post -n sanlk-reset
%service_add_post sanlk-resetd.service

%preun
%service_del_preun wdmd.service sanlock.service

%preun -n fence-sanlock
%service_del_preun fence_sanlockd.service

%preun -n sanlk-reset
%service_del_preun sanlk-resetd.service

%postun
%service_del_postun wdmd.service sanlock.service

%postun -n libsanlock1 -p /sbin/ldconfig
%postun -n fence-sanlock
%service_del_postun fence_sanlockd.service

%postun -n sanlk-reset
%service_del_postun sanlk-resetd.service

%files
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

%if %{with python2}
%files -n python2-%{name}
%{python2_sitearch}/*
%endif

%files -n python3-%{name}
%{python3_sitearch}/*

%files devel
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

%if %{with_fence_sanlockd}
%files -n fence-sanlock
%{_sbindir}/fence_sanlockd
%{_prefix}/lib/systemd/systemd-fence_sanlockd
%{_unitdir}/fence_sanlockd.service
%{_sbindir}/fence_sanlock
%{_sbindir}/fence_sanlockd
%{_sbindir}/rcfence_sanlockd
%{_mandir}/man8/fence_sanlock*
%endif

%if %{with_sanlk_reset}
%files -n sanlk-reset
%{_sbindir}/sanlk-reset
%{_sbindir}/sanlk-resetd
%{_sbindir}/rcsanlk-resetd
%{_unitdir}/sanlk-resetd.service
%{_mandir}/man8/sanlk-reset.8%{?ext_man}
%{_mandir}/man8/sanlk-resetd.8%{?ext_man}
%endif

%changelog
