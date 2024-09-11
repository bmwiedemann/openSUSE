#
# spec file for package 3proxy
#
# Copyright (c) 2024 SUSE LLC
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


%define _user   proxy
%define _group  proxy
%define _home   %{_localstatedir}/lib/%{name}
Name:           3proxy
Version:        0.9.4+git20240718
Release:        0
Summary:        Tiny proxy servers set
License:        BSD-3-Clause OR Apache-2.0 OR GPL-2.0-or-later OR LGPL-2.1-or-later
URL:            https://github.com/%{name}/%{name}
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}.service
Source2:        %{name}-socks.firewalld
Source3:        %{name}.cfg
Requires(pre):  shadow
Provides:       group(%{_group})
Provides:       user(%{_user})

%description
Universal proxy server with HTTP, HTTPS, SOCKS v5, FTP,PO P3, UDP and TCP
portmapping, access control, bandwith control, traffic limitation and accounting
based on username, client IP, target IP, day time, day of week, etc.

%prep
%autosetup -p1
sed -i -e 's/USER/%{_user}/' -e 's/GROUP/%{_group}/' %{SOURCE1}
sed -i -e 's/CFLAGS = -g/CFLAGS = %{optflags}/' -e 's/LDFLAGS = -fPIE/LDFLAGS = -fPIC %{optflags}/' Makefile.Linux

%build
%make_build -f Makefile.Linux

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man{3,8}
mkdir -p %{buildroot}%{_localstatedir}/log/%{name}
install -pm0755 bin/%{name} %{buildroot}%{_bindir}/%{name}
install -pm0644 man/%{name}.cfg.3 %{buildroot}%{_mandir}/man3/%{name}.cfg.3
install -pm0644 man/%{name}.8 %{buildroot}%{_mandir}/man8/%{name}.8
install -Dpm0644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
install -Dpm0644 %{SOURCE2} %{buildroot}%{_prefix}/lib/firewalld/services/%{name}-socks.xml
install -Dpm0660 %{SOURCE3} %{buildroot}%{_home}/%{name}.cfg

%pre
getent group %{_group} &> /dev/null || groupadd -r %{_group}
getent passwd %{_user} &> /dev/null || %{_sbindir}/useradd -rc 'User for tiny proxy servers set.' -s /bin/false -d %{_home} -g %{_group} %{_user}
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%license copying
%doc authors cfg README
%config(noreplace) %attr(0660,%{_user},%{_group}) %{_home}/%{name}.cfg
%{_bindir}/%{name}
%{_mandir}/man3/%{name}.cfg.3%{?ext_man}
%{_mandir}/man8/%{name}.8%{?ext_man}
%{_unitdir}/%{name}.service
%{_prefix}/lib/firewalld
%dir %attr(-,%{_user},%{_group}) %{_home}
%dir %attr(-,%{_user},%{_group}) %{_localstatedir}/log/%{name}

%changelog
