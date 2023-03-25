#
# spec file for package podman
#
# Copyright (c) 2023 SUSE LLC
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

%{!?_user_tmpfilesdir: %global _user_tmpfilesdir %{_datadir}/user-tmpfiles.d}
%define project        github.com/containers/podman
Name:           podman
Version:        4.4.3
Release:        0
Summary:        Daemon-less container engine for managing containers, pods and images
License:        Apache-2.0
Group:          System/Management
URL:            https://%{project}
Source0:        %{name}-%{version}.tar.xz
Source1:        podman.conf
Source2:        README.SUSE.SLES
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
BuildRequires:  golang(API) = 1.18
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  pkgconfig(libsystemd)
Recommends:     apparmor-abstractions
Recommends:     apparmor-parser
Requires:       catatonit >= 0.1.7
Requires:       cni
Requires:       cni-plugins
Requires:       conmon >= 2.0.24
Requires:       fuse-overlayfs
Requires:       iptables
Requires:       libcontainers-common >= 20210626
Requires:       runc >= 1.0.1
Requires:       slirp4netns >= 0.4.0
Requires:       timezone
Recommends:     %{name}-cni-config = %{version}
Suggests:       katacontainers
BuildRequires:  libostree-devel


%description
Podman is a container engine for managing pods, containers, and container
images.
It is a standalone tool and it directly manipulates containers without the need
of a container engine daemon.
Podman is able to interact with container images create in buildah, cri-o, and
skopeo, as they all share the same datastore backend.

%prep
%autosetup -p1

%package remote
Summary: Client for managing podman containers remotely
Group:          System/Management
Conflicts:      %{name} < 3.1.2
Provides:       podman:%{_bindir}/%{name}-remote

%description remote
This client allows controlling podman on a separate host, e.g. over SSH.

%package cni-config
Summary:        Basic CNI configuration for podman
Group:          System/Management
Requires:       %{name} = %{version}
# iproute2 is needed by the %%triggerun scriplet
Requires:       iproute2
BuildArch:      noarch

%description cni-config
A "basic" CNI configuration for podman that makes networking usable for basic
setups. In more complicated setups, users are recommended to write their own
CNI configurations.

%package docker
Summary:        Emulate Docker CLI using podman
BuildArch:      noarch
Requires:       %{name} = %{version}
Conflicts:      docker
Conflicts:      docker-ce
Conflicts:      docker-ee
Conflicts:      docker-latest
Conflicts:      moby-engine

%description docker
This package installs a script named docker that emulates the Docker CLI by
executes podman commands, it also creates links between all Docker CLI man
pages and %{name}.

%build
# Build podman
BUILDFLAGS="-buildmode=pie" PREFIX=%{_prefix} %make_build

# Build manpages
%make_build docs

%check
# Too many tests fail due to the restricted permissions in the build enviroment.
# Updates must be tested manually.

%install
%make_install PREFIX=%{_prefix} LIBEXECDIR=%{_libexecdir} install.completions install.docker

# remove the user tmpfile on SLE/Leap as it cannot handle them
%if 0%{?suse_version} == 1500
rm %{buildroot}%{_user_tmpfilesdir}/podman-docker.conf
%endif

# Add podman modprobe.d drop-in config
mkdir -p %{buildroot}%{_prefix}/lib/modules-load.d
install -m 0644 -t %{buildroot}%{_prefix}/lib/modules-load.d/ %{SOURCE1}

# README.SUSE is SLES specifc currently
%if !0%{?is_opensuse}
install -D -m 0644 %{SOURCE2} %{buildroot}%{_docdir}/%{name}/README.SUSE
%endif

%fdupes %{buildroot}/%{_datadir}
%fdupes %{buildroot}/%{_systemd_util_dir}

%files
%if !0%{?is_opensuse}
%doc %{_docdir}/%{name}
%endif
# Binaries
%{_bindir}/podman
# Manpages
%{_mandir}/man1/podman*.1*
%{_mandir}/man5/podman*.5*
%{_mandir}/man5/quadlet*.5*
%exclude %{_mandir}/man1/podman-remote*.1*
# Configs
%dir %{_prefix}/lib/modules-load.d
%{_prefix}/lib/modules-load.d/podman.conf
%{_tmpfilesdir}/podman.conf
# Rootless port
%dir %{_libexecdir}/podman
%{_libexecdir}/podman/rootlessport
%{_libexecdir}/podman/quadlet
# Completion
%{_datadir}/bash-completion/completions/podman
%{_datadir}/zsh/site-functions/_podman
%dir %{_datadir}/fish/
%dir %{_datadir}/fish/vendor_completions.d/
%{_datadir}/fish/vendor_completions.d/podman.fish
%{_unitdir}/podman.service
%{_unitdir}/podman.socket
%{_unitdir}/podman-auto-update.service
%{_unitdir}/podman-kube@.service
%{_unitdir}/podman-restart.service
%{_unitdir}/podman-auto-update.timer
%{_unitdir}/podman-clean-transient.service
%{_userunitdir}/podman.service
%{_userunitdir}/podman.socket
%{_userunitdir}/podman-auto-update.service
%{_userunitdir}/podman-kube@.service
%{_userunitdir}/podman-restart.service
%{_userunitdir}/podman-auto-update.timer
%{_systemdusergeneratordir}/podman-user-generator
%{_systemdgeneratordir}/podman-system-generator
%ghost /run/podman
%license LICENSE

%files remote
%{_bindir}/podman-remote
%{_mandir}/man1/podman-remote*.1*
%{_datadir}/bash-completion/completions/podman-remote
%{_datadir}/zsh/site-functions/_podman-remote
%dir %{_datadir}/fish/
%dir %{_datadir}/fish/vendor_completions.d/
%{_datadir}/fish/vendor_completions.d/podman-remote.fish

%files cni-config
%license LICENSE

%files docker
%{_bindir}/docker
%{_tmpfilesdir}/podman-docker.conf
%if 0%{?suse_version} > 1500
%{_user_tmpfilesdir}/podman-docker.conf
%dir %{_user_tmpfilesdir}
%endif

%post docker
%tmpfiles_create %{_tmpfilesdir}/podman-docker.conf

%pre
%service_add_pre podman.service podman.socket podman-auto-update.service podman-restart.service podman-auto-update.timer podman-clean-transient.service

%post
%service_add_post podman.service podman.socket podman-auto-update.service podman-restart.service podman-auto-update.timer podman-clean-transient.service
%tmpfiles_create %{_tmpfilesdir}/podman.conf
%systemd_user_post podman.service podman.socket podman-auto-update.service podman-restart.service podman-auto-update.timer

%preun
%service_del_preun podman.service podman.socket podman-auto-update.service podman-restart.service podman-auto-update.timer podman-clean-transient.service
%systemd_user_preun podman.service podman.socket podman-auto-update.service podman-restart.service podman-auto-update.timer

%postun
%service_del_postun podman.service podman.socket podman-auto-update.service podman-restart.service podman-auto-update.timer podman-clean-transient.service
%systemd_user_postun podman.service podman.socket podman-auto-update.service podman-restart.service podman-auto-update.timer

%changelog
