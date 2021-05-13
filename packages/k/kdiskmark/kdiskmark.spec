#
# spec file for package kdiskmark
#
# Copyright (c) 2021 SUSE LLC
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
Version:        2.2.0
Release:        0
Summary:        A simple open-source disk benchmark tool for Linux distros
License:        GPL-3.0-only
URL:            https://github.com/JonMagon/KDiskMark
Source:         %{url}/archive/%{version}.tar.gz#/KDiskMark-%{version}.tar.gz
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libqt5-linguist-devel
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  update-desktop-files
BuildRequires:  kauth-devel
Requires:       fio

%description
KDiskMark is an HDD and SSD benchmark tool with a very friendly graphical user interface.

%prep
%setup -n KDiskMark-%{version} -q

%build
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_CXX_FLAGS="-Wno-error" \
    -DCMAKE_CXXFLAGS="-Wno-error"
%cmake_build

%install
%cmake_install
%suse_update_desktop_file -i %{name} System Filesystem
%find_lang %{name} --with-qt

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_kf5_libdir}/libexec/
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/translations
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor
%{_datadir}/icons/hicolor/*/*/*
%{_kf5_sharedir}/dbus-1/system-services/org.jonmagon.kdiskmark.service
%{_kf5_dbuspolicydir}//org.jonmagon.kdiskmark.conf
%{_kf5_sharedir}/polkit-1/actions/org.jonmagon.kdiskmark.policy

%changelog
