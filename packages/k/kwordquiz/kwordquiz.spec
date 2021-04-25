#
# spec file for package kwordquiz
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
Name:           kwordquiz
Version:        21.04.0
Release:        0
Summary:        Vocabulary Trainer
License:        GPL-2.0-or-later
Group:          Amusements/Teaching/Language
URL:            https://apps.kde.org/kwordquiz
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5ItemViews)
BuildRequires:  cmake(KF5NewStuff)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5NotifyConfig)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(LibKEduVocDocument)
BuildRequires:  cmake(Phonon4Qt5)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Widgets)
Recommends:     %{name}-lang
Obsoletes:      %{name}5 < %{version}
Provides:       %{name}5 = %{version}

%description
A flashcard and vocabulary learning program.

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
  %fdupes -s %{buildroot}

%files
%license COPYING*
%doc AUTHORS README
%doc %lang(en) %{_kf5_htmldir}/en/kwordquiz/
%{_kf5_applicationsdir}/org.kde.kwordquiz.desktop
%{_kf5_appsdir}/kwordquiz/
%{_kf5_appstreamdir}/org.kde.kwordquiz.appdata.xml
%{_kf5_bindir}/kwordquiz
%{_kf5_configkcfgdir}/
%{_kf5_iconsdir}/hicolor/*/apps/kwordquiz.*
%{_kf5_iconsdir}/hicolor/*/mimetypes/application-x-kwordquiz.png
%{_kf5_knsrcfilesdir}/kwordquiz.knsrc
%{_kf5_kxmlguidir}/kwordquiz/
%{_kf5_sharedir}/knotifications5/

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
