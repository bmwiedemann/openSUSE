#
# spec file for package docker
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
# nodebuginfo


# Where important update information will be stored, such that an administrator
# is guaranteed to see the relevant warning.
%define update_messages %{_localstatedir}/adm/update-messages/%{name}-%{version}-%{release}

#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

# Handle _multibuild magic.
%define flavour @BUILD_FLAVOR@%{nil}

# We split the Name: into "realname" and "name_suffix".
%define realname docker
%if "%flavour" == ""
%define name_suffix %{nil}
%else
%define name_suffix -%{flavour}
%endif

# Used when generating the "build" information for Docker version. The value of
# git_commit_epoch is unused here (we use SOURCE_DATE_EPOCH, which rpm
# helpfully injects into our build environment from the changelog). If you want
# to generate a new git_commit_epoch, use this:
#  $ date --date="$(git show --format=fuller --date=iso $COMMIT_ID | grep -oP '(?<=^CommitDate: ).*')" '+%s'
%define real_version 20.10.21
%define git_version 3056208812eb
%define git_commit_epoch 1666698255

# We require a specific pin of libnetwork because it doesn't really do
# versioning and minor version mismatches in libnetwork can break Docker
# networking. All other key runtime dependencies (containerd, runc) are stable
# enough that this isn't necessary.
%define libnetwork_version 0dde5c895075df6e3630e76f750a447cf63f4789

%define dist_builddir  %{_builddir}/dist-suse
%define cli_builddir   %{dist_builddir}/src/github.com/docker/cli
%define proxy_builddir %{dist_builddir}/src/github.com/docker/libnetwork

Name:           %{realname}%{name_suffix}
Version:        %{real_version}_ce
# This "nice version" is so that docker --version gives a result that can be
# parsed by other people. boo#1182476
%define nice_version %{real_version}-ce
Release:        0
Summary:        The Moby-project Linux container runtime
License:        Apache-2.0
Group:          System/Management
URL:            http://www.docker.io
Source:         %{realname}-%{version}_%{git_version}.tar.xz
Source1:        %{realname}-cli-%{version}.tar.xz
Source2:        %{realname}-libnetwork-%{libnetwork_version}.tar.xz
Source3:        docker-rpmlintrc
# TODO: Move these source files to somewhere nicer.
Source100:      docker.service
Source101:      80-docker.rules
Source102:      sysconfig.docker
Source103:      README_SUSE.md
Source104:      docker-audit.rules
Source105:      docker-daemon.json
Source106:      docker.sysusers
# Kubelet-specific sources.
# bsc#1086185 -- but we only apply this on Kubic.
Source900:      docker-kubic-service.conf
Source901:      kubelet.env
# NOTE: All of these patches are maintained in <https://github.com/suse/docker>
#       in the suse-<version> branch. Make sure you update the patches in that
#       branch and then git-format-patch the patch here.
# SUSE-FEATURE: Adds the /run/secrets mountpoint inside all Docker containers
#               which is not snapshotted when images are committed.
Patch100:       0001-SECRETS-daemon-allow-directory-creation-in-run-secre.patch
Patch101:       0002-SECRETS-SUSE-implement-SUSE-container-secrets.patch
# SUSE-FEATURE: Add support to mirror unofficial/private registries
#               <https://github.com/docker/docker/pull/34319>.
Patch200:       0003-PRIVATE-REGISTRY-add-private-registry-mirror-support.patch
# SUSE-BACKPORT: Backport of https://github.com/docker/docker/pull/37353. bsc#1073877 bsc#1099277
Patch300:       0004-bsc1073877-apparmor-clobber-docker-default-profile-o.patch
# SUSE-BACKPORT: Backport of https://github.com/moby/moby/pull/42273. bsc#1183855 bsc#1175081
Patch301:       0005-bsc1183855-btrfs-Do-not-disable-quota-on-cleanup.patch
# SUSE-BACKPORT: Backport of several golang.org/x/crypto updates.
#                bsc#1193930 CVE-2021-43565 bsc#1197284 CVE-2022-27191
Patch302:       0006-bsc1193930-vendor-update-golang.org-x-crypto.patch
# SUSE-BACKPORT: Backport of <https://github.com/containerd/fifo/pull/32>. bsc#1200022
Patch303:       0007-bsc1200022-fifo.Close-prevent-possible-panic-if-fifo.patch
BuildRequires:  audit
BuildRequires:  bash-completion
BuildRequires:  ca-certificates
BuildRequires:  device-mapper-devel >= 1.2.68
BuildRequires:  fdupes
BuildRequires:  libapparmor-devel
BuildRequires:  libbtrfs-devel >= 3.8
BuildRequires:  libseccomp-devel >= 2.2
BuildRequires:  libtool
BuildRequires:  procps
BuildRequires:  sqlite3-devel
BuildRequires:  zsh
BuildRequires:  fish
BuildRequires:  go-go-md2man
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  sysuser-tools
# Due to a limitation in openSUSE's Go packaging we cannot have a BuildRequires
# for 'golang(API) >= 1.18' here, so just require 1.18 exactly. bsc#1172608
BuildRequires:  go1.18
Requires:       (apparmor-parser or container-selinux)
Requires:       ca-certificates-mozilla
# The docker-proxy binary used to be in a separate package. We obsolete it,
# since now docker-proxy is maintained as part of this package.
Obsoletes:      docker-libnetwork%{name_suffix} < 0.7.0.2
Provides:       docker-libnetwork%{name_suffix} = 0.7.0.2.%{version}
# Required to actually run containers. We require the minimum version that is
# pinned by Docker, but in order to avoid headaches we allow for updates.
Requires:       runc >= 1.1.2
Requires:       containerd >= 1.6.9
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
%sysusers_requires
Requires(post): %fillup_prereq
Requires(post): udev
Requires(post): shadow
# This recommends is added to make sure that even if you have container-selinux
# installed you will still be prompted to install apparmor-parser which Docker
# requires to apply AppArmor profiles (for SELinux systems this doesn't matter
# but if you switch back to AppArmor on reboot this would result in insecure
# containers).
Recommends:     apparmor-parser
# Not necessary, but must be installed when the underlying system is
# configured to use lvm and the user doesn't explicitly provide a
# different storage-driver than devicemapper
Recommends:     lvm2 >= 2.2.89
Recommends:     git-core >= 1.7
ExcludeArch:    s390 ppc

