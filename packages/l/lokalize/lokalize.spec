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


%bcond_without released
Name:           lokalize
Version:        24.05.2
Release:        0
Summary:        KDE Translation Editor
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/lokalize
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  hunspell-devel
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5Sonnet)
BuildRequires:  cmake(KF5TextWidgets)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
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
%cmake_kf5 -d build -- -DCMAKE_CXXFLAGS="%{optflags}" -DCMAKE_CFLAGS="%{optflags}"
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name
%{kf5_find_htmldocs}

%suse_update_desktop_file -r org.kde.lokalize Development Translation
%fdupes -s %{buildroot}%{_kf5_sharedir}/lokalize

%files
%license LICENSES/*
%doc %lang(en) %{_kf5_htmldir}/en/lokalize/
%{_kf5_applicationsdir}/org.kde.lokalize.desktop
%{_kf5_appstreamdir}/org.kde.lokalize.appdata.xml
%{_kf5_bindir}/lokalize
%{_kf5_configkcfgdir}/lokalize.kcfg
%{_kf5_debugdir}/lokalize.categories
%{_kf5_iconsdir}/hicolor/*/apps/lokalize.*
%{_kf5_notifydir}/lokalize.notifyrc
%{_kf5_sharedir}/lokalize/

%files lang -f %{name}.lang

%changelog
