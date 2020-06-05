#
# spec file for package containerd
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

# Handle _multibuild magic.
%define flavour @BUILD_FLAVOR@%{nil}

# We split the Name: into "realname" and "name_suffix".
%define realname containerd
%if "%flavour" == ""
%define name_suffix %{nil}
%else
%define name_suffix -%{flavour}
%endif

# MANUAL: Update the git_version.
%define git_version 7ad184331fa3e55e52b890ea95e65ba581ae3429
%define git_short   7ad184331fa3

Name:           %{realname}%{name_suffix}
Version:        1.2.13
Release:        0
Summary:        Standalone OCI Container Daemon
License:        Apache-2.0
Group:          System/Management
URL:            https://containerd.tools
Source:         %{realname}-%{version}_%{git_short}.tar.xz
Source1:        %{realname}-rpmlintrc
# OPENSUSE-FIX-UPSTREAM: Backport of https://github.com/containerd/containerd/pull/2764.
Patch1:         0001-makefile-remove-emoji.patch
BuildRequires:  fdupes
BuildRequires:  glibc-devel-static
BuildRequires:  go-go-md2man
BuildRequires:  libbtrfs-devel >= 3.8
BuildRequires:  libseccomp-devel >= 2.2
BuildRequires:  pkg-config
BuildRequires:  golang(API) >= 1.11
# We provide a git revision so that Docker can require it properly.
Provides:       %{name}-git = %{git_version}
# Currently runc is the only supported runtime for containerd. We pin the same
# flavour as us, to avoid mixing (the version pinning is done by docker.spec).
Requires:       docker-runc%{name_suffix}
Requires(post): %fillup_prereq
ExcludeArch:    s390
# KUBIC-SPECIFIC: This was required when upgrading from the original kubic
#                 packaging, when everything was renamed to -kubic. It also is
#                 used to ensure that nothing complains too much when using
#                 -kubic packages. Hopfully it can be removed one day.
%if "%flavour" == "kubic"
# Obsolete older package without -kubic suffix: v2 -> v3
Obsoletes:      %{realname} = 0.2.5+gitr569_2a5e70c
Obsoletes:      %{realname}_2a5e70c
# Conflict with non-kubic package, and provide equivalent
Conflicts:      %{realname} > 0.2.5+gitr569_2a5e70c
Provides:       %{realname} = %{version}
# Disable leap based builds for kubic flavor (bsc#1121412)
%if 0%{?suse_version} == 1500 && 0%{?is_opensuse}
ExclusiveArch:  do_not_build
%endif
%endif

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
# KUBIC-SPECIFIC: This was required when upgrading from the original kubic
#                 packaging, when everything was renamed to -kubic. It also is
#                 used to ensure that nothing complains too much when using
#                 -kubic packages. Hopfully it can be removed one day.
%if "%flavour" == "kubic"
# Obsolete older package without -kubic suffix: v2 -> v3
Obsoletes:      %{realname}-ctr = 0.2.5+gitr569_2a5e70c
# Conflict with non-kubic package, and provide equivalent
Conflicts:      %{realname}-ctr > 0.2.5+gitr569_2a5e70c
Provides:       %{realname}-ctr = %{version}
%endif

%description ctr
Standalone client for containerd, which allows management of containerd containers
separately from Docker.

%prep
%setup -q -n %{realname}-%{version}_%{git_short}
%patch1 -p1

%build
# Do not use symlinks. If you want to run the unit tests for this package at
# some point during the build and you need to directly use go list directly it
# will get confused by symlinks.
export GOPATH=$HOME/go
export PROJECT=$HOME/go/src/github.com/containerd/containerd
mkdir -p $PROJECT
rm -rf $PROJECT/*
cp -ar * $PROJECT

BUILDTAGS="apparmor selinux seccomp"
make -C $PROJECT \
	BUILDTAGS="$BUILDTAGS" \
	VERSION="v%{version}" \
	REVISION="%{git_version}"
make man

cp $PROJECT/bin/ctr ctr-%{version}
cp $PROJECT/bin/containerd containerd-%{version}
cp $PROJECT/bin/containerd-shim containerd-shim-%{version}

%check
# We used to run 'go test' here, however we found that this actually didn't
# catch any issues that were caught by smoke testing, and %check would
# continually cause package builds to fail due to flaky tests. If you ever need
# to know how the testing was done, you can always look in the package history.
# boo#1095817

%install
# Install binaries.
install -D -m755 containerd-%{version} %{buildroot}/%{_sbindir}/%{realname}
install -D -m755 containerd-shim-%{version} %{buildroot}/%{_sbindir}/%{realname}-shim
install -D -m755 ctr-%{version} %{buildroot}/%{_sbindir}/%{realname}-ctr

# Install docker-* symlinks to said binaries, since in order to use the
# upstream setup, Docker needs to spawn containerd and needs to have the
# binaries have specific names.
ln -s %{_sbindir}/%{realname} %{buildroot}/%{_sbindir}/docker-%{realname}
ln -s %{_sbindir}/%{realname}-shim %{buildroot}/%{_sbindir}/docker-%{realname}-shim

# Set up dummy configuration.
install -d -m755 %{buildroot}/%{_sysconfdir}/%{realname}
echo "# See containerd-config.toml(5) for documentation." >%{buildroot}/%{_sysconfdir}/%{realname}/config.toml

# Man pages.
for file in man/*
do
	section="${file##*.}"
	install -D -m644 "$file" "%{buildroot}/%{_mandir}/man$section/$(basename "$file")"
done
ln -s ctr.1 %{buildroot}/%{_mandir}/man1/%{realname}-ctr.1

%fdupes %{buildroot}

%files
%defattr(-,root,root)
%doc README.md
%license LICENSE
%dir %{_sysconfdir}/%{realname}
%config %{_sysconfdir}/%{realname}/config.toml
%{_sbindir}/%{realname}
%{_sbindir}/docker-%{realname}
%{_sbindir}/%{realname}-shim
%{_sbindir}/docker-%{realname}-shim
%{_mandir}/man*/%{realname}*
%exclude %{_mandir}/man1/*ctr.1*

%files ctr
%{_sbindir}/%{realname}-ctr
%{_mandir}/man1/*ctr.1*

%changelog
