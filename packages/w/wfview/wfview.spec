#
# spec file for package wfview
#
# Copyright (c) 2025 Wojciech Kazubski <wk@ire.pw.edu.pl>
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


Name:           wfview
Version:        2.03
Release:        0
Summary:        ICOM SDR transceiver control software
License:        GPL-3.0-or-later
Group:          Productivity/Hamradio/Other
URL:            https://wfview.org/
Source:         https://gitlab.com/eliggett/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
BuildRequires:  eigen3-devel
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libhidapi-devel
BuildRequires:  libopus-devel
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  libqt5-qtgamepad-devel
BuildRequires:  libqt5-qtmultimedia-devel
BuildRequires:  libqt5-qtserialport-devel
BuildRequires:  libqt5-qtwebsockets-devel
BuildRequires:  portaudio-devel
BuildRequires:  qcustomplot-devel
BuildRequires:  rtaudio-devel
BuildRequires:  update-desktop-files
Requires:       hicolor-icon-theme

%description
wfview controls modern Icom rigs using either a USB serial connection or OEM
network (ethernet or wifi) connection. Live, real-time spectrum analyzer data
are displayed, and rig controls are presented. Additional programs may tie into the
CIV bus using the pseudo-terminal device (linux and macOS), virtual serial port
loopback (windows), or hamlib-compatible rigctld server.

%prep
%autosetup -p1 -n %{name}-v%{version}

%build
%qmake5 \
	%{name}.pro \
	PREFIX=%{_prefix} \
	%{nil}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

#install desktop file
%suse_update_desktop_file %{name} HamRadio

%files
%doc CHANGELOG CI-V.md CONTRIBUTING.md README.md WHATSNEW
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/256x256/apps/wfview.png
%{_datadir}/metainfo/org.wfview.wfview.metainfo.xml

%changelog
