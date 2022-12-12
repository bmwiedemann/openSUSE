#
# spec file for package kdelibs4support
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


%define lname   libKF5KDELibs4Support5
%define _tar_path 5.101
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kdelibs4support
Version:        5.101.0
Release:        0
Summary:        Code and utilities to ease the transition to KDE Frameworks 5
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         %{name}-%{version}.tar.xz
%if %{with released}
Source1:        %{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  NetworkManager-devel
BuildRequires:  extra-cmake-modules >= %{_kf5_bugfix_version}
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  perl-URI
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF5Auth) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KDED) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5Completion) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5Config) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5ConfigWidgets) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5Crash) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5DBusAddons) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5DesignerPlugin) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5DocTools) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5Emoticons) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5GlobalAccel) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5GuiAddons) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5I18n) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5IconThemes) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5KIO) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5Notifications) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5Parts) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5Service) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5TextWidgets) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5UnitConversion) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5WidgetsAddons) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5WindowSystem) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5XmlGui) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(Qt5Concurrent) >= 5.15.0
BuildRequires:  cmake(Qt5Core) >= 5.15.0
BuildRequires:  cmake(Qt5DBus) >= 5.15.0
BuildRequires:  cmake(Qt5Designer) >= 5.15.0
BuildRequires:  cmake(Qt5Network) >= 5.15.0
BuildRequires:  cmake(Qt5PrintSupport) >= 5.15.0
BuildRequires:  cmake(Qt5Svg) >= 5.15.0
BuildRequires:  cmake(Qt5Test) >= 5.15.0
BuildRequires:  cmake(Qt5Widgets) >= 5.15.0
BuildRequires:  cmake(Qt5X11Extras) >= 5.15.0
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(x11)
Provides:       kde4support = %{version}
Obsoletes:      kde4support < %{version}

%description
This package includes CMake macros and C++
classes whose functionality has been replaced by code in CMake, Qt and
other frameworks.

Code should aim to port away from this framework eventually.  The API
documentation of the classes in this framework and the notes at
<https://community.kde.org/Frameworks/Porting_Notes> should help with
this.

Note that some of the classes in this framework, especially
KStandardDirs, may not work correctly unless any libraries and other
software using the KDE4 Support framework are installed to the same
location as KDELibs4Support, although it may be sufficient to set the
KDEDIRS environment variable correctly.

%package -n kssl
Summary:        Code and utilities to ease the transition to KDE Frameworks 5
License:        GPL-2.0-or-later

%description -n kssl
This package includes CMake macros and C++
classes whose functionality has been replaced by code in CMake, Qt and
other frameworks.

Code should aim to port away from this framework eventually.  The API
documentation of the classes in this framework and the notes at
<https://community.kde.org/Frameworks/Porting_Notes> should help with
this.

Note that some of the classes in this framework, especially
KStandardDirs, may not work correctly unless any libraries and other
software using the KDE4 Support framework are installed to the same
location as KDELibs4Support, although it may be sufficient to set the
KDEDIRS environment variable correctly.

%package -n %{lname}
Summary:        Code and utilities to ease the transition to KDE Frameworks 5
License:        LGPL-2.1-or-later
Requires:       kded >= %{_kf5_bugfix_version}

%description -n %{lname}
This package includes CMake macros and C++
classes whose functionality has been replaced by code in CMake, Qt and
other frameworks.

Code should aim to port away from this framework eventually.  The API
documentation of the classes in this framework and the notes at
<https://community.kde.org/Frameworks/Porting_Notes> should help with
this.

Note that some of the classes in this framework, especially
KStandardDirs, may not work correctly unless any libraries and other
software using the KDE4 Support framework are installed to the same
location as KDELibs4Support, although it may be sufficient to set the
KDEDIRS environment variable correctly.

