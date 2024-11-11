#
# spec file for package lxqt-wayland-session
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


Name:           lxqt-wayland-session
Version:        0.1.0
Release:        0
Summary:        Files needed for the LXQt Wayland Session
License:        LGPL-2.1-or-later
URL:            https://github.com/lxqt/lxqt-wayland-session
Source0:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
Patch1:         001-labwc-autostart-swaybg.patch
BuildRequires:  cmake
BuildRequires:  cmake(lxqt2-build-tools)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(lxqt) >= 2.1.0
BuildRequires:  xdg-user-dirs
Requires:       xdg-user-dirs
#ecommends:     kwin6
#uggests:       labwc
BuildArch:      noarch

%description
Files needed for the LXQt Wayland Session: Wayland session start script,
its desktop entry for display managers and default configurations for
actually supported compositors.

%package -n     labwc-theme-vent
Summary:        Vent openbox themes
Requires:       labwc
Requires:       swaybg
Requires:       swayidle
Requires:       swaylock
Supplements:    (%{name} and labwc)

%description -n labwc-theme-vent
This package contains the openbox themes and other files for labwc.

%prep
%autosetup -p1

%build
%cmake
%make_build

%install
%cmake_install
%fdupes -s %{buildroot}%{_datadir}/themes/

%files
%doc README.md
%{_bindir}/startlxqtwayland
%dir %{_datadir}/lxqt
%dir %{_datadir}/lxqt/wayland
%{_datadir}/lxqt/wayland/lxqt-*
%dir %{_datadir}/lxqt/wayland/firstrun
%{_datadir}/lxqt/wayland/firstrun/autostart
%dir %{_datadir}/wayland-sessions
%{_datadir}/wayland-sessions/lxqt-wayland.desktop
%license COPYING.LESSER

%files -n labwc-theme-vent
%{_datadir}/themes/Vent/
%{_datadir}/themes/Vent-dark/
%dir %{_datadir}/lxqt/wallpapers
%{_datadir}/lxqt/wallpapers/origami-dark-labwc.png
%dir %{_datadir}/lxqt/wayland/labwc
%{_datadir}/lxqt/wayland/labwc/README
%{_datadir}/lxqt/wayland/labwc/autostart
%{_datadir}/lxqt/wayland/labwc/environment
%{_datadir}/lxqt/wayland/labwc/menu.xml
%{_datadir}/lxqt/wayland/labwc/rc.xml
%{_datadir}/lxqt/wayland/labwc/themerc
%{_datadir}/lxqt/wayland/labwc/themerc-override
%dir %{_datadir}/lxqt/graphics
%{_datadir}/lxqt/graphics/lxqt-labwc.png

%changelog
