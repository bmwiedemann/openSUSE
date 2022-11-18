#
# spec file for package fcitx5-qt
#
# Copyright (c) 2022 SUSE LLC
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

%if 0%{?suse_version} >= 1550
%define build_qt6 1
%else
%define build_qt6 0
%endif

Name:           fcitx5-qt
Version:        5.0.15
Release:        0
Summary:        Qt library and IM module for fcitx5
License:        BSD-3-Clause AND LGPL-2.1-or-later
Group:          System/I18n/Chinese
URL:            https://github.com/fcitx/fcitx5-qt
Source:         https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.xz
Patch:          %{name}-5.9.patch
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  gcc-c++
%if %build_qt4
BuildRequires:  libqt4-devel
%endif
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  libqt5-qtbase-private-headers-devel
BuildRequires:  libqt5-qtx11extras-devel
%if %build_qt6
BuildRequires:  qt6-base-devel
BuildRequires:  qt6-base-private-devel
%endif
BuildRequires:  fcitx5-devel
BuildRequires:  libxcb-devel
BuildRequires:  libxkbcommon-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Qt library and IM module for fcitx5.

%if %build_qt4
%package -n fcitx5-qt4
Summary:        Qt4 IM module for Fcitx5
Group:          System/I18n/Chinese
Provides:       fcitx-qt4 = %{version}
Obsoletes:      fcitx-qt4 < 5.0.0
Supplements:    (fcitx5 and libqt4)

%description -n fcitx5-qt4
Qt4 IM module for Fcitx5.

%package -n libFcitx5Qt4DBusAddons1
Summary:        Qt4 DBus Addons library for Fcitx5
Group:          System/Libraries

%description -n libFcitx5Qt4DBusAddons1
This package provides Qt4 DBus Addons library for Fcitx5.
%endif

%if %build_qt6
%package -n fcitx5-qt6
Summary:        Qt6 IM module for Fcitx5
Group:          System/I18n/Chinese
Provides:       fcitx-qt6 = %{version}
Obsoletes:      fcitx-qt6 < 5.0.0
Supplements:    (fcitx5 and libQt6Core6)

%description -n fcitx5-qt6
Qt6 IM module for Fcitx5.

%package -n libFcitx5Qt6DBusAddons1
Summary:        Qt6 DBus Addons library for Fcitx5
Group:          System/Libraries

%description -n libFcitx5Qt6DBusAddons1
This package provides Qt6 DBus Addons library for Fcitx5.
%endif

%package -n fcitx5-qt5
Summary:        Qt5 IM module for Fcitx5
Group:          System/I18n/Chinese
Provides:       fcitx-qt5 = %{version}
Obsoletes:      fcitx-qt5 < 5.0.0
Supplements:    (fcitx5 and libqt5-qtbase)

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

%package devel
Summary:        Development files for fcitx5-qt
Group:          Development/Libraries/C and C++
%if %build_qt4
Requires:       fcitx5-qt4 = %{version}
Requires:       libFcitx5Qt4DBusAddons1 = %{version}
%endif
Requires:       fcitx5-qt5 = %{version}
Requires:       libFcitx5Qt5DBusAddons1 = %{version}
Requires:       libFcitx5Qt5WidgetsAddons2 = %{version}
%if %build_qt6
Requires:       fcitx5-qt6 = %{version}
Requires:       libFcitx5Qt6DBusAddons1 = %{version}
%endif

%description devel
This package provides development files for fcitx5-qt.

%prep
%setup -q
%autopatch -p1

%build
ARGS=""
%if !%build_qt4
ARGS="$ARGS -DENABLE_QT4=OFF"
%endif
%if %build_qt6
ARGS="$ARGS -DENABLE_QT6=ON"
%endif
%cmake -DCMAKE_INSTALL_LIBEXECDIR=%{_libexecdir} $ARGS
make %{?_smp_mflags}

%install
%cmake_install
%find_lang %{name}
%fdupes -s %{buildroot}

%if %build_qt4
%post -n libFcitx5Qt4DBusAddons1 -p /sbin/ldconfig
%postun -n libFcitx5Qt4DBusAddons1 -p /sbin/ldconfig
%endif
%post -n libFcitx5Qt5DBusAddons1 -p /sbin/ldconfig
%post -n libFcitx5Qt5WidgetsAddons2 -p /sbin/ldconfig
%postun -n libFcitx5Qt5DBusAddons1 -p /sbin/ldconfig
%postun -n libFcitx5Qt5WidgetsAddons2 -p /sbin/ldconfig
%if %build_qt6
%post -n libFcitx5Qt6DBusAddons1 -p /sbin/ldconfig
%postun -n libFcitx5Qt6DBusAddons1 -p /sbin/ldconfig
%endif

%files -n fcitx5-qt5 -f %{name}.lang
%defattr(-,root,root)
%doc README.md
%license LICENSES
%{_libexecdir}/fcitx5-qt5-gui-wrapper
%{_datadir}/applications/org.fcitx.fcitx5-qt5-gui-wrapper.desktop
%{_fcitx5_qt5dir}/libfcitx-quickphrase-editor5.so
%{_libdir}/qt5/plugins/platforminputcontexts/libfcitx5platforminputcontextplugin.so

%if %build_qt6
%files -n fcitx5-qt6
%defattr(-,root,root)
%{_libdir}/qt6/plugins/platforminputcontexts/libfcitx5platforminputcontextplugin.so

%files -n libFcitx5Qt6DBusAddons1
%defattr(-,root,root)
%{_libdir}/libFcitx5Qt6DBusAddons.so.1
%{_libdir}/libFcitx5Qt6DBusAddons.so.%{version}
%endif

%if %build_qt4
%files -n fcitx5-qt4
%defattr(-,root,root)
%{_libdir}/qt4/plugins/inputmethods/libqtim-fcitx5.so

%files -n libFcitx5Qt4DBusAddons1
%defattr(-,root,root)
%{_libdir}/libFcitx5Qt4DBusAddons.so.1
%{_libdir}/libFcitx5Qt4DBusAddons.so.%{version}
%endif

%files -n libFcitx5Qt5DBusAddons1
%defattr(-,root,root)
%{_libdir}/libFcitx5Qt5DBusAddons.so.1
%{_libdir}/libFcitx5Qt5DBusAddons.so.%{version}

%files -n libFcitx5Qt5WidgetsAddons2
%defattr(-,root,root)
%{_libdir}/libFcitx5Qt5WidgetsAddons.so.2
%{_libdir}/libFcitx5Qt5WidgetsAddons.so.%{version}

%files devel
%defattr(-,root,root)
%if %build_qt4
%{_includedir}/Fcitx5Qt4
%{_libdir}/libFcitx5Qt4DBusAddons.so
%{_libdir}/cmake/Fcitx5Qt4DBusAddons
%endif
%{_includedir}/Fcitx5Qt5
%{_libdir}/cmake/Fcitx5Qt5DBusAddons
%{_libdir}/cmake/Fcitx5Qt5WidgetsAddons
%{_libdir}/libFcitx5Qt5DBusAddons.so
%{_libdir}/libFcitx5Qt5WidgetsAddons.so
%if %build_qt6
%{_includedir}/Fcitx5Qt6
%{_libdir}/libFcitx5Qt6DBusAddons.so
%{_libdir}/cmake/Fcitx5Qt6DBusAddons
%endif

%changelog
