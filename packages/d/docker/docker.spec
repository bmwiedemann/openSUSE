#
# spec file for package docker
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
# nodebuginfo

%bcond_without  apparmor

# Where important update information will be stored, such that an administrator
# is guaranteed to see the relevant warning.
%define update_messages %{_localstatedir}/adm/update-messages/%{name}-%{version}-%{release}

#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

# Used when generating the "build" information for Docker version. The value of
# git_commit_epoch is unused here (we use SOURCE_DATE_EPOCH, which rpm
# helpfully injects into our build environment from the changelog). If you want
# to generate a new git_commit_epoch, use this:
#  $ date --date="$(git show --format=fuller --date=iso $COMMIT_ID | grep -oP '(?<=^CommitDate: ).*')" '+%s'
%define real_version 26.1.4
%define git_version de5c9cf0b96e
%define git_commit_epoch 1717583601

Name:           docker
Version:        %{real_version}_ce
# This "nice version" is so that docker --version gives a result that can be
# parsed by other people. boo#1182476
%define nice_version %{real_version}-ce
Release:        0
Summary:        The Moby-project Linux container runtime
License:        Apache-2.0
Group:          System/Management
URL:            http://www.docker.io
Source:         %{name}-%{version}_%{git_version}.tar.xz
Source1:        %{name}-cli-%{version}.tar.xz
Source3:        docker-rpmlintrc
# TODO: Move these source files to somewhere nicer.
Source100:      docker.service
Source101:      docker.socket
Source110:      80-docker.rules
Source120:      sysconfig.docker
Source130:      README_SUSE.md
Source140:      docker-audit.rules
Source150:      docker-daemon.json
Source160:      docker.sysusers
# NOTE: All of these patches are maintained in <https://github.com/suse/docker>
#       in the suse-v<version> branch. Make sure you update the patches in that
#       branch and then git-format-patch the patch here.
# SUSE-FEATURE: Adds the /run/secrets mountpoint inside all Docker containers
#               which is not snapshotted when images are committed.
Patch100:       0001-SECRETS-daemon-allow-directory-creation-in-run-secre.patch
Patch101:       0002-SECRETS-SUSE-implement-SUSE-container-secrets.patch
# UPSTREAM: Revert of upstream patch to keep SLE-12 build working.
Patch200:       0003-BUILD-SLE12-revert-graphdriver-btrfs-use-kernel-UAPI.patch
# UPSTREAM: Backport of <https://github.com/moby/moby/pull/41954>.
Patch201:       0004-bsc1073877-apparmor-clobber-docker-default-profile-o.patch
# UPSTREAM: Revert of upstream patches to make apparmor work on SLE 12.
Patch202:       0005-SLE12-revert-apparmor-remove-version-conditionals-fr.patch
# UPSTREAM: Backport of <https://github.com/moby/buildkit/pull/4896> and
#           <https://github.com/moby/buildkit/pull/5060>.
Patch203:       0006-bsc1221916-update-to-patched-buildkit-version-to-fix.patch
# UPSTREAM: Backport of <https://github.com/moby/moby/pull/48034>.
Patch204:       0007-bsc1214855-volume-use-AtomicWriteFile-to-save-volume.patch
# UPSTREAM: Backport of <https://github.com/docker/cli/pull/4228>.
Patch900:       cli-0001-docs-include-required-tools-in-source-tree.patch
BuildRequires:  audit
BuildRequires:  bash-completion
BuildRequires:  ca-certificates
BuildRequires:  device-mapper-devel >= 1.2.68
BuildRequires:  fdupes
%if %{with apparmor}
BuildRequires:  libapparmor-devel
%endif
BuildRequires:  libbtrfs-devel >= 3.8
BuildRequires:  libseccomp-devel >= 2.2
BuildRequires:  libtool
BuildRequires:  linux-glibc-devel
BuildRequires:  procps
BuildRequires:  sqlite3-devel
BuildRequires:  zsh
BuildRequires:  fish
BuildRequires:  go-go-md2man
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  sysuser-tools
BuildRequires:  golang(API) = 1.21
%if %{with apparmor}
%if 0%{?sle_version} >= 150000
# This conditional only works on rpm>=4.13, which SLE 12 doesn't have. But we
# don't need to support Docker+selinux for SLE 12 anyway.
Requires:       (apparmor-parser or container-selinux)
# This recommends is added to make sure that even if you have container-selinux
# installed you will still be prompted to install apparmor-parser which Docker
# requires to apply AppArmor profiles (for SELinux systems this doesn't matter
# but if you switch back to AppArmor on reboot this would result in insecure
# containers).
Recommends:     apparmor-parser
%else
Requires:       apparmor-parser
%endif
%else
Requires:       container-selinux
%endif
Requires:       ca-certificates-mozilla
# The docker-proxy binary used to be in a separate package. We obsolete it,
# since now docker-proxy is maintained as part of this package.
Obsoletes:      docker-libnetwork < 0.7.0.2
Provides:       docker-libnetwork = 0.7.0.2.%{version}
# Required to actually run containers. We require the minimum version that is
# pinned by Docker, but in order to avoid headaches we allow for updates.
Requires:       runc >= 1.1.9
Requires:       containerd >= 1.7.3
# Needed for --init support. We don't use "tini", we use our own implementation
# which handles edge-cases better.
Requires:       catatonit
# Provides mkfs.ext4 - used by Docker when devicemapper storage driver is used
Requires:       e2fsprogs
Requires:       iproute2 >= 3.5
Requires:       iptables >= 1.4
Requires:       procps
Requires:       tar >= 1.26
Requires:       xz >= 4.9
%?sysusers_requires
Requires(post): %fillup_prereq
Requires(post): udev
Requires(post): shadow
# Not necessary, but must be installed when the underlying system is
# configured to use lvm and the user doesn't explicitly provide a
# different storage-driver than devicemapper
Recommends:     lvm2 >= 2.2.89
Recommends:     git-core >= 1.7
# Required for "docker buildx" support.
Recommends:     %{name}-buildx
Recommends:     %{name}-rootless-extras
ExcludeArch:    s390 ppc

