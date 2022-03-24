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


Name:           kdiskmark
Version:        2.3.0
Release:        0
Summary:        A simple open-source disk benchmark tool for Linux distros
License:        GPL-3.0-only
URL:            https://github.com/JonMagon/KDiskMark
Source:         %{url}/archive/%{version}.tar.gz#/KDiskMark-%{version}.tar.gz
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Auth)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Widgets)
Requires:       fio

%description
KDiskMark is an HDD and SSD benchmark tool with a very friendly graphical user interface.

%prep
%setup -q -n KDiskMark-%{version}

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
%{_kf5_dbuspolicydir}/org.jonmagon.kdiskmark.conf
%{_kf5_iconsdir}/hicolor
%{_kf5_iconsdir}/hicolor/*/*/*
%if %{pkg_vcmp kf5-filesystem >= 20220307}
%{_libexecdir}/kauth/kdiskmark_helper
%else
%dir %{_kf5_libdir}/libexec/kauth
%{_kf5_libdir}/libexec/kauth/kdiskmark_helper
%endif
%dir %{_kf5_sharedir}/%{name}
%{_kf5_sharedir}/%{name}/translations
%{_kf5_sharedir}/dbus-1/system-services/org.jonmagon.kdiskmark.service
%{_kf5_sharedir}/polkit-1/actions/org.jonmagon.kdiskmark.policy


%changelog
