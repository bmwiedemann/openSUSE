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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%global appid net.lutris.Lutris
Name:           lutris
Version:        0.5.2.2
Release:        0
Summary:        Manager for game installation and execution
License:        GPL-3.0-or-later
Group:          Amusements/Games/Other
URL:            http://lutris.net
Source0:        http://lutris.net/releases/lutris_%{version}.tar.xz
Source1:        lutris.rpmlintrc
BuildRequires:  fdupes
BuildRequires:  gobject-introspection
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  polkit
BuildRequires:  python3-devel
BuildRequires:  python3-gobject
BuildRequires:  python3-setuptools
BuildRequires:  update-desktop-files
# https://bugzilla.suse.com/show_bug.cgi?id=1022470
#!BuildIgnore:  rpmlint-mini
Requires:       cabextract
Requires:       fluid-soundfont-gm
Requires:       python3-Pillow
Requires:       python3-PyYAML
Requires:       python3-gobject
Requires:       python3-gobject-Gdk
Requires:       python3-requests
# controller support
Requires:       python3-evdev
Recommends:     winetricks
BuildArch:      noarch

%description
Lutris allows to gather and manage (install, configure and launch)
all games acquired from any source, in a single interface.
This includes, for example, Steam or Desura games, Windows games (WINE),
or emulated console games and browser games.

%prep
%setup -q -n %{name}

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
%{_datadir}/polkit-1/actions/*
%{python3_sitelib}/%{name}-*.egg-info
%{python3_sitelib}/%{name}/
%dir %{_datadir}/metainfo/
%{_datadir}/metainfo/%{appid}.appdata.xml

%changelog
