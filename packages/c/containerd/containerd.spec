#
# spec file for package containerd
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

# MANUAL: Update the git_version.
%define git_version 7b11cfaabd73bb80907dd23182b9347b4245eb5d
%define git_short   7b11cfaabd73

Name:           containerd
Version:        1.4.12
Release:        0
Summary:        Standalone OCI Container Daemon
License:        Apache-2.0
Group:          System/Management
URL:            https://containerd.tools
Source:         %{name}-%{version}_%{git_short}.tar.xz
Source1:        %{name}-rpmlintrc
Source2:        %{name}.service
BuildRequires:  fdupes
BuildRequires:  glibc-devel-static
BuildRequires:  go-go-md2man
BuildRequires:  libbtrfs-devel >= 3.8
BuildRequires:  libseccomp-devel >= 2.2
BuildRequires:  pkg-config
# Due to a limitation in openSUSE's Go packaging we cannot have a BuildRequires
# for 'golang(API) >= 1.16' here, so just require 1.16 exactly. bsc#1172608
BuildRequires:  go1.16
# We provide a git revision so that Docker can require it properly.
Provides:       %{name}-git = %{git_version}
# Currently runc is the only supported runtime for containerd. We pin the same
# flavour as us, to avoid mixing (the version pinning is done by docker.spec).
Requires:       runc
Requires(post): %fillup_prereq
# KUBIC-SPECIFIC: There used to be a kubic-specific containerd package, but now
#                 it's been merged into the one package. bsc#1181677
Obsoletes:      %{name}-kubic < %{version}
Provides:       %{name}-kubic = %{version}
Obsoletes:      %{name} = 0.2.5+gitr569_2a5e70c
Obsoletes:      %{name}_2a5e70c
ExcludeArch:    s390

%description
Containerd is a daemon with an API and a command line client, to manage
containers on one machine. It uses runC to run containers according to the OCI
specification. Containerd has advanced features such as seccomp and user
namespace support as well as checkpoint and restore for cloning and live
migration of containers.

%package ctr
Summary:        Client for %{name}
Group:          System/Management
Requires:       %{name} = %{version}
# KUBIC-SPECIFIC: There used to be a kubic-specific containerd package, but now
#                 it's been merged into the one package.
Obsoletes:      %{name}-ctr = 0.2.5+gitr569_2a5e70c
Obsoletes:      %{name}-ctr-kubic <= %{version}
Obsoletes:      %{name}-ctr_2a5e70c

%description ctr
Standalone client for containerd, which allows management of containerd containers
separately from Docker.

%prep
%setup -q -n %{name}-%{version}_%{git_short}

%build
# NOTE: containerd will switch to go.mod in 1.5.x so this can be removed after
#       we update to that version.

# Do not use symlinks. If you want to run the unit tests for this package at
# some point during the build and you need to directly use go list directly it
# will get confused by symlinks.
export GOPATH=$HOME/go
export PROJECT=$HOME/go/src/github.com/containerd/containerd
export GO111MODULE=off
mkdir -p $PROJECT
rm -rf $PROJECT/*
cp -ar * $PROJECT

BUILDTAGS="apparmor selinux seccomp"
make -C "$PROJECT"\
	BUILDTAGS="$BUILDTAGS" \
	VERSION="v%{version}" \
	REVISION="%{git_version}"
# TODO: Fix man-page generation.
#make man

cp -r "$PROJECT/bin" bin

%install
# Install binaries.
pushd bin/
for bin in containerd{,-shim*}
do
	install -D -m755 "$bin" "%{buildroot}/%{_sbindir}/$bin"
done
# "ctr" is a bit too generic.
install -D -m755 ctr %{buildroot}/%{_sbindir}/%{name}-ctr
popd

# Set up dummy configuration.
install -d -m755 %{buildroot}/%{_sysconfdir}/%{name}
echo "# See containerd-config.toml(5) for documentation." >%{buildroot}/%{_sysconfdir}/%{name}/config.toml

# Install system service
install -Dp -m644 %{SOURCE2} %{buildroot}%{_unitdir}/%{name}.service

# Man pages.
# TODO: Fix man page generation.
#for file in man/*
#do
#	section="${file##*.}"
#	install -D -m644 "$file" "%{buildroot}/%{_mandir}/man$section/$(basename "$file")"
#done
#ln -s ctr.1 %{buildroot}/%{_mandir}/man1/%{name}-ctr.1

%fdupes %{buildroot}

%pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%defattr(-,root,root)
%doc README.md
%license LICENSE
%dir %{_sysconfdir}/%{name}
%config %{_sysconfdir}/%{name}/config.toml
%{_sbindir}/containerd
%{_sbindir}/containerd-shim*
%{_unitdir}/%{name}.service
# TODO: Fix man page generation.
#%{_mandir}/man*/%{name}*
#%exclude %{_mandir}/man1/*ctr.1*

%files ctr
%{_sbindir}/containerd-ctr
# TODO: Fix man page generation.
#%{_mandir}/man1/*ctr.1*

%changelog
