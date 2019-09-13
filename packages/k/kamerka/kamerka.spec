#
# spec file for package kamerka
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           kamerka
Version:        0.12+git20161002
Release:        0
Summary:        Take photographs with a webcam and an animated interface
License:        GPL-2.0-or-later
Group:          System/GUI/KDE
URL:            https://dos1.github.com/kamerka
Source:         %{name}-%{version}.tar.xz
# PATCH-FIX-OPENSUSE kamerka-suse-qimageblitz.patch sor.alexei@meowr.ru
Patch0:         kamerka-suse-qimageblitz.patch
BuildRequires:  kf5-filesystem
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Declarative)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KDELibs4Support)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(Phonon4Qt5)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Script)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  pkgconfig(libv4l2)
BuildRequires:  pkgconfig(libv4lconvert)
BuildRequires:  pkgconfig(qimageblitz5)
Requires:       phonon4qt5-backend
Recommends:     %{name}-lang

%description
Kamerka is a Qt5 application using KF5 libraries. It uses
Video4Linux to get an image from the webcam and is able to save
photographs. The interface is based on QML and uses its
possibilities to show an animated UI.

%lang_package

%prep
%setup -q
%patch0 -p1

%build
%cmake_kf5 -d build
make %{?_smp_mflags} V=1

%install
%kf5_makeinstall -C build
%{kf5_post_install}

%find_lang %{name}

%if 0%{?suse_version} <= 1320
%post
%desktop_database_post

%postun
%desktop_database_postun
%endif

%files
%license COPYING
%doc AUTHORS README
%{_kf5_bindir}/kamerka
%dir %{_kf5_configkcfgdir}/
%{_kf5_configkcfgdir}/kamerka.kcfg
%{_kf5_applicationsdir}/kamerka.desktop
%dir %{_kf5_appsdir}/kamerka/
%{_kf5_appsdir}/kamerka/camera_click.ogg
%{_kf5_appsdir}/kamerka/timer.ogg
%{_kf5_notifydir}/kamerka.notifyrc
%{_kf5_prefix}/share/pixmaps/kamerka.png
%{_kf5_mandir}/man1/kamerka.1%{?ext_man}

%files lang -f %{name}.lang

%changelog
