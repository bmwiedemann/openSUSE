#
# spec file for package cura-engine
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        4.1.0
Release:        0
Summary:        3D printer control software
License:        AGPL-3.0-only
Group:          Hardware/Printing
Url:            https://github.com/Ultimaker/CuraEngine
Source0:        CuraEngine-%{version}.tar.xz
Source1:        CuraEngine.1
# X-OPENSUSE-PATCH fix-build.patch follow openSUSE policies
Patch1:         fix-build.patch
# PATCH-FIX-OPENSUSE CuraEngine-gcc9.patch based on a patch from fedora, submitted upstream, but not merged yet
Patch2:         CuraEngine-gcc9.patch
# On TW/Factory or Leap/SLE 15 use latest gcc, gcc6 otherwise
%if 0%{?suse_version} < 1500
BuildRequires:  gcc6-c++
#!BuildIgnore:  libgcc_s1
%else
BuildRequires:  gcc-c++
%endif
BuildRequires:  cmake
BuildRequires:  gmock
BuildRequires:  gtest
BuildRequires:  libArcus-devel
BuildRequires:  stb-devel
# No 32bit support anymore
ExcludeArch:    %ix86 %arm

%description
CuraEngine is an engine for processing 3D models into 3D printing
instruction for Ultimaker and other GCode-based 3D printers.
It is part of the larger project called "Cura".

%prep
%setup -q -n CuraEngine-%version
%patch1 -p1
%patch2 -p0
# the test is hardcoding the version number
sed -i -e 's,"master","%{version}",' tests/GCodeExportTest.cpp

%build
%if 0%{?suse_version} < 1500
export CC=gcc-6
export CXX=g++-6
%endif
# make sure lib_CuraEngine is statically build and linked
%cmake -DCURA_ENGINE_VERSION=%version \
       -DCMAKE_POSITION_INDEPENDENT_CODE="true" \
       -DBUILD_SHARED_LIBS="false" \
       -DCMAKE_BUILD_TYPE=Release \
       -DBUILD_TESTS=ON
%make_jobs

%install
cd build
%make_install

install -Dm0644 %{SOURCE1} %{buildroot}%{_mandir}/man1/CuraEngine.1

%check
cd build
# we don't use "make test" to get the output on failure
/usr/bin/ctest --force-new-ctest-process --output-on-failure

%files
%license LICENSE
%doc README.md
%_bindir/CuraEngine
%_mandir/man1/CuraEngine.1*

%changelog
