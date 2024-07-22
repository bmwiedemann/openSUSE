#
# spec file for package vimiv-qt
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

%define pythons python3
%define bin vimiv
%define app org.karlch.vimiv.qt

Name:           vimiv-qt
Version:        0.9.0
Release:        0
Summary:        An image viewer with vim-like keybindings
License:        GPL-3.0-or-later
Url:            https://karlch.github.io/vimiv-qt/
Source0:        https://github.com/karlch/vimiv-qt/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        vimiv-qt.rpmlintrc
BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-wheel
BuildRequires:  python3-setuptools
BuildRequires:  python3-qt5
BuildRequires:  fdupes
BuildRequires:  desktop-file-utils
BuildRequires:  hicolor-icon-theme
Requires:       python3-qt5
# Formats and exif data.
Recommends:     python3-exiv2
Recommends:     python3-piexif
Recommends:     libQt5Svg5
Recommends:     libqt5-qtimageformats

%description
Vimiv is an image viewer with vim-like keybindings.
 
- Basic image operations and navigation
- ranger-like library to browse your images
- Thumbnail mode: navigable grid of image previews
- Command mode with tab-completion
- Search with pattern matching
- Simple mark and tag system

%prep
%autosetup

# Place makefile in correct location
mv misc/Makefile .

# License installs to licensedir/vimiv, not vimiv-qt
sed -i '/LICENSE/ d' Makefile
# We use make_install for installing non-python parts
sed -i '/python3 setup.py install/ d' Makefile

%build
%pyproject_wheel

%install
%pyproject_install
%make_install
%fdupes %{buildroot}%{python3_sitearch}
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{bin}.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/%{bin}
%{python3_sitearch}/vimiv
%{python3_sitearch}/vimiv-%{version}.dist-info
%{_datadir}/applications/%{bin}.desktop
%{_datadir}/icons/hicolor/*/apps/vimiv.*
%{_datadir}/metainfo/%{app}.metainfo.xml
%{_mandir}/man?/%{bin}.?%{?ext_man}

%changelog
