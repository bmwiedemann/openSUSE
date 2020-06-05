#
# spec file for package docker
#
# Copyright (c) 2020 SUSE LLC
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
%define git_version 42e35e61f352
%define git_commit_epoch 1591001995

# These are the git commits required. We verify them against the source to make
# sure we didn't miss anything important when doing upgrades.
%define required_containerd 7ad184331fa3e55e52b890ea95e65ba581ae3429
%define required_dockerrunc dc9208a3303feef5b3839f4323d9beb36df0a9dd
%define required_libnetwork 153d0769a1181bf591a9637fd487a541ec7db1e6

Name:           %{realname}%{name_suffix}
Version:        19.03.11_ce
Release:        0
Summary:        The Moby-project Linux container runtime
License:        Apache-2.0
Group:          System/Management
URL:            http://www.docker.io
# TODO(VR): check those SOURCE files below
Source:         %{realname}-%{version}_%{git_version}.tar.xz
Source1:        docker.service
# bsc#1086185 -- but we only apply this on Kubic.
Source2:        docker-kubic-service.conf
Source3:        80-docker.rules
Source4:        sysconfig.docker
Source5:        kubelet.env
Source6:        docker-rpmlintrc
Source7:        README_SUSE.md
Source8:        docker-audit.rules
Source9:        tests.sh
Source10:       docker-daemon.json
# SUSE-FEATURE: Adds the /run/secrets mountpoint inside all Docker containers
# which is not snapshotted when images are committed. Note that if you modify
# this patch, please also modify the patch in the suse-secrets-v<version>
# branch in http://github.com/suse/docker.mirror.
Patch200:       secrets-0001-daemon-allow-directory-creation-in-run-secrets.patch
Patch201:       secrets-0002-SUSE-implement-SUSE-container-secrets.patch
# SUSE-ISSUE: Revert of https://github.com/docker/docker/pull/37907.
Patch300:       packaging-0001-revert-Remove-docker-prefix-for-containerd-and-runc-.patch
# SUSE-BACKPORT: Backport of https://github.com/docker/docker/pull/37353. bsc#1099277
Patch401:       bsc1073877-0001-apparmor-clobber-docker-default-profile-on-start.patch
# SUSE-BACKPORT: Backport of https://github.com/docker/docker/pull/39121. bsc#1122469
Patch402:       bsc1122469-0001-apparmor-allow-readby-and-tracedby.patch
# FIX-UPSTREAM: Backport of https://github.com/gotestyourself/gotest.tools/pull/169. bsc#1172377
Patch410:       bsc1172377-0001-unexport-testcase.Cleanup-to-fix-Go-1.14.patch
# SUSE-FEATURE: Add support to mirror inofficial/private registries
#               (https://github.com/docker/docker/pull/34319)
Patch500:       private-registry-0001-Add-private-registry-mirror-support.patch
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
BuildRequires:  pkgconfig(libsystemd)
Requires:       apparmor-parser
Requires:       ca-certificates-mozilla
# Required in order for networking to work. fix_bsc_1057743 is a work-around
# for some old packaging issues (where rpm would delete a binary that was
# installed by docker-libnetwork). See bsc#1057743 for more details.
Requires:       docker-libnetwork%{name_suffix}-git = %{required_libnetwork}
Requires:       fix_bsc_1057743
# Containerd and runC are required as they are the only currently supported
# execdrivers of Docker. NOTE: The version pinning here matches upstream's
# vendor.conf to ensure that we don't use a slightly incompatible version of
# runC or containerd (which would be bad).
Requires:       containerd%{name_suffix}-git  = %{required_containerd}
Requires:       docker-runc%{name_suffix}-git = %{required_dockerrunc}
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
Requires(post): %fillup_prereq
Requires(post): udev
Requires(post): shadow
# We used to have a migration tool for the upgrade from v1.9.x to v1.10.x.
# It is no longer useful, so we obsolete it. bsc#1069758
Obsoletes:      docker-image-migrator
# Not necessary, but must be installed when the underlying system is
# configured to use lvm and the user doesn't explicitly provide a
# different storage-driver than devicemapper
Recommends:     lvm2 >= 2.2.89
Recommends:     git-core >= 1.7
Conflicts:      lxc < 1.0
ExcludeArch:    s390 ppc
BuildRequires:  go-go-md2man
BuildRequires:  golang(API) >= 1.13
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

