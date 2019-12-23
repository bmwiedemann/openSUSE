#
# spec file for package AusweisApp2
#
# Copyright (c) 2019 SUSE LLC
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


Name:           AusweisApp2
Version:        1.18.2
Release:        0
Summary:        Official authentication app for German ID cards and residence titles
License:        EUPL-1.2
Group:          Productivity/Security
URL:            https://www.ausweisapp.bund.de
Source0:        https://github.com/Governikus/AusweisApp2/archive/%{version}.tar.gz
Source1:        AusweisApp2.png
Patch0:         0001-fix-resource-file-path.patch
Patch1:         0002-fix-translation-files-path.patch
Patch2:         0003-disable-auto-updater.patch
Patch3:         0004-set-config-path.patch
Patch4:         0005-disable-qtquick.patch
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  libQt5Concurrent-devel
BuildRequires:  libQt5Core-devel
BuildRequires:  libQt5Network-devel
BuildRequires:  libQt5Svg-devel
BuildRequires:  libQt5Xml-devel
BuildRequires:  libopenssl-1_1-devel
BuildRequires:  libqt5-linguist-devel
BuildRequires:  libqt5-qttools-devel
BuildRequires:  libqt5-qtwebsockets-devel
BuildRequires:  ninja
BuildRequires:  pcsc-lite-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(libudev)
Requires:       hicolor-icon-theme

%description
This app is developed and issued by the German government to be
used for online authentication with electronic German ID cards
and residence titles. To use this app, a supported RFID card
reader is required.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
export CFLAGS="%{optflags} -fPIC"
export CXXFLAGS="%{optflags} -fPIC"
%define __builder ninja
%cmake -DBUILD_SHARED_LIBS=OFF
ninja

%install
%cmake_install

%suse_update_desktop_file %{name} X-SuSE-DesktopUtility
install -DTm644 %{SOURCE1} %{buildroot}/%{_datadir}/icons/hicolor/64x64/apps/AusweisApp2.png

mkdir -p %{buildroot}/%{_libdir}/%{name}
mkdir -p %{buildroot}/%{_datadir}/%{name}/translations

mv %{buildroot}/%{_prefix}/translations/*.qm %{buildroot}/%{_datadir}/%{name}/translations/
mv %{buildroot}/%{_bindir}/*.rcc %{buildroot}/%{_datadir}/%{name}/
mv %{buildroot}/%{_bindir}/config.json %{buildroot}/%{_datadir}/%{name}/

%fdupes -s %{buildroot}/%{_prefix}

%files
%doc README.rst
%license LICENSE.txt LICENSE.officially.txt
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_libdir}/%{name}
%{_datadir}/applications/AusweisApp2.desktop
%{_datadir}/icons/hicolor
%exclude %{_bindir}/qtlogging.ini

%changelog