# KUBIC-SPECIFIC: This was required when upgrading from the original kubic
#                 packaging, when everything was renamed to -kubic. It also is
#                 used to ensure that nothing complains too much when using
#                 -kubic packages. Hopfully it can be removed one day.
%if "%flavour" == "kubic"
# Obsolete old packege without the -kubic suffix
Obsoletes:      %{realname} = 1.12.6
Obsoletes:      %{realname}_1_12_6
# Conflict with non-kubic package, and provide equivalent
Conflicts:      %{realname}
Provides:       %{realname} = %{version}
# Kubernetes requires cri-runtime, which should be provided only by the -kubic flavour of this package
Provides:       cri-runtime
# No i586 Kubernetes, so docker-kubic must not be built for i586 also
ExcludeArch:    i586
# Disable leap based builds for kubic flavor (bsc#1121412)
%if 0%{?suse_version} == 1500 && 0%{?is_opensuse}
ExclusiveArch:  do_not_build
%endif
%endif

%description
Docker complements LXC with a high-level API which operates at the process
level. It runs unix processes with strong guarantees of isolation and
repeatability across servers.

Docker is a great building block for automating distributed systems: large-scale
web deployments, database clusters, continuous deployment systems, private PaaS,
service-oriented architectures, etc.

%package bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    packageand(%{name}:bash-completion)
BuildArch:      noarch
# KUBIC-SPECIFIC: This was required when upgrading from the original kubic
#                 packaging, when everything was renamed to -kubic. It also is
#                 used to ensure that nothing complains too much when using
#                 -kubic packages. Hopfully it can be removed one day.
%if "%flavour" == "kubic"
# Obsolete old packege without the -kubic suffix
Obsoletes:      %{realname}-bash-completion = 1.12.6
# Conflict with non-kubic package, and provide equivalent
Conflicts:      %{realname}-bash-completion > 1.12.6
Provides:       %{realname}-bash-completion = %{version}
%endif

%description bash-completion
Bash command line completion support for %{name}.

%package zsh-completion
Summary:        Zsh Completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Requires:       zsh
Supplements:    packageand(%{name}:zsh)
BuildArch:      noarch
# KUBIC-SPECIFIC: This was required when upgrading from the original kubic
#                 packaging, when everything was renamed to -kubic. It also is
#                 used to ensure that nothing complains too much when using
#                 -kubic packages. Hopfully it can be removed one day.
%if "%flavour" == "kubic"
# Obsolete old packege without the -kubic suffix
Obsoletes:      %{realname}-zsh-completion = 1.12.6
# Conflict with non-kubic package, and provide equivalent
Conflicts:      %{realname}-zsh-completion > 1.12.6
Provides:       %{realname}-zsh-completion = %{version}
%endif

%description zsh-completion
Zsh command line completion support for %{name}.

