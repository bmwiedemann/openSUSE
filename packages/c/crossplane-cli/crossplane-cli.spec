#
# spec file for package crossplane-cli
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


%define __arch_install_post export NO_BRP_STRIP_DEBUG=true

%define executable_name crossplane

Name:           crossplane-cli
Version:        1.18.1
Release:        0
Summary:        The Cloud Native Control Plane
License:        Apache-2.0
URL:            https://github.com/crossplane/crossplane
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go >= 1.20
Provides:       crossplane = %{version}

%description
Crossplane is a framework for building cloud native control planes without
needing to write code. It has a highly extensible backend that enables you to
build a control plane that can orchestrate applications and infrastructure no
matter where they run, and a highly configurable frontend that puts you in
control of the schema of the declarative API it offers.

Crossplane is a Cloud Native Computing Foundation project.

%prep
%autosetup -p 1 -a 1

%build
DATE_FMT="+%%Y-%%m-%%dT%%H:%%M:%%SZ"
BUILD_DATE=$(date -u -d "@${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u -r "${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u "${DATE_FMT}")
go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags="-X github.com/crossplane/crossplane/internal/version.version=%{version}" \
   -o bin/%{executable_name} ./cmd/crossplane

%install
install -D -m 0755 bin/%{executable_name} %{buildroot}/%{_bindir}/%{executable_name}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{executable_name}

%changelog
