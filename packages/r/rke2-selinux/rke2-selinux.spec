#
# spec file for package rke2-selinux
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


%define rke2_relabel_files() \
mkdir -p /var/lib/cni; \
mkdir -p /var/lib/kubelet/pods; \
mkdir -p /var/lib/rancher/rke2/agent/containerd/io.containerd.snapshotter.v1.overlayfs/snapshots; \
mkdir -p /var/lib/rancher/rke2/data; \
mkdir -p /var/run/flannel; \
mkdir -p /var/run/k3s; \
restorecon -R -i /etc/systemd/system/rke2.service; \
restorecon -R -i /usr/lib/systemd/system/rke2.service; \
restorecon -R /var/lib/cni; \
restorecon -R /var/lib/kubelet; \
restorecon -R /var/lib/rancher; \
restorecon -R /var/run/k3s; \
restorecon -R /var/run/flannel

%define selinux_policyver 20210716-3.1
%define container_policyver 2.164.2-1.1

Name:           rke2-selinux
Version:        0.11.latest.1
Release:        0
Summary:        SELinux policy module for rke2

Group:          System Environment/Base
License:        Apache-2.0
URL:            https://github.com/rancher/rke2-selinux
Source:         %{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  container-selinux >= %{container_policyver}
BuildRequires:  git
BuildRequires:  selinux-policy >= %{selinux_policyver}
BuildRequires:  selinux-policy-devel >= %{selinux_policyver}

Requires:       policycoreutils
Requires:       selinux-tools
Requires(post): selinux-policy-base >= %{selinux_policyver}
Requires(post): policycoreutils
Requires(post): container-selinux >= %{container_policyver}
Requires(postun):policycoreutils

Provides:       %{name} = %{version}-%{release}
Obsoletes:      rke2-selinux < 0.9
Conflicts:      k3s-selinux

%description
This package installs and sets up the SELinux policy security module for rke2.

%prep
%setup -q

%build
cd policy/microos
make -f /usr/share/selinux/devel/Makefile rke2.pp

%install
install -d %{buildroot}%{_datadir}/selinux/packages
install -m 644 policy/microos/rke2.pp %{buildroot}%{_datadir}/selinux/packages
install -d %{buildroot}%{_datadir}/selinux/devel/include/contrib
install -m 644 policy/microos/rke2.if %{buildroot}%{_datadir}/selinux/devel/include/contrib/
install -d %{buildroot}/etc/selinux/targeted/contexts/users/

%pre
%selinux_relabel_pre

%post
semodule -n -i %{_datadir}/selinux/packages/rke2.pp
if /usr/sbin/selinuxenabled ; then
    /usr/sbin/load_policy
    %rke2_relabel_files
fi;

%postun
if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall rke2
fi;

%posttrans
%selinux_relabel_post

%files
%attr(0600,root,root) %{_datadir}/selinux/packages/rke2.pp
%{_datadir}/selinux/devel/include/contrib/rke2.if

%changelog
