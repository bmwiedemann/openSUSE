#
# spec file for package kustomize
#
# Copyright (c) 2020 SUSE LLC
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


Name:           kustomize
Version:        3.8.4
Release:        0
Summary:        Customization of kubernetes YAML configurations
License:        Apache-2.0
Group:          System/Management
URL:            https://github.com/kubernetes-sigs/kustomize
Source:         %{name}-%{name}-v%{version}.tar.gz
Source1:        vendor.tar.xz
BuildRequires:  golang(API) = 1.13
ExcludeArch:    s390
ExcludeArch:    %{ix86}
%ifarch %arm aarch64
BuildRequires:  binutils-gold
%endif

%description
kustomize customizes raw, template-free kubernetes YAML files for
multiple purposes, leaving the original YAML untouched and usable
as is.

%prep
%setup -qa1 -n %{name}-%{name}-v%{version}

%build
cd kustomize
go build -mod vendor -buildmode=pie .

%install
# Install the binary.
mkdir -p %{buildroot}%{_bindir}/
install -m 0755 kustomize/kustomize %{buildroot}%{_bindir}

%files
%license LICENSE
%{_bindir}/kustomize

%changelog
