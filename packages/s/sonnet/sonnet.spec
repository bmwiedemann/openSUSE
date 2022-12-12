#
# spec file for package sonnet
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


%define sonum   5
%define _tar_path 5.101
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           sonnet
Version:        5.101.0
Release:        0
Summary:        KDE spell checking library
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         %{name}-%{version}.tar.xz
%if %{with released}
Source1:        %{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
#BuildRequires:  aspell-devel
# Enchant plugin is currently disabled upstream
#BuildRequires:  enchant-devel
BuildRequires:  extra-cmake-modules >= %{_kf5_bugfix_version}
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  myspell-dictionaries
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt5Core) >= 5.15.0
BuildRequires:  cmake(Qt5LinguistTools) >= 5.15.0
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5Test) >= 5.15.0
BuildRequires:  cmake(Qt5UiPlugin) >= 5.15.0
BuildRequires:  cmake(Qt5Widgets) >= 5.15.0
BuildRequires:  pkgconfig(hunspell)
BuildRequires:  pkgconfig(libvoikko)

%description
Sonnet is a plugin-based spell checking library for Qt-based
applications. It supports several different plugins, including
HSpell, Enchant, ASpell and HUNSPELL.

%package -n libKF5SonnetCore%{sonum}
Summary:        KDE spell checking library
Requires:       %{name} >= %{_kf5_bugfix_version}
%requires_ge    libQt5Core5
Obsoletes:      libKF5SonnetCore4

%description -n libKF5SonnetCore%{sonum}
Sonnet is a plugin-based spell checking library for Qt-based
applications. It supports several different plugins, including
HSpell, Enchant, ASpell and HUNSPELL.

%package -n libKF5SonnetUi%{sonum}
Summary:        KDE spell checking library
%requires_ge    libKF5SonnetCore5
%requires_ge    libQt5Gui5
%requires_ge    libQt5Widgets5

%description -n libKF5SonnetUi%{sonum}
Sonnet is a plugin-based spell checking library for Qt-based
applications. It supports several different plugins, including
HSpell, Enchant, ASpell and HUNSPELL.

%package imports
Summary:        KDE spell checking library: QML files
Requires:       libKF5SonnetCore%{sonum} = %{version}
Requires:       libKF5SonnetUi%{sonum} = %{version}

%description imports

Sonnet is a plugin-based spell checking library for Qt-based
applications. It supports several different plugins, including
HSpell, Enchant, ASpell and HUNSPELL.
This package contains files that allow use of sonnet with
QtQuick based applications.

%package devel
Summary:        KDE spell checking library: Build Environment
Requires:       extra-cmake-modules
Requires:       libKF5SonnetCore%{sonum} = %{version}
Requires:       libKF5SonnetUi%{sonum} = %{version}
Requires:       cmake(Qt5Core) >= 5.15.0

%description devel
Sonnet is a plugin-based spell checking library for Qt-based
applications. It supports several different plugins, including
HSpell, Enchant, ASpell and HUNSPELL. Development files.

%package voikko
Summary:        KDE spell checking library: Support for Voikko
Requires:       %{name} = %{version}
Provides:       locale(sonnet:fi)

%description voikko
Plug-in adding Voikko based spell checking for the Finnish language
to the Sonnet spell checking framework.

%lang_package -n libKF5SonnetCore%{sonum}

%prep
%autosetup -p1

%build
%cmake_kf5 -d build -- -Dlconvert_executable=%{_kf5_libdir}/qt5/bin/lconvert
%cmake_build

%install
%kf5_makeinstall -C build

%fdupes %{buildroot}

%find_lang sonnet5 --with-qt --without-mo

%post -n libKF5SonnetCore%{sonum} -p /sbin/ldconfig
%postun -n libKF5SonnetCore%{sonum} -p /sbin/ldconfig
%post -n libKF5SonnetUi%{sonum} -p /sbin/ldconfig
%postun -n libKF5SonnetUi%{sonum} -p /sbin/ldconfig

%files -n libKF5SonnetCore%{sonum}-lang -f sonnet5.lang

%files
%doc README*
%dir %{_kf5_plugindir}/kf5
%dir %{_kf5_plugindir}/kf5/sonnet
%{_kf5_debugdir}/sonnet.categories
%{_kf5_debugdir}/*.renamecategories
%{_kf5_plugindir}/kf5/sonnet/sonnet_hunspell.so

%files -n libKF5SonnetCore%{sonum}
%license LICENSES/*
%{_kf5_libdir}/libKF5SonnetCore.so.*

%files -n libKF5SonnetUi%{sonum}
%{_kf5_libdir}/libKF5SonnetUi.so.*

%files imports
%dir %{_kf5_qmldir}/org/
%dir %{_kf5_qmldir}/org/kde/
%dir %{_kf5_qmldir}/org/kde/sonnet
%{_kf5_qmldir}/org/kde/sonnet/libsonnetquickplugin.so
%{_kf5_qmldir}/org/kde/sonnet/plugins.qmltypes
%{_kf5_qmldir}/org/kde/sonnet/qmldir

%files devel
%dir %{_kf5_plugindir}/designer
%{_kf5_bindir}/gentrigrams
%{_kf5_bindir}/parsetrigrams
%{_kf5_includedir}/
%{_kf5_libdir}/cmake/KF5Sonnet/
%{_kf5_libdir}/libKF5SonnetCore.so
%{_kf5_libdir}/libKF5SonnetUi.so
%{_kf5_mkspecsdir}/qt_Sonnet*.pri
%{_kf5_plugindir}/designer/sonnetui5widgets.so

%files voikko
%{_kf5_plugindir}/kf5/sonnet/sonnet_voikko.so

%changelog
