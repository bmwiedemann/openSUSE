#
# spec file for package kde-cli-tools6
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


%global kf6_version 6.2.0
%define qt6_version 6.6.0

%bcond_without released
%define rname kde-cli-tools
Name:           kde-cli-tools6
Version:        6.1.2
Release:        0
Summary:        Additional CLI tools for KDE applications
License:        GPL-2.0-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  qt6-gui-private-devel >= %{qt6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Parts) >= %{kf6_version}
BuildRequires:  cmake(KF6Service) >= %{kf6_version}
BuildRequires:  cmake(KF6Su) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
# for kquitapp6
Requires:       kf6-kdbusaddons-tools
Provides:       kde-cli-tools5 = %{version}
Obsoletes:      kde-cli-tools5 < %{version}
Obsoletes:      kde-cli-tools5-lang < %{version}

%description
Additional CLI tools for KDE applications and workspaces.

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install
# For xdg-su
ln -s %{_kf6_libexecdir}/kdesu %{buildroot}%{_kf6_bindir}/kdesu

%find_lang %{name} --with-man --with-html --all-name

%files
%license LICENSES/*
%doc %lang(en) %{_kf6_htmldir}/en/*
%{_kf6_applicationsdir}/kcm_filetypes.desktop
%{_kf6_applicationsdir}/org.kde.keditfiletype.desktop
%{_kf6_applicationsdir}/org.kde.plasma.settings.open.desktop
%{_kf6_bindir}/kbroadcastnotification
%{_kf6_bindir}/kde-inhibit
%{_kf6_bindir}/kde-open{5,}
%{_kf6_bindir}/kdecp{5,}
%{_kf6_bindir}/kdemv{5,}
%{_kf6_bindir}/kdesu
%{_kf6_bindir}/keditfiletype{5,}
%{_kf6_bindir}/kinfo
%{_kf6_bindir}/kioclient{5,}
%{_kf6_bindir}/kmimetypefinder{5,}
%{_kf6_bindir}/kstart{5,}
%{_kf6_bindir}/ksvgtopng{5,}
%{_kf6_bindir}/plasma-open-settings
%{_kf6_libexecdir}/kdeeject
%{_kf6_libexecdir}/kdesu
%{_kf6_mandir}/man1/kdesu*
%{_kf6_plugindir}/plasma/kcms/systemsettings_qwidgets/kcm_filetypes.so
%dir %{_kf6_sharedir}/zsh
%dir %{_kf6_sharedir}/zsh/site-functions
%{_kf6_sharedir}/zsh/site-functions/_kde-inhibit

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en

%changelog
