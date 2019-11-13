#
# spec file for package palapeli
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define kf5_version 5.26.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without	lang
Name:           palapeli
Version:        19.08.3
Release:        0
Summary:        Jigsaw puzzle game
License:        GPL-2.0-or-later
Group:          Amusements/Games/Board/Puzzle
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  karchive-devel
BuildRequires:  kconfig-devel
BuildRequires:  kconfigwidgets-devel
BuildRequires:  kcoreaddons-devel
BuildRequires:  kcrash-devel
BuildRequires:  kdelibs4support-devel
BuildRequires:  kdoctools-devel
BuildRequires:  ki18n-devel
BuildRequires:  kio-devel
BuildRequires:  kitemviews-devel
BuildRequires:  knotifications-devel
BuildRequires:  kservice-devel
BuildRequires:  kwidgetsaddons-devel
BuildRequires:  kxmlgui-devel
BuildRequires:  libkdegames-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
Requires:       palapeli-data = %{version}
Requires(post): shared-mime-info
Requires(postun): shared-mime-info
%if %{with lang}
Recommends:     %{name}-lang
%endif

%description
Palapeli is a jigsaw puzzle game. Unlike other games in that genre, you are not
limited to aligning pieces on imaginary grids. The pieces are freely moveable.
Also, Palapeli features real persistency, i.e. everything you do is saved on
your disk immediately.

%package data
Summary:        Palapeli's standard puzzle files
Group:          System/GUI/KDE
Requires:       palapeli = %{version}
BuildArch:      noarch

%description data
This package contains the standard puzzle files for Palapeli.

%package devel
Summary:        Development package for Palapeli
Group:          Development/Libraries/KDE
Requires:       palapeli = %{version}

%description devel
This package contains the development files for Palapeli.

%if %{with lang}
%lang_package
%endif

%prep
%setup -q

%build
  %cmake_kf5 -d build
  %make_jobs

%install
  %kf5_makeinstall -C build
%if %{with lang}
  %find_lang %{name} --with-man --all-name
  %{kf5_find_htmldocs}
%endif
  %suse_update_desktop_file -r org.kde.palapeli          Game BoardGame

%post
/sbin/ldconfig
%mime_database_post

%postun
/sbin/ldconfig
%mime_database_postun

%files
%license COPYING*
%dir %{_kf5_iconsdir}/hicolor/16x16
%dir %{_kf5_iconsdir}/hicolor/16x16/apps
%dir %{_kf5_iconsdir}/hicolor/16x16/mimetypes
%dir %{_kf5_iconsdir}/hicolor/24x24
%dir %{_kf5_iconsdir}/hicolor/24x24/apps
%dir %{_kf5_iconsdir}/hicolor/24x24/mimetypes
%dir %{_kf5_iconsdir}/hicolor/32x32
%dir %{_kf5_iconsdir}/hicolor/32x32/apps
%dir %{_kf5_iconsdir}/hicolor/32x32/mimetypes
%dir %{_kf5_iconsdir}/hicolor/64x64
%dir %{_kf5_iconsdir}/hicolor/64x64/apps
%dir %{_kf5_iconsdir}/hicolor/64x64/mimetypes
%dir %{_kf5_iconsdir}/hicolor/128x128/
%dir %{_kf5_iconsdir}/hicolor/128x128/apps
%dir %{_kf5_iconsdir}/hicolor/128x128/mimetypes/
%{_kf5_iconsdir}/hicolor/*/apps/palapeli.png
%{_kf5_iconsdir}/hicolor/*/mimetypes/application-x-palapeli.png
%dir %{_kf5_servicesdir}/ServiceMenus
%doc %lang(en) %{_kf5_htmldir}/en/palapeli/
%{_kf5_applicationsdir}/org.kde.palapeli.desktop
%{_kf5_appstreamdir}/org.kde.palapeli.appdata.xml
%{_kf5_bindir}/palapeli
%{_kf5_kxmlguidir}/palapeli/
%{_kf5_libdir}/libpala.so.*
%{_kf5_notifydir}/palapeli.notifyrc
%{_kf5_plugindir}/pala*
%{_kf5_servicesdir}/ServiceMenus/palapeli_servicemenu.desktop
%{_kf5_servicesdir}/palapeli_goldbergslicer.desktop
%{_kf5_servicesdir}/palapeli_jigsawslicer.desktop
%{_kf5_servicesdir}/palapeli_rectslicer.desktop
%{_kf5_servicesdir}/palathumbcreator.desktop
%{_kf5_servicetypesdir}/libpala-slicerplugin.desktop
%{_kf5_sharedir}/mime/packages/palapeli-mimetypes.xml
%{_kf5_debugdir}/palapeli.categories

%files data
%license COPYING*
%{_kf5_appsdir}/palapeli/
%config %{_kf5_configdir}/palapeli-collectionrc

%files devel
%license COPYING*
%{_includedir}/Pala
%{_includedir}/libpala
%{_kf5_libdir}/libpala.so
%{_kf5_libdir}/libpala/

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
