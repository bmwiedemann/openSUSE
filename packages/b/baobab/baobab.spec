#
# spec file for package baobab
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2011 Dominique Leuenberger, Amsterdam, The Netherlands
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


%define glib2_version 2.44

Name:           baobab
Version:        48.0
Release:        0
Summary:        Disk Usage Analyzer
License:        GPL-2.0-or-later
Group:          System/GUI/GNOME
URL:            https://wiki.gnome.org/Apps/DiskUsageAnalyzer
Source0:        %{name}-%{version}.tar.zst
# PATCH-FIX-UPSTREAM baobab-Improve-Scaning-Speed_cpu.patch -- Improve Scaning Speed and Memory Usage
Patch0:         baobab-Improve-Scaning-Speed_cpu.patch

BuildRequires:  appstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  meson >= 0.50.0
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.38.0.11
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(gio-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(glib-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(gobject-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(gtk4) >= 4.4.0
BuildRequires:  pkgconfig(libadwaita-1) >= 1.6.alpha

%description
Disk Usage Analyzer is a graphical, menu-driven application to analyse
disk usage in any GNOME environment. Disk Usage Analyzer can easily
scan either the whole filesystem tree, or a specific user-requested
directory branch (local or remote).

It also auto-detects in real-time any changes made to your home
directory as far as any mounted/unmounted device. Disk Usage Analyzer
also provides a full graphical treemap window for each selected folder.

%lang_package

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}%{_datadir}

%check
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/org.gnome.baobab.metainfo.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.gnome.baobab.desktop

%files
%license COPYING
%doc AUTHORS NEWS README.md
%doc %{_datadir}/help/C/%{name}/
%{_bindir}/%{name}
%{_datadir}/applications/org.gnome.%{name}.desktop
%{_datadir}/dbus-1/services/org.gnome.baobab.service
%{_datadir}/glib-2.0/schemas/org.gnome.baobab.gschema.xml
%{_datadir}/icons/hicolor/
%{_datadir}/metainfo/org.gnome.baobab.metainfo.xml
%{_mandir}/man1/%{name}.1%{?ext_man}

%files lang -f %{name}.lang

%changelog
