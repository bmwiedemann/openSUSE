#
# spec file for package kubelogin
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


Name:           kubelogin
Version:        0.1.6
Release:        0
Summary:        Kubernetes client credential plugin implementing Azure authentication
License:        MIT
URL:            https://github.com/Azure/kubelogin
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang-packaging
BuildRequires:  golang(API) >= 1.21
%{go_provides}

%description
A client-go credential (exec) plugin implementing azure authentication. This plugin provides features
that are not available in kubectl. It is supported on kubectl v1.11+

%prep
%setup -qa1

%build
%goprep github.com/Azure/kubelogin
%ifarch s390x i586 armv7l
export CGO_ENABLED=1
%else
export CGO_ENABLED=0
%endif
%gobuild -mod vendor -buildmode pie -ldflags "-X main.version=v%{version}" "${name}"

%install
%goinstall

%files
%{_bindir}/%{name}
%license LICENSE
%doc README.md

%changelog
