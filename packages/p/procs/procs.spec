#
# spec file for package procs
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


Name:           procs
Version:        0.14.0
Release:        0
Summary:        A modern replacement for ps written in Rust
License:        MIT
URL:            https://github.com/dalance/procs
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
Source2:        cargo_config
BuildRequires:  cargo-packaging

%description
procs is a replacement for ps written in Rust.

%prep
%setup -qa1
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
%{cargo_build}

%install
%{cargo_install}

%check
%{cargo_test}

%files
%license LICENSE
%doc README.md
%{_bindir}/procs

%changelog
