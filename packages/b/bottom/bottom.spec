#
# spec file for package bottom
#
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


Name:           bottom
Version:        0.4.1
Release:        0
Summary:        Yet another graphical process/system monitor
License:        MIT
Group:          System/Monitoring
URL:            https://github.com/ClementTsang/bottom
Source:         https://github.com/ClementTsang/bottom/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.xz
BuildRequires:  cargo
BuildRequires:  rust

%description
A cross-platform graphical process/system monitor with a
customizable interface and a multitude of features.

%prep
%setup -qa1
mkdir .cargo
cat >.cargo/config <<EOF
[source.crates-io]
registry = 'https://github.com/rust-lang/crates.io-index'
replace-with = 'vendored-sources'
[source.vendored-sources]
directory = './vendor'
EOF

%build
cargo build --release --locked %{?_smp_mflags}

%install
cargo install --no-track --root=%{buildroot}%{_prefix} --path .

%files
%license LICENSE
%doc CHANGELOG.md README.md
%doc sample_configs/*
%{_bindir}/btm

%changelog
