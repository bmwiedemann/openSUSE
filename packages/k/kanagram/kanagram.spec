#
# spec file for package kanagram
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
Name:           kanagram
Version:        24.05.2
Release:        0
Summary:        Anagram Game
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/kanagram
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6NewStuff) >= %{kf6_version}
BuildRequires:  cmake(KF6Sonnet) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(LibKEduVocDocument)
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6TextToSpeech) >= %{qt6_version}
Requires:       kdeedu-data
Obsoletes:      kanagram5 < %{version}
Provides:       kanagram5 = %{version}

%description
Kanagram is a letter order game.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

# Remove exotic icons resolution
rm -r %{buildroot}%{_kf6_iconsdir}/hicolor/80x80

%find_lang %{name} --with-html --all-name

%files
%license COPYING*
%doc %lang(en) %{_kf6_htmldir}/en/kanagram/
%{_kf6_applicationsdir}/org.kde.kanagram.desktop
%{_kf6_appstreamdir}/org.kde.kanagram.appdata.xml
%{_kf6_bindir}/kanagram
%{_kf6_configkcfgdir}/kanagram.kcfg
%{_kf6_iconsdir}/hicolor/*/apps/kanagram*.*
%{_kf6_knsrcfilesdir}/kanagram.knsrc
%{_kf6_sharedir}/kanagram/

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/kanagram/

%changelog
