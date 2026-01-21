#
# spec file for package transactional-update
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2021 Neal Gompa
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


%global somajor 8
%global libprefix libtukit
%global libname %{libprefix}%{somajor}
%global devname %{libprefix}-devel

# Compatibility macros
%{!?_distconfdir: %global _distconfdir %{_prefix}%{_sysconfdir}}

Name:           transactional-update
Version:        6.0.6
Release:        0
Summary:        Transactional Updates with btrfs and snapshots
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/Base
URL:            https://github.com/openSUSE/transactional-update
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        transactional-update.check

BuildRequires:  acl
BuildRequires:  attr
BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  bats
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  fdupes
%if %{?suse_version} <= 1500
BuildRequires:  gcc10-c++
%else
BuildRequires:  gcc-c++
%endif
BuildRequires:  libtool
BuildRequires:  libxml2-tools
BuildRequires:  libzypp
BuildRequires:  make
BuildRequires:  suse-module-tools
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dracut)
BuildRequires:  pkgconfig(libeconf)
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(mount)
BuildRequires:  pkgconfig(rpm)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(udev)
# Cannot use python3dist() names yet...
BuildRequires:  python3-lxml
BuildRequires:  w3m
BuildRequires:  xsltproc
# XXX libsolv never sees the rpmlib provides fulfilled
Requires:       (compat-usrmerge-tools or rpmlib(X-CheckUnifiedSystemdir))
Requires:       /usr/bin/bc
Requires:       dracut-transactional-update = %{version}-%{release}
Requires:       logrotate
Requires:       lsof
# psmisc is needed because of fuser
Requires:       psmisc
Requires:       tukit = %{version}-%{release}
Requires:       zypper
Requires:       (tukit-snapper-plugin if (snapper and read-only-root-fs))
# Parameter --drop-if-no-change requires it
Recommends:     inotify-tools
Recommends:     rebootmgr
Suggests:       tukitd = %{version}-%{release}
Conflicts:      health-checker < 1.8
Conflicts:      kdump < 2.1.0
# Support for /etc as subvolume
Conflicts:      read-only-root-fs < 1.0+git20250410
Conflicts:      sdbootutil < 1+git20250409
# Includes policy for the 50-etc snapper plugin
%if 0%{?suse_version} == 1600 && !0%{?is_opensuse}
Conflicts:      selinux-policy < 20241031+git652.e1d5a07e
%else
Conflicts:      selinux-policy < 20250411
%endif

%description
transactional-update is a tool to update a system in an atomic
way with zypper, btrfs and snapshots.

%package -n tukit
Summary:        Tool for doing transactional updates using Btrfs snapshots
License:        GPL-2.0-or-later
Group:          System/Base
Requires:       %{libname} = %{version}-%{release}
Conflicts:      transactional-update < 3.0.0

%description -n tukit
tukit is a simple tool to make changes to a system in an atomic way
with btrfs and snapshots.

%package -n dracut-%{name}
Summary:        Dracut module for supporting transactional updates
License:        GPL-2.0-or-later
Group:          System/Boot
Supplements:    (tukit and kernel)
Requires:       tukit = %{version}-%{release}
Conflicts:      transactional-update < 3.0.0

%description -n dracut-%{name}
This package contains the dracut modules for handling early boot aspects
for transactional updates.

%package -n tukit-snapper-plugin
Summary:        Snapper plugin for creating r/w /etc subvolumes
License:        GPL-2.0-or-later
Group:          System/Fhs
Requires:       tukit = %{version}-%{release}
BuildArch:      noarch

%description -n tukit-snapper-plugin
This package contains the snapper plugin for creating /etc subvolumes on a
read-only system.

%package -n %{libname}
Summary:        Library for doing transactional updates using Btrfs snapshots
License:        GPL-2.0-or-later OR LGPL-2.1-or-later
Group:          System/Libraries
Requires:       btrfsprogs
Requires:       rsync
Requires:       snapper >= 0.8.10

