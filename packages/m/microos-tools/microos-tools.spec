#
# spec file for package microos-tools
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


%{!?_distconfdir: %global _distconfdir %{_prefix}%{_sysconfdir}}

Name:           microos-tools
Version:        4.0+git23
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

%package -n zypp-no-recommends
Summary:        Disable recommends of libzypp by default
Requires:       libzypp(econf)

%description -n zypp-no-recommends
This package installs a zypp.conf snippet to disable Recommends.

%package -n zypp-excludedocs
Summary:        Exclude installation of docs by libzypp
Requires:       libzypp(econf)

%description -n zypp-excludedocs
This package installs a zypp.conf snippet to enable excludedocs.

%package -n zypp-no-multiversion
Summary:        Don't install multiple packages in parallel
Requires:       libzypp(econf)

%description -n zypp-no-multiversion
This package installs a zypp.conf snippet to disable multiversion
settings. This is normally used to install the kernel in different
versions at the same time, but not necessary with snapshots or
transactional-update.

%prep
%autosetup -p1

%build
./autogen.sh
%configure
%make_build

%install
%make_install

%pre
%service_add_pre printenv.service import-pubring-from-rpmdb.path import-pubring-from-rpmdb.service

%preun
%service_del_preun printenv.service import-pubring-from-rpmdb.path import-pubring-from-rpmdb.service

%post
%service_add_post printenv.service import-pubring-from-rpmdb.path import-pubring-from-rpmdb.service

%postun
%service_del_postun printenv.service import-pubring-from-rpmdb.path import-pubring-from-rpmdb.service

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
%{_unitdir}/import-pubring-from-rpmdb.path
%{_unitdir}/import-pubring-from-rpmdb.service
%{_unitdir}/printenv.service
%dir %{_unitdir}/salt-minion.service.d
%{_unitdir}/salt-minion.service.d/TMPDIR.conf
%{_tmpfilesdir}/salt-minion-tmpdir.conf
%dir %{_distconfdir}/tukit.conf.d
%{_distconfdir}/tukit.conf.d/salt-tukit.conf
%{_bindir}/import-pubring-from-rpmdb
%{_bindir}/man-online
%{_distconfdir}/profile.d/man-online.sh
%{_distconfdir}/profile.d/zypp-single-rpmtrans.sh
%dir %{_systemd_util_dir}/system.conf.d
%{_systemd_util_dir}/system.conf.d/10-zypp-single-rpmtrans.conf

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

%files -n zypp-no-recommends
%dir %{_prefix}/etc/zypp
%dir %{_prefix}/etc/zypp/zypp.conf.d
%{_prefix}/etc/zypp/zypp.conf.d/no-recommends.conf

%files -n zypp-excludedocs
%dir %{_prefix}/etc/zypp
%dir %{_prefix}/etc/zypp/zypp.conf.d
%{_prefix}/etc/zypp/zypp.conf.d/excludedocs.conf

%files -n zypp-no-multiversion
%dir %{_prefix}/etc/zypp
%dir %{_prefix}/etc/zypp/zypp.conf.d
%{_prefix}/etc/zypp/zypp.conf.d/no-multiversion.conf

%changelog
