#
# spec file for package timeshift
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2017-2024 Malcolm J Lewis <malcolmlewis@opensuse.org>
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


Name:           timeshift
Version:        24.06.1
Release:        0
Summary:        System restore utility
License:        GPL-3.0-only
URL:            https://github.com/linuxmint/timeshift
Source0:        https://codeload.github.com/linuxmint/timeshift/tar.gz/refs/tags/%{version}#/%{name}-%{version}.tar.gz
BuildRequires:  chrpath
BuildRequires:  fdupes
BuildRequires:  help2man
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  vala
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(polkit-agent-1)
BuildRequires:  pkgconfig(vte-2.91)
BuildRequires:  pkgconfig(xapp)
Requires:       rsync
#Lets just recommend for btrfs as more likely used with other filesystems
Recommends:     btrfsprogs

%description
A system restore utility which takes snapshots of the system at regular
intervals. These snapshots can be restored at a later date to undo system
changes. Creates incremental snapshots using rsync or BTRFS snapshots
using BTRFS tools.

%lang_package

%prep
%autosetup -p1
# rpmlint
sed -i -e 's|/usr/bin/env bash|/usr/bin/bash|g' src/timeshift-launcher

%build
%meson -Dxapp=false
%meson_build

%install
%meson_install
#Cleanup rpath references
chrpath --delete %{buildroot}%{_bindir}/timeshift
chrpath --delete %{buildroot}%{_bindir}/timeshift-gtk
#Fix file permissions
chmod 0644 %{buildroot}%{_sysconfdir}/timeshift/default.json
chmod 0644 %{buildroot}%{_datadir}/metainfo/timeshift.appdata.xml
chmod 0644 %{buildroot}%{_datadir}/timeshift/images/*.svg
#Remove as we use rpm/zypper
rm -f %{buildroot}%{_bindir}/timeshift-uninstall
#Remove appdata in preference to metadinfo
rm -rf %{buildroot}%{_datadir}/appdata
#Manually add log directories, set mode to 0750 and owned by root (boo#1165805)
install -d %{buildroot}%{_localstatedir}/log/timeshift
install -d %{buildroot}%{_localstatedir}/log/timeshift-btrfs
%suse_update_desktop_file -r timeshift-gtk Utility Archiving
%find_lang %{name} %{?no_lang_C}

%fdupes %{buildroot}%{_datadir}

%files
%license LICENSES/*
%dir %{_sysconfdir}/timeshift
%config(noreplace) %{_sysconfdir}/timeshift/default.json
%{_bindir}/timeshift*
%{_datadir}/applications/timeshift-gtk.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_mandir}/man1/timeshift.1%{?ext_man}
%{_mandir}/man1/timeshift-gtk.1%{?ext_man}
%{_datadir}/metainfo/timeshift.appdata.xml
%{_datadir}/polkit-1/actions/in.teejeetech.pkexec.timeshift.policy
%{_datadir}/pixmaps/timeshift.png
%{_datadir}/timeshift/
%attr(0750,root,root) %dir %{_localstatedir}/log/timeshift
%attr(0750,root,root) %dir %{_localstatedir}/log/timeshift-btrfs

%files lang -f %{name}.lang

%changelog
