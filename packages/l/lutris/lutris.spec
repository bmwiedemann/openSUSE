#
# spec file for package lutris
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


%global appid net.lutris.Lutris
Name:           lutris
Version:        0.5.12
Release:        0
Summary:        Manager for game installation and execution
License:        GPL-3.0-or-later
URL:            https://lutris.net
Source0:        https://lutris.net/releases/lutris_%{version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  gobject-introspection
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  python3-devel >= 3.7
BuildRequires:  python3-gobject
BuildRequires:  python3-setuptools
BuildRequires:  update-desktop-files
Requires:       cabextract
#
Requires:       curl
Requires:       fluid-soundfont-gm
Requires:       p7zip
Requires:       psmisc
Requires:       python3-Pillow
Requires:       python3-PyYAML
Requires:       python3-cssselect
Requires:       python3-dbus-python
# controller support
Requires:       python3-evdev
Requires:       python3-gobject
Requires:       python3-gobject-Gdk
Requires:       python3-lxml
Requires:       python3-magic
Requires:       python3-requests
Requires:       xrandr
Recommends:     python3-distro
Recommends:     winetricks
BuildArch:      noarch

%description
Lutris allows to gather and manage (install, configure and launch)
all games acquired from any source, in a single interface.
This includes, for example, Steam or GOG games, Windows games (WINE),
or emulated console games and browser games.

%prep
%setup -q -n %{name}
sed -i "s|!%{_bindir}/env python3|!%{_bindir}/python3|" share/lutris/bin/lutris-wrapper

%build
%py3_build

%install
%py3_install
%fdupes %{buildroot}%{_prefix}

%if 0%{?suse_version} < 1330
%post
%icon_theme_cache_post
%desktop_database_post

%postun
%icon_theme_cache_postun
%desktop_database_postun
%endif

%files
%doc README.rst CONTRIBUTING.md AUTHORS
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_datadir}/%{name}/
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/icons/hicolor/??x??/apps/%{name}.png
%{_datadir}/icons/hicolor/???x???/apps/%{name}.png
%{python3_sitelib}/%{name}-*.egg-info
%{python3_sitelib}/%{name}/
%dir %{_datadir}/metainfo/
%{_datadir}/metainfo/%{appid}.metainfo.xml

%changelog
