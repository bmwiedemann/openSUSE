#
# spec file for package ldas-tools-cmake
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

Name:           ldas-tools-cmake
Version:        1.1.1
Release:        0
Summary:        A collection of CMake functions used by LDAS (LIGO Data Analysis System) Tools
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Physics
URL:            http://software.ligo.org
Source:         http://software.ligo.org/lscsoft/source/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildArch:      noarch

%description
LDAS (LIGO Data Analysis System) is a collection of libraries and executables
aid in the processing of gravitation wave data sets. %{name} provides the
a collection of cmake functions used by LDAS.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc NEWS
%{_datadir}/ldas-tools/
%{_datadir}/pkgconfig/*.pc
 
%changelog
