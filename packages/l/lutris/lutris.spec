#
# spec file for package lutris
#
# Copyright (c) 2024 SUSE LLC
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
%if 0%{?suse_version} > 1500
%define _py 3
%define _pyb 3
%else
%{?sle15_python_module_pythons}
%define _py 311
%define _pyb 3.11
%endif
Name:           lutris
Version:        0.5.16
Release:        0
Summary:        Manager for game installation and execution
License:        GPL-3.0-or-later
URL:            https://lutris.net
Source0:        https://lutris.net/releases/lutris_%{version}.tar.xz
BuildRequires:  %{python_module devel >= 3.7}
BuildRequires:  %{python_module gobject}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  gobject-introspection
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
Requires:       cabextract
#
Requires:       curl
Requires:       fluid-soundfont-gm
Requires:       p7zip
Requires:       psmisc
Requires:       python%{_py}-Pillow
Requires:       python%{_py}-PyYAML
Requires:       python%{_py}-cssselect
Requires:       python%{_py}-dbus-python
# controller support
Requires:       python%{_py}-evdev
Requires:       python%{_py}-gobject
Requires:       python%{_py}-gobject-Gdk
Requires:       python%{_py}-lxml
Requires:       python%{_py}-requests
Requires:       xrandr
# boo#1213440
Recommends:     ca-certificates-steamtricks
Recommends:     python%{_py}-distro
Recommends:     winetricks
BuildArch:      noarch

%description
Lutris allows to gather and manage (install, configure and launch)
all games acquired from any source, in a single interface.
This includes, for example, Steam or GOG games, Windows games (WINE),
or emulated console games and browser games.

%prep
%autosetup -p1 -n %{name}
sed -i "s|!%{_bindir}/env python3|!%{_bindir}/python%{_pyb}|" share/lutris/bin/lutris-wrapper

%build
%if 0%{?suse_version} > 1500
%py3_build
%else
%python_build
%endif

%install
%if 0%{?suse_version} > 1500
%py3_install
%else
%python_install
%endif
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
%{python_sitelib}/%{name}-*.egg-info
%{python_sitelib}/%{name}/
%dir %{_datadir}/metainfo/
%{_datadir}/metainfo/%{appid}.metainfo.xml

%changelog
