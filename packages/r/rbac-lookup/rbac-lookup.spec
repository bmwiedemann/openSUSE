#
# spec file for package rbac-lookup
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
# nodebuginfo


Name:           rbac-lookup
Version:        0.3.2
Release:        0
Summary:        Tool to find roles and cluster roles in a Kubernetes cluster
License:        Apache-2.0
Group:          System/Management
URL:            https://github.com/reactiveops/rbac-lookup
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang(API) >= 1.11
BuildRequires:  golang-packaging
ExcludeArch:    s390
ExcludeArch:    %{ix86}
%{go_nostrip}

%description
This tool allows finding Kubernetes roles and cluster roles bound to
any user, service account, or group name.

%prep
%setup -qa1

%build
go build -mod vendor -buildmode=pie -a -o rbac-lookup ./main.go

%install
mkdir -p %{buildroot}%{_sbindir}/
install -D -m 0755 rbac-lookup %{buildroot}%{_sbindir}/

%files
%license LICENSE
%doc README.md
%{_sbindir}/rbac-lookup

%changelog
