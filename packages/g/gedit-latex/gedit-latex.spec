#
# spec file for package gedit-latex
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


Name:           gedit-latex
Version:        3.20.0
Release:        0
Summary:        GEdit Plugin for Editing LaTeX Documents
# Code itself is GPLv2+ as of 0.2, but upstream explicitly ships a GPLv3 COPYING file
License:        GPL-3.0-or-later
Group:          Productivity/Text/Editors
URL:            https://live.gnome.org/Gedit/LaTeXPlugin
Source0:        https://download.gnome.org/sources/gedit-latex/3.20/%{name}-%{version}.tar.xz

BuildRequires:  fdupes
# For directory ownership
BuildRequires:  gedit
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0) >= 2.26.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.0.0

%description
This plugin turns the gedit editor into a productive environment for
editing LaTeX documents and managing BibTeX bibliographies.

%package -n gedit-plugin-latex
Summary:        GEdit Plugin for Editing LaTeX Documents
Group:          Productivity/Text/Editors
Requires:       dbus-1-python3
Requires:       gedit
# For gvfs-open
Requires:       gvfs
Requires:       python3-gobject-Gdk
Requires:       rubber
# Nice, and needed to make lang package installable
Provides:       %{name} = %{version}
%glib2_gsettings_schema_requires

%description -n gedit-plugin-latex
This plugin turns the gedit editor into a productive environment for
editing LaTeX documents and managing BibTeX bibliographies.

%lang_package

%prep
%autosetup -p1

%build
%configure \
	--disable-static \
	%{nil}
%make_build

%install
%make_install
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}%{_libdir}
%fdupes %{buildroot}%{_datadir}

%files -n gedit-plugin-latex
%license COPYING
%doc AUTHORS NEWS README
%{_libdir}/gedit/plugins/latex/
%{_libdir}/gedit/plugins/latex.plugin
%{_datadir}/gedit/plugins/latex/
%{_datadir}/glib-2.0/schemas/org.gnome.gedit.plugins.latex.gschema.xml

%files lang -f %{name}.lang

%changelog
