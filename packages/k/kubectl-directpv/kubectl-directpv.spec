#
# spec file for package kubectl-directpv
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

Name:           kubectl-directpv
Version:        4.1.4
Release:        0
Summary:        Kubectl plugin for the MinIO CSI driver for Direct Attached Storage
License:        Apache-2.0
URL:            https://github.com/minio/directpv
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go1.22

%description
DirectPV is a CSI driver for Direct Attached Storage. In a simpler sense, it is
a distributed persistent volume manager, and not a storage system like SAN or
NAS. It is useful to discover, format, mount, schedule and monitor drives
across servers.

This package contains the Kubectl plugin to manage the DirectPV CSI driver.

%prep
%autosetup -a 1 -p 1

%build
go build \
   -mod=vendor \
   -buildmode=pie \
   -tags "osusergo netgo" \
   -ldflags="-X main.Version=v%{version}" \
   -o bin/%{name} ./cmd/kubectl-directpv

%install
# Install the binary.
install -D -m 0755 bin/%{name} "%{buildroot}/%{_bindir}/%{name}"

%check

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
