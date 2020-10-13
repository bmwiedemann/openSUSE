#
# spec file for package kdebugsettings
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


%define kf5_version 5.60.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           kdebugsettings
Version:        20.08.2
Release:        0
Summary:        Program to set debug verbosity for KDE applications
License:        LGPL-2.0-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:  extra-cmake-modules
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5ItemViews)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
Recommends:     %{name}-lang
Obsoletes:      kdebugsettings5 < %{version}
Provides:       kdebugsettings5 = %{version}
%if %{with lang}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif

%description
This program allows to tune the debug output of KDE applications, ranging
from verbose to completely silent.

%if %{with lang}
%lang_package
%endif

%prep
%setup -q -n kdebugsettings-%{version}

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build
%if %{with lang}
  %find_lang %{name} --with-man --all-name
%endif

%suse_update_desktop_file org.kde.kdebugsettings Utility DesktopUtility

%files
%license COPYING*
%{_kf5_appstreamdir}/org.kde.kdebugsettings.appdata.xml
%{_kf5_debugdir}/kde.renamecategories
%{_kf5_applicationsdir}/org.kde.kdebugsettings.desktop
%{_kf5_bindir}/kdebugsettings
%{_kf5_debugdir}/kdebugsettings.categories
%{_kf5_libdir}/libkdebugsettings.so.*
%{_kf5_libdir}/libkdebugsettings.so.5

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
