#
# spec file for package photoqt
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


Name:           photoqt
Version:        5.4
Release:        0
Summary:        A Qt-based image viewer
License:        GPL-2.0-or-later
Group:          Productivity/Graphics/Viewers
URL:            https://photoqt.org/
Source0:        https://gitlab.com/lspies/photoqt/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
BuildRequires:  cmake >= 3.16
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(IL)
BuildRequires:  pkgconfig(Magick++)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core) >= 6.4
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Linguist)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6Pdf)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6UiTools)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  pkgconfig(exiv2)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libraw)
BuildRequires:  pkgconfig(mpv)
BuildRequires:  pkgconfig(poppler-qt6)
BuildRequires:  pkgconfig(pugixml)
BuildRequires:  qt6-imageformats-devel 
Requires:       qt6-sql-sqlite
Requires:       qt6-location
Requires:       qt6-multimedia
Requires:       qt6-positioning

%description
PhotoQt is a configurable image viewer.

%prep
%autosetup -p1 -n %{name}-v%{version}

%build
%cmake -DCRYPTKEY:STRING=4242 \
       -DWITH_CHROMECAST=OFF \
       -DWITH_ZXING=OFF \
       -DCMAKE_SKIP_RPATH=ON

%make_build

%install
%cmake_install

%files
%license COPYING
%doc CHANGELOG
%{_bindir}/%{name}
%{_datadir}/metainfo/org.photoqt.PhotoQt.metainfo.xml
%{_datadir}/applications/org.photoqt.PhotoQt*.desktop
%{_datadir}/icons/hicolor/*/apps/org.photoqt.PhotoQt.png
%dir %{_datadir}/icons/hicolor/1024x1024/
%dir %{_datadir}/icons/hicolor/1024x1024/apps

%changelog
