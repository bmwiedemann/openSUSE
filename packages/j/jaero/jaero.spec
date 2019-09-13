#
# spec file for package jaero
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2017, Martin Hauke <mardnh@gmx.de>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           jaero
Version:        1.0.4.6
Release:        0
Summary:        A SatCom ACARS demodulator and decoder for the Aero standard
# Bundled qcustomplot is GPL-3.0+
License:        MIT and GPL-3.0+
Group:          Productivity/Hamradio/Other
Url:            http://jontio.zapto.org/hda1/jaero.html
Source:         https://github.com/jontio/JAERO/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.xz
BuildRequires:  gcc-c++
BuildRequires:  libqt5-qtbase-common-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
Requires(post): update-desktop-files
Requires(postun): update-desktop-files

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

%build
mkdir JAERO/build
cd JAERO/build
%qmake5 ..
%make_jobs

%install
install -Dpm 0755 JAERO/build/JAERO %{buildroot}/%{_bindir}/JAERO
mkdir -p %{buildroot}/%{_datadir}/applications/
install -Dpm 0644 JAERO/JAERO.desktop %{buildroot}/%{_datadir}/applications/JAERO.desktop
mkdir -p %{buildroot}/%{_datadir}/pixmaps/
install -Dpm 0644 JAERO/images/primary-modem.svg %{buildroot}/%{_datadir}/pixmaps/JAERO.svg

%post
%desktop_database_post

%postun
%desktop_database_postun

%files
%defattr(-,root,root)
%doc README.md JAERO/LICENSE
%{_bindir}/JAERO
%{_datadir}/applications/JAERO.desktop
%{_datadir}/pixmaps/JAERO.svg

%changelog
