#
# spec file for package golangci-lint
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           golangci-lint
Version:        2.10.1
Release:        0
Summary:        A fast Go linters runner
License:        GPL-3.0-only
URL:            https://golangci-lint.run
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang(API) >= 1.25

%description
golangci-lint is a fast Go linters runner. It runs linters in parallel, uses
caching, supports yaml config, has integrations with all major IDE and has
dozens of linters included.

%prep
%autosetup -a 1

%build
%ifnarch ppc64
export GOFLAGS="-buildmode=pie -trimpath"
%endif
export BUILDDATE=$(date -d @${SOURCE_DATE_EPOCH:-$(date +%%s)} +%Y-%m-%d)
go build \
    -ldflags "-s -w -X main.version=%{version} -X main.commit=OpenBuildService -X main.date=$BUILDDATE" \
    ./cmd/%{name}

%check
# execute the binary as a basic check
./%{name} --version | grep -q "%{version}"

%install
install -D -m 0755 %{name} "%{buildroot}/%{_bindir}/%{name}"

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
