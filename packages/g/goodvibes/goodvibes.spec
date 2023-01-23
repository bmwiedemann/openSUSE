#
# spec file for package goodvibes
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


Name:           goodvibes
Version:        0.7.6
Release:        0
Summary:        A lightweight radio player
License:        GPL-3.0-only
Group:          Productivity/Multimedia/Sound/Players
URL:            https://gitlab.com/goodvibes/goodvibes
Source:         https://gitlab.com/goodvibes/goodvibes/-/archive/v%{version}/%{name}-v%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  gettext >= 0.19.7
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson >= 0.49
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(amtk-5)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.44
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-audio-1.0) >= 1.4.4
BuildRequires:  pkgconfig(gstreamer-base-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(keybinder-3.0)
BuildRequires:  pkgconfig(libsoup-2.4) >= 2.42
Recommends:     gstreamer-plugins-bad
Recommends:     gstreamer-plugins-base
Recommends:     gstreamer-plugins-good
Recommends:     gstreamer-plugins-ugly

%description
A lightweight radio player written in C and GTK+. It offers a simple way
to have your favorite radio stations at easy reach.

%lang_package

%prep
%setup -q -n %{name}-v%{version}

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name}
%fdupes %{buildroot}%{_datadir}

%files
%license COPYING
%doc NEWS README.md
%{_bindir}/goodvibes
%{_bindir}/goodvibes-client
%{_datadir}/applications/io.gitlab.Goodvibes.desktop
%{_datadir}/dbus-1/services/io.gitlab.Goodvibes.service
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/icons/hicolor/*/apps/io.gitlab.Goodvibes*.??g
%{_datadir}/metainfo/io.gitlab.Goodvibes.appdata.xml
%{_mandir}/man?/*.?%{ext_info}

%files lang -f %{name}.lang

%changelog
