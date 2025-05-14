#
# spec file for package welle-io
#
# Copyright (c) 2025 SUSE LLC
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


%if 0%{?gcc_version} < 8
%define with_gcc 13
%endif
Name:           welle-io
Version:        2.7
Release:        0
Summary:        Receiver for DAB and DAB+ broadcast radio
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Other
URL:            https://www.welle.io/
Source0:        %{name}-%{version}.tar.xz
Patch0:         %{name}-fdk-aac.patch
Patch1:         %{name}-qt6.4.1.patch
BuildRequires:  cmake
BuildRequires:  gcc%{?with_gcc}-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  qt6-charts-devel
BuildRequires:  qt6-multimedia-devel
BuildRequires:  qt6-quickcontrols2-devel
BuildRequires:  xdg-utils
BuildRequires:  xxd
BuildRequires:  pkgconfig(SoapySDR)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(fdk-aac)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(libairspy)
BuildRequires:  pkgconfig(libmp3lame)
BuildRequires:  pkgconfig(libmpg123)
BuildRequires:  pkgconfig(librtlsdr)
Requires:       qt6-charts-imports
Requires:       qt6-multimedia-imports
Requires:       qt6-qt5compat-imports

%description
Receive digital audio broadcasts with your computer: welle.io is an open source
DAB and DAB+ software defined radio (SDR) with direct support for RTL-SDR and
other SDR hardware through SoapySDR. It supports high DPI and touch displays and
it runs even on cheap computers.

%package -n welle-cli
Summary:        Receiver for DAB and DAB+ broadcast radio: command line tool
Group:          Productivity/Multimedia/Other

%description -n welle-cli
Receive digital audio broadcasts with your computer: welle.io is an open source
DAB and DAB+ software defined radio (SDR) with direct support for RTL-SDR and
other SDR hardware through SoapySDR.

This package contains the welle-cli command line tool that does not need GUI

%prep
%setup -q
%patch -P 0 -p1
%patch -P 1 -p1

%build
%if 0%{?with_gcc}
export CXX=g++-%{with_gcc}
export CC=gcc-%{with_gcc}
%endif
%cmake -DSOAPYSDR=1 -DRTLSDR=1 -DAIRSPY=1 -DFLAC=1 -DFDK_AAC=1 -DGIT_DESCRIBE=%{version}
%cmake_build

%check
%if 0%{?with_gcc}
export CXX=g++-%{with_gcc}
export CC=gcc-%{with_gcc}
%endif
%ctest

%install
%cmake_install
install -dm 0755 %{buildroot}%{_datadir}/appdata

%files
%license COPYING
%{_bindir}/welle-io
%{_datadir}/metainfo
%{_datadir}/applications/io.welle.welle-gui.desktop
%{_datadir}/icons/hicolor/*/apps/io.welle.welle-gui.png
%{_mandir}/man1/welle-io.1%{?ext_man}
%doc README.md AUTHORS THANKS

%files -n welle-cli
%{_bindir}/welle-cli
%{_mandir}/man1/welle-cli.1%{?ext_man}

%changelog