%package test
%global __requires_exclude ^libgo.so.*$
Summary:        Test package for docker
# Needed for test-suite.
Group:          System/Management
Requires:       curl
Requires:       go
Requires:       iputils
Requires:       jq
Requires:       net-tools-deprecated
# KUBIC-SPECIFIC: This was required when upgrading from the original kubic
#                 packaging, when everything was renamed to -kubic. It also is
#                 used to ensure that nothing complains too much when using
#                 -kubic packages. Hopfully it can be removed one day.
%if "%flavour" == "kubic"
# Obsolete old packege without the -kubic suffix
Obsoletes:      %{realname}-test = 1.12.6
# Conflict with non-kubic package, and provide equivalent
Conflicts:      %{realname}-test > 1.12.6
Provides:       %{realname}-test = %{version}
%endif

%description test
Test package for docker. It contains the source code and the tests.

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
%patch200 -p1
%patch201 -p1
%endif
# revert upstream
%patch300 -p1
# bsc#1099277
%patch401 -p1
# bsc#1122469
%patch402 -p1
# bsc#1172377
%patch410 -p1
%if "%flavour" == "kubic"
# PATCH-SUSE: Mirror patch.
%patch500 -p1
%endif

cp %{SOURCE7} .

%build
BUILDTAGS="exclude_graphdriver_aufs apparmor selinux seccomp pkcs11"
%if 0%{?sle_version} == 120000
	# Provided by patch406, to allow us to build with older distros but still
	# have deferred removal support at runtime. We only use this when building
	# on SLE12.
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
export VERSION="$(cat ./VERSION 2>/dev/null || echo '%{version}')"
export DOCKER_GITCOMMIT="%{git_version}"
export GITCOMMIT="%{git_version}"
export SOURCE_DATE_EPOCH="${SOURCE_DATE_EPOCH:-%{git_commit_epoch}}"
export BUILDTIME="$(date -u -d "@$SOURCE_DATE_EPOCH" --rfc-3339 ns 2>/dev/null | sed -e 's/ /T/')"
EOF
) > docker_build_env
. ./docker_build_env

# Preparing GOPATH so that the client is visible to the compiler
mkdir -p src/github.com/docker/
ln -s $(pwd)/components/cli $(pwd)/src/github.com/docker/cli
export GOPATH=$GOPATH:$(pwd)

###################
## DOCKER ENGINE ##
###################

pushd components/engine/
# Ignore the warning that we compile outside a Docker container.
./hack/make.sh dynbinary

