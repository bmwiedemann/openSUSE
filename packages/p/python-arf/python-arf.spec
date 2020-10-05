#
# spec file for package python-arf
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
# This version of the package intentionally doesn't work with
# Python < 3.5.
%define skip_python2 1
Name:           python-arf
Version:        2.6.0
Release:        0
# Note: I know that "advertisement" words are frowned on, but in this case
# the package name is an acronym so "advanced" needs to stay in
Summary:        Advanced Recording Format for physiology and behavior
License:        GPL-2.0-only
URL:            https://github.com/melizalab/arf
Source:         https://files.pythonhosted.org/packages/source/a/arf/arf-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-h5py >= 2.2
Requires:       python-numpy >= 1.3
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module h5py >= 2.2}
BuildRequires:  %{python_module numpy >= 1.3}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
The Advanced Recording Format ARF is an open standard for storing
data from neuronal, acoustic, and behavioral experiments in a
portable, high-performance, archival format. The goal is to enable
labs to share data and tools, and to allow data to be accessed and
analyzed for many years in the future.

ARF is built on the the HDF5 format, and all arf files are accessible
through standard HDF5 tools, including interfaces to HDF5 written for
other languages (e.g. MATLAB, Python, etc). ARF comprises a set of
specifications on how different kinds of data are stored.

%prep
%setup -q -n arf-%{version}
%autopatch -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license COPYING
%{python_sitelib}/*

%changelog
