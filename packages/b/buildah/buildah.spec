#
# spec file for package buildah
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


%define project github.com/containers/buildah
# Build with libostree-devel in Tumbleweed, Leap 15 and SLES 15
%if 0%{?suse_version} >= 1500
%define with_libostree 1
%endif
Name:           buildah
Version:        1.16.2
Release:        0
Summary:        Tool for building OCI containers
License:        Apache-2.0
Group:          System/Management
URL:            https://github.com/containers/buildah
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}-rpmlintrc
BuildRequires:  bash-completion
BuildRequires:  device-mapper-devel
BuildRequires:  fdupes
BuildRequires:  git
BuildRequires:  glib2-devel-static
BuildRequires:  glibc-devel-static
BuildRequires:  golang-packaging
BuildRequires:  libapparmor-devel
BuildRequires:  libassuan-devel
BuildRequires:  libbtrfs-devel
BuildRequires:  libgpgme-devel
BuildRequires:  libseccomp-devel
BuildRequires:  golang(API) >= 1.13
Requires:       patterns-base-apparmor
Requires:       libcontainers-common
Requires:       libcontainers-image
Requires:       libcontainers-storage
Requires:       runc >= 1.0.0~rc4
Requires:       slirp4netns
%{go_nostrip}
%if 0%{?with_libostree}
BuildRequires:  libostree-devel
%endif

%description
Buildah provides a command line tool which can be used to:
- Create a working container, either from scratch or using an image as a
  starting point
- Create an image, either from a working container or via the instructions in a
  Dockerfile
- Build images in either the OCI image format or the traditional
  upstream docker image format
- Mount a working container's root filesystem for manipulation
- Unmount a working container's root filesystem
- Update the contents of a container's root filesystem
- Delete a working container or an image

%prep
%setup -q

%build
# We can't use symlinks here because go-list gets confused by symlinks, so we
# have to copy the source to $HOME/go and then use that as the GOPATH.
export GOPATH=$HOME/go
mkdir -pv $HOME/go/src/%{project}
rm -rf $HOME/go/src/%{project}/*
cp -avr * $HOME/go/src/%{project}
cd $HOME/go/src/%{project}

# Build buildah
make %{?_smp_mflags} GIT_COMMIT=unknown EXTRALDFLAGS=-buildmode=pie

%check
# Too many tests fail due to the restricted permissions in the build enviroment.
# Updates must be tested manually.

%install
cd $HOME/go/src/%{project}

install -D -m 0755 bin/buildah %{buildroot}/%{_bindir}/buildah
install -d %{buildroot}/%{_mandir}/man1
install -m 0644 docs/buildah*.1 %{buildroot}/%{_mandir}/man1
install -D -m 0644 contrib/completions/bash/buildah %{buildroot}/%{_datadir}/bash-completion/completions/buildah

%fdupes %{buildroot}/%{_prefix}

%files
%{_bindir}/buildah
%{_mandir}/man1/buildah*
%{_datadir}/bash-completion/completions/buildah
%license LICENSE

%changelog
