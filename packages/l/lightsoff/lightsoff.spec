#
# spec file for package lightsoff
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


Name:           lightsoff
Version:        48.1
Release:        0
Summary:        Lights Out Game for GNOME
License:        GPL-2.0-or-later
Group:          Amusements/Games/Board/Other
URL:            https://wiki.gnome.org/Apps/Lightsoff
Source0:        %{name}-%{version}.tar.zst
BuildSystem:    meson

BuildRequires:  AppStream
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  vala >= 0.22.0
Obsoletes:      %{name}-doc <= 3.28.0

%description
Lights Out is a board game where the goal is to switch off all tiles.
Toggling the status of one tile, will also toggle the status of its
adjacent tiles.

%lang_package

%generate_buildrequires
%meson_buildrequires

%install -a

%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}%{_datadir}

%files
%license COPYING
%doc NEWS
%doc %{_datadir}/help/C/%{name}/
%{_bindir}/%{name}
%{_datadir}/applications/org.gnome.LightsOff.desktop
%{_datadir}/dbus-1/services/org.gnome.LightsOff.service
%{_datadir}/glib-2.0/schemas/org.gnome.LightsOff.gschema.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.LightsOff*
%{_datadir}/metainfo/org.gnome.LightsOff.metainfo.xml
%{_mandir}/man6/lightsoff.6%{?ext_man}

%files lang -f %{name}.lang

%changelog
