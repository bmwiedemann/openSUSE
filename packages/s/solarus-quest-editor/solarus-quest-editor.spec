#
# spec file for package solarus-quest-editor
#
# Copyright (c) 2020 SUSE LLC
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


Name:           solarus-quest-editor
Version:        1.6.4
Release:        0
Summary:        GUI to edit quests for the Solarus engine
License:        GPL-3.0-or-later AND CC-BY-SA-3.0
Group:          Productivity/Graphics/Other
URL:            https://www.solarus-games.org/
Source:         https://gitlab.com/solarus-games/solarus-quest-editor/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
# PATCH-FIX-UPSTREAM
Patch0:         0001-Add-missing-include-directive-for-QPainterPath.patch
BuildRequires:  cmake >= 3.1
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  glm-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  physfs-devel
BuildRequires:  solarus-devel >= 1.6.0
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Help)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(SDL2_ttf)
BuildRequires:  pkgconfig(libmodplug)
BuildRequires:  pkgconfig(luajit)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(vorbis)
Requires:       %{name}-assets = %{version}

%description
Solarus Quest Editor is a graphical user interface to create and
modify quests for the Solarus engine.

%package assets
Summary:        Assets for the Solarus Quest Editor
Group:          Productivity/Graphics/Other
BuildArch:      noarch

%description assets
This package contains assets for the Solarus Quest Editor.

%lang_package

%prep
%autosetup -p1 -n %{name}-v%{version}

%build
%cmake
%cmake_build

%install
%cmake_install
%fdupes %{buildroot}%{_prefix}
%find_lang solarus_editor --with-qt

%files
%license license.txt license_gpl.txt
%doc readme.md changelog.txt
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%dir %{_datadir}/icons/hicolor/20x20
%dir %{_datadir}/icons/hicolor/20x20/apps
%dir %{_datadir}/icons/hicolor/40x40
%dir %{_datadir}/icons/hicolor/40x40/apps
%{_datadir}/icons/hicolor/*/apps/%{name}*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%files assets
%{_datadir}/%{name}/assets

%files lang -f solarus_editor.lang
%dir %{_datadir}/%{name}/translations

%changelog
