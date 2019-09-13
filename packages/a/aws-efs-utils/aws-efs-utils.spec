#
# spec file for package aws-efs-utils
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


Name:           aws-efs-utils
Version:        1.7
Release:        0
Summary:        Utilities for using the EFS file systems
License:        MIT
Group:          System/Management
Url:            https://github.com/aws/efs-utils
Source0:        https://github.com/aws/efs-utils/archive/v%{version}.tar.gz
Patch:          efs-switchparser.patch
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros
Requires:       nfs-utils
Requires:       python3
Requires:       stunnel >= 4.56
BuildArch:      noarch

%description
This package provides utilities for using the EFS file systems.

%prep
%setup -n efs-utils-%{version}
find . -name "*.py" -exec sed -i 's/env python/python3/' {} +
%patch  -p1

%build
# No build required

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
%service_del_preun -f amazon-efs-mount-watchdog.service

%postun
%service_del_postun -f amazon-efs-mount-watchdog.service

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
