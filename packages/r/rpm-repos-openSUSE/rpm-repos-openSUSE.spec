#
# spec file for package rpm-repos-openSUSE
#
# Copyright (c) 2021 Neal Gompa <ngompa13@gmail.com>.
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

%if 0%{?suse_version} && (!0%{?sle_version})
%global distname Tumbleweed
%endif

%if 0%{?suse_version} && 0%{?sle_version} && 0%{?is_opensuse}
%global distname Leap
%endif

# This needs to be archful to implement different repo paths for Ports and such,
# but contains no compiled content...
%global debug_package %{nil}

# Main package version
%global mainversion 0

Name:           rpm-repos-openSUSE
Version:        %{mainversion}
Release:        0
Summary:        openSUSE package repositories
Group:          System/Management
License:        MIT
URL:            https://opensuse.org/

# Script to generate symlinks for RPM GPG key files
Source0:        create-rpmgpg-symlinks.sh

# openSUSE Tumbleweed repo configs
Source1:        opensuse-tumbleweed-oss.repo
Source2:        opensuse-tumbleweed-non-oss.repo
Source3:        opensuse-tumbleweed-oss-ports.repo.in
Source4:        opensuse-tumbleweed-update.repo
Source5:        opensuse-tumbleweed-update-ports.repo.in

# openSUSE Leap repo configs
Source11:       opensuse-leap-oss.repo
Source12:       opensuse-leap-non-oss.repo
Source13:       opensuse-leap-oss-ports.repo.in
Source14:       opensuse-leap-sle-update.repo
Source15:       opensuse-leap-sle-backports-update.repo

%description
openSUSE package repository files for DNF and PackageKit with GPG public keys

# -------------------------------------------------------------------------------

%package %{distname}
Summary:        openSUSE %{distname} package repositories
Version:        %{suse_version}
%if "%{distname}" == "Tumbleweed"
# Unconditionally ensure Leap upgrades to Tumbleweed
Obsoletes:      %{name}-Leap
Conflicts:      %{name}-Leap
%endif

# We require the GPG keys in the repo keys subpackage
Requires:       rpm-repo-keys-openSUSE = %{mainversion}-%{release}

# We're compatible with any SUSE Linux distribution
Requires:       suse-release

# Only one instance of this package may be installed at a time...
Provides:       %{name}
Conflicts:      %{name}

# Prefer the version that matches our distribution
Suggests:       %{name}-%{distname}

%description %{distname}
openSUSE %{distname} package repository files for DNF and PackageKit.

