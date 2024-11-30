#
# spec file for package gqrx
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


Name:           gqrx
Version:        2.17.6
Release:        0
Summary:        Software defined radio receiver
License:        GPL-3.0-only
Group:          Productivity/Hamradio/Other
URL:            https://gqrx.dk/
#Git-Clone:     https://github.com/csete/gqrx.git
Source0:        https://github.com/csete/gqrx/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  alsa-devel
BuildRequires:  cmake
BuildRequires:  fftw3-devel
BuildRequires:  gnuradio-devel
BuildRequires:  gr-osmosdr-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  libboost_atomic-devel
BuildRequires:  libboost_date_time-devel
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_program_options-devel
BuildRequires:  libboost_regex-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_test-devel
BuildRequires:  libboost_thread-devel
BuildRequires:  libjack-devel
BuildRequires:  libsndfile-devel
BuildRequires:  orc
BuildRequires:  pkgconfig
BuildRequires:  portaudio-devel
BuildRequires:  python3-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(libpulse)
Recommends:     airspy

%description
Gqrx is an experimental software defined radio receiver implemented using
GNU Radio and the Qt GUI toolkit. Currently it works on Linux and Mac and it
can use the Funcube Dongle, RTL2832U-based DVB-T dongles, OsmoSDR devices and
USRP devices as input source.

%prep
%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license COPYING
%doc LICENSE-CTK README.md
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/scalable/apps/gqrx.svg
%{_datadir}/applications/dk.gqrx.gqrx.desktop
%{_datadir}/metainfo/dk.gqrx.gqrx.appdata.xml

%changelog
