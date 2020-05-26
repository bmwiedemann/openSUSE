#
# spec file for package target-isns
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


Name:           target-isns
Summary:        Supplies iSNS support for Linux kernel target
License:        GPL-2.0-or-later
Group:          System/Kernel
Version:        0.6.8
Release:        0
Source:         %{name}-%{version}.tar.xz
URL:            https://github.com/open-iscsi/target-isns
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  cmake
BuildRequires:  flex
BuildRequires:  glibc-devel
BuildRequires:  systemd-rpm-macros
%{?systemd_requires}

%description
Target-isns is an Internet Storage Name Service (iSNS) client for the
Linux LIO iSCSI target. It allows to register LIO iSCSI targets to an
iSNS server.

The iSNS protocol is specified in
[RFC 4171](http://tools.ietf.org/html/rfc4171) and its purpose is to
make easier to discover, manage, and configure iSCSI devices. With
iSNS, iSCSI targets can be registered to a central iSNS server and
initiators can be configured to discover the targets by asking the
iSNS server.

%prep
%setup -n %{name}-%{version}

%build
%cmake -DSUPPORT_SYSTEMD=ON
make

%install
cd build
make DESTDIR="%{buildroot}" install
if [ ! -d "%{buildroot}/usr/sbin" ] ; then
	mkdir -p "%{buildroot}/usr/sbin"
fi
ln -sf /usr/sbin/service "%{buildroot}/usr/sbin/rc%{name}"

%post
%{service_add_post target-isns.service}

%postun
%{service_del_postun target-isns.service}

%pre
%{service_add_pre target-isns.service}

%preun
%{service_del_preun target-isns.service}

%files
%defattr(-,root,root)
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/target-isns.conf
%{_bindir}/target-isns
%{_sbindir}/rctarget-isns
%doc COPYING README.md THANKS
%doc %{_mandir}/man8/target-isns.8%{?ext_man}
%{_unitdir}/target-isns.service

%changelog
