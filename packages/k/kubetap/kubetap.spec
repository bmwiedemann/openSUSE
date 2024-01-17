#
# spec file for package kubetap
#
# Copyright (c) 2021 SUSE LLC
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

Name:           kubetap
Version:        0.1.4
Release:        0
Summary:        Kubectl plugin to interactively proxy Kubernetes Services with ease
License:        Apache-2.0
URL:            https://github.com/soluble-ai/kubetap
Source:         kubetap-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go >= 1.13

%description
Kubetap is a kubectl plugin that enables an operator to easily deploy intercepting proxies for Kubernetes Services.

%prep
%setup -q
%setup -q -T -D -a 1

%build
#go generate
go build \
    -mod=vendor \
    ./cmd/kubectl-tap

%install
# Install the binary.
install -D -m 0755 kubectl-tap "%{buildroot}/%{_bindir}/kubectl-tap"

%files
%defattr(-,root,root)
%doc README.md
%license LICENSE
%{_bindir}/kubectl-tap

%changelog
