#
# spec file for package fcitx5-qt
#
# Copyright (c) 2025 SUSE LLC
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


%if 0%{?suse_version} <= 1500 && 0%{?sle_version} <= 150200
%define build_qt4 1
%else
%define build_qt4 0
%endif
%if 0%{?suse_version} >= 1500
%define build_qt6 1
%else
%define build_qt6 0
%endif

%define build_qt5 1
Name:           fcitx5-qt
Version:        5.1.8
Release:        0
Summary:        Qt library and IM module for fcitx5
License:        BSD-3-Clause AND LGPL-2.1-or-later
Group:          System/I18n/Chinese
URL:            https://github.com/fcitx/fcitx5-qt
Source:         https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.zst
BuildRequires:  cmake >= 3.16
BuildRequires:  extra-cmake-modules
BuildRequires:  fcitx5-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libQt5Gui-private-headers-devel
BuildRequires:  pkgconfig
%if %{build_qt5}
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5X11Extras)
%endif
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xkbcommon)
%if %{build_qt4}
BuildRequires:  libqt4-devel
%endif
%if %{build_qt6}
BuildRequires:  qt6-gui-private-devel
BuildRequires:  qt6-waylandclient-private-devel
BuildRequires:  qt6-waylandglobal-private-devel
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6WaylandClient)
BuildRequires:  cmake(Qt6Widgets)
%endif
BuildRequires:  zstd

%description
Qt library and IM module for fcitx5.

%if %{build_qt4}
%package -n fcitx5-qt4
Summary:        Qt4 IM module for Fcitx5
Group:          System/I18n/Chinese
Supplements:    (fcitx5 and libqt4)
Provides:       fcitx-qt4 = %{version}
Obsoletes:      fcitx-qt4 < 5.0.0

%description -n fcitx5-qt4
Qt4 IM module for Fcitx5.

%package -n libFcitx5Qt4DBusAddons1
Summary:        Qt4 DBus Addons library for Fcitx5
Group:          System/Libraries

%description -n libFcitx5Qt4DBusAddons1
This package provides Qt4 DBus Addons library for Fcitx5.
%endif

%if %{build_qt6}
%package -n fcitx5-qt6
Summary:        Qt6 IM module for Fcitx5
Group:          System/I18n/Chinese
Supplements:    (fcitx5 and libQt6Core6)
Provides:       fcitx-qt6 = %{version}
Obsoletes:      fcitx-qt6 < 5.0.0
Requires:       %{name}-lang

%description -n fcitx5-qt6
Qt6 IM module for Fcitx5.

%package -n libFcitx5Qt6DBusAddons1
Summary:        Qt6 DBus Addons library for Fcitx5
Group:          System/Libraries

%description -n libFcitx5Qt6DBusAddons1
This package provides Qt6 DBus Addons library for Fcitx5.

%package -n libFcitx5Qt6WidgetsAddons2
Summary:        Qt6 Widgets Addons library for Fcitx5
Group:          System/Libraries

%description -n libFcitx5Qt6WidgetsAddons2
This package provides Qt6 Widgets Addons library for Fcitx5.
%endif

%if %{build_qt5}
%package -n fcitx5-qt5
Summary:        Qt5 IM module for Fcitx5
Group:          System/I18n/Chinese
Supplements:    (fcitx5 and libqt5-qtbase)
Provides:       fcitx-qt5 = %{version}
Obsoletes:      fcitx-qt5 < 5.0.0
Requires:       %{name}-lang

%description -n fcitx5-qt5
Qt5 IM module for Fcitx5.

%package -n libFcitx5Qt5DBusAddons1
Summary:        Qt5 DBus Addons library for Fcitx5
Group:          System/Libraries

%description -n libFcitx5Qt5DBusAddons1
This package provides Qt5 DBus Addons library for Fcitx5.

%package -n libFcitx5Qt5WidgetsAddons2
Summary:        Qt5 Widgets Addons library for Fcitx5
Group:          System/Libraries

%description -n libFcitx5Qt5WidgetsAddons2
This package provides Qt5 Widgets Addons library for Fcitx5.
%endif

%package lang
Summary:        Summary: Translations for package fcitx5-qt
Group:          System/Localization
BuildArch:      noarch
Enhances:       (fcitx5-qt5 or fcitx5-qt6 or fcitx5-qt4)

%description lang
Provides translations for the fcitx5-qt package.

%package devel
Summary:        Development files for fcitx5-qt
Group:          Development/Libraries/C and C++
%if %{build_qt5}
Requires:       fcitx5-qt5 = %{version}
Requires:       libFcitx5Qt5DBusAddons1 = %{version}
Requires:       libFcitx5Qt5WidgetsAddons2 = %{version}
%endif
%if %{build_qt4}
Requires:       fcitx5-qt4 = %{version}
Requires:       libFcitx5Qt4DBusAddons1 = %{version}
%endif
%if %{build_qt6}
Requires:       fcitx5-qt6 = %{version}
Requires:       libFcitx5Qt6DBusAddons1 = %{version}
Requires:       libFcitx5Qt6WidgetsAddons2 = %{version}
%endif

