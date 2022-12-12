#
# spec file for package khtml
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


%define lname   libKF5KHtml5
%define _tar_path 5.101
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           khtml
Version:        5.101.0
Release:        0
Summary:        HTML rendering engine
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         %{name}-%{version}.tar.xz
%if %{with released}
Source1:        %{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  extra-cmake-modules >= %{_kf5_bugfix_version}
BuildRequires:  fdupes
BuildRequires:  giflib-devel
BuildRequires:  gperf
BuildRequires:  kf5-filesystem
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF5Archive) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5Codecs) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5GlobalAccel) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5I18n) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5IconThemes) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5JS) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5KIO) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5Notifications) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5Parts) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5Sonnet) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5TextWidgets) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5Wallet) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5WidgetsAddons) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5WindowSystem) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5XmlGui) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(Phonon4Qt5)
BuildRequires:  cmake(Qt5Core) >= 5.15.0
BuildRequires:  cmake(Qt5DBus) >= 5.15.0
BuildRequires:  cmake(Qt5Network) >= 5.15.0
BuildRequires:  cmake(Qt5PrintSupport) >= 5.15.0
BuildRequires:  cmake(Qt5Test) >= 5.15.0
BuildRequires:  cmake(Qt5Widgets) >= 5.15.0
BuildRequires:  cmake(Qt5X11Extras) >= 5.15.0
BuildRequires:  cmake(Qt5Xml) >= 5.15.0
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(x11)

%description
KHTML is a web rendering engine, based on the KParts
technology and using KJS for JavaScript support.

%package -n %{lname}
Summary:        HTML rendering engine
Obsoletes:      libKF5KHtml4

%description -n %{lname}
KHTML is a web rendering engine, based on the KParts
technology and using KJS for JavaScript support.

%package devel
Summary:        HTML rendering engine
Requires:       %{lname} = %{version}
Requires:       extra-cmake-modules
Requires:       cmake(KF5Codecs) >= %{_kf5_bugfix_version}
Requires:       cmake(KF5I18n) >= %{_kf5_bugfix_version}
Requires:       cmake(KF5JS) >= %{_kf5_bugfix_version}
Requires:       cmake(KF5KIO) >= %{_kf5_bugfix_version}
Requires:       cmake(KF5Parts) >= %{_kf5_bugfix_version}
Requires:       cmake(KF5TextWidgets) >= %{_kf5_bugfix_version}
Requires:       cmake(Qt5Gui) >= 5.15.0

%description devel
KHTML is a web rendering engine, based on the KParts
technology and using KJS for JavaScript support.
Development files.

%lang_package -n %{lname}

%prep
%autosetup -p1

%build
%ifarch ppc64
%define _lto_cflags %{nil}
%endif

%cmake_kf5 -d build -- -DSYSCONF_INSTALL_DIR=%{_kf5_sysconfdir}
%cmake_build

%install
%kf5_makeinstall -C build
%fdupes %{buildroot}


%find_lang khtml5

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}-lang -f khtml5.lang

%files -n %{lname}
%license COPYING*
%doc README*
%{_kf5_libdir}/libKF5KHtml.so.*
%{_kf5_plugindir}/
%{_kf5_servicesdir}/
%{_kf5_datadir}/khtml/
%config %{_kf5_configdir}/khtmlrc
%{_kf5_debugdir}/*.categories
%{_kf5_debugdir}/*.renamecategories

%files devel
%{_kf5_libdir}/libKF5KHtml.so
%{_kf5_libdir}/cmake/KF5KHtml/
%{_kf5_includedir}/KHtml/
%{_kf5_mkspecsdir}/qt_KHtml.pri

%changelog
