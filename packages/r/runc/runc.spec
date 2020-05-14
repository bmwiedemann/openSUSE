#
# spec file for package runc
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


# We don't include a git_version in the "upstream" runc package, because we
# only package released versions (unlike docker-runc).
%define git_version %{nil}

# Package-wide golang version
%define go_version 1.10
%define go_tool go
%define _version 1.0.0-rc10
%define project github.com/opencontainers/runc

# enable libseccomp for sle >= sle12sp2
%if 0%{?sle_version} >= 120200
%define with_libseccomp 1
%endif
# enable libseccomp for leap >= 42.2
%if 0%{?leap_version} >= 420200
%define with_libseccomp 1
%endif
# enable libseccomp for Factory
%if 0%{?suse_version} > 1320
%define with_libseccomp 1
%endif

Name:           runc
Version:        1.0.0~rc10
Release:        0
Summary:        Tool for spawning and running OCI containers
License:        Apache-2.0
Group:          System/Management
URL:            https://github.com/opencontainers/runc
Source0:        https://github.com/opencontainers/runc/releases/download/v%{_version}/runc.tar.xz#/runc-%{_version}.tar.xz
Source1:        https://github.com/opencontainers/runc/releases/download/v%{_version}/runc.tar.xz.asc#/runc-%{_version}.tar.xz.asc
Source2:        runc.keyring
Source3:        runc-rpmlintrc
# FIX-UPSTREAM: Backport of https://github.com/opencontainers/runc/pull/1807. bsc#1149954
Patch0:         bsc1149954-0001-sd-notify-do-not-hang-when-NOTIFY_SOCKET-is-used-wit.patch
# FIX-UPSTREAM: Backport of https://github.com/opencontainers/runc/pull/2391. bsc#1168481
Patch1:         bsc1168481-0001-cgroup-devices-major-cleanups-and-minimal-transition.patch
BuildRequires:  fdupes
BuildRequires:  go-go-md2man
BuildRequires:  golang(API) >= %{go_version}
%if 0%{?with_libseccomp}
BuildRequires:  libseccomp-devel
%endif
BuildRequires:  libselinux-devel
Recommends:     criu

%description
runc is a CLI tool for spawning and running containers according to the OCI
specification. It is designed to be as minimal as possible, and is the workhorse
of Docker. It was originally designed to be a replacement for LXC within Docker,
and has grown to become a separate project entirely.

%package test
Summary:        Test package for runc
Group:          System/Management
BuildRequires:  golang(API) >= %{go_version}
%if 0%{?with_libseccomp}
BuildRequires:  libseccomp-devel
%endif
Requires:       go-go-md2man
Requires:       libapparmor-devel
Requires:       libselinux-devel
Recommends:     criu
BuildArch:      noarch

%description test
Test package for runc. It contains the source code and the tests.

%prep
%setup -q -n %{name}-%{_version}
# bsc#1149954
%patch0 -p1
# bsc#1168481
%patch1 -p1

%build
# Do not use symlinks. If you want to run the unit tests for this package at
# some point during the build and you need to directly use go list directly it
# will get confused by symlinks.
export GOPATH=${HOME}/go
mkdir -p $HOME/go/src/%project
rm -rf $HOME/go/src/%project/*
cp -a * $HOME/go/src/%project

# Additionally enable seccomp.
%if 0%{?with_libseccomp}
export EXTRA_BUILDTAGS+="seccomp"
export EXTRA_GCCFLAGS+="-lseccomp"
%endif

# Build all features.
export BUILDTAGS="apparmor selinux $EXTRA_BUILDTAGS"
export BUILDFLAGS="-buildmode=pie -gccgoflags='-Wl,--add-needed -Wl,--no-as-needed -static-libgo -ldl -lselinux -lapparmor $EXTRA_GCCFLAGS'"

(cat <<EOF
export GOPATH="$GOPATH"
export BUILDTAGS="$BUILDTAGS"
export BUILDFLAGS="$BUILDFLAGS"
EOF
) >./.runc_build_env
source ./.runc_build_env

# Build runc.
make -C "$HOME/go/src/%project" EXTRA_FLAGS="$BUILDFLAGS" BUILDTAGS="$BUILDTAGS" COMMIT_NO="%{git_version}" runc
mv "$HOME/go/src/%project/runc" %{name}-%{version}

# Build man pages, this can only be done on arches where we can build go-md2man.
man/md2man-all.sh

%check
# We used to run 'go test' here, however we found that this actually didn't
# catch any issues that were caught by smoke testing, and %check would
# continually cause package builds to fail due to flaky tests. If you ever need
# to know how the testing was done, you can always look in the package history.
# boo#1095817

%install
source ./.runc_build_env

# We install to /usr/sbin/runc as per upstream an create a symlink in /usr/bin
# for rootless tools.
install -D -m755 %{name}-%{version} %{buildroot}%{_sbindir}/%{name}
install -m 755 -d %{buildroot}%{_bindir}
ln -s  %{_sbindir}/%{name} %{buildroot}%{_bindir}/%{name}
install -d -m755 %{buildroot}/usr/src/%{name}/
cp -av $HOME/go/src/%{project}/* %{buildroot}/usr/src/%{name}/

# Man pages.
install -d -m755 %{buildroot}%{_mandir}/man8
install -m644 man/man8/runc*.8 %{buildroot}%{_mandir}/man8

%fdupes %{buildroot}

%post

%files
%defattr(-,root,root)
%doc README.md
%license LICENSE
%{_sbindir}/%{name}
%{_bindir}/%{name}
%{_mandir}/man8/runc*.8.gz

%files test
%defattr(-,root,root)
/usr/src/runc/
%exclude /usr/src/runc/runc
%exclude /usr/src/runc/runc/Godeps/_workspace/pkg

%changelog
