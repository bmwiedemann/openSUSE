#
# spec file for package golangci-lint
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


%define __arch_install_post export NO_BRP_STRIP_DEBUG=true
# approximate build date for display in golangci-lint version output, exact
# timemstap can be obtained by doing an rpm query

Name:           golangci-lint
Version:        1.52.1
Release:        0
Summary:        A fast Go linters runner
License:        GPL-3.0-only
URL:            https://golangci-lint.run
Source0:        %{name}-%{version}.tar.xz
Source1:        vendor.tar.xz
BuildRequires:  go
BuildRequires:  go-md2man

%description
golangci-lint is a fast Go linters runner. It runs linters in parallel, uses
caching, supports yaml config, has integrations with all major IDE and has
dozens of linters included.

%prep
%setup -q
%setup -q T -D -a 1

%build
# Build the binary, use PIE unless on PPC64
release_build_date=$(date -u -d @${SOURCE_DATE_EPOCH:-$(date +%%s)} +"%%Y-%%m-%%d")
go build \
   -mod=vendor \
%ifnarch ppc64
   -buildmode=pie \
%endif
   -ldflags "-s -w -X main.date=${release_build_date}" \
   -o %{name} \
   cmd/%{name}/main.go

%install
install -D -m 0755 %{name} "%{buildroot}/%{_bindir}/%{name}"

# Build the man pages.
go-md2man -in README.md -out %{name}.1

# Install the man pages.
mkdir -p "%{buildroot}/%{_mandir}/man1"
install -D -m 0644 %{name}.1 "%{buildroot}/%{_mandir}/man1"

%files
%doc README.md
%if 0%{?suse_version} < 1500
%doc LICENSE
%else
%license LICENSE
%endif
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*.1.gz

%changelog
