#
# spec file for package obs-service-cargo_audit
#
# Copyright (c) 2021 SUSE LLC
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


%define service cargo_audit
Name:           obs-service-%{service}
Summary:        An OBS source service: Audit vendored Rust crates for security issues
License:        MPL-2.0
Group:          Development/Tools/Building
URL:            https://github.com/openSUSE/obs-service-%{service}
Version:        0.1.2~git0.e25df37
Release:        0
Source:         %{name}-%{version}.tar.gz
BuildRequires:  python3
Requires:       cargo-audit
Requires:       cargo-audit-advisory-db
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
An OBS Source Service that will audit vendored Rust
crates (libraries) for security issues

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_prefix}/lib/obs/service
mkdir -p %{buildroot}%{_prefix}/lib/obs/service
install -m 0755 %{service} %{buildroot}%{_prefix}/lib/obs/service
install -m 0644 %{service}.service %{buildroot}%{_prefix}/lib/obs/service

%files
%defattr(-,root,root)
%doc README.md
%dir %{_prefix}/lib/obs
%{_prefix}/lib/obs/service

%changelog
