#
# spec file for package alacarte
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        3.11.91
Release:        0
Summary:        Menu editor for GNOME
License:        LGPL-2.1-or-later
Group:          System/GUI/GNOME
URL:            http://www.realistanew.com/projects/alacarte
Source:         http://download.gnome.org/sources/alacarte/3.11/%{name}-%{version}.tar.xz
# PATCH-FIX-OPENSUSE alacarte-trans.patch bnc#947793 qzhao@suse.org -- Fix untranslated messages
Patch0:         alacarte-trans.patch
# PATCH-FIX-UPSTREAM fix-bad-command-validation.patch bsc#1057908 bgo#728372 qzheng@suse.com -- Fix bad command validation
Patch1:         fix-bad-command-validation.patch
# PATCH-FIX-UPSTREAM alacarte-python3.patch bsc#1075771 bgo#787490 mgorse@suse.com -- Support python 3.
Patch2:         alacarte-python3.patch
# Needed for Patch2
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  glib2-devel
# Needed for the typelib() dependency parser
BuildRequires:  gobject-introspection
# Needed for %%icon_theme_cache_* macros.
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  suse-xsl-stylesheets
BuildRequires:  translation-update-upstream
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(libgnome-menu-3.0) >= 3.5.3
BuildRequires:  pkgconfig(pygobject-3.0)
Requires:       python3-gobject-Gdk
Recommends:     %{name}-lang

%description
Alacarte is a simple freedesktop.org compliant menu editor for GNOME
that lets you change your menus, simply and quickly. Just click and
type to edit, add, and delete any menu entry.

%lang_package

%prep
%setup -q
translation-update-upstream
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
# needed for Patch2
autoreconf -fi
%configure
make %{?_smp_mflags}

%install
%make_install
%suse_update_desktop_file -r alacarte GNOME Utility DesktopUtility X-GNOME-PersonalSettings
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}

%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun

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
