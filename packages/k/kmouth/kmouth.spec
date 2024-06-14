#
# spec file for package kmouth
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
Name:           kmouth
Version:        24.05.1
Release:        0
Summary:        Speech Synthesizer Frontend
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/kmouth
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6Completion) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6PrintSupport) >= %{qt6_version}
BuildRequires:  cmake(Qt6TextToSpeech) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Xml) >= %{qt6_version}
Requires:       python3-speechd
Provides:       kde4-kmouth = 4.3.0
Obsoletes:      kde4-kmouth < 4.3.0

%description
The computer "speaks" the entered text for talking with people.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-html --with-man --all-name

%files
%license COPYING COPYING.DOC
%config %{_kf6_configdir}/kmouthrc
%doc %lang(en) %{_kf6_htmldir}/en/kmouth/
%doc %lang(en) %{_mandir}/man1/kmouth.1%{?ext_man}
%{_kf6_applicationsdir}/org.kde.kmouth.desktop
%{_kf6_appstreamdir}/org.kde.kmouth.appdata.xml
%{_kf6_bindir}/kmouth
%{_kf6_iconsdir}/hicolor/*/*/*.png
%{_kf6_sharedir}/kmouth/

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/kmouth/

%changelog
