#
# spec file
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2015 Bjørn Lie, Bryne, Norway.
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == ""
ExclusiveArch:  do_not_build
%endif
%if "%{flavor}" == "qt5"
  %define qt5 1
  %define qt_min_version 5.15.2
  %define _plugindir %{_libqt5_plugindir}
  %define _suffix %{nil}
%endif
%if "%{flavor}" == "qt6"
  %define qt6 1
  %define qt_min_version 6.2.0
  %define _plugindir %{_qt6_pluginsdir}
  %define _suffix 6
%endif
%define sover 1
Name:           adwaita-qt%{?_suffix}%{?_suffix:-src}
Version:        1.4.2
Release:        0
Summary:        Adwaita theme for Qt-based applications
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://github.com/FedoraQt/adwaita-qt
Source0:        %{url}/archive/%{version}/adwaita-qt-%{version}.tar.gz
BuildRequires:  cmake >= 3.17
BuildRequires:  fdupes
BuildRequires:  pkgconfig
%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150400
BuildRequires:  extra-cmake-modules
%else
BuildRequires:  gcc-c++
%endif
%if 0%{?qt5}
BuildRequires:  cmake(Qt5Core) >= %{qt_min_version}
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  pkgconfig(xcb) >= 1.10
Requires:       adwaita-%{flavor}
Obsoletes:      adwaita-qt4 < 1.2.0
%endif
%if 0%{?qt6}
BuildRequires:  cmake(Qt6Core) >= %{qt_min_version}
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
Requires:       adwaita-%{flavor}
%endif

%description
Theme to let Qt applications fit nicely into GNOME desktop.

%package -n adwaita-%{flavor}
Requires:       libadwaita%{flavor}-%{sover} = %{version}-%{release}
%if 0%{?qt5}
Summary:        Adwaita Qt5 theme
%endif
%if 0%{?qt6}
Summary:        Adwaita Qt6 theme
%endif
%if 0%{?qt5}
Supplements:    (libQt5Core5 and gnome-session)
%endif
%if 0%{?qt6}
Supplements:    (libQt6Core6 and gnome-session)
%endif

%description -n adwaita-%{flavor}
%if 0%{?qt5}
Adwaita theme variant for applications utilizing Qt5
%endif
%if 0%{?qt6}
Adwaita theme variant for applications utilizing Qt6
%endif

%package -n libadwaita%{flavor}-%{sover}
%if 0%{?qt5}
Summary:        Adwaita Qt5 library
# The package was wwronlgy called  libadwaitaqt1_2_0 in the past
# As long as we are at .so.1, we can obsolete this old, wrong
# package name
Obsoletes:      libadwaitaqt1_2_0
Obsoletes:      libadwaitaqt%{sover} <= 1.4.0
Provides:       libadwaitaqt%{sover} = %{version}
%endif
%if 0%{?qt6}
Summary:        Adwaita Qt6 library
%endif

%description -n libadwaita%{flavor}-%{sover}
%if 0%{?qt5}
Adwaita theme variant for applications utilizing Qt5
%endif
%if 0%{?qt6}
Adwaita theme variant for applications utilizing Qt6
%endif

%package -n libadwaita-%{flavor}-devel
Summary:        Development files for libadwaita-%{flavor}
Requires:       libadwaita%{flavor}-%{sover} = %{version}
%if 0%{?qt5}
Obsoletes:      libadwaitaqt-devel <= 1.4.0
Provides:       libadwaitaqt-devel = %{version}
%endif
%if 0%{?qt6}
Requires:       cmake(Qt6Core)
Requires:       cmake(Qt6Widgets)
%endif

%description -n libadwaita-%{flavor}-devel
The libadwaita-%{flavor}-devel package contains libraries and header files for
developing applications that use libadwaita-%{flavor}-%{sover}.

%prep
%autosetup -p1 -n adwaita-qt-%{version}

%build

%if 0%{?qt5}
%cmake \
  -DUSE_QT6=false \
%endif
%if 0%{?qt6}
%cmake_qt6 \
  -DUSE_QT6=true \
%endif

%if 0%{?qt6}
%{qt6_build}
%else
%cmake_build
%endif

%install

%if 0%{?qt6}
%{qt6_install}
%else
%cmake_install
%endif

# qt6 does not have a pc file, so the generated pc we have is invalid, nuke it.
rm -rf %{buildroot}%{_libdir}/pkgconfig/adwaita-qt6.pc

%ldconfig_scriptlets -n libadwaita%{flavor}-%{sover}

%files -n adwaita-%{flavor}
%license LICENSE.LGPL2
%doc README.md
%dir %{_plugindir}/styles
%{_plugindir}/styles/adwaita.so

%files -n libadwaita%{flavor}-%{sover}
%{_libdir}/libadwaitaqt%{_suffix}.so.*
%{_libdir}/libadwaitaqt%{_suffix}priv.so.*

%files -n libadwaita-%{flavor}-devel
%dir %{_includedir}/AdwaitaQt%{_suffix}
%{_includedir}/AdwaitaQt%{_suffix}/*.h
%dir %{_libdir}/cmake/AdwaitaQt%{_suffix}
%{_libdir}/cmake/AdwaitaQt%{_suffix}/*.cmake
%if 0%{?qt5}
%{_libdir}/pkgconfig/adwaita-qt%{_suffix}.pc
%endif
%{_libdir}/libadwaitaqt%{_suffix}.so
%{_libdir}/libadwaitaqt%{_suffix}priv.so

%changelog
