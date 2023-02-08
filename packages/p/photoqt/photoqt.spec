#
# spec file for package photoqt
#
# Copyright (c) 2023 SUSE LLC
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
Version:        3.0
Release:        0
Summary:        A Qt-based image viewer
License:        GPL-2.0-or-later
Group:          Productivity/Graphics/Viewers
URL:            https://photoqt.org/
Source0:        https://photoqt.org/pkgs/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  freeimage-devel
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(IL)
BuildRequires:  pkgconfig(Magick++)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Multimedia) >= 5.4.0
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5UiTools)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(exiv2)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libraw)
BuildRequires:  pkgconfig(poppler-qt5)
BuildRequires:  pkgconfig(pugixml)

%description
PhotoQt is a configurable image viewer.

%prep
%autosetup -p1

%build
%cmake -DCRYPTKEY:STRING=4242 \
       -DCHROMECAST=OFF \
       -DGRAPHICSMAGICK=OFF \
       -DIMAGEMAGICK=ON

make %{?_smp_mflags}

%install
%cmake_install

%files
%license COPYING
%doc CHANGELOG
%{_bindir}/%{name}
%{_datadir}/metainfo/org.photoqt.PhotoQt.metainfo.xml
%{_datadir}/applications/org.photoqt.PhotoQt*.desktop
%{_datadir}/icons/hicolor/*/apps/org.photoqt.PhotoQt.png

%changelog
