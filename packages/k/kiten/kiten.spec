#
# spec file for package kiten
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
Name:           kiten
Version:        24.05.2
Release:        0
Summary:        Japanese Reference/Study Tool
# Data files are under CC-BY-SA-3.0 (edict) and CC-BY-SA-4.0 ("kanjidic"/SKIP numbers therein)
License:        GPL-2.0-or-later AND CC-BY-SA-3.0 AND CC-BY-SA-4.0
URL:            https://apps.kde.org/kiten
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF6Archive) >= %{kf6_version}
BuildRequires:  cmake(KF6Completion) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(KF6StatusNotifierItem) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
%if 0%{?suse_version} >= 1599
BuildRequires:  edict-eucjp >= 20230511
Requires:       edict-eucjp >= 20230511
%endif
Requires:       fonts-KanjiStrokeOrders
Provides:       kiten5 = %{version}
Obsoletes:      kiten5 < %{version}

%description
Kiten is a tool to learn Japanese.

%package devel
Summary:        Development files for kiten
License:        GPL-2.0-or-later
Requires:       kiten = %{version}

%description devel
Kiten is a tool to learn Japanese.

This package contains files for developing applications using kiten.

%package -n fonts-KanjiStrokeOrders
Summary:        Font for learning Japanese Kanji
License:        BSD-3-Clause
BuildRequires:  fontpackages-devel
BuildArch:      noarch
%reconfigure_fonts_prereq

%description -n fonts-KanjiStrokeOrders
This font provides an easy way to view stroke order diagrams for over 6350
kanji, 183 kana symbols, the Latin characters and quite a few other symbols.
I have also used it as a dumping ground for my own character creation doodles.

My hope is that this font will assist people who are learning kanji. I
also hope it will help teachers of Japanese in the preparation of
classroom material. Beware that Japanese stroke order can differ from the
stroke order used in other languages that use Chinese characters.

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
%if 0%{?suse_version} >= 1599
for i in edict kanjidic radkfile; do
	ln -fsv "%{_datadir}/edict/$i.eucjp" "%{buildroot}%{_datadir}/kiten/$i"
done
%endif

%find_lang %{name} --with-html --all-name

%reconfigure_fonts_scriptlets -n fonts-KanjiStrokeOrders

%ldconfig_scriptlets

%files
%license LICENSES/*
%doc AUTHORS README.md
%doc %lang(en) %{_kf6_htmldir}/en/kiten/
%{_kf6_applicationsdir}/org.kde.kiten.desktop
%{_kf6_applicationsdir}/org.kde.kitenkanjibrowser.desktop
%{_kf6_applicationsdir}/org.kde.kitenradselect.desktop
%{_kf6_appstreamdir}/org.kde.kiten.appdata.xml
%{_kf6_bindir}/kiten
%{_kf6_bindir}/kitenkanjibrowser
%{_kf6_bindir}/kitenradselect
%{_kf6_configkcfgdir}/kiten.kcfg
%{_kf6_iconsdir}/hicolor/*/*/kiten.*
%{_kf6_libdir}/libkiten.so.*
%{_kf6_sharedir}/kiten/

%files devel
%{_kf6_libdir}/libkiten.so
%{_includedir}/libkiten/

%files -n fonts-KanjiStrokeOrders
%license data/font/KanjiStrokeOrders.ttf.license
%doc data/font/readme_en_v2.016.txt
%dir %{_kf6_sharedir}/fonts/kanjistrokeorders/
%{_kf6_sharedir}/fonts/kanjistrokeorders/KanjiStrokeOrders.ttf

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/kiten/

%changelog