# Build test binaries (integration-cli and integration/*). They are all stored
# within the testdir -- we will only end up installing these test files for
# docker-test.
for testdir in {integration-cli,integration/*/}
do
	( find "$testdir" -name '*_test.go' | grep -q '.' ) || continue
	GOPATH=$(pwd)/vendor:$(pwd)/.gopath/ go test \
		-buildmode=pie \
		-tags "$DOCKER_BUILDTAGS daemon autogen" \
		-c "github.com/docker/docker/$testdir" -o "$testdir/tests.main"
done
popd

###################
## DOCKER CLIENT ##
###################

pushd components/cli/
./scripts/build/dynbinary

mkdir -p ./man/man1
go build -buildmode=pie -o gen-manpages github.com/docker/cli/man
./gen-manpages --root "$(pwd)" --target "$(pwd)/man/man1"
./man/md2man-all.sh
popd

%check
# We used to run 'go test' here, however we found that this actually didn't
# catch any issues that were caught by smoke testing, and %check would
# continually cause package builds to fail due to flaky tests. If you ever need
# to know how the testing was done, you can always look in the package history.
# boo#1095817

# We verify that all of our -git requires are correct, and match the contents
# of the upstream vendoring scripts. This is done on-build to make sure that
# someone doing an update didn't miss anything.
cd components/engine
grep 'RUNC_COMMIT:=%{required_dockerrunc}'       hack/dockerfile/install/runc.installer
grep 'CONTAINERD_COMMIT:=%{required_containerd}' hack/dockerfile/install/containerd.installer
grep 'LIBNETWORK_COMMIT:=%{required_libnetwork}' hack/dockerfile/install/proxy.installer

%install
install -d %{buildroot}%{_bindir}
install -D -m755 components/cli/build/docker %{buildroot}/%{_bindir}/docker
install -D -m755 components/engine/bundles/dynbinary-daemon/dockerd %{buildroot}/%{_bindir}/dockerd
install -d %{buildroot}/%{_localstatedir}/lib/docker
install -Dd -m 0755 \
	%{buildroot}%{_sysconfdir}/init.d \
	%{buildroot}%{_sbindir}

install -D -m0644 components/cli/contrib/completion/bash/docker "%{buildroot}%{_datarootdir}/bash-completion/completions/%{realname}"
install -D -m0644 components/cli/contrib/completion/zsh/_docker "%{buildroot}%{_sysconfdir}/zsh_completion.d/_%{realname}"

#
# systemd service
#
install -D -m0644 %{SOURCE1} %{buildroot}%{_unitdir}/%{realname}.service
%if "%flavour" == "kubic"
install -D -m0644 %{SOURCE2} %{buildroot}%{_unitdir}/%{realname}.service.d/90-kubic.conf
%endif
ln -sf service %{buildroot}%{_sbindir}/rcdocker

#
# udev rules that prevents dolphin to show all docker devices and slows down
# upstream report https://bugs.kde.org/show_bug.cgi?id=329930
#
install -D -m 0644 %{SOURCE3} %{buildroot}%{_udevrulesdir}/80-%{realname}.rules

# audit rules
install -D -m 0640 %{SOURCE8} %{buildroot}%{_sysconfdir}/audit/rules.d/%{realname}.rules

# sysconfig file
install -D -m 644 %{SOURCE4} %{buildroot}%{_fillupdir}/sysconfig.docker

# install docker config file
install -D -m 644 %{SOURCE10} %{buildroot}%{_sysconfdir}/docker/daemon.json

# install manpages (using the ones from the engine)
install -d %{buildroot}%{_mandir}/man1
install -p -m 644 components/cli/man/man1/*.1 %{buildroot}%{_mandir}/man1
install -d %{buildroot}%{_mandir}/man5
install -p -m 644 components/cli/man/man5/Dockerfile.5 %{buildroot}%{_mandir}/man5
install -d %{buildroot}%{_mandir}/man8
install -p -m 644 components/cli/man/man8/*.8 %{buildroot}%{_mandir}/man8

# install docker-test files -- we want to avoid installing the entire source tree.
install -d %{buildroot}%{_prefix}/src/docker/
install -D -m0755 %{SOURCE9} %{buildroot}%{_prefix}/src/docker/tests.sh
# We need hack/, contrib/, profiles/, and the integration*/ trees.
cp -a components/engine/{hack,contrib,profiles,integration{,-cli}} %{buildroot}%{_prefix}/src/docker/
echo "%{version}" > %{buildroot}%{_prefix}/src/docker/VERSION
# And now we can remove all *_test.go files -- since we already have test
# binaries. Due to a lot of hacks within the Docker integration tests, we can't
# really do a bigger cleanup than this.
find %{buildroot}%{_prefix}/src/docker \
	-type f -name '*_test.go' -delete

%if "%flavour" == "kubic"
# place kubelet.env in fillupdir (for kubeadm-criconfig)
install -D -m 0644 %{SOURCE5} %{buildroot}%{_fillupdir}/sysconfig.kubelet
%endif

%fdupes %{buildroot}

%pre
# /var/run/docker.sock group owner.
getent group docker >/dev/null || groupadd -r docker

# used for --userns-remap=default.
getent passwd dockremap >/dev/null || \
	useradd -Ur -p '!' -s /bin/false -c 'docker --userns-remap=default' dockremap

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
%doc components/engine/README.md README_SUSE.md CHANGELOG.md
%license components/engine/LICENSE
%{_bindir}/docker
%{_bindir}/dockerd
%{_sbindir}/rcdocker
%dir %{_localstatedir}/lib/docker/

%{_unitdir}/%{realname}.service
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

%files test
%defattr(-,root,root)
%{_prefix}/src/docker/

%if "%flavour" == "kubic"
%files kubeadm-criconfig
%defattr(-,root,root)
%{_fillupdir}/sysconfig.kubelet
%endif

%changelog
