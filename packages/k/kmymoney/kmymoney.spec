#
# spec file for package kmymoney
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


%bcond_without lang
# Only include WebEngine for platforms that support it
%ifarch %{ix86} x86_64 %{arm} aarch64 mips mips64
%bcond_without qtwebengine
%else
%bcond_with qtwebengine
%endif
Name:           kmymoney
Version:        5.1.0
Release:        0
Summary:        A Personal Finance Manager by KDE
License:        GPL-2.0-only OR GPL-3.0-only
Group:          Productivity/Office/Finance
URL:            https://www.kmymoney.org/
Source0:        https://download.kde.org/stable/kmymoney/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:  doxygen
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  kdiagram-devel
BuildRequires:  kf5-filesystem
BuildRequires:  libQt5Sql-private-headers-devel
BuildRequires:  libalkimia5-devel >= 7.0
BuildRequires:  libofx-devel
BuildRequires:  libqgpgme-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  cmake(KF5Activities)
BuildRequires:  cmake(KF5Akonadi)
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5Completion)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5Contacts)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5Holidays)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5IdentityManagement)
BuildRequires:  cmake(KF5ItemModels)
BuildRequires:  cmake(KF5ItemViews)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5Service)
BuildRequires:  cmake(KF5TextWidgets)
BuildRequires:  cmake(KF5Wallet)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Concurrent) >= 5.6.0
BuildRequires:  cmake(Qt5Core) >= 5.6.0
BuildRequires:  cmake(Qt5DBus) >= 5.6.0
BuildRequires:  cmake(Qt5PrintSupport) >= 5.6.0
BuildRequires:  cmake(Qt5QuickWidgets) >= 5.6.0
BuildRequires:  cmake(Qt5Sql) >= 5.6.0
BuildRequires:  cmake(Qt5Svg) >= 5.6.0
BuildRequires:  cmake(Qt5Test) >= 5.6.0
BuildRequires:  cmake(Qt5Widgets) >= 5.6.0
BuildRequires:  cmake(Qt5Xml) >= 5.6.0
BuildRequires:  cmake(aqbanking) >= 6.0.1
BuildRequires:  pkgconfig(libical)
BuildRequires:  pkgconfig(sqlcipher)
BuildRequires:  pkgconfig(sqlite3)
Recommends:     %{name}-lang = %{version}
# For users of KDE:Unstable:Extra
Provides:       kmymoney5 = %{version}
Obsoletes:      kmymoney5 < %{version}
Provides:       kmymoney-doc = %{version}
Obsoletes:      kmymoney-doc < %{version}
%if %{with qtwebengine}
BuildRequires:  cmake(Qt5WebEngine) >= 5.8.0
%else
BuildRequires:  cmake(KF5WebKit)
%endif

%description
KMyMoney is a Personal Finance Manager by KDE. It operates
similar to Quicken, supports various account types, categorization
of expenses, multiple currencies, online banking support via QIF,
OFX and HBCI, budgeting and a rich set of reports.

%package devel
Summary:        Development Files for KMyMoney
Group:          Development/Languages/C and C++
Requires:       %{name} = %{version}

%description devel
Development files and headers need to build software using KMyMoney.

%lang_package

%prep
%setup -q

%build
%if %{with qtwebengine}
%cmake_kf5 -d build -- -DENABLE_WEBENGINE=ON
%else
%cmake_kf5 -d build
%endif
%cmake_build

%install
%kf5_makeinstall -C build
%fdupes -s %{buildroot}

%if %{with lang}
%find_lang %{name} --with-man
%{kf5_find_htmldocs}
%endif

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license COPYING
%doc %lang(en) %{_kf5_htmldir}/en/kmymoney/
%doc AUTHORS ChangeLog ChangeLog.original README.Fileformats
%{_datadir}/mime/packages/x-kmymoney.xml
%{_kf5_applicationsdir}/org.kde.kmymoney.desktop
%{_kf5_appsdir}/kbanking/
%{_kf5_appsdir}/kmymoney/
%{_kf5_appstreamdir}/org.kde.kmymoney.appdata.xml
%{_kf5_bindir}/kmymoney
%{_kf5_configkcfgdir}/
%{_kf5_iconsdir}/hicolor/*/*/*
%{_kf5_kxmlguidir}/
%{_kf5_libdir}/libkmm_csvimportercore.so.*
%{_kf5_libdir}/libkmm_icons.so.*
%{_kf5_libdir}/libkmm_menus.so.*
%{_kf5_libdir}/libkmm_models.so.*
%{_kf5_libdir}/libkmm_mymoney.so.*
%{_kf5_libdir}/libkmm_payeeidentifier.so.*
%{_kf5_libdir}/libkmm_plugin.so.*
%{_kf5_libdir}/libkmm_printer.so.*
%{_kf5_libdir}/libkmm_settings.so.*
%{_kf5_libdir}/libkmm_widgets.so.*
%{_kf5_plugindir}/
%{_kf5_servicesdir}/*.desktop
%{_kf5_servicetypesdir}/*.desktop
%{_kf5_sharedir}/checkprinting/
%{_kf5_sharedir}/kconf_update/
%{_mandir}/man1/kmymoney.1%{?ext_man}

%files devel
%{_includedir}/kmymoney/
%{_kf5_libdir}/libkmm_csvimportercore.so
%{_kf5_libdir}/libkmm_icons.so
%{_kf5_libdir}/libkmm_menus.so
%{_kf5_libdir}/libkmm_models.so
%{_kf5_libdir}/libkmm_mymoney.so
%{_kf5_libdir}/libkmm_payeeidentifier.so
%{_kf5_libdir}/libkmm_plugin.so
%{_kf5_libdir}/libkmm_printer.so
%{_kf5_libdir}/libkmm_settings.so
%{_kf5_libdir}/libkmm_widgets.so

%if %{with lang}
%files lang -f %{name}.lang
%endif

%changelog
