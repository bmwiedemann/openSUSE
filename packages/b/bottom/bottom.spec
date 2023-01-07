#
# spec file for package bottom
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2020-2021, Martin Hauke <mardnh@gmx.de>
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
Version:        0.7.1~0
Release:        0
Summary:        Yet another graphical process/system monitor
License:        MIT
Group:          System/Monitoring
URL:            https://github.com/ClementTsang/bottom
Source:         %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
Source2:        cargo_config
BuildRequires:  cargo-packaging
BuildRequires:  zstd

%description
A cross-platform graphical process/system monitor with a
customizable interface and a multitude of features.

%prep
%autosetup -p 1 -a 1
install -D -m 0644 %{SOURCE2} .cargo/config

%build
cargo build --release --locked %{?_smp_mflags}

%install
cargo install --no-track --root=%{buildroot}%{_prefix} --path .

%check
%{cargo_test}

%files
%license LICENSE
%doc CHANGELOG.md README.md
%doc sample_configs/*
%{_bindir}/btm

%changelog