%files %{distname}
%dir %{_sysconfdir}/yum.repos.d
%config(noreplace) %{_sysconfdir}/yum.repos.d/*
%if "%{distname}" == "Leap"
%exclude %{_sysconfdir}/yum.repos.d/opensuse-tumbleweed-*.repo
%endif

# -------------------------------------------------------------------------------

%if "%{distname}" == "Leap"
%package Tumbleweed
Summary:        openSUSE Tumbleweed package repositories
Version:        %{suse_version}
Conflicts:      %{name}-Leap

# We require the GPG keys in the repo keys subpackage
Requires:       rpm-repo-keys-openSUSE = %{mainversion}-%{release}

# We're compatible with any SUSE Linux distribution
Requires:       suse-release

# Only one instance of this package may be installed at a time...
Provides:       %{name}
Conflicts:      %{name}

%description Tumbleweed
openSUSE %{distname} package repository files for DNF and PackageKit.

%files Tumbleweed
%dir %{_sysconfdir}/yum.repos.d
%config(noreplace) %{_sysconfdir}/yum.repos.d/opensuse-tumbleweed-*.repo

%endif

# -------------------------------------------------------------------------------

%package -n rpm-repo-keys-openSUSE
Summary:        openSUSE repository GPG keys
# The actual keys are stored in openSUSE-build-key
BuildRequires:  openSUSE-build-key
Requires:       openSUSE-build-key
BuildArch:      noarch


%description -n rpm-repo-keys-openSUSE
openSUSE GPG keys for validating packages from openSUSE repositories by
DNF and PackageKit.

%files -n rpm-repo-keys-openSUSE
%dir %{_sysconfdir}/pki
%dir %{_sysconfdir}/pki/rpm-gpg
%{_sysconfdir}/pki/rpm-gpg/*

# -------------------------------------------------------------------------------

%prep
# Nothing to prepare


%build
# Nothing to build


%install
# Install the GPG key symlinks
mkdir -p %{buildroot}%{_sysconfdir}/pki/rpm-gpg
bash %{S:0} %{buildroot}

%if (0%{?sle_version} && 0%{?sle_version} < 150300) || "%{distname}" == "Tumbleweed"
rm %{buildroot}%{_sysconfdir}/pki/rpm-gpg/*SuSE*
rm %{buildroot}%{_sysconfdir}/pki/rpm-gpg/*Backports*
%endif

# Install the repositories
mkdir -p %{buildroot}%{_sysconfdir}/yum.repos.d

# ==== Primary Tumbleweed repository configuration ====

# Setup for primary arches
%ifarch %{ix86} x86_64
install %{S:1} -pm 0644 %{buildroot}%{_sysconfdir}/yum.repos.d
install %{S:2} -pm 0644 %{buildroot}%{_sysconfdir}/yum.repos.d
install %{S:4} -pm 0644 %{buildroot}%{_sysconfdir}/yum.repos.d
%endif

# Setup for ports
%ifarch aarch64 %{arm} %{power64} ppc s390x riscv64
install %{S:3} -pm 0644 %{buildroot}%{_sysconfdir}/yum.repos.d/opensuse-tumbleweed-oss.repo
install %{S:5} -pm 0644 %{buildroot}%{_sysconfdir}/yum.repos.d/opensuse-tumbleweed-update.repo

%ifnarch %{power64} ppc s390x riscv64
sed -e 's/@DIST_ARCH@/%{_target_cpu}/g' -i %{buildroot}%{_sysconfdir}/yum.repos.d/opensuse-tumbleweed-{oss,update}.repo
%endif

%ifarch %{power64} ppc
sed -e 's/@DIST_ARCH@/ppc/g' -i %{buildroot}%{_sysconfdir}/yum.repos.d/opensuse-tumbleweed-{oss,update}.repo
%endif

%ifarch riscv64
sed -e 's/@DIST_ARCH@/riscv/g' -i %{buildroot}%{_sysconfdir}/yum.repos.d/opensuse-tumbleweed-{oss,update}.repo
%endif

%ifarch s390x
sed -e 's/@DIST_ARCH@/zsystems/g' -i %{buildroot}%{_sysconfdir}/yum.repos.d/opensuse-tumbleweed-{oss,update}.repo
%endif

%endif

%if "%{distname}" == "Leap"

# ==== Primary Leap repository configuration ====

%if 0%{?sle_version} >= 150300
# Setup for main SLE/Leap arches
#ifarch ix86 x86_64 aarch64 power64 s390x
install %{S:11} -pm 0644 %{buildroot}%{_sysconfdir}/yum.repos.d
install %{S:12} -pm 0644 %{buildroot}%{_sysconfdir}/yum.repos.d
install %{S:14} -pm 0644 %{buildroot}%{_sysconfdir}/yum.repos.d
install %{S:15} -pm 0644 %{buildroot}%{_sysconfdir}/yum.repos.d

# TODO: Add "Step" repos for arm and riscv64

%else
# Setup for primary arches
%ifarch %{ix86} x86_64
install %{S:11} -pm 0644 %{buildroot}%{_sysconfdir}/yum.repos.d
install %{S:12} -pm 0644 %{buildroot}%{_sysconfdir}/yum.repos.d

# Remove gpgkey lines that are not useful
sed -e "/*.RPM-GPG-KEY-SuSE*.$/d" \
    -e "/*.RPM-GPG-KEY-openSUSE-Backports*.$/d" \
    -i %{buildroot}%{_sysconfdir}/yum.repos.d/*.repo
%endif

# Setup for ports
%ifarch aarch64 %{arm} %{power64} ppc s390x riscv64
install %{S:13} -pm 0644 %{buildroot}%{_sysconfdir}/yum.repos.d/opensuse-leap-oss.repo

%ifnarch %{power64} ppc s390x riscv64
sed -e 's/@DIST_ARCH@/%{_target_cpu}/g' -i %{buildroot}%{_sysconfdir}/yum.repos.d/opensuse-leap-oss.repo
%endif

%ifarch %{power64} ppc
sed -e 's/@DIST_ARCH@/ppc/g' -i %{buildroot}%{_sysconfdir}/yum.repos.d/opensuse-leap-oss.repo
%endif

%ifarch riscv64
sed -e 's/@DIST_ARCH@/riscv/g' -i %{buildroot}%{_sysconfdir}/yum.repos.d/opensuse-leap-oss.repo
%endif

%ifarch s390x
sed -e 's/@DIST_ARCH@/zsystems/g' -i %{buildroot}%{_sysconfdir}/yum.repos.d/opensuse-leap-oss.repo
%endif

%endif

%endif

%endif

%changelog
