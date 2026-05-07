#
# spec file for package aliyun-alinas-utils
#
# Copyright (c) 2026 SUSE LLC and contributors
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

Name:           aliyun-alinas-utils
Version:        2.2+20260207_0a55ca4
Release:        0
Summary:        Utilities for Aliyun Alinas File System (alinas)
License:        MIT
Group:          System/Management
URL:            https://github.com/alibaba/alibabacloud-nas-utils
Source0:        aliyun-alinas-utils-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(systemd)

%description
Utilities for Aliyun Alinas and CPFS File System (alinas)

%prep
%setup -n %{name}-%{version}
# Fix interpretor shebang
find . -name "*.py" -exec sed -i 's|#\!/usr/bin/env\ python3|#\!/usr/bin/python3|g' {} \;
# Fix installation path for Python modules and executables
sed -i 's|\(PACKAGE_PATH\ \=\ \)\"/opt/aliyun/cpfs/\"|\1\"%{python_sitelib}/aliyun/cpfs/\"|g' alinas-utils/src/cpfs/mount_cpfs/__init__.py
sed -i 's|\(PACKAGE_PATH\ \=\ \)\"/opt/aliyun/cpfs/\"|\1\"%{python_sitelib}/aliyun/cpfs/\"|g' alinas-utils/src/cpfs/watchdog/__init__.py
sed -i 's|\(PACKAGE_PATH\ \=\ \)\"/opt/aliyun/cpfs/\"|\1\"%{python_sitelib}/aliyun/cpfs/\"|g' alinas-utils/src/cpfs/cpfs_nfs_tool/ping.py
sed -i 's|\(PACKAGE_PATH\ \=\ \)\"/opt/aliyun/cpfs/\"|\1\"%{python_sitelib}/aliyun/cpfs/\"|g' alinas-utils/src/cpfs/cpfs_nfs_tool/switch_server.py
sed -i 's|\(TOOL_DIR\=\)/opt/aliyun/cpfs/tools|\1%{_libexecdir}/aliyun|g' alinas-utils/src/cpfs/cpfs_nfs_tool/cpfsu.sh
sed -i 's|/sbin|%{_sbindir}|g' alinas-utils/src/alinas/mount_alinas/umount.efc.sh
sed -i 's|/usr/bin/env\ aliyun-alinas-mount-watchdog|%{_sbindir}/aliyun-alinas-mount-watchdog|g' alinas-utils/dist/alinas/aliyun-alinas-mount-watchdog.service
sed -i 's|/usr/bin/env\ aliyun-cpfs-mount-watchdog|%{_sbindir}/aliyun-cpfs-mount-watchdog|g' alinas-utils/dist/cpfs/aliyun-cpfs-mount-watchdog.service

%build
make -C alinas-utils id-gen

%install
mkdir -p %{buildroot}%{_libexecdir}/aliyun
mkdir -p %{buildroot}%{_sysconfdir}/aliyun/alinas
mkdir -p %{buildroot}%{_sysconfdir}/aliyun/cpfs
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_sitelibdir}/aliyun/cpfs
mkdir -p %{buildroot}%{_localstatedir}/log/aliyun/alinas
mkdir -p %{buildroot}%{_localstatedir}/log/aliyun/cpfs

install -p -m 644 %{_builddir}/%{name}-%{version}/alinas-utils/dist/alinas/alinas-utils.conf %{buildroot}%{_sysconfdir}/aliyun/alinas/alinas-utils.conf
install -p -m 644 %{_builddir}/%{name}-%{version}/alinas-utils/dist/alinas-utils.crt %{buildroot}%{_sysconfdir}/aliyun/alinas/alinas-utils.crt
install -p -m 644 %{_builddir}/%{name}-%{version}/alinas-utils/dist/cpfs/cpfs-utils.conf %{buildroot}%{_sysconfdir}/aliyun/cpfs/cpfs-utils.conf

install -p -m 644 %{_builddir}/%{name}-%{version}/alinas-utils/dist/alinas/aliyun-alinas-mount-watchdog.conf %{buildroot}%{_sysconfdir}/aliyun/alinas/
install -p -m 644 %{_builddir}/%{name}-%{version}/alinas-utils/dist/cpfs/aliyun-cpfs-mount-watchdog.conf %{buildroot}%{_sysconfdir}/aliyun/cpfs/

install -p -m 644 %{_builddir}/%{name}-%{version}/alinas-utils/dist/alinas/aliyun-alinas-mount-watchdog.service %{buildroot}%{_unitdir}
install -p -m 644 %{_builddir}/%{name}-%{version}/alinas-utils/dist/cpfs/aliyun-cpfs-mount-watchdog.service %{buildroot}%{_unitdir}

install -D -p -m 755 alinas-utils/src/alinas/nas_agent/identifier-generator %{buildroot}%{_bindir}/identifier-generator

