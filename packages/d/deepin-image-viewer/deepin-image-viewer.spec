#
# spec file for package deepin-image-viewer
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2017-2022 Hillwood Yang <hillwood@opensuse.org>
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


%if 0%{?is_opensuse}
    %define  distribution  openSUSE-Edition
%else
    %define  distribution  SUSE-Edition
%endif

Name:           deepin-image-viewer
Version:        5.9.9
Release:        0
Summary:        Deepin Image Viewer
License:        GPL-3.0-or-later
Group:          Productivity/Graphics/Viewers
URL:            https://github.com/linuxdeepin/deepin-image-viewer
Source0:        https://github.com/linuxdeepin/deepin-image-viewer/archive/%{version}/%{name}-%{version}.tar.gz
Source99:       %{name}.appdata.xml
%if 0%{?suse_version} > 1500
# PATCH-FIX-UPSTREAM update-libraw-api.patch hillwood@opensuse.org - Update api for libraw
Patch0:         update-libraw-api.patch
%endif
BuildRequires:  deepin-gettext-tools
%ifarch ppc ppc64 ppc64le s390 s390x
BuildRequires:  deepin-desktop-base
%else
BuildRequires:  deepin-manual
%endif
BuildRequires:  dtkcore >= 5.0.0
BuildRequires:  fdupes
BuildRequires:  freeimage-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  libQt5Widgets-private-headers-devel
BuildRequires:  libimageviewer-devel
BuildRequires:  libqt5-linguist
BuildRequires:  update-desktop-files
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(dtkwidget) >= 5.0.0
BuildRequires:  pkgconfig(gio-qt)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libraw)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(udisks2-qt5)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
Recommends:     %{name}-lang
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Deepin Image Viewer is the Image Viewer for Deepin Desktop Environment(DDE)

%lang_package

%prep
%autosetup -p1
sed -i "s/(lrelease/(lrelease-qt5/g" src/src.pro
# sed -i '/FIF_FAXG3/d' src/src/utils/unionimage.cpp
sed -i 's/Exec=deepin-image-viewer/Exec=env QT_QPA_PLATFORMTHEME=deepin deepin-image-viewer/g' \
src/%{name}.desktop
sed -i 's|"../libimageviewer/image-viewer_global.h"|<libimageviewer/image-viewer_global.h>|g' \
src/src/module/view/homepagewidget.cpp

%build
%cmake -DCMAKE_BUILD_TYPE=Release \
       -DAPP_VERSION=%{version}-%{distribution} \
       -DVERSION=%{version}-%{distribution}
%cmake_build

%install
%cmake_install
# Install appdata
install -d %{buildroot}%{_datadir}/appdata
cp %{SOURCE99} %{buildroot}%{_datadir}/appdata/
# Fix version in appdata
RELEASE_DATE=$(stat --format="%%y" %{SOURCE0} | grep -Po "\\d{4}-\\d{2}-\\d{2}")
sed -i "s/@VERSION@/%{version}/g;s/@DATE@/$RELEASE_DATE/g" \
%{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

# Fix desktop profile
%suse_update_desktop_file -r -G "Deepin Image Viewer" %{name} Graphics 2DGraphics RasterGraphics Viewer

# Find translations
%find_lang %{name} --with-qt
%fdupes %{buildroot}

%files
%doc README.md README.zh_CN.md
%license LICENSE.txt
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/icons/
%{_datadir}/deepin-manual/manual-assets/application/%{name}
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/appdata
%{_datadir}/appdata/%{name}.appdata.xml
%{_libdir}/qt5/plugins/imageformats/libxraw.so*
%{_datadir}/dbus-1/services/com.deepin.ImageViewer.service

%files lang -f %{name}.lang
%dir %{_datadir}/%{name}/translations
%lang(ast) %{_datadir}/deepin-image-viewer/translations/deepin-image-viewer_ast.qm
%{_datadir}/%{name}/translations/deepin-image-viewer.qm

%changelog
