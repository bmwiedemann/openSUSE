#
# spec file for package sndiff
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


%global rustflags '-Clink-arg=-Wl,-z,relro,-z,now'
Name:           sndiff
Version:        0.2.1~0
Release:        0
Summary:        Tool for diffing packages and files from snapshots
License:        MIT
URL:            https://github.com/aplanas/sndiff
Source:         %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
Source2:        config.toml
Source3:        sndiff.8.md
BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  go-md2man

%description
Small tool to get diff information of packages and files in /etc from
different snapshots

%prep
%autosetup -a1 -p1
mkdir .cargo
install -D -m 644 %{SOURCE2} .cargo/config.toml

%build
sed -i 's/edition = "2024"/edition = "2018"/' Cargo.toml
%{cargo_build}
go-md2man -in %{SOURCE3} -out sndiff.8

%install
%{cargo_install}
install -D -m 644 sndiff.8 %{buildroot}%{_mandir}/man8/sndiff.8

# %_check
# %_{cargo_test}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man8/sndiff.8%{?ext_man}

%changelog
