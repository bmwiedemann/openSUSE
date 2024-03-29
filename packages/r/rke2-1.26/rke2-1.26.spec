#
# spec file for package rke2-1.26
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
%define binary_name rke2

Name:           rke2-1.26
Version:        1.26.15+rke2r1
Release:        0
Summary:        Rancher Kubernetes Engine
License:        Apache-2.0
URL:            https://github.com/rancher/rke2
Source:         rke2-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go >= 1.19
Provides:       rke2 = %{version}-%{release}
Conflicts:      rke2 < 1.26
Conflicts:      rke2 > 1.27

%description
RKE2, also known as RKE Government, is Rancher's next-generation Kubernetes distribution.
It is a fully conformant Kubernetes distribution that focuses on security and compliance within the U.S. Federal Government sector.

To meet these goals, RKE2 does the following:
    Provides defaults and configuration options that allow clusters to pass the CIS Kubernetes Benchmark with minimal operator intervention
    Enables FIPS 140-2 compliance
    Supports SELinux policy and Multi-Category Security (MCS) label enforcement
    Regularly scans components for CVEs using trivy in our build pipeline

%prep
%setup -q -n rke2-%{version}
%setup -q -T -D -a 1 -n rke2-%{version}

%build
go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags="-X main.Version=%{version}"

%install
# Install the binary.
install -D -m 0755 %{binary_name} "%{buildroot}/%{_bindir}/%{binary_name}"

%files
%defattr(-,root,root)
%doc README.md
%license LICENSE
%{_bindir}/%{binary_name}

%changelog
