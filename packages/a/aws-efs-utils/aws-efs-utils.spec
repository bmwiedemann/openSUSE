#
# spec file for package aws-efs-utils
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


Name:           aws-efs-utils
Version:        1.34.3
Release:        0
Summary:        Utilities for using the EFS file systems
License:        MIT
Group:          System/Management
URL:            https://github.com/aws/efs-utils
Source0:        %{url}/archive/v%{version}.tar.gz#/efs-utils-%{version}.tar.gz
Patch0:         disable_mount_efs_test.patch
Patch1:         harden_amazon-efs-mount-watchdog.service.patch
Patch2:         skip-styletest.patch
Patch3:         use_mock_from_unittest.patch
BuildRequires:  openssl
BuildRequires:  python3-attrs >= 17.4.0
BuildRequires:  python3-botocore >= 1.17.53
BuildRequires:  python3-coverage >= 4.5.4
#BuildRequires:  python3-flake8 >= 3.7.9
BuildRequires:  python3-flake8
BuildRequires:  python3-mccabe >= 0.6.1
BuildRequires:  python3-pbr >= 3.1.1
BuildRequires:  python3-pluggy >= 0.13.0
BuildRequires:  python3-py >= 1.10.0
BuildRequires:  python3-pycodestyle >= 2.5.0
BuildRequires:  python3-pyflakes >= 2.1.1
BuildRequires:  python3-pytest >= 4.6.7
BuildRequires:  python3-pytest-cov >= 2.8.1
BuildRequires:  python3-pytest-html >= 1.19.0
BuildRequires:  python3-pytest-metadata >= 1.7.0
BuildRequires:  python3-pytest-mock >= 1.11.2
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(systemd)
Requires:       nfs-utils
Requires:       stunnel >= 4.56
BuildArch:      noarch

%description
This package provides utilities for using the EFS file systems.

%prep
%setup -n efs-utils-%{version}
%patch0 -p1
find . -name "*.py" -exec sed -i 's/env python3/python3/' {} +
%patch1 -p1
%patch2
%patch3 -p1

%build
# No build required

%check
make test

%install
mkdir -p %{buildroot}%{_sysconfdir}/amazon/efs
mkdir -p %{buildroot}%{_unitdir}
install -p -m 644 %{_builddir}/efs-utils-%{version}/dist/amazon-efs-mount-watchdog.service %{buildroot}%{_unitdir}

mkdir -p %{buildroot}/sbin
mkdir -p %{buildroot}/usr/sbin
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_localstatedir}/log/amazon/efs
mkdir -p %{buildroot}%{_mandir}/man8
mkdir -p %{buildroot}%{_sysconfdir}/amazon/efs

install -p -m 644 %{_builddir}/efs-utils-%{version}/dist/efs-utils.conf %{buildroot}%{_sysconfdir}/amazon/efs
install -p -m 444 %{_builddir}/efs-utils-%{version}/dist/efs-utils.crt %{buildroot}%{_sysconfdir}/amazon/efs
install -p -m 755 %{_builddir}/efs-utils-%{version}/src/mount_efs/__init__.py %{buildroot}/sbin/mount.efs
install -p -m 755 %{_builddir}/efs-utils-%{version}/src/watchdog/__init__.py %{buildroot}%{_bindir}/amazon-efs-mount-watchdog
install -p -m 644 %{_builddir}/efs-utils-%{version}/man/mount.efs.8 %{buildroot}%{_mandir}/man8

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
/sbin/mount.efs
%{_bindir}/amazon-efs-mount-watchdog
%{_sbindir}/rcamazon-efs-mount-watchdog
/var/log/amazon
%{_mandir}/man8/mount.efs.8.gz

%changelog
