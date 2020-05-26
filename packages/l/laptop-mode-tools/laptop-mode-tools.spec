#
# spec file for package laptop-mode-tools
#
# Copyright (c) 2020 SUSE LLC
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


%{!?_tmpfilesdir:%global _tmpfilesdir /usr/lib/tmpfiles.d}
%{!?_udevdir:%global _udevdir  %{_libexecdir}/udev}

Name:           laptop-mode-tools
Version:        1.73.1
Release:        0
Summary:        The Laptop Mode Tools
License:        GPL-2.0-or-later
Group:          System/Base
URL:            http://rickysarraf.github.io/laptop-mode-tools/
Source:         https://github.com/rickysarraf/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        README.SUSE
Patch0:         laptop-mode-1.53_conf.diff
Patch1:         laptop-mode-1.49-new-dirty-ratio-defaults.diff
Patch2:         laptop-mode-1.53-moblin-enable-intel-hda-powersave.patch
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(udev)
Suggests:       %{name}-gui
BuildArch:      noarch
%{?systemd_requires}

%description
Laptop Mode Tools is a laptop power saving package for Linux systems.
It allows you to extend the battery life of your laptop, in several
ways. It is the primary way to enable the Laptop Mode feature of the
Linux kernel, which lets your hard drive spin down. In addition, it
allows you to tweak a number of other power-related settings using a
simple configuration file.

%package gui
Summary:        Graphical User Interface for the laptop mode tools
Group:          System/Base
BuildRequires:  update-desktop-files
Requires:       %{name} = %{version}
Requires:       python3-qt5
BuildArch:      noarch

%description gui
This package contains a graphical user interface for laptop-mode-tools.

%prep
%autosetup -p1
cp %{SOURCE1} .

%build

%install
DESTDIR=%{buildroot} \
MAN_D=%{_mandir} \
INIT_D="none" \
LIB_D=%{_libdir} \
UDEV_D=%{_udevdir} \
SYSTEMD_UNIT_D=%{_unitdir} \
ACPI=disabled PMU=disabled APM=disabled INSTALL=install ./install.sh

# Fix spurious executable permission
chmod 644 %{buildroot}/%{_mandir}/man8/*

# Fix suse-missing-rclink
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rclaptop-mode
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rclmt-poll

# remove pm-utils hook: as soon as DESTDIR is defined, the hook is always installed
rm -rf %{buildroot}%{_libexecdir}/pm-utils

# Fix insufficient category definition
%suse_update_desktop_file -r laptop-mode-tools Settings HardwareSettings

%pre
%service_add_pre laptop-mode.service lmt-poll.service

%post
%service_add_post laptop-mode.service lmt-poll.service
systemd-tmpfiles --create %{_tmpfilesdir}/laptop-mode.conf

%preun
%service_del_preun laptop-mode.service lmt-poll.service

%postun
%service_del_postun laptop-mode.service lmt-poll.service

%files
%doc README.SUSE
%license COPYING
%dir %{_sysconfdir}/laptop-mode
%config %{_sysconfdir}/laptop-mode/*
%{_sbindir}/*
%exclude %{_sbindir}/*gui*
%dir %{_datadir}/%{name}/
%dir %{_datadir}/%{name}/modules/
%dir %{_datadir}/%{name}/module-helpers/
%{_datadir}/%{name}/modules/*
%{_datadir}/%{name}/module-helpers/lm-polling-daemon
%{_datadir}/%{name}/module-helpers/pm-freeze
%{_datadir}/%{name}/module-helpers/pm-helper
%{_datadir}/%{name}/module-helpers/pm-hibernate
%{_datadir}/%{name}/module-helpers/pm-suspend
%{_udevdir}/lmt-udev
%{_udevrulesdir}/99-laptop-mode.rules
%{_mandir}/man8/*
%{_tmpfilesdir}/laptop-mode.conf
%{_unitdir}/laptop-mode.service
%{_unitdir}/laptop-mode.timer
%{_unitdir}/lmt-poll.service

%files gui
%license COPYING
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.svg
%dir %{_datadir}/polkit-1
%dir %{_datadir}/polkit-1/actions
%{_datadir}/polkit-1/actions/org.linux.lmt.gui.policy
%{_datadir}/%{name}/lmt.py
%{_sbindir}/*gui*

%changelog
