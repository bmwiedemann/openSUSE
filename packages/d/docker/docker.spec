#
# spec file for package docker
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
# nodebuginfo


%bcond_without  apparmor

# This subpackage is only used for testing by developers, and shouldn't be
# built for actual users.
%bcond_with     integration_tests

%if 0%{?is_opensuse} == 0 && 0%{?suse_version} < 1600
# SUSEConnect support ("SUSE secrets") only makes sense for SLES hosts.
%bcond_without  suseconnect
%else
%bcond_with     suseconnect
%endif
# BuildKit (docker-buildx) is only provided for SLE >= 15 and openSUSE.
%if 0%{?is_opensuse} || 0%{?suse_version} >= 1500
%bcond_without  buildx
%else
%bcond_with     buildx
%endif

# The flavour is defined with a macro to try to keep docker and docker-stable
# as similar as possible, to make maintenance a little easier.
%define flavour %{nil}

# Where important update information will be stored, such that an administrator
# is guaranteed to see the relevant warning.
%define update_messages %{_localstatedir}/adm/update-messages/%{name}-%{version}-%{release}

# Test binaries.
%define testdir /usr/src/docker-test

#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

# MANUAL: This needs to be updated with every docker update.
%define docker_real_version 28.4.0
%define docker_git_version 249d679a6
%define docker_version %{docker_real_version}_ce
# This "nice version" is so that docker --version gives a result that can be
# parsed by other people. boo#1182476
%define docker_nice_version %{docker_real_version}-ce

%if %{with buildx}
# MANUAL: This needs to be updated with every docker-buildx update.
%define buildx_version 0.28.0
%endif

# Used when generating the "build" information for Docker version. The value of
# git_commit_epoch is unused here (we use SOURCE_DATE_EPOCH, which rpm
# helpfully injects into our build environment from the changelog). If you want
# to generate a new git_commit_epoch, use this:
#  $ date --date="$(git show --format=fuller --date=iso $COMMIT_ID | grep -oP '(?<=^CommitDate: ).*')" '+%s'
%define git_commit_epoch 1756931329

