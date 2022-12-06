#
# spec file for package kyverno
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


%define __arch_install_post export NO_BRP_STRIP_DEBUG=true

Name:           kyverno
Version:        1.8.3
Release:        0
Summary:        CLI and kubectl plugin for Kyverno
License:        Apache-2.0
URL:            https://github.com/kyverno/kyverno
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go >= 1.17

%description
Kyverno is a policy engine designed for Kubernetes. It can validate, mutate, and generate configurations using admission controls and background scans. Kyverno policies are Kubernetes resources and do not require learning a new language. Kyverno is designed to work nicely with tools you already use like kubectl, kustomize, and Git.

%prep
%setup -q
%setup -q -T -D -a 1

%build
DATE_FMT="+%%Y-%%m-%%dT%%H:%%M:%%SZ"
BUILD_DATE=$(date -u -d "@${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u -r "${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u "${DATE_FMT}")
go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags="-s -w -X github.com/kyverno/kyverno/pkg/version.BuildVersion=%{version} -X github.com/kyverno/kyverno/pkg/version.BuildHash=%{version} -X github.com/kyverno/kyverno/pkg/version.BuildTime=$BUILD_DATE" \
   -o bin/kyverno ./cmd/cli/kubectl-kyverno

%install
# Install the binary.
install -D -m 0755 bin/%{name} %{buildroot}/%{_bindir}/%{name}
cd %{buildroot}/%{_bindir}/
ln -s %{name} kubectl-%{name}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_bindir}/kubectl-%{name}

%changelog
