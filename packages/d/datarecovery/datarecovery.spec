#
# spec file for package datarecovery
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           datarecovery
Version:        0.6.1
Release:        0
Summary:        GTK4/Libadwaita application for data recovery
License:        GPL-2.0-or-later
Group:          System/Filesystems
BuildArch:      noarch
URL:            https://github.com/koxt2/DataRecovery
Source0:        https://github.com/koxt2/DataRecovery/archive/refs/tags/v%version.tar.gz
Source1:        %name-rpmlintrc

BuildRequires:  desktop-file-utils
BuildRequires:  meson >= 1.0.0
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)

Requires:       dbus-1-common
Requires:       gnu_ddrescue
Requires:       hicolor-icon-theme
Requires:       photorec
Requires:       polkit
Requires:       python3
Requires:       python3-gobject
Requires:       rdfind
Requires:       udisks2
Requires:       typelib(Adw) = 1
Requires:       typelib(Gtk) = 4.0

%description
A GTK4/Libadwaita application for data recovery using ddrescue and
PhotoRec. Recovers all files (not just deleted ones) from storage
devices or disk images, organizes them by file type, and optionally
removes duplicates using rdfind.

%prep
%autosetup -p1 -n DataRecovery-%version

%build
%meson
%meson_build

%install
%meson_install

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/datarecovery.desktop

%files
%license LICENSE
%doc README.md
%{_bindir}/datarecovery
%{_bindir}/datarecovery-pkexec-helper
%{_datadir}/datarecovery/
%{_datadir}/applications/datarecovery.desktop
%{_datadir}/dbus-1/services/com.github.koxt2.datarecovery.service
%{_datadir}/icons/hicolor/*/apps/com.github.koxt2.datarecovery*.*
%{_datadir}/metainfo/com.github.koxt2.datarecovery.metainfo.xml
%{_datadir}/polkit-1/actions/datarecovery.policy

%changelog