#
# spec file for package syft
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

Name:           syft
Version:        0.64.0
Release:        0
Summary:        CLI tool and library for generating a Software Bill of Materials
License:        Apache-2.0
URL:            https://github.com/anchore/syft
Source:         syft-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go >= 1.18

%description
A CLI tool and Go library for generating a Software Bill of Materials (SBOM) from container images and filesystems. Exceptional for vulnerability detection when used with a scanner like Grype.

%prep
%setup -q
%setup -q -T -D -a 1

%build
DATE_FMT="+%%Y-%%m-%%dT%%H:%%M:%%SZ"
BUILD_DATE=$(date -u -d "@${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u -r "${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u "${DATE_FMT}")
go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags="-X github.com/anchore/syft/internal/version.version=%{version} -X github.com/anchore/syft/internal/version.buildDate=$BUILD_DATE" \
   -o bin/syft ./cmd/syft

%install
# Install the binary.
install -D -m 0755 bin/%{name} "%{buildroot}/%{_bindir}/%{name}"

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
