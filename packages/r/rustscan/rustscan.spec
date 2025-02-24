#
# spec file for package rustscan
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2020, Martin Hauke <mardnh@gmx.de>
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


Name:           rustscan
Version:        2.4.1+0
Release:        0
Summary:        Fast network port scanner
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Diagnostic
URL:            https://github.com/RustScan/RustScan
Source:         RustScan-%{version}.tar.xz
Source1:        vendor.tar.xz
BuildRequires:  cargo-packaging
BuildRequires:  python3
Recommends:     nmap

%description
Find all open ports fast with RustScan, then automatically
pipe them into Nmap.

%prep
%setup -qa1 -n RustScan-%{version}

%build
%{cargo_build}

%install
%{cargo_install}

%check
%{cargo_test} -- \
  --skip address::tests::parse_correct_host_addresses \
  --skip address::tests::parse_hosts_file_and_incorrect_hosts \
  --skip address::tests::resolver_args_google_dns \
  --skip address::tests::resolver_default_cloudflare

%files
%license LICENSE
%doc README.md
%{_bindir}/rustscan

%changelog
