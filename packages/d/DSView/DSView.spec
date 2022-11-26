#
# spec file for package DSView
#
# Copyright (c) 2021 SUSE LLC
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


Name:           DSView
Version:        1.2.1
Release:        0
Summary:        GUI for DreamSourceLab USB-based instruments
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Electronics
URL:            https://www.dreamsourcelab.com
Source0:        https://github.com/DreamSourceLab/DSView/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  automake
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  fftw3-threads-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_thread-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libftdi)
BuildRequires:  pkgconfig(libserialport)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libzip)
BuildRequires:  pkgconfig(python3)
Obsoletes:      libsigrok4DSL1
Obsoletes:      libsigrokdecode4DSL4

%description
GUI for DreamSourceLab USB-based instruments

%prep
%setup -q

%build
%cmake
%cmake_build

%install
%cmake_install
%fdupes %{buildroot}%{_datadir}/libsigrokdecode4DSL/

%files
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/dsview.desktop
%{_datadir}/icons/hicolor/scalable/apps/dsview.svg
%{_datadir}/pixmaps/dsview.svg
%{_udevrulesdir}/*
%{_datadir}/libsigrokdecode4DSL/

%changelog
