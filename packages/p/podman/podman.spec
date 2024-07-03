#
# spec file for package podman
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


%{!?_user_tmpfilesdir: %global _user_tmpfilesdir %{_datadir}/user-tmpfiles.d}
%define project        github.com/containers/podman

%bcond_without  apparmor

Name:           podman
Version:        5.1.1
Release:        0
Summary:        Daemon-less container engine for managing containers, pods and images
License:        Apache-2.0
Group:          System/Management
URL:            https://%{project}
Source0:        %{name}-%{version}.tar.gz
Source1:        podman.conf
Patch0:         0001-Backport-fix-for-CVE-2024-6104.patch
BuildRequires:  man
BuildRequires:  bash-completion
BuildRequires:  device-mapper-devel
BuildRequires:  fdupes
BuildRequires:  git-core
BuildRequires:  glib2-devel-static
BuildRequires:  glibc-devel-static
BuildRequires:  go-go-md2man
BuildRequires:  golang-packaging
%if %{with apparmor}
BuildRequires:  libapparmor-devel
%endif
BuildRequires:  libassuan-devel
BuildRequires:  libbtrfs-devel
BuildRequires:  libcontainers-common
BuildRequires:  libgpgme-devel
BuildRequires:  libostree-devel
BuildRequires:  libseccomp-devel
# at least go 1.18 is needed from go.mod
BuildRequires:  golang(API) >= 1.21
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(systemd)
%if %{with apparmor}
Recommends:     apparmor-abstractions
Recommends:     apparmor-parser
%endif
# requirement for `podman machine`
Recommends:     gvisor-tap-vsock
Requires:       catatonit >= 0.1.7
Requires:       conmon >= 2.0.24
Requires:       fuse-overlayfs
Requires:       iptables
Requires:       libcontainers-common >= 20230214
%if 0%{?sle_version} && 0%{?sle_version} <= 150500
# Build podman with CNI support for SLE-15-SP5 and lower
Requires:       (netavark or cni-plugins)
# We still want users with fresh installation to start off
# with Netavark but if they already have cni-plugins installed
# and are attempting a migration, it's better to continue with cni
Suggests:       netavark
%else
Requires:       netavark
%endif
# use crun on Tumbleweed & ALP for WASM support
%if 0%{suse_version} >= 1600
# crun is only available for selected archs (because of criu)
%ifarch x86_64 aarch64 ppc64le armv7l armv7hl s390x
Requires:       crun
%else
Requires:       runc >= 1.0.1
%endif
%else
Requires:       runc >= 1.0.1
%endif
Requires:       passt
Requires:       timezone
Suggests:       katacontainers

# deprecate unused podman-cni-config subpackage
Provides:       %{name}-cni-config = %{version}
Obsoletes:      %{name}-cni-config < 4.5.1

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
Summary:        Client for managing podman containers remotely
Group:          System/Management
Conflicts:      %{name} < 3.1.2
Provides:       podman:%{_bindir}/%{name}-remote

%description remote
This client allows controlling podman on a separate host, e.g. over SSH.

%package docker
Summary:        Emulate Docker CLI using podman
BuildArch:      noarch
Requires:       %{name} = %{version}
Conflicts:      docker
Conflicts:      docker-ce
Conflicts:      docker-ee
Conflicts:      docker-latest
Conflicts:      moby-engine
Provides:       docker

%description docker
This package installs a script named docker that emulates the Docker CLI by
executes podman commands, it also creates links between all Docker CLI man
pages and %{name}.

%package -n %{name}sh
Summary:        Confined login and user shell using %{name}
Requires:       %{name} = %{version}
Provides:       %{name}-%{name}sh = %{version}
Provides:       %{name}-shell = %{version}

%description -n %{name}sh
%{name}sh provides a confined login and user shell with access to volumes and
capabilities specified in user quadlets.

It is a symlink to %{_bindir}/%{name} and execs into the `%{name}sh` container
when `%{_bindir}/%{name}sh is set as a login shell or set as os.Args[0].

%build
# Build podman
BUILDTAGS="$(hack/apparmor_tag.sh) \
    $(hack/btrfs_installed_tag.sh) \
    $(hack/btrfs_tag.sh) \
    $(hack/systemd_tag.sh) \
    $(hack/libsubid_tag.sh) \
    exclude_graphdriver_devicemapper \
    seccomp"

%if 0%{?sle_version} && 0%{?sle_version} <= 150500
# Podman >= 5.0.0 disables CNI support by default,
# update buildtags to build podman with CNI support
# for SLE-15-SP5 and lower.
BUILDTAGS="cni $BUILDTAGS"
%endif

BUILDFLAGS="-buildmode=pie" BUILDTAGS="$BUILDTAGS" PREFIX=%{_prefix} %make_build

# Build manpages
%make_build docs

%check
# Too many tests fail due to the restricted permissions in the build enviroment.
# Updates must be tested manually.

%install
%make_install PREFIX=%{_prefix} LIBEXECDIR=%{_libexecdir} ETCDIR=%{_sysconfdir} \
    install.completions \
    install.docker

# remove the user tmpfile on SLE/Leap as it cannot handle them
%if 0%{?suse_version} == 1500
rm %{buildroot}%{_user_tmpfilesdir}/podman-docker.conf
%endif

# Add podman modprobe.d drop-in config
# https://bugzilla.redhat.com/show_bug.cgi?id=1703261
mkdir -p %{buildroot}%{_prefix}/lib/modules-load.d
install -m 0644 -t %{buildroot}%{_prefix}/lib/modules-load.d/ %{SOURCE1}

%fdupes %{buildroot}/%{_datadir}
%fdupes %{buildroot}/%{_systemd_util_dir}

%files
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

%files docker
%{_bindir}/docker
%{_tmpfilesdir}/podman-docker.conf
%{_sysconfdir}/profile.d/%{name}-docker.*
%if 0%{?suse_version} > 1500
%{_user_tmpfilesdir}/podman-docker.conf
%dir %{_user_tmpfilesdir}
%endif

%files -n %{name}sh
%license LICENSE
%doc README.md CONTRIBUTING.md install.md transfer.md
%{_bindir}/%{name}sh

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
