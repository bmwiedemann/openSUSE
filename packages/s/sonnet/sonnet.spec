#
# spec file for package sonnet
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


%define sonum   5
%define _tar_path 5.74
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           sonnet
Version:        5.74.0
Release:        0
Summary:        KDE spell checking library
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/frameworks/%{_tar_path}/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/frameworks/%{_tar_path}/%{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
Source99:       baselibs.conf
#BuildRequires:  aspell-devel
# Enchant plugin is currently disabled upstream
#BuildRequires:  enchant-devel
BuildRequires:  extra-cmake-modules >= %{_kf5_bugfix_version}
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  myspell-dictionaries
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt5Core) >= 5.12.0
BuildRequires:  cmake(Qt5Test) >= 5.12.0
BuildRequires:  cmake(Qt5UiPlugin) >= 5.12.0
BuildRequires:  cmake(Qt5Widgets) >= 5.12.0
BuildRequires:  pkgconfig(hunspell)
BuildRequires:  pkgconfig(libvoikko)
%if %{with lang}
BuildRequires:  cmake(Qt5LinguistTools) >= 5.12.0
%endif

%description
Sonnet is a plugin-based spell checking library for Qt-based
applications. It supports several different plugins, including
HSpell, Enchant, ASpell and HUNSPELL.

%package -n libKF5SonnetCore%{sonum}
Summary:        KDE spell checking library
Group:          System/GUI/KDE
Requires:       %{name} >= %{_kf5_bugfix_version}
%requires_ge    libQt5Core5
Obsoletes:      libKF5SonnetCore4
%if %{with lang}
Recommends:     libKF5SonnetCore%{sonum}-lang = %{version}
%endif

%description -n libKF5SonnetCore%{sonum}
Sonnet is a plugin-based spell checking library for Qt-based
applications. It supports several different plugins, including
HSpell, Enchant, ASpell and HUNSPELL.

%package -n libKF5SonnetUi%{sonum}
Summary:        KDE spell checking library
Group:          System/GUI/KDE
%requires_ge    libKF5SonnetCore5
%requires_ge    libQt5Gui5
%requires_ge    libQt5Widgets5

%description -n libKF5SonnetUi%{sonum}
Sonnet is a plugin-based spell checking library for Qt-based
applications. It supports several different plugins, including
HSpell, Enchant, ASpell and HUNSPELL.

%package devel
Summary:        KDE spell checking library: Build Environment
Group:          Development/Libraries/KDE
Requires:       extra-cmake-modules
Requires:       libKF5SonnetCore%{sonum} = %{version}
Requires:       libKF5SonnetUi%{sonum} = %{version}
Requires:       cmake(Qt5Core) >= 5.12.0

%description devel
Sonnet is a plugin-based spell checking library for Qt-based
applications. It supports several different plugins, including
HSpell, Enchant, ASpell and HUNSPELL. Development files.

%package voikko
Summary:        KDE spell checking library: Support for Voikko
Group:          System/GUI/KDE
Requires:       %{name} = %{version}
Provides:       locale(sonnet:fi)

%description voikko
Plug-in adding Voikko based spell checking for the Finnish language
to the Sonnet spell checking framework.

%lang_package -n libKF5SonnetCore%{sonum}

%prep
%setup -q

%build
  %cmake_kf5 -d build -- -Dlconvert_executable=%{_kf5_libdir}/qt5/bin/lconvert
  %cmake_build

%install
  %kf5_makeinstall -C build
  %fdupes %{buildroot}

%if %{with lang}
%find_lang %{name}5 --with-qt --without-mo
%endif

%post -n libKF5SonnetCore%{sonum} -p /sbin/ldconfig
%postun -n libKF5SonnetCore%{sonum} -p /sbin/ldconfig
%post -n libKF5SonnetUi%{sonum} -p /sbin/ldconfig
%postun -n libKF5SonnetUi%{sonum} -p /sbin/ldconfig

%if %{with lang}
%files -n libKF5SonnetCore%{sonum}-lang -f %{name}5.lang
%endif

%files
%license LICENSES/*
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
%license LICENSES/*
%{_kf5_libdir}/libKF5SonnetUi.so.*

%files devel
%license LICENSES/*
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
%license LICENSES/*
%{_kf5_plugindir}/kf5/sonnet/sonnet_voikko.so

%changelog
