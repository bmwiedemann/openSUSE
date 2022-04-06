#
# spec file for package python-extension-helpers
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-extension-helpers
Version:        1.0.0
Release:        0
Summary:        Utilities for building and installing packages in the Astropy ecosystem
License:        BSD-3-Clause
URL:            https://github.com/astropy/extension-helpers
Source:         https://files.pythonhosted.org/packages/source/e/extension-helpers/extension-helpers-%{version}.tar.gz
Source100:      python-extension-helpers-rpmlintrc
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 43}
BuildRequires:  %{python_module setuptools_scm >= 6.2}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
# /SECTION
Requires:       python-setuptools >= 40.2
BuildArch:      noarch
%python_subpackages

%description
A package that includes convenience helpers to assist with building Python
packages with compiled C/Cython extensions. It is developed by the Astropy
project but is intended to be general and usable by any Python package.

This is not a traditional package in the sense that it is not intended to be
installed directly by users or developers. Instead, it is meant to be accessed
when the setup.py command is run and should be defined as a build-time
dependency in pyproject.toml files.

%prep
%setup -q -n extension-helpers-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# do not test local source dir
%pytest --pyargs extension_helpers

%files %{python_files}
%doc CHANGES.rst README.rst
%license LICENSE.rst licenses/LICENSE_ASTROSCRAPPY.rst
%{python_sitelib}/extension_helpers
%{python_sitelib}/extension_helpers-%{version}*-info

%changelog