%description
Docker complements LXC with a high-level API which operates at the process
level. It runs unix processes with strong guarantees of isolation and
repeatability across servers.

Docker is a great building block for automating distributed systems: large-scale
web deployments, database clusters, continuous deployment systems, private PaaS,
service-oriented architectures, etc.

%package rootless-extras
Summary:        Rootless support for Docker
Group:          System/Management
Requires:       %{name} = %{version}
Requires:       slirp4netns >= 0.4
Requires:       fuse-overlayfs >= 0.7
Requires:       rootlesskit
BuildArch:      noarch

%description rootless-extras
Rootless support for Docker.
Use dockerd-rootless.sh to run the daemon.
Use dockerd-rootless-setuptool.sh to setup systemd for dockerd-rootless.sh.

%package bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    packageand(%{name}:bash-completion)
BuildArch:      noarch

%description bash-completion
Bash command line completion support for %{name}.

%package zsh-completion
Summary:        Zsh Completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Requires:       zsh
Supplements:    packageand(%{name}:zsh)
BuildArch:      noarch

%description zsh-completion
Zsh command line completion support for %{name}.

%package fish-completion
Summary:        Fish completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Requires:       fish
Supplements:    packageand(%{name}:fish)
BuildArch:      noarch

%description fish-completion
Fish command line completion support for %{name}.

%prep
# docker-cli
%define cli_builddir %{_builddir}/%{name}-cli-%{version}
%setup -q -T -b 1 -n %{name}-cli-%{version}
[ "%{cli_builddir}" = "$PWD" ]
# offline manpages
%patch -P900 -p1

# docker
%define docker_builddir %{_builddir}/%{name}-%{version}_%{git_version}
%setup -q -n %{name}-%{version}_%{git_version}
[ "%{docker_builddir}" = "$PWD" ]
# README_SUSE.md for documentation.
cp %{SOURCE130} .

