#
# spec file for package kguiaddons
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


%define lname   libKF5GuiAddons5
%define _tar_path 5.75
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
# Only needed for the package signature condition
%bcond_without lang
Name:           kguiaddons
Version:        5.75.0
Release:        0
Summary:        Utilities for graphical user interfaces
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/frameworks/%{_tar_path}/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/frameworks/%{_tar_path}/%{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
Source99:       baselibs.conf
BuildRequires:  extra-cmake-modules >= %{_kf5_bugfix_version}
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt5Gui) >= 5.12.0
# Tests
BuildRequires:  cmake(Qt5Test) >= 5.12.0
BuildRequires:  cmake(Qt5Widgets) >= 5.12.0
BuildRequires:  cmake(Qt5X11Extras) >= 5.12.0
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)

%description
The KDE GUI addons provide utilities for graphical user interfaces in the areas
of colors, fonts, text, images, keyboard input.

%package -n %{lname}
Summary:        Utilities for graphical user interfaces
Group:          System/GUI/KDE
%requires_ge    libQt5Gui5

%description -n %{lname}
The KDE GUI addons provide utilities for graphical user interfaces in the areas
of colors, fonts, text, images, keyboard input.

%package devel
Summary:        Utilities for graphical user interfaces: Build Environment
Group:          Development/Libraries/KDE
Requires:       %{lname} = %{version}
Requires:       extra-cmake-modules
Requires:       cmake(Qt5Gui) >= 5.12.0

%description devel
The KDE GUI addons provide utilities for graphical user interfaces in the areas
of colors, fonts, text, images, keyboard input. Development files.

%prep
%setup -q

%build
  %cmake_kf5 -d build
  %cmake_build

%install
  %kf5_makeinstall -C build
  %fdupes %{buildroot}

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%license LICENSES/*
%doc README*
%dir %{_kf5_plugindir}/kf5/
%dir %{_kf5_plugindir}/kf5/kguiaddons
%dir %{_kf5_plugindir}/kf5/kguiaddons/kmodifierkey
%{_kf5_libdir}/libKF5GuiAddons.so.*
%{_kf5_plugindir}/kf5/kguiaddons/kmodifierkey/kmodifierkey_xcb.so
%{_kf5_debugdir}/kguiaddons.categories

%files devel
%{_kf5_includedir}/
%{_kf5_libdir}/cmake/KF5GuiAddons/
%{_kf5_libdir}/libKF5GuiAddons.so
%{_kf5_mkspecsdir}/qt_KGuiAddons.pri

%changelog
