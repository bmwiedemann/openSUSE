#
# spec file for package cri-o
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define project github.com/cri-o/cri-o
#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
# Define macros for further referenced sources
Name:           cri-o
Version:        1.36.7
Release:        0
Summary:        OCI-based implementation of Kubernetes Container Runtime Interface
# crio links MPL-2.0 code (hashicorp errwrap and go-multierror, parts
# of cyphar filepath-securejoin), hence the ANDed tag below.
License:        Apache-2.0 AND MPL-2.0
URL:            https://github.com/cri-o/cri-o
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        crio.service
Source3:        sysconfig.crio
Source4:        crio.conf
Source5:        kubelet.env
BuildRequires:  device-mapper-devel
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  glib2-devel-static
BuildRequires:  glibc-devel-static
BuildRequires:  go-md2man
BuildRequires:  golang(API) >= 1.26
BuildRequires:  golang-packaging
BuildRequires:  libapparmor-devel
BuildRequires:  libassuan-devel
BuildRequires:  libbtrfs-devel
BuildRequires:  libgpgme-devel
BuildRequires:  libseccomp-devel
BuildRequires:  make
BuildRequires:  sed
Requires:       cni
Requires:       cni-plugins
Requires:       conmon
Requires:       conntrack-tools
Requires:       iproute2
Requires:       iptables
Requires:       libcontainers-common >= 0.0.1
Requires:       patterns-base-apparmor
Requires:       runc >= 1.0.2
Suggests:       katacontainers
# Provide generic cri-runtime dependency (needed by kubernetes)
Provides:       cri-runtime
ExcludeArch:    i586
# disable stripping of binaries
%{go_nostrip}

%description
CRI-O provides an integration path between OCI conformant runtimes
and the kubelet. Specifically, it implements the Kubelet Container Runtime
Interface (CRI) using OCI conformant runtimes. The scope of CRI-O is tied to
the scope of the CRI.

%package kubeadm-criconfig
Summary:        CRI-O container runtime configuration for kubeadm
License:        Apache-2.0 AND MPL-2.0
Requires:       kubernetes-kubeadm-provider
Requires(post): %fillup_prereq
Supplements:    cri-o
Conflicts:      docker-kubic-kubeadm-criconfig
Provides:       kubernetes-kubeadm-criconfig

%description kubeadm-criconfig
This package provides the CRI-O container runtime configuration for kubeadm

%prep
%setup -qa1

%build
# Keep cgroupfs as the default cgroup manager for SLE15 builds
%if 0%{?sle_version} >= 150000 && !0%{?is_opensuse}
sed -i "s|.*apparmor_profile =.*|apparmor_profile = \"crio-default-%{version}\"|" %{SOURCE4}
sed -i "s|^cgroup_manager = \"systemd\"$|cgroup_manager = \"cgroupfs\"|g" %{SOURCE4}
sed -i "s|--cgroup-driver=systemd|--cgroup-driver=cgroupfs|g" %{SOURCE5}
%endif

# We can't use symlinks here because go-list gets confused by symlinks, so we
# have to copy the source to $HOME/go and then use that as the GOPATH.
export GOPATH=$HOME/go
mkdir -pv $HOME/go/src/%{project}
rm -rf $HOME/go/src/%{project}/*
cp -avr * $HOME/go/src/%{project}
cd $HOME/go/src/%{project}

# Build crio
GO_BUILD="go build -mod vendor" GO_MD2MAN=%{_bindir}/go-md2man make

%pre
%service_add_pre crio.service

%post
%service_add_post crio.service
# This is the additional directory where cri-o is going to look up for CNI
# plugins installed by DaemonSets running on Kubernetes (i.e. Cilium).
mkdir -p /opt/cni/bin

%post kubeadm-criconfig
%fillup_only -n kubelet

%preun
%service_del_preun crio.service

%postun
%service_del_postun crio.service

%install
cd $HOME/go/src/%{project}

# Binaries
install -D -m 0755 bin/crio    %{buildroot}/%{_bindir}/crio
install -D -m 0755 bin/pinns    %{buildroot}/%{_bindir}/pinns
install -d %{buildroot}/%{_libexecdir}/crio/bin
# Completions
install -D -m 0644 completions/bash/crio %{buildroot}/%{_datadir}/bash-completion/completions/crio
install -D -m 0644 completions/zsh/_crio %{buildroot}%{_sysconfdir}/zsh_completion.d/_crio
install -D -m 0644 completions/fish/crio.fish %{buildroot}/%{_datadir}/fish/completions/crio.fish
# Manpages
install -d %{buildroot}/%{_mandir}/man5
install -d %{buildroot}/%{_mandir}/man8
install -m 0644 docs/crio.conf.5 %{buildroot}/%{_mandir}/man5
install -m 0644 docs/crio.conf.d.5 %{buildroot}/%{_mandir}/man5
install -m 0644 docs/crio.8      %{buildroot}/%{_mandir}/man8
# Configs
sed -e 's-@LIBEXECDIR@-%{_libexecdir}-g' -i %{SOURCE4}
install -D -m 0644 %{SOURCE4}       %{buildroot}/%{_sysconfdir}/crio/crio.conf.d/00-default.conf
install -D -m 0644 crio-umount.conf %{buildroot}/%{_datadir}/oci-umount/oci-umount.d/cri-umount.conf
install -D -m 0644 %{SOURCE3}       %{buildroot}%{_fillupdir}/sysconfig.crio
# Systemd
install -D -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}/crio.service
# place kubelet.env in fillupdir
install -D -m 0644 %{SOURCE5} %{buildroot}%{_fillupdir}/sysconfig.kubelet
# Symlinks to rc files
install -d -m 0755 %{buildroot}%{_sbindir}
ln -sf service %{buildroot}%{_sbindir}/rccrio

%fdupes %{buildroot}/%{_prefix}

%files
# Binaries
%{_bindir}/crio
%{_bindir}/pinns
%dir %{_libexecdir}/crio
%dir %{_libexecdir}/crio/bin
# Completions
%{_datadir}/bash-completion/completions/crio
%{_sysconfdir}/zsh_completion.d
%{_sysconfdir}/zsh_completion.d/_crio
%{_datadir}/fish
%{_datadir}/fish/completions
%{_datadir}/fish/completions/crio.fish
# Manpages
%{_mandir}/man5/crio.conf.5%{?ext_man}
%{_mandir}/man5/crio.conf.d.5%{?ext_man}
%{_mandir}/man8/crio.8%{?ext_man}
# License
%license LICENSE
# Configs
%dir %{_sysconfdir}/crio
%dir %{_sysconfdir}/crio/crio.conf.d
%config %{_sysconfdir}/crio/crio.conf.d/00-default.conf
%dir %{_datadir}/oci-umount
%dir %{_datadir}/oci-umount/oci-umount.d
%{_datadir}/oci-umount/oci-umount.d/cri-umount.conf
%{_fillupdir}/sysconfig.crio
# Systemd
%{_unitdir}/crio.service
%{_sbindir}/rccrio

%files kubeadm-criconfig
%{_fillupdir}/sysconfig.kubelet

%changelog
