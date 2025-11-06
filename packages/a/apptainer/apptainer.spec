#
# spec file for package apptainer
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2025 SUSE LLC and contributors
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

Summary:        Application and environment virtualization
# CRYPTOGAMS isn't known in OBS
#License:        BSD-3-Clause-LBNL and (OpenSSL or CRYPTOGAMS)
License:        BSD-3-Clause-LBNL AND OpenSSL
Group:          Productivity/Clustering/Computing
Name:           apptainer
Version:        1.4.2
Release:        0
# https://spdx.org/licenses/BSD-3-Clause-LBNL.html
URL:            https://apptainer.org
Obsoletes:      singularity <= 3.8.5
Conflicts:      singularity
Conflicts:      singularity-ce
Conflicts:      singularity-runtime
Source0:        https://github.com/apptainer/apptainer/archive/v%{version}%{?vers_suffix}/apptainer-%{version}%{?vers_suffix}.tar.gz
Source1:        README.SUSE
Source2:        SUSE.def
Source5:        SLE-15SP7.def
Source6:        SLE-16.def
Source10:       Leap.def
Source20:       %{name}-rpmlintrc
Source21:       vendor.tar.gz
BuildRequires:  cryptsetup
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  git
BuildRequires:  go >= 1.19
BuildRequires:  libuuid-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  sysuser-tools
BuildRequires:  libseccomp-devel
Requires:       squashfs
Requires:       squashfuse
Recommends:     fuse2fs
Recommends:     gocryptfs
Requires:       (apptainer-leap = %version if product(Leap) >= 15.5)
Requires:       (apptainer-sle15_7 = %version if product(SUSE_SLE) = 15.7)
Requires:       (apptainer-sle16 = %version if product(SUSE_SLE) = 16.0)

# Needed for container decryption in userspace, upstream rpms include this
# but factory should have this seperately
Recommends:     gocryptfs
PreReq:         permissions

# there's no golang for ppc64 & %ix86, ppc64le does not have non pie builds
ExcludeArch:    ppc64 ppc64le %ix86 s390 s390x

%description
Apptainer provides functionality to make portable
containers that can be used across host environments.

%package   sle15_7
Summary:        Apptainer Definition File Templates for SLE 15 SP7
BuildArch:      noarch
Requires:       apptainer = %version

%description sle15_7
The package provides a definition file template for Apptainer containers
based on SUSE Linux Enterprise 15 SP7.

%package   sle16
Summary:        Apptainer Definition File Templates for SLE 16
BuildArch:      noarch
Requires:       apptainer = %version

%description sle16
The package provides a definition file template for Apptainer containers
based on SUSE Linux Enterprise 16.

%package leap
Summary:        Apptainer Definition File Templates for current openSUSE Leap
BuildArch:      noarch
Requires:       apptainer = %version

%description leap
The package provides a definition file template for Apptainer containers
based on the latest openSUSE Leap release.

%prep
%autosetup -n %{name}-%{version}%{?vers_suffix} -a21
cp %{S:1} .

%build

# create VERSION file
echo %version > VERSION
# Not all of these parameters currently have an effect, but they might be
# used someday.  They are the same parameters as in the configure macro.
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
        --localstatedir=%{_localstatedir}/lib \
        --sharedstatedir=%{_sharedstatedir} \
        --mandir=%{_mandir} \
        --infodir=%{_infodir} \
        --without-suid \
        --reproducible

%make_build -C builddir V=""

%install
export GOPATH=$PWD/gopath
export GOFLAGS=-mod=vendor
export PATH=$GOPATH/bin:$PATH

%make_install -C builddir V=
install -d -m 0755 %{buildroot}/%{_datarootdir}/apptainer/templates
install -m 0644 %{S:2} %{S:5} %{S:6} %{S:10} %{buildroot}/%{_datarootdir}/apptainer/templates

%fdupes apptainer/examples
%fdupes -s %buildroot

%files
%doc examples
%doc CONTRIBUTING.md
%doc README.md
%doc CHANGELOG.md
%doc CONTRIBUTORS.md
%doc %{basename:%{S:1}}
%license LICENSE.md
%license LICENSE_THIRD_PARTY.md
%license LICENSE_DEPENDENCIES.md
%{_bindir}/*
%dir %{_libexecdir}/apptainer
%dir %{_libexecdir}/apptainer/bin
%dir %{_libexecdir}/apptainer/cni
%dir %{_libexecdir}/apptainer/lib
%dir %{_datarootdir}/apptainer
%dir %{_datarootdir}/apptainer/templates
%{_libexecdir}/apptainer/bin/starter
%{_libexecdir}/apptainer/lib/offsetpreload.so
%{_libexecdir}/apptainer/cni/*
%{_datarootdir}/apptainer/templates/%{basename:%{S:2}}
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
%dir %{_localstatedir}/lib/apptainer
%dir %{_localstatedir}/lib/apptainer/mnt
%dir %{_localstatedir}/lib/apptainer/mnt/session
%{_mandir}/man1/*

%files sle15_7
%{_datarootdir}/apptainer/templates/%{basename:%{S:5}}

%files sle16
%{_datarootdir}/apptainer/templates/%{basename:%{S:6}}

%files leap
%{_datarootdir}/apptainer/templates/%{basename:%{S:10}}

%changelog
