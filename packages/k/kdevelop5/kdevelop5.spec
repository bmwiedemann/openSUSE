#
# spec file for package kdevelop5
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


%define rname   kdevelop
%define libkdev_major 510
%bcond_without released
Name:           kdevelop5
Version:        22.12.0
Release:        0
Summary:        Plugin-extensible IDE for C/C++ and other programming languages
License:        GPL-2.0-or-later
URL:            https://www.kdevelop.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
ExclusiveArch:  %{arm} aarch64 %{ix86} x86_64 %{mips} %{riscv}
BuildRequires:  kdevelop5-pg-qt
BuildRequires:  kf5-filesystem
BuildRequires:  libboost_headers-devel
BuildRequires:  clang-devel
BuildRequires:  okteta-devel
BuildRequires:  shared-mime-info
BuildRequires:  subversion-devel
BuildRequires:  cmake(Grantlee5)
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5Declarative)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5ItemModels)
BuildRequires:  cmake(KF5ItemViews)
BuildRequires:  cmake(KF5JobWidgets)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5NewStuff)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5NotifyConfig)
BuildRequires:  cmake(KF5Parts)
BuildRequires:  cmake(KF5Plasma)
BuildRequires:  cmake(KF5Purpose)
BuildRequires:  cmake(KF5Runner)
BuildRequires:  cmake(KF5Service)
BuildRequires:  cmake(KF5SysGuard)
BuildRequires:  cmake(KF5TextEditor)
BuildRequires:  cmake(KF5ThreadWeaver)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(LibKompareDiff2)
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Help)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5QuickWidgets)
BuildRequires:  cmake(Qt5Script)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5WebEngineWidgets)
BuildRequires:  cmake(Qt5Widgets)
# contains the headers that are needed for the C++ parser to work (see boo#1119186)
Requires:       clang%(rpm -q --qf '%''{version}' clang-devel | cut -d. -f1)
Recommends:     clazy
Recommends:     cppcheck
Recommends:     heaptrack-gui
# Used by the docker plugin
Recommends:     /usr/bin/pkexec
Conflicts:      kdevelop4
Conflicts:      kdevelop4-plugin-clang
# To allow "zypper in kdevelop"
Provides:       kdevelop = %{version}
# The following plugins were provided by the KDE repos providing unstable packages
Provides:       kdevelop5-cpp-parser
Provides:       kdevelop5-plugin-qmljs = %{version}
Obsoletes:      kdevelop5-plugin-qmljs < %{version}
Provides:       kdevelop5-plugin-clang = %{version}
Obsoletes:      kdevelop5-plugin-clang < %{version}
Provides:       kdevelop5-plugin-qmake = %{version}
Obsoletes:      kdevelop5-plugin-qmake < %{version}
Provides:       kdevelop5-plugin-cppsupport = %{version}
Obsoletes:      kdevelop5-plugin-cppsupport < %{version}
# Available separately before, now included in kdevelop5 itself
Provides:       kdevelop5-plugin-clang-tidy = %{version}
Obsoletes:      kdevelop5-plugin-clang-tidy < %{version}

%description
KDevelop is an integrated development environment (IDE).
It provides editing, navigation and debugging features for several programming languages,
as well as integration with multiple build systems and version-control systems
using a plugin-based architecture.
KDevelop has parser backends for C, C++ and Javascript/QML,
with further external plugins supporting e.g. PHP or Python.

%package -n kdevplatform
Summary:        Base Package for Integrated Development Environments
Requires:       libkdevplatform%{libkdev_major} = %{version}
%requires_eq    grantlee5
Conflicts:      kdevplatform4
Conflicts:      libkdevplatform4-devel

%description -n kdevplatform
This package contains the common plugins for integrated developments
environment based on the KDevelop framework.

%package -n libkdevplatform%{libkdev_major}
Summary:        Libraries for Integrated Development Environments
Requires:       kdevplatform
Obsoletes:      libkdevplatform10 < %{version}

%description -n libkdevplatform%{libkdev_major}
This package contains the libraries for integrated development
environments based on the KDevelop framework.

%package -n kdevplatform-devel
Summary:        Base Package for Integrated Development Environments: Build Environment
Requires:       libkdevplatform%{libkdev_major} = %{version}
# Not installed automatically
Requires:       cmake(KF5TextEditor)
Requires:       cmake(KF5ThreadWeaver)
Conflicts:      libkdevplatform4-devel

%description -n kdevplatform-devel
This package contains the development files for building integrated
developments environments based on the KDevelop framework.

%package lang
Summary:        Translations for package %{name}
Requires:       %{name} = %{version}
Provides:       %{name}-lang-all = %{version}
Conflicts:      kdevelop4-lang
# Available separately before, now included in kdevelop5 itself
Provides:       kdevelop5-plugin-clang-tidy-lang = %{version}
Obsoletes:      kdevelop5-plugin-clang-tidy-lang < %{version}
BuildArch:      noarch

%description lang
Provides translations for the "kdevelop" package.

%package -n kdevplatform-lang
Summary:        Translations for package kdevplatform
Requires:       kdevplatform = %{version}
Conflicts:      kdevplatform4-lang
Provides:       kdevplatform-lang-all = %{version}
BuildArch:      noarch

%description -n kdevplatform-lang
Provides translations for the "kdevplatform" package.

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf5 -d build
%make_jobs

%install
%kf5_makeinstall -C build

