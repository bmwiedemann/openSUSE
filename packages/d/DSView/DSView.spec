#
# spec file for package DSView
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


Name:           DSView
Version:        1.3.2
Release:        0
Summary:        GUI for DreamSourceLab USB-based instruments
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Electronics
URL:            https://www.dreamsourcelab.com
Source0:        https://github.com/DreamSourceLab/DSView/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         0000-added-missing-includes.patch

BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  fftw3-devel
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  libusb-1_0-devel
BuildRequires:  python3-devel
BuildRequires:  zlib-devel

Obsoletes:      libsigrok4DSL1
Obsoletes:      libsigrokdecode4DSL4

%description
GUI for DreamSourceLab USB-based instruments

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%check
%ctest

%install
%cmake_install
%fdupes %{buildroot}%{_datadir}

%files
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/dsview.desktop
%{_datadir}/icons/hicolor
%{_datadir}/icons/hicolor/scalable
%{_datadir}/icons/hicolor/scalable/apps
%{_datadir}/icons/hicolor/scalable/apps/dsview.svg
%{_datadir}/pixmaps/dsview.svg
%{_datadir}/libsigrokdecode4DSL/
%{_udevrulesdir}/*

%changelog
