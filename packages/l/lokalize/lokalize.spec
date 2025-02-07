#
# spec file for package lokalize
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


%define kf6_version 6.6.0
%define qt6_version 6.6.0

%bcond_without released
Name:           lokalize
Version:        24.12.2
Release:        0
Summary:        KDE Translation Editor
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/lokalize
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  fdupes
BuildRequires:  hunspell-devel
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6Sonnet) >= %{kf6_version}
BuildRequires:  cmake(KF6TextWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Sql) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
Obsoletes:      %{name}5 < %{version}
Provides:       %{name}5 = %{version}

%description
This package contains lokalize, an editor for translations

%lang_package

%prep
%autosetup -p1

%build
%ifarch ppc64
RPM_OPT_FLAGS="%{optflags} -mminimal-toc"
%endif
export CXXFLAGS="%{optflags} -fPIC"
export CFLAGS="%{optflags} -fPIC"
%cmake_kf6 -DCMAKE_CXXFLAGS="%{optflags}" -DCMAKE_CFLAGS="%{optflags}"

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-html --all-name

%fdupes %{buildroot}%{_kf6_sharedir}/lokalize

%files
%license LICENSES/*
%doc %lang(en) %{_kf6_htmldir}/en/lokalize/
%{_kf6_applicationsdir}/org.kde.lokalize.desktop
%{_kf6_appstreamdir}/org.kde.lokalize.appdata.xml
%{_kf6_bindir}/lokalize
%{_kf6_configkcfgdir}/lokalize.kcfg
%{_kf6_debugdir}/lokalize.categories
%{_kf6_iconsdir}/hicolor/*/apps/lokalize.*
%{_kf6_notificationsdir}/lokalize.notifyrc
%{_kf6_sharedir}/lokalize/

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/lokalize/

%changelog
