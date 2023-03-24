#
# spec file for package parsec-tool
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


%global rustflags '-Clink-arg=-Wl,-z,relro,-z,now'
%define archive_version 0.6.0-rc1

%{?systemd_ordering}
Name:           parsec-tool
Version:        0.6.0~rc1
Release:        0
Summary:        Platform AbstRaction for SECurity
License:        Apache-2.0
URL:            https://github.com/parallaxsecond/parsec-tool
Source0:        https://github.com/parallaxsecond/parsec-tool/archive/%{archive_version}.tar.gz#/parsec-tool-%{archive_version}.tar.gz
Source1:        vendor.tar.xz
Source2:        cargo_config
BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  protobuf-devel
Requires:       parsec
ExcludeArch:    %{ix86} armv6l armv6hl

%description
A tool to communicate with the Parsec service on the command-line.

%prep
%setup -qa1 -n parsec-tool-%{archive_version}
rm -rf .cargo && mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
export PROTOC=/usr/bin/protoc
%cargo_build

%install
%cargo_install
# Install parsec-tool in the right directory
mkdir %{buildroot}%{_bindir} && mv .cargo/bin/* %{buildroot}%{_bindir}
# Clean-up
find %{buildroot} -name .crates2.json -delete
rm -rf %{buildroot}%{_datadir}/cargo/registry

%files
%license LICENSE
%doc README.md
%{_bindir}/parsec-tool

%changelog
