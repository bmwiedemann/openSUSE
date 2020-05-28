#
# spec file for package podman
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


%define project        github.com/containers/libpod
# Build with libostree-devel in Tumbleweed, Leap 15 and SLES 15
%if 0%{?suse_version} >= 1500
%define with_libostree 1
%endif
Name:           podman
Version:        1.9.3
Release:        0
Summary:        Daemon-less container engine for managing containers, pods and images
License:        Apache-2.0
Group:          System/Management
Url:            https://github.com/containers/libpod
Source0:        %{name}-%{version}.tar.xz
Source1:        podman.conf
Source2:        libpod.conf
Source3:        %{name}-rpmlintrc
Source4:        README.SUSE.SLES
BuildRequires:  bash-completion
BuildRequires:  cni
BuildRequires:  device-mapper-devel
BuildRequires:  fdupes
BuildRequires:  git-core
BuildRequires:  glib2-devel-static
BuildRequires:  glibc-devel-static
BuildRequires:  go-go-md2man
BuildRequires:  golang-packaging
BuildRequires:  libapparmor-devel
BuildRequires:  libassuan-devel
BuildRequires:  libbtrfs-devel
BuildRequires:  libcontainers-common
BuildRequires:  libgpgme-devel
BuildRequires:  libseccomp-devel
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  golang(API) >= 1.12
# Build fails with PIE enabled on ppc64le due to boo#1098017
%ifarch ppc64le
#!BuildIgnore: gcc-PIE
%endif
Requires:       apparmor-parser
Requires:       apparmor-abstractions
Requires:       cni
Requires:       cni-plugins
Requires:       conmon
Requires:       iptables
Requires:       libcontainers-common
Requires:       libcontainers-image
Requires:       libcontainers-storage
Requires:       runc >= 1.0.0~rc4
Requires:       slirp4netns >= 0.4.0
Requires:       catatonit
Requires:       fuse-overlayfs
Recommends:     %{name}-cni-config = %{version}
Recommends:     katacontainers
%{go_nostrip}
%if 0%{?with_libostree}
BuildRequires:  libostree-devel
%endif

%description
Podman is a container engine for managing pods, containers, and container
images.
It is a standalone tool and it directly manipulates containers without the need
of a container engine daemon.
Podman is able to interact with container images create in buildah, cri-o, and
skopeo, as they all share the same datastore backend.

%prep
%setup -q

%package cni-config
Summary:        Basic CNI configuration for podman
Group:          System/Management
Requires:       %{name} = %{version}
# iproute2 is needed by the %triggerun scriplet
Requires:       iproute2
BuildArch:      noarch

%description cni-config
A "basic" CNI configuration for podman that makes networking usable for basic
setups. In more complicated setups, users are recommended to write their own
CNI configurations.

%build
# We can't use symlinks here because go-list gets confused by symlinks, so we
# have to copy the source to $HOME/go and then use that as the GOPATH.
export GOPATH=$HOME/go
mkdir -pv $HOME/go/src/%{project}
rm -rf $HOME/go/src/%{project}/*
cp -avr * $HOME/go/src/%{project}
cd $HOME/go/src/%{project}

# Build podman
make BUILDFLAGS=-buildmode=pie

# Build manpages
make %{?_smp_mflags} docs

%check
# Too many tests fail due to the restricted permissions in the build enviroment.
# Updates must be tested manually.

%install

# libpod
cd $HOME/go/src/%{project}
install -D -m 0755 bin/podman         %{buildroot}/%{_bindir}/podman
install -D -m 0755 bin/podman-remote  %{buildroot}/%{_bindir}/podman-remote
install -d %{buildroot}/%{_mandir}/man1
install -m 0644 docs/build/man/podman*.1 %{buildroot}/%{_mandir}/man1
install -d %{buildroot}/%{_mandir}/man5
install -m 0644 docs/build/man/libpod*.5 %{buildroot}/%{_mandir}/man5
install -D -m 0644 cni/87-podman-bridge.conflist %{buildroot}/%{_sysconfdir}/cni/net.d/87-podman-bridge.conflist
install -D -m 0644 %{SOURCE2} %{buildroot}/%{_sysconfdir}/containers/libpod.conf
install -D -m 0644 %{SOURCE2} %{buildroot}/%{_datadir}/containers/libpod.conf
install -D -m 0644 completions/bash/podman %{buildroot}/%{_datadir}/bash-completion/completions/podman
install -D -m 0644 completions/zsh/_podman %{buildroot}%{_sysconfdir}/zsh_completion.d/_podman

# podman varlink
install -D -m 0644 contrib/varlink/podman.conf %{buildroot}/%{_tmpfilesdir}/podman.conf
install -D -m 0644 contrib/varlink/io.podman.service %{buildroot}%{_unitdir}/io.podman.service
install -D -m 0644 contrib/varlink/io.podman.socket %{buildroot}%{_unitdir}/io.podman.socket

# Add podman modprobe.d drop-in config
mkdir -p %{buildroot}%{_libexecdir}/modules-load.d
install -m 0644 -t %{buildroot}%{_libexecdir}/modules-load.d/ %{SOURCE1}

# README.SUSE is SLES specifc currently
%if !0%{?is_opensuse}
install -D -m 0644 %{SOURCE4} %{buildroot}%{_docdir}/%{name}/README.SUSE
%endif

%fdupes %{buildroot}/%{_prefix}

%files
%if !0%{?is_opensuse}
%doc %{_docdir}/%{name}
%endif
# Binaries
%{_bindir}/podman
%{_bindir}/podman-remote
# Manpages
%{_mandir}/man1/podman*.1*
%{_mandir}/man5/libpod*.5*
# Configs
%config(noreplace) %{_sysconfdir}/containers/libpod.conf
%dir %{_datadir}/containers
%{_datadir}/containers/libpod.conf
%dir %{_libexecdir}/modules-load.d
%{_libexecdir}/modules-load.d/podman.conf
# Completion
%{_datadir}/bash-completion/completions/podman
%{_sysconfdir}/zsh_completion.d/_podman
# Varlink
%{_tmpfilesdir}/podman.conf
%{_unitdir}/io.podman.service
%{_unitdir}/io.podman.socket
%ghost /run/podman
%license LICENSE

%files cni-config
%config %{_sysconfdir}/cni/net.d/87-podman-bridge.conflist
%license LICENSE

%pre
%service_add_pre io.podman.service io.podman.socket

%post
%service_add_post io.podman.service io.podman.socket
%tmpfiles_create %{_tmpfilesdir}/podman.conf

%preun
%service_del_preun io.podman.service io.podman.socket

%postun
%service_del_postun io.podman.service io.podman.socket

%triggerun cni-config -- %{name}-cni-config < 1.6.0
# The name of the network bridge changed from cni0 to podman-cni0 with
# podman 1.6. We need to rename the existing bridge to the new name to
# to avoid network issues after upgrade
if ip link show dev cni0 > /dev/null 2>&1; then
    ip link set dev cni0 down
    ip link set dev cni0 name cni-podman0
    ip link set dev cni-podman0 up
fi

%changelog
