#
# spec file for package terragrunt
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

Name:           terragrunt
Version:        0.58.14
Release:        0
Summary:        Thin wrapper for Terraform for working with multiple Terraform modules
License:        MIT
URL:            https://github.com/gruntwork-io/terragrunt
Source:         terragrunt-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        Makefile
Source3:        PACKAGING_README.md
BuildRequires:  go1.21 >= 1.21.7

%description
Terragrunt is a thin wrapper for Terraform that provides extra tools for keeping your Terraform configurations DRY, working with multiple Terraform modules, and managing remote state.

%prep
%autosetup -p1 -a 1

%build
go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags="-X github.com/gruntwork-io/go-commons/version.Version=v%{version}"

%install
# Install the binary.
install -D -m 0755 %{name} "%{buildroot}/%{_bindir}/%{name}"

%files
%doc README.md
%license LICENSE.txt
%{_bindir}/%{name}

%changelog
