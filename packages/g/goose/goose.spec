#
# spec file for package goose
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


Name:           goose
Version:        1.14.0
Release:        0
Summary:        A local, extensible, open source AI agent that automates engineering tasks
License:        Apache-2.0
URL:            https://github.com/block/goose
Source0:        goose-%{version}.tar.zst
Source1:        vendor.tar.zst
Patch1:         disable-self-update.patch
BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  libxcb-devel
BuildRequires:  protobuf-devel

%description
Goose is an extensible open source AI agent that enhances your software development by automating coding tasks.

%prep
%autosetup -a1 -p0

%build
# optimize binary
export CARGO_REGISTRIES_CRATES_IO_PROTOCOL=sparse
export CARGO_PROFILE_RELEASE_LTO=true
export CARGO_PROFILE_RELEASE_CODEGEN_UNITS=1
export CARGO_PROFILE_RELEASE_OPT_LEVEL=z

%{cargo_build} --package goose-cli

%install
mkdir -p %{buildroot}%{_bindir}

install -m 0755 %{_builddir}/%{name}-%{version}/target/release/%{name} %{buildroot}%{_bindir}/%{name}

%check
# basic check
%{buildroot}%{_bindir}/%{name} info

# check if self update subcommand is disabled
%{buildroot}%{_bindir}/%{name} update || echo "self update is disabled!"

%files
%license LICENSE
%{_bindir}/%{name}

%changelog
