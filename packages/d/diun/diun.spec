#
# spec file for package diun
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           diun
Version:        4.31.0
Release:        0
Summary:        Receive notifications when an image is updated on a Docker registry
License:        MIT
URL:            https://github.com/crazy-max/diun
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source11:       %{name}.service
Source12:       %{name}.sysusers
BuildRequires:  sysuser-tools
BuildRequires:  golang(API) >= 1.24
%{sysusers_requires}

%description
Diun is a CLI application written in Go to receive notifications when a Docker
image is updated on a Docker registry.

%prep
%autosetup -p 1 -a 1

%build
go build \
   -mod=vendor \
   -buildmode=pie \
   -trimpath \
   -ldflags="-X main.version=v%{version}" \
   -o bin/%{name} ./cmd/

# user and group
%sysusers_generate_pre %{SOURCE12} %{name} %{name}.conf

%install
# Install the binary.
install -D -m 0755 bin/%{name} %{buildroot}/%{_bindir}/%{name}

install -d -m 0750 %{buildroot}%{_sysconfdir}/%{name}/
install -d -m 0750 %{buildroot}%{_sharedstatedir}/%{name}/

install -d -m 0755 %{buildroot}%{_unitdir}/
install -D -m 0644 %{SOURCE11} %{buildroot}%{_unitdir}/%{name}.service

install -D -m 0644 %{SOURCE12} %{buildroot}%{_sysusersdir}/%{name}.conf

%pre -f %{name}.pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_unitdir}/%{name}.service
%{_sysusersdir}/%{name}.conf
%dir %attr(750,root,%{name}) %{_sysconfdir}/%{name}/
%dir %attr(750,%{name},%{name}) %{_sharedstatedir}/%{name}/

%changelog
