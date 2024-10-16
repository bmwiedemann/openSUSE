#
# spec file for package digikam
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


%define soversion 8_4_0
%bcond_without released
%bcond_with    apidocs
Name:           digikam
Version:        8.4.0
Release:        0
Summary:        A KDE Photo Manager
License:        GPL-2.0-or-later
URL:            https://www.digikam.org/
Source0:        https://download.kde.org/stable/%{name}/%{version}/digiKam-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/%{name}/%{version}/digiKam-%{version}.tar.xz.sig
Source2:        %{name}.keyring
%endif
# PATCH-FIX-OPENSUSE
Patch0:         0001-Look-for-each-akonadi-component-separately.patch
# QtWebEngine is not available on ppc and zSystems
ExclusiveArch:  %{arm} aarch64 %{ix86} x86_64 %{riscv}
BuildRequires:  bison
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  hicolor-icon-theme
BuildRequires:  lensfun
BuildRequires:  libboost_graph-devel
BuildRequires:  libeigen3-devel
BuildRequires:  libexiv2-devel >= 0.27.1
BuildRequires:  liblqr-devel
BuildRequires:  libtiff-devel
BuildRequires:  opencv-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
%if %{with apidocs}
BuildRequires:  doxygen
BuildRequires:  graphviz-devel
BuildRequires:  cmake(KF5DocTools)
%endif
BuildRequires:  cmake(KF5CalendarCore)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5Contacts)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5FileMetaData)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5NotifyConfig)
BuildRequires:  cmake(KF5Sane)
BuildRequires:  cmake(KF5Service)
BuildRequires:  cmake(KF5Solid)
BuildRequires:  cmake(KF5Sonnet)
BuildRequires:  cmake(KF5ThreadWeaver)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Marble)
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Multimedia)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5NetworkAuth)
BuildRequires:  cmake(Qt5OpenGL)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5WebEngineWidgets)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  cmake(Qt5XmlPatterns)
BuildRequires:  cmake(libheif)
BuildRequires:  pkgconfig(Magick++)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(jasper)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(lensfun)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libgphoto2) >= 2.4.0
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libjxl)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libswresample)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(zlib)
Requires:       %{name}-plugins
Requires:       libQt5Sql5-sqlite
Recommends:     marble
Recommends:     showfoto
# Got merged into libimageeditor in 5.2.0
Provides:       %{name}-plugin-color = %{version}
Obsoletes:      %{name}-plugin-color < %{version}
Provides:       %{name}-plugin-decorate = %{version}
Obsoletes:      %{name}-plugin-decorate < %{version}
Provides:       %{name}-plugin-enhance = %{version}
Obsoletes:      %{name}-plugin-enhance < %{version}
Provides:       %{name}-plugin-fxfilters = %{version}
Obsoletes:      %{name}-plugin-fxfilters < %{version}
Provides:       %{name}-plugin-transform = %{version}
Obsoletes:      %{name}-plugin-transform < %{version}
Obsoletes:      digikam-libs < %{version}
# Docs no longer included in 6.0.0
Provides:       %{name}-doc = %{version}
Obsoletes:      %{name}-doc < %{version}

%description
digiKam is a simple digital photo management application for KDE, which
allows you to import and organize your digital photos easily. The
photos can be organized in albums, which can be sorted chronologically,
by directory layout, or by custom collections. An easy-to-use interface
that enables you to connect to your camera and preview, download, or
delete your images, is provided.

%package plugins
Summary:        DigiKam plugins
Recommends:     enblend-enfuse
Recommends:     hugin

%description plugins
Additional plugins for digiKam.

%package devel
Summary:        DigiKam development files
Requires:       libdigikamcore%{soversion} = %{version}

%description devel
Development headers and libraries for digiKam.

%package -n showfoto
Summary:        DigiKam: Showfoto
Supplements:    %{name}

%description -n showfoto
Additional program to browse and view photos

%package -n libdigikamcore%{soversion}
Summary:        The main digikam libraries
Recommends:     %{name}-plugins

%description -n libdigikamcore%{soversion}
The main digikam libraries that are being shared between showfoto and digikam

%lang_package

%prep
%autosetup -p1

%build
%{cmake_kf5 -d build -- \
  -DENABLE_APPSTYLES=ON \
  -DENABLE_MEDIAPLAYER=ON \
  -DENABLE_KFILEMETADATASUPPORT=ON \
  -DENABLE_AKONADICONTACTSUPPORT=OFF
}

%cmake_build

%if %{with apidocs}
%cmake_build doc
%endif

%install
%kf5_makeinstall -C build

%suse_update_desktop_file -r org.kde.digikam Qt KDE Graphics Photography
%suse_update_desktop_file -r org.kde.showfoto Qt KDE Graphics Photography

%find_lang %{name} --without-kde

%fdupes %{buildroot}

%ldconfig_scriptlets -n libdigikamcore%{soversion}

%files
%doc AUTHORS NEWS README.md
%dir %{_kf5_sharedir}/solid
%dir %{_kf5_sharedir}/solid/actions
%doc %{_kf5_mandir}/man1/cleanup_digikamdb.1%{ext_man}
%doc %{_kf5_mandir}/man1/digitaglinktree.1%{ext_man}
%{_kf5_applicationsdir}/org.kde.digikam.desktop
%{_kf5_appstreamdir}/org.kde.digikam.appdata.xml
%{_kf5_bindir}/cleanup_digikamdb
%{_kf5_bindir}/digikam
%{_kf5_bindir}/digitaglinktree
%{_kf5_iconsdir}/hicolor/*/actions/
%{_kf5_iconsdir}/hicolor/*/apps/avplayer.*
%{_kf5_iconsdir}/hicolor/*/apps/digikam.*
%{_kf5_kxmlguidir}/digikam/
%{_kf5_notifydir}/digikam.notifyrc
%{_kf5_sharedir}/digikam/
%{_kf5_sharedir}/solid/actions/digikam-opencamera.desktop

%files plugins
%{_kf5_iconsdir}/hicolor/*/apps/dk-*
%{_kf5_iconsdir}/hicolor/*/apps/expoblending.*
%{_kf5_iconsdir}/hicolor/*/apps/panorama.*
%{_kf5_plugindir}/digikam/

%files devel
%{_includedir}/digikam/
%{_kf5_cmakedir}/DigikamCore/
%{_kf5_cmakedir}/DigikamDatabase/
%{_kf5_cmakedir}/DigikamGui/
%{_kf5_cmakedir}/DigikamPlugin/
%{_kf5_libdir}/libdigikamcore.so
%{_kf5_libdir}/libdigikamdatabase.so
%{_kf5_libdir}/libdigikamgui.so

%files -n showfoto
%{_kf5_applicationsdir}/org.kde.showfoto.desktop
%{_kf5_appstreamdir}/org.kde.showfoto.appdata.xml
%{_kf5_bindir}/showfoto
%{_kf5_iconsdir}/hicolor/*/apps/showfoto.*
%{_kf5_kxmlguidir}/showfoto/
%{_kf5_sharedir}/showfoto/

%files -n libdigikamcore%{soversion}
%license LICENSES/*
%{_kf5_libdir}/libdigikamcore.so.%{version}
%{_kf5_libdir}/libdigikamdatabase.so.%{version}
%{_kf5_libdir}/libdigikamgui.so.%{version}

%files lang -f %{name}.lang

%changelog
