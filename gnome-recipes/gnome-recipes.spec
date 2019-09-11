#
# spec file for package gnome-recipes
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           gnome-recipes
Version:        2.0.2
Release:        0
Summary:        A recipe app for GNOME
License:        GPL-3.0-or-later
Group:          Productivity/Other
URL:            https://wiki.gnome.org/Design/Apps/Recipes
Source0:        http://download.gnome.org/sources/gnome-recipes/2.0/%{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM gnome-recipes-nb-translations.patch bjorn.lie@gmail.com -- Update Norwegian Bokmål translations
Patch0:         gnome-recipes-nb-translations.patch
BuildRequires:  appstream-glib
BuildRequires:  fdupes
BuildRequires:  glib2-devel >= 2.42
BuildRequires:  gobject-introspection-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  itstool
BuildRequires:  libxml2-tools
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  vala-devel
BuildRequires:  pkgconfig(gnome-autoar-0)
BuildRequires:  pkgconfig(goa-1.0)
BuildRequires:  pkgconfig(gspell-1)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.20
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(rest-0.7)
Recommends:     %{name}-lang = %{version}

%description
GNOME Recipes is an easy-to-use application that will help you to discover what to cook
today, tomorrow, rest of the week and for your special occasions.

Recipes comes with a collection of recipes that have been collected by GNOME contributors
from all over the world. It also lets you store your own recipes, and share them with your
friends.

%package -n gnome-shell-search-provider-%{name}
Summary:        A recipe app for GNOME -- Search Provider for GNOME Shell
Group:          Productivity/Office/Organizers
Requires:       %{name} = %{version}
Requires:       gnome-shell
Supplements:    packageand(%{name}:gnome-shell)

%description -n gnome-shell-search-provider-%{name}
GNOME Recipes is an easy-to-use application that will help you to discover what to cook
today, tomorrow, rest of the week and for your special occasions.

Recipes comes with a collection of recipes that have been collected by GNOME contributors
from all over the world. It also lets you store your own recipes, and share them with your
friends.

This package contains a search provider to enable GNOME Shell to get
search results from Recipes.

%lang_package

%prep
%autosetup -p1

%build
%meson \
	-D autoar=yes \
	-D gspell=yes \
	-D canberra=yes \
	%{nil}
%meson_build

%install
%meson_install
%suse_update_desktop_file -r org.gnome.Recipes GTK GNOME Office ProjectManagement
%fdupes %{buildroot}%{_datadir}
%find_lang %{name} %{?no_lang_C}
%find_lang org.gnome.Recipes %{?no_lang_C}
%find_lang %{name}-data %{?no_lang_C}

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/dbus-1/services/org.gnome.Recipes.service
%{_datadir}/appdata/org.gnome.Recipes.appdata.xml
%{_datadir}/glib-2.0/schemas/org.gnome.Recipes.gschema.xml
%{_datadir}/mime/packages/org.gnome.Recipes-mime.xml
%{_datadir}/%{name}
%{_datadir}/help/C/org.gnome.Recipes/

%files -n gnome-shell-search-provider-%{name}
%dir %{_datadir}/gnome-shell
%dir %{_datadir}/gnome-shell/search-providers
%{_datadir}/gnome-shell/search-providers/org.gnome.Recipes-search-provider.ini

%files lang -f %{name}.lang -f %{name}-data.lang -f org.gnome.Recipes.lang

%changelog
