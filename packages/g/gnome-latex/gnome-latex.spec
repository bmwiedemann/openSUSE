#
# spec file for package gnome-latex
#
# Copyright (c) 2023 SUSE LLC
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


Name:           gnome-latex
Version:        3.44.0
Release:        0
Summary:        Integrated LaTeX Environment for the GNOME desktop
License:        GPL-3.0-or-later
Group:          Productivity/Publishing/TeX/Frontends
URL:            https://wiki.gnome.org/Apps/GNOME-LaTeX
Source0:        https://download.gnome.org/sources/%{name}/3.44/%{name}-%{version}.tar.xz

BuildRequires:  fdupes
BuildRequires:  gsettings-desktop-schemas-devel
BuildRequires:  gtk-doc
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  itstool
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.34
BuildRequires:  pkgconfig(amtk-5) >= 5.6
BuildRequires:  pkgconfig(dconf)
BuildRequires:  pkgconfig(gee-0.8) >= 0.10
BuildRequires:  pkgconfig(gio-2.0) >= 2.56
BuildRequires:  pkgconfig(glib-2.0) >= 2.56
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 1.30.0
BuildRequires:  pkgconfig(gspell-1) >= 1.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
BuildRequires:  pkgconfig(gtksourceview-4) >= 3.99.7
BuildRequires:  pkgconfig(tepl-6) >= 6.4
BuildRequires:  pkgconfig(vapigen) >= 0.34
Requires:       gsettings-desktop-schemas
Requires:       texlive-latexmk-bin
Provides:       latexila = %{version}
Obsoletes:      latexila < %{version}

%description
Gnome-latex is an Integrated LaTeX Environment for GNOME. The main
features are:
  * Configurable buttons to compile, convert and view a document in
    one click.
  * LaTeX commands auto-completion.
  * Symbol tables (Greek letters, arrows, ...).
  * File browser integrated.
  * Template managing.
  * Menus with the most commonly used LaTeX commands.
  * Easy projects management.

%prep
%autosetup -p1

%build
autoreconf -fiv
%configure \
	--enable-gtk-doc \
	%{nil}
%make_build

%install
%make_install
%find_lang %{name}
%fdupes -s %{buildroot}%{_datadir}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS README NEWS HACKING
%{_bindir}/*
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/*/*/
%{_datadir}/applications/*
%{_datadir}/dbus-1/services/org.gnome.%{name}.service
%{_datadir}/glib-2.0/schemas/org.gnome.%{name}.gschema.xml
%{_datadir}/metainfo/org.gnome.%{name}.appdata.xml
%{_mandir}/man1/%{name}.1%{?ext_man}
%dir %{_datadir}/gtk-doc/html
%dir %{_datadir}/gtk-doc/html/%{name}
%doc %{_datadir}/gtk-doc/html/%{name}

%changelog
