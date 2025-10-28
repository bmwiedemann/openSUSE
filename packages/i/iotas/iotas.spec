#
# spec file for package iotas
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


Name:           iotas
Version:        0.12.1
Release:        0
Summary:        Distraction-free note taking app with optional cloud sync
License:        GPL-3.0-or-later
URL:            https://apps.gnome.org/Iotas/
Source:         https://gitlab.gnome.org/World/iotas/-/archive/%{version}/%{name}-%{version}.tar.bz2
# PATCH-FIX-UPSTREAM iotas-optional-pypandoc.patch glgo#World/iotas#291 badshah400@gmail.com -- Make pypandoc optional so that app does not crash when it is unavailable on system
Patch0:         iotas-optional-pypandoc.patch
BuildRequires:  desktop-file-utils
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson
BuildRequires:  python3
BuildRequires:  pkgconfig(gio-2.0) >= 2.76
BuildRequires:  pkgconfig(glib-2.0) >= 2.76
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 1.66.0
BuildRequires:  pkgconfig(gtk4) >= 4.20
BuildRequires:  pkgconfig(gtksourceview-5) >= 5.6
BuildRequires:  pkgconfig(libadwaita-1) >= 1.8
Requires:       python3-gobject-Gdk
Requires:       python3-linkify-it-py
Requires:       python3-packaging
Requires:       python3-pygtkspellcheck
Requires:       python3-urllib3
Requires:       python3-markdown-it-py
Recommends:     python3-requests
Suggests:       python3-mdit-py-plugins
Suggests:       python3-pypandoc
BuildArch:      noarch

%description
Iotas is a simple note taking with mobile-first design and optional speedy
Nextcloud Notes sync.

%package -n gnome-shell-search-provider-%{name}
Summary:        Note taking app -- Search Provider for GNOME Shell
BuildArch:      noarch
Requires:       %{name} = %{version}
Requires:       gnome-shell
Supplements:    (%{name} and gnome-shell)

%description -n gnome-shell-search-provider-%{name}
Iotas is a simple note taking with mobile-first design and optional speedy
Nextcloud Notes sync.

This package provides a search provider for gnome-shell to show notes in iotas
with matching titles.

%lang_package

%prep
%autosetup -p1

# Not installed to PATH, drop unnecessary hashbang
sed -Ei "1{/^#\!@PYTHON@/d}" iotas/const.py.in

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}

# Remove build files from installed dirs
rm %{buildroot}%{python3_sitelib}/markdown_it_*/meson.*

%files
%license LICENSE
%doc README.md
%{_bindir}/iotas
%{_datadir}/applications/org.gnome.World.Iotas.desktop
%{_datadir}/dbus-1/services/org.gnome.World.Iotas.service
%{_datadir}/glib-2.0/schemas/org.gnome.World.Iotas.gschema.xml
%{_datadir}/gtksourceview-5/language-specs/iotas-markdown.lang
%{_datadir}/gtksourceview-5/styles/iotas-*.xml
%{_datadir}/icons/hicolor/*/apps/*.svg
%{_datadir}/iotas/
%{_datadir}/metainfo/org.gnome.World.Iotas.metainfo.xml
%{_libexecdir}/iotas-search-provider
%{python3_sitelib}/iotas/
%{python3_sitelib}/markdown_it_img_figures_plugin/
%{python3_sitelib}/markdown_it_modified_tasklists_plugin/

%files -n gnome-shell-search-provider-%{name}
%license LICENSE
%{_datadir}/dbus-1/services/org.gnome.World.Iotas.SearchProvider.service
%dir %{_datadir}/gnome-shell
%dir %{_datadir}/gnome-shell/search-providers
%{_datadir}/gnome-shell/search-providers/org.gnome.World.Iotas.SearchProvider.ini

%files lang -f %{name}.lang

%changelog
