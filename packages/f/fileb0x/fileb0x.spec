#
# spec file for package fileb0x
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


Name:           fileb0x
Version:        v1.1.1~git10.d54f404
Release:        0
Summary:	Tool to embed files in go applications
License:        MIT
URL:            https://github.com/Velocidex/fileb0x
Source:         fileb0x-%{version}.tar.xz
Source1:	vendor.tar.xz
BuildRequires:  go

%description
A better customizable tool to embed files in go.

It is an alternative to `go-bindata` that have better features and organized configuration.

%prep
%setup -q -a 1

%build
go build -mod=vendor

%install
mkdir -p %buildroot/%{_bindir}
install -m 755 fileb0x %buildroot/%{_bindir}/

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/fileb0x

%changelog
