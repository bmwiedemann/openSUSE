#
# spec file for package obs-service-cargo
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


Name:           obs-service-cargo
Summary:        OBS Source Service and utilities for Rust software packaging
License:        MPL-2.0
Group:          Development/Tools/Building
# Repository name subject to change
URL:            https://github.com/openSUSE-Rust/%{name}
Version:        5.1.0
Release:        0
Source0:        https://github.com/openSUSE-Rust/%{name}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  pkgconfig(libzstd)
# Version with fixed vendor filterer
Requires:       cargo-vendor-filterer >= 0.5.16
Requires:       (cargo or rustup)
# At 0.6.0, vendor was introduced so we obsolete versions before that
Conflicts:      obs-service-cargo_vendor
Obsoletes:      obs-service-cargo_vendor
Provides:       obs-service-cargo_vendor = %{version}
# At 0.7.0, audit was introduced so we obsolete versions before that
Conflicts:      obs-service-cargo_audit
Obsoletes:      obs-service-cargo_audit
Provides:       obs-service-cargo_audit = %{version}

%description
This is an OBS Source Service that contains two main utilities:
- OBS Service Cargo Vendor
- OBS Service Cargo Vendor Home Registry

This vendors and audits dependencies for packaging Rust software.

See the <https://github.com/openSUSE-Rust/obs-service-cargo/blob/master/README.md>
for full documentation.

%prep
%autosetup -a1

%build
%{cargo_build}

%install
mkdir -p %{buildroot}%{_prefix}/lib/obs/service
install -m0755 %{_builddir}/%{name}-%{version}/target/release/cargo_vendor %{buildroot}%{_prefix}/lib/obs/service
# This will get removed in the future.
install -m0755 %{_builddir}/%{name}-%{version}/target/release/cargo_audit  %{buildroot}%{_prefix}/lib/obs/service
install -m0644 cargo_vendor.service %{buildroot}%{_prefix}/lib/obs/service

%files
%defattr(-,root,root)
%doc README.md CHANGELOG.md CONTRIBUTING.md CODE_OF_CONDUCT.md
%license LICENSE
%dir %{_prefix}/lib/obs
%{_prefix}/lib/obs/service

%changelog
