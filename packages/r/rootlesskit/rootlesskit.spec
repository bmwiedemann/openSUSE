#
# spec file for package rootlesskit
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


Name:           rootlesskit
Version:        2.1.0
Release:        0
Summary:        Linux-native fakeroot using user namespaces
License:        Apache-2.0
URL:            https://github.com/rootless-containers/rootlesskit
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang(API) >= 1.21
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
RootlessKit is a Linux-native implementation of "fake root"
using user_namespaces. RootlessKit is intended to run Docker and
Kubernetes as an unprivileged user (known as "Rootless mode"), so as to protect
the real root on the host from potential container-breakout attacks.

%prep
%setup -qa1

%build
go build -mod=vendor -buildmode=pie -o _output/rootlesskit ./cmd/rootlesskit
go build -mod=vendor -buildmode=pie -o _output/rootlessctl ./cmd/rootlessctl
go build -mod=vendor -buildmode=pie -o _output/rootlesskit-docker-proxy ./cmd/rootlesskit-docker-proxy

%install
mkdir -p %{buildroot}%{_bindir}/
install -m 0755 _output/rootlesskit %{buildroot}%{_bindir}/rootlesskit
install -m 0755 _output/rootlessctl %{buildroot}%{_bindir}/rootlessctl
install -m 0755 _output/rootlesskit-docker-proxy %{buildroot}%{_bindir}/rootlesskit-docker-proxy

%files
%license LICENSE
%doc README.md docs/*.md
%{_bindir}/rootlesskit
%{_bindir}/rootlessctl
%{_bindir}/rootlesskit-docker-proxy

%changelog
