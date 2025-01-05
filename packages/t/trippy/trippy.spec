#
# spec file for package trippy
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


Name:           trippy
Version:        0.12.2
Release:        0
Summary:        A network diagnostic tool
License:        Apache-2.0
Group:          Productivity/Networking/Diagnostic
URL:            https://github.com/fujiapple852/trippy
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging

%description
Trippy combines the functionality of traceroute and ping and is designed
to assist with the analysis of networking issues.

%prep
%autosetup -a 1

%build
%{cargo_build}

%install
install -D -m 755 -t "%{buildroot}/%{_sbindir}" target/release/trip
install -D -m 644 -t "%{buildroot}/%{_docdir}/%{name}" README.md trippy-config-sample.toml

%files
%doc README.md trippy-config-sample.toml
%license LICENSE
%{_sbindir}/trip

%changelog
