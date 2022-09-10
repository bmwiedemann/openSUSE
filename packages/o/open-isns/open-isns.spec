#
# spec file for package open-isns
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


Name:           open-isns
Summary:        Partial Implementation of iSNS iSCSI registration
License:        LGPL-2.1-or-later
Group:          System/Kernel
Version:        0.102
Release:        0
Source:         %{name}-%{version}.tar.xz
Patch1:         Quiet-a-commpiler-warning.patch
URL:            https://github.com/open-iscsi/%{name}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  glibc-devel
BuildRequires:  make
BuildRequires:  meson >= 0.55.0
BuildRequires:  openslp-devel
BuildRequires:  openssl-devel
BuildRequires:  systemd-rpm-macros
%{?systemd_requires}
Requires:       coreutils
Recommends:     open-iscsi

%description
This is a partial implementation of the iSNS protocol (see below),
which supplies directory services for iSCSI initiators and targets.

The iSNS protocol is specified in
[RFC 4171](http://tools.ietf.org/html/rfc4171) and its purpose is to
make easier to discover, manage, and configure iSCSI devices. With
iSNS, iSCSI targets can be registered to a central iSNS server and
initiators can be configured to discover the targets by asking the
iSNS server.

%package devel
Summary:        Development files for open-isns
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
Files to develop an application using the open-isns library.

%prep
%autosetup -p1

%build
%global _lto_cflags %{?_lto_cflags} -ffat-lto-objects
%meson --default-library=both
%meson_build

%install
%meson_install
ln -sf /usr/sbin/service %{buildroot}/usr/sbin/rcisnsd

%post
%{run_ldconfig}
%{service_add_post isnsd.socket isnsd.service}

%postun
%{service_del_postun isnsd.socket isnsd.service}
%{run_ldconfig}

%pre
%{service_add_pre isnsd.socket isnsd.service}

%preun
%{service_del_preun isnsd.socket isnsd.service}

%post devel -p %{run_ldconfig}
%postun devel -p %{run_ldconfig}

%files
%defattr(-,root,root)
%{_sbindir}/isnsd
%{_sbindir}/isnsadm
%{_sbindir}/isnsdd
%dir %{_sysconfdir}/isns
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/isns/isnsd.conf
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/isns/isnsadm.conf
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/isns/isnsdd.conf
%{_sbindir}/rcisnsd
%license COPYING
%doc HACKING README TODO
%doc %{_mandir}/man8/isnsd.8%{?ext_man}
%doc %{_mandir}/man8/isnsadm.8%{?ext_man}
%doc %{_mandir}/man8/isnsdd.8%{?ext_man}
%doc %{_mandir}/man5/isns_config.5%{?ext_man}
%{_unitdir}/isnsd.service
%{_unitdir}/isnsd.socket
%{_libdir}/libisns.so.0

%files devel
%defattr(-,root,root)
%dir %{_includedir}/libisns
%{_includedir}/libisns/attrs.h
%{_includedir}/libisns/buffer.h
%{_includedir}/libisns/isns.h
%{_includedir}/libisns/isns-proto.h
%{_includedir}/libisns/message.h
%{_includedir}/libisns/paths.h
%{_includedir}/libisns/source.h
%{_includedir}/libisns/types.h
%{_includedir}/libisns/util.h
%{_libdir}/libisns.a
%{_libdir}/libisns.so
%{_libdir}/pkgconfig/libisns.pc

%changelog
