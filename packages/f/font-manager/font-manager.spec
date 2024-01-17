#
# spec file for package font-manager
#
# Copyright (c) 2022 SUSE LLC
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


%global DBusName org.gnome.FontManager
%global DBusName2 org.gnome.FontViewer
Name:           font-manager
Version:        0.8.8
Release:        0
Summary:        A simple font management application for Gtk+ Desktop Environments
License:        GPL-3.0-or-later
URL:            https://fontmanager.github.io
Source0:        https://github.com/FontManager/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
BuildRequires:  appstream-glib
BuildRequires:  gettext-runtime
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  vala >= 0.42
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(glib-2.0) >= 2.44
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
BuildRequires:  pkgconfig(json-glib-1.0)
# Disable nautilus until font-manager is ported to gtk4
#BuildRequires:  pkgconfig(libnautilus-extension)
BuildRequires:  pkgconfig(libnemo-extension)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(thunarx-3)
BuildRequires:  pkgconfig(webkit2gtk-4.0) >= 2.13.90
Requires:       %{name}-common
Requires:       font-viewer
Requires:       fontconfig
Requires:       webkit2gtk-4_0-injected-bundles
Obsoletes:      nautilus-%{name} <= %{version}

%description
Font Manager is intended to provide a way for average users to easily
 manage desktop fonts, without having to resort to command line tools
 or editing configuration files by hand. While designed primarily with
 the Gnome Desktop Environment in mind, it should work well with other
 Gtk+ desktop environments.

Font Manager is NOT a professional-grade font management solution.

%lang_package

%package -n %{name}-common
Summary:        Common files used by font-manager

%description -n %{name}-common
This package contains common files such as libraries.
 These files are required by font-manager and font-viewer.

%package -n font-viewer
Summary:        Full featured font file preview application for GTK+ Desktop Environments
Requires:       %{name}-common >= %{version}

%description -n font-viewer
This package contains the font-viewer component of font-manager.

%package -n nautilus-%{name}
Summary:        Nautilus extension for Font Manager
Requires:       %{name}-common >= %{version}
Requires:       font-viewer >= %{version}

%description -n nautilus-%{name}
This package provides integration with the Nautilus file manager.

%package -n nemo-%{name}
Summary:        Nemo extension for Font Manager
Requires:       %{name}-common >= %{version}
Requires:       font-viewer >= %{version}

%description -n nemo-%{name}
This package provides integration with the Nemo file manager.

%package -n thunar-%{name}
Summary:        Thunar extension for Font Manager
Requires:       %{name}-common >= %{version}
Requires:       font-viewer >= %{version}

%description -n thunar-%{name}
This package provides integration with the Thunar file manager.

%prep
%autosetup

%build
%meson \
  --buildtype=release \
  -Dnautilus=false \
  -Dnemo=True \
  -Dthunar=true \
  -Dreproducible=true
%meson_build

%install
%meson_install
rm %{buildroot}/%{_libdir}/%{name}/libfontmanager.so

%find_lang %{name}
%suse_update_desktop_file -r org.gnome.FontManager Graphics Viewer
%suse_update_desktop_file -r org.gnome.FontViewer Graphics Viewer

%check
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/*.appdata.xml

%posttrans
%{_bindir}/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :

%files
%{_bindir}/%{name}
%{_datadir}/metainfo/%{DBusName}.appdata.xml
%{_datadir}/applications/%{DBusName}.desktop
%{_datadir}/dbus-1/services/%{DBusName}.service
%{_datadir}/glib-2.0/schemas/%{DBusName}.gschema.xml
%dir %{_datadir}/gnome-shell
%dir %{_datadir}/gnome-shell/search-providers
%{_datadir}/gnome-shell/search-providers/%{DBusName}.SearchProvider.ini
%{_datadir}/icons/hicolor/128x128/apps/%{DBusName}.png
%{_datadir}/icons/hicolor/256x256/apps/%{DBusName}.png
%{_mandir}/man1/%{name}.*

%files -n %{name}-common
%license COPYING
%{_libdir}/%{name}

%files lang -f %{name}.lang

%files -n font-viewer
%{_libexecdir}/%{name}/
%{_datadir}/metainfo/%{DBusName2}.appdata.xml
%{_datadir}/applications/%{DBusName2}.desktop
%{_datadir}/dbus-1/services/%{DBusName2}.service
%{_datadir}/glib-2.0/schemas/%{DBusName2}.gschema.xml
%{_datadir}/icons/hicolor/128x128/apps/%{DBusName2}.png
%{_datadir}/icons/hicolor/256x256/apps/%{DBusName2}.png

#%%files -n nautilus-%%{name}
#%%{_libdir}/nautilus/extensions-3.0/nautilus-%%{name}.so

%files -n nemo-%{name}
%{_libdir}/nemo/extensions-3.0/nemo-%{name}.so

%files -n thunar-%{name}
%{_libdir}/thunarx-3/thunar-%{name}.so

%changelog
