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


%define project        github.com/containers/podman
# Build with libostree-devel in Tumbleweed, Leap 15 and SLES 15
%if 0%{?suse_version} >= 1500
%define with_libostree 1
%endif
Name:           podman
Version:        2.1.1
Release:        0
Summary:        Daemon-less container engine for managing containers, pods and images
License:        Apache-2.0
Group:          System/Management
Url:            https://github.com/containers/libpod
Source0:        %{name}-%{version}.tar.xz
Source1:        podman.conf
Source3:        %{name}-rpmlintrc
Source4:        README.SUSE.SLES
Patch0:         varlink.patch
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
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  golang(API) = 1.13
# Build fails with PIE enabled on ppc64le due to boo#1098017
%ifarch ppc64le
#!BuildIgnore: gcc-PIE
%endif
Recommends:     apparmor-parser
Recommends:     apparmor-abstractions
Requires:       cni
Requires:       cni-plugins
Requires:       conmon
Requires:       iptables
Requires:       libcontainers-common >= 20200727
Requires:       runc >= 1.0.0~rc4
Requires:       slirp4netns >= 0.4.0
Requires:       catatonit
Requires:       fuse-overlayfs
Recommends:     %{name}-cni-config = %{version}
Suggests:       katacontainers
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
%patch0 

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
# Build podman
BUILDFLAGS="-buildmode=pie" make

# Build manpages
make %{?_smp_mflags} docs

%check
# Too many tests fail due to the restricted permissions in the build enviroment.
# Updates must be tested manually.

%install
make DESTDIR=%{buildroot} PREFIX=/usr install
make DESTDIR=%{buildroot} PREFIX=/usr install.completions

# packaged in libcontainers-common
rm %{buildroot}/usr/share/man/man5/containers-mounts.conf.* %{buildroot}/usr/share/man/man5/oci-hooks.*

# Add podman modprobe.d drop-in config
mkdir -p %{buildroot}%{_prefix}/lib/modules-load.d
install -m 0644 -t %{buildroot}%{_prefix}/lib/modules-load.d/ %{SOURCE1}

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
# Configs
%dir %{_prefix}/lib/modules-load.d
%{_prefix}/lib/modules-load.d/podman.conf
# Completion
%{_datadir}/bash-completion/completions/podman
%{_datadir}/zsh/site-functions/_podman
%{_unitdir}/podman.service
%{_unitdir}/podman.socket
%{_unitdir}/podman-auto-update.service
%{_unitdir}/podman-auto-update.timer
%{_userunitdir}/podman.service
%{_userunitdir}/podman.socket
%{_userunitdir}/podman-auto-update.service
%{_userunitdir}/podman-auto-update.timer
%ghost /run/podman
%ghost  %{_localstatedir}/adm/update-messages/%{name}-%{version}-%{release}-libpodconf
%license LICENSE

%files cni-config
%config %{_sysconfdir}/cni/net.d/87-podman-bridge.conflist
%license LICENSE

%pre
%service_add_pre podman.service podman.socket
# move away any old rpmsave config file to avoid having it re-activated again in
# %posttrans
test -f /etc/containers/libpod.conf.rpmsave && mv -v /etc/containers/libpod.conf.rpmsave /etc/containers/libpod.conf.rpmsave.old ||:

%post
%service_add_post podman.service podman.socket

%preun
%service_del_preun podman.service podman.socket

%postun
%service_del_postun podman.service podman.socket

%posttrans
# if libpod.conf.rpmsave was created move it back into place and set an update
# message informing about the libpod.conf -> containers.conf change
if test -f /etc/containers/libpod.conf.rpmsave ; then
    mv -v /etc/containers/libpod.conf.rpmsave /etc/containers/libpod.conf ||:
    cat >> %{_localstatedir}/adm/update-messages/%{name}-%{version}-%{release}-libpodconf << EOF
WARNING: Podman configuration file changes

With version 2.0 Podman changed to a slightly different configuration file format.
Also the name of default configuration file has been changed. The new format is
documented in the containers.conf(5) man-page and changes should usually be
straight-forward.

The new default configuration is located in /usr/share/containers/containers.conf.
In order to override setting from that file you can create
/etc/containers/containers.conf with your changed settings.

For backwards compatibility Podman 2.0 is still able to read libpod.conf. The support
for this will go away in future releases. Please migrate your configuration to the new
format as soon as possible.
EOF
fi

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
