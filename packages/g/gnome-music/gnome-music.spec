#
# spec file for package gnome-music
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


Name:           gnome-music
Version:        48.0
Release:        0
Summary:        Music Player for GNOME
License:        LGPL-2.1-or-later AND SUSE-GPL-2.0-with-plugin-exception
Group:          Productivity/Multimedia/Sound/Players
URL:            https://www.gnome.org
Source0:        %{name}-%{version}.tar.zst

BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  pkgconfig
%if 0%{?sle_version}
BuildRequires:  python3-devel >= 3.6
%else
BuildRequires:  python3-devel >= 3.7
%endif
BuildRequires:  pkgconfig(glib-2.0) >= 2.67.1
BuildRequires:  pkgconfig(goa-1.0) >= 3.35.90
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 1.35.0
BuildRequires:  pkgconfig(grilo-0.3) >= 0.3.13
BuildRequires:  pkgconfig(grilo-plugins-0.3) >= 0.3.12
BuildRequires:  pkgconfig(gtk4) >= 4.10.0
BuildRequires:  pkgconfig(libadwaita-1) >= 1.5.beta
BuildRequires:  pkgconfig(libmediaart-2.0) >= 1.9.1
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(pango) >= 1.44.0
BuildRequires:  pkgconfig(py3cairo) >= 1.14
BuildRequires:  pkgconfig(pygobject-3.0) >= 3.47.0
BuildRequires:  pkgconfig(tracker-sparql-3.0) >= 2.99.3
Requires:       dbus-1-python3
# gnome-music requires grilo-plugin-tracker to interact with tracker and find files (bsc#1083659)
Requires:       grilo-plugin-tracker
# gnomemusic/albumArtCache.py imports cairo directly.
Requires:       python3-cairo >= 1.14
# This is a python 3 application
Requires:       python3-gobject
# ... a python3 GUI application
Requires:       python3-gobject-Gdk
# gnomemusic/player.py imports requests (not introspected)
Requires:       python3-requests
# gnome-music relies on tracker to find local files (bsc#1084861)
Requires:       localsearch
# The versioned format depenency is written in a form not understood by our gi-scanner
Requires:       typelib(Tracker) = 3.0
Requires:       typelib(GstTag) = 1.0
Recommends:     gstreamer-plugins-base
Recommends:     gstreamer-plugins-good
BuildArch:      noarch

%description
Music player and management application for GNOME.

%lang_package

%prep
%autosetup -p1

%build
%meson
%meson_build

%check
%meson_test

%install
%meson_install
# Explicitly create the pycache/.pyc files, not relying on the
# generation done by meson. Should make the package reproducible.
%py3_compile %{buildroot}%{python3_sitelib}/gnomemusic
%find_lang %{name} %{?no_lang_C}
%find_lang org.gnome.Music %{?no_lang_C} %{name}.lang
%fdupes %{buildroot}%{python3_sitelib}/gnomemusic
%fdupes %{buildroot}%{_datadir}/
%python3_fix_shebang

%files
%license LICENSE
%doc %{_datadir}/help/C/%{name}/
%{_bindir}/gnome-music
%{_datadir}/applications/org.gnome.Music.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.Music.gschema.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.Music*
%{_datadir}/metainfo/org.gnome.Music.metainfo.xml
%{_datadir}/org.gnome.Music/
%{python3_sitelib}/gnomemusic/

%files lang -f %{name}.lang

%changelog