Name:           docker%{flavour}
Version:        %{docker_version}
Release:        0
Summary:        The Moby-project Linux container runtime
License:        Apache-2.0
Group:          System/Management
URL:            http://www.docker.io
Source:         docker-%{docker_version}_%{docker_git_version}.tar.xz
Source1:        docker-cli-%{docker_version}.tar.xz
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
# docker-integration-tests-devel
Source900:      docker-integration.sh
# NOTE: All of these patches are maintained in <https://github.com/suse/docker>
#       in the suse-v<version> branch. Make sure you update the patches in that
#       branch and then git-format-patch the patch here.
# SUSE-FEATURE: Adds the /run/secrets mountpoint inside all Docker containers
#               which is not snapshotted when images are committed.
Patch100:       0001-SECRETS-SUSE-always-clear-our-internal-secrets.patch
Patch101:       0002-SECRETS-daemon-allow-directory-creation-in-run-secre.patch
Patch102:       0003-SECRETS-SUSE-implement-SUSE-container-secrets.patch
Patch901:       cli-0001-openSUSE-point-users-to-docker-buildx-package.patch
Patch902:       cli-0002-SECRETS-SUSE-default-to-DOCKER_BUILDKIT-0-for-docker.patch
# UPSTREAM: Revert of upstream patch to keep SLE-12 build working.
Patch200:       0004-BUILD-SLE12-revert-graphdriver-btrfs-use-kernel-UAPI.patch
# UPSTREAM: Backport of <https://github.com/moby/moby/pull/41954>.
Patch201:       0005-bsc1073877-apparmor-clobber-docker-default-profile-o.patch
# UPSTREAM: Revert of upstream patches to make apparmor work on SLE 12.
Patch202:       0006-SLE12-revert-apparmor-remove-version-conditionals-fr.patch
BuildRequires:  audit
BuildRequires:  bash-completion
BuildRequires:  ca-certificates
BuildRequires:  fdupes
%if %{with apparmor}
BuildRequires:  libapparmor-devel
%endif
BuildRequires:  fish
BuildRequires:  go-go-md2man
BuildRequires:  libbtrfs-devel >= 3.8
BuildRequires:  libseccomp-devel >= 2.2
BuildRequires:  libtool
BuildRequires:  linux-glibc-devel
BuildRequires:  procps
BuildRequires:  sqlite3-devel
BuildRequires:  sysuser-tools
BuildRequires:  zsh
BuildRequires:  golang(API) = 1.24
BuildRequires:  pkgconfig(libsystemd)
%if %{with apparmor}
%if 0%{?suse_version} >= 1500
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
%if 0%{?suse_version} >= 1500
# This conditional only works on rpm>=4.13, which SLE 12 doesn't have. But we
# don't need to support Docker+selinux for SLE 12 anyway.
Requires:       (container-selinux if selinux-policy)
%else
Requires:       container-selinux
%endif
%endif
Requires:       ca-certificates-mozilla
# The docker-proxy binary used to be in a separate package. We obsolete it,
# since now docker-proxy is maintained as part of this package.
Obsoletes:      docker-libnetwork < 0.7.0.2
Provides:       docker-libnetwork = 0.7.0.2.%{docker_version}
# docker-stable cannot be used alongside docker.
%if "%{name}" == "docker-stable"
Provides:       docker = %{docker_version}
Obsoletes:      docker < %{docker_version}
Conflicts:      docker
%else
Conflicts:      docker-stable
%endif
# Required to actually run containers. We require the minimum version that is
# pinned by Docker, but in order to avoid headaches we allow for updates.
Requires:       runc >= 1.1.9
Requires:       containerd >= 1.7.3
# Needed for --init support. We don't use "tini", we use our own implementation
# which handles edge-cases better.
Requires:       catatonit
Requires:       iproute2 >= 3.5
Requires:       iptables >= 1.4
Requires:       procps
Requires:       tar >= 1.26
Requires:       xz >= 4.9
%if %{with buildx}
# Standard docker-build is deprecated, so require docker-buildx to avoid users
# hitting bugs that have long since been fixed by docker-buildx. bsc#1230331
Requires:       %{name}-buildx
%endif
%?sysusers_requires
Requires(post): %fillup_prereq
Requires(post): udev
Requires(post): shadow
Recommends:     %{name}-rootless-extras
Recommends:     git-core >= 1.7
ExcludeArch:    s390 ppc

%description
Docker complements LXC with a high-level API which operates at the process
level. It runs unix processes with strong guarantees of isolation and
repeatability across servers.

Docker is a great building block for automating distributed systems: large-scale
web deployments, database clusters, continuous deployment systems, private PaaS,
service-oriented architectures, etc.

%if %{with buildx}
%package buildx
Version:        %{buildx_version}
Summary:        Docker CLI plugin for extended build capabilities with BuildKit
License:        Apache-2.0
URL:            https://github.com/docker/buildx
Source500:      docker-buildx-%{buildx_version}.tar.xz
Group:          System/Management
Requires:       %{name} >= 19.03.0_ce
# docker-stable cannot be used alongside docker.
%if "%{name}" == "docker-stable"
Provides:       docker-buildx = %{buildx_version}
Obsoletes:      docker-buildx < %{buildx_version}
Conflicts:      docker-buildx
%else
Conflicts:      docker-stable-buildx
%endif

%description buildx
buildx is a Docker CLI plugin for extended build capabilities with BuildKit.

Key features:
- Familiar UI from docker build
- Full BuildKit capabilities with container driver
- Multiple builder instance support
- Multi-node builds for cross-platform images
- Compose build support
- High-level build constructs (bake)
- In-container driver support (both Docker and Kubernetes)
%endif

