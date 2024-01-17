#
# spec file
#
# Copyright (c) 2023 SUSE LLC
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
Version:        0.1.8~6
Release:        0
Source:         %{name}-%{version}.tar.xz
Source99:       obs-service-cargo_audit-rpmlintrc
BuildRequires:  cargo-packaging
BuildRequires:  python3 >= 3.8
Requires:       cargo-audit
Requires:       cargo-audit-advisory-db
Requires:       python3 >= 3.8
ExclusiveArch:  %{rust_tier1_arches}

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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
