#
# spec file for package okteta
#
# Copyright (c) 2023 SUSE LLC
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


%define Kasten_sover 4
%define Okteta_sover 3
%bcond_without released
Name:           okteta
Version:        0.26.10
Release:        0
Summary:        Hex Editor
License:        GFDL-1.2-only AND GPL-2.0-only
Group:          Development/Tools/Other
URL:            https://apps.kde.org/okteta
Source0:        https://download.kde.org/stable/okteta/%{version}/src/okteta-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/okteta/%{version}/src/okteta-%{version}.tar.xz.sig
Source2:        okteta.keyring
%endif
Source99:       okteta-rpmlintrc
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules >= 5.48.0
BuildRequires:  kf5-filesystem
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Bookmarks)
BuildRequires:  cmake(KF5Codecs)
BuildRequires:  cmake(KF5Completion)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5NewStuff)
BuildRequires:  cmake(KF5Parts)
BuildRequires:  cmake(KF5Service)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qca-qt5)
BuildRequires:  cmake(Qt5Core) >= 5.9.0
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Script)
BuildRequires:  cmake(Qt5ScriptTools)
BuildRequires:  cmake(Qt5UiPlugin)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
Recommends:     %{name}-lang
Obsoletes:      %{name}5 < %{version}
Provides:       %{name}5 = %{version}

%description
Okteta is a hex editor for the raw data of files.

%package data
Summary:        Hex Editor data files
Group:          Development/Tools/Other
# the files were in the main package before
Conflicts:      %{name} < 0.26
BuildArch:      noarch

%description data
Data files used by Okteta/libKasten, e.g. structures definitions.

%package part
Summary:        Hex Editor KParts plugin
Group:          Development/Tools/Other
Recommends:     %{name}-part-lang

%description part
Hex editing component for KParts

%package -n libKasten%{Kasten_sover}
Summary:        High-level hex editor/viewer framework libraries
Group:          Development/Tools/Other
Requires:       %{name}-data
Recommends:     libkasten-lang
Provides:       libkasten = %{version}

%description -n libKasten%{Kasten_sover}
Kasten is a WIP higher-level framework for composable document-centric
applications.

%package -n libOkteta%{Okteta_sover}
Summary:        Hex editor/viewer QWidgets libraries
Group:          Development/Tools/Other
Recommends:     libokteta-lang
Provides:       libokteta = %{version}

%description -n libOkteta%{Okteta_sover}
Okteta libraries for QWidget-based hex editing widgets.

%package devel
Summary:        Development files for the Okteta Hex Editor
Group:          Development/Tools/Other
Requires:       libKasten%{Kasten_sover} = %{version}
Requires:       libOkteta%{Okteta_sover} = %{version}
# designer plugin was in the main package before
Conflicts:      %{name} < 0.26
Obsoletes:      %{name}5-devel

%description devel
Contains the development files for the Okteta Hex Editor.

%lang_package
%lang_package -n %{name}-part
%lang_package -n libkasten
%lang_package -n libokteta

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang okteta
%find_lang oktetapart
%find_lang liboktetacore libokteta.lang
%find_lang liboktetagui libokteta.lang
%find_lang libkasten libkasten.lang
%find_lang liboktetakasten libkasten.lang
%{kf5_find_htmldocs}

%suse_update_desktop_file    org.kde.okteta         Utility Editor

%post -n libKasten%{Kasten_sover} -p /sbin/ldconfig
%postun -n libKasten%{Kasten_sover} -p /sbin/ldconfig
%post -n libOkteta%{Okteta_sover} -p /sbin/ldconfig
%postun -n libOkteta%{Okteta_sover} -p /sbin/ldconfig

%files
%license LICENSES/*
%doc %lang(en) %{_kf5_htmldir}/en/okteta/
%{_kf5_applicationsdir}/org.kde.okteta.desktop
%{_kf5_appstreamdir}/org.kde.okteta.appdata.xml
%{_kf5_bindir}/okteta
%{_kf5_iconsdir}/hicolor/*/*/*.*

%files data
%license LICENSES/*
%{_kf5_bindir}/struct2osd
%{_kf5_configkcfgdir}/
%{_kf5_knsrcfilesdir}/okteta-structures.knsrc
%{_kf5_sharedir}/mime/packages/okteta.xml
%{_kf5_sharedir}/okteta/

%files part
%license LICENSES/*
%{_kf5_plugindir}/kf5/
%{_kf5_servicesdir}/oktetapart.desktop

%files -n libKasten%{Kasten_sover}
%license LICENSES/*
%{_kf5_libdir}/libKasten%{Kasten_sover}*.so.*

%files -n libOkteta%{Okteta_sover}
%license LICENSES/*
%{_kf5_libdir}/libOkteta%{Okteta_sover}*.so.*

%files devel
%license LICENSES/*
%{_kf5_cmakedir}/
%{_kf5_libdir}/libKasten%{Kasten_sover}*.so
%{_kf5_libdir}/libOkteta%{Okteta_sover}*.so
%{_kf5_prefix}/include/*/
%{_kf5_mkspecsdir}/qt_OktetaCore.pri
%{_kf5_mkspecsdir}/qt_OktetaGui.pri
%{_kf5_libdir}/pkgconfig/OktetaCore.pc
%{_kf5_libdir}/pkgconfig/OktetaGui.pc
%{_kf5_plugindir}/designer/

%files lang -f %{name}.lang
%license LICENSES/*

%files part-lang -f oktetapart.lang
%license LICENSES/*

%files -n libkasten-lang -f libkasten.lang
%license LICENSES/*

%files -n libokteta-lang -f libokteta.lang
%license LICENSES/*

%changelog