%package fish-completion
Summary:        Fish completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Requires:       fish
Supplements:    packageand(%{name}:fish)
BuildArch:      noarch
%if "%flavour" == "kubic"
# Conflict with non-kubic package, and provide equivalent
Conflicts:      %{realname}-fish-completion
Provides:       %{realname}-fish-completion = %{version}
%endif

%description fish-completion
Fish command line completion support for %{name}.

%if "%flavour" == "kubic"
%package kubeadm-criconfig
Summary:        docker container runtime configuration for kubeadm
Group:          System/Management
Requires:       kubernetes-kubeadm
Requires(post): %fillup_prereq
Supplements:    docker-kubic
Provides:       kubernetes-kubeadm-criconfig
Conflicts:      cri-o-kubeadm-criconfig

%description kubeadm-criconfig
docker container runtime configuration for kubeadm
%endif

%prep
%setup -q -n %{realname}-%{version}_%{git_version}

%if 0%{?is_opensuse}
# nothing
%else
# PATCH-SUSE: Secrets patches.
%patch100 -p1
%patch101 -p1
%endif
%if "%flavour" == "kubic"
# PATCH-SUSE: Mirror patch.
%patch200 -p1
%endif
# bsc#1099277
%patch300 -p1
# bsc#1183855 bsc#1175081
%patch301 -p1
# bsc#1193930 CVE-2021-43565 bsc#1197284 CVE-2022-27191
%patch302 -p1
# bsc#1200022
%patch303 -p1

# README_SUSE.md for documentation.
cp %{SOURCE103} .

# Extract the docker-cli source in a subdir.
mkdir -p %{cli_builddir}
pushd %{cli_builddir}
xz -dc %{SOURCE1} | tar -xof - --strip-components=1
popd

# Extract the docker-libnetwork source in a subdir.
mkdir -p %{proxy_builddir}
pushd %{proxy_builddir}
xz -dc %{SOURCE2} | tar -xof - --strip-components=1
popd

%build
%sysusers_generate_pre %{SOURCE106} %{name} %{name}.conf
echo "$PWD -- $PWD -- $PWD"

BUILDTAGS="exclude_graphdriver_aufs apparmor selinux seccomp pkcs11"
%if 0%{?sle_version} == 120000
	# Allow us to build with older distros but still have deferred removal
	# support at runtime. We only use this when building on SLE12, because
	# later openSUSE/SLE versions have a new enough libdevicemapper to not
	# require the runtime checking.
	BUILDTAGS="libdm_dlsym_deferred_remove $BUILDTAGS"
%endif

(cat <<EOF
export AUTO_GOPATH=1
export DOCKER_BUILDTAGS="$BUILDTAGS"
# Until boo#1038493 is fixed properly we need to do this hack to get the
# compiled-into-the-binary GOROOT.
export GOROOT="$(GOROOT= go env GOROOT)"
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
# NOTE: This will have to be removed with the next major Docker bump.
export GO111MODULE=off
EOF
) > docker_build_env
. ./docker_build_env

# Preparing GOPATH so that the client is visible to the compiler
mkdir -p src/github.com/docker/
ln -s "%{cli_builddir}" "$PWD/src/github.com/docker/cli"
export GOPATH="$GOPATH:$PWD"

###################
## DOCKER ENGINE ##
###################

# Ignore the warning that we compile outside a Docker container.
./hack/make.sh dynbinary

###################
## DOCKER CLIENT ##
###################

pushd %{cli_builddir}
make dynbinary

mkdir -p ./man/man1
go build -buildmode=pie -o gen-manpages github.com/docker/cli/man
./gen-manpages --root "$PWD" --target "$PWD/man/man1"
./man/md2man-all.sh
popd

##################
## DOCKER PROXY ##
##################

pushd %{proxy_builddir}
GOPATH="%{dist_builddir}" \
	go build -buildmode=pie -o docker-proxy github.com/docker/libnetwork/cmd/proxy
popd

# We verify that our libnetwork source is the correct version. This is done
# on-build to make sure that someone doing an update didn't miss anything.
grep 'LIBNETWORK_COMMIT:=%{libnetwork_version}' hack/dockerfile/install/proxy.installer

%install
install -Dd -m0755 \
	%{buildroot}%{_sysconfdir}/init.d \
	%{buildroot}%{_bindir} \
	%{buildroot}%{_sbindir}

# docker daemon
install -D -m0755 bundles/dynbinary-daemon/dockerd %{buildroot}/%{_bindir}/dockerd
install -d %{buildroot}/%{_localstatedir}/lib/docker
# daemon.json config file
install -D -m0644 %{SOURCE105} %{buildroot}%{_sysconfdir}/docker/daemon.json

