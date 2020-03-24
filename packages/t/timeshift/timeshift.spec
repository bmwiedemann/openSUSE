#
# spec file for package timeshift
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2017-2020 Malcolm J Lewis <malcolmlewis@opensuse.org>
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
Version:        20.03
Release:        0
Summary:        System restore utility
License:        GPL-3.0-only
URL:            https://teejeetech.in/timeshift/
Source0:        %{name}-%{version}.tar.xz
#PATCH-FIX-OPENSUSE timeshift-fix-timeshift-launcher.patch malcolmlewis@opensuse.org -- Fix `pkexec env` invocation in `timeshift-launcher` is wrong.
Patch0:         timeshift-fix-timeshift-launcher.patch
BuildRequires:  chrpath
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  vala
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(polkit-agent-1)
BuildRequires:  pkgconfig(vte-2.91)
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

%build
%make_build

%install
%make_install
#Cleanup rpath references
chrpath --delete %{buildroot}%{_bindir}/timeshift
chrpath --delete %{buildroot}%{_bindir}/timeshift-gtk
#Fix file permissions
chmod 0644 %{buildroot}%{_sysconfdir}/default/timeshift.json
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
%fdupes -s %{buildroot}

%files
%doc AUTHORS
%license LICENSE.md
%config(noreplace) %{_sysconfdir}/default/timeshift.json
%{_bindir}/timeshift*
%{_datadir}/applications/timeshift-gtk.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_mandir}/man1/timeshift.1%{?ext_man}
%{_datadir}/metainfo/timeshift.appdata.xml
%{_datadir}/polkit-1/actions/in.teejeetech.pkexec.timeshift.policy
%{_datadir}/timeshift/
%attr(0750,root,root) %dir %{_localstatedir}/log/timeshift
%attr(0750,root,root) %dir %{_localstatedir}/log/timeshift-btrfs

%files lang -f %{name}.lang

%changelog
