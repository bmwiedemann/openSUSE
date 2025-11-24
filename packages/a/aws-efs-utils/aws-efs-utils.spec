#
# spec file for package aws-efs-utils
#
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


%if 0%{?suse_version} >= 1600
%define pythons %{primary_python}
%else
%define pythons python311
%endif
%global _sitelibdir %{%{pythons}_sitelib}
Name:           aws-efs-utils
Version:        2.4.1
Release:        0
Summary:        Utilities for using the EFS file systems
License:        MIT
Group:          System/Management
URL:            https://github.com/aws/efs-utils
Source0:        efs-utils-v%{version}.tar.gz
Source1:        vendor.tar.gz
Patch0:         disable_mount_efs_test.patch
Patch1:         harden_amazon-efs-mount-watchdog.service.patch
Patch2:         skip-styletest.patch
Patch3:         use_mock_from_unittest.patch
# PATCH-FIX-UPSTREAM - Initialize arrays as arrays - https://github.com/aws/aws-lc/pull/2042
Patch4:         initialize-arrays-as-arrays.patch
# PATCH-FIX-UPSTREAM - Support relro in delocator - https://github.com/aws/aws-lc/pull/2455
Patch5:         support-relro-in-delocator.patch
# PATCH-FIX-OPENSUSE - fix cargo checksums after patching
Patch6:         fix-cargo-checksums.patch
BuildRequires:  %{pythons}-botocore >= 1.34.140
BuildRequires:  %{pythons}-coverage >= 7.6.0
BuildRequires:  %{pythons}-pbr >= 3.1.1
BuildRequires:  %{pythons}-pluggy >= 0.13.0
BuildRequires:  %{pythons}-py >= 1.11.0
BuildRequires:  %{pythons}-pytest >= 8.2.2
BuildRequires:  %{pythons}-pytest-cov >= 5.0.0
BuildRequires:  %{pythons}-pytest-html >= 4.1.1
BuildRequires:  %{pythons}-pytest-metadata >= 3.1.1
BuildRequires:  %{pythons}-pytest-mock >= 3.14.0
BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  clang-devel
BuildRequires:  cmake
%if 0%{?suse_version} <= 1500
BuildRequires:  gcc13
BuildRequires:  gcc13-c++
%endif
BuildRequires:  libopenssl-devel
BuildRequires:  openssl
BuildRequires:  rust
BuildRequires:  systemd-rpm-macros
BuildRequires:  golang(API) >= 1.24
BuildRequires:  pkgconfig(systemd)
Requires:       nfs-utils
Requires:       stunnel >= 4.56

%description
This package provides utilities for using the EFS file systems.

%prep
%setup -n efs-utils-v%{version} -a1
%patch -P 0 -p1
find src/mount_efs src/watchdog -name "*.py" -exec sed -i 's/env python3/python3/' {} +
%patch -P 1 -p1
%patch -P 2
%patch -P 3 -p1
%patch -P 4 -p1
%patch -P 5 -p1
%patch -P 6 -p1

%build
%if 0%{?suse_version} <= 1500
export RUSTFLAGS=" -C linker=/usr/bin/gcc-13"
%endif
cd src/proxy
%cargo_build

%check
make test

%install
mkdir -p %{buildroot}%{_sysconfdir}/amazon/efs
mkdir -p %{buildroot}%{_unitdir}
install -p -m 644 %{_builddir}/efs-utils-v%{version}/dist/amazon-efs-mount-watchdog.service %{buildroot}%{_unitdir}

mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_localstatedir}/log/amazon/efs
mkdir -p %{buildroot}%{_mandir}/man8
mkdir -p %{buildroot}%{_sysconfdir}/amazon/efs

install -p -m 644 %{_builddir}/efs-utils-v%{version}/dist/efs-utils.conf %{buildroot}%{_sysconfdir}/amazon/efs
install -p -m 444 %{_builddir}/efs-utils-v%{version}/dist/efs-utils.crt %{buildroot}%{_sysconfdir}/amazon/efs
install -p -m 755 %{_builddir}/efs-utils-v%{version}/src/mount_efs/__init__.py %{buildroot}%{_sbindir}/mount.efs
install -p -m 755 %{_builddir}/efs-utils-v%{version}/src/watchdog/__init__.py %{buildroot}%{_bindir}/amazon-efs-mount-watchdog
install -p -m 644 %{_builddir}/efs-utils-v%{version}/man/mount.efs.8 %{buildroot}%{_mandir}/man8

%if 0%{?suse_version} <= 1500
export RUSTFLAGS=" -C linker=/usr/bin/gcc-13"
%endif
cd src/proxy
%cargo_install

# Create rc-link
for srv_name in %{buildroot}%{_unitdir}/*.service; do rc_name=$(basename -s '.service' $srv_name); ln -s service %{buildroot}%{_sbindir}/rc$rc_name; done

%pre
%service_add_pre amazon-efs-mount-watchdog.service

%post
%service_add_post amazon-efs-mount-watchdog.service

%preun
%service_del_preun amazon-efs-mount-watchdog.service

%postun
%service_del_postun amazon-efs-mount-watchdog.service

%files
%defattr(-,root,root,-)
%doc NOTICE README.md
%license LICENSE
%{_unitdir}/amazon-efs-mount-watchdog.service
%{_sysconfdir}/amazon
%config %{_sysconfdir}/amazon/efs/efs-utils.conf
%config %{_sysconfdir}/amazon/efs/efs-utils.crt
%{_bindir}/efs-proxy
%{_sbindir}/mount.efs
%{_bindir}/amazon-efs-mount-watchdog
%{_sbindir}/rcamazon-efs-mount-watchdog
%{_var}/log/amazon
%{_mandir}/man8/mount.efs.8.gz

%changelog
