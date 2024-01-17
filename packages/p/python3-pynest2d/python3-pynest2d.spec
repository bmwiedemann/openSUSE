#
# spec file for package python3-pynest2d
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


Name:           python3-pynest2d
Version:        4.12.0
Release:        0
Summary:        CPython bindings for libnest2d
License:        LGPL-3.0-only
Group:          Development/Libraries/C and C++
URL:            https://github.com/Ultimaker/pynest2d
Source:         https://github.com/Ultimaker/pynest2d/archive/refs/tags/%{version}.tar.gz#/pynest2d-%{version}.tar.gz
# PATCH-FIX-OPENSUSE -- add PyQt5 namespace
Patch0:         pynest2d-PyQt5.sip.patch
# PATCH-FIX-UPSTREAM -- https://github.com/Ultimaker/pynest2d/pull/3
Patch1:         Retrieve-required-flags-from-Libnest2D-target.patch
BuildRequires:  cmake >= 3.6
BuildRequires:  gcc-c++
BuildRequires:  libnest2d-devel
BuildRequires:  python3-sip-devel < 5
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} > 150300
# The PyQt5.sip module. NOT a dependency on (Py)Qt5
BuildRequires:  python3-qt5-sip
Requires:       python3-qt5-sip
%else
# Older distributions provide PyQt5.sip through python3-sip
BuildRequires:  python3-sip < 5
Requires:       python3-sip < 5
%endif

%description
Binding allowing libnest2d to be called from Python using Numpy.

%prep
%autosetup -n pynest2d-%{version} -p1

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
