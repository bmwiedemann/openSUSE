#
# spec file for package kubectl-who-can
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


Name:           kubectl-who-can
Version:        0.0+git20190606.c185aaa
Release:        0
Summary:        Tool to show who has permissions to verbs and resources in Kubernetes
License:        Apache-2.0
Group:          System/Management
URL:            https://github.com/aquasecurity/kubectl-who-can
Source:         %{name}-%{version}.tar.xz
Source1:        vendor.tar.gz
BuildRequires:  golang(API) >= 1.11
BuildRequires:  golang-packaging
ExcludeArch:    s390 %{ix86}

%description
kubectl-who-can shows who has permissions
to <verb> <resources> in kubernetes

%prep
%setup -qa1

%build
sed -i -e 's|go build -o|go build -buildmode=pie -mod vendor -o|g' makefile
make

%install
mkdir -p %{buildroot}%{_bindir}/
install -D -m 0755 kubectl-who-can %{buildroot}%{_bindir}/

%files
%license LICENSE
%doc README.md
%{_bindir}/kubectl-who-can

%changelog
