#
# spec file for package forgejo-guardian
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


Name:           forgejo-guardian
Version:        0.6.0
Release:        0
Summary:        Simple Forgejo instance guardian
License:        AGPL-3.0-or-later
URL:            https://git.4rs.nl/awiteb/forgejo-guardian
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
Source2:        %{name}.service
Source3:        %{name}.config.example.toml
BuildRequires:  cargo-packaging
Requires:       forgejo >= 10.0.0
%{?systemd_requires}

%description
Simple Forgejo instance guardian, banning users and alerting admins based on
certain regular expressions (regex)

%prep
%autosetup -a1
cp %{SOURCE3} .

%build
%{cargo_build}

%install
install -d %{buildroot}%{_sysconfdir}/%{name}
install -Dm0755 ./target/release/%{name} %{buildroot}%{_bindir}/%{name}
install -Dm0644 %{SOURCE2} %{buildroot}%{_unitdir}/%{name}.service

%pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%license LICENSE
%doc README.md DCO %{name}.config.example.toml
%{_bindir}/%{name}
%{_unitdir}/%{name}.service
%dir %{_sysconfdir}/%{name}

%changelog
