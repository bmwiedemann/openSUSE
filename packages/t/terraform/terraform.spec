#
# spec file for package terraform
#
# Copyright (c) 2023 SUSE LLC
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


Name:           terraform
Version:        1.3.7
Release:        0
Summary:        Tool for building infrastructure safely and efficiently
License:        MPL-2.0
Group:          System/Management
URL:            https://www.terraform.io/
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source99:       terraform-rpmlintrc
BuildRequires:  golang-packaging
BuildRequires:  golang(API) >= 1.17
# See: https://github.com/hashicorp/terraform/issues/22807
ExcludeArch:    %{ix86} %{arm}
%{go_nostrip}
%{go_provides}

%description
Terraform is a tool for building, changing, and versioning infrastructure
safely and efficiently. Terraform can manage existing and popular service
providers as well as custom in-house solutions.

%prep
%setup -q
%setup -q -T -D -a 1

%build
export GOFLAGS='-mod=vendor -buildmode=pie'
%{goprep} github.com/hashicorp/terraform
%{gobuild} .

%install
%{goinstall}
rm -rf %{buildroot}/%{_libdir}/go/contrib

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/%{name}

%changelog
