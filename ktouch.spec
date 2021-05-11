#
# spec file for package ktouch
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


%define kf5_version 5.60.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           ktouch
Version:        21.04.0
Release:        0
Summary:        Touch Typing Tutor
License:        GPL-2.0-or-later
Group:          Amusements/Teaching/Other
URL:            https://apps.kde.org/ktouch
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  xz
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Declarative)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5IdleTime)
BuildRequires:  cmake(KF5ItemViews)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5NewStuff)
BuildRequires:  cmake(KF5TextEditor)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  cmake(Qt5QuickWidgets)
BuildRequires:  cmake(Qt5Script)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  cmake(Qt5XmlPatterns)
BuildRequires:  pkgconfig(xkbfile)
# Runtime deps
Requires:       kdeclarative-components
Requires:       kqtquickcharts
Requires:       libqt5-qtquickcontrols2
Provides:       kde4-ktouch = 4.3.0
Obsoletes:      kde4-ktouch < 4.3.0
Recommends:     %{name}-lang

%description
A KDE program that helps you to learn and practice touch typing.

%lang_package

%prep
%autosetup -p1

%build
%ifarch ppc ppc64
export RPM_OPT_FLAGS="%{optflags} -mminimal-toc"
%endif
  %cmake_kf5 -d build
  %cmake_build

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %find_lang %{name} --with-man --all-name
    %{kf5_find_htmldocs}
  %endif
  %suse_update_desktop_file org.kde.ktouch       X-KDE-Edu-Teaching

%files
%license COPYING*
%doc AUTHORS README.md
%doc %lang(en) %{_kf5_htmldir}/en/ktouch/
%{_kf5_applicationsdir}/org.kde.ktouch.desktop
%{_kf5_appsdir}/ktouch/
%{_kf5_appstreamdir}/org.kde.ktouch.appdata.xml
%{_kf5_bindir}/ktouch
%{_kf5_configkcfgdir}/ktouch.kcfg
%{_kf5_iconsdir}/hicolor/*/apps/ktouch.*
%{_kf5_mandir}/man1/ktouch.1.gz

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
