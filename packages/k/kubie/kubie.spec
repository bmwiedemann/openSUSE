#
# spec file for package kubie
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


%global rustflags '-Clink-arg=-Wl,-z,relro,-z,now'

Name:           kubie
Version:        0.16.0
Release:        0
Summary:        A Kubernetes context switcher
License:        Zlib
URL:            https://github.com/sbstp/kubie
Source:         https://github.com/sbstp/kubie/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.xz
Source2:        cargo_config
Recommends:     fzf
BuildRequires:  cargo
BuildRequires:  rust

%description
kubie offers context switching, namespace switching and prompt modification in a
way that makes each shell independent from others. It also has support for
split configuration files, meaning it can load Kubernetes contexts from
multiple files. You can configure the paths where kubie will look for
contexts, see the settings section.

%prep
%autosetup -a1

mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
RUSTFLAGS=%{rustflags} cargo build --release

%install
RUSTFLAGS=%{rustflags} cargo install --root=%{buildroot}%{_prefix} --path .

# remove residue crate files
rm %{buildroot}%{_prefix}/.crates.toml
rm -f %{buildroot}%{_prefix}/.crates2.json

%files
%license LICENSE
%{_bindir}/%{name}

%changelog
