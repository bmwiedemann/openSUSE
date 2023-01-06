#
# spec file for package kde-cli-tools5
#
# Copyright (c) 2023 SUSE LLC
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


%define kf5_version 5.98.0
%bcond_without released
Name:           kde-cli-tools5
Version:        5.26.5
Release:        0
Summary:        Additional CLI tools for KDE applications
License:        GPL-2.0-or-later
Group:          System/GUI/KDE
URL:            http://www.kde.org
Source:         https://download.kde.org/stable/plasma/%{version}/kde-cli-tools-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/kde-cli-tools-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
# PATCH-FIX-OPENSUSE kdesu-add-some-i18n-love.patch -- boo#852256
Patch0:         kdesu-add-some-i18n-love.patch
BuildRequires:  extra-cmake-modules >= %{kf5_version}
BuildRequires:  kf5-filesystem
BuildRequires:  xz
BuildRequires:  cmake(KF5Activities) >= %{kf5_version}
BuildRequires:  cmake(KF5Config) >= %{kf5_version}
BuildRequires:  cmake(KF5Declarative) >= %{kf5_version}
BuildRequires:  cmake(KF5DocTools) >= %{kf5_version}
BuildRequires:  cmake(KF5I18n) >= %{kf5_version}
BuildRequires:  cmake(KF5IconThemes) >= %{kf5_version}
BuildRequires:  cmake(KF5Init) >= %{kf5_version}
BuildRequires:  cmake(KF5KCMUtils) >= %{kf5_version}
BuildRequires:  cmake(KF5KDELibs4Support) >= %{kf5_version}
BuildRequires:  cmake(KF5KIO) >= %{kf5_version}
BuildRequires:  cmake(KF5Su) >= %{kf5_version}
BuildRequires:  cmake(KF5WindowSystem) >= %{kf5_version}
# Needs KWorkSpace::detectPlatform
BuildRequires:  cmake(LibKWorkspace) >= 5.12.4
BuildRequires:  cmake(Qt5DBus) >= 5.15.0
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
# Unversioned kde-open, kdesu, etc.
Conflicts:      kdebase4-runtime
# for kquitapp5
Requires:       kdbusaddons-tools

%description
Additional CLI tools for KDE applications and workspaces.

%lang_package

%prep
%autosetup -p1 -n kde-cli-tools-%{version}

%build
  %cmake_kf5 -d build
  %cmake_build

%install
  %kf5_makeinstall -C build
%if %{with released}
  %find_lang %{name} --with-man --all-name
  %kf5_find_htmldocs
%endif
  ln -s %{_kf5_libexecdir}/kdesu %{buildroot}%{_kf5_bindir}/kdesu

%pre
# Remove old update-alternatives entry
if [ -x "%{_sbindir}/update-alternatives" ]; then
    %{_sbindir}/update-alternatives --remove kdesu %{_kf5_libexecdir}/kdesu
fi

%files
%license LICENSES/*
%{_kf5_applicationsdir}/kcm_filetypes.desktop
%{_kf5_bindir}/kdesu
%{_kf5_bindir}/kcmshell5
%{_kf5_bindir}/kdecp{5,}
%{_kf5_bindir}/kde-inhibit
%{_kf5_bindir}/kdemv{5,}
%{_kf5_bindir}/kde-open{5,}
%{_kf5_bindir}/keditfiletype{5,}
%{_kf5_bindir}/kioclient{5,}
%{_kf5_bindir}/kmimetypefinder{5,}
%{_kf5_bindir}/ksvgtopng{5,}
%{_kf5_bindir}/kstart{5,}
%{_kf5_bindir}/ktraderclient5
%{_kf5_bindir}/kbroadcastnotification
%{_kf5_bindir}/plasma-open-settings
%{_kf5_libexecdir}/kdeeject
%{_kf5_libexecdir}/kdesu
%{_kf5_applicationsdir}/org.kde.keditfiletype.desktop
%{_kf5_applicationsdir}/org.kde.plasma.settings.open.desktop
%dir %{_kf5_plugindir}/
%dir %{_kf5_plugindir}/plasma/
%dir %{_kf5_plugindir}/plasma/kcms/
%dir %{_kf5_plugindir}/plasma/kcms/systemsettings_qwidgets/
%{_kf5_plugindir}/plasma/kcms/systemsettings_qwidgets/kcm_filetypes.so
%doc %{_kf5_htmldir}/en
%{_kf5_mandir}/man1/kdesu*

%if %{with released}
%files lang -f %{name}.lang
%endif

%changelog
