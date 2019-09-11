#
# spec file for package govpn
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           govpn
Version:        7.5
Release:        0
Summary:        Virtual Private Network Implementation
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Web/Proxy
URL:            http://govpn.info/
Source:         http://www.govpn.info/download/%{name}-%{version}.tar.xz
Source1:        http://www.govpn.info/download/%{name}-%{version}.tar.xz.sig
Source2:        %{name}.keyring
Source3:        %{name}.conf
Source4:        %{name}@.service
Source5:        %{name}.target
BuildRequires:  go >= 1.6
BuildRequires:  systemd-rpm-macros
Requires(post): info
Requires(preun): info
Suggests:       %{name}-server = %{version}

%description
GoVPN is a virtual private network daemon, written in Go.

It uses strong passphrase authenticated key agreement protocol with
augmented zero-knowledge mutual peers authentication (PAKE DH A-EKE).
It features encrypted authenticated data transport that hides
message's length and timestamps, has the Perfect Forward Secrecy
property, is resistant to offline dictionary attacks, replay attacks,
client's passphrases compromising and dictionary attacks on the
server side, has built-in heartbeating, rehandshaking, real-time
statistics, the ability to work through UDP, TCP and HTTP proxies,
and IPv4/IPv6-compatibility.

%package server
Summary:        Simple Virtual Private Network Server
Group:          Productivity/Networking/Web/Servers
Requires:       %{name} = %{version}
Requires(pre):  shadow
%systemd_requires

%description server
GoVPN is a virtual private network daemon, written in Go.

It uses strong passphrase authenticated key agreement protocol with
augmented zero-knowledge mutual peers authentication (PAKE DH A-EKE).
It features encrypted authenticated data transport that hides
message's length and timestamps, has the Perfect Forward Secrecy
property, is resistant to offline dictionary attacks, replay attacks,
client's passphrases compromising and dictionary attacks on the
server side, has built-in heartbeating, rehandshaking, real-time
statistics, the ability to work through UDP, TCP and HTTP proxies,
and IPv4/IPv6-compatibility.

%prep
%setup -q
cp -f %{SOURCE3} %{name}.conf
cp -f %{SOURCE4} %{name}@.service
cp -f %{SOURCE5} %{name}.target

%build
make %{?_smp_mflags} V=1

%install
make install-strip \
  DESTDIR=%{buildroot}                   \
  PREFIX=%{_prefix}                      \
  INFODIR=%{buildroot}%{_infodir}        \
  DOCDIR=%{buildroot}%{_docdir}/%{name}/
rm -f %{buildroot}%{_docdir}/%{name}/INSTALL

install -Dpm 0644 %{name}.conf %{buildroot}%{_sysconfdir}/%{name}.conf
mkdir -p %{buildroot}%{_sysconfdir}/%{name}.d/

install -Dpm 0644 %{name}@.service %{buildroot}%{_unitdir}/%{name}@.service
install -Dpm 0644 %{name}.target %{buildroot}%{_unitdir}/%{name}.target

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info%{?ext_info}

%postun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info%{?ext_info}

%pre server
getent group %{name} >/dev/null || %{_sbindir}/groupadd -r %{name}
getent passwd %{name} >/dev/null || \
	%{_sbindir}/useradd -g %{name} -s /bin/false -r -c "%{name} daemon" \
	-d "%{_localstatedir}/lib/empty" %{name}

%post server
%service_add_post %{name}.target

%preun server
%service_del_preun %{name}.target

%postun server
%service_del_postun %{name}.target

%files
%license COPYING
%doc %{_docdir}/%{name}/
%{_bindir}/%{name}-client
%{_bindir}/%{name}-verifier
%{_datadir}/%{name}/
%{_infodir}/%{name}.info%{?ext_info}

%files server
%config %{_sysconfdir}/%{name}.conf
%dir %{_sysconfdir}/%{name}.d/
%{_bindir}/%{name}-server
%{_unitdir}/%{name}*

%changelog
