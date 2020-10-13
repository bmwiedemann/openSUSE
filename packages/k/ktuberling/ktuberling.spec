#
# spec file for package ktuberling
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
Name:           ktuberling
Version:        20.08.2
Release:        0
Summary:        Potato drawing editor
License:        GPL-2.0-or-later
Group:          Amusements/Toys/Other
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:  extra-cmake-modules
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Completion)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KDEGames)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Multimedia)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
Recommends:     %{name}-lang
Provides:       ktuberling5 = %{version}
Obsoletes:      ktuberling5 < %{version}
%if %{with lang}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif

%description
KTuberling is a nice potato editor for kids. The game intended for
small children. Of course, it may be suitable for adults who have
remained young at heart. Eyes, mouths, mustache, and other parts of
face and goodies can be attached onto a potato-like guy.

%lang_package

%prep
%setup -q

%build
  %cmake_kf5 -d build
  %cmake_build

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %find_lang %{name} --with-man --all-name
    %{kf5_find_htmldocs}
  %endif
  %suse_update_desktop_file -r org.kde.ktuberling          Game KidsGame

%files
%license COPYING*
%doc %lang(en) %{_kf5_htmldir}/en/ktuberling/
%{_kf5_applicationsdir}/org.kde.ktuberling.desktop
%{_kf5_appsdir}/ktuberling/
%{_kf5_bindir}/ktuberling
%{_kf5_debugdir}/ktuberling.categories
%{_kf5_iconsdir}/hicolor/*/*/*
%{_kf5_kxmlguidir}/ktuberling/
%{_kf5_appstreamdir}/org.kde.ktuberling.appdata.xml

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
