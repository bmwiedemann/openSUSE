#
# spec file for package qucs-s
#
# Copyright (c) 2022 SUSE LLC
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


Name:           qucs-s
Version:        1.0.0
Release:        0
Summary:        Qucs with SPICE
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Electronics
URL:            https://ra3xdh.github.io/
Source:         https://github.com/ra3xdh/qucs_s/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:        qucs-s.rpmlintrc
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Xml)
Requires:       ngspice

%description
Qucs-S is a spin-off of the Qucs cross-platform circuit simulator. "S" letter indicates SPICE. The purpose of the Qucs-S subproject is to use free SPICE circuit simulation kernels with the Qucs GUI. It merges the power of SPICE and the simplicity of the Qucs GUI. Qucs intentionally uses its own SPICE incompatible simulation kernel Qucsator. It has advanced RF and AC domain simulation features, but most of the existing industrial SPICE models are incompatible with it. Qucs-S is not a simulator by itself, but it requires to use a simulation backend with it. The schematic document format of Qucs and Qucs-S are fully compatible.

%prep
%setup -q -n %{name}-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install
%fdupes %{buildroot}%{_datadir}/%{name}/

%files
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/
%{_datadir}/applications/%{name}.desktop
%doc %{_datadir}/man/man1/%{name}.1.gz

%changelog
