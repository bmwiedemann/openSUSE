#
# spec file for package fotowall
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2007-2014 Packman Team <packman@links2linux.de>
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


Name:           fotowall
Version:        1.1.4
Release:        0
Summary:        A wallpaper generator
# fotowall is GPL-2.0+, everything else regards 3rdparty modules
License:        BSD-2-Clause AND GPL-2.0-or-later AND LGPL-2.1-or-later AND GPL-3.0-or-later
URL:            https://github.com/fotowall/fotowall
Source0:        https://github.com/fotowall/fotowall/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(libv4l2)

%description
FotoWall is a wallpaper generator rendering pictures
in a high resolution composition.

The interface offers functionality such as:
- drag multiple pictures inside fotowall
- use the red button on the lower rigt corner to resize the picture
- use the green button on the lower right corner to rotate the picture
- press the "del" button after selecting a picture to remove it from the composition
- move the mouse on the corners to change various colors in an extremely cool way

%prep
%autosetup -p1

%build
%qmake5
%make_build

%install
%qmake5_install
%suse_update_desktop_file -r %{name} Graphics RasterGraphics

%files
%doc README.md
%license GPL_V2
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
