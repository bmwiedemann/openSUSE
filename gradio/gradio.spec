#
# spec file for package gradio
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           gradio
Version:        7.2
Release:        0
Summary:        GTK3 app for finding and listening to internet radio stations
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/Sound/Players
Url:            https://github.com/haecker-felix/gradio
Source:         https://github.com/haecker-felix/gradio/archive/v%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  vala
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(vapigen) >= 0.16
Recommends:     %{name}-lang

%description
Gradio is a native GTK application. It lets you browse, search and find radio
stations, as well as listen to them, without needing to use a browser or enter
an internet radio stream URL. The application uses the Community Radio Browser
website for its database backend.

%lang_package

%prep
%setup -q -n Gradio-%{version}

%build
%{meson}
%{meson_build}

%install
%{meson_install}

%fdupes %{buildroot}%{_prefix}
%find_lang %{name}

%files
%license LICENSE.md
%doc README.md
%{_bindir}/gradio
%{_datadir}/appdata/de.haeckerfelix.gradio.appdata.xml
%{_datadir}/applications/de.haeckerfelix.gradio.desktop
%{_datadir}/icons/hicolor/*/apps/de.haeckerfelix.gradio.png
%{_datadir}/icons/hicolor/scalable/apps/de.haeckerfelix.gradio.svg
%{_datadir}/icons/hicolor/symbolic/apps/de.haeckerfelix.gradio-symbolic.svg
%{_datadir}/glib-2.0/schemas/de.haeckerfelix.gradio.gschema.xml
%{_datadir}/dbus-1/services/de.haeckerfelix.gradio.service
%dir %{_datadir}/gnome-shell/
%{_datadir}/gnome-shell/search-providers/

%files lang -f %{name}.lang

%changelog
