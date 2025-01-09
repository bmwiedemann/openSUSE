#
# spec file for package lxqt-wayland-session
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


Name:           lxqt-wayland-session
Version:        0.1.1
Release:        0
Summary:        Files needed for the LXQt Wayland Session
License:        BSD-3-Clause AND GPL-2.0-or-later AND LGPL-2.1-or-later AND GPL-3.0-or-later AND MIT AND CC-BY-SA-4.0
URL:            https://github.com/lxqt/lxqt-wayland-session
Source0:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
## PATCH-CONFIGURATION-openSUSE 0001-configuration-changes-for-default-labwc-session.patch
Patch0:         0001-configuration-changes-for-default-labwc-session.patch
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  pkgconfig
BuildRequires:  xdg-user-dirs
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(lxqt2-build-tools)
BuildRequires:  pkgconfig(lxqt) >= 2.1.0
Requires:       layer-shell-qt6 >= 6.2.0
Requires:       lxqt-session >= 2.1.0
Requires:       xdg-user-dirs
BuildArch:      noarch

%description
Files needed for the LXQt Wayland Session: Wayland session start script,
its desktop entry for display managers and default configurations for
actually supported compositors.

%package -n     lxqt-hyprland-session
Summary:        Session files for LXQt-Hyprland
License:        BSD-3-Clause
Requires:       %{name} = %{version}
Requires:       hyprland
Requires:       hyprland-qtutils
Supplements:    (%{name} and hyprland)

%description -n lxqt-hyprland-session
This package contains the files necessary to use Hyprland as the Wayland
compositor with LXQt

%package -n     lxqt-niri-session
Summary:        Session files for LXQT-niri
License:        GPL-3.0-or-later
Requires:       %{name} = %{version}
Requires:       niri
Supplements:    (%{name} and niri)

%description -n lxqt-niri-session
This package contains the files necessary to use niri as the Wayland compositor
for LXQt

%package -n     lxqt-river-session
Summary:        Session files for LXQt-river
License:        GPL-3.0-or-later
Requires:       %{name} = %{version}
Requires:       river
Supplements:    (%{name} and river)

%description -n lxqt-river-session
This package contains the files necessary to use river as the Wayland
compositor with LXQt

%package -n     lxqt-sway-session
Summary:        Session files for LXQt-Sway
License:        MIT
Requires:       %{name} = %{version}
Requires:       sway
Supplements:    (%{name} and sway)

%description -n lxqt-sway-session
This package contains the files necessary to use Sway as the Wayland compositor
with LXQt

%package -n     lxqt-wayfire-session
Summary:        Session files for LXQt-wayfire
License:        MIT
Requires:       %{name} = %{version}
Requires:       wayfire
Recommends:     sddm-conf
Recommends:     wcm
Supplements:    (%{name} and wayfire)

%description -n lxqt-wayfire-session
This package contains the files necessary to use wayfire as the Wayland
compositor with LXQt

%package -n     lxqt-labwc-session
Summary:        Session files and theme for labwc
License:        CC-BY-SA-4.0 AND GPL-2.0-or-later
Requires:       %{name} = %{version}
Requires:       labwc >= 0.7.2
Requires:       swaybg
Requires:       swayidle
Requires:       swaylock
Recommends:     labwc-tweaks
Recommends:     sddm-conf
Recommends:     wdisplays
Supplements:    (%{name} and labwc)
Conflicts:      labwc-theme-vent <= %{version}

%description -n lxqt-labwc-session
This package contains the openbox themes and other files for labwc.

%prep
%autosetup -p1 -S git_am

%build
%cmake
%cmake_build

%install
%cmake_install

%fdupes -s %{buildroot}%{_datadir}/themes/

%check
%ctest

%files
%doc README.md
%license COPYING.LESSER LICENSE
%dir %{_datadir}/lxqt
%dir %{_datadir}/lxqt/wayland
%dir %{_datadir}/lxqt/wayland/firstrun
%dir %{_datadir}/wayland-sessions
%{_bindir}/startlxqtwayland
%{_datadir}/lxqt/wayland/firstrun/autostart
%{_datadir}/wayland-sessions/lxqt-wayland.desktop

%files -n lxqt-hyprland-session
%license LICENSE.BSD
%{_datadir}/lxqt/wayland/lxqt-hyprland.conf

%files -n lxqt-niri-session
%license COPYING
%{_datadir}/lxqt/wayland/lxqt-niri.kdl

%files -n lxqt-river-session
%license COPYING
%attr(0755,root,root)%{_datadir}/lxqt/wayland/lxqt-river-init

%files -n lxqt-sway-session
%license LICENSE.MIT
%{_datadir}/lxqt/wayland/lxqt-sway.config

%files -n lxqt-wayfire-session
%license LICENSE.MIT
%{_datadir}/lxqt/wayland/lxqt-wayfire.ini

%files -n lxqt-labwc-session
%license LICENSE.GPLv2
%dir %{_datadir}/lxqt/wallpapers
%dir %{_datadir}/lxqt/wayland/labwc
%dir %{_datadir}/lxqt/graphics
%{_datadir}/themes/Vent/
%{_datadir}/themes/Vent-dark/
%{_datadir}/lxqt/wallpapers/origami-dark-labwc.png
%{_datadir}/lxqt/wayland/labwc/README
%{_datadir}/lxqt/wayland/labwc/autostart
%{_datadir}/lxqt/wayland/labwc/environment
%{_datadir}/lxqt/wayland/labwc/menu.xml
%{_datadir}/lxqt/wayland/labwc/rc.xml
%{_datadir}/lxqt/wayland/labwc/themerc
%{_datadir}/lxqt/wayland/labwc/themerc-override
%{_datadir}/lxqt/graphics/lxqt-labwc.png

%changelog
