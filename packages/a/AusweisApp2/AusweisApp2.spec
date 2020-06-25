#
# spec file for package AusweisApp2
#
# Copyright (c) 2020 SUSE LLC
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
Version:        1.20.1
Release:        0
Summary:        Official authentication app for German ID cards and residence permits
License:        EUPL-1.2
Group:          Productivity/Security
URL:            https://www.ausweisapp.bund.de
Source0:        https://github.com/Governikus/AusweisApp2/archive/%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  libQt5Concurrent-devel
BuildRequires:  libQt5Core-devel
BuildRequires:  libQt5Network-devel
BuildRequires:  libQt5QuickControls2-devel
BuildRequires:  libQt5Svg-devel
BuildRequires:  libQt5Xml-devel
BuildRequires:  libopenssl-1_1-devel
BuildRequires:  libqt5-linguist-devel
BuildRequires:  libqt5-qtdeclarative-devel
BuildRequires:  libqt5-qttools-devel
BuildRequires:  libqt5-qtwebsockets-devel
BuildRequires:  ninja
BuildRequires:  pcsc-lite-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(libudev)
Requires:       hicolor-icon-theme
Requires:       libqt5-qtgraphicaleffects
Requires:       libqt5-qtquickcontrols2

%description
This app is developed and issued by the German government to be
used for online authentication with electronic German ID cards
and residence permits. To use this app, a supported RFID card
reader or compatible NFC smart phone is required.

%prep
%setup -q

%build
export CFLAGS="%{optflags} -fPIC"
export CXXFLAGS="%{optflags} -fPIC"
%define __builder ninja
%cmake -DBUILD_SHARED_LIBS=OFF
ninja

%install
%cmake_install

%suse_update_desktop_file com.governikus.ausweisapp2 X-SuSE-DesktopUtility
install -DTm644 %{_builddir}/%{name}-%{version}/resources/images/npa.png %{buildroot}/%{_datadir}/icons/hicolor/96x96/apps/AusweisApp2.png

%fdupes -s %{buildroot}/%{_prefix}

%files
%doc README.rst
%license LICENSE.txt LICENSE.officially.txt
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/metainfo
%{_datadir}/applications/com.governikus.ausweisapp2.desktop
%{_datadir}/icons/hicolor

%changelog
