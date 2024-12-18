#
# spec file for package bstone
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2019-2024, Martin Hauke <mardnh@gmx.de>
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


Name:           bstone
Version:        1.2.13
Release:        0
Summary:        A source port of Blake Stone
# bstone is GPL-2.0+, but statically links GLM (MIT license), STB (public domain or MIT), and xbrz (GPL-3.0+)
License:        GPL-2.0-or-later AND MIT AND GPL-3.0-or-later
Group:          Amusements/Games/3D/Shoot
URL:            https://bibendovsky.github.io/bstone/
Source:         https://github.com/bibendovsky/bstone/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  ImageMagick
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(sdl2)

%description
A source port of the first-person shooter Blake Stone.

Features:
 *  High resolution rendering of world (extended vanilla engine)
 *  Modern and vanilla controls
 *  Allows to customize control bindings
 *  Separate volume control of sound effects and music
Supported games:
 *  Aliens of Gold (v1.0/v2.0/v2.1/v3.0) full or shareware
 *  Planet Strike (v1.0/v1.1)

NOTE: To play Blake Stone with bstone you need the original game files
You need to start the game from within the folder with these files.

%prep
%autosetup -p1
magick convert src/bstone/src/resources/win32/bstone_icon.ico %{name}.png

%build
%cmake
%cmake_build

%install
install -Dm0755 build/src/bstone/bstone %{buildroot}%{_bindir}/bstone
install -Dm0644 %{name}-4.png %{buildroot}/%{_datadir}/icons/hicolor/256x256/apps/%{name}.png

%files
%license LICENSE.txt "Blake Stone source code license.doc"
%doc CHANGELOG.md README.md
%{_bindir}/bstone
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
