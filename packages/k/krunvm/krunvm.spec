#
# spec file for package krunvm
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


Name:           krunvm
Version:        0.2.3+git12dac81
Release:        0
Summary:        Manage lightweight VMs created from OCI images
License:        Apache-2.0
URL:            https://github.com/containers/krunvm
Source0:        krunvm-%{version}.tar.gz
Source1:        vendor.tar.zst
Source2:        cargo_config
ExclusiveArch:  x86_64 aarch64
BuildRequires:  cargo-packaging
BuildRequires:  libkrun-devel
BuildRequires:  zstd
BuildRequires:  rubygem(asciidoctor)
Requires:       buildah
Requires:       libkrun1 >= 1.4.4
Conflicts:      libkrun0

%description
Manage lightweight VMs created from OCI images

%files
%doc README.md
%{_bindir}/krunvm

%prep
%setup -qa1
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
export RUSTFLAGS="%{__rustflags}"
%make_build

%install
export RUSTFLAGS="%{__rustflags}"
%make_install PREFIX=%{_prefix}

%changelog
