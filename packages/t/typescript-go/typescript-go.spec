#
# spec file for package typescript-go
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


%global         provider_prefix github.com/microsoft/typescript-go
%global         import_path     %{provider_prefix}
Name:           typescript-go
Version:        0.0.1245
Release:        0
Summary:        Port of TypeScript compiler to go
License:        Apache-2.0
Group:          Development/Tools/Building
URL:            https://github.com/microsoft/typescript-go
Source0:        typescript-go-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  golang(API) >= 1.24
BuildRequires:  golang-packaging
BuildRequires:  zstd

%description
typescript-go is an experimental port of the TypeScript compiler to Go.

%prep
%autosetup -a1

%build
%{goprep} %{import_path}
%{gobuild} -mod=vendor ./cmd/tsgo

%install
%{goinstall}

%check
%{gotest} ./...

%files
%license LICENSE
%doc README.md
%{_bindir}/tsgo

%changelog
