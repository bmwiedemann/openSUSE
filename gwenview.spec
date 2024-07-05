#
# spec file for package gwenview
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
%define plasma6_version 5.27.80
%define qt6_version 6.6.0

%bcond_without released
Name:           gwenview
Version:        24.05.2
Release:        0
Summary:        Image Viewer by KDE
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/gwenview
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  cfitsio-devel
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  libjpeg-devel
BuildRequires:  liblcms2-devel
BuildRequires:  libpng-devel
BuildRequires:  pkgconfig
BuildRequires:  qt6-gui-private-devel >= %{qt6_version}
BuildRequires:  cmake(KF6Baloo) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6ItemModels) >= %{kf6_version}
BuildRequires:  cmake(KDcrawQt6)
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6Parts) >= %{kf6_version}
BuildRequires:  cmake(KF6Purpose) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(Phonon4Qt6)
BuildRequires:  cmake(PlasmaActivities) >= %{plasma6_version}
BuildRequires:  cmake(Qt6Concurrent) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6OpenGLWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6PrintSupport) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6SvgWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6WaylandClient) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(exiv2)
BuildRequires:  cmake(kImageAnnotator-Qt6)
BuildRequires:  cmake(kColorPicker-Qt6)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(x11)
Provides:       gwenview5 = %{version}
Obsoletes:      gwenview5 < %{version}
Obsoletes:      gwenview5-lang < %{version}

%description
Gwenview is an image viewer by KDE. It features a folder tree window and a file
list window, providing navigation of file hierarchies.

%lang_package

%prep
%autosetup -p1


%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-man --with-html --all-name

%ldconfig_scriptlets

%files
%license COPYING*
%doc %lang(en) %{_kf6_htmldir}/en/gwenview/
%{_kf6_applicationsdir}/org.kde.gwenview.desktop
%{_kf6_applicationsdir}/org.kde.gwenview_importer.desktop
%{_kf6_appstreamdir}/org.kde.gwenview.appdata.xml
%{_kf6_bindir}/gwenview
%{_kf6_bindir}/gwenview_importer
%{_kf6_debugdir}/gwenview.categories
%{_kf6_iconsdir}/hicolor/*/*/*
%{_kf6_libdir}/libgwenviewlib.so.*
%dir %{_kf6_plugindir}/kf6/kfileitemaction
%{_kf6_plugindir}/kf6/kfileitemaction/slideshowfileitemaction.so
%{_kf6_plugindir}/kf6/parts/gvpart.so
%{_kf6_sharedir}/gwenview/
%dir %{_kf6_sharedir}/solid
%dir %{_kf6_sharedir}/solid/actions
%{_kf6_sharedir}/solid/actions/gwenview_importer.desktop
%{_kf6_sharedir}/solid/actions/gwenview_importer_camera.desktop

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/gwenview/

%changelog
