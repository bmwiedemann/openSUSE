#
# spec file for package kdiskmark
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2020, Dmitry Sidorov <jonmagon@gmail.com>
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


%define _singleapplication_version 3.3.4
Name:           kdiskmark
Version:        3.1.3
Release:        0
Summary:        A simple open-source disk benchmark tool for Linux distros
License:        GPL-3.0-only
URL:            https://github.com/JonMagon/KDiskMark
Source0:        %{url}/archive/%{version}.tar.gz#/KDiskMark-%{version}.tar.gz
# SingleApplication is licensed under MIT
Source1:        https://github.com/itay-grudev/SingleApplication/archive/v%{_singleapplication_version}.tar.gz#/SingleApplication-%{_singleapplication_version}.tar.gz
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  update-desktop-files
BuildRequires:  cmake(PolkitQt5-1)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Network)
Requires:       fio
Provides:       bundled(singleapplication) = %{_singleapplication_version}

%description
KDiskMark is an HDD and SSD benchmark tool with a very friendly graphical user interface.

%prep
%setup -q -n KDiskMark-%{version} -a1
mv SingleApplication-%{_singleapplication_version}/* src/singleapplication/

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%suse_update_desktop_file -i %{name} System Filesystem
%find_lang %{name} --with-qt

%files
%license LICENSE
%doc README.md
%{_kf5_applicationsdir}/%{name}.desktop
%{_kf5_bindir}/%{name}
%{_kf5_iconsdir}/hicolor
%{_kf5_iconsdir}/hicolor/*/*/*
%dir %{_kf5_sharedir}/%{name}
%{_kf5_sharedir}/%{name}/translations
# Helper files
%{_libexecdir}/kdiskmark_helper
%{_kf5_dbuspolicydir}/dev.jonmagon.kdiskmark.helperinterface.conf
%{_kf5_sharedir}/dbus-1/system-services/dev.jonmagon.kdiskmark.helperinterface.service
%{_kf5_sharedir}/polkit-1/actions/dev.jonmagon.kdiskmark.helper.policy

%changelog
