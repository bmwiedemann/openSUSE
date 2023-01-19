#
# spec file for package monero-gui
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


Name:           monero-gui
Version:        0.18.1.2
Release:        0
Summary:        The official GUI app for the Monero cryptocurrency
License:        BSD-3-Clause
URL:            https://github.com/monero-project/monero-gui
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  automake
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  hicolor-icon-theme
BuildRequires:  libQt5Core-devel
BuildRequires:  libQt5QuickControls2-devel
BuildRequires:  libboost_chrono-devel
BuildRequires:  libboost_date_time-devel
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_locale-devel
BuildRequires:  libboost_program_options-devel
BuildRequires:  libboost_regex-devel
BuildRequires:  libboost_serialization-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_thread-devel
BuildRequires:  libcurl-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libgcrypt20
BuildRequires:  libhidapi-devel
BuildRequires:  libminiupnpc-devel
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  libqt5-qtdeclarative-devel
BuildRequires:  libqt5-qtsvg-devel
BuildRequires:  libqt5-qttools-devel
BuildRequires:  libsodium-devel
BuildRequires:  libunwind-devel
BuildRequires:  libusb-devel
BuildRequires:  ninja
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  unbound-devel
BuildRequires:  update-desktop-files
BuildRequires:  zeromq-devel
Requires:       graphviz
Requires:       gtk3-tools
Requires:       monero-utils
Requires:       monerod

%description
The official Qt-based GUI wallet app for the privacy-focused Monero cryptocurrency

%prep
%autosetup

%build
%define __builder ninja
export CXXFLAGS="%{optflags} -Wno-sign-compare"
%cmake \
  -DARCH=default \
  -DBUILD_SHARED_LIBS=OFF \
  -DCMAKE_EXE_LINKER_FLAGS="%{?build_ldflags}" \
  -DCMAKE_MODULE_LINKER_FLAGS="%{?build_ldflags}" \
  -DCMAKE_SHARED_LINKER_FLAGS="%{?build_ldflags}" \
  -Wno-dev
%cmake_build

%install
install -D -m 0755 build/bin/monero-wallet-gui %{buildroot}%{_bindir}/monero-wallet-gui
install -D -m 644 images/appicons/16x16.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/monero-gui.png
install -D -m 644 images/appicons/24x24.png %{buildroot}%{_datadir}/icons/hicolor/24x24/apps/monero-gui.png
install -D -m 644 images/appicons/32x32.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/monero-gui.png
install -D -m 644 images/appicons/48x48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/monero-gui.png
install -D -m 644 images/appicons/64x64.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/monero-gui.png
install -D -m 644 images/appicons/96x96.png %{buildroot}%{_datadir}/icons/hicolor/96x96/apps/monero-gui.png
install -D -m 644 images/appicons/128x128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/monero-gui.png
install -D -m 644 images/appicons/256x256.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/monero-gui.png
%suse_update_desktop_file -c %{name} "Monero Wallet" "GUI wallet for the Monero cryptocurrency" monero-wallet-gui monero-gui Finance\;Network\;Qt\;

%files
%license LICENSE
%{_bindir}/monero-wallet-gui
%{_datadir}/icons/hicolor/16x16/apps/monero-gui.png
%{_datadir}/icons/hicolor/24x24/apps/monero-gui.png
%{_datadir}/icons/hicolor/32x32/apps/monero-gui.png
%{_datadir}/icons/hicolor/48x48/apps/monero-gui.png
%{_datadir}/icons/hicolor/64x64/apps/monero-gui.png
%{_datadir}/icons/hicolor/96x96/apps/monero-gui.png
%{_datadir}/icons/hicolor/128x128/apps/monero-gui.png
%{_datadir}/icons/hicolor/256x256/apps/monero-gui.png
%{_datadir}/applications/monero-gui.desktop

%changelog
