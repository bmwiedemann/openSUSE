#
# spec file for package skrooge
#
# Copyright (c) 2020 SUSE LLC
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


%ifarch %{ix86} x86_64 %{arm} aarch64 mips mips64
# Only include WebEngine for platforms that support it
%bcond_without qtwebengine
%else
%bcond_with qtwebengine
%endif
Name:           skrooge
Version:        2.23.0
Release:        0
Summary:        A Personal Finance Management Tool
License:        GPL-3.0-only
Group:          Productivity/Office/Finance
URL:            https://www.skrooge.org/
Source:         https://download.kde.org/stable/skrooge/%{name}-%{version}.tar.xz
BuildRequires:  breeze5-icons
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  grantlee5-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  libQt5Sql-private-headers-devel
BuildRequires:  libofx-devel
BuildRequires:  libqca-qt5-devel
BuildRequires:  libxslt-tools
BuildRequires:  pkgconfig
BuildRequires:  shared-mime-info
BuildRequires:  sqlcipher-devel
BuildRequires:  sqlite-devel
BuildRequires:  cmake(KF5Activities)
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5Completion)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5DesignerPlugin)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5ItemViews)
BuildRequires:  cmake(KF5JobWidgets)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5NewStuff)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5NotifyConfig)
BuildRequires:  cmake(KF5Parts)
BuildRequires:  cmake(KF5Runner)
BuildRequires:  cmake(KF5Wallet)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Designer)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5QuickWidgets)
BuildRequires:  cmake(Qt5Script)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
Recommends:     %{name}-lang = %{version}
%if %{with qtwebengine}
BuildRequires:  cmake(Qt5WebEngineWidgets)
%else
BuildRequires:  cmake(Qt5WebKitWidgets)
%endif
Requires:       hicolor-icon-theme

%description
Skrooge allows managing personal finances, powered by KDE.
It has many features and can be used to enter, follow, and
analyze expenses.

%lang_package

%prep
%setup -q

%build
%if %{with qtwebengine}
%cmake_kf5 -- -DSKG_WEBENGINE=ON
%else
%cmake_kf5
%endif

%cmake_build

%install
%kf5_makeinstall

%find_lang %{name} --with-kde
%{kf5_find_htmldocs}
%fdupes -s %{buildroot}

%{kf5_post_install}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING
%doc CHANGELOG README AUTHORS
%doc %lang(en) %{_kf5_htmldir}/en/skrooge/
%config %{_sysconfdir}/xdg/skrooge_*.knsrc
%dir %{_kf5_appstreamdir}
%dir %{_kf5_iconsdir}/breeze
%dir %{_kf5_iconsdir}/breeze-dark
%dir %{_kf5_iconsdir}/breeze-dark/actions
%dir %{_kf5_iconsdir}/breeze-dark/actions/22
%dir %{_kf5_iconsdir}/breeze/actions
%dir %{_kf5_iconsdir}/breeze/actions/22
%dir %{_kf5_iconsdir}/hicolor/512x512
%dir %{_kf5_iconsdir}/hicolor/512x512/actions
%dir %{_kf5_iconsdir}/hicolor/512x512/apps
%dir %{_kf5_iconsdir}/hicolor/512x512/mimetypes
%dir %{_kf5_sharedir}/config.kcfg
%{_kf5_appstreamdir}/org.kde.%{name}.appdata.xml
%{_kf5_bindir}/%{name}*
%{_kf5_iconsdir}/breeze*/actions/22/*.svgz
%{_kf5_iconsdir}/hicolor/*/*/%{name}*.svgz
%{_kf5_iconsdir}/hicolor/*/*/skg*.svgz
%{_kf5_iconsdir}/hicolor/*/actions/*.png
%{_kf5_iconsdir}/hicolor/*/apps/*.png
%{_kf5_iconsdir}/hicolor/*/mimetypes/*.png
%{_kf5_iconsdir}/hicolor/*/mimetypes/*.svgz
%{_kf5_kxmlguidir}/*
%{_kf5_libdir}/libskgbankgui.so.%{version}
%{_kf5_libdir}/libskgbankgui.so.2
%{_kf5_libdir}/libskgbankmodeler.so.%{version}
%{_kf5_libdir}/libskgbankmodeler.so.2
%{_kf5_libdir}/libskgbasegui.so.%{version}
%{_kf5_libdir}/libskgbasegui.so.2
%{_kf5_libdir}/libskgbasemodeler.so.%{version}
%{_kf5_libdir}/libskgbasemodeler.so.2
%{_kf5_notifydir}/%{name}.notifyrc
%{_kf5_plugindir}/%{name}_*.so
%{_kf5_plugindir}/designer/libskgbankguidesigner.so
%{_kf5_plugindir}/designer/libskgbaseguidesigner.so
%{_kf5_plugindir}/grantlee
%{_kf5_plugindir}/skg_*.so
%{_kf5_plugindir}/sqldrivers/libskgsqlcipher.so
%{_kf5_servicesdir}/org.kde.*
%{_kf5_servicesdir}/sources/
%{_kf5_servicetypesdir}/org.kde.*
%{_kf5_sharedir}/%{name}
%{_kf5_sharedir}/applications/org.kde.%{name}.desktop
%{_kf5_sharedir}/config.kcfg/skg*.kcfg
%{_kf5_sharedir}/mime/packages/x-skg.xml

%files lang -f %{name}.lang

%changelog
