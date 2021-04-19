#
# spec file for package k3s
#
# Copyright (c) 2021 SUSE LLC
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


# To workaround https://github.com/rancher/k3s/issues/231, build kubectl
%define build_kubectl 1

# baseversion - version of kubernetes for this package
%define baseversion 1.20

Name:           k3s
Version:        1.20.6+k3s1
Release:        0
Summary:        A container orchestration system based on a reduced Kubernetes feature set
License:        Apache-2.0
Group:          System/Management
URL:            https://k3s.io
Source0:        https://github.com/k3s-io/k3s/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        k3s-server.service
Source2:        k3s-agent.service
Source3:        server.conf
Source4:        agent.conf
Patch0:         cni-bin-dir.patch
BuildRequires:  c_compiler
BuildRequires:  golang-packaging
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  golang(API) >= 1.15
BuildRequires:  pkgconfig(sqlite3)
Requires:       cni-plugins
Requires:       conntrack-tools
Requires:       containerd
Requires:       iptables
Requires:       runc
# Conflicts:      cri-tools
Conflicts:      kubectl
Conflicts:      kubernetes-client
Conflicts:      kubernetes-client-provider
Requires(post): update-alternatives
Requires(postun):update-alternatives
%{?systemd_requires}

%description
k3s is a container orchestration system for automating application
deployment, scaling, and management. It is a Kubernetes-compliant
distribution that differs from the original Kubernetes (colloquially
"k8s") in that:

  * Legacy, alpha, or non-default features are removed.
  * Most in-tree plugins (cloud providers and storage plugins) were
    removed, since they can be replaced with out-of-tree addons.
  * sqlite3 is the default storage mechanism.
    etcd3 is still available, but not the default.
  * There is a new launcher that handles a lot of the complexity of
    TLS and options.

%prep
%setup -q -n %{name}-%(echo %{version} | tr '+' '-')
sed -e 's-@LIBEXECDIR@-%{_libexecdir}-g' -i %{PATCH0}
%patch0 -p1

%build
%{goprep} github.com/rancher/k3s
%{gobuild}
%if %{build_kubectl}
%{gobuild} ./cmd/kubectl
%endif

%install
%{goinstall}
%if %{build_kubectl}
%{goinstall} ./cmd/kubectl
mv -v %{buildroot}%{_bindir}/kubectl %{buildroot}%{_bindir}/kubectl%{baseversion}
%endif

# Install symlinks
pushd %{buildroot}%{_bindir}
%if !%{build_kubectl}
ln -s k3s kubectl%{baseversion}
%endif
# ln -s k3s crictl
popd

mkdir -p %{buildroot}%{_localstatedir}/lib/rancher/k3s
mkdir -p %{buildroot}%{_localstatedir}/lib/rancher/k3s/server/manifests

mkdir -p %{buildroot}%{_sysconfdir}/rancher/k3s
install -D -m 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/rancher/k3s/server.conf
install -D -m 644 %{SOURCE4} %{buildroot}%{_sysconfdir}/rancher/k3s/agent.conf

mkdir -p %{buildroot}%{_unitdir}
install -D -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/k3s-server.service
install -D -m 644 %{SOURCE2} %{buildroot}%{_unitdir}/k3s-agent.service
mkdir -p %{buildroot}%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rck3s-server
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rck3s-agent

# alternatives
ln -s -f %{_sysconfdir}/alternatives/kubectl %{buildroot}%{_bindir}/kubectl

%pre
%service_add_pre k3s-server.service k3s-agent.service

%post
export baseversion="%{baseversion}"
%{_sbindir}/update-alternatives \
  --install %{_bindir}/kubectl kubectl %{_bindir}/kubectl%{baseversion} ${baseversion/./}

%service_add_post k3s-server.service k3s-agent.service

%preun
%service_del_preun k3s-server.service k3s-agent.service

%postun
if [ ! -f %{_bindir}/kubectl%{baseversion} ] ; then
  update-alternatives --remove kubectl %{_bindir}/kubectl%{baseversion}
fi

%service_del_postun k3s-server.service k3s-agent.service

%files
%license LICENSE
%doc README.md
# %{_bindir}/crictl
%{_bindir}/k3s
%{_bindir}/kubectl
%{_bindir}/kubectl%{baseversion}
%{_localstatedir}/lib/rancher
%config %{_sysconfdir}/rancher
%config(noreplace) %{_sysconfdir}/rancher/k3s/agent.conf
%config(noreplace) %{_sysconfdir}/rancher/k3s/server.conf
%{_unitdir}/k3s-agent.service
%{_unitdir}/k3s-server.service
%{_sbindir}/rck3s-agent
%{_sbindir}/rck3s-server
%ghost %_sysconfdir/alternatives/kubectl

%changelog
