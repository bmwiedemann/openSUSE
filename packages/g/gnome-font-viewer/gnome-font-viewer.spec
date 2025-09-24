#
# spec file for package gnome-font-viewer
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


Name:           gnome-font-viewer
Version:        49.0
Release:        0
Summary:        A font viewer utility for GNOME
License:        GPL-2.0-or-later
Group:          System/GUI/GNOME
URL:            https://gitlab.gnome.org/GNOME/gnome-font-viewer
Source0:        %{name}-%{version}.tar.zst
BuildSystem:    meson
BuildRequires:  meson >= 0.50.0
Conflicts:      gnome-utils < 3.3.1

%description
A utility to let you see the installed fonts at a glance.

%lang_package

%generate_buildrequires
%meson_buildrequires

%install -a
%meson_install
%find_lang %{name}

%files
%license COPYING
%doc NEWS
%{_bindir}/%{name}
%{_bindir}/gnome-thumbnail-font
%{_datadir}/applications/org.gnome.font-viewer.desktop
%{_datadir}/dbus-1/services/org.gnome.font-viewer.service
%dir %{_datadir}/thumbnailers
%{_datadir}/thumbnailers/%{name}.thumbnailer
%{_datadir}/metainfo/org.gnome.font-viewer.appdata.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.font-viewer*.svg

%files lang -f %{name}.lang

%changelog
