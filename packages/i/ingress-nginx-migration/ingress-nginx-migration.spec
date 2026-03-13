#
# spec file for package ingress-nginx-migration
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


Name:           ingress-nginx-migration
Version:        1.0.0
Release:        0
Summary:        Analyze Kubernetes NGINX Ingress resources to help with migration to Traefik
License:        Apache-2.0
URL:            https://ingressnginxmigration.org
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang(API) >= 1.24

%description
The Ingress NGINX Migration is a tool that analyzes Kubernetes NGINX Ingress
resources to help with migration planning to Traefik.

The Ingress NGINX Migration tool creates and serves an interactive HTML report,
and to do so it:

- Analyzes all Ingress resources in a Kubernetes cluster or specific namespaces
- Identifies Ingress NGINX Controller annotations and their compatibility with
  Traefik
- Supports both in-cluster deployment and external kubeconfig access
- Generates timestamped migration HTML report showing:
  - Total number of Ingress resources
  - How many can be migrated automatically
  - Which Ingress resources need manual attention
  - Unsupported annotations and their frequency
- Provides flexible ingress filtering by controller class, ingress class name,
  and namespace

%prep
%autosetup -p 1 -a 1

%build
COMMIT_HASH="$(sed -n 's/commit: \(.*\)/\1/p' %_sourcedir/%{name}.obsinfo)"

DATE_FMT="+%%Y-%%m-%%dT%%H:%%M:%%SZ"
BUILD_DATE=$(date -u -d "@${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u -r "${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u "${DATE_FMT}")
go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags=" \
   -X github.com/traefik/ingress-nginx-migration/pkg/version.Version=%{version} \
   -X github.com/traefik/ingress-nginx-migration/pkg/version.BuildDate=${BUILD_DATE}" \
   -o bin/%{name} ./cmd

%install
# Install the binary.
install -D -m 0755 bin/%{name} %{buildroot}/%{_bindir}/%{name}

%check
%{buildroot}/%{_bindir}/%{name} version
%{buildroot}/%{_bindir}/%{name} version | grep %{version}

%files
%doc readme.md
%license LICENSE
%{_bindir}/%{name}

%changelog