%description -n %{libname}
This package contains the libraries required for programs to do
transactional updates using btrfs snapshots.

%package -n tukitd
Summary:        D-Bus controlling service for transactional updates
License:        GPL-2.0-or-later
Group:          System/Libraries
Requires:       %{libname} = %{version}-%{release}
Requires:       dbus-service

%description -n tukitd
This package provedes the D-Bus service to access %{libname}'s
functionality to manage transactional systems.

%package -n %{devname}
Summary:        Development files for tukit library
License:        GPL-2.0-or-later OR LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Provides:       tukit-devel = %{version}-%{release}
Provides:       tukit-devel = %{version}-%{release}
Requires:       %{libname} = %{version}-%{release}

%description -n %{devname}
This package contains the files required to develop programs to do
transactional updates using btrfs snapshots.

%package zypp-config
Summary:        Zypper rule to prevent uninstallation of transactional-update
Group:          System/Base
BuildArch:      noarch
Requires:       transactional-update = %{version}-%{release}

%description zypp-config
Adds a zypper rule to prevent accidental uninstallation of
transactional-update.

%prep
%autosetup -p1

%build
%if %{?suse_version} <= 1500
export CXX=g++-10
%endif
autoreconf -fiv
%configure --with-doc --docdir=%{_docdir}/%{name} --disable-static
%make_build

# Use "up" for non-rolling releases
%if (%{defined sle_version} && %{undefined is_susecasp}) || 0%{?suse_version} == 1600
sed -i 's/^UPDATE_METHOD=.*/UPDATE_METHOD=up/' etc/transactional-update.conf
%endif

# Enable soft-reboot by default
sed -i 's/^REBOOT_ALLOW_SOFT_REBOOT=.*/REBOOT_ALLOW_SOFT_REBOOT=false/' etc/tukit.conf

%install
%make_install

%fdupes %{buildroot}%{_mandir}

# Install zypp config files
mkdir -p %{buildroot}%{_sysconfdir}/zypp/systemCheck.d/
install -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/zypp/systemCheck.d/