%description devel
This package provides development files for fcitx5-qt.

%prep
%setup -q

%build
ARGS="-DCMAKE_INSTALL_LIBEXECDIR=%{_libexecdir}"
%if %{build_qt4}
ARGS="$ARGS -DENABLE_QT4=ON"
%endif
%if !%{build_qt5}
ARGS="$ARGS -DENABLE_QT5=OFF"
%endif
%if !%{build_qt6}
ARGS="$ARGS -DENABLE_QT6=OFF"
%endif

%if %{build_qt6}
%cmake_qt6 $ARGS
%qt6_build
%else
%cmake $ARGS
%cmake_build
%endif

%install
%if %{build_qt6}
%qt6_install
%else
%cmake_install
%endif

%find_lang %{name}

%fdupes %{buildroot}

%if %{build_qt4}
%ldconfig_scriptlets -n libFcitx5Qt4DBusAddons1
%endif
%if %{build_qt5}
%ldconfig_scriptlets -n libFcitx5Qt5DBusAddons1
%ldconfig_scriptlets -n libFcitx5Qt5WidgetsAddons2
%endif
%if %{build_qt6}
%ldconfig_scriptlets -n libFcitx5Qt6DBusAddons1
%ldconfig_scriptlets -n libFcitx5Qt6WidgetsAddons2
%endif

%files lang -f %{name}.lang

%if %{build_qt5}
%files -n fcitx5-qt5
%doc README.md
%license LICENSES
%{_bindir}/fcitx5-qt5-immodule-probing
%{_libexecdir}/fcitx5-qt5-gui-wrapper
%{_datadir}/applications/org.fcitx.fcitx5-qt5-gui-wrapper.desktop
%dir %{_libdir}/fcitx5
%dir %{_libdir}/fcitx5/qt5
%{_libdir}/fcitx5/qt5/libfcitx-quickphrase-editor5.so
%{_libdir}/qt5/plugins/platforminputcontexts/libfcitx5platforminputcontextplugin.so

%files -n libFcitx5Qt5DBusAddons1
%{_libdir}/libFcitx5Qt5DBusAddons.so.1
%{_libdir}/libFcitx5Qt5DBusAddons.so.%{version}

%files -n libFcitx5Qt5WidgetsAddons2
%{_libdir}/libFcitx5Qt5WidgetsAddons.so.2
%{_libdir}/libFcitx5Qt5WidgetsAddons.so.%{version}
%endif

%if %{build_qt6}
%files -n fcitx5-qt6
%doc README.md
%license LICENSES
%{_bindir}/fcitx5-qt6-immodule-probing
%{_libexecdir}/fcitx5-qt6-gui-wrapper
%dir %{_libdir}/fcitx5/qt6
%{_libdir}/fcitx5/qt6/libfcitx-quickphrase-editor5.so
%{_libdir}/qt6/plugins/platforminputcontexts/libfcitx5platforminputcontextplugin.so
%{_datadir}/applications/org.fcitx.fcitx5-qt6-gui-wrapper.desktop

%files -n libFcitx5Qt6DBusAddons1
%{_libdir}/libFcitx5Qt6DBusAddons.so.1
%{_libdir}/libFcitx5Qt6DBusAddons.so.%{version}

%files -n libFcitx5Qt6WidgetsAddons2
%{_libdir}/libFcitx5Qt6WidgetsAddons.so.2
%{_libdir}/libFcitx5Qt6WidgetsAddons.so.%{version}
%endif

%if %{build_qt4}
%files -n fcitx5-qt4
%{_libdir}/qt4/plugins/inputmethods/libqtim-fcitx5.so

%files -n libFcitx5Qt4DBusAddons1
%{_libdir}/libFcitx5Qt4DBusAddons.so.1
%{_libdir}/libFcitx5Qt4DBusAddons.so.%{version}
%endif

%files devel
%if %{build_qt4}
%{_includedir}/Fcitx5Qt4
%{_libdir}/libFcitx5Qt4DBusAddons.so
%{_libdir}/cmake/Fcitx5Qt4DBusAddons
%endif
%if %{build_qt5}
%{_includedir}/Fcitx5Qt5
%{_libdir}/cmake/Fcitx5Qt5DBusAddons
%{_libdir}/cmake/Fcitx5Qt5WidgetsAddons
%{_libdir}/libFcitx5Qt5DBusAddons.so
%{_libdir}/libFcitx5Qt5WidgetsAddons.so
%endif
%if %{build_qt6}
%{_includedir}/Fcitx5Qt6
%{_libdir}/libFcitx5Qt6DBusAddons.so
%{_libdir}/libFcitx5Qt6WidgetsAddons.so
%{_libdir}/cmake/Fcitx5Qt6DBusAddons
%{_libdir}/cmake/Fcitx5Qt6WidgetsAddons
%endif

%changelog
