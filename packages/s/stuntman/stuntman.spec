#
# spec file for package stuntman
#
# Copyright (c) 2020, Martin Hauke <mardnh@gmx.de>
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

%define stuntman_user stuntman
%define stuntman_group stuntman
%define stuntman_home %{_localstatedir}/lib/stuntman
Name:           stuntman
Version:        1.2.16
Release:        0
Summary:        STUN server and client
License:        Apache-2.0
Group:          Productivity/Telephony/Servers
URL:            http://www.stunprotocol.org
#Git-Clone:     https://github.com/jselbie/stunserver.git
Source:         http://www.stunprotocol.org/stunserver-%{version}.tgz
Source1:        %{name}.service
Source2:        %{name}.sysconfig
BuildRequires:  boost-devel
BuildRequires:  gcc-c++
BuildRequires:  help2man
BuildRequires:  openssl-devel
BuildRequires:  systemd-rpm-macros
Requires(pre):  shadow

%description
An implementation of the STUN protocol (Session Traversal Utilities
for NAT) as specified in RFCs 5389, 5769, and 5780. It also includes
backwards compatibility for RFC 3489.
This package provides an STUN server and client application.

%prep
%setup -q -n stunserver

%build
%make_build STANDARD_FLAGS="%optflags"

%install
install -d %{buildroot}%{_bindir}
install -pm755 stunclient %{buildroot}%{_bindir}/stunclient
install -pm755 stunserver %{buildroot}%{_bindir}/stunserver
install -d %{buildroot}/%{_localstatedir}/lib/stuntman
install -D -m0644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
install -D -m0644 %{SOURCE2} %{buildroot}%{_fillupdir}/sysconfig.stuntman
install -d %{buildroot}%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}
# create manpages
install -d %{buildroot}%{_mandir}/man1
help2man ./stunclient -n stunclient > %{buildroot}%{_mandir}/man1/stunclient.1
help2man ./stunserver -n stunserver > %{buildroot}%{_mandir}/man1/stunserver.1

%pre
%service_add_pre %{name}.service
# Create stuntman user/group
getent group %{stuntman_group} >/dev/null || groupadd -r %{stuntman_group}
getent passwd %{stuntman_user} >/dev/null || useradd -r -g %{stuntman_group} -d %{stuntman_home} -s /sbin/nologin -c "stuntman - STUN Server" %{stuntman_user}

%post
%service_add_post %{name}.service
%fillup_only

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%check
cd testcode && ./stuntestcode

%files
%license LICENSE
%doc HISTORY README
%doc testcode/stun.conf
%{_bindir}/stunclient
%{_bindir}/stunserver
%{_sbindir}/rc%{name}
%{_unitdir}/%{name}.service
%{_fillupdir}/sysconfig.stuntman
%{_mandir}/man1/stunclient.1%{ext_man}
%{_mandir}/man1/stunserver.1%{ext_man}

%changelog
