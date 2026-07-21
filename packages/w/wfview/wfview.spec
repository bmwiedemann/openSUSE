#
# spec file for package wfview
#
# Copyright (c) 2025 Wojciech Kazubski <wk@ire.pw.edu.pl>
# Copyright (c) 2026 Andreas Stieger <Andreas.Stieger@gmx.de>
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
Version:        2.11
Release:        0
Summary:        ICOM SDR transceiver control software
License:        GPL-3.0-or-later
Group:          Productivity/Hamradio/Other
URL:            https://wfview.org/
Source:         https://github.com/wf-group/wfview/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         wfview-add-qcustomplot-library-name.patch
Patch1:         wfview-2.11-cachingqueue-const.patch
BuildRequires:  c++_compiler
BuildRequires:  hicolor-icon-theme
BuildRequires:  libhidapi-devel
BuildRequires:  pkgconfig
BuildRequires:  portaudio-devel
BuildRequires:  cmake(Qt6)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6SerialPort)
BuildRequires:  cmake(Qt6WebSockets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  pkgconfig(eigen3)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(qcustomplot-qt6)
BuildRequires:  pkgconfig(rtaudio)
Requires:       hicolor-icon-theme

%description
wfview controls modern Icom rigs using either a USB serial connection or OEM
network (ethernet or wifi) connection. Live, real-time spectrum analyzer data
are displayed, and rig controls are presented. Additional programs may tie into the
CIV bus using the pseudo-terminal device (linux and macOS), virtual serial port
loopback (windows), or hamlib-compatible rigctld server.

%prep
%autosetup -p1

%build
%{qmake6} \
	%{name}.pro \
	PREFIX=%{_prefix} \
	%{nil}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%files
%doc CHANGELOG CI-V.md CONTRIBUTING.md README.md WHATSNEW
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/256x256/apps/wfview.png
%{_datadir}/metainfo/org.wfview.wfview.metainfo.xml

%changelog
