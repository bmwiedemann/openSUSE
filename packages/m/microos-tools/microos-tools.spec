#
# spec file for package microos-tools
#
# Copyright (c) 2024 SUSE LLC
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
Version:        4.0+git6
Release:        0
Summary:        Files and Scripts for openSUSE MicroOS
License:        GPL-2.0-or-later
Group:          Development/Tools/Other
URL:            https://github.com/openSUSE/microos-tools
Source:         microos-tools-%{version}.tar.xz
BuildRequires:  automake
BuildRequires:  distribution-release
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(dracut)
BuildRequires:  pkgconfig(rpm)
BuildRequires:  pkgconfig(systemd)
Requires:       read-only-root-fs
Requires:       selinux-autorelabel = %{version}
# for man-online
Requires:       mandoc-bin

%description
Files, scripts and directories for openSUSE MicroOS.

%package -n selinux-autorelabel
Summary:        Automatic SELinux relabelling during early boot
Requires:       /usr/bin/findmnt
Requires:       policycoreutils

%description -n selinux-autorelabel
This package contains a dracut module and systemd generator for relabelling
the system during early boot.

%package -n microos-devel-tools
Summary:        Tools to develop MicroOS

%description -n microos-devel-tools
This package contains tools to make developing of MicroOS easier.

%prep
%autosetup -p1

%build
./autogen.sh
%configure
%make_build

%install
%make_install

%pre
%service_add_pre setup-systemd-proxy-env.service setup-systemd-proxy-env.path printenv.service

%preun
%service_del_preun setup-systemd-proxy-env.service setup-systemd-proxy-env.path printenv.service

%post
%service_add_post setup-systemd-proxy-env.service setup-systemd-proxy-env.path printenv.service

%postun
%service_del_postun setup-systemd-proxy-env.service setup-systemd-proxy-env.path printenv.service

%pre -n microos-devel-tools
%service_add_pre microos-ro.service

%post -n microos-devel-tools
%service_add_post microos-ro.service

%preun -n microos-devel-tools
%service_del_preun microos-ro.service

%postun -n microos-devel-tools
%service_del_postun microos-ro.service

%pre -n selinux-autorelabel
%service_add_pre systemd-tmpfiles-setup-sys.service

%post -n selinux-autorelabel
%{regenerate_initrd_post}
%service_add_post systemd-tmpfiles-setup-sys.service

%preun -n selinux-autorelabel
%service_del_preun systemd-tmpfiles-setup-sys.service

%postun -n selinux-autorelabel
%{regenerate_initrd_post}
%service_del_postun systemd-tmpfiles-setup-sys.service

%posttrans -n selinux-autorelabel
%{regenerate_initrd_posttrans}

%files
%dir %{_sysconfdir}/selinux
%config %{_sysconfdir}/selinux/fixfiles_exclude_dirs
%{_unitdir}/printenv.service
%{_unitdir}/setup-systemd-proxy-env.path
%{_unitdir}/setup-systemd-proxy-env.service
%dir %{_unitdir}/salt-minion.service.d
%{_unitdir}/salt-minion.service.d/TMPDIR.conf
%{_tmpfilesdir}/salt-minion-tmpdir.conf
%dir %{_distconfdir}/tukit.conf.d
%{_distconfdir}/tukit.conf.d/salt-tukit.conf
%{_sbindir}/setup-systemd-proxy-env
%{_bindir}/man-online
%{_distconfdir}/profile.d/man-online.sh

%files -n selinux-autorelabel
%license COPYING
%dir %{_prefix}/lib/dracut
%dir %{_prefix}/lib/dracut/modules.d
%{_prefix}/lib/dracut/modules.d/98selinux-microos
%{_systemdgeneratordir}/selinux-autorelabel-generator
%{_unitdir}/systemd-tmpfiles-setup-sys.service

%files -n microos-devel-tools
%{_unitdir}/microos-ro.service
%{_sbindir}/microos-ro
%{_sbindir}/microos-rw
%{_sbindir}/rpm-sortbysize
%{_sbindir}/rpmorphan
%{_sbindir}/sysext-add-debug

%changelog