# docker cli
install -D -m0755 %{cli_builddir}/build/docker %{buildroot}/%{_bindir}/docker
install -D -m0644 %{cli_builddir}/contrib/completion/bash/docker "%{buildroot}%{_datarootdir}/bash-completion/completions/%{realname}"
install -D -m0644 %{cli_builddir}/contrib/completion/zsh/_docker "%{buildroot}%{_sysconfdir}/zsh_completion.d/_%{realname}"
install -D -m0644 %{cli_builddir}/contrib/completion/fish/docker.fish "%{buildroot}/%{_datadir}/fish/vendor_completions.d/%{realname}.fish"

# docker proxy
install -D -m0755 %{proxy_builddir}/docker-proxy %{buildroot}/%{_bindir}/docker-proxy

# systemd service
install -D -m0644 %{SOURCE100} %{buildroot}%{_unitdir}/%{realname}.service
%if "%flavour" == "kubic"
install -D -m0644 %{SOURCE900} %{buildroot}%{_unitdir}/%{realname}.service.d/90-kubic.conf
%endif
ln -sf service %{buildroot}%{_sbindir}/rcdocker

# udev rules that prevents dolphin to show all docker devices and slows down
# upstream report https://bugs.kde.org/show_bug.cgi?id=329930
install -D -m0644 %{SOURCE101} %{buildroot}%{_udevrulesdir}/80-%{realname}.rules

# audit rules
install -D -m0640 %{SOURCE104} %{buildroot}%{_sysconfdir}/audit/rules.d/%{realname}.rules

# sysconfig file
install -D -m0644 %{SOURCE102} %{buildroot}%{_fillupdir}/sysconfig.docker

# install manpages (using the ones from the engine)
install -d %{buildroot}%{_mandir}/man1
install -p -m0644 %{cli_builddir}/man/man1/*.1 %{buildroot}%{_mandir}/man1
install -d %{buildroot}%{_mandir}/man5
install -p -m0644 %{cli_builddir}/man/man5/Dockerfile.5 %{buildroot}%{_mandir}/man5
install -d %{buildroot}%{_mandir}/man8
install -p -m0644 %{cli_builddir}/man/man8/*.8 %{buildroot}%{_mandir}/man8

# sysusers.d
install -D -m0644 %{SOURCE106} %{buildroot}%{_sysusersdir}/%{name}.conf

%if "%flavour" == "kubic"
# place kubelet.env in fillupdir (for kubeadm-criconfig)
sed -e 's-@LIBEXECDIR@-%{_libexecdir}-g' -i %{SOURCE901}
install -D -m0644 %{SOURCE901} %{buildroot}%{_fillupdir}/sysconfig.kubelet
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

%service_add_pre %{realname}.service

%post
%service_add_post %{realname}.service
%{fillup_only -n docker}

%if "%flavour" == "kubic"
%post kubeadm-criconfig
%fillup_only -n kubelet
%endif

%preun
%service_del_preun %{realname}.service

%postun
%service_del_postun %{realname}.service

%files
%defattr(-,root,root)
%doc README.md README_SUSE.md
%license LICENSE
%{_bindir}/docker
%{_bindir}/dockerd
%{_bindir}/docker-proxy
%{_sbindir}/rcdocker
%dir %{_localstatedir}/lib/docker/

%{_unitdir}/%{realname}.service
%{_sysusersdir}/%{name}.conf
%if "%flavour" == "kubic"
%dir %{_unitdir}/%{realname}.service.d/
%{_unitdir}/%{realname}.service.d/90-kubic.conf
%endif

%dir %{_sysconfdir}/docker
%config(noreplace) %{_sysconfdir}/docker/daemon.json
%{_fillupdir}/sysconfig.docker

%config %{_sysconfdir}/audit/rules.d/%{realname}.rules
%{_udevrulesdir}/80-%{realname}.rules

%{_mandir}/man1/docker-*.1%{ext_man}
%{_mandir}/man1/docker.1%{ext_man}
%{_mandir}/man5/Dockerfile.5%{ext_man}
%{_mandir}/man8/dockerd.8%{ext_man}

%files bash-completion
%defattr(-,root,root)
%{_datarootdir}/bash-completion/completions/%{realname}

%files zsh-completion
%defattr(-,root,root)
%{_sysconfdir}/zsh_completion.d/_%{realname}

%files fish-completion
%defattr(-,root,root)
%{_datadir}/fish/vendor_completions.d/%{realname}.fish

%if "%flavour" == "kubic"
%files kubeadm-criconfig
%defattr(-,root,root)
%{_fillupdir}/sysconfig.kubelet
%endif

%changelog
