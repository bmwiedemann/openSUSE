#
# spec file for package ldas-tools-cmake
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


Name:           ldas-tools-cmake
Version:        1.3.0
Release:        0
Summary:        A collection of CMake functions used by LDAS (LIGO Data Analysis System) Tools
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Physics
URL:            https://software.ligo.org
Source0:        https://software.ligo.org/lscsoft/source/%{name}-%{version}.tar.gz
# Upstream missed COPYING file in tarball
Source1:        https://git.ligo.org/computing/ldastools/igwn-cmake/-/raw/igwn-cmake-macros-1.5.0/COPYING
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(igwncmake)
Requires:       pkgconfig(igwncmake)
BuildArch:      noarch

%description
LDAS (LIGO Data Analysis System) is a collection of libraries and executables
aid in the processing of gravitation wave data sets. %{name} provides the
a collection of cmake functions used by LDAS.

%prep
%autosetup -p1
cp %{SOURCE1} ./

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license COPYING
%{_datadir}/ldas-tools/
%{_datadir}/pkgconfig/*.pc

%changelog
