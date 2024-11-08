#
# spec file for package klettres
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


%define kf6_version 6.3.0
%define qt6_version 6.6.0

%bcond_without released
Name:           klettres
Version:        24.08.3
Release:        0
Summary:        Alphabet Learning Game
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/klettres
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6NewStuff) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Phonon4Qt6)
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
Obsoletes:      klettres5 < %{version}
Provides:       klettres5 = %{version}

%description
Helps to learn the alphabet and read some syllables.

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

%files
%license LICENSES/*
%doc AUTHORS ChangeLog
%doc %lang(en) %{_kf6_htmldir}/en/klettres/
%{_kf6_applicationsdir}/org.kde.klettres.desktop
%{_kf6_appstreamdir}/org.kde.klettres.appdata.xml
%{_kf6_bindir}/klettres
%{_kf6_configkcfgdir}/klettres.kcfg
%{_kf6_debugdir}/klettres.categories
%{_kf6_iconsdir}/hicolor/*/apps/klettres.*
%{_kf6_knsrcfilesdir}/klettres.knsrc
%{_kf6_sharedir}/klettres/

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/klettres/

%changelog
