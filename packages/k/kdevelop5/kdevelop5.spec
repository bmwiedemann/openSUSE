#
# spec file for package kdevelop5
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


%define rname   kdevelop
%define libkdev_major 56
Name:           kdevelop5
Version:        5.6.0
Release:        0
Summary:        Plugin-extensible IDE for C/C++ and other programming languages
License:        GPL-2.0-or-later
Group:          Development/Tools/IDE
URL:            https://www.kdevelop.org
Source0:        https://download.kde.org/stable/%{rname}/%{version}/src/%{rname}-%{version}.tar.xz
BuildRequires:  kdevelop5-pg-qt
BuildRequires:  kf5-filesystem
BuildRequires:  libboost_headers-devel
BuildRequires:  llvm-clang-devel
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
%ifarch %{ix86} x86_64 %{arm} aarch64 mips mips64
BuildRequires:  cmake(Qt5WebEngineWidgets)
%else
BuildRequires:  cmake(Qt5WebKitWidgets)
%endif
BuildRequires:  cmake(Qt5Widgets)
# contains the headers that are needed for the C++ parser to work (see boo#1119186)
Requires:       clang%(rpm -q --qf '%''{version}' clang-devel | cut -d. -f1)
Recommends:     %{name}-lang
Recommends:     clazy
Recommends:     cppcheck
Recommends:     heaptrack-gui
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
Group:          Development/Tools/IDE
Requires:       libkdevplatform%{libkdev_major} = %{version}
%requires_eq    grantlee5
Recommends:     kdevplatform-lang
Conflicts:      kdevplatform4
Conflicts:      libkdevplatform4-devel

%description -n kdevplatform
This package contains the common plugins for integrated developments
environment based on the KDevelop framework.

%package -n libkdevplatform%{libkdev_major}
Summary:        Libraries for Integrated Development Environments
Group:          Development/Tools/IDE
Requires:       kdevplatform
Obsoletes:      libkdevplatform10 < %{version}

%description -n libkdevplatform%{libkdev_major}
This package contains the libraries for integrated development
environments based on the KDevelop framework.

%package -n kdevplatform-devel
Summary:        Base Package for Integrated Development Environments: Build Environment
Group:          Development/Tools/IDE
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
Group:          System/Localization
Requires:       %{name} = %{version}
Supplements:    (bundle-lang-other and %{name})
Conflicts:      kdevelop4-lang
Provides:       %{name}-lang-all = %{version}
# Available separately before, now included in kdevelop5 itself
Provides:       kdevelop5-plugin-clang-tidy-lang = %{version}
Obsoletes:      kdevelop5-plugin-clang-tidy-lang < %{version}
BuildArch:      noarch

%description lang
Provides translations to the package %{name}

%package -n kdevplatform-lang
Summary:        Translations for package kdevplatform
Group:          System/Localization
Requires:       kdevplatform = %{version}
Supplements:    (bundle-lang-other and kdevplatform)
Conflicts:      kdevplatform4-lang
Provides:       kdevplatform-lang-all = %{version}
BuildArch:      noarch

%description -n kdevplatform-lang
Provides translations to the package kdevplatform

%prep
%setup -q -n %{rname}-%{version}

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

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%post -n kdevplatform -p /sbin/ldconfig
%postun -n kdevplatform -p /sbin/ldconfig
%post -n libkdevplatform%{libkdev_major} -p /sbin/ldconfig
%postun -n libkdevplatform%{libkdev_major} -p /sbin/ldconfig

%files -n libkdevplatform%{libkdev_major}
%license kdevplatform/COPYING*
%{_kf5_libdir}/libKDevPlatform*.so.%{libkdev_major}
%{_kf5_libdir}/libKDevPlatform*.so.5.*

%files
%license COPYING*
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
%if %pkg_vcmp knewstuff-devel >= 5.57.0
# It installs .knsrc files when built with knewstuff-devel >= 5.57.0
%{_kf5_knsrcfilesdir}/kdevappwizard.knsrc
%{_kf5_knsrcfilesdir}/kdevelop-qthelp.knsrc
%{_kf5_knsrcfilesdir}/kdevfiletemplates.knsrc
%endif
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
%if %pkg_vcmp krunner-devel < 5.72.0
# Only installed when built with krunner < 5.72.0
%{_kf5_servicesdir}/kdevelopsessions.desktop
%endif
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
%{_kf5_sharedir}/mime/packages/kdevclang.xml
%{_kf5_sharedir}/mime/packages/kdevelop.xml
%{_kf5_sharedir}/mime/packages/kdevgit.xml

%files lang -f %{name}.lang

%files -n kdevplatform-lang -f kdevplatform.lang

%files -n kdevplatform
%license kdevplatform/COPYING*
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
%license kdevplatform/COPYING*
%{_kf5_libdir}/cmake/KDevPlatform/
%{_kf5_libdir}/libKDevPlatform*.so
%{_kf5_prefix}/include/kdevplatform/

%changelog
