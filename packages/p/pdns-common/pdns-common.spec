#
# spec file for package pdns-common
#
# Copyright (c) 2025 SUSE LLC
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


%define home           %{_var}/lib/pdns
%{!?_tmpfilesdir: %global _tmpfilesdir %{_prefix}/lib/tmpfiles.d }
Name:           pdns-common
Version:        4.0
Release:        0
Summary:        Shared directories between PowerDNS Packages
License:        MIT
Group:          Productivity/Networking/DNS/Servers
URL:            https://www.powerdns.com/
Source0:        pdns-common.tmpfiles.d
Source1:        system-user-pdns.conf
BuildRequires:  sysuser-tools
BuildArch:      noarch
%sysusers_requires
%if 0%{?suse_version}
# FIXME: use proper Requires(pre/post/preun/...)
PreReq:         shadow
%else
# FIXME: use proper Requires(pre/post/preun/...)
PreReq:         shadow-utils
%endif

%description
Shared directories between PowerDNS Packages

%prep

%build
%sysusers_generate_pre %{SOURCE1} pdns system-user-pdns.conf

%install
mkdir -p %{buildroot}%{_sysusersdir}
install -m 0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/

install -Dd -m 0755 %{buildroot}%{home}
install -Dd -m 0755 %{buildroot}%{_sysconfdir}/pdns

install -D    -m 0644 %{SOURCE0} %{buildroot}%{_tmpfilesdir}/%{name}.conf

%pre -f pdns.pre

%post
%tmpfiles_create %{_tmpfilesdir}/%{name}.conf

%files
%{_tmpfilesdir}/%{name}.conf
%dir %attr(750,root,pdns) %{_sysconfdir}/pdns/
%dir %attr(750,pdns,pdns) %{home}/
%{_sysusersdir}/system-user-pdns.conf

%changelog