%package devel
Summary:        Code and utilities to ease the transition to KDE Frameworks 5
License:        LGPL-2.1-or-later
Requires:       %{lname} = %{version}
Requires:       %{name} = %{version}
Requires:       extra-cmake-modules
Requires:       cmake(KF5Archive) >= %{_kf5_bugfix_version}
Requires:       cmake(KF5Auth) >= %{_kf5_bugfix_version}
Requires:       cmake(KF5ConfigWidgets) >= %{_kf5_bugfix_version}
Requires:       cmake(KF5CoreAddons) >= %{_kf5_bugfix_version}
Requires:       cmake(KF5Crash) >= %{_kf5_bugfix_version}
Requires:       cmake(KF5DBusAddons) >= %{_kf5_bugfix_version}
Requires:       cmake(KF5DesignerPlugin) >= %{_kf5_bugfix_version}
Requires:       cmake(KF5DocTools) >= %{_kf5_bugfix_version}
Requires:       cmake(KF5Emoticons) >= %{_kf5_bugfix_version}
Requires:       cmake(KF5GuiAddons) >= %{_kf5_bugfix_version}
Requires:       cmake(KF5IconThemes) >= %{_kf5_bugfix_version}
Requires:       cmake(KF5Init) >= %{_kf5_bugfix_version}
Requires:       cmake(KF5ItemModels) >= %{_kf5_bugfix_version}
Requires:       cmake(KF5Notifications) >= %{_kf5_bugfix_version}
Requires:       cmake(KF5Parts) >= %{_kf5_bugfix_version}
Requires:       cmake(KF5TextWidgets) >= %{_kf5_bugfix_version}
Requires:       cmake(KF5UnitConversion) >= %{_kf5_bugfix_version}
Requires:       cmake(KF5WindowSystem) >= %{_kf5_bugfix_version}
Requires:       cmake(Qt5Core) >= 5.15.0
Requires:       cmake(Qt5DBus) >= 5.15.0
Requires:       cmake(Qt5PrintSupport) >= 5.15.0
Requires:       cmake(Qt5Xml) >= 5.15.0
Provides:       kde4support-devel = %{version}
Obsoletes:      kde4support-devel < %{version}

%description devel
This package includes CMake macros and C++
classes whose functionality has been replaced by code in CMake, Qt and
other frameworks.

Code should aim to port away from this framework eventually.  The API
documentation of the classes in this framework and the notes at
<https://community.kde.org/Frameworks/Porting_Notes> should help with
this.

Note that some of the classes in this framework, especially
KStandardDirs, may not work correctly unless any libraries and other
software using the KDE4 Support framework are installed to the same
location as KDELibs4Support, although it may be sufficient to set the
KDEDIRS environment variable correctly. Development files.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build
%fdupes %{buildroot}

%find_lang %{name} --with-man --all-name
%{kf5_find_htmldocs}

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files lang -f %{name}.lang

%files
%{_kf5_bindir}/kdebugdialog5
%{_kf5_bindir}/kf5-config
%{_kf5_configdir}/colors/
%{_kf5_configdir}/kdebug.areas
%{_kf5_configdir}/kdebugrc
%{_kf5_libexecdir}/filesharelist
%{_kf5_libexecdir}/fileshareset
%{_kf5_plugindir}/
%{_kf5_servicesdir}/
# within kssl package
%exclude %{_kf5_plugindir}/kcm_ssl.so
%exclude %{_kf5_servicesdir}/kcm_ssl.desktop
%{_kf5_servicetypesdir}/
%{_kf5_datadir}/kdoctools/
%{_kf5_datadir}/widgets/
%{_kf5_sharedir}/locale/kf5_all_languages
%{_kf5_datadir}/locale/
%doc %lang(en) %{_kf5_mandir}/*/kf5-config.*
%dir %{_kf5_htmldir}/en
%dir %{_kf5_htmldir}
%doc %lang(en) %{_kf5_htmldir}/en/*/

%files -n kssl
%{_kf5_configdir}/ksslcalist
%{_kf5_plugindir}/kcm_ssl.so
%{_kf5_servicesdir}/kcm_ssl.desktop
%{_kf5_datadir}/kssl/

%files -n %{lname}
%license COPYING*
%doc README*
%{_kf5_libdir}/libKF5KDELibs4Support.so.*

%files devel
%{_kf5_libdir}/libKF5KDELibs4Support.so
%{_kf5_libdir}/cmake/KF5KDELibs4Support/
%{_kf5_libdir}/cmake/KF5KDE4Support/
%{_kf5_libdir}/cmake/KDELibs4/
%{_kf5_includedir}/KDELibs4Support/
%{_kf5_sharedir}/dbus-1/interfaces/kf5_org.freedesktop.PowerManagement.Inhibit.xml
%{_kf5_sharedir}/dbus-1/interfaces/kf5_org.freedesktop.PowerManagement.xml
%{_kf5_sharedir}/dbus-1/interfaces/kf5_org.kde.Solid.Networking.Client.xml
%{_kf5_sharedir}/dbus-1/interfaces/kf5_org.kde.Solid.PowerManagement.PolicyAgent.xml

%changelog
