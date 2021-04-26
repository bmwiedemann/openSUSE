#
# spec file for package deepin-image-viewer
#
# Copyright (c) 2021 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2017-2021 Hillwood Yang <hillwood@opensuse.org>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%if 0%{?is_opensuse}
    %define  distribution  openSUSE-Edition
%else
    %define  distribution  SUSE-Edition
%endif

Name:           deepin-image-viewer
Version:        5.7.4
Release:        0
License:        GPL-3.0+
Summary:        Deepin Image Viewer
Url:            https://github.com/linuxdeepin/deepin-image-viewer
Group:          Productivity/Graphics/Viewers
Source0:        https://github.com/linuxdeepin/deepin-image-viewer/archive/%{version}/%{name}-%{version}.tar.gz
Source99:       %{name}.appdata.xml
BuildRequires:  fdupes
BuildRequires:  libqt5-linguist
BuildRequires:  hicolor-icon-theme
BuildRequires:  update-desktop-files
BuildRequires:  deepin-gettext-tools
BuildRequires:  freeimage-devel
BuildRequires:  dtkcore >= 5.0.0
BuildRequires:  libQt5Widgets-private-headers-devel
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  pkgconfig(libraw)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(dtkwidget) >= 5.0.0
BuildRequires:  pkgconfig(gio-qt)
BuildRequires:  pkgconfig(udisks2-qt5)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(gio-unix-2.0)
Recommends:     %{name}-lang
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Deepin Image Viewer is the Image Viewer for Deepin Desktop Environment(DDE)

%lang_package

%prep
%setup -q
# %patch0 -p1
%if 0%{?suse_version} > 1500
# %patch1 -p1
%endif
sed -i "s/(lrelease/(lrelease-qt5/g" src/src.pro
# sed -i '/#include <QDebug>/a #include <QPainterPath>' \
#         viewer/frame/toptoolbar.cpp \
#         viewer/module/view/contents/ttbcontent.cpp
# sed -i '/#include <QtDebug>/a #include <QPainterPath>' \
#         viewer/module/view/contents/imageinfowidget.cpp
sed -i '/FIF_FAXG3/d' src/src/utils/unionimage.cpp
sed -i 's/Exec=deepin-image-viewer/Exec=env QT_QPA_PLATFORMTHEME=deepin deepin-image-viewer/g' \
src/%{name}.desktop

%build
%cmake -DCMAKE_BUILD_TYPE=Release \
       -DAPP_VERSION=%{version}-%{distribution} \
       -DVERSION=%{version}-%{distribution}
%make_build

%install
%cmake_install
install -d %{buildroot}%{_datadir}/appdata
cp %{SOURCE99} %{buildroot}%{_datadir}/appdata/

sed -i 's/1.2.15/%{version}/g;s/2017-08-18/2021-03-19/g' \
%{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

%suse_update_desktop_file -r -G "Deepin Image Viewer" %{name} Graphics 2DGraphics RasterGraphics Viewer

%fdupes %{buildroot}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/deepin-manual
%{_datadir}/%{name}/icons/
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/appdata
%{_datadir}/appdata/%{name}.appdata.xml
%{_libdir}/qt5/plugins/imageformats/*.so
%{_datadir}/dbus-1/services/com.deepin.ImageViewer.service

%files lang
%{_datadir}/%{name}/translations

%changelog

