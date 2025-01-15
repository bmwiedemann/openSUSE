#
# spec file for package alacarte
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


Name:           alacarte
Version:        3.54.1
Release:        0
Summary:        Menu editor for GNOME
License:        LGPL-2.1-or-later
Group:          System/GUI/GNOME
URL:            https://gitlab.gnome.org/GNOME/alacarte
Source:         %{name}-%{version}.tar.zst

BuildRequires:  fdupes
BuildRequires:  gettext-devel
BuildRequires:  glib2-devel
BuildRequires:  libtool
# Needed for the typelib() dependency parser
BuildRequires:  gobject-introspection
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  python3 >= 3.3
BuildRequires:  suse-xsl-stylesheets
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(libgnome-menu-3.0) >= 3.5.3
BuildRequires:  pkgconfig(pygobject-3.0)
Requires:       python3-gobject-Gdk
BuildArch:      noarch

%description
Alacarte is a simple freedesktop.org compliant menu editor for GNOME
that lets you change your menus, simply and quickly. Just click and
type to edit, add, and delete any menu entry.

%lang_package

%prep
%autosetup -p1

%build
NOCONFIGURE=1 ./autogen.sh
%configure
%make_build

%install
%make_install
%suse_update_desktop_file -r alacarte GNOME Utility DesktopUtility X-GNOME-PersonalSettings
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}%{_prefix}

# If ChangeLog is empty, don't package it.
if test -s ChangeLog; then
    install -p -m 0644 -D ChangeLog \
      %{buildroot}%{_defaultdocdir}/Alacarte/ChangeLog
else
    rm -f ChangeLog
fi

%files
%license COPYING
%doc AUTHORS NEWS README.md
%{_bindir}/alacarte
%{_datadir}/alacarte
%{_datadir}/applications/alacarte.desktop
%{_datadir}/metainfo/org.gnome.alacarte.metainfo.xml
%{_datadir}/icons/hicolor/
%{python3_sitelib}/Alacarte
%{_mandir}/man1/alacarte.1%{?ext_man}

%files lang -f %{name}.lang

%changelog
