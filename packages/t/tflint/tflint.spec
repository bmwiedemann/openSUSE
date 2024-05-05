#
# spec file for package tflint
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

Name:           tflint
Version:        0.51.0
Release:        0
Summary:        A Pluggable Terraform Linter
License:        MPL-2.0
URL:            https://github.com/terraform-linters/tflint
Source:         tflint-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go1.22

%description
A Pluggable Terraform Linter

Features

TFLint is a framework and each feature is provided by plugins, the key features are as follows:
* Find possible errors (like invalid instance types) for Major Cloud providers (AWS/Azure/GCP).
* Warn about deprecated syntax, unused declarations.
* Enforce best practices, naming conventions.

%prep
%autosetup -p1 -a 1

%build
go build \
   -mod=vendor \
   -buildmode=pie \
   -o ./bin/tflint

%install
# Install the binary.
install -D -m 0755 ./bin/%{name} "%{buildroot}/%{_bindir}/%{name}"

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
