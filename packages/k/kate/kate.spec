#
# spec file for package kate
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


%define _appstreamkpackage 0%(cat %{_kf5_cmakedir}/KF5Package/KF5PackageMacros.cmake | grep -q 'appstream-metainfo' && echo 1)
%define kf5_version 5.60.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           kate
Version:        21.04.0
Release:        0
Summary:        Advanced Text Editor
License:        GPL-3.0-or-later
Group:          Productivity/Text/Editors
URL:            https://kate-editor.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
# PATCH-FIX-OPENSUSE
Patch0:         0001-Defuse-root-block.patch
BuildRequires:  libgit2-devel
BuildRequires:  cmake(KF5Activities)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5ItemModels)
BuildRequires:  cmake(KF5JobWidgets)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5NewStuff)
BuildRequires:  cmake(KF5Parts)
BuildRequires:  cmake(KF5Plasma)
BuildRequires:  cmake(KF5Service)
BuildRequires:  cmake(KF5SyntaxHighlighting)
BuildRequires:  cmake(KF5TextEditor)
BuildRequires:  cmake(KF5ThreadWeaver)
BuildRequires:  cmake(KF5Wallet)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(KUserFeedback)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Script)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
Requires:       %{name}-plugins = %{version}
Recommends:     %{name}-lang
Obsoletes:      %{name}5 < %{version}
Provides:       %{name}5 = %{version}

%description
Kate is an advanced text editor by KDE.

%package -n kwrite
Summary:        KDE Text Editor
Group:          Productivity/Text/Editors
Requires:       %{name}-plugins = %{version}
Obsoletes:      kwrite5 < %{version}

%description -n kwrite
KWrite is a text editor by KDE.

%package plugins
Summary:        KDE Text Editor plugins
Group:          Productivity/Text/Editors
Obsoletes:      kate5-plugins < %{version}
Provides:       ktexteditorpreviewplugin = %{version}
Obsoletes:      ktexteditorpreviewplugin < %{version}

%description plugins
Kate is an advanced text editor by KDE. This package contains
plugins and data files for Kate and KWrite editors.

%lang_package

%prep
%autosetup -p1

%build
  %cmake_kf5 -d build
  %cmake_build

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %find_lang %{name} --with-man --all-name
    %{kf5_find_htmldocs}
  %endif

%files
%license LICENSES/*
%doc README*
%dir %{_kf5_iconsdir}/hicolor/150x150/
%dir %{_kf5_iconsdir}/hicolor/150x150/apps
%dir %{_kf5_iconsdir}/hicolor/310x310/
%dir %{_kf5_iconsdir}/hicolor/310x310/apps
%dir %{_kf5_iconsdir}/hicolor/44x44/
%dir %{_kf5_iconsdir}/hicolor/44x44/apps
%dir %{_kf5_iconsdir}/hicolor/256x256/
%dir %{_kf5_iconsdir}/hicolor/256x256/apps
%dir %{_kf5_iconsdir}/hicolor/512x512/
%dir %{_kf5_iconsdir}/hicolor/512x512/apps
%doc %lang(en) %{_kf5_htmldir}/en/kate/
%doc %lang(en) %{_kf5_htmldir}/en/katepart/
%doc %{_kf5_mandir}/man1/kate.*
%{_kf5_applicationsdir}/org.kde.kate.desktop
%{_kf5_appstreamdir}/org.kde.kate.appdata.xml
%{_kf5_bindir}/kate
%{_kf5_iconsdir}/hicolor/*/apps/kate.*

%files -n kwrite
%license LICENSES/*
%doc README*
%doc %lang(en) %{_kf5_htmldir}/en/kwrite/
%{_kf5_applicationsdir}/org.kde.kwrite.desktop
%{_kf5_appstreamdir}/org.kde.kwrite.appdata.xml
%{_kf5_bindir}/kwrite
%{_kf5_iconsdir}/hicolor/*/apps/kwrite.*

%files plugins
%license LICENSES/*
%doc README*
%if 0%{?_appstreamkpackage}
%{_kf5_appstreamdir}/org.kde.plasma.katesessions.appdata.xml
%endif
%{_kf5_plugindir}/
%{_kf5_servicesdir}/
%{_kf5_sharedir}/kateproject/
%{_kf5_sharedir}/katexmltools/
%{_kf5_sharedir}/plasma/

%if %{with lang}
%files lang -f %{name}.lang
%license LICENSES/*
%endif

%changelog
