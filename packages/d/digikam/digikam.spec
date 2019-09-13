#
# spec file for package digikam
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define soversion 6
%bcond_without lang
Name:           digikam
Version:        6.2.0
Release:        0
Summary:        A KDE Photo Manager
License:        GPL-2.0-or-later
Group:          Productivity/Graphics/Viewers
URL:            http://www.digikam.org/
Source0:        http://download.kde.org/stable/%{name}/%{version}/%{name}-%{version}.tar.xz
# PATCH-FIX-OPENSUSE 0001-Disable-detection-of-OpenGL-for-GLES-platforms.patch -- The OpenGL slideshow depends on Desktop GL, see kde#383715
Patch0:         0001-Disable-detection-of-OpenGL-for-GLES-platforms.patch
BuildRequires:  QtAV-devel >= 1.12
BuildRequires:  bison
BuildRequires:  boost-devel
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  graphviz-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  kconfig-devel
BuildRequires:  kcoreaddons-devel
BuildRequires:  kdoctools-devel
BuildRequires:  kfilemetadata5-devel
BuildRequires:  ki18n-devel
BuildRequires:  kiconthemes-devel
BuildRequires:  kio-devel
BuildRequires:  knotifications-devel
BuildRequires:  knotifyconfig-devel
BuildRequires:  kservice-devel
BuildRequires:  kwindowsystem-devel
BuildRequires:  kxmlgui-devel
BuildRequires:  lensfun
BuildRequires:  lensfun-devel
BuildRequires:  libeigen3-devel
BuildRequires:  libexiv2-devel >= 0.26
BuildRequires:  libexpat-devel
BuildRequires:  libjpeg8-devel
BuildRequires:  libksane-devel >= 15.12.0
BuildRequires:  liblcms2-devel
BuildRequires:  liblqr-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
BuildRequires:  marble-devel
BuildRequires:  opencv-devel
BuildRequires:  pkgconfig
BuildRequires:  solid-devel
BuildRequires:  threadweaver-devel >= 5.1.0
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5CalendarCore)
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Core) >= 5.6.0
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5OpenGL)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  cmake(Qt5XmlPatterns)
BuildRequires:  pkgconfig(Magick++)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libgphoto2) >= 2.4.0
BuildRequires:  pkgconfig(libswscale)
Requires:       %{name}-plugins
Requires:       libQt5Sql5-sqlite
Recommends:     %{name}-lang
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
#This pulls in QWebEngine, which is not available on ppc64
%ifarch %{ix86} x86_64 %{arm} aarch64 mips mips64
BuildRequires:  akonadi-contact-devel
BuildRequires:  pkgconfig(Qt5WebEngineWidgets)
%else
BuildRequires:  pkgconfig(Qt5WebKitWidgets)
%endif
%if 0%{?suse_version} < 1320
# It does not build with the default compiler (GCC 4.8) on Leap 42.x
BuildRequires:  gcc7-c++
%endif

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
%ifarch %{arm} aarch64
# Disable OpenGL slideshow on embedded platforms
%patch0 -p1
%endif

# Remove build time references so build-compare can do its work
FAKE_BUILDDATE=$(LC_ALL=C date -u -r %{_sourcedir}/%{name}.changes '+%%b %%e %%Y')
FAKE_BUILDTIME=$(LC_ALL=C date -u -r %{_sourcedir}/%{name}.changes '+%%H:%%M')
sed -i "s/__DATE__/\"$FAKE_BUILDDATE\"/" core/app/utils/digikam_version.h.cmake.in
sed -i "s/__DATE__/\"$FAKE_BUILDDATE\"/g" core/libs/dimg/filters/greycstoration/cimg/CImg.h
sed -i "s/__TIME__/\"$FAKE_BUILDTIME\"/g" core/libs/dimg/filters/greycstoration/cimg/CImg.h

%build
%if 0%{?suse_version} < 1320
# gcc 4.8.5 is too old
export CC=gcc-7
export CXX=g++-7
%endif
%ifarch %{ix86} x86_64 %{arm} aarch64 mips mips64
%cmake_kf5 -d build -- -DENABLE_APPSTYLES=ON -DENABLE_MEDIAPLAYER=ON -DENABLE_QWEBENGINE=ON
%else
%cmake_kf5 -d build -- -DENABLE_APPSTYLES=ON -DENABLE_MEDIAPLAYER=ON
%endif
%make_jobs VERBOSE=1

%install
%kf5_makeinstall -C build

%if 0%{?suse_version}
%suse_update_desktop_file -r org.kde.digikam Qt KDE Graphics Photography
%suse_update_desktop_file -r org.kde.showfoto Qt KDE Graphics Photography
%endif

%if %{with lang}
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

%files plugins
%{_kf5_iconsdir}/hicolor/*/apps/dk-*
%{_kf5_iconsdir}/hicolor/*/apps/expoblending.*
%{_kf5_iconsdir}/hicolor/*/apps/panorama.*
%{_kf5_plugindir}/digikam/

%files devel
%{_includedir}/digikam/
%{_kf5_cmakedir}/digikam/
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
%doc AUTHORS ChangeLog NEWS README.md
%{_kf5_libdir}/libdigikamcore.so.%{soversion}.*
%{_kf5_libdir}/libdigikamdatabase.so.%{soversion}.*
%{_kf5_libdir}/libdigikamgui.so.%{soversion}.*

%if %{with lang}
%files lang -f %{name}.lang
%endif

%changelog
