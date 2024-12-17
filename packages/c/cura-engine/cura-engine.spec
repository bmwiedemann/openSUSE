#
# spec file for package cura-engine
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


Name:           cura-engine
%define sversion 4.13.1
Version:        4.13.1
Release:        0
Summary:        3D printer control software
License:        AGPL-3.0-only
Group:          Hardware/Printing
URL:            https://github.com/Ultimaker/CuraEngine
Source0:        https://github.com/Ultimaker/CuraEngine/archive/%{sversion}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        CuraEngine.1
# X-OPENSUSE-PATCH fix-build.patch follow openSUSE policies
Patch1:         fix-build.patch
# PATCH-FIX-UPSTREAM add-missing-include.patch -- Add missing include <cstdint>
Patch2:         add-missing-include.patch
# PATCH-FIX-OPENSUSE
Patch3:         0001-Fix-failing-build-due-to-missing-iomanip.h-include.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gmock
BuildRequires:  gtest
BuildRequires:  libArcus-devel >= %{version}
BuildRequires:  stb-devel
BuildRequires:  cmake(RapidJSON)
BuildRequires:  pkgconfig(polyclipping)
# No 32bit support anymore
ExcludeArch:    %ix86 %arm s390

%description
CuraEngine is an engine for processing 3D models into 3D printing
instruction for Ultimaker and other GCode-based 3D printers.
It is part of the larger project called "Cura".

%prep
%autosetup -p1 -n CuraEngine-%sversion
# the test is hardcoding the version number
sed -i -e 's,"master","%{version}",' tests/GCodeExportTest.cpp

%build
# make sure lib_CuraEngine is statically build and linked
%cmake -DCURA_ENGINE_VERSION=%version \
       -DCMAKE_POSITION_INDEPENDENT_CODE="true" \
       -DBUILD_SHARED_LIBS="false" \
       -DUSE_SYSTEM_LIBS=ON \
       -DBUILD_TESTS=ON
%cmake_build

%install
%cmake_install

install -Dm0644 %{SOURCE1} %{buildroot}%{_mandir}/man1/CuraEngine.1

%check
# we don't use "make test" to get the output on failure
%ctest

%files
%license LICENSE
%doc README.md
%_bindir/CuraEngine
%_mandir/man1/CuraEngine.1*

%changelog
