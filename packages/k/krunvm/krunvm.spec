#
# spec file for package krunvm
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


Name:           krunvm
Version:        0.1.4+git5add8c5
Release:        0
Summary:        Manage lightweight VMs created from OCI images
License:        Apache-2.0
URL:            https://github.com/containers/krunvm
Source0:        krunvm-%{version}.tar.gz
Source1:        vendor.tar.xz
Source2:        cargo_config
ExclusiveArch:  x86_64 aarch64
BuildRequires:  cargo-packaging
BuildRequires:  libkrun >= 0.1.7
Requires:       buildah
Conflicts:      libkrun-devel
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
