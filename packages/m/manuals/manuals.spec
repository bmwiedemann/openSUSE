#
# spec file for package manuals
#
# Copyright (c) 2025 SUSE LLC
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


Name:           manuals
Version:        50.1
Release:        0
Summary:        Install, Browse, and Search developer documentation
License:        GPL-3.0-or-later
URL:            https://gitlab.gnome.org/GNOME/manuals
Source:         %{name}-%{version}.tar.xz
BuildSystem:    meson

#BuildRequires:  fdupes
BuildRequires:  desktop-file-utils
BuildRequires:  meson
BuildRequires:  rpm_macro(meson_buildrequires)

%description
Install, Browse, and Search developer documentation

Manuals is an extraction of the Documentation component of GNOME
Builder into a standalone application.

%lang_package

%generate_buildrequires
%meson_buildrequires

%install -a
%find_lang %{name} %{?no_lang_C}

%files
%license COPYING
%doc README.md
%{_bindir}/manuals
%{_datadir}/applications/org.gnome.Manuals.desktop
%{_datadir}/dbus-1/services/org.gnome.Manuals.service
%{_datadir}/glib-2.0/schemas/org.gnome.Manuals.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Manuals.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Manuals-symbolic.svg
%{_datadir}/metainfo/org.gnome.Manuals.metainfo.xml

%files lang -f %{name}.lang

%changelog

