#
# spec file for package kucero
#
# Copyright (c) 2020 SUSE LLC, Nuernberg, Germany.
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

%define goipath github.com/jenting/kucero

Name:           kucero
Version:        1.3.0
Release:        0
Summary:        Kubernetes control plane certificate auto rotation
License:        Apache-2.0
Group:          System/Management
URL:            https://github.com/jenting/kucero
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang-packaging
BuildRequires:  golang(API) = 1.14

%description
A Kubernetes daemonset to perform automatic control plane certificate rotation.

%prep
%autosetup -p1 -a 1

%build
%goprep %{goipath}
export CGO_ENABLED=0
%gobuild -mod vendor -ldflags "-s -w -X main.version=%{version}" cmd/kucero

%install
%goinstall

%files
%defattr(-,root,root)
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
