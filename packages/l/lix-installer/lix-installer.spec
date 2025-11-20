#
# spec file for package lix-installer
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define __rustflags --cfg tokio_unstable

Name:           lix-installer
Version:        2.94.0
Release:        0
Summary:        The easiest way to install Lix
License:        LGPL-2.1-only
URL:            https://git.lix.systems/lix-project/lix-installer
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  zstd
ExclusiveArch:  x86_64

%description
A fast, friendly, and reliable tool to help you use Lix, the community implementation of the nix tooling.

%prep
%autosetup -a 1 -p 1

%build
%{cargo_build}

%install
install -D -d -m 0755 %{buildroot}%{_bindir}
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/%{name} %{buildroot}%{_bindir}/%{name}

%check
%{cargo_test}

%files
%{_bindir}/lix-installer

%changelog
