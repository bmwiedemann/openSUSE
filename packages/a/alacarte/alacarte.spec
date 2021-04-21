#
# spec file for package alacarte
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


Name:           alacarte
Version:        3.36.0
Release:        0
Summary:        Menu editor for GNOME
License:        LGPL-2.1-or-later
Group:          System/GUI/GNOME
URL:            https://gitlab.gnome.org/GNOME/alacarte
Source:         https://download.gnome.org/sources/alacarte/3.36/%{name}-%{version}.tar.xz
# PATCH-FIX-OPENSUSE alacarte-trans.patch bnc#947793 qzhao@suse.org -- Fix untranslated messages
Patch0:         alacarte-trans.patch
BuildRequires:  fdupes
BuildRequires:  glib2-devel
# Needed for the typelib() dependency parser
BuildRequires:  gobject-introspection
# Needed for %%icon_theme_cache_* macros.
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  python3 >= 3.2
BuildRequires:  suse-xsl-stylesheets
BuildRequires:  translation-update-upstream
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(libgnome-menu-3.0) >= 3.5.3
BuildRequires:  pkgconfig(pygobject-3.0)
Requires:       python3-gobject-Gdk

%description
Alacarte is a simple freedesktop.org compliant menu editor for GNOME
that lets you change your menus, simply and quickly. Just click and
type to edit, add, and delete any menu entry.

%lang_package

%prep
%setup -q
translation-update-upstream
%patch0 -p1

%build
%configure
make %{?_smp_mflags}

%install
%make_install
%suse_update_desktop_file -r alacarte GNOME Utility DesktopUtility X-GNOME-PersonalSettings
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/alacarte
%{_datadir}/alacarte
%{_datadir}/applications/alacarte.desktop
%{_datadir}/icons/hicolor/*/*/*.*
%{python3_sitelib}/Alacarte
%{_mandir}/man1/alacarte.1%{?ext_man}

%files lang -f %{name}.lang

%changelog
