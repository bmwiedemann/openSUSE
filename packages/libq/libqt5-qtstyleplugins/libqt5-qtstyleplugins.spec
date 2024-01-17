#
# spec file for package libqt5-qtstyleplugins
#
# Copyright (c) 2021 SUSE LLC
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


%define _name   qtstyleplugins
%define base_name libqt5
%define qt_version 5.0.0
%bcond_without gtk2
Name:           libqt5-qtstyleplugins
Version:        5.0.0+git20170311
Release:        0
Summary:        Qt 5 Style Plugins
License:        LGPL-2.1-with-Qt-Company-Qt-exception-1.1 OR LGPL-3.0-only
URL:            https://qt.io/
Source:         %{_name}-opensource-src-%{version}.tar.xz
# PATCH-FIX-OPENSUSE qtstyleplugins-gtksettings.patch sor.alexei@meowr.ru -- Align Qt with GTK settings a bit better.
Patch0:         qtstyleplugins-gtksettings.patch
# PATCH-FIX-OPENSUSE qtstyleplugins-fix-deprecations.patch -- Fix various Qt deprecations.
Patch1:         qtstyleplugins-fix-deprecations.patch
BuildRequires:  fdupes
BuildRequires:  libQt5Core-private-headers-devel >= %{qt_version}
BuildRequires:  libQt5Gui-private-headers-devel >= %{qt_version}
BuildRequires:  libQt5Widgets-private-headers-devel >= %{qt_version}
BuildRequires:  libqt5-qtbase-devel >= %{qt_version}
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libudev)
%requires_eq    libQt5Core5
%if %{with gtk2}
BuildRequires:  libQt5PlatformSupport-private-headers-devel >= %{qt_version}
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(x11)
%endif

%description
Qt is a set of libraries for developing applications.

This package contains additional style plugins.

%if %{with gtk2}
%package platformtheme-gtk2
Summary:        Qt 5 gtk2 plugin
%requires_eq    libQt5Gui5
Supplements:    (libQt5Gui5 and libgtk-2_0-0)

%description platformtheme-gtk2
Qt 5 plugin for better integration with gtk-based desktop enviroments.
%endif

%package devel
Summary:        Qt 5 Style Plugins Development Files
Requires:       %{name} = %{version}
%if %{with gtk2}
Requires:       %{name}-platformtheme-gtk2 = %{version}
%endif

%description devel
You need this package, if you want to compile programs with qtstyleplugins.

%prep
%autosetup -p1 -n %{_name}-opensource-src-%{version}

%build
%qmake5
%make_build

%install
%qmake5_install

find %{buildroot} -type f -name "*.la" -delete -print

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%post platformtheme-gtk2 -p /sbin/ldconfig

%postun platformtheme-gtk2 -p /sbin/ldconfig

%files
%dir %{_libqt5_libdir}/qt5/plugins/styles/
%{_libqt5_libdir}/qt5/plugins/styles/*.so
%if %{with gtk2}
%exclude %{_libqt5_libdir}/qt5/plugins/styles/libqgtk2style.so
%endif

%if %{with gtk2}
%files platformtheme-gtk2
%dir %{_libqt5_libdir}/qt5/plugins/platformthemes/
%{_libqt5_libdir}/qt5/plugins/platformthemes/libqgtk2.so
%dir %{_libqt5_libdir}/qt5/plugins/styles/
%{_libqt5_libdir}/qt5/plugins/styles/libqgtk2style.so
%endif

%files devel
%{_libqt5_libdir}/cmake/Qt5Widgets/Qt5Widgets_*StylePlugin.cmake
%if %{with gtk2}
%{_libqt5_libdir}/cmake/Qt5Gui/Qt5Gui_*ThemePlugin.cmake
%endif

%changelog
