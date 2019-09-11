#
# spec file for package photoqt
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        1.7.1
Release:        0
Summary:        A Qt-based image viewer
License:        GPL-2.0-or-later
Group:          Productivity/Graphics/Viewers
URL:            http://photoqt.org/
Source0:        http://photoqt.org/pkgs/%{name}-%{version}.tar.gz
Patch0:         photoqt-1.7-link.patch
Patch1:         0001-Switch-to-FindLibExiv2-from-ECM-5.53.0.patch
Patch2:         0002-Fix-build-with-exiv2-0.27.patch
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  freeimage-devel
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(GraphicsMagick++)
BuildRequires:  pkgconfig(IL)
BuildRequires:  pkgconfig(Qt5Multimedia) >= 5.4.0
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5UiTools)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(exiv2)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libraw)
BuildRequires:  pkgconfig(poppler-qt5)

%description
PhotoQt is a configurable image viewer.

%prep
%autosetup -p1

%build
%cmake -DCRYPTKEY:STRING=4242
make %{?_smp_mflags}

%install
%cmake_install

%post
%icon_theme_cache_post
%desktop_database_post

%postun
%icon_theme_cache_postun
%desktop_database_postun

%files
%license COPYING
%doc CHANGELOG
%{_bindir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.??g

%changelog
