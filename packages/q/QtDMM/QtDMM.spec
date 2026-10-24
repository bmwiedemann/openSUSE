#
# spec file for package QtDMM
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           QtDMM
Version:        26.2
Release:        0
Summary:        DMM Readout Software Including a Configurable Recorder
License:        GPL-3.0-only
Group:          System/GUI/Other
URL:            https://qtdmm.de/
Source:         https://github.com/qtdmm/QtDMM/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  hicolor-icon-theme
BuildRequires:  libhidapi-devel
BuildRequires:  cmake(Qt6Bluetooth)
BuildRequires:  cmake(Qt6Charts)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6SerialPort)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  pkgconfig(udev)

%description
QtDMM is a DMM readout software including a configurable recorder. The
recorder features manual start, scheduled start (at a given time), and
triggered automatic start when given thresholds are reached.
Additionally, you can start an external application when given
thresholds are reached.

Although initially written for Metex (and compatible, like VOLTCRAFT)
multimeter, which use a 14-byte protocol, several more protocols have
been added. For more information about the currently supported DMMs,
refer to the preset table.

%prep
%autosetup -p1

%build
%cmake_qt6
%qt6_build

%install
%qt6_install

%check
%ctest

%files
%doc CHANGELOG
%{_bindir}/qtdmm
%{_mandir}/man1/qtdmm.1%{?ext_man}
%{_licensedir}/qtdmm/
%{_datadir}/applications/*qtdmm.desktop
%{_datadir}/icons/hicolor/*/apps/*qtdmm.*
%{_datadir}/metainfo/*.xml
%{_udevrulesdir}/*.rules

%changelog
