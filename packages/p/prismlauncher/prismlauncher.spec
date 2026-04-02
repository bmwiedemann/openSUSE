#
# spec file for package prismlauncher
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define _name PrismLauncher
Name:           prismlauncher
Version:        10.0.5
Release:        0
Summary:        A custom launcher for Minecraft
License:        GPL-3.0-only AND Apache-2.0 AND LGPL-3.0-only AND OFL-1.1 AND LGPL-2.1-only AND MIT AND BSD-3-Clause
URL:            https://github.com/%{_name}/%{_name}
# n=PrismLauncher && v=10.0.5 && d=$n-$v && f=$d.tar.xz && cd /tmp && git clone -b$v https://github.com/$n/$n.git $n && pushd $n && git submodule && git submodule update --init --recursive libraries/libnbtplusplus && git submodule status && rm -rf .??* && popd && mv $n $d && tar c --remove-files "$d" | xz -9e > "$f"
Source0:        %{_name}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  java-17-devel
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6CoreTools)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6NetworkAuth)
BuildRequires:  cmake(Qt6OpenGL)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  pkgconfig(gamemode)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libcmark)
BuildRequires:  pkgconfig(libqrencode)
BuildRequires:  pkgconfig(scdoc)
BuildRequires:  pkgconfig(tomlplusplus)
BuildRequires:  pkgconfig(zlib)
Requires:       pciutils
Recommends:     java <= 25
# xrandr needed for LWJGL on NVidia blob https://github.com/LWJGL/lwjgl/issues/128
Recommends:     xrandr
Suggests:       flite
Suggests:       gamemode
Conflicts:      %{name}-cracked
ExcludeArch:    i586 armv6hl armv7hl ppc s390

%description
A custom launcher for Minecraft that allows you to easily manage multiple installations of Minecraft at once.

%prep
%autosetup -p1 -n %{_name}-%{version}
sed -i -e 's|\$ORIGIN/||' -e 's/\${TODAY}/unknown/' CMakeLists.txt

%build
%cmake -LA \
       -DLauncher_BUILD_PLATFORM="openSUSE" \
       -DLauncher_QT_VERSION_MAJOR="6"
%cmake_build

%check
%ctest

%install
%cmake_install

%files
%license COPYING.md LICENSE
%doc README.md
%{_bindir}/%{name}
%dir %{_datadir}/PrismLauncher
%{_datadir}/PrismLauncher/*
%{_datadir}/applications/org.%{name}.PrismLauncher.desktop
%{_datadir}/icons/hicolor/*/apps/org.%{name}.PrismLauncher.{png,svg}
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/org.%{name}.PrismLauncher.metainfo.xml
%{_datadir}/mime/packages/modrinth-mrpack-mime.xml
%dir %{_datadir}/qlogging-categories6
%{_datadir}/qlogging-categories6/%{name}.categories
%{_mandir}/man?/prismlauncher.*

%changelog