install -D -p -m 755 alinas-utils/src/alinas/mount_alinas/__init__.py %{buildroot}%{_sbindir}/mount.alinas
install -D -p -m 755 alinas-utils/src/alinas/mount_alinas/umount.efc.sh %{buildroot}%{_sbindir}/umount.alifuse.aliyun-alinas-efc
install -D -p -m 755 alinas-utils/src/alinas/mount_alinas/umount.efc.sh %{buildroot}%{_sbindir}/umount.alifuse.aliyun-alinas-eac
install -D -p -m 755 alinas-utils/src/alinas/mount_alinas/umount.efc.sh %{buildroot}%{_sbindir}/umount.fuse.aliyun-alinas-efc
install -D -p -m 755 alinas-utils/src/alinas/watchdog/__init__.py %{buildroot}%{_sbindir}/aliyun-alinas-mount-watchdog
install -D -p -m 755 alinas-utils/src/cpfs/mount_cpfs/__init__.py %{buildroot}%{_sbindir}/mount.cpfs-nfs
install -D -p -m 755 alinas-utils/src/cpfs/watchdog/__init__.py %{buildroot}%{_sbindir}/aliyun-cpfs-mount-watchdog
install -D -p -m 755 alinas-utils/src/cpfs/cpfs_nfs_common/__init__.py %{buildroot}%{_sitelibdir}/aliyun/cpfs/cpfs_nfs_common.py
install -D -p -m 755 alinas-utils/src/cpfs/cpfs_nfs_tool/cpfsu.sh %{buildroot}%{_sbindir}/cpfsu

install -p -m 755 %{_builddir}/%{name}-%{version}/alinas-utils/src/cpfs/cpfs_nfs_tool/ping.py %{buildroot}%{_libexecdir}/aliyun/ping
install -p -m 755 %{_builddir}/%{name}-%{version}/alinas-utils/src/cpfs/cpfs_nfs_tool/switch_server.py %{buildroot}%{_libexecdir}/aliyun/switch_server

install -p -m 644 %{_builddir}/%{name}-%{version}/alinas-utils/dist/alinas/aliyun-alinas-efc-minimum-supported-kernel-versions.json \
                  %{buildroot}%{_sysconfdir}/aliyun/alinas/aliyun-alinas-efc-minimum-supported-kernel-versions.json

%fdupes %{buildroot}

%pre
%service_add_pre aliyun-alinas-mount-watchdog.service aliyun-cpfs-mount-watchdog.service

%post
%service_add_post aliyun-alinas-mount-watchdog.service aliyun-cpfs-mount-watchdog.service

%preun
%service_del_preun aliyun-alinas-mount-watchdog.service aliyun-cpfs-mount-watchdog.service

%postun
%service_del_postun aliyun-alinas-mount-watchdog.service aliyun-cpfs-mount-watchdog.service

%files
%defattr(-,root,root,-)
%doc README.md
%license LICENSE
%{_unitdir}/aliyun-alinas-mount-watchdog.service
%{_unitdir}/aliyun-cpfs-mount-watchdog.service
%dir %{_sysconfdir}/aliyun
%dir %{_sysconfdir}/aliyun/alinas
%dir %{_sysconfdir}/aliyun/cpfs
%config(noreplace) %{_sysconfdir}/aliyun/alinas/alinas-utils.conf
%config(noreplace) %{_sysconfdir}/aliyun/alinas/aliyun-alinas-mount-watchdog.conf
%config(noreplace) %{_sysconfdir}/aliyun/cpfs/aliyun-cpfs-mount-watchdog.conf
%config(noreplace) %{_sysconfdir}/aliyun/cpfs/cpfs-utils.conf
%{_sysconfdir}/aliyun/alinas/aliyun-alinas-efc-minimum-supported-kernel-versions.json
%{_sysconfdir}/aliyun/alinas/alinas-utils.crt
%dir %{python_sitelib}/aliyun/cpfs/
%dir %{python_sitelib}/aliyun/
%{_sitelibdir}/aliyun/cpfs/cpfs_nfs_common.py
%{_bindir}/identifier-generator
%dir %{_libexecdir}/aliyun/
%{_libexecdir}/aliyun/ping
%{_libexecdir}/aliyun/switch_server
%dir %{_localstatedir}/log/aliyun/
%dir %{_localstatedir}/log/aliyun/alinas
%dir %{_localstatedir}/log/aliyun/cpfs
%{_sbindir}/aliyun-alinas-mount-watchdog
%{_sbindir}/aliyun-cpfs-mount-watchdog
%{_sbindir}/cpfsu
%{_sbindir}/mount.alinas
%{_sbindir}/mount.cpfs-nfs
%{_sbindir}/umount.alifuse.aliyun-alinas-eac
%{_sbindir}/umount.alifuse.aliyun-alinas-efc
%{_sbindir}/umount.fuse.aliyun-alinas-efc

%changelog
