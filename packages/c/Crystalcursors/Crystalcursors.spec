#
# spec file for package Crystalcursors
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


Name:           Crystalcursors
BuildRequires:  libpng
BuildRequires:  xcursorgen
URL:            https://digilander.libero.it/m4rt/html/crystalcursors.html
Summary:        Mouse Cursors in Crystal Icon Style
License:        LGPL-2.1-or-later
Group:          System/X11/Icons
Version:        0.9
Release:        0
Source:         https://digilander.libero.it/m4rt/files/Crystalcursors.tar.bz2
Patch0:         root-installation.diff
BuildRequires:  ImageMagick
BuildArch:      noarch

%description
Four different mouse cursor icon sets in the KDE CrystalSVG style. In
white, gray, blue, and green versions. They can be selected from KDE
Control Center, in the mouse configuration.

%prep
%autosetup -p1 -n %name

%build
make

%install
%make_install

%files
%license LICENSE
%doc CHANGELOG CREDITS README
/usr/share/icons/*

%changelog
