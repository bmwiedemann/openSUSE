#
# spec file for package hedgewars
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


%bcond_with server
%bcond_with videorec
# FPC (Pascal) engine is disabled on some 32-bit archs due to a FPC bug
%ifarch %{ppc}
%bcond_without engine_c
%else
%bcond_with engine_c
%endif
Name:           hedgewars
Version:        1.0.3
Release:        0
Summary:        Turn-based artillery game, featuring fighting hedgehogs
License:        GPL-2.0-only
Group:          Amusements/Games/Strategy/Turn Based
URL:            https://www.hedgewars.org/
Source:         https://hedgewars.org/download/releases/hedgewars-src-%{version}.tar.bz2
Source99:       %{name}-rpmlintrc
Patch0:         hedgewars-disable_fpc_workaround.patch
# PATCH-FIX-OPENSUSE hedgewars-1.0.2-rpath.patch -- Fix RPATH with non-system library path
Patch1:         hedgewars-1.0.2-rpath.patch
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
# Required for QAbstractFileEngine*, which is no longer public since Qt5.12
BuildRequires:  libQt5Core-private-headers-devel
BuildRequires:  libphysfs-devel >= 3.0
BuildRequires:  libpng-devel
BuildRequires:  libqt5-linguist-devel
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(SDL2_net)
BuildRequires:  pkgconfig(SDL2_ttf)
BuildRequires:  pkgconfig(lua5.1)
BuildRequires:  pkgconfig(sdl2)
Requires:       %{name}-data = %{version}
Recommends:     %{name}-server = %{version}
ExcludeArch:    armv6l armv6hl
%if %{with engine_c}
BuildRequires:  clang
BuildRequires:  ghc
BuildRequires:  glew-devel
%else
BuildRequires:  fpc
BuildRequires:  gcc
BuildRequires:  gcc-c++
%endif
# to build server
%if %{with server}
BuildRequires:  ghc
# BuildRequires:  ghc-dataenc-devel
BuildRequires:  ghc-SHA-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-entropy-devel
BuildRequires:  ghc-hslogger-devel
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-random-devel
BuildRequires:  ghc-regex-tdfa-devel
BuildRequires:  ghc-sandi-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-utf8-string-devel
BuildRequires:  ghc-vector-devel
BuildRequires:  ghc-zlib-devel
%endif

%description
Hedgewars is a turn-based artillery game where slow-moving hedgehocks fight
each other with over-the-top weaponary. It can be played both online and
rotational on the same computer.

%package data
Summary:        Game data files for Hedgewars, a turn-based artillery game
Group:          Amusements/Games/Strategy/Turn Based
Requires:       %{name} = %{version}
BuildArch:      noarch

%description data
Hedgewars is a turn-based artillery game where slow-moving hedgehocks fight
each other with over-the-top weaponary. It can be played both online and
rotational on the same computer.

This package contains all the data files for hedgewars.

%package server
Summary:        Standalone server for Hedgewars, a turn-based strategy game
Group:          Amusements/Games/Strategy/Turn Based
Requires:       %{name}-data = %{version}

%description server
Hedgewars is a turn-based artillery game where slow-moving hedgehocks fight
each other with over-the-top weaponary. It can be played both online and
rotational on the same computer.

This package contains a standalone local hedgewars server.

%prep
%setup -q -n %{name}-src-%{version}
%patch -P 0 -p0
%patch -P 1 -p1

%build
# CMAKE_POLICY_DEFAULT_CMP0083=NEW - apply POSITION_INDEPENDENT_CODE also to "-pie", since CMake 3.14
%cmake \
  -DPOSITION_INDEPENDENT_CODE=ON \
  -DCMAKE_POLICY_DEFAULT_CMP0083=NEW \
  -DNOVIDEOREC=%{?_with_videorec:0}%{!?_with_videorec:1} \
  -DNOSERVER=%{?_with_server:0}%{!?_with_server:1} \
  -DBUILD_ENGINE_C=%{?_with_engine_c:1}%{!?_with_engine_c:0}
%cmake_build

%install
%cmake_install

install -D -m 0644 man/%{name}.6 %{buildroot}%{_mandir}/man6/%{name}.6
install -D -m 0644 misc/hedgewars_ico.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -D -m 0644 misc/hedgewars.png %{buildroot}%{_datadir}/icons/hicolor/512x512/apps/%{name}.png
mkdir -p  %{buildroot}%{_datadir}/applications/
mv %{buildroot}%{_datadir}/%{name}/Data/misc/%{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
mkdir -p  %{buildroot}%{_datadir}/mime/packages
mv %{buildroot}%{_datadir}/%{name}/Data/misc/hedgewars-mimeinfo.xml %{buildroot}%{_datadir}/mime/packages/%{name}.xml
# appdata name is deprecated in favor of metainfo
mv %{buildroot}%{_datadir}/{appdata,metainfo}
chmod -x %{buildroot}%{_datadir}/mime/packages/%{name}.xml %{buildroot}%{_datadir}/metainfo/hedgewars.appdata.xml

# Delete obsolete xpm icon, .desktop uses the ones from hicolor
rm %{buildroot}%{_datadir}/pixmaps/hedgewars.xpm

%fdupes %{buildroot}%{_datadir}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc README.md ChangeLog.txt
%license COPYING Fonts_LICENSE.txt
%{_mandir}/man6/*
%{_datadir}/applications/*.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%dir %{_datadir}/metainfo/
%{_datadir}/metainfo/hedgewars.appdata.xml
%{_bindir}/%{name}
%{_bindir}/hwengine
# ugly, but necessary:
%{_libdir}/libphyslayer.so.1.0
%{_libdir}/libphyslayer.so

%files data
%{_datadir}/%{name}/

%if %{with server}
%files server
%{_bindir}/%{name}-server
%endif

%changelog