%if 0%{?is_opensuse} == 0
# PATCH-SUSE: Secrets patches.
%patch -P100 -p1
%patch -P101 -p1
%endif
%if 0%{?sle_version} == 120000
# Patches to build on SLE-12.
%patch -P200 -p1
%endif
# bsc#1099277
%patch -P201 -p1
# Solves apparmor issues on SLE-12, but okay for newer SLE versions too.
%patch -P202 -p1
# bsc#1221916
%patch -P203 -p1
# bsc#1214855
%patch -P204 -p1

%build
%sysusers_generate_pre %{SOURCE160} %{name} %{name}.conf

BUILDTAGS="exclude_graphdriver_aufs apparmor selinux seccomp pkcs11"
%if 0%{?sle_version} == 120000
	# Allow us to build with older distros but still have deferred removal
	# support at runtime. We only use this when building on SLE12, because
	# later openSUSE/SLE versions have a new enough libdevicemapper to not
	# require the runtime checking.
	BUILDTAGS="libdm_dlsym_deferred_remove $BUILDTAGS"
%endif

export AUTO_GOPATH=1
# Make sure we always build PIC code. bsc#1048046
export BUILDFLAGS="-buildmode=pie"
# Specify all of the versioning information. We use SOURCE_DATE_EPOCH if it's
# been injected by rpmbuild, otherwise we use the hardcoded git_commit_epoch
# generated above. boo#1064781
export VERSION="%{nice_version}"
export DOCKER_GITCOMMIT="%{git_version}"
export GITCOMMIT="%{git_version}"
export SOURCE_DATE_EPOCH="${SOURCE_DATE_EPOCH:-%{git_commit_epoch}}"
export BUILDTIME="$(date -u -d "@$SOURCE_DATE_EPOCH" --rfc-3339 ns 2>/dev/null | sed -e 's/ /T/')"

###################
## DOCKER ENGINE ##
###################

pushd "%{docker_builddir}"
# use go module for build
ln -s {vendor,go}.mod
ln -s {vendor,go}.sum
./hack/make.sh dynbinary
popd

###################
## DOCKER CLIENT ##
###################

pushd "%{cli_builddir}"
# use go module for build
ln -s {vendor,go}.mod
ln -s {vendor,go}.sum
make DISABLE_WARN_OUTSIDE_CONTAINER=1 dynbinary manpages
popd

%install
install -Dd -m0755 \
	%{buildroot}%{_sysconfdir}/init.d \
	%{buildroot}%{_bindir} \
	%{buildroot}%{_sbindir}

# docker daemon
install -D -m0755 %{docker_builddir}/bundles/dynbinary-daemon/dockerd %{buildroot}/%{_bindir}/dockerd
# docker proxy
install -D -m0755 %{docker_builddir}/bundles/dynbinary-daemon/docker-proxy %{buildroot}/%{_bindir}/docker-proxy

# cli-plugins/
install -d %{buildroot}/usr/lib/docker/cli-plugins

# /var/lib/docker
install -d %{buildroot}/%{_localstatedir}/lib/docker
# daemon.json config file
install -D -m0644 %{SOURCE150} %{buildroot}%{_sysconfdir}/docker/daemon.json

# docker cli
install -D -m0755 %{cli_builddir}/build/docker %{buildroot}/%{_bindir}/docker
install -D -m0644 %{cli_builddir}/contrib/completion/bash/docker "%{buildroot}%{_datarootdir}/bash-completion/completions/%{name}"
install -D -m0644 %{cli_builddir}/contrib/completion/zsh/_docker "%{buildroot}%{_sysconfdir}/zsh_completion.d/_%{name}"
install -D -m0644 %{cli_builddir}/contrib/completion/fish/docker.fish "%{buildroot}/%{_datadir}/fish/vendor_completions.d/%{name}.fish"

# systemd service
install -D -m0644 %{SOURCE100} %{buildroot}%{_unitdir}/%{name}.service
install -D -m0644 %{SOURCE101} %{buildroot}%{_unitdir}/%{name}.socket
ln -sf service %{buildroot}%{_sbindir}/rcdocker

# udev rules that prevents dolphin to show all docker devices and slows down
# upstream report https://bugs.kde.org/show_bug.cgi?id=329930
install -D -m0644 %{SOURCE110} %{buildroot}%{_udevrulesdir}/80-%{name}.rules

