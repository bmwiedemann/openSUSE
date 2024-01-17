#
# spec file for package jaero
#
# Copyright (c) 2021 SUSE LLC
# Copyright (c) 2017-2021, Martin Hauke <mardnh@gmx.de>
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


Name:           jaero
Version:        1.0.4.13
Release:        0
Summary:        A SatCom ACARS demodulator and decoder for the Aero standard
License:        GPL-3.0-or-later AND MIT
Group:          Productivity/Hamradio/Other
URL:            https://jontio.zapto.org/hda1/jaero.html
Source:         https://github.com/jontio/JAERO/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.xz
# Bundled JFFT is licenced under MIT
Source1:        https://github.com/jontio/JFFT/archive/refs/heads/master.zip
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libcorrect-devel
BuildRequires:  libqt5-qtbase-common-devel
BuildRequires:  pkgconfig
BuildRequires:  unzip
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(libacars)
BuildRequires:  pkgconfig(libzmq)
BuildRequires:  pkgconfig(qcustomplot)
BuildRequires:  pkgconfig(vorbis)
Requires:       unzip

%description
JAERO is a program that demodulates and decodes Classic Aero ACARS (Aircraft
Communications Addressing and Reporting System) messages sent from satellites to
aeroplanes (SatCom ACARS), commonly used when planes are beyond VHF range.

Demodulation is performed using the soundcard.

Such signals are typically around 1.5Ghz and can be received with a
low-gain antenna that can be home-brewed in conjunction with an
RTL-SDR dongle.

%prep
%setup -q -n JAERO-%{version}
unzip %{SOURCE1} && mv JFFT-master JFFT

%build
mkdir JAERO/build
cd JAERO/build
%qmake5 ..
%make_jobs

%install
install -Dpm 0755 JAERO/build/JAERO  %{buildroot}/%{_bindir}/jaero
install -Dpm 0644 JAERO/images/primary-modem.svg %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%suse_update_desktop_file -c %{name} JAERO "A SatCom ACARS demodulator and decoder for the Aero standard" %{name} %{name} Network HamRadio

%files
%license LICENSE
%doc README.md
%{_bindir}/jaero
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%changelog