%package rootless-extras
Summary:        Rootless support for Docker
Group:          System/Management
Requires:       %{name} = %{docker_version}
Requires:       fuse-overlayfs >= 0.7
Requires:       rootlesskit
Requires:       slirp4netns >= 0.4
BuildArch:      noarch
# docker-stable cannot be used alongside docker.
%if "%{name}" == "docker-stable"
Provides:       docker-rootless-extras = %{docker_version}
Obsoletes:      docker-rootless-extras < %{docker_version}
Conflicts:      docker-rootless-extras
%else
Conflicts:      docker-stable-rootless-extras
%endif

%description rootless-extras
Rootless support for Docker.
Use dockerd-rootless.sh to run the daemon.
Use dockerd-rootless-setuptool.sh to setup systemd for dockerd-rootless.sh.

%if %{with integration_tests}
%package integration-tests-devel
Summary:        Rootless support for Docker
Group:          TestSuite
Requires:       %{name} = %{docker_version}
Requires:       containerd-ctr
Requires:       curl
Requires:       gcc
Requires:       git
Requires:       glibc-devel-static
Requires:       go
Requires:       jq
Requires:       libcap-progs

%description integration-tests-devel
Integration testing binaries for Docker.

THIS PACKAGE SHOULD NOT BE INSTALLED BY END-USERS, IT IS ONLY INTENDED FOR
INTERNAL DEVELOPMENT OF THE DOCKER PACKAGE FOR (OPEN)SUSE.
%endif

%package bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{docker_version}
Requires:       bash-completion
Supplements:    packageand(%{name}:bash-completion)
BuildArch:      noarch
# docker-stable cannot be used alongside docker.
%if "%{name}" == "docker-stable"
Provides:       docker-bash-completion = %{docker_version}
Obsoletes:      docker-bash-completion < %{docker_version}
Conflicts:      docker-bash-completion
%else
Conflicts:      docker-stable-bash-completion
%endif

%description bash-completion
Bash command line completion support for %{name}.

%package zsh-completion
Summary:        Zsh Completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{docker_version}
Requires:       zsh
Supplements:    packageand(%{name}:zsh)
BuildArch:      noarch
# docker-stable cannot be used alongside docker.
%if "%{name}" == "docker-stable"
Provides:       docker-zsh-completion = %{docker_version}
Obsoletes:      docker-zsh-completion < %{docker_version}
Conflicts:      docker-zsh-completion
%else
Conflicts:      docker-stable-zsh-completion
%endif

%description zsh-completion
Zsh command line completion support for %{name}.

%package fish-completion
Summary:        Fish completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{docker_version}
Requires:       fish
Supplements:    packageand(%{name}:fish)
BuildArch:      noarch
# docker-stable cannot be used alongside docker.
%if "%{name}" == "docker-stable"
Provides:       docker-fish-completion = %{docker_version}
Obsoletes:      docker-fish-completion < %{docker_version}
Conflicts:      docker-fish-completion
%else
Conflicts:      docker-stable-fish-completion
%endif

%description fish-completion
Fish command line completion support for %{name}.

%prep
# docker-cli
%define cli_builddir %{_builddir}/docker-cli-%{docker_version}
%setup -q -T -b 1 -n docker-cli-%{docker_version}
[ "%{cli_builddir}" = "$PWD" ]
%if %{with buildx}
%patch -P901 -p1
%if %{with suseconnect}
# PATCH-SUSE: Secrets patch for docker-build.
%patch -P902 -p1
%endif
%endif

%if %{with buildx}
# docker-buildx
%define buildx_builddir %{_builddir}/docker-buildx-%{buildx_version}
%setup -q -T -b 500 -n docker-buildx-%{buildx_version}
[ "%{buildx_builddir}" = "$PWD" ]
%endif

# docker
%define docker_builddir %{_builddir}/docker-%{docker_version}_%{docker_git_version}
%setup -q -n docker-%{docker_version}_%{docker_git_version}
[ "%{docker_builddir}" = "$PWD" ]
# README_SUSE.md for documentation.
cp %{SOURCE130} .

