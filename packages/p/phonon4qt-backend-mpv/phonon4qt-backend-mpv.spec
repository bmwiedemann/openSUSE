#
# spec file for package phonon4qt-backend-mpv
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

%global _p4bm_flavor @BUILD_FLAVOR@%{nil}
%if "%{_p4bm_flavor}" == ""
ExclusiveArch:  do_not_build
%endif
%if "%{_p4bm_flavor}" == "qt5"
%define qt5_package 1
%define pkg_suffix 5
%define qt_descr Qt5
%define _p4qt_version 4.11
%endif
%if "%{_p4bm_flavor}" == "qt6"
%define qt6_package 1
%define pkg_suffix 6
%define qt_descr Qt6
%define _p4qt_version 4.10.60
%endif

Name:           phonon4qt%{?pkg_suffix}-backend-mpv
Version:        0.1.0
Release:        0
Summary:        %{qt_descr} Phonon Backend using MPV Player(libmpv)
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://github.com/OpenProgger/phonon-mpv
Source0:        https://github.com/OpenProgger/phonon-mpv/archive/v%{version}.tar.gz#/phonon-mpv-%{version}.tar.gz
BuildRequires:  cmake >= 3.5
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(mpv) >= 1.101.0
BuildRequires:  pkgconfig(phonon4qt%{pkg_suffix}) >= %{_p4qt_version}
%if 0%{?qt5_package}
BuildRequires:  extra-cmake-modules >= 5.90
BuildRequires:  kf5-filesystem
BuildRequires:  libQt5Gui-private-headers-devel
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5X11Extras)
%endif
%if 0%{?qt6_package}
BuildRequires:  kf6-extra-cmake-modules
BuildRequires:  pkgconfig(xcb-atom)
BuildRequires:  pkgconfig(xcb-aux)
BuildRequires:  pkgconfig(xcb-cursor)
BuildRequires:  pkgconfig(xcb-event)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  cmake(Qt6OpenGLWidgets)
BuildRequires:  cmake(Qt6XcbQpaPrivate)
%endif
Requires:       libphonon4qt%{pkg_suffix} >= %{_p4qt_version}
Provides:       phonon4qt%{pkg_suffix}-backend = %{version}

%description
This is a fork of phonon-vlc, rewritten to work with libmpv instead of
libVLC. libmpv supports less features than VLC but they are only
related to memory streams and audio/video dumps. This backend should be
a lightweight alternative to libVLC with less dependencies.

%prep
%autosetup -n phonon-mpv-%{version}

%build
%if 0%{?qt5_package}
%cmake_kf5
%cmake_build
%endif

%if 0%{?qt6_package}
%cmake_kf6 \
  -DPHONON_BUILD_QT5=OFF \
  -DPHONON_BUILD_QT6=ON
%kf6_build
%endif

%install
%if 0%{?qt5_package}
%kf5_makeinstall
%endif
%if 0%{?qt6_package}
%kf6_install
%endif

%check

%files
%license COPYING.LIB
%doc README.md
%if 0%{?qt5_package}
%dir %{_kf5_plugindir}/phonon4qt5_backend
%{_kf5_plugindir}/phonon4qt5_backend/phonon_mpv_qt5.so
%endif
%if 0%{?qt6_package}
%dir %{_kf6_plugindir}/phonon4qt6_backend
%{_kf6_plugindir}/phonon4qt6_backend/phonon_mpv_qt6.so
%endif

%changelog
