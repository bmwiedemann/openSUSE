#
# spec file for package kail
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


Name:           kail
Version:        0.17.0
Release:        0
Summary:        Kubernetes log viewer
License:        MIT
Group:          System/Management
URL:            https://github.com/boz/kail
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang(API) >= 1.20
ExcludeArch:    s390
ExcludeArch:    %{ix86}

%description
Kubernetes tail: streams logs from all containers of all matched pods.
Match pods by service, replicaset, deployment, and others. Adjusts to a
changing cluster - pods are added and removed from logging as they fall
in or out of the selection.

%prep
%autosetup -p 1 -a 1

%build
go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags="-X main.version=%{version} -X main.commit=v%{version}" \
   -o bin/%{name} ./cmd/%{name}

%install
# Install the binary.
install -D -m 0755 bin/%{name} %{buildroot}/%{_bindir}/%{name}

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/%{name}

%changelog
