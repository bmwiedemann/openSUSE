#
# spec file for package kubectl-view-secret
#
# Copyright (c) 2025 SUSE LLC and contributors
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


# to be recognized as a kubectl plugin,
# there must not be a hyphen in the plugin name
%define executable_name kubectl-view_secret

Name:           kubectl-view-secret
Version:        0.15.1
Release:        0
Summary:        Kubernetes CLI plugin to decode Kubernetes secrets
License:        MIT
URL:            https://github.com/elsesiy/kubectl-view-secret
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go1.25 >= 1.25.4

%description
This plugin allows for easy secret decoding. Useful if you want to see what's
inside of a secret without always go through the following:

* kubectl get secret <secret> -o yaml
* Copy base64 encoded secret
* echo "b64string" | base64 -d

%prep
%autosetup -p1 -a 1

%build
go build \
   -mod=vendor \
   -buildmode=pie \
   -o bin/%{name} ./cmd/kubectl-view-secret.go

ls -lh

%install
# Install the binary.
install -D -m 0755 bin/%{name} %{buildroot}/%{_bindir}/%{name}
cd %{buildroot}/%{_bindir}/
ln -s %{name} %{executable_name}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_bindir}/%{executable_name}

%changelog
