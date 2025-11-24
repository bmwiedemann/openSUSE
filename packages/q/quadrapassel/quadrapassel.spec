#
# spec file for package quadrapassel
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


Name:           quadrapassel
Version:        49.2.1
Release:        0
Summary:        Tetris Game for GNOME
License:        GPL-2.0-or-later
Group:          Amusements/Games/Action/Other
URL:            https://live.gnome.org/Quadrapassel
Source0:        %{name}-%{version}.tar.zst
BuildSystem:    meson

BuildRequires:  blueprint-compiler
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  vala >= 0.24.0
BuildRequires:  rpm_macro(meson_buildrequires)

%description
Quadrapassel is a version of Tetris, the classic game of interlocking
four-piece blocks. As they fall from the top, the player must orient
them to fit the other blocks at the bottom so that they form a
complete horizontal line, in which case that line disappears and the
player gains points

%lang_package

%generate_buildrequires
%meson_buildrequires

%install -a
%find_lang %{name} %{?no_lang_C}
%find_lang %{name}_libgnome-games-support %{?no_lang_C}
%fdupes %{buildroot}%{_datadir}

%files
%license COPYING
%doc NEWS
%{_bindir}/%{name}
%{_datadir}/metainfo/org.gnome.Quadrapassel.metainfo.xml
%{_datadir}/applications/org.gnome.Quadrapassel.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.Quadrapassel.gschema.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.Quadrapassel*
%{_mandir}/man6/%{name}.6%{?ext_man}
%{_datadir}/dbus-1/services/org.gnome.Quadrapassel.service
%dir %{_datadir}/sounds/quadrapassel
%{_datadir}/sounds/quadrapassel/gameover.ogg
%{_datadir}/sounds/quadrapassel/land.ogg
%{_datadir}/sounds/quadrapassel/lines1.ogg
%{_datadir}/sounds/quadrapassel/lines2.ogg
%{_datadir}/sounds/quadrapassel/lines3.ogg
%{_datadir}/sounds/quadrapassel/quadrapassel.ogg
%{_datadir}/sounds/quadrapassel/slide.ogg
%{_datadir}/sounds/quadrapassel/turn.ogg

%files lang -f %{name}.lang -f %{name}_libgnome-games-support.lang

%changelog
