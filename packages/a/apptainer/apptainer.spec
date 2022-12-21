#
# spec file for package apptainer
#
# Copyright (c) 2022 SUSE LLC
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


%define apptainerpath src/github.com/apptainer/
%define _buildshell /bin/bash

%global squashfuse_version 0.1.105

Summary:        Application and environment virtualization
License:        BSD-3-Clause-LBNL
Group:          Productivity/Clustering/Computing
Name:           apptainer
Version:        1.1.4
Release:        0
# https://spdx.org/licenses/BSD-3-Clause-LBNL.html
URL:            https://apptainer.org
Provides:       singularity
Obsoletes:      singularity <= 3.8.5
Source0:        https://github.com/apptainer/apptainer/archive/v%{version}%{?vers_suffix}/apptainer-%{version}%{?vers_suffix}.tar.gz
Source1:        README.SUSE
Source2:        SLE-12SP5.def
Source3:        SLE-15SP3.def
Source5:        %{name}-rpmlintrc
Source9:        vendor.tar.gz
%if "%{?squashfuse_version}" != ""
Source10:       https://github.com/vasi/squashfuse/archive/%{squashfuse_version}/squashfuse-%{squashfuse_version}.tar.gz
Patch10:        https://github.com/vasi/squashfuse/pull/70.patch
%endif
BuildRequires:  cryptsetup
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  git
BuildRequires:  go >= 1.17
BuildRequires:  libuuid-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  sysuser-tools
%ifarch aarch64
BuildRequires:  binutils-gold
%endif
BuildRequires:  libseccomp-devel
%if "%{?squashfuse_version}" != ""
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fuse3-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel
%endif
Requires:       squashfs
Recommends:     fuse2fs
PreReq:         permissions

# there's no golang for ppc64, ppc64le does not have non pie builds
ExcludeArch:    ppc64 ppc64le

Obsoletes:      singularity
Obsoletes:      singularity-ce
Obsoletes:      singularity-runtime

%description
Singularity provides functionality to make portable
containers that can be used across host environments.

%prep
%if "%{?squashfuse_version}" != ""
# the default directory for other steps is where the %prep section ends
# so do main package last
%setup -b 10 -n squashfuse-%{squashfuse_version}
%patch -P 10 -p1
%endif
%setup -q -n %{name}-%{version}
cp %{S:1} %{S:2} %{S:3} .

%build
%if "%{?squashfuse_version}" != ""
pushd ../squashfuse-%{squashfuse_version}
./autogen.sh
FLAGS=-std=c99 ./configure --enable-multithreading
%make_build squashfuse_ll
popd
%endif

# create VERSION file
echo %version > VERSION
# Not all of these parameters currently have an effect, but they might be
# used someday.  They are the same parameters as in the configure macro.
tar xzf %{S:9}
./mconfig -V %{version}-%{release} \
        -P release \
        --prefix=%{_prefix} \
        --exec-prefix=%{_exec_prefix} \
        --bindir=%{_bindir} \
        --sbindir=%{_sbindir} \
        --sysconfdir=%{_sysconfdir} \
        --datadir=%{_datadir} \
        --includedir=%{_includedir} \
        --libdir=%{_libdir} \
        --libexecdir=%{_libexecdir} \
        --localstatedir=%{_localstatedir} \
        --sharedstatedir=%{_sharedstatedir} \
        --mandir=%{_mandir} \
        --infodir=%{_infodir} \
        --without-suid

%make_build -C builddir V=""

%install
export GOPATH=$PWD/gopath
export GOFLAGS=-mod=vendor
export PATH=$GOPATH/bin:$PATH

%make_install -C builddir V=

%if "%{?squashfuse_version}" != ""
install -m 755 ../squashfuse-%{squashfuse_version}/squashfuse_ll %{buildroot}%{_libexecdir}/%{name}/bin/squashfuse_ll
%endif

%fdupes apptainer/examples
%fdupes -s %buildroot

%files
%doc examples
%doc CONTRIBUTING.md
%doc README.md
%doc CHANGELOG.md
%doc CONTRIBUTORS.md
%doc %{basename:%{S:1}}
%doc %{basename:%{S:2}}
%doc %{basename:%{S:3}}
%license LICENSE.md
%license LICENSE_THIRD_PARTY.md
%license LICENSE_DEPENDENCIES.md
%{_bindir}/*
%dir %{_libexecdir}/apptainer
%dir %{_libexecdir}/apptainer/bin
%dir %{_libexecdir}/apptainer/cni
%dir %{_libexecdir}/apptainer/lib
%{_libexecdir}/apptainer/bin/starter
%{_libexecdir}/apptainer/bin/squashfuse_ll
%{_libexecdir}/apptainer/lib/offsetpreload.so
%{_libexecdir}/apptainer/cni/*
%dir %{_sysconfdir}/apptainer
%config(noreplace) %{_sysconfdir}/apptainer/capability.json
%config(noreplace) %{_sysconfdir}/apptainer/cgroups
%config(noreplace) %{_sysconfdir}/apptainer/ecl.toml
%config(noreplace) %{_sysconfdir}/apptainer/global-pgp-public
%config(noreplace) %{_sysconfdir}/apptainer/network
%config(noreplace) %{_sysconfdir}/apptainer/nvliblist.conf
%config(noreplace) %{_sysconfdir}/apptainer/seccomp-profiles
%config(noreplace) %{_sysconfdir}/apptainer/apptainer.conf
%config(noreplace) %{_sysconfdir}/apptainer/remote.yaml
%config(noreplace) %{_sysconfdir}/apptainer/rocmliblist.conf
%config(noreplace) %{_sysconfdir}/apptainer/dmtcp-conf.yaml
%{_datadir}/bash-completion/completions/*
%dir %{_localstatedir}/apptainer
%dir %{_localstatedir}/apptainer/mnt
%dir %{_localstatedir}/apptainer/mnt/session
%{_mandir}/man1/*

%changelog