names="kdevandroid kdevappwizard kdevastyle kdevbazaar kdevclang kdevclassbrowser \
      kdevclangtidy kdevclazy kdevcmake kdevcmakebuilder kdevcodeutils kdevcompileanalyzercommon \
      kdevcontextbrowser kdevcppcheck kdevcustombuildsystem kdevcustomdefinesandincludes \
      kdevcustommake kdevcustomscript kdevdebuggercommon kdevdocker kdevdocumentswitcher \
      kdevdocumentview kdevelop kdevexecute kdevexecuteplasmoid kdevexecutescript \
      kdevexternalscript kdevfilemanager kdevfiletemplates kdevflatpak kdevgdb \
      kdevghprovider kdevgit kdevgrepview kdevheaptrack kdevkonsole kdevlldb \
      kdevmakebuilder kdevmanpage kdevmesonmanager kdevninja kdevokteta kdevopenwith
      kdevpatchreview kdevperforce kdevproblemreporter kdevprojectfilter kdevprojectmanagerview \
      kdevqmakebuilder kdevqmakemanager kdevqmljs kdevqthelp kdevquickopen kdevscratchpad \
      kdevsourceformatter kdevoutlineview kdevstandardoutputview kdevsubversion  \
      kdevswitchtobuddy kdevtestview kdevvcsprojectintegration kdevwelcomepage \
      plasma_applet_kdevelopsessions plasma_runner_kdevelopsessions"

for name in $names; do
  %find_lang $name %{name}.lang
done

%find_lang kdevplatform kdevplatform.lang
%{kf5_find_htmldocs}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%post -n kdevplatform -p /sbin/ldconfig
%postun -n kdevplatform -p /sbin/ldconfig
%post -n libkdevplatform%{libkdev_major} -p /sbin/ldconfig
%postun -n libkdevplatform%{libkdev_major} -p /sbin/ldconfig

%files -n libkdevplatform%{libkdev_major}
%license LICENSES/*
%{_kf5_libdir}/libKDevPlatform*.so.%{libkdev_major}
%{_kf5_libdir}/libKDevPlatform*.so.5.*

%files
%doc README.md
%dir %{_kf5_iconsdir}/hicolor/1024x1024
%dir %{_kf5_iconsdir}/hicolor/1024x1024/apps
%dir %{_kf5_iconsdir}/hicolor/256x256
%dir %{_kf5_iconsdir}/hicolor/256x256/apps
%dir %{_kf5_iconsdir}/hicolor/512x512
%dir %{_kf5_iconsdir}/hicolor/512x512/apps
%dir %{_kf5_plugindir}/kf5
%dir %{_kf5_plugindir}/kf5/krunner
%doc %lang(en) %{_kf5_htmldir}/en/kdevelop
%exclude %{_kf5_iconsdir}/hicolor/*/actions/breakpoint.*
%{_kf5_applicationsdir}/*kdevelop*.desktop
%{_kf5_appstreamdir}/org.kde.kdevelop.appdata.xml
%{_kf5_bindir}/kdev_includepathsconverter
%{_kf5_bindir}/kdevelop*
%{_kf5_debugdir}/kdevelop.categories
%{_kf5_iconsdir}/*/*/*/*
%{_kf5_libdir}/cmake/KDevelop/
%{_kf5_libdir}/libKDevCMakeCommon.so.*
%{_kf5_libdir}/libKDevClangPrivate.so.*
%{_kf5_libdir}/libKDevCompileAnalyzerCommon.so.*
%{_kf5_libdir}/libKDevelopSessionsWatch.so
%{_kf5_notifydir}/kdevelop.notifyrc
%{_kf5_plasmadir}/
%{_kf5_plugindir}/kdevplatform/
%{_kf5_plugindir}/kf5/krunner/krunner_kdevelopsessions.so
%{_kf5_prefix}/include/kdevelop/
%{_kf5_qmldir}/
%{_kf5_servicesdir}/plasma-applet-kdevelopsessions.desktop
%{_kf5_sharedir}/kdevappwizard/
%{_kf5_sharedir}/kdevclangsupport/
%{_kf5_sharedir}/kdevcodegen/
%{_kf5_sharedir}/kdevcodeutils/
%{_kf5_sharedir}/kdevelop/
%{_kf5_sharedir}/kdevfiletemplates/
%{_kf5_sharedir}/kdevgdb/
%{_kf5_sharedir}/kdevlldb/
%{_kf5_sharedir}/kdevmanpage/
%{_kf5_sharedir}/kdevqmljssupport/
%{_kf5_sharedir}/knsrcfiles/kdevappwizard.knsrc
%{_kf5_sharedir}/knsrcfiles/kdevelop-qthelp.knsrc
%{_kf5_sharedir}/knsrcfiles/kdevfiletemplates.knsrc
%{_kf5_sharedir}/mime/packages/kdevclang.xml
%{_kf5_sharedir}/mime/packages/kdevelop.xml
%{_kf5_sharedir}/mime/packages/kdevgit.xml

%files -n kdevplatform
%doc kdevplatform/README.md
%{_kf5_bindir}/kdev_dbus_socket_transformer
%{_kf5_bindir}/kdev_format_source
%{_kf5_bindir}/kdevplatform_shell_environment.sh
%{_kf5_debugdir}/kdevplatform.categories
%{_kf5_iconsdir}/hicolor/*/actions/breakpoint.*
%{_kf5_plugindir}/grantlee/
%{_kf5_servicetypesdir}/
%{_kf5_sharedir}/kdevplatform/

%files -n kdevplatform-devel
%{_kf5_libdir}/cmake/KDevPlatform/
%{_kf5_libdir}/libKDevPlatform*.so
%{_kf5_prefix}/include/kdevplatform/

%files lang -f %{name}.lang

%files -n kdevplatform-lang -f kdevplatform.lang

%changelog
