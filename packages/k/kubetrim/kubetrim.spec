#
# spec file for package kubetrim
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

Name:           kubetrim
Version:        0.0.1
Release:        0
Summary:        Trim your KUBECONFIG automatically
License:        MIT
URL:            https://github.com/alexellis/kubetrim
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go >= 1.22

%description
Tidy up old Kubernetes clusters from kubeconfig.

kubetrim tries to connect to each cluster in the current kubeconfig file, and
removes any that are unreachable, or which error.

%prep
%autosetup -p 1 -a 1

%build
COMMIT_HASH="$(sed -n 's/commit: \(.*\)/\1/p' %_sourcedir/%{name}.obsinfo)"

go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags=" \
   -X github.com/alexellis/kubetrim/pkg.Version=%{version} \
   -X github.com/alexellis/kubetrim/pkg.GitCommit=${COMMIT_HASH}" \
   -o bin/%{name}

%install
# Install the binary.
install -D -m 0755 bin/%{name} %{buildroot}/%{_bindir}/%{name}

%check
CGO_ENABLED=0 go test $(go list ./... | grep -v /vendor/|xargs echo) -cover

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
