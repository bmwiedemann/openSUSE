#
# spec file for package istgt
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           istgt
Version:        0.20
Release:        0
%define upstreamrel 20141125
Summary:        Userspace iSCSI Target
License:        BSD-2-Clause
Group:          Productivity/Networking/Other
Url:            http://www.peach.ne.jp/archives/istgt/
Source:         istgt-%{upstreamrel}.tar.gz
Requires:       bash
BuildRequires:  autoconf
%define systemd_init 0
%if 0%{?suse_version} >= 1300
BuildRequires:  systemd
%define systemd_init 1
%{?systemd_requires}
%endif
%if 0%{?fedora_version} >= 20
BuildRequires: systemd-units
%define systemd_init 1
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Patch2:         add-istgtcontrol-manpage.patch
Patch3:         disk-support-0-len-read-and-write-CBDs.patch
Patch4:         lu-perform-lba-range-check-before-0-byte-fastpath.patch
Patch5:         lu-add-sense-data-to-out-of-range-read-and-write-err.patch
Patch6:         iscsi-cancel-conn-worker-threads-using-the-task_pipe.patch
Patch7:         md5-add-in-tree-MD5-library.patch
Patch8:         md5-use-in-tree-MD5-rather-than-libcrypto.patch
Patch9:         etc-add-systemd-service-file.patch
Patch10:        build-specify-systemd-services-file-on-Linux.patch
Patch11:        build-regenerate-configure.patch
Patch12:        etc-use-bindir-instead-of-sbindir-in-init-scripts.patch

%description
This software (istgt) is the implementation of iSCSI target
(refer to RFC3720 about iSCSI) developed for FreeBSD.
It includes iSCSI protocol processor and SPC-3 (SCSI Primary
Commands - 3) based logical unit emulation.

Key Features:
* MCS/MPIO for failover (up to 255 concurrent sessions)
* Multipath I/O (only support Microsoft MPIO/VMware ESXi)
* SPC-3 Persistent Reservation for cluster nodes
* 64bit LBA for over 2TB
* Header/Data digest by CRC32C
* CHAP w/Mutual authentication
* Multiple LUNs and ACLs for portals
* IPv6/IPv4 dual support

%prep
%setup -q -n istgt-%{upstreamrel}
%patch2 -p0
%patch3 -p0
%patch4 -p0
%patch5 -p0
%patch6 -p0
%patch7 -p0
%patch8 -p0
%patch9 -p0
%patch10 -p0
%patch11 -p0
%patch12 -p0

autoconf

%build
%if 0%{?systemd_init}
	%configure --with-unitdir=%{_unitdir} --with-configdir=%{_sysconfdir}/istgt
%else
	%configure --with-configdir=%{_sysconfdir}/istgt
%endif
make

%install
make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p  %{buildroot}/%{_sbindir}
%if 0%{?systemd_init}
	ln -s ../../%{_sbindir}/service %{buildroot}/%{_sbindir}/rc%{name}
%else
	ln -s ../../%{_sysconfdir}/init.d/%{name} %{buildroot}/%{_sbindir}/rc%{name}
%endif

%pre
%if 0%{?systemd_init}
	%service_add_pre istgt.service
%endif

%post
/sbin/ldconfig
%if 0%{?systemd_init}
	%service_add_post istgt.service
%endif

%preun
%if 0%{?systemd_init}
	%service_del_preun istgt.service
%else
	%{?stop_on_removal:%{stop_on_removal istgt}}
%endif

%postun
/sbin/ldconfig
%if 0%{?systemd_init}
	%service_del_postun istgt.service
%else
	%{?restart_on_update:%{restart_on_update istgt}}
	%{?insserv_cleanup:%{insserv_cleanup}}
%endif

%files
%defattr(-,root,root)
%{_bindir}/istgt
%{_bindir}/istgtcontrol
%dir %{_sysconfdir}/istgt/
%config %{_sysconfdir}/istgt/*.conf.sample
%if 0%{?systemd_init}
	%{_unitdir}/istgt.service
%else
	%{_sysconfdir}/init.d/istgt
%endif
%{_sbindir}/rcistgt

%doc %{_mandir}/man1/istgt.1.gz
%doc %{_mandir}/man1/istgtcontrol.1.gz

%changelog
