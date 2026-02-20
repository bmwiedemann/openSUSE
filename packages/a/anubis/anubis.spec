#
# spec file for package Anubis
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


Name:           anubis
Version:        1.25.0
Release:        0
Summary:        Web AI Firewall Utility
License:        MIT
URL:            https://github.com/TecharoHQ/anubis
Source0:        %{url}/releases/download/v%{version}/%{name}-src-vendor-npm-%{version}.tar.gz
Source1:        %{url}/releases/download/v%{version}/%{name}-src-vendor-npm-%{version}.tar.gz.asc
Source3:        %{name}@.service
Patch0:         block-tencent-cloud-by-default.patch
BuildRequires:  golang-packaging
BuildRequires:  systemd-rpm-macros
%{?systemd_ordering}

%description
%{name} is a Web AI Firewall Utility that weighs the soul of your connection using
one or more challenges in order to protect upstream resources from scraper bots.

%prep
%autosetup -p1 -n %{name}-src-vendor-npm-%{version}

%build
export GO_LDFLAGS="-buildmode=pie -mod=vendor -X 'github.com/TecharoHQ/%{name}.Version=%{version}'"

go build -o .%{_localstatedir}/%{name} ./cmd/%{name}
go build -o .%{_localstatedir}/robots2policy ./cmd/robots2policy
go build -o .%{_localstatedir}/iplist2rule ./utils/cmd/iplist2rule

%install
install -D -m 0755 var/%{name} %{buildroot}%{_bindir}/%{name}
install -D -m 0755 var/robots2policy %{buildroot}%{_bindir}/robots2policy
install -D -m 0755 var/iplist2rule %{buildroot}%{_bindir}/iplist2rule
install -D -m 0644 run/default.env %{buildroot}%{_sysconfdir}/%{name}/default.env

# # service
install -D -p -m 0644 %{SOURCE3} %{buildroot}%{_unitdir}/%{name}@.service

%pre
%service_add_pre %{name}@.service

%post
%service_add_post %{name}@.service

%preun
%service_del_preun %{name}@.service

%postun
%service_del_postun %{name}@.service

%files
%license LICENSE
%config %{_sysconfdir}/%{name}/default.env
%dir %{_sysconfdir}/%{name}
%doc data
%doc docs
%doc SECURITY.md
%doc README.md
%{_bindir}/%{name}
%{_bindir}/robots2policy
%{_bindir}/iplist2rule
%{_unitdir}/%{name}@.service

%changelog
