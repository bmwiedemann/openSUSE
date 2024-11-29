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


%define kf6_version 6.0.0
%define qt6_version 6.4.0

%define soversion 8_5_0
%bcond_without released
%bcond_with    apidocs
Name:           digikam
Version:        8.5.0
Release:        0
Summary:        A KDE Photo Manager
License:        GPL-2.0-or-later
URL:            https://www.digikam.org/
Source0:        https://download.kde.org/stable/digikam/%{version}/digiKam-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/digikam/%{version}/digiKam-%{version}.tar.xz.sig
Source2:        digikam.keyring
%endif
BuildRequires:  bison
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  hicolor-icon-theme
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  lensfun
BuildRequires:  libboost_graph-devel
BuildRequires:  libeigen3-devel
BuildRequires:  libexiv2-devel >= 0.27.1
BuildRequires:  libtiff-devel
BuildRequires:  opencv-devel
BuildRequires:  pkgconfig
BuildRequires:  qt6-gui-private-devel >= %{qt6_version}
BuildRequires:  cmake(KF6CalendarCore) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6Contacts) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6FileMetaData) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6NotifyConfig) >= %{kf6_version}
BuildRequires:  cmake(KF6Service) >= %{kf6_version}
BuildRequires:  cmake(KF6Solid) >= %{kf6_version}
BuildRequires:  cmake(KF6Sonnet) >= %{kf6_version}
BuildRequires:  cmake(KF6ThreadWeaver) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(KPim6Akonadi)
BuildRequires:  cmake(KPim6AkonadiContactCore)
BuildRequires:  cmake(KSaneWidgets6)
BuildRequires:  cmake(Qt6Concurrent) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Multimedia) >= %{qt6_version}
BuildRequires:  cmake(Qt6MultimediaWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6NetworkAuth) >= %{qt6_version}
BuildRequires:  cmake(Qt6OpenGL) >= %{qt6_version}
BuildRequires:  cmake(Qt6OpenGLWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6PrintSupport) >= %{qt6_version}
BuildRequires:  cmake(Qt6Sql) >= %{qt6_version}
BuildRequires:  cmake(Qt6StateMachine) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6SvgWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6WebEngineWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Xml) >= %{qt6_version}
BuildRequires:  cmake(libheif)
BuildRequires:  pkgconfig(Magick++)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(gl)
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
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(libswresample)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(vdpau)
%if %{with apidocs}
BuildRequires:  doxygen
BuildRequires:  graphviz-devel
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
%endif
Requires:       digikam-plugins
Requires:       qt6-sql-sqlite >= %{qt6_version}
Recommends:     marble
Recommends:     showfoto
# Got merged into libimageeditor in 5.2.0
Provides:       digikam-plugin-color = %{version}
Obsoletes:      digikam-plugin-color < %{version}
Provides:       digikam-plugin-decorate = %{version}
Obsoletes:      digikam-plugin-decorate < %{version}
Provides:       digikam-plugin-enhance = %{version}
Obsoletes:      digikam-plugin-enhance < %{version}
Provides:       digikam-plugin-fxfilters = %{version}
Obsoletes:      digikam-plugin-fxfilters < %{version}
Provides:       digikam-plugin-transform = %{version}
Obsoletes:      digikam-plugin-transform < %{version}
Obsoletes:      digikam-libs < %{version}
# Docs no longer included in 6.0.0
Provides:       digikam-doc = %{version}
Obsoletes:      digikam-doc < %{version}
# QtWebEngine is not available on ppc and zSystems
ExclusiveArch:  aarch64 x86_64 %{x86_64} riscv64

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
Supplements:    digikam

%description -n showfoto
Additional program to browse and view photos

%package -n libdigikamcore%{soversion}
Summary:        The main digikam libraries
Recommends:     digikam-plugins

%description -n libdigikamcore%{soversion}
The main digikam libraries that are being shared between showfoto and digikam

%lang_package

%prep
%autosetup -p1 -n digikam-%{version}

%build
%cmake_kf6 \
  -DBUILD_WITH_QT6:BOOL=TRUE \
  -DENABLE_AKONADICONTACTSUPPORT:BOOL=TRUE \
  -DENABLE_APPSTYLES:BOOL=TRUE \
  -DENABLE_KFILEMETADATASUPPORT:BOOL=TRUE \
  -DENABLE_MEDIAPLAYER:BOOL=TRUE \
  -DSSE3_FOUND:BOOL=FALSE \
  -DSSE4_1_FOUND:BOOL=FALSE \
  -DSSE4_2_FOUND:BOOL=FALSE \
  -DSSSE3_FOUND:BOOL=FALSE \
%ifarch x86_64 %{?x86_64}
  -DSSE2_FOUND:BOOL=TRUE
%else
  -DSSE2_FOUND:BOOL=FALSE
%endif

%kf6_build

%if %{with apidocs}
%kf6_build doc
%endif

%install
%kf6_install

%find_lang %{name} --without-kde

%fdupes %{buildroot}

%ldconfig_scriptlets -n libdigikamcore%{soversion}

%files
%doc AUTHORS NEWS README.md
%doc %{_kf6_mandir}/man1/cleanup_digikamdb.1%{ext_man}
%doc %{_kf6_mandir}/man1/digitaglinktree.1%{ext_man}
%{_kf6_applicationsdir}/org.kde.digikam.desktop
%{_kf6_appstreamdir}/org.kde.digikam.appdata.xml
%{_kf6_bindir}/cleanup_digikamdb
%{_kf6_bindir}/digikam
%{_kf6_bindir}/digitaglinktree
%{_kf6_iconsdir}/hicolor/*/actions/
%{_kf6_iconsdir}/hicolor/*/apps/digikam.*
%{_kf6_kxmlguidir}/digikam/
%{_kf6_notificationsdir}/digikam.notifyrc
%{_kf6_sharedir}/digikam/
%dir %{_kf6_sharedir}/solid
%dir %{_kf6_sharedir}/solid/actions
%{_kf6_sharedir}/solid/actions/digikam-opencamera.desktop

%files plugins
%{_kf6_iconsdir}/hicolor/*/apps/dk-*
%{_kf6_iconsdir}/hicolor/*/apps/expoblending.*
%{_kf6_iconsdir}/hicolor/*/apps/panorama.*
%{_kf6_plugindir}/digikam/

%files devel
%{_includedir}/digikam/
%{_kf6_cmakedir}/DigikamCore/
%{_kf6_cmakedir}/DigikamDatabase/
%{_kf6_cmakedir}/DigikamGui/
%{_kf6_cmakedir}/DigikamPlugin/
%{_kf6_libdir}/libdigikamcore.so
%{_kf6_libdir}/libdigikamdatabase.so
%{_kf6_libdir}/libdigikamgui.so

%files -n showfoto
%{_kf6_applicationsdir}/org.kde.showfoto.desktop
%{_kf6_appstreamdir}/org.kde.showfoto.appdata.xml
%{_kf6_bindir}/showfoto
%{_kf6_iconsdir}/hicolor/*/apps/showfoto.*
%{_kf6_kxmlguidir}/showfoto/
%{_kf6_sharedir}/showfoto/

%files -n libdigikamcore%{soversion}
%license LICENSES/*
%{_kf6_libdir}/libdigikamcore.so.*
%{_kf6_libdir}/libdigikamdatabase.so.*
%{_kf6_libdir}/libdigikamgui.so.*

%files lang -f %{name}.lang

%changelog
