#
# spec file for package ktuberling
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
Name:           ktuberling
Version:        24.05.1
Release:        0
Summary:        Potato drawing editor
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/ktuberling
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KDEGames6) 
BuildRequires:  cmake(KF6Completion) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Qt6Multimedia) >= %{qt6_version}
BuildRequires:  cmake(Qt6PrintSupport) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6SvgWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Xml) >= %{qt6_version}
Provides:       ktuberling5 = %{version}
Obsoletes:      ktuberling5 < %{version}

%description
KTuberling is a nice potato editor for kids. The game intended for
small children. Of course, it may be suitable for adults who have
remained young at heart. Eyes, mouths, mustache, and other parts of
face and goodies can be attached onto a potato-like guy.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}%{_kf6_sharedir}/ktuberling

%find_lang %{name} --with-man --with-html --all-name

%files
%license LICENSES/*
%doc %lang(en) %{_kf6_htmldir}/en/ktuberling/
%{_kf6_applicationsdir}/org.kde.ktuberling.desktop
%{_kf6_appstreamdir}/org.kde.ktuberling.appdata.xml
%{_kf6_bindir}/ktuberling
%{_kf6_debugdir}/ktuberling.categories
%{_kf6_iconsdir}/hicolor/*/*/*tuberling.png
%{_kf6_sharedir}/ktuberling/

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/ktuberling/

%changelog
