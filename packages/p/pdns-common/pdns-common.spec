#
# spec file for package pdns-common
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


%if 0%{?suse_version} > 1230
%bcond_without systemd
%define  _localstatedir /run/pdns
%else
%bcond_with    systemd
%define  _localstatedir /var/run/pdns
%endif

%define home           %{_var}/lib/pdns

%{!?_tmpfilesdir: %global _tmpfilesdir /usr/lib/tmpfiles.d }

Name:           pdns-common
Version:        4.0
Release:        0
Summary:        Shared directories between PowerDNS Packages
License:        MIT
Group:          Productivity/Networking/DNS/Servers
Url:            https://www.powerdns.com/
Source:         pdns-common.tmpfiles.d
BuildArch:      noarch
%if %{with systemd}
BuildRequires:  pkgconfig(systemd)
%{?systemd_requires}
%endif
%if 0%{?suse_version}
PreReq:         shadow
%else
PreReq:         shadow-utils
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Shared directories between PowerDNS Packages

%prep

%build

%install
install -Dd -m 0755 %{buildroot}%{home}
install -Dd -m 0755 %{buildroot}%{_sysconfdir}/pdns

%if %{with systemd}
install -D    -m 0644 %{SOURCE0} %{buildroot}%{_tmpfilesdir}/%{name}.conf
%else
install -D -d -m 0750 %{buildroot}%{_localstatedir}
%endif

%pre
/usr/sbin/groupadd -r pdns >/dev/null 2>&1 || :
/usr/sbin/useradd -g pdns -s /bin/false -r -c "PowerDNS" -d %{home} pdns >/dev/null 2>&1 || :

%if %{with systemd}
%post
systemd-tmpfiles --create /usr/lib/tmpfiles.d/%{name}.conf ||:
%endif

%files
%defattr(-,root,root)
%if %{with systemd}
%{_tmpfilesdir}/%{name}.conf
%dir %attr(750,pdns,pdns) %ghost %{_localstatedir}/
%else
%dir %attr(750,pdns,pdns)        %{_localstatedir}/
%endif
%dir %attr(750,root,pdns)        %{_sysconfdir}/pdns/
%dir %attr(750,pdns,pdns)        %{home}/

%changelog
