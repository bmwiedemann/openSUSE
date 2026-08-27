#
# spec file for package jaero
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2017-2026, Martin Hauke <mardnh@gmx.de>
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


# JFFT has no releases or tags, so pin the revision that upstream JAERO
# builds and ships against.
%define jfft_commit 4b74486e58e1d266f1cc3c570f3d073d40c353d6
Name:           jaero
Version:        1.0.4.14
Release:        0
Summary:        A SatCom ACARS demodulator and decoder for the Aero standard
License:        GPL-3.0-or-later AND MIT
URL:            https://jontio.zapto.org/hda1/jaero.html
Source0:        https://github.com/jontio/JAERO/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Bundled JFFT is licenced under MIT
Source1:        https://github.com/jontio/JFFT/archive/%{jfft_commit}.tar.gz#/JFFT-%{jfft_commit}.tar.gz
Source2:        %{name}.desktop
# PATCH-FIX-OPENSUSE jaero-fix-build-with-qcustomplot-qt5.patch -- link against
# the Qt5 flavour of qcustomplot, which is how openSUSE names the library
Patch0:         jaero-fix-build-with-qcustomplot-qt5.patch
# PATCH-FIX-OPENSUSE jaero-use-system-qmqtt.patch -- build against the system
# qmqtt shared library instead of the qmake module upstream builds in-tree
Patch1:         jaero-use-system-qmqtt.patch
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libcorrect-devel
BuildRequires:  libqt5-qtbase-common-devel
BuildRequires:  pkgconfig
BuildRequires:  qmqtt-qt5-devel
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(libacars-2)
BuildRequires:  pkgconfig(libzmq)
BuildRequires:  pkgconfig(qcustomplot-qt5)
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
%autosetup -p1 -n JAERO-%{version} -a1
mv JFFT-%{jfft_commit} JFFT

%build
mkdir -p JAERO/build
pushd JAERO/build
%qmake5 ..
%make_build
popd

%install
install -D -m 0755 JAERO/build/JAERO %{buildroot}%{_bindir}/%{name}
install -D -m 0644 JAERO/images/primary-modem.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
install -D -m 0644 %{SOURCE2} %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%changelog
