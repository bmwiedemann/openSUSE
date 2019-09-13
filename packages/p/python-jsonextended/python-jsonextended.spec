#
# spec file for package python-jsonextended
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-jsonextended
Version:        0.7.11
Release:        0
Summary:        A module to extend the python json package functionality
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/chrisjsewell/jsonextended
Source:         https://github.com/chrisjsewell/jsonextended/archive/v%{version}.tar.gz#/jsonextended-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pathlib2
Recommends:     python-Pint
Recommends:     python-h5py
Recommends:     python-ijson
Recommends:     python-numpy
Recommends:     python-psutil
Recommends:     python-ruamel.yaml
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Pint}
BuildRequires:  %{python_module h5py}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pytest >= 3.6}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module ruamel.yaml}
BuildRequires:  python-pathlib2
# /SECTION
%ifpython2
Requires:       python-pathlib2
%endif
%python_subpackages

%description
A module to extend the python json package functionality:

  * Treat a directory structure like a nested dictionary
  * Plugin system
  * Lazy Loading
  * Tab Completion
  * Manipulation of nested structures
  * Enhanced pretty printer
  * Output to directory structure (of n folder levels)
  * On-disk indexing option for large json files
  * Units schema concept to apply and convert physical quantities

%prep
%setup -q -n jsonextended-%{version}

%build
export LANG=en_US.UTF-8
%python_build

%install
export LANG=en_US.UTF-8
%python_install
%python_expand chmod -R a-x+X %{buildroot}%{$python_sitelib}
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
# Some tests fail in i586
%pytest jsonextended -k 'not Encode_NDArray and not HDF5_Parser'

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
