#
# spec file for package python3-pynest2d
#
# Copyright (c) 2020 SUSE LLC
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


Name:           python3-pynest2d
Version:        4.8~beta
Release:        0
%define sversion        4.8-beta
Summary:        CPython bindings for libnest2d
License:        LGPL-3.0-only
Group:          Development/Libraries/C and C++
URL:            https://github.com/Ultimaker/%name
Source:         https://github.com/Ultimaker/pynest2d/archive/cura-%{sversion}.tar.gz#/pynest2d-%{version}.tar.gz
# PATCH-FIX-OPENSUSE -- add PyQt5 namespace
Patch0:         pynest2d-PyQt5.sip.patch
# PATCH-FIX-UPSTREAM -- https://github.com/Ultimaker/pynest2d/pull/3
Patch1:         Retrieve-required-flags-from-Libnest2D-target.patch
BuildRequires:  cmake >= 3.6
BuildRequires:  gcc-c++
BuildRequires:  libnest2d-devel
BuildRequires:  python3-sip-devel

%description
Binding allowing libnest2d to be called from Python using Numpy.

%prep
%autosetup -n pynest2d-cura-%{sversion} -p1

%build
%cmake

%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{python3_sitearch}/pynest2d.so

%changelog
