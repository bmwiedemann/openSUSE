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


%{?sle15_python_module_pythons}
%define         _py 311
%define         _pyb 3.11
%define         appid net.lutris.Lutris
Name:           lutris
Version:        0.5.17
Release:        0
Summary:        Manager for game installation and execution
License:        GPL-3.0-or-later
URL:            https://lutris.net
Source0:        https://lutris.net/releases/lutris_%{version}.tar.xz
%if 0%{?suse_version} >= 1600
BuildRequires:  fdupes
BuildRequires:  gettext-tools
BuildRequires:  gobject-introspection
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  python3-devel >= 3.7
BuildRequires:  python3-gobject
BuildRequires:  python3-setuptools
BuildRequires:  update-desktop-files
Requires:       cabextract
Requires:       curl
Requires:       fluid-soundfont-gm
Requires:       p7zip
Requires:       psmisc
Requires:       python3-Pillow
Requires:       python3-PyYAML
Requires:       python3-certifi
Requires:       python3-dbus-python
Requires:       python3-distro
Requires:       python3-protobuf
# controller support
Requires:       python3-evdev
Requires:       python3-gobject
Requires:       python3-gobject-Gdk
Requires:       python3-lxml
Requires:       python3-requests
%if %{with discord}
Requires:       python3-pypresence
%endif
%if %{with moddb}
Requires:       python3-moddb
%endif
%else
BuildRequires:  fdupes
BuildRequires:  gettext-tools
BuildRequires:  gobject-introspection
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  python%{_py}-devel
BuildRequires:  python%{_py}-gobject
BuildRequires:  python%{_py}-setuptools
BuildRequires:  update-desktop-files
Requires:       cabextract
Requires:       curl
Requires:       fluid-soundfont-gm
Requires:       p7zip
Requires:       psmisc
Requires:       python%{_py}-Pillow
Requires:       python%{_py}-PyYAML
Requires:       python%{_py}-certifi
Requires:       python%{_py}-dbus-python
Requires:       python%{_py}-distro
Requires:       python%{_py}-lxml
Requires:       python%{_py}-protobuf
Requires:       python%{_py}-requests
# controller support
# we can't have controller support in Leap as python311-evdev is missing
%if %{with discord}
Requires:       python%{_py}-pypresence
%endif
%if %{with moddb}
Requires:       python%{_py}-moddb
%endif
%endif
Requires:       xrandr
# boo#1213440
Recommends:     ca-certificates-steamtricks
Recommends:     winetricks
BuildArch:      noarch
%lang_package

%description
Lutris allows to gather and manage (install, configure and launch)
all games acquired from any source, in a single interface.
This includes, for example, Steam or GOG games, Windows games (WINE),
or emulated console games and browser games.

%prep
%autosetup -n %{name}

%build
%if 0%{?suse_version} >= 1600
%meson
%meson_build
%else
%python_build
%endif

%install
%if 0%{?suse_version} >= 1600
%meson_install
%find_lang %{name}
%python3_fix_shebang_path %{buildroot}%{_bindir}/*
%python3_fix_shebang_path %{buildroot}%{_datadir}/%{name}/bin/*
%else
%python_install
sed -i "s|!%{_bindir}/env python3|!%{_bindir}/python%{_pyb}|" \
     %{buildroot}%{_datadir}/%{name}/bin/%{name}-wrapper
%endif
%fdupes %{buildroot}

%files
%doc README.rst CONTRIBUTING.md AUTHORS
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man?/%{name}.?%{?ext_man}
%{_datadir}/%{name}
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/icons/hicolor/??x??/apps/%{name}.png
%{_datadir}/icons/hicolor/???x???/apps/%{name}.png
%{python_sitelib}/%{name}
%{_datadir}/metainfo/%{appid}.metainfo.xml

%if 0%{?suse_version} >= 1600
%files lang -f %{name}.lang
%else
%{python_sitelib}/%{name}-*.egg-info
%endif

%changelog
