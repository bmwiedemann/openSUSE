#
# spec file for package cni-plugin-flannel
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


%define cni_dir %{_libexecdir}/cni

Name:           cni-plugin-flannel
Version:        1.6.0
Release:        0
Summary:        A CNI network plugin that is powered by flannel
License:        Apache-2.0
URL:            https://github.com/flannel-io/cni-plugin
Source0:        cni-plugin-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang-packaging
BuildRequires:  golang(API) >= 1.16
Requires:       flannel

%description
This plugin is designed to work in conjunction with flannel, a network fabric
for containers. When flannel daemon is started, it outputs a
/run/flannel/subnet.env file that looks like this:

FLANNEL_NETWORK=10.1.0.0/16
FLANNEL_SUBNET=10.1.17.1/24
FLANNEL_MTU=1472
FLANNEL_IPMASQ=true

This information reflects the attributes of flannel network on the host. The
flannel CNI plugin uses this information to configure another CNI plugin, such
as bridge plugin.

%prep
%autosetup -n cni-plugin-%{version} -a 1

%build
%{goprep} github.com/flannel-io/cni-plugin
%{gobuild}

%install
%{goinstall}
mkdir -p %{buildroot}%{cni_dir}
mv %{buildroot}%{_bindir}/cni-plugin %{buildroot}%{cni_dir}/flannel

%files
%license LICENSE
%doc README.md
%dir %{cni_dir}/
%{cni_dir}/flannel

%changelog
