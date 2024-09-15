#
# spec file for package k3kcli
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

Name:           k3kcli
Version:        0.2.1
Release:        0
Summary:        Kubernetes in Kubernetes
License:        Apache-2.0
URL:            https://github.com/rancher/k3k
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go >= 1.22

%description
A Kubernetes in Kubernetes tool, k3k provides a way to run multiple embedded
isolated k3s clusters on your kubernetes cluster.

%prep
%autosetup -p 1 -a 1

%build
# hash will be shortended by COMMIT_HASH:0:8 later
COMMIT_HASH="$(sed -n 's/commit: \(.*\)/\1/p' %_sourcedir/%{name}.obsinfo)"
go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags=" \
   -X github.com/rancher/k3k.Version=v%{version} \
   -X github.com/rancher/k3k.GitCommit=${COMMIT_HASH:0:8}" \
   -o bin/%{name} ./cli

%install
# Install the binary.
install -D -m 0755 bin/%{name} %{buildroot}/%{_bindir}/%{name}

%check
bin/%{name} --version

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
