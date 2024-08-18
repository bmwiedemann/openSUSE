#
# spec file for package kubectl-dup
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

Name:           kubectl-dup
Version:        0.3.2
Release:        0
Summary:        Kubectl plugin for duplication of existing kubernetes resources
License:        MIT
URL:            https://github.com/vash/dup
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go >= 1.22

%description
This plugin is designed for on-the-fly duplication of Kubernetes resources. It
focuses on providing a convenient way to edit resources before duplication,
with a specific emphasis on Pods to create a fine-tuned resource quickly. This
tool can be used for debugging running containers without them crashing, and
simplifying the administration and general interaction with Kubernetes
clusters.

%prep
%autosetup -p 1 -a 1

%build
go build \
   -mod=vendor \
   -buildmode=pie \
   -o bin/%{name}

%install
# Install the binary.
install -D -m 0755 bin/%{name} %{buildroot}/%{_bindir}/%{name}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
