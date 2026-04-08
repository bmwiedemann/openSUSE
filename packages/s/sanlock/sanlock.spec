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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
%define pname   sanlock
Name:           %{pname}
Version:        5.1.0
Release:        0
Summary:        A shared disk lock manager
License:        GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/Base
URL:            https://codeberg.org/sanlock/sanlock
Source0:        %{pname}-%{version}.tar.xz
Source1:        sysconfig.sanlock
Source2:        sysconfig.wdmd
# Upstream patches
# SUSE patches
Patch100:       sanlock-SCHED_RESET_ON_FORK-undefined.patch
Patch101:       suse-systemd.patch
Patch102:       suse-no-date-time.patch
BuildRequires:  device-mapper-devel
BuildRequires:  libaio-devel
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(blkid)
BuildRequires:  pkgconfig(uuid)
Requires(pre):  %fillup_prereq
Requires(pre):  shadow
Provides:       group(sanlock)
Provides:       user(sanlock)
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

%package        -n %{pname}-devel
Summary:        Development files for %{pname}
Group:          Development/Libraries/C and C++
Requires:       libsanlock1 = %{version}-%{release}

%description    -n %{pname}-devel
The %{pname}-devel package contains libraries and header files for
developing applications that use %{pname}.

%prep
%setup -q -n %{pname}-%{version}
%patch -P 100
%patch -P 101 -p1
%patch -P 102 -p1

%build
# upstream does not require configure
# upstream does not support _smp_mflags
CFLAGS="%{optflags}" make -j1 -C wdmd
CFLAGS="%{optflags}" make -j1 -C src

%install
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

%changelog
