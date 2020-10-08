# spec file for package cni-plugin-dnsname
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


Name:           cni-plugin-dnsname
Version:        1.0.0
Release:        0
Summary:        CNI plugin to provide name resolution for containers
License:        Apache-2.0
URL:            https://github.com/containers/dnsname
Source:         dnsname-%{version}.tar.xz
BuildRequires:  golang-packaging
BuildRequires:  golang(API) >= 1.13
Requires:       cni

%description
This CNI plugin sets up the use of dnsmasq on a given CNI network so that Pods
can resolve each other by name. When configured, the pod and its IP address are
added to a network specific hosts file that dnsmasq reads in. Similarly, when a
pod is removed from the network, it will remove the entry from the hosts file.
Each CNI network will have its own dnsmasq instance.

The dnsname plugin was specifically designed for the Podman container engine.

%prep
%setup -q -n dnsname-%{version}

%build
%make_build GO_BUILD="GO111MODULE=on go build -mod=vendor -buildmode=pie" binaries

%install
PREFIX=/usr %make_install

%files
%license LICENSE
%doc README.md README_PODMAN.md
%dir %{_libexecdir}/cni
%{_libexecdir}/cni/dnsname

%changelog
