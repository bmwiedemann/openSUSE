#
# spec file for package votca-csgapps
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2013-2020 Christoph Junghans
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

Name:       votca-csgapps
Version:    1.6
%define     uversion %{version}
Release:    0
Summary:    VOTCA coarse-graining engine applications
Group:      Productivity/Scientific/Chemistry
License:    Apache-2.0
URL:        http://www.votca.org
Source0:    https://github.com/votca/csgapps/archive/v%{uversion}.tar.gz#/%{name}-%{uversion}.tar.gz
BuildRoot:  %{_tmppath}/%{name}-%{version}-build

BuildRequires:  gromacs-devel
BuildRequires:  gcc-c++
BuildRequires:  pkg-config
BuildRequires:  fdupes
BuildRequires:  libboost_program_options-devel
BuildRequires:  votca-csg-devel = %{version}
BuildRequires:  votca-tools-devel = %{version}
BuildRequires:  cmake

%description
Versatile Object-oriented Toolkit for Coarse-graining Applications (VOTCA) is
a package to reduce the amount of routine work when doing systematic
coarse-graining of various systems. The core is written in C++.

This package contains sample applications of the VOTCA Coarse Graining Engine.

%prep
%setup -n csgapps-%{uversion} -q

%build
%{cmake} -DENABLE_TESTING=ON
%cmake_build

%install
%cmake_install

%fdupes %{buildroot}%{_prefix}

%check
make -C build test CTEST_OUTPUT_ON_FAILURE=1

%files
%doc README.md
%{_bindir}/*

%changelog
