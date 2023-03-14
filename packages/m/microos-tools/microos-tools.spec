#
# spec file for package microos-tools
#
# Copyright (c) 2023 SUSE LLC
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


%{!?_distconfdir: %global _distconfdir %{_prefix}%{_sysconfdir}}

Name:           microos-tools
Version:        2.19
Release:        0
Summary:        Files and Scripts for openSUSE MicroOS
License:        GPL-2.0-or-later
Group:          Development/Tools/Other
URL:            https://github.com/openSUSE/microos-tools
Source:         https://github.com/openSUSE/microos-tools/releases/download/v%{version}/microos-tools-%{version}.tar.xz
Source1:        tmp.mount
Source2:        microos-tmp.conf
Source99:       microos-tools-rpmlintrc
BuildRequires:  distribution-release
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(dracut)
BuildRequires:  pkgconfig(rpm)
BuildRequires:  pkgconfig(systemd)
Requires:       read-only-root-fs
Conflicts:      systemd-coredump

%description
Files, scripts and directories for openSUSE MicroOS.

%package -n microos-devel-tools
Summary:        Tools to develop MicroOS

%description -n microos-devel-tools
This package contains tools to make developing of MicroOS easier.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install
%if 0%{?suse_version} <= 1500
install -m 0644 %{SOURCE1} %{buildroot}/%{_unitdir}/
install -m 0644 %{SOURCE2} %{buildroot}/%{_tmpfilesdir}
%endif

%pre
%service_add_pre setup-systemd-proxy-env.service setup-systemd-proxy-env.path printenv.service

%post
%{regenerate_initrd_post}
%service_add_post setup-systemd-proxy-env.service setup-systemd-proxy-env.path printenv.service

%preun
%service_del_preun setup-systemd-proxy-env.service setup-systemd-proxy-env.path printenv.service

%postun
%{regenerate_initrd_post}
%service_del_postun setup-systemd-proxy-env.service setup-systemd-proxy-env.path printenv.service

%posttrans
%{regenerate_initrd_posttrans}

%pre -n microos-devel-tools
%service_add_pre microos-ro.service

%post -n microos-devel-tools
%service_add_post microos-ro.service

%preun -n microos-devel-tools
%service_del_preun microos-ro.service

%postun -n microos-devel-tools
%service_del_postun microos-ro.service

%files
%license COPYING
%dir %{_sysconfdir}/selinux
%config %{_sysconfdir}/selinux/fixfiles_exclude_dirs
%{_unitdir}/printenv.service
%{_unitdir}/setup-systemd-proxy-env.path
%{_unitdir}/setup-systemd-proxy-env.service
%dir %{_unitdir}/salt-minion.service.d
%{_unitdir}/salt-minion.service.d/TMPDIR.conf
%{_tmpfilesdir}/salt-minion-tmpdir.conf
%if %{?suse_version} <= 1500
%dir %{_distconfdir}
%endif
%dir %{_distconfdir}/tukit.conf.d
%{_distconfdir}/tukit.conf.d/salt-tukit.conf
%{_sysctldir}/30-corefiles.conf
%{_sbindir}/setup-systemd-proxy-env
%dir %{_prefix}/lib/dracut
%dir %{_prefix}/lib/dracut/modules.d
%{_prefix}/lib/dracut/modules.d/98selinux-microos
%{_systemdgeneratordir}/selinux-autorelabel-generator
%if 0%{?suse_version} <= 1500
%{_unitdir}/tmp.mount
%{_tmpfilesdir}/microos-tmp.conf
%endif

%files -n microos-devel-tools
%{_unitdir}/microos-ro.service
%{_sbindir}/microos-ro
%{_sbindir}/microos-rw
%{_sbindir}/rpm-sortbysize
%{_sbindir}/rpmorphan
%{_sbindir}/sysext-add-debug

%changelog
