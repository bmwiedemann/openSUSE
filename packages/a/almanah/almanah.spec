#
# spec file for package almanah
#
# Copyright (c) 2021 SUSE LLC
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


Name:           almanah
Version:        0.12.4
Release:        0
Summary:        GTK+ application to allow you to keep a diary of your life
License:        GPL-3.0+
Group:          Productivity/Office/Other
URL:            https://gitlab.gnome.org/GNOME/almanah
Source:         https://download.gnome.org/sources/almanah/0.12/%{name}-%{version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  gpgme-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  meson >= 0.51
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(atk)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(cryptui-0.0)
BuildRequires:  pkgconfig(gcr-4)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.5.6
BuildRequires:  pkgconfig(gtksourceview-4)
BuildRequires:  pkgconfig(gtkspell3-3.0)
BuildRequires:  pkgconfig(libecal-2.0)
BuildRequires:  pkgconfig(libedataserver-1.2)
BuildRequires:  pkgconfig(sqlite3)
Requires:       evolution-data-server

%description
Almanah Diary is a small application to ease the management of an encrypted
personal diary. It's got good editing abilities, including text formatting
and printing. Evolution tasks and appointments will be listed to ease the
creation of diary entries related to them. At the same time, you can create
diary entries using multiple events.

%lang_package

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name} %{?no_lang_C}

%check
%meson_test

%files
%license COPYING
%doc AUTHORS NEWS.md README.md
%{_bindir}/%{name}
%{_datadir}/glib-2.0/schemas/org.gnome.%{name}.gschema.xml
%{_datadir}/applications/org.gnome.Almanah.desktop
%{_datadir}/icons/hicolor/*/apps/org.gnome.Almanah.png
%{_datadir}/icons/hicolor/scalable/a*/org.gnome.Almanah-*.svg
%{_datadir}/metainfo/org.gnome.Almanah.metainfo.xml

%files lang -f %{name}.lang

%changelog
