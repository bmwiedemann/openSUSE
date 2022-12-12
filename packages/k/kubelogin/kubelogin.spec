#
# spec file for package kubelogin
#
# Copyright (c) 2022 SUSE LLC
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


Name:           kubelogin
Version:        0.0.24
Release:        0
Summary:        Kubernetes client credential plugin implementing Azure authentication
License:        MIT
URL:            https://github.com/Azure/kubelogin
Source0:        https://github.com/Azure/kubelogin/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang-packaging
BuildRequires:  golang(API) >= 1.17
%{go_provides} 

%description
A client-go credential (exec) plugin implementing azure authentication. This plugin provides features
that are not available in kubectl. It is supported on kubectl v1.11+

%prep
%setup -qa1

%build
%goprep github.com/Azure/kubelogin
export CGO_ENABLED=0
%gobuild -mod vendor -buildmode pie -ldflags "-X main.version=v%{version}" "${name}"

%install
%goinstall

%files
%{_bindir}/%{name}
%license LICENSE
%doc README.md

%changelog

