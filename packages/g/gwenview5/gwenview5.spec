#
# spec file for package gwenview5
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


%define rname gwenview
%define kf5_version 5.43.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           gwenview5
Version:        20.08.1
Release:        0
Summary:        Image Viewer by KDE
License:        GPL-2.0-or-later
Group:          Productivity/Graphics/Viewers
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz
BuildRequires:  cfitsio-devel
BuildRequires:  extra-cmake-modules >= %{kf5_version}
BuildRequires:  kf5-filesystem
BuildRequires:  libexiv2-devel
BuildRequires:  libjpeg-devel
BuildRequires:  liblcms2-devel
BuildRequires:  libpng-devel
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Activities)
BuildRequires:  cmake(KF5Baloo)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5ItemModels)
BuildRequires:  cmake(KF5KDcraw)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Kipi)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5Parts)
BuildRequires:  cmake(KF5Purpose)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(Phonon4Qt5)
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5OpenGL)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5X11Extras)
Recommends:     %{name}-lang
Provides:       gwenview = %{version}
Obsoletes:      gwenview < %{version}
%if %{with lang}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif

%description
Gwenview is an image viewer for KDE. It features a folder tree
window and a file list window, providing navigation of file
hierarchies.

%lang_package

%prep
%setup -q -n %{rname}-%{version}

%build
%cmake_kf5 -d build -- -DGWENVIEW_SEMANTICINFO_BACKEND="Baloo"
%cmake_build

%install
%kf5_makeinstall -C build
%if %{with lang}
  %find_lang %{name} --with-man --all-name
  %{kf5_find_htmldocs}
%endif

%suse_update_desktop_file -r org.kde.gwenview       Graphics RasterGraphics Viewer KDE

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING*
%dir %{_datadir}/solid
%dir %{_datadir}/solid/actions
%dir %{_kf5_htmldir}
%dir %{_kf5_htmldir}/en
%doc %lang(en) %{_kf5_htmldir}/en/*/
%{_kf5_applicationsdir}/org.kde.gwenview.desktop
%{_kf5_appstreamdir}/
%{_kf5_bindir}/gwenview
%{_kf5_bindir}/gwenview_importer
%{_kf5_debugdir}/gwenview.categories
%{_kf5_iconsdir}/hicolor/*/*/*
%{_kf5_libdir}/libgwenviewlib.so.*
%{_kf5_plugindir}/
%{_kf5_servicesdir}/
%{_kf5_sharedir}/gwenview/
%{_kf5_sharedir}/kxmlgui5/
%{_kf5_sharedir}/solid/actions/gwenview_*.desktop
%dir %{_kf5_sharedir}/kconf_update/
%{_kf5_sharedir}/kconf_update/gwenview.upd
%{_kf5_sharedir}/kconf_update/gwenview-imageview-alphabackgroundmode-update.pl

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
