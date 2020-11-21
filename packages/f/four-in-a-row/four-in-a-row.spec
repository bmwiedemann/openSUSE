#
# spec file for package four-in-a-row
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


Name:           four-in-a-row
Version:        3.36.7
Release:        0
Summary:        Connect Four Game for GNOME
# License notice: Source code is GPL-2.0+, Icon themes are GPL-3.0+
License:        GPL-2.0-or-later AND GPL-3.0-or-later
Group:          Amusements/Games/Board/Other
URL:            https://wiki.gnome.org/Apps/Four-in-a-row
Source0:        https://download.gnome.org/sources/four-in-a-row/3.36/%{name}-%{version}.tar.xz

BuildRequires:  fdupes
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gsound) >= 1.0.2
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.23
BuildRequires:  pkgconfig(librsvg-2.0) >= 2.32.0

%description
The object of Four-in-a-Row is to place four pieces in a vertical,
horizontal, or diagonal row while the opponent tries to block and make
his/her own row of four. Four-in-a-Row can be played against another
human or the computer.

%lang_package

%prep
%autosetup -p1

%build
%meson \
	%{nil}
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}/%{_datadir}

%files
%license COPYING
%doc NEWS
%doc %{_datadir}/help/C/%{name}/
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/metainfo/org.gnome.Four-in-a-row.appdata.xml
%{_datadir}/applications/org.gnome.Four-in-a-row.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.Four-in-a-row.gschema.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.Four-in-a-row*
%{_mandir}/man6/%{name}.6%{?ext_man}
%{_datadir}/dbus-1/services/org.gnome.Four-in-a-row.service

%files lang -f %{name}.lang

%changelog
