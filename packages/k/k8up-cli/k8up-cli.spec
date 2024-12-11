#
# spec file for package k8up-cli
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

%define executable_name k8up

Name:           k8up-cli
Version:        2.11.2
Release:        0
Summary:        CLI for the K8up Kubernetes and OpenShift Backup Operator
License:        Apache-2.0
URL:            https://github.com/k8up-io/k8up
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go >= 1.21

%description
K8up is a Kubernetes backup operator based on Restic that will handle PVC and
application backups on a Kubernetes or OpenShift cluster.

Just create a schedule and a credentials object in the namespace you’d like to
backup. It’s that easy. K8up takes care of the rest. It also provides a
Prometheus endpoint for monitoring.

K8up is production ready. It is used in production deployments since 2019.

This package contains the CLI.

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
   -X main.version=v%{version} \
   -X main.commit=${COMMIT_HASH} \
   -X main.date=${BUILD_DATE}" \
   -o bin/%{executable_name} ./cmd/%{executable_name}

%install
# Install the binary.
install -D -m 0755 bin/%{executable_name} %{buildroot}/%{_bindir}/%{executable_name}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{executable_name}

%changelog
