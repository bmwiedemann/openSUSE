#
# spec file for package kwordquiz
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


%define kf6_version 6.0.0
%define qt6_version 6.6.0

%bcond_without released
Name:           kwordquiz
Version:        24.05.2
Release:        0
Summary:        Vocabulary Trainer
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/kwordquiz
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  fdupes
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6Kirigami) >= %{kf6_version}
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(KF6NewStuff) >= %{kf6_version}
BuildRequires:  cmake(LibKEduVocDocument)
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Multimedia) >= %{qt6_version}
BuildRequires:  cmake(Qt6PrintSupport) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickControls2) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Xml) >= %{qt6_version}
Requires:       kf6-kirigami-imports >= %{kf6_version}
Requires:       kirigami-addons6
Obsoletes:      kwordquiz5 < %{version}
Provides:       kwordquiz5 = %{version}

%description
A flashcard and vocabulary learning program.

%lang_package

%prep
%autosetup -p1

%build
%ifarch ppc ppc64
export RPM_OPT_FLAGS="%{optflags} -mminimal-toc"
%endif
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-html --all-name

%fdupes %{buildroot}

%files
%license LICENSES/*
%doc AUTHORS README
%doc %lang(en) %{_kf6_htmldir}/en/kwordquiz/
%{_kf6_applicationsdir}/org.kde.kwordquiz.desktop
%{_kf6_appstreamdir}/org.kde.kwordquiz.appdata.xml
%{_kf6_bindir}/kwordquiz
%{_kf6_configkcfgdir}/kwordquiz.kcfg
%{_kf6_iconsdir}/hicolor/*/apps/kwordquiz.*
%{_kf6_iconsdir}/hicolor/*/apps/org.kde.kwordquiz.*
%{_kf6_iconsdir}/hicolor/*/mimetypes/application-x-kwordquiz.png
%{_kf6_knsrcfilesdir}/kwordquiz.knsrc
%{_kf6_sharedir}/kwordquiz/

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/kwordquiz/

%changelog
