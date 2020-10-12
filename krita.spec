#
# spec file for package krita
#
# Copyright (c) 2020 SUSE LLC
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


%bcond_without lang
# Enable VC only on x86*
%ifarch %{ix86} x86_64
%bcond_without vc
%else
%bcond_with vc
%endif
Name:           krita
Version:        4.3.0
Release:        0
Summary:        Digital Painting Application
License:        GPL-2.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND GPL-3.0-or-later AND BSD-2-Clause AND CC0-1.0 AND LGPL-2.0-only
Group:          Productivity/Graphics/Bitmap Editors
URL:            https://www.krita.org/
Source0:        https://download.kde.org/stable/krita/%{version}/krita-%{version}.tar.xz
# PATCH-FIX-UPSTREAM
Patch0:         Support-quazip-1.0.patch
%ifnarch %{arm} aarch64
# causes build failure on ARM currently
BuildRequires:  OpenColorIO-devel
%endif
BuildRequires:  OpenEXR-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  fftw3-devel
BuildRequires:  giflib-devel
BuildRequires:  gsl-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libeigen3-devel
BuildRequires:  libexiv2-devel
BuildRequires:  libjpeg-devel
BuildRequires:  liblcms2-devel
BuildRequires:  libpng-devel
BuildRequires:  libpoppler-qt5-devel
BuildRequires:  libquazip-qt5-devel
BuildRequires:  libraw-devel
BuildRequires:  libtiff-devel
BuildRequires:  openjpeg2-devel
BuildRequires:  perl
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  python3-qt5-devel
BuildRequires:  python3-sip-devel
BuildRequires:  update-desktop-files
BuildRequires:  zlib-devel
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5Completion)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5ItemModels)
BuildRequires:  cmake(KF5ItemViews)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Core) >= 5.9
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Multimedia)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  pkgconfig(xcb-atom)
BuildRequires:  pkgconfig(xi) >= 1.4.99.1
Recommends:     %{name}-lang = %{version}
Recommends:     python3-qt5
Obsoletes:      calligra-krita < %{version}
Provides:       calligra-krita = %{version}
%if %{with vc}
BuildRequires:  Vc-devel-static
%endif

%description
Krita is a painting program. It supports concept art, texture and
matte painters, as well as illustrations and comics.

%package devel
Summary:        Krita Build Environment
Group:          Development/Libraries/KDE
Requires:       %{name} = %{version}

%description devel
Development headers and libraries for Krita.

%lang_package

%prep
%setup -q
%autopatch -p1

%build
%ifarch %{arm} aarch64
# workaround to avoid build failure on ARM, see https://bugs.kde.org/show_bug.cgi?id=421136
export CXXFLAGS="%{optflags} -DHAS_ONLY_OPENGL_ES"
%endif
# install translations to %%{_kf5_localedir} so they don't clash with the krita translations in calligra-l10n (KDE4 based)
# can probably be changed back to the standard location when calligra is KF5 based...
%cmake_kf5 -d build -- -DCMAKE_INSTALL_LOCALEDIR=%{_kf5_localedir}
%make_jobs

%install
%kf5_makeinstall -C build
%suse_update_desktop_file -r org.kde.krita      Qt KDE Graphics RasterGraphics
%if %{with lang}
%kf5_find_lang %{name}
%endif

chmod -x %{buildroot}/%{_kf5_applicationsdir}/*.desktop

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING*
%doc AUTHORS HACKING README*
%{_kf5_bindir}/krita
%{_kf5_bindir}/kritarunner
%{_kf5_applicationsdir}/*.desktop
%{_kf5_sharedir}/krita/
%{_kf5_appstreamdir}/
%{_kf5_libdir}/libkrita*.so.*
%{_kf5_libdir}/kritaplugins/
%{_kf5_libdir}/krita-python-libs/
%{_kf5_qmldir}
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

%if %{with lang}
%files lang -f %{name}.lang
%endif

%changelog
