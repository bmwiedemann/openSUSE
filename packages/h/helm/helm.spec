#
# spec file for package helm
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


%define git_commit ac925eb7279f4a6955df663a0128044a8a6b7593
Name:           helm
Version:        3.0.3
Release:        0
Summary:        The Kubernetes Package Manager
License:        Apache-2.0
Group:          Development/Languages/Other
URL:            https://github.com/kubernetes/helm
Source:         %{name}-%{version}.tar.xz
Source1:        vendor.tar.xz
BuildRequires:  golang-packaging
BuildRequires:  xz
BuildRequires:  golang(API) >= 1.12
%{go_nostrip}
%{go_provides}

%description
Helm is a tool for managing Kubernetes charts. Charts are packages of pre-configured Kubernetes resources.

%prep
%setup -q
tar xJf %{SOURCE1}

%build
go build -mod=vendor -buildmode=pie ./cmd/helm

%install
mkdir -p %{buildroot}%{_bindir}
install -m755 helm %{buildroot}/%{_bindir}/helm

%files
%doc README.md
%license LICENSE
%{_bindir}/helm

%changelog
