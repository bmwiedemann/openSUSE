#
# spec file for package keditbookmarks
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
Name:           keditbookmarks
Version:        24.05.1
Release:        0
Summary:        KDE Bookmark Editor
License:        GPL-2.0-only
URL:            https://www.kde.org/
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6Bookmarks) >= %{kf6_version}
BuildRequires:  cmake(KF6Codecs) >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Parts) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  pkgconfig(x11)

%description
This is an editor to edit your KDE-wide bookmark set.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-html --with-man --all-name

%ldconfig_scriptlets

%files
%license COPYING*
%doc %lang(en) %{_kf6_htmldir}/en/keditbookmarks/
%doc %lang(en) %{_kf6_mandir}/man1/kbookmarkmerger.1%{ext_man}
%{_kf6_applicationsdir}/org.kde.keditbookmarks.desktop
%{_kf6_bindir}/kbookmarkmerger
%{_kf6_bindir}/keditbookmarks
%{_kf6_configkcfgdir}/keditbookmarks.kcfg
%{_kf6_debugdir}/keditbookmarks.categories
%{_kf6_libdir}/libkbookmarkmodel_private.so.*


%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/keditbookmarks/

%changelog
