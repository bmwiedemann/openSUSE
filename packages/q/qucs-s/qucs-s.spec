#
# spec file for package qucs-s
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


%if 0%{?suse_version} < 1600
%if 0%{?sle_version} >= 1506000
%define gcc_ver 13
%else
%define gcc_ver 12
%endif
%endif

Name:           qucs-s
Version:        25.2.0
Release:        0
Summary:        Qucs with SPICE
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Electronics
URL:            https://ra3xdh.github.io/
Source:         https://github.com/ra3xdh/qucs_s/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:        qucs-s.rpmlintrc
Patch0:         qucs-s-fix-missing-returns.patch
BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  flex
%if 0%{?suse_version} < 1600
BuildRequires:  gcc%{gcc_ver}-c++
%endif
BuildRequires:  gperf
BuildRequires:  cmake(Qt6Charts)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Xml)
Requires:       ngspice

%description
Qucs-S is a spin-off of the Qucs cross-platform circuit simulator. "S" 
letter indicates SPICE. The purpose of the Qucs-S subproject is to use
free SPICE circuit simulation kernels with the Qucs GUI It merges the power
of SPICE and the simplicity of the Qucs GUI. Qucs intentionally uses its
own SPICE incompatible simulation kernel Qucsator. It has advanced RF and
AC domain simulation features, but most of the existing industrial SPICE
models are incompatible with it. Qucs-S is not a simulator by itself, but
it requires to use a simulation backend with it. The schematic document
format of Qucs and Qucs-S are fully compatible.

%prep
%setup -q -n %{name}-%{version}
%if 0%{?suse_version} >= 1600
%patch -P 0 -p1
%endif

%build
%if 0%{?suse_version} >= 1600
%cmake
%else
%cmake -DCMAKE_CXX_COMPILER=/usr/bin/g++-%{gcc_ver}
%endif
%cmake_build

%install
%cmake_install
%fdupes %{buildroot}%{_datadir}/%{name}/

%check

%files
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.1.gz
%{_mandir}/man1/qucsator_rf.1.gz
%{_mandir}/man1/qucsconv_rf.1.gz
%{_datadir}/metainfo/io.github.ra3xdh.qucs_s.metainfo.xml

%changelog
