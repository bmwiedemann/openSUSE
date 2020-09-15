#
# spec file for package libqt5-qtvirtualkeyboard
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


%define qt5_snapshot 0

Name:           libqt5-qtvirtualkeyboard
Version:        5.15.1
Release:        0
Summary:        Qt 5 Virtual Keyboard
License:        GPL-3.0
Group:          Development/Libraries/X11
Url:            https://www.qt.io
%define base_name libqt5
%define real_version 5.15.1
%define so_version 5.15.1
%define tar_version qtvirtualkeyboard-everywhere-src-5.15.1
Source:         https://download.qt.io/official_releases/qt/5.15/%{real_version}/submodules/%{tar_version}.tar.xz
BuildRequires:  libQt5Gui-private-headers-devel >= %{version}
BuildRequires:  libQt5Core-private-headers-devel >= %{version}
BuildRequires:  pkgconfig(Qt5Qml) >= %{version}
BuildRequires:  pkgconfig(Qt5Quick) >= %{version}
BuildRequires:  pkgconfig(Qt5Svg) >= %{version}
%if %qt5_snapshot
#to create the forwarding headers
BuildRequires:  perl
%endif
BuildRequires:  xz
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(hunspell)
# Was part of the core before 5.12
Recommends:     %{name}-hunspell
%requires_ge libQtQuick5

%description
Qt is a set of libraries for developing applications.

This package contains a virtual keyboard.

%package -n libQt5VirtualKeyboard5
Summary:       Qt5 Virtual Keyboard library
Group:         System/Libraries

%description -n libQt5VirtualKeyboard5
Internal library used by Qt for providing Hunspell support.

%package examples
Summary:        Qt5 virtualkeyboard examples
Group:          Development/Libraries/X11

%description examples
Examples for libqt5-qtvirtualkeyboard module.

%package devel
Summary:        Qt Development Kit
Group:          Development/Libraries/X11
Requires:       %{name} = %{version}

%description devel
You need this package if you want to compile programs or plugins with
Qt Virtual Keyboard.

%package private-headers-devel
Summary:        Non-ABI stable API for the Qt5 Virtual Keyboard
Group:          Development/Libraries/C and C++
Requires:       %{name}-devel = %{version}
Requires:       libQt5Gui-private-headers-devel >= %{version}
Requires:       libQt5Core-private-headers-devel >= %{version}

%description private-headers-devel
This package provides private headers of libqt5-qtvirtualkeyboard that are
normally not used by application development and that do not have any ABI or
API guarantees. The packages that build against these have to require
the exact Qt version.

%package hunspell
Summary:       Hunspell Plugin for the Qt5 Virtual Keyboard
# TODO!
Group:         System/Libraries
Requires:      %{name} = %{version}

%description hunspell
This package provides a hunspell spell checking plugin for the Qt Virtual Keyboard.

%package -n libQt5HunspellInputMethod5
Summary:       Qt5 Hunspell Input Method
Group:         System/Libraries

%description -n libQt5HunspellInputMethod5
Internal library used by Qt for providing Hunspell support.

%package -n libQt5HunspellInputMethod-private-headers-devel
Summary:        Non-ABI stable API for libQt5HunspellInputMethod
Group:          Development/Libraries/C and C++
Requires:       libQt5HunspellInputMethod5 = %{version}	
Requires:       %{name}-private-headers-devel = %{version}

%description -n libQt5HunspellInputMethod-private-headers-devel
This package provides private headers of libQt5HunspellInputMethod that are
normally not used by application development and that do not have any ABI or
API guarantees. The packages that build against these have to require
the exact Qt version.

%prep
%setup -q -n %{tar_version}

%build
%if %qt5_snapshot
#force the configure script to generate the forwarding headers (it checks whether .git directory exists)
mkdir .git
%endif
# Only enable languages that don't force-include bundled 3rdparty libs
%qmake5 "CONFIG+=lang-ar_AR lang-da_DK lang-de_DE lang-en_GB lang-es_ES lang-fa_FA lang-fi_FI lang-fr_FR lang-hi_IN lang-it_IT lang-nb_NO lang-pl_PL lang-pt_PT lang-ro_RO lang-ru_RU lang-sv_SE"
%make_jobs

%install
%qmake5_install

# kill .la files
rm -f %{buildroot}%{_libqt5_libdir}/lib*.la

%post   -n libQt5VirtualKeyboard5 -p /sbin/ldconfig
%postun -n libQt5VirtualKeyboard5 -p /sbin/ldconfig
%post   -n libQt5HunspellInputMethod5 -p /sbin/ldconfig
%postun -n libQt5HunspellInputMethod5 -p /sbin/ldconfig

%files
%license LICENSE.*
%dir %{_libqt5_plugindir}/virtualkeyboard
%{_libqt5_plugindir}/platforminputcontexts/libqtvirtualkeyboardplugin.so
%{_libqt5_archdatadir}/qml/QtQuick/VirtualKeyboard/

%files -n libQt5VirtualKeyboard5
%license LICENSE.*
%{_libqt5_libdir}/libQt5VirtualKeyboard.so.*

%files devel
%license LICENSE.*
%exclude %{_libqt5_includedir}/QtVirtualKeyboard/%{so_version}
%{_libqt5_includedir}/QtVirtualKeyboard/
%{_libqt5_libdir}/cmake/Qt5VirtualKeyboard/
%{_libqt5_libdir}/cmake/Qt5Gui/Qt5Gui_QVirtualKeyboardPlugin.cmake
%{_libqt5_libdir}/libQt5VirtualKeyboard.prl
%{_libqt5_libdir}/libQt5VirtualKeyboard.so
%{_libqt5_libdir}/pkgconfig/Qt5VirtualKeyboard.pc
%{_libqt5_libdir}/qt5/mkspecs/modules/qt_lib_virtualkeyboard.pri

%files private-headers-devel
%license LICENSE.*
%{_libqt5_libdir}/qt5/mkspecs/modules/qt_lib_virtualkeyboard_private.pri
%{_libqt5_includedir}/QtVirtualKeyboard/%{so_version}/

%files hunspell
%license LICENSE.*
%{_libqt5_plugindir}/virtualkeyboard/libqtvirtualkeyboard_hunspell.so

%files -n libQt5HunspellInputMethod5
%license LICENSE.*
%{_libqt5_libdir}/libQt5HunspellInputMethod.so.*

%files -n libQt5HunspellInputMethod-private-headers-devel
%license LICENSE.*
# Private headers + non-private Version/Depends headers
%{_libqt5_includedir}/QtHunspellInputMethod/
%{_libqt5_libdir}/libQt5HunspellInputMethod.prl
%{_libqt5_libdir}/libQt5HunspellInputMethod.so
%{_libqt5_libdir}/cmake/Qt5HunspellInputMethod/
%{_libqt5_libdir}/qt5/mkspecs/modules/qt_lib_hunspellinputmethod_private.pri

%files examples
%license LICENSE.*
%{_libqt5_examplesdir}/

%changelog
