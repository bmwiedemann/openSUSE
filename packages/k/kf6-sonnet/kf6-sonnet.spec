#
# spec file for package kf6-sonnet
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


%define qt6_version 6.6.0

%define rname sonnet
# Full KF6 version (e.g. 6.3.0)
%{!?_kf6_version: %global _kf6_version %{version}}
# Last major and minor KF6 version (e.g. 6.0)
%{!?_kf6_bugfix_version: %define _kf6_bugfix_version %(echo %{_kf6_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kf6-sonnet
Version:        6.3.0
Release:        0
Summary:        KDE spell checking library
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_bugfix_version}
BuildRequires:  myspell-dictionaries
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6LinguistTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6UiPlugin) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(hunspell)
BuildRequires:  pkgconfig(libvoikko)

%description
Sonnet is a plugin-based spell checking library for Qt-based
applications. It supports different plugins, including
HSpell, Enchant, ASpell and HUNSPELL.

%package imports
Summary:        KDE spell checking library: QML files
Requires:       libKF6SonnetCore6 = %{version}
Requires:       libKF6SonnetUi6 = %{version}

%description imports

Sonnet is a plugin-based spell checking library for Qt-based
applications. It supports different plugins, including
HSpell, Enchant, ASpell and HUNSPELL.
This package contains files that allow use of sonnet with
QtQuick based applications.

%package -n libKF6SonnetCore6
Summary:        KDE spell checking library
Requires:       kf6-sonnet >= %{_kf6_bugfix_version}

%description -n libKF6SonnetCore6
Sonnet is a plugin-based spell checking library for Qt-based
applications. It supports different plugins, including
HSpell, Enchant, ASpell and HUNSPELL.

%package -n libKF6SonnetUi6
Summary:        KDE spell checking library

%description -n libKF6SonnetUi6
Sonnet is a plugin-based spell checking library for Qt-based
applications. It supports different plugins, including
HSpell, Enchant, ASpell and HUNSPELL.

%package devel
Summary:        KDE spell checking library: Build Environment
Requires:       libKF6SonnetCore6 = %{version}
Requires:       libKF6SonnetUi6 = %{version}
Requires:       cmake(Qt6Core) >= %{qt6_version}

%description devel
Sonnet is a plugin-based spell checking library for Qt-based
applications. It supports different plugins, including
HSpell, Enchant, ASpell and HUNSPELL. Development files.

%package voikko
Summary:        KDE spell checking library: Support for Voikko
Requires:       kf6-sonnet >= %{version}
Provides:       locale(sonnet:fi)

%description voikko
Plug-in adding Voikko based spell checking for the Finnish language
to the Sonnet spell checking framework.

%lang_package -n libKF6SonnetCore6

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 -DBUILD_QCH:BOOL=ON

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%find_lang sonnet6 --with-qt --without-mo

%ldconfig_scriptlets -n libKF6SonnetCore6
%ldconfig_scriptlets -n libKF6SonnetUi6

%files -n libKF6SonnetCore6-lang -f sonnet6.lang

%files
%dir %{_kf6_plugindir}/kf6/sonnet
%{_kf6_debugdir}/sonnet.categories
%{_kf6_debugdir}/sonnet.renamecategories
%{_kf6_plugindir}/kf6/sonnet/sonnet_hunspell.so

%files -n libKF6SonnetCore6
%license LICENSES/*
%doc README.md
%{_kf6_libdir}/libKF6SonnetCore.so.*

%files -n libKF6SonnetUi6
%{_kf6_libdir}/libKF6SonnetUi.so.*

%files imports
%{_kf6_qmldir}/org/kde/sonnet/

%files devel
%doc %{_kf6_qchdir}/KF6Sonnet*.*
%{_kf6_bindir}/parsetrigrams6
%{_kf6_cmakedir}/KF6Sonnet/
%{_kf6_includedir}/Sonnet/
%{_kf6_includedir}/SonnetCore/
%{_kf6_includedir}/SonnetUi/
%{_kf6_libdir}/libKF6SonnetCore.so
%{_kf6_libdir}/libKF6SonnetUi.so
%{_kf6_plugindir}/designer/sonnet6widgets.so

%files voikko
%{_kf6_plugindir}/kf6/sonnet/sonnet_voikko.so

%changelog
