#
# spec file for package gopls
#
# Copyright (c) 2024 SUSE LLC
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


Name:           gopls
Version:        0.16.1
Release:        0
Summary:        Go LSP protocol language server
License:        Apache-2.0 AND MIT AND BSD-3-Clause
Group:          Development/Tools/Other
URL:            https://pkg.go.dev/golang.org/x/tools/gopls
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang(API) >= 1.18

%description
gopls (pronounced "Go please") is the official Go language server developed
by the Go team. It provides IDE features to any LSP-compatible editor.

%prep
%autosetup -a 1
# Upstream Go x/tools monorepo has a subdir per tool.
# Unlike most Go applications at the repository root,
# package x/tools sources as subdir/ so we can include
# LICENSE file from monorepo top level dir.
mv LICENSE %{name}
# vendor dir must also be moved to subdir to be detected
mv vendor %{name}

%build
# Change to subdir, see comment in prep phase
cd %{name}
%ifnarch ppc64
export GOFLAGS="-buildmode=pie"
%endif
go build

%check
# Account for subdir, see comment in prep phase
# Execute the binary as a basic check
./%{name}/%{name} --help

%install
# Account for subdir, see comment in prep phase
install -D -m 0755 %{name}/%{name} "%{buildroot}/%{_bindir}/%{name}"

%files
# Account for subdir, see comment in prep phase
%doc %{name}/README.md
%license %{name}/LICENSE
%{_bindir}/%{name}

%changelog
