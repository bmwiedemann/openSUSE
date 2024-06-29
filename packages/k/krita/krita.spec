#
# spec file for package krita
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


%bcond_without released
# Build fails on x86 and powerpc with xsimd (kde#462122)
%ifnarch %{ix86} ppc64 ppc64le
%bcond_without xsimd
%endif
# Default python version is too old in Leap 15
%{?sle15_python_module_pythons}
%if 0%{?suse_version} > 1500
%define pyver python3
%else
%define pyver python311
%endif
Name:           krita
Version:        5.2.3
Release:        0
Summary:        Digital Painting Application
License:        BSD-2-Clause AND GPL-2.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND GPL-3.0-or-later AND CC0-1.0 AND LGPL-2.0-only
URL:            https://www.krita.org/
Source0:        https://download.kde.org/stable/krita/%{version}/krita-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/krita/%{version}/krita-%{version}.tar.xz.sig
Source2:        krita.keyring
%endif
# PATCH-FIX-UPSTREAM
Patch0:         0004-Fix-build-with-sip6.8.patch
BuildRequires:  %{pyver}-devel
BuildRequires:  %{pyver}-qt5-devel
BuildRequires:  %{pyver}-sip-devel
BuildRequires:  OpenEXR-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  fftw3-devel
BuildRequires:  giflib-devel
BuildRequires:  gsl-devel
%if 0%{?suse_version} > 1500
BuildRequires:  libboost_system-devel
%else
BuildRequires:  libboost_system1_75_0-devel
#!BuildIgnore:  libboost_headers1_66_0-devel
%endif
BuildRequires:  libQt5Gui-private-headers-devel
BuildRequires:  libeigen3-devel
BuildRequires:  libexiv2-devel
BuildRequires:  libheif-devel
BuildRequires:  libjpeg-devel
BuildRequires:  liblcms2-devel
BuildRequires:  libpng-devel
BuildRequires:  libpoppler-qt5-devel
BuildRequires:  libraw-devel
BuildRequires:  libtiff-devel
BuildRequires:  openjpeg2-devel
BuildRequires:  perl
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  zlib-devel
BuildRequires:  cmake(Immer)
BuildRequires:  cmake(KF5Completion)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5ItemModels)
BuildRequires:  cmake(KF5ItemViews)
BuildRequires:  cmake(KF5KDcraw)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(Lager)
BuildRequires:  cmake(Mlt7)
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5QuickWidgets)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  cmake(QuaZip-Qt5)
BuildRequires:  cmake(Zug)
BuildRequires:  cmake(kseexpr)
BuildRequires:  cmake(sdl2)
%if %{with xsimd}
BuildRequires:  cmake(xsimd)
%endif
BuildRequires:  pkgconfig(OpenColorIO)
BuildRequires:  pkgconfig(fontconfig) >= 2.13.1
BuildRequires:  pkgconfig(freetype2) >= 2.11.0
BuildRequires:  pkgconfig(fribidi) >= 1.0.6
BuildRequires:  pkgconfig(harfbuzz) >= 4.0
BuildRequires:  pkgconfig(libjxl)
BuildRequires:  pkgconfig(libmypaint)
BuildRequires:  pkgconfig(libunibreak)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(xcb-atom)
BuildRequires:  pkgconfig(xcb-xinput)
BuildRequires:  pkgconfig(xi) >= 1.4.99.1
Recommends:     %{pyver}-qt5
Recommends:     krita-plugin-gmic
Obsoletes:      calligra-krita < %{version}
Provides:       calligra-krita = %{version}

%description
Krita is a painting program. It supports concept art, texture and
matte painters, as well as illustrations and comics.

%package devel
Summary:        Krita Build Environment
Requires:       krita = %{version}
Requires:       cmake(Qt5Core)

%description devel
Development headers and libraries for Krita.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build -- -DKRITA_ENABLE_PCH:BOOL=OFF

%cmake_build

%install
%kf5_makeinstall -C build

%suse_update_desktop_file -r org.kde.krita Qt KDE Graphics RasterGraphics

%find_lang %{name}

chmod -x %{buildroot}%{_kf5_applicationsdir}/*.desktop

# remove shebang to avoid rpmlint warning, that file is not supposed to be run directly anyway
sed -i "/#!\/usr\/bin\/env/d" %{buildroot}%{_kf5_libdir}/krita-python-libs/krita/sceditor/highlighter.py

%ldconfig_scriptlets

%files
%license COPYING*
%doc AUTHORS HACKING README*
%{_kf5_bindir}/krita
%{_kf5_bindir}/krita_version
%{_kf5_bindir}/kritarunner
%{_kf5_applicationsdir}/*.desktop
%{_kf5_sharedir}/krita/
%{_kf5_appstreamdir}/
%{_kf5_libdir}/libkrita*.so.*
%{_kf5_libdir}/kritaplugins/
%{_kf5_libdir}/krita-python-libs/
%{_kf5_sharedir}/kritaplugins/
%{_kf5_sharedir}/color/
%{_kf5_sharedir}/color-schemes/
%{_kf5_iconsdir}/hicolor/*/apps/krita.*
%{_kf5_iconsdir}/hicolor/*/mimetypes/application-x-krita.png
%dir %{_kf5_iconsdir}/hicolor/1024x1024
%dir %{_kf5_iconsdir}/hicolor/1024x1024/apps
%dir %{_kf5_iconsdir}/hicolor/1024x1024/mimetypes
%dir %{_kf5_iconsdir}/hicolor/256x256
%dir %{_kf5_iconsdir}/hicolor/256x256/apps
%dir %{_kf5_iconsdir}/hicolor/256x256/mimetypes
%dir %{_kf5_iconsdir}/hicolor/512x512
%dir %{_kf5_iconsdir}/hicolor/512x512/apps
%dir %{_kf5_iconsdir}/hicolor/512x512/mimetypes
%config %{_kf5_configdir}/krita*

%files devel
%{_kf5_libdir}/libkrita*.so
%{_includedir}/kis_qmic_interface.h
%{_includedir}/kis_qmic_plugin_interface.h
%{_includedir}/kritaqmicinterface_export.h

%files lang -f %{name}.lang

%changelog