# bsc#1244035 (secrets patch to remove unreferenced secrets -- always applies).
%patch -P100 -p1
%if %{with suseconnect}
# PATCH-SUSE: Secrets patches.
%patch -P101 -p1
%patch -P102 -p1
%endif
%if 0%{?sle_version} == 120000
# Patches to build on SLE-12.
%patch -P200 -p1
%endif
# bsc#1099277
%patch -P201 -p1
# Solves apparmor issues on SLE-12, but okay for newer SLE versions too.
%patch -P202 -p1

%build
%sysusers_generate_pre %{SOURCE160} %{name} docker.conf

BUILDTAGS="apparmor selinux seccomp pkcs11"

export AUTO_GOPATH=1
# Make sure we always build PIC code. bsc#1048046
export BUILDFLAGS="-buildmode=pie"
# Specify all of the versioning information. We use SOURCE_DATE_EPOCH if it's
# been injected by rpmbuild, otherwise we use the hardcoded git_commit_epoch
# generated above. boo#1064781
export VERSION="%{docker_nice_version}"
export DOCKER_GITCOMMIT="%{docker_git_version}"
export GITCOMMIT="%{docker_git_version}"
export SOURCE_DATE_EPOCH="${SOURCE_DATE_EPOCH:-%{git_commit_epoch}}"
export BUILDTIME="$(date -u -d "@$SOURCE_DATE_EPOCH" --rfc-3339 ns 2>/dev/null | sed -e 's/ /T/')"

###################
## DOCKER ENGINE ##
###################

pushd "%{docker_builddir}"
# use go module for build
cp {vendor,go}.mod
cp {vendor,go}.sum
./hack/make.sh dynbinary
# dockerd man page
GO_MD2MAN=go-md2man make -C ./man/

%if %{with integration_tests}
# build test binaries for integration tests
readarray -t integration_dirs \
	<<<"$(go list -test -f '{{- if ne .ForTest "" -}}{{- .Dir -}}{{- end -}}' ./integration/... ./integration-cli/...)"
for dir in "${integration_dirs[@]}"
do
	pushd "$dir"
	go test -c -buildmode=pie -tags "$BUILDTAGS" -o test.main .
	popd
done
# Update __DOCKER_BUILDIR in the integration testing script.
sed -i 's|^__DOCKER_BUILDIR=.*|__DOCKER_BUILDIR=%{docker_builddir}|g' "%{SOURCE900}"
%endif

popd

###################
## DOCKER CLIENT ##
###################

pushd "%{cli_builddir}"
# use go module for build
cp {vendor,go}.mod
cp {vendor,go}.sum
make DISABLE_WARN_OUTSIDE_CONTAINER=1 dynbinary manpages
popd

%if %{with buildx}
###################
## DOCKER BUILDX ##
###################

pushd "%{buildx_builddir}"
make \
	CGO_ENABLED=1 \
	VERSION="%{buildx_version}" \
	REVISION="v%{buildx_version}" \
	GO_EXTRA_FLAGS="-buildmode=pie" \
	build
popd
%endif

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
%if %{with buildx}
# buildx plugin
install -D -m0755 %{buildx_builddir}/bin/build/docker-buildx %{buildroot}/usr/lib/docker/cli-plugins/docker-buildx
%endif

# /var/lib/docker
install -d %{buildroot}/%{_localstatedir}/lib/docker
# daemon.json config file
install -D -m0644 %{SOURCE150} %{buildroot}%{_sysconfdir}/docker/daemon.json
%if %{with suseconnect}
# SUSE-specific config file
echo 1 > %{buildroot}%{_sysconfdir}/docker/suse-secrets-enable
%endif

# docker cli
install -D -m0755 %{cli_builddir}/build/docker %{buildroot}/%{_bindir}/docker
install -D -m0644 %{cli_builddir}/contrib/completion/bash/docker "%{buildroot}%{_datarootdir}/bash-completion/completions/docker"
install -D -m0644 %{cli_builddir}/contrib/completion/zsh/_docker "%{buildroot}%{_sysconfdir}/zsh_completion.d/_docker"
install -D -m0644 %{cli_builddir}/contrib/completion/fish/docker.fish "%{buildroot}/%{_datadir}/fish/vendor_completions.d/docker.fish"

