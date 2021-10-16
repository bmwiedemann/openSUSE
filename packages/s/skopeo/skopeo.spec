#
# spec file for package skopeo
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


%define project        github.com/containers/skopeo

%if 0%{?is_opensuse} && 0%{?suse_version} >= 1500
# Build with libostree-devel for openSUSE Tumbleweed and Leap 15
%define with_libostree 1
%endif
Name:           skopeo
Version:        1.5.0
Release:        0
Summary:        Container image repository tool
License:        Apache-2.0
Group:          System/Management
URL:            https://github.com/containers/skopeo
Source:         %{name}-%{version}.tar.xz
Source1:        skopeo.rpmlintrc
Requires:       libcontainers-common
BuildRequires:  bash
BuildRequires:  device-mapper-devel >= 1.2.68
BuildRequires:  glib2-devel
BuildRequires:  go-go-md2man
BuildRequires:  libbtrfs-devel >= 3.8
BuildRequires:  libcontainers-common
BuildRequires:  libgpgme-devel
BuildRequires:  golang(API) >= 1.15
ExcludeArch:    s390
%if 0%{?with_libostree}
BuildRequires:  libostree-devel
%endif

%description
skopeo is a command line utility for various operations on container images and
image repositories. skopeo is able to inspect a repository on a Docker registry
and fetch images layers. skopeo can copy container images between various
storage mechanisms.

%package bash-completion
Summary:        Bash completion for skopeo

%description bash-completion
This package contains the bash completion for skopeo.

%prep
%setup -q
# No shbang for completions
sed -i 's|#! /bin/bash|# bash completion for skopeo|' completions/bash/skopeo

%build
mkdir -p .gopath/src/github.com/containers
ln -s $PWD .gopath/src/%{project}
export GOPATH=$PWD/.gopath

export BUILDTAGS="exclude_graphdriver_aufs"

%if 0%{?suse_version} <= 1320
	BUILDTAGS+=" libdm_no_deferred_remove"
%endif

# Starting from https://github.com/containers/image/pull/587, ostree is disabled
# by default.
%if 0%{?with_libostree}
	BUILDTAGS+=" containers_image_ostree"
%endif

# Build.
GO111MODULE=on go build -mod=vendor "-buildmode=pie" -ldflags "-X main.gitCommit=" -gcflags "" -tags "$BUILDTAGS" -o skopeo %{project}/cmd/skopeo
make %{?_smp_mflags} docs PREFIX=%{_prefix}

%install
%make_install PREFIX=%{_prefix}
# Drop unneeded files
rm -rv %{buildroot}/etc/containers

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/skopeo*.1*

%files bash-completion
%{_datadir}/bash-completion/completions/*

%changelog
