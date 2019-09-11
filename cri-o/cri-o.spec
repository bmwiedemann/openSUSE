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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

%define project github.com/cri-o/cri-o
# Define macros for further referenced sources
%define	name_source1 crio.service
%define	name_source2 sysconfig.crio
%define	name_source3 crio.conf
Name:           cri-o
Version:        1.15.0
Release:        0
Summary:        OCI-based implementation of Kubernetes Container Runtime Interface
License:        Apache-2.0
Group:          System/Management
Url:            https://github.com/cri-o/cri-o
ExcludeArch:    i586
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name_source1}
Source2:        %{name_source2}
Source3:        %{name_source3}
Source4:        cri-o-rpmlintrc
Source5:        kubelet.env
BuildRequires:  device-mapper-devel
BuildRequires:  fdupes
BuildRequires:  glib2-devel-static
BuildRequires:  glibc-devel-static
BuildRequires:  golang-packaging
BuildRequires:  libapparmor-devel
BuildRequires:  libassuan-devel
BuildRequires:  libbtrfs-devel
BuildRequires:  libgpgme-devel
BuildRequires:  libseccomp-devel
BuildRequires:  golang(API) >= 1.12
Requires:       patterns-base-apparmor
Requires:       conntrack-tools
Requires:       cni
Requires:       cni-plugins
Requires:       iproute2
Requires:       iptables
Requires:       libcontainers-common
Requires:       libcontainers-image
Requires:       libcontainers-storage
Requires:       runc >= 1.0.0~rc6
Requires:       socat
# Provide generic cri-runtime dependency (needed by kubernetes)
Provides:       cri-runtime
# disable stripping of binaries
%{go_nostrip}

%description
CRI-O provides an integration path between OCI conformant runtimes
and the kubelet. Specifically, it implements the Kubelet Container Runtime
Interface (CRI) using OCI conformant runtimes. The scope of CRI-O is tied to
the scope of the CRI.

%package kubeadm-criconfig
Summary:        CRI-O container runtime configuration for kubeadm
Group:          System/Management
Requires:       kubernetes-kubeadm
Requires(post): %fillup_prereq
Supplements:    cri-o
Provides:       kubernetes-kubeadm-criconfig
Conflicts:      docker-kubic-kubeadm-criconfig

%description kubeadm-criconfig
This package provides the CRI-O container runtime configuration for kubeadm

%prep
%setup -q

%build
# We can't use symlinks here because go-list gets confused by symlinks, so we
# have to copy the source to $HOME/go and then use that as the GOPATH.
export GOPATH=$HOME/go
mkdir -pv $HOME/go/src/%{project}
rm -rf $HOME/go/src/%{project}/*
cp -avr * $HOME/go/src/%{project}
cd $HOME/go/src/%{project}

# Build crio
make

%pre
%service_add_pre %{name_source1}

%post
%service_add_post %{name_source1}
# This is the additional directory where cri-o is going to look up for CNI
# plugins installed by DaemonSets running on Kubernetes (i.e. Cilium).
mkdir -p /opt/cni/bin

%post kubeadm-criconfig
%fillup_only -n kubelet

%preun
%service_del_preun %{name_source1}

%postun
%service_del_postun %{name_source1}

%install
cd $HOME/go/src/%{project}

# Binaries
install -D -m 0755 bin/crio    %{buildroot}/%{_bindir}/crio
install -d %{buildroot}/%{_libexecdir}/crio/bin
install -D -m 0755 bin/conmon  %{buildroot}/%{_libexecdir}/crio/bin/conmon
install -D -m 0755 bin/pause   %{buildroot}/%{_libexecdir}/crio/bin/pause
# Manpages
install -d %{buildroot}/%{_mandir}/man5
install -d %{buildroot}/%{_mandir}/man8
install -m 0644 docs/crio.conf.5 %{buildroot}/%{_mandir}/man5
install -m 0644 docs/crio.8      %{buildroot}/%{_mandir}/man8
# Configs
install -D -m 0644 %{SOURCE3}       %{buildroot}/%{_sysconfdir}/crio/%{name_source3}
install -D -m 0644 crio-umount.conf %{buildroot}/%{_datadir}/oci-umount/oci-umount.d/cri-umount.conf
install -D -m 0644 %{SOURCE2}       %{buildroot}%{_fillupdir}/%{name_source2}
# Systemd
install -D -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name_source1}
# place kubelet.env in fillupdir
install -D -m 0644 %{SOURCE5} %{buildroot}%{_fillupdir}/sysconfig.kubelet
# Symlinks to rc files
install -d -m 0755 %{buildroot}%{_sbindir}
ln -sf service %{buildroot}%{_sbindir}/rccrio

%fdupes %{buildroot}/%{_prefix}

%files
# Binaries
%{_bindir}/crio
%dir %{_libexecdir}/crio
%dir %{_libexecdir}/crio/bin
%{_libexecdir}/crio/bin/conmon
%{_libexecdir}/crio/bin/pause
# Manpages
%{_mandir}/man5/crio.conf.5*
%{_mandir}/man8/crio.8*
# License
%license LICENSE
# Configs
%dir %{_sysconfdir}/crio
%config(noreplace) %{_sysconfdir}/crio/%{name_source3}
%dir %{_datadir}/oci-umount
%dir %{_datadir}/oci-umount/oci-umount.d
%{_datadir}/oci-umount/oci-umount.d/cri-umount.conf
%{_fillupdir}/%{name_source2}
# Systemd
%{_unitdir}/%{name_source1}
%{_sbindir}/rccrio

%files kubeadm-criconfig
%defattr(-,root,root)
%{_fillupdir}/sysconfig.kubelet

%changelog
