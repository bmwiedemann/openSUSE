#
# spec file for package name
#
# Copyright (c) 2022 SUSE LLC
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


Name:           golang-github-google-jsonnet
Version:        0.20.0
Release:        0
Summary:        Jsonnet implementation in pure Go
License:        Apache-2.0
URL:            https://opensuse.org
Source:         %{name}-%{version}.tar.xz
Source1:        vendor.tar.gz
BuildRequires:  golang-packaging
Provides:       jsonnet
Conflicts:      jsonnet
%{go_nostrip}

%description
Feature complete, production-ready implementation of Jsonnet. It is compatible with the original
Jsonnet C++ implementation.

%prep
%autosetup -p1 -a1

%build
go build \
   -mod=vendor \
   -buildmode=pie \
   ./cmd/jsonnet

go build \
   -mod=vendor \
   -buildmode=pie \
   ./cmd/jsonnetfmt


go build \
   -mod=vendor \
   -buildmode=pie \
   ./cmd/jsonnet-lint

%install
install -D -m0755 %{_builddir}/%{name}-%{version}/jsonnet %{buildroot}%{_bindir}/jsonnet
install -D -m0755 %{_builddir}/%{name}-%{version}/jsonnetfmt %{buildroot}%{_bindir}/jsonnetfmt
install -D -m0755 %{_builddir}/%{name}-%{version}/jsonnet-lint %{buildroot}%{_bindir}/jsonnet-lint

%files
%license LICENSE
%doc README.md
%{_bindir}/jsonnet
%{_bindir}/jsonnetfmt
%{_bindir}/jsonnet-lint

%changelog
