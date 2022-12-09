#
# spec file for package digikam
#
# Copyright (c) 2022 SUSE LLC
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


%define soversion 7_9_0
%bcond_without released
%bcond_with    apidocs
Name:           digikam
Version:        7.9.0
Release:        0
Summary:        A KDE Photo Manager
License:        GPL-2.0-or-later
Group:          Productivity/Graphics/Viewers
URL:            https://www.digikam.org/
Source0:        https://download.kde.org/stable/%{name}/%{version}/digiKam-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/%{name}/%{version}/digiKam-%{version}.tar.xz.sig
Source2:        %{name}.keyring
%endif
# PATCH-FIX-OPENSUSE -- Lower minimum exiv2 version to 0.26
Patch0:         0001-Revert-Exiv2-is-now-released-with-exported-targets-u.patch
# QtWebEngine is not available on ppc and zSystems
ExclusiveArch:  %{arm} aarch64 %{ix86} x86_64 %{mips} %{riscv}
BuildRequires:  QtAV-devel >= 1.12
BuildRequires:  bison
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  hicolor-icon-theme
BuildRequires:  lensfun
BuildRequires:  lensfun-devel
BuildRequires:  libboost_graph-devel
BuildRequires:  libeigen3-devel
BuildRequires:  libexiv2-devel >= 0.26
BuildRequires:  libexpat-devel
BuildRequires:  libjasper-devel
BuildRequires:  libjpeg8-devel
BuildRequires:  liblcms2-devel
BuildRequires:  liblqr-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
BuildRequires:  opencv-devel >= 3.4.0
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
%if %{with apidocs}
BuildRequires:  doxygen
BuildRequires:  graphviz-devel
BuildRequires:  cmake(KF5DocTools)
%endif
BuildRequires:  cmake(KF5AkonadiContact)
BuildRequires:  cmake(KF5CalendarCore)
BuildRequires:  cmake(KF5Config)
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
BuildRequires:  cmake(KF5ThreadWeaver) >= 5.5.0
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Marble)
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Core) >= 5.9.0
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5OpenGL)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5WebEngineWidgets)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  cmake(Qt5XmlPatterns)
BuildRequires:  cmake(libheif)
BuildRequires:  pkgconfig(Magick++)
%if 0%{suse_version} >= 1550
BuildRequires:  ffmpeg-4-libavcodec-devel
BuildRequires:  ffmpeg-4-libavdevice-devel
BuildRequires:  ffmpeg-4-libavfilter-devel
BuildRequires:  ffmpeg-4-libavformat-devel
BuildRequires:  ffmpeg-4-libavutil-devel
%else
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
%endif
BuildRequires:  pkgconfig(libgphoto2) >= 2.4.0
BuildRequires:  pkgconfig(libswscale)
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
Group:          Productivity/Graphics/Viewers
Recommends:     enblend-enfuse
Recommends:     hugin

%description plugins
Additional plugins for digiKam.

%package devel
Summary:        DigiKam development files
Group:          Development/Libraries/KDE
Requires:       libdigikamcore%{soversion} = %{version}

%description devel
Development headers and libraries for digiKam.

%package -n showfoto
Summary:        DigiKam: Showfoto
Group:          Productivity/Graphics/Viewers
Supplements:    %{name}

%description -n showfoto
Additional program to browse and view photos

%package -n libdigikamcore%{soversion}
Summary:        The main digikam libraries
Group:          Development/Libraries/KDE
Recommends:     %{name}-plugins

%description -n libdigikamcore%{soversion}
The main digikam libraries that are being shared between showfoto and digikam

%lang_package

%prep
%setup -q
%if 0%{?suse_version} <= 1500
# Leap 15 only has exiv2 0.26
%patch0 -p1
%endif

%build
%cmake_kf5 -d build -- -DENABLE_APPSTYLES=ON -DENABLE_MEDIAPLAYER=ON -DENABLE_KFILEMETADATASUPPORT=ON -DENABLE_AKONADICONTACTSUPPORT=ON
%cmake_build

%if %{with apidocs}
%cmake_build doc
%endif

%install
%kf5_makeinstall -C build

%if 0%{?suse_version}
%suse_update_desktop_file -r org.kde.digikam Qt KDE Graphics Photography
%suse_update_desktop_file -r org.kde.showfoto Qt KDE Graphics Photography
%endif

%if %{with released}
%find_lang %{name} --without-kde
%endif

%fdupes %{buildroot}

%post -n libdigikamcore%{soversion} -p /sbin/ldconfig
%postun -n libdigikamcore%{soversion} -p /sbin/ldconfig

%files
%{_kf5_bindir}/digikam
%{_kf5_bindir}/digitaglinktree
%{_kf5_bindir}/cleanup_digikamdb
%{_kf5_applicationsdir}/org.kde.digikam.desktop
%{_kf5_iconsdir}/hicolor/*/actions/
%{_kf5_iconsdir}/hicolor/*/apps/digikam.*
%doc %{_kf5_mandir}/man1/cleanup_digikamdb.1%{ext_man}
%doc %{_kf5_mandir}/man1/digitaglinktree.1%{ext_man}
%{_kf5_sharedir}/digikam/
%dir %{_kf5_sharedir}/solid
%dir %{_kf5_sharedir}/solid/actions
%{_kf5_sharedir}/solid/actions/digikam-opencamera.desktop
%{_kf5_kxmlguidir}/digikam/
%{_kf5_notifydir}/digikam.notifyrc
%{_kf5_appstreamdir}/org.kde.digikam.appdata.xml
%doc AUTHORS NEWS README.md

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
%{_kf5_bindir}/showfoto
%{_kf5_applicationsdir}/org.kde.showfoto.desktop
%{_kf5_iconsdir}/hicolor/*/apps/showfoto.*
%{_kf5_sharedir}/showfoto/
%{_kf5_kxmlguidir}/showfoto/
%{_kf5_appstreamdir}/org.kde.showfoto.appdata.xml

%files -n libdigikamcore%{soversion}
%license COPYING*
%{_kf5_libdir}/libdigikamcore.so.7.9.0
%{_kf5_libdir}/libdigikamdatabase.so.7.9.0
%{_kf5_libdir}/libdigikamgui.so.7.9.0

%if %{with released}
%files lang -f %{name}.lang
%endif

%changelog
