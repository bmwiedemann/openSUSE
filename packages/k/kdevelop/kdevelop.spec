#
# spec file for package kdevelop
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



%define kf6_version 6.6.0
%define qt6_version 6.6.0

%define libkdev_major 61

%bcond_without released
Name:           kdevelop
Version:        24.12.2
Release:        0
Summary:        Plugin-extensible IDE for C/C++ and other programming languages
License:        GPL-2.0-or-later
URL:            https://www.kdevelop.org
Source:         %{name}-%{version}.tar.xz
%if %{with released}
Source1:        %{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  clang-devel
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  kdevelop-pg-qt >= 1.9
BuildRequires:  libboost_headers-devel
# TODO: not ported to Qt6. Expected: 10/2024
# BuildRequires:  okteta-devel
BuildRequires:  shared-mime-info
BuildRequires:  subversion-devel
BuildRequires:  cmake(KF6Archive) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6ItemModels) >= %{kf6_version}
BuildRequires:  cmake(KF6ItemViews) >= %{kf6_version}
BuildRequires:  cmake(KF6JobWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6NewStuff) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6NotifyConfig) >= %{kf6_version}
BuildRequires:  cmake(KF6Parts) >= %{kf6_version}
BuildRequires:  cmake(KF6Purpose) >= %{kf6_version}
BuildRequires:  cmake(KF6Runner) >= %{kf6_version}
BuildRequires:  cmake(KF6Service) >= %{kf6_version}
BuildRequires:  cmake(KF6Sonnet) >= %{kf6_version}
BuildRequires:  cmake(KF6TextEditor) >= %{kf6_version}
BuildRequires:  cmake(KF6TextTemplate) >= %{kf6_version}
BuildRequires:  cmake(KF6TextWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6ThreadWeaver) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(KSysGuard) >= 6.0.0
BuildRequires:  cmake(KompareDiff2) >= 6.0
BuildRequires:  cmake(Plasma) >= 6.0.0
BuildRequires:  cmake(Qt6Concurrent) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core5Compat) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Help) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6WebEngineWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
# contains the headers that are needed for the C++ parser to work (see boo#1119186)
Requires:       clang%(rpm -q --qf '%''{version}' clang-devel | cut -d. -f1)
# Used by the docker plugin
Recommends:     %{_bindir}/pkexec
Recommends:     clazy
Recommends:     cppcheck
Recommends:     heaptrack
Recommends:     heaptrack-gui
Recommends:     meson
Conflicts:      kdevelop4
Conflicts:      kdevelop4-plugin-clang
Provides:       kdevelop5 = %{version}
Obsoletes:      kdevelop5 < %{version}
# Available separately before, now included in kdevelop5 itself
Provides:       kdevelop5-plugin-clang-tidy = %{version}
Obsoletes:      kdevelop5-plugin-clang-tidy < %{version}
ExclusiveArch:  aarch64 x86_64 %{x86_64} riscv64

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
Requires:       cmake(KF6TextEditor) >= %{kf6_version}
Requires:       cmake(KF6ThreadWeaver) >= %{kf6_version}
Requires:       cmake(Qt6Core5Compat) >= %{qt6_version}
Requires:       cmake(Qt6Test) >= %{qt6_version}
Requires:       cmake(Qt6WebEngineWidgets) >= %{qt6_version}
Conflicts:      libkdevplatform4-devel

%description -n kdevplatform-devel
This package contains the development files for building integrated
developments environments based on the KDevelop framework.

%package lang
Summary:        Translations for package kdevelop
Requires:       kdevelop = %{version}
Conflicts:      kdevelop4-lang
Provides:       kdevelop-lang-all = %{version}
Obsoletes:      kdevelop5-lang < %{version}
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
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

names="kdevandroid kdevappwizard kdevastyle kdevbazaar kdevclang kdevclassbrowser \
      kdevclangtidy kdevclazy kdevcmake kdevcmakebuilder kdevcodeutils kdevcompileanalyzercommon \
      kdevcontextbrowser kdevcppcheck kdevcustombuildsystem kdevcustomdefinesandincludes \
      kdevcustommake kdevcustomscript kdevdebuggercommon kdevdocker kdevdocumentswitcher \
      kdevdocumentview kdevexecute kdevexecuteplasmoid kdevexecutescript \
      kdevexternalscript kdevfilemanager kdevfiletemplates kdevflatpak kdevgdb \
      kdevghprovider kdevgit kdevgrepview kdevheaptrack kdevkonsole kdevlldb \
      kdevmakebuilder kdevmanpage kdevmesonmanager kdevninja kdevokteta kdevopenwith \
      kdevpatchreview kdevperforce kdevproblemreporter kdevprojectfilter kdevprojectmanagerview \
      kdevqmakebuilder kdevqmakemanager kdevqmljs kdevqthelp kdevquickopen kdevscratchpad \
      kdevsourceformatter kdevoutlineview kdevstandardoutputview kdevsubversion  \
      kdevswitchtobuddy kdevtestview kdevvcsprojectintegration kdevwelcomepage \
      plasma_applet_kdevelopsessions plasma_runner_kdevelopsessions"

