#
# spec file for package lutris
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


%global appid net.lutris.Lutris
Name:           lutris
Version:        0.5.4
Release:        0
Summary:        Manager for game installation and execution
License:        GPL-3.0-or-later
URL:            https://lutris.net
Source0:        https://lutris.net/releases/lutris_%{version}.tar.xz
# boo#1161650: Remove xboxdrv and polkit
Patch0:         lutris-0.5.4-boo1161650-remove-polkit.patch
BuildRequires:  fdupes
BuildRequires:  gobject-introspection
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  python3-gobject
BuildRequires:  python3-setuptools
BuildRequires:  update-desktop-files
Requires:       cabextract
Requires:       fluid-soundfont-gm
Requires:       python3-Pillow
Requires:       python3-PyYAML
# controller support
Requires:       python3-evdev
Requires:       python3-gobject
Requires:       python3-gobject-Gdk
Requires:       python3-requests
#
Requires:       curl
Requires:       p7zip
Requires:       psmisc
Requires:       xrandr
Recommends:     winetricks
BuildArch:      noarch

%description
Lutris allows to gather and manage (install, configure and launch)
all games acquired from any source, in a single interface.
This includes, for example, Steam or Desura games, Windows games (WINE),
or emulated console games and browser games.

%prep
%setup -q -n %{name}
# boo#1161650
%patch0 -p1
rm -rf share/polkit-1/

%build
CFLAGS="%{optflags}" python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}
%suse_update_desktop_file -r -i %{appid} Network FileTransfer
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
%{_bindir}/lutris-wrapper
%{_datadir}/%{name}/
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/icons/hicolor/??x??/apps/%{name}.png
%{python3_sitelib}/%{name}-*.egg-info
%{python3_sitelib}/%{name}/
%dir %{_datadir}/metainfo/
%{_datadir}/metainfo/%{appid}.metainfo.xml

%changelog
