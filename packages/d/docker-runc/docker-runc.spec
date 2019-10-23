#
# spec file for package docker
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


# Handle _multibuild magic.
%define flavour @BUILD_FLAVOR@%{nil}

# We split the Name: into "realname" and "name_suffix".
%define realname docker-runc
%if "%flavour" == ""
%define name_suffix %{nil}
%else
%define name_suffix -%{flavour}
%endif

# MANUAL: Update the git_version, git_short, and git_revision
%define git_version 3e425f80a8c931f88e6d94a8c831b9d5aa481657
%define git_short   3e425f80a8c9
# How to get the git_revision
# git clone ${url}.git runc-upstream
# cd runc-upstream
# git checkout $git_version
# git_revision=r$(git rev-list HEAD | wc -l)
%define git_revision r3917

%define go_tool go
%define _name runc
%define project github.com/opencontainers/%{_name}

Name:           %{realname}%{name_suffix}
Version:        1.0.0rc8+git%{git_revision}_%{git_short}
Release:        0
Summary:        Tool for spawning and running OCI containers
License:        Apache-2.0
Group:          System/Management
Url:            https://github.com/opencontainers/runc
Source:         %{realname}-git.%{git_short}.tar.xz
Source1:        %{realname}-rpmlintrc
# FIX-UPSTREAM: Backport of https://github.com/opencontainers/runc/pull/2130.
Patch1:         CVE-2019-16884.patch
BuildRequires:  fdupes
BuildRequires:  go-go-md2man
BuildRequires:  libapparmor-devel
BuildRequires:  libseccomp-devel >= 2.2
BuildRequires:  libselinux-devel
BuildRequires:  golang(API) >= 1.10
Recommends:     criu
Obsoletes:      runc <= 1.0
# We provide a git revision so that Docker can require it properly.
Provides:       %{name}-git = %{git_version}
ExcludeArch:    s390
# KUBIC-SPECIFIC: This was required when upgrading from the original kubic
#                 packaging, when everything was renamed to -kubic. It also is
#                 used to ensure that nothing complains too much when using
#                 -kubic packages. Hopfully it can be removed one day.
%if "%flavour" == "kubic"
# Obsolete older package without -kubic suffix: v2 -> v3
Obsoletes:      %{_name}_50a19c6
Obsoletes:      %{realname} = 0.1.1+gitr2819_50a19c6
# Conflict with non-kubic package, and provide equivalent
Conflicts:      %{realname}
Provides:       %{realname} = %{version}
# Disable leap based builds for kubic flavor (bsc#1121412)
%if 0%{?suse_version} == 1500 && 0%{?is_opensuse}
ExclusiveArch:  do_not_build
%endif
%endif

%description
runc is a CLI tool for spawning and running containers according to the OCI
specification. It is designed to be as minimal as possible, and is the workhorse
of Docker. It was originally designed to be a replacement for LXC within Docker,
and has grown to become a separate project entirely.

%prep
%setup -q -n %{realname}-git.%{git_short}
# CVE-2019-16884 bsc#1152308
%patch1 -p1

%build
# Do not use symlinks. If you want to run the unit tests for this package at
# some point during the build and you need to directly use go list directly it
# will get confused by symlinks.
export GOPATH=${HOME}/go
export PROJECT=${HOME}/go/src/%project
mkdir -p $PROJECT
rm -rf $PROJECT/*
cp -a * $PROJECT

# Build all features.
export BUILDTAGS="apparmor selinux seccomp"
export BUILDFLAGS="-buildmode=pie -gccgoflags='-Wl,--add-needed -Wl,--no-as-needed -static-libgo -ldl -lselinux -lapparmor -lseccomp'"

(cat <<EOF
export GOPATH="$GOPATH"
export BUILDTAGS="$BUILDTAGS"
export BUILDFLAGS="$BUILDFLAGS"
EOF
) >./.runc_build_env
source ./.runc_build_env

# Build runc.
make -C $PROJECT EXTRA_FLAGS="$BUILDFLAGS" BUILDTAGS="$BUILDTAGS" COMMIT_NO=%{git_version} runc
cp $PROJECT/runc %{realname}-%{version}

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

# Make sure we install in /usr/sbin/docker-runc
install -D -m755 %{realname}-%{version} %{buildroot}%{_sbindir}/%{realname}

# We have to rename the man pages to docker-runc.
install -d -m755 %{buildroot}%{_mandir}/man8
cd man/man8
for mp in $(ls runc*.8); do
	install -m644 ${mp} %{buildroot}%{_mandir}/man8/docker-${mp}
done

%fdupes %{buildroot}

%files
%defattr(-,root,root)
%doc README.md
%license LICENSE
%{_sbindir}/docker-runc
%{_mandir}/man8/docker-runc*.8.gz

%changelog