for name in $names; do
  %find_lang $name kdevelop.lang
done
%find_lang kdevelop kdevelop.lang --with-html

%find_lang kdevplatform kdevplatform.lang

%ldconfig_scriptlets
%ldconfig_scriptlets -n kdevplatform
%ldconfig_scriptlets -n libkdevplatform%{libkdev_major}

%files -n libkdevplatform%{libkdev_major}
%license LICENSES/*
%{_kf6_libdir}/libKDevPlatform*.so.*

%files
%doc README.md
%doc %lang(en) %{_kf6_htmldir}/en/kdevelop/
%{_includedir}/kdevelop/
%{_kf6_applicationsdir}/org.kde.kdevelop*.desktop
%{_kf6_appstreamdir}/org.kde.kdevelop.appdata.xml
%{_kf6_appstreamdir}/org.kde.kdevelopsessions.appdata.xml
%{_kf6_bindir}/kdev_includepathsconverter
%{_kf6_bindir}/kdevelop*
%{_kf6_cmakedir}/KDevelop/
%{_kf6_debugdir}/kdevelop.categories
%dir %{_kf6_iconsdir}/hicolor/1024x1024
%dir %{_kf6_iconsdir}/hicolor/1024x1024/apps
%dir %{_kf6_iconsdir}/hicolor/256x256
%dir %{_kf6_iconsdir}/hicolor/256x256/apps
%dir %{_kf6_iconsdir}/hicolor/512x512
%dir %{_kf6_iconsdir}/hicolor/512x512/apps
%{_kf6_iconsdir}/*/*/*/*
%{_kf6_libdir}/libKDevCMakeCommon.so.*
%{_kf6_libdir}/libKDevClangPrivate.so.*
%{_kf6_libdir}/libKDevCompileAnalyzerCommon.so.*
%{_kf6_libdir}/libKDevelopSessionsWatch.so
%{_kf6_notificationsdir}/kdevelop.notifyrc
%{_kf6_plasmadir}/plasmoids/org.kde.kdevelopsessions/
%{_kf6_plugindir}/kdevplatform/
%dir %{_kf6_plugindir}/kf6/krunner
%{_kf6_plugindir}/kf6/krunner/kdevelopsessions.so
%dir %{_kf6_plugindir}/kf6/ktexttemplate
%{_kf6_plugindir}/kf6/ktexttemplate/kdev_filters.so
%dir %{_kf6_qmldir}/org/kde/plasma
%dir %{_kf6_qmldir}/org/kde/plasma/private
%{_kf6_qmldir}/org/kde/plasma/private/kdevelopsessions/
%{_kf6_sharedir}/kdevappwizard/
%{_kf6_sharedir}/kdevclangsupport/
%{_kf6_sharedir}/kdevcodegen/
%{_kf6_sharedir}/kdevcodeutils/
%{_kf6_sharedir}/kdevelop/
%{_kf6_sharedir}/kdevfiletemplates/
%{_kf6_sharedir}/kdevgdb/
%{_kf6_sharedir}/kdevlldb/
%{_kf6_sharedir}/kdevmanpage/
%{_kf6_sharedir}/knsrcfiles/kdevappwizard.knsrc
%{_kf6_sharedir}/knsrcfiles/kdevelop-qthelp.knsrc
%{_kf6_sharedir}/knsrcfiles/kdevfiletemplates.knsrc
%{_kf6_sharedir}/mime/packages/kdevclang.xml
%{_kf6_sharedir}/mime/packages/kdevelop.xml
%{_kf6_sharedir}/mime/packages/kdevgit.xml
%exclude %{_kf6_iconsdir}/hicolor/*/actions/breakpoint.*

%files -n kdevplatform
%doc kdevplatform/README.md
%{_kf6_bindir}/kdev_dbus_socket_transformer
%{_kf6_bindir}/kdev_format_source
%{_kf6_bindir}/kdevplatform_shell_environment.sh
%{_kf6_debugdir}/kdevplatform.categories
%{_kf6_iconsdir}/hicolor/*/actions/breakpoint.*
%dir %{_kf6_sharedir}/kdevplatform/
%{_kf6_sharedir}/kdevplatform/shellutils/

%files -n kdevplatform-devel
%{_includedir}/kdevplatform/
%{_kf6_cmakedir}/KDevPlatform/
%{_kf6_libdir}/libKDevPlatform*.so

%files lang -f kdevelop.lang
%exclude %{_kf6_htmldir}/en/kdevelop

%files -n kdevplatform-lang -f kdevplatform.lang

%changelog
