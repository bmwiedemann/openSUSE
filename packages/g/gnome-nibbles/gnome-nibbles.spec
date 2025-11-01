#
# spec file for package gnome-nibbles
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


Name:           gnome-nibbles
Version:        4.4.2
Release:        0
Summary:        Worm Game for GNOME
License:        GPL-3.0-or-later
Group:          Amusements/Games/Action/Arcade
URL:            https://gitlab.gnome.org/GNOME/gnome-nibbles/-/wikis/home
Source0:        %{name}-%{version}.tar.zst
BuildSystem:    meson

BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  gettext-devel
BuildRequires:  meson >= 0.50.1
BuildRequires:  vala
BuildRequires:  yelp-tools

%description
Nibbles is a worm game for GNOME. The player controls a 2D worm while
trying to get food. Getting food gives points, but hitting anything
causes a loss of points. When all points are lost, the player loses.

%lang_package

%generate_buildrequires
export BUILDREQ_IGNORE_DEP="gtk5"
%meson_buildrequires

%install -a
%fdupes %{buildroot}/%{_datadir}
%find_lang %{name} %{?no_lang_C}
%find_lang %{name}_libgnome-games-support %{?no_lang_C}

%files
%license COPYING
%doc NEWS
%doc %{_datadir}/help/C/%{name}/
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/org.gnome.Nibbles.desktop
%{_datadir}/dbus-1/services/org.gnome.Nibbles.service
%{_datadir}/glib-2.0/schemas/org.gnome.Nibbles.gschema.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.Nibbles*.*
%{_datadir}/metainfo/org.gnome.Nibbles.metainfo.xml
%{_mandir}/man6/%{name}.6%{?ext_man}

%files lang -f %{name}.lang -f %{name}_libgnome-games-support.lang

%changelog
