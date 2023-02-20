#
# spec file for package kjournald
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

%define soname  0
%bcond_without released
Name:           kjournald
Version:        0.1.0
Release:        0
Summary:        Qt browser for journald database
License:        LGPL-2.1-or-later
URL:            https://invent.kde.org/system/kjournald
Source0:        https://download.kde.org/stable/kjournald/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/kjournald/%{name}-%{version}.tar.xz.sig
Source2:        kjournald.keyring
%endif
BuildRequires:  fdupes
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  pkgconfig(libsystemd)

Requires:       libqt5-qtquickcontrols2

%description
This project aims to provide an abstraction of the systemd’s journald API in
terms of QAbstractItemModel classes. The main purpose is to ease the
integration of journald into Qt based applications (both QML and QtWidget).
Additional to the library, the project provides a reference implementation of
the API, called kjournaldbrowser. Even though that application provides a
powerful journal database reader, we aim to do a clear split between 
reuseable library and application logic.

%lang_package

%prep
%autosetup -p1 

%build
%cmake_kf5 -d build

%cmake_build

%install
%kf5_makeinstall -C build

rm %{buildroot}%{_libdir}/lib%{name}.so

%suse_update_desktop_file -i org.kde.kjournaldbrowser Utility

%find_lang %{name} --all-name

%fdupes %{buildroot}

%ldconfig_scriptlets

%files
%license LICENSES/*
%{_bindir}/kjournaldbrowser
%{_libdir}/lib%{name}.so.*
%{_datadir}/applications/org.kde.kjournaldbrowser.desktop
%{_datadir}/metainfo/*.xml
%{_datadir}/qlogging-categories5/*

%files lang -f %{name}.lang

%changelog
