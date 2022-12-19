#
# spec file for package AusweisApp2
#
# Copyright (c) 2022 SUSE LLC
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
Version:        1.26.1
Release:        0
Summary:        Official authentication app for German ID cards and residence permits
License:        EUPL-1.2
Group:          Productivity/Security
URL:            https://www.ausweisapp.bund.de
Source0:        https://github.com/Governikus/AusweisApp2/archive/%{version}.tar.gz
BuildRequires:  cmake
%if 0%{?suse_version} > 1500
BuildRequires:  gcc-c++
%else
BuildRequires:  gcc11-c++
%endif
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  libopenssl-1_1-devel
BuildRequires:  ninja
BuildRequires:  pcsc-lite-devel
BuildRequires:  pkgconfig
BuildRequires:  qt6-concurrent-devel
BuildRequires:  qt6-core-devel
BuildRequires:  qt6-linguist-devel
BuildRequires:  qt6-network-devel
BuildRequires:  qt6-qml-devel
BuildRequires:  qt6-qmlworkerscript-devel
BuildRequires:  qt6-quick-devel
BuildRequires:  qt6-quickcontrols2-devel
BuildRequires:  qt6-shadertools-devel
BuildRequires:  qt6-statemachine-devel
BuildRequires:  qt6-svg-devel
BuildRequires:  qt6-websockets-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(libudev)
Requires:       hicolor-icon-theme

%description
This app is developed and issued by the German government to be
used for online authentication with electronic German ID cards
and residence permits. To use this app, a supported RFID card
reader or compatible NFC smart phone is required.

%prep
%setup -q

%build
%if 0%{?suse_version} <= 1500
export CC=gcc-11
export CXX=g++-11
%endif
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
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
