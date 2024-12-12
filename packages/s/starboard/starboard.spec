#
# spec file for package starboard
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

Name:           starboard
Version:        0.15.23
Release:        0
Summary:        Kubernetes-native security toolkit
License:        Apache-2.0
URL:            https://github.com/aquasecurity/starboard
Source:         starboard-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go >= 1.23

%description
Starboard integrates security tools into the Kubernetes environment, so that
users can find and view the risks that relate to different resources in a
Kubernetes-native way. Starboard provides custom resources definitions and a Go
module to work with a range of existing security scanners, as well as a
kubectl-compatible command, the Octant plugin, and the Lens extension that make
security reports available through familiar Kubernetes tools.

%prep
%autosetup -p 1 -a 1

%build
go build -mod=vendor \
   -o ./bin/starboard ./cmd/starboard/main.go
go build -mod=vendor \
   -o ./bin/starboard-operator ./cmd/starboard-operator/main.go
go build -mod=vendor \
   -o ./bin/starboard-scanner-aqua ./cmd/scanner-aqua/main.go

%install
# Install the binary.
ls -lah
install -D -m 0755 ./bin/%{name} "%{buildroot}/%{_bindir}/%{name}"
install -D -m 0755 ./bin/starboard-operator "%{buildroot}/%{_bindir}/starboard-operator"
install -D -m 0755 ./bin/starboard-scanner-aqua "%{buildroot}/%{_bindir}/starboard-scanner-aqua"

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_bindir}/starboard-operator
%{_bindir}/starboard-scanner-aqua

%changelog
