#
# spec file for package snphost
#
# Copyright (c) 2025 SUSE LLC
# Copyright (C) 2023 VirTEE
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


Name:           snphost
Version:        0.7.0
Release:        0
Summary:        A Rust command-line tool for interacting with the AMD Secure Processor
License:        Apache-2.0
Group:          Productivity/Security
URL:            https://github.com/virtee/snphost
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  openssl-devel
BuildRequires:  rubygem(asciidoctor)
ExclusiveArch:  x86_64

%description
snphost is a command line utility for interacting with the AMD Secure Encrypted Virtualization - Secure Nested Paging (SEV-SNP) host environment (via the /dev/sev device).

%prep
# The number passed to -a (a stands for "after") should be equivalent to the Source tag number
# of the vendor tarball, 1 in this case (from Source1).
%autosetup -a1

%build
%{cargo_build}

%install
%{cargo_install}

%check
%{cargo_test}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
