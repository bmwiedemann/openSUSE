#
# spec file for package efm-langserver
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


Name:           efm-langserver
Version:        0.0.49
Release:        0
Summary:        General purpose language server
License:        MIT
URL:            https://github.com/mattn/efm-langserver
Source0:        https://github.com/mattn/efm-langserver/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  c_compiler
BuildRequires:  zstd
BuildRequires:  golang(API) >= 1.20

%description
General purpose Language Server that can use specified error message format generated from specified command e.g.
using linters and other tooling that supports the LSP specification.

%prep
%setup -qa1

%build
%ifarch ppc64
BUILDMOD=""
%else
BUILDMOD="-buildmode=pie"
%endif
export RPM_OPT_FLAGS="%{optflags}"
go build -v -x -mod=vendor $BUILDMOD -a -ldflags "-s -X main.version=%{version} -X main.revision=%{version}" -o %{name}

%install
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%license LICENSE
%doc README.md

%changelog
