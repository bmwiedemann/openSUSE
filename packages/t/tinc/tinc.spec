#
# spec file for package tinc
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           tinc
Version:        1.0.36
Release:        1%{?dist}
Summary:        A virtual private network daemon
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Security

URL:            http://www.tinc-vpn.org/
Source0:        http://www.tinc-vpn.org/packages/%{name}-%{version}.tar.gz
Patch0:         tinc-systemd-path-fix.patch
Patch1:	harden_tinc.service.patch
Patch2:	harden_tinc@.service.patch

BuildRequires:  lzo-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(zlib)

Requires(post):   info
Requires(preun):  info
%systemd_ordering

%description
tinc is a Virtual Private Network (VPN) daemon that uses tunnelling
and encryption to create a secure private network between hosts on
the Internet. Because the tunnel appears to the IP level network
code as a normal network device, there is no need to adapt any
existing software. This tunnelling allows VPN sites to share
information with each other over the Internet without exposing any
information to others.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%configure \
	--libexecdir=%{_prefix}/lib/ \
	--with-systemd
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} INSTALL="install -p"
mkdir -p %{buildroot}/etc/tinc
ln -s /usr/sbin/service %{buildroot}%{_sbindir}/rc%{name}
rm -f %{buildroot}%{_infodir}/dir

%pre
%service_add_pre %{name}.service %{name}@.service

%post
/sbin/install-info %{_infodir}/%{name}.info %{_infodir}/dir || :
%service_add_post %{name}.service %{name}@.service

%preun
if [ $1 = 0 ] ; then
/sbin/install-info --delete %{_infodir}/%{name}.info %{_infodir}/dir || :
fi
%service_del_preun %{name}.service %{name}@.service

%postun
%service_del_postun %{name}.service %{name}@.service

%files
%doc AUTHORS COPYING.README NEWS README THANKS doc/sample* doc/*.tex
%config(noreplace) /etc/tinc/
%{_mandir}/man*/%{name}*.*
%{_sbindir}/rc%{name}
%{_infodir}/%{name}.info.gz
%{_sbindir}/%{name}d
%{_unitdir}/%{name}*.service

%changelog
