#
# spec file for package ttl
#
# Copyright (c) 2026, Martin Hauke <mardnh@gmx.de>
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


Name:           ttl
Version:        0.15.1
Release:        0
Summary:        Modern traceroute/mtr-style TUI
License:        Apache-2.0 OR MIT
URL:            https://github.com/lance0/ttl
#Git-Clone:     https://github.com/lance0/ttl.git
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
Requires(post): permissions
Recommends:     bash-completion

%description
ttl provides a live traceroute interface that can trace multiple targets,
detect ECMP paths, run PMTUD, export JSON/CSV reports, and optionally
enrich hop data with DNS, ASN, geolocation, and PeeringDB information.

%prep
%autosetup -p 1 -a 1

%build
%{cargo_build}

%install
%{cargo_install}

%verifyscript
%verify_permissions -e %{_bindir}/ttl

%post
%set_permissions %{_bindir}/ttl

%check
%{cargo_test}

%files
%license LICENSE-APACHE LICENSE-MIT
%doc CHANGELOG.md README.md
%verify(not mode caps) %attr(0755,root,root) %caps(cap_net_raw,cap_net_admin=ep) %{_bindir}/ttl

%changelog
