#
# spec file for package skrooge
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2008 - 2012 Sascha Manns <saigkill@opensuse.org>
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


%define kf6_version 6.3.0
%define qt6_version 6.6.0

%bcond_without released
%ifarch x86_64 %{x86_64} aarch64 riscv64
# Only include WebEngine for platforms that support it
%define with_qtwebengine 1
%endif
Name:           skrooge
Version:        25.1.0
Release:        0
Summary:        A Personal Finance Management Tool
License:        GPL-3.0-only
Group:          Productivity/Office/Finance
URL:            https://www.skrooge.org/
Source:         https://download.kde.org/stable/skrooge/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/skrooge/%{name}-%{version}.tar.xz.sig
# https://invent.kde.org/sysadmin/release-keyring/-/blob/master/keys/smankowski@key2.asc?ref_type=heads
Source2:        skrooge.keyring
%endif
BuildRequires:  kf6-breeze-icons
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  libofx-devel
BuildRequires:  qt6-sql-private-devel >= %{qt6_version}
BuildRequires:  shared-mime-info
BuildRequires:  sqlcipher-devel
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6Archive) >= %{kf6_version}
BuildRequires:  cmake(KF6ColorScheme) >= %{kf6_version}
BuildRequires:  cmake(KF6Completion) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6ItemViews) >= %{kf6_version}
BuildRequires:  cmake(KF6JobWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6NewStuff) >= %{kf6_version}
BuildRequires:  cmake(KF6NewStuffCore) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6NotifyConfig) >= %{kf6_version}
BuildRequires:  cmake(KF6Parts) >= %{kf6_version}
BuildRequires:  cmake(KF6Runner) >= %{kf6_version}
BuildRequires:  cmake(KF6StatusNotifierItem) >= %{kf6_version}
BuildRequires:  cmake(KF6TextTemplate)
BuildRequires:  cmake(KF6Wallet) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(PlasmaActivities)
BuildRequires:  cmake(Qt6Concurrent) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core5Compat) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Designer) >= %{qt6_version}
BuildRequires:  cmake(Qt6PrintSupport) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickControls2) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Sql) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
%if 0%{?with_qtwebengine}
BuildRequires:  cmake(Qt6WebEngineWidgets) >= %{qt6_version}
%endif
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Xml) >= %{qt6_version}
Requires:       hicolor-icon-theme
Requires:       qt6-sql-sqlite >= %{qt6_version}

%description
Skrooge allows managing personal finances, powered by KDE.
It has many features and can be used to enter, follow, and
analyze expenses.

%lang_package

%prep
%autosetup -p1

%build
%if 0%{?with_qtwebengine}
%cmake_kf6 -DSKG_WEBENGINE:BOOL=TRUE -DBUILD_WITH_QT6:BOOL=TRUE
%else
%cmake_kf6 -DSKG_WEBENGINE:BOOL=FALSE -DBUILD_WITH_QT6:BOOL=TRUE
%endif

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-html --all-name --with-kde

%fdupes %{buildroot}

# E: env-script-interpreter
sed -i 's#env python3#python3#' %{buildroot}%{_kf6_sharedir}/skrooge/*.py

%ldconfig_scriptlets

%files
%license COPYING
%doc CHANGELOG README.md AUTHORS
%doc %lang(en) %{_kf6_htmldir}/en/skrooge/
%{_kf6_applicationsdir}/org.kde.skrooge.desktop
%{_kf6_appstreamdir}/org.kde.skrooge.appdata.xml
%{_kf6_bindir}/skrooge*
%{_kf6_configkcfgdir}/skg*.kcfg
%{_kf6_iconsdir}/breeze*/actions/22/*.svgz
%{_kf6_iconsdir}/hicolor/*/*/*
%{_kf6_knsrcfilesdir}/skrooge_*.knsrc
%{_kf6_kxmlguidir}/*
%{_kf6_libdir}/libskgbankgui.so.*
%{_kf6_libdir}/libskgbankmodeler.so.*
%{_kf6_libdir}/libskgbasegui.so.*
%{_kf6_libdir}/libskgbasemodeler.so.*
%{_kf6_notificationsdir}/skrooge.notifyrc
# %%{_kf6_plugindir}/designer/libskgbankguidesigner.so
# %%{_kf6_plugindir}/designer/libskgbaseguidesigner.so
%dir %{_kf6_plugindir}/kf6/ktexttemplate
%{_kf6_plugindir}/kf6/ktexttemplate/grantlee_skgfilters.so
%{_kf6_plugindir}/skg_gui/
%{_kf6_plugindir}/skrooge_import/
%{_kf6_plugindir}/sqldrivers/libskgsqlcipher.so
%{_kf6_sharedir}/mime/packages/x-skg.xml
%{_kf6_sharedir}/skrooge/
%{_kf6_sharedir}/skrooge_import_backend/
%{_kf6_sharedir}/skrooge_source/

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/skrooge/

%changelog
