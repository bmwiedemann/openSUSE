#
# spec file for package kubepug
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

Name:           kubepug
Version:        1.7.1
Release:        0
Summary:        Kubernetes PreUpGrade (Checker)
License:        Apache-2.0
URL:            https://github.com/kubepug/kubepug
Source:         kubepug-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go >= 1.21
Provides:       kubectl-deprecations

%description
KubePug/Deprecations is intended to be a kubectl plugin, which:

- Downloads a swagger.json from a specific Kubernetes version
- Parses this Json finding deprecation notices
- Verifies the current kubernetes cluster or input files checking whether exists objects in this deprecated API Versions, allowing the user to check before migrating

%prep
%autosetup -p 1 -a 1

%build
DATE_FMT="+%%Y-%%m-%%dT%%H:%%M:%%SZ"
BUILD_DATE=$(date -u -d "@${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u -r "${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u "${DATE_FMT}")
go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags="-X sigs.k8s.io/release-utils/version.gitVersion=v%{version}\
   -X sigs.k8s.io/release-utils/version.gitTreeState=clean \
   -X sigs.k8s.io/release-utils/version.gitCommit=v%{version} \
   -X sigs.k8s.io/release-utils/version.buildDate=$BUILD_DATE" \
   -o bin/kubepug .

%install
# Install the binary.
install -D -m 0755 bin/%{name} "%{buildroot}/%{_bindir}/%{name}"
cd %{buildroot}/%{_bindir}/
ln -s %{name} kubectl-deprecations

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_bindir}/kubectl-deprecations

%changelog
