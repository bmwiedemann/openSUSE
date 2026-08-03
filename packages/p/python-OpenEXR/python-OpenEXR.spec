#
# spec file for package python-OpenEXR
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


%define         modname openexr
Name:           python-OpenEXR
Version:        3.4.13
Release:        0
Summary:        Python bindings for the OpenEXR image file format
License:        BSD-3-Clause
URL:            https://github.com/AcademySoftwareFoundation/OpenEXR
Source0:        https://files.pythonhosted.org/packages/source/O/OpenEXR/%{modname}-%{version}.tar.gz
Patch0:         force-system-dependencies.patch
Patch1:         remove-rpath.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pybind11-devel}
BuildRequires:  %{python_module scikit-build-core}
BuildRequires:  c++_compiler
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(Imath)
BuildRequires:  pkgconfig(libdeflate)
BuildRequires:  pkgconfig(openjph)
Requires:       python-numpy
%python_subpackages

%description
This package provides python bindings for openexr image file format.

%prep
%autosetup -p1 -n %{modname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%python_expand rm %{buildroot}%{$python_sitearch}/Imath.py
%python_expand rm -r %{buildroot}%{$python_sitearch}/__pycache__

%files %{python_files}
%{python_sitearch}/OpenEXR.cpython-%{python_version_nodots}-%{_arch}-linux-gnu.so
%{python_sitearch}/%{modname}-%{version}.dist-info

%changelog
