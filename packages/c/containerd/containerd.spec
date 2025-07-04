#
# spec file for package containerd
#
# Copyright (c) 2025 SUSE LLC
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
%define git_version 05044ec0a9a75232cad458027ca83437aae3f4da
%define git_short   05044ec0

%global provider_prefix github.com/containerd/containerd
%global import_path %{provider_prefix}

Name:           containerd
Version:        1.7.27
Release:        0
Summary:        Standalone OCI Container Daemon
License:        Apache-2.0
Group:          System/Management
URL:            https://containerd.tools
Source:         %{name}-%{version}_%{git_short}.tar.xz
Source1:        %{name}-rpmlintrc
Source2:        %{name}.service
# UPSTREAM: Revert <https://github.com/containerd/containerd/pull/7933> to fix build on SLE-12.
Patch1:         0001-BUILD-SLE12-revert-btrfs-depend-on-kernel-UAPI-inste.patch
BuildRequires:  fdupes
BuildRequires:  glibc-devel-static
BuildRequires:  go >= 1.22
BuildRequires:  go-go-md2man
BuildRequires:  golang-packaging
BuildRequires:  libbtrfs-devel >= 3.8
BuildRequires:  libseccomp-devel >= 2.2
BuildRequires:  pkg-config
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
Provides:       cri-runtime

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

%package devel
Summary:        Source code for containerd
Group:          Development/Libraries/Go
Requires:       %{name} = %{version}
# cannot switch to noarch on SLE as that breaks maintenance updates
%if 0%{?suse_version} > 1500
BuildArch:      noarch
%endif

%description devel
This package contains the source code needed for building packages that
reference the following Go import paths: github.com/containerd/containerd

%prep
%setup -q -n %{name}-%{version}_%{git_short}
%if 0%{?sle_version} == 120000
%patch -P 1 -p1
%endif

%build
%goprep %{import_path}
BUILDTAGS="apparmor selinux seccomp"
make \
        BUILDTAGS="$BUILDTAGS" \
        VERSION="v%{version}" \
        REVISION="%{git_version}"

make man

cp -r "$PROJECT/bin" bin

%install
%gosrc
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
for file in man/*
do
        section="${file##*.}"
        install -D -m644 "$file" "%{buildroot}/%{_mandir}/man$section/$(basename "$file")"
done
mv %{buildroot}/%{_mandir}/man8/{ctr.8,%{name}-ctr.8}

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
%{_mandir}/man*/%{name}*
%exclude %{_mandir}/man8/*ctr.8*

%files ctr
%{_sbindir}/%{name}-ctr
%{_mandir}/man8/%{name}-ctr.8*

%files devel
%license LICENSE
%dir %{go_contribsrcdir}/github.com
%dir %{go_contribsrcdir}/github.com/containerd
%{go_contribsrcdir}/%{import_path}

%changelog