# systemd service
install -D -m0644 %{SOURCE100} %{buildroot}%{_unitdir}/docker.service
install -D -m0644 %{SOURCE101} %{buildroot}%{_unitdir}/docker.socket
ln -sf service %{buildroot}%{_sbindir}/rcdocker

# udev rules that prevents dolphin to show all docker devices and slows down
# upstream report https://bugs.kde.org/show_bug.cgi?id=329930
install -D -m0644 %{SOURCE110} %{buildroot}%{_udevrulesdir}/80-docker.rules

# audit rules
install -D -m0640 %{SOURCE140} %{buildroot}%{_sysconfdir}/audit/rules.d/docker.rules

# sysconfig file
install -D -m0644 %{SOURCE120} %{buildroot}%{_fillupdir}/sysconfig.docker

# install manpages (using the ones from the engine)
for mansrcdir in %{cli_builddir}/man/man[1-9] %{docker_builddir}/man/man[1-9]
do
	section="$(basename $mansrcdir)"
	install -d %{buildroot}%{_mandir}/$section
	install -p -m0644 $mansrcdir/* %{buildroot}%{_mandir}/$section
done

# sysusers.d
install -D -m0644 %{SOURCE160} %{buildroot}%{_sysusersdir}/docker.conf

# rootless extras
install -D -p -m 0755 contrib/dockerd-rootless.sh %{buildroot}/%{_bindir}/dockerd-rootless.sh
install -D -p -m 0755 contrib/dockerd-rootless-setuptool.sh %{buildroot}/%{_bindir}/dockerd-rootless-setuptool.sh

%if %{with integration_tests}
# integration tests
install -d %{buildroot}%{testdir}
cp -ar %{docker_builddir} %{buildroot}%{testdir}/src
install -d %{buildroot}%{testdir}/bin
install -D -p -m 0755 %{SOURCE900} %{buildroot}%{testdir}/docker-integration.sh
# remove all of the non-test binaries in bundles/
rm -rfv %{buildroot}%{testdir}/src/bundles/
%endif

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

%service_add_pre docker.service docker.socket

%post
%service_add_post docker.service docker.socket
%{fillup_only -n docker}

%preun
%service_del_preun docker.service docker.socket

%postun
%service_del_postun docker.service docker.socket

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

%{_unitdir}/docker.service
%{_unitdir}/docker.socket
%{_sysusersdir}/docker.conf

%dir %{_sysconfdir}/docker
%config(noreplace) %{_sysconfdir}/docker/daemon.json
%if %{with suseconnect}
%config(noreplace) %{_sysconfdir}/docker/suse-secrets-enable
%endif
%{_fillupdir}/sysconfig.docker

%dir %attr(750,root,root) %{_sysconfdir}/audit/rules.d
%config %{_sysconfdir}/audit/rules.d/docker.rules
%{_udevrulesdir}/80-docker.rules

%{_mandir}/man*/*%{ext_man}

%if %{with buildx}
%files buildx
%defattr(-,root,root)
/usr/lib/docker/cli-plugins/docker-buildx
%endif

%files rootless-extras
%defattr(-,root,root)
%{_bindir}/dockerd-rootless.sh
%{_bindir}/dockerd-rootless-setuptool.sh

%if %{with integration_tests}
%files integration-tests-devel
%defattr(-,root,root)
%{testdir}
%endif

%files bash-completion
%defattr(-,root,root)
%{_datarootdir}/bash-completion/completions/docker

%files zsh-completion
%defattr(-,root,root)
%{_sysconfdir}/zsh_completion.d/_docker

%files fish-completion
%defattr(-,root,root)
%{_datadir}/fish/vendor_completions.d/docker.fish

%changelog