# audit rules
install -D -m0640 %{SOURCE140} %{buildroot}%{_sysconfdir}/audit/rules.d/%{name}.rules

# sysconfig file
install -D -m0644 %{SOURCE120} %{buildroot}%{_fillupdir}/sysconfig.docker

# install manpages (using the ones from the engine)
install -d %{buildroot}%{_mandir}/man1
install -p -m0644 %{cli_builddir}/man/man1/*.1 %{buildroot}%{_mandir}/man1
install -d %{buildroot}%{_mandir}/man5
install -p -m0644 %{cli_builddir}/man/man5/Dockerfile.5 %{buildroot}%{_mandir}/man5
install -d %{buildroot}%{_mandir}/man8
install -p -m0644 %{cli_builddir}/man/man8/*.8 %{buildroot}%{_mandir}/man8

# sysusers.d
install -D -m0644 %{SOURCE160} %{buildroot}%{_sysusersdir}/%{name}.conf

# rootless extras
install -D -p -m 0755 contrib/dockerd-rootless.sh %{buildroot}/%{_bindir}/dockerd-rootless.sh
install -D -p -m 0755 contrib/dockerd-rootless-setuptool.sh %{buildroot}/%{_bindir}/dockerd-rootless-setuptool.sh

%fdupes %{buildroot}

%pre -f %{name}.pre
# /etc/sub[ug]id should exist already (it's part of shadow-utils), but older
# distros don't have it. Docker just parses it and doesn't need any special
# shadow-utils helpers.
touch /etc/subuid /etc/subgid ||:

# "useradd -r" doesn't add sub[ug]ids so we manually add some. Hopefully there
# aren't any conflicts here, because usermod doesn't provide the same "get
# unusued range" feature that dockremap does.
grep -q '^dockremap:' /etc/subuid || \
	usermod -v 100000000-200000000 dockremap &>/dev/null || \
	echo "dockremap:100000000:100000001" >>/etc/subuid ||:
grep -q '^dockremap:' /etc/subgid || \
	usermod -w 100000000-200000000 dockremap &>/dev/null || \
	echo "dockremap:100000000:100000001" >>/etc/subgid ||:

%service_add_pre %{name}.service %{name}.socket

%post
%service_add_post %{name}.service %{name}.socket
%{fillup_only -n docker}

%preun
%service_del_preun %{name}.service %{name}.socket

%postun
%service_del_postun %{name}.service %{name}.socket

%files
%defattr(-,root,root)
%doc README.md README_SUSE.md
%license LICENSE
%{_bindir}/docker
%{_bindir}/dockerd
%{_bindir}/docker-proxy
%{_sbindir}/rcdocker
%dir %{_localstatedir}/lib/docker/

%dir /usr/lib/docker
%dir /usr/lib/docker/cli-plugins

%{_unitdir}/%{name}.service
%{_unitdir}/%{name}.socket
%{_sysusersdir}/%{name}.conf

%dir %{_sysconfdir}/docker
%config(noreplace) %{_sysconfdir}/docker/daemon.json
%{_fillupdir}/sysconfig.docker

%config %{_sysconfdir}/audit/rules.d/%{name}.rules
%{_udevrulesdir}/80-%{name}.rules

%{_mandir}/man1/docker-*.1%{ext_man}
%{_mandir}/man1/docker.1%{ext_man}
%{_mandir}/man5/Dockerfile.5%{ext_man}
%{_mandir}/man8/dockerd.8%{ext_man}

%files bash-completion
%defattr(-,root,root)
%{_datarootdir}/bash-completion/completions/%{name}

%files zsh-completion
%defattr(-,root,root)
%{_sysconfdir}/zsh_completion.d/_%{name}

%files fish-completion
%defattr(-,root,root)
%{_datadir}/fish/vendor_completions.d/%{name}.fish

%files rootless-extras
%defattr(-,root,root)
%{_bindir}/dockerd-rootless.sh
%{_bindir}/dockerd-rootless-setuptool.sh

%changelog