# Delete libtool cruft
rm -rf %{buildroot}%{_libdir}/*.la

# Delete unwanted HTML documentation
rm -rf %{buildroot}%{_docdir}/%{name}/*.html

# move logrotate files from /etc/logrotate.d to /usr/etc/logrotate.d
%if 0%{?suse_version} > 1500
mkdir -p %{buildroot}%{_distconfdir}/logrotate.d
mv %{buildroot}/%{_sysconfdir}/logrotate.d/transactional-update %{buildroot}%{_distconfdir}/logrotate.d
%endif

%pre
%systemd_pre %{name}.service %{name}.timer
%systemd_pre %{name}-cleanup.service %{name}-cleanup.timer
%if 0%{?suse_version} > 1500
# Prepare for migration of logrotate configuration to /usr/etc; save any old .rpmsave
for i in logrotate.d/transactional-update ; do
   test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i}.rpmsave.old ||:
done
%endif

%post
%systemd_post %{name}.service %{name}.timer
%systemd_post %{name}-cleanup.service %{name}-cleanup.timer

%if 0%{?suse_version} > 1500
%posttrans
# Migration of logrotate configuration to /usr/etc, restore just created .rpmsave
for i in logrotate.d/transactional-update ; do
   test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i} ||:
done
%endif

%preun
%systemd_preun %{name}.service %{name}.timer
%systemd_preun %{name}-cleanup.service %{name}-cleanup.timer

%postun
%systemd_postun_with_restart %{name}.service %{name}.timer
%systemd_postun_with_restart %{name}-cleanup.service %{name}-cleanup.timer

%pre -n tukit
%systemd_pre create-dirs-from-rpmdb.service
%systemd_pre prepare-nextroot-for-softreboot.service

%post -n tukit
%systemd_post create-dirs-from-rpmdb.service
%systemd_post prepare-nextroot-for-softreboot.service

%preun -n tukit
%systemd_preun create-dirs-from-rpmdb.service
%systemd_preun prepare-nextroot-for-softreboot.service

%postun -n tukit
%systemd_postun_with_restart create-dirs-from-rpmdb.service
%systemd_postun_with_restart prepare-nextroot-for-softreboot.service

%pre -n tukitd
%systemd_pre tukitd.service

%post -n tukitd
%systemd_post tukitd.service

%preun -n tukitd
%systemd_preun tukitd.service

%postun -n tukitd
%systemd_postun_with_restart tukitd.service

%post -n dracut-%{name}
%regenerate_initrd_post

%posttrans -n dracut-%{name}
%regenerate_initrd_posttrans

%postun -n dracut-%{name}
%regenerate_initrd_post

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files
%license COPYING gpl-2.0.txt
%doc NEWS
%doc %{_docdir}/%{name}/transactional-update.txt
%if 0%{?suse_version} > 1500
%{_distconfdir}/logrotate.d/transactional-update
%else
%config(noreplace) %{_sysconfdir}/logrotate.d/transactional-update
%endif
%{_unitdir}/transactional-update.service
%{_unitdir}/transactional-update.timer
%{_unitdir}/transactional-update-cleanup.service
%{_unitdir}/transactional-update-cleanup.timer
%{_sbindir}/transactional-update
%{_distconfdir}/transactional-update.conf
%{_mandir}/man5/transactional-update.conf.5*
%{_mandir}/man8/transactional-update.8*
%{_mandir}/man8/transactional-update.timer.8*
%{_mandir}/man8/transactional-update.service.8*
%ghost %attr(0644,root,root) %{_localstatedir}/log/transactional-update.log

%files -n tukit
%license COPYING gpl-2.0.txt
%doc README.md NEWS
%{_sbindir}/tukit
%{_sbindir}/create_dirs_from_rpmdb
%{_unitdir}/create-dirs-from-rpmdb.service
%{_libexecdir}/prepare-nextroot-for-softreboot
%{_unitdir}/prepare-nextroot-for-softreboot.service
%{_distconfdir}/tukit.conf
%{_mandir}/man5/tukit.conf.5.gz

%files -n dracut-%{name}
%license COPYING gpl-2.0.txt
%doc README.md NEWS
%dir %{_prefix}/lib/dracut
%dir %{_prefix}/lib/dracut/modules.d
%{_prefix}/lib/dracut/modules.d/50transactional-update/
%{_libexecdir}/transactional-update-sync-etc-state

%files -n tukit-snapper-plugin
%license COPYING gpl-2.0.txt
%dir %{_prefix}/lib/snapper
%dir %{_prefix}/lib/snapper/plugins
%{_prefix}/lib/snapper/plugins/50-etc

%files -n %{libname}
%license COPYING gpl-2.0.txt lgpl-2.1.txt
%{_libdir}/libtukit.so.%{somajor}{,.*}

%files -n tukitd
%license COPYING gpl-2.0.txt
%{_sbindir}/tukitd
%{_unitdir}/tukitd.service
%{_prefix}/share/dbus-1/system-services/org.opensuse.tukit.service
%{_prefix}/share/dbus-1/system.d/org.opensuse.tukit.conf
%{_prefix}/share/dbus-1/interfaces/org.opensuse.tukit.Snapshot.xml
%{_prefix}/share/dbus-1/interfaces/org.opensuse.tukit.Transaction.xml

%files -n %{devname}
%license COPYING gpl-2.0.txt lgpl-2.1.txt
%{_includedir}/tukit/
%{_libdir}/libtukit.so
%{_libdir}/pkgconfig/tukit.pc

%files zypp-config
%config(noreplace) %{_sysconfdir}/zypp/systemCheck.d/transactional-update.check

%check

%changelog
