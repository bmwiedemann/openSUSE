#
# spec file for package python-Pint
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
%define         skip_python2 1
Name:           python-Pint
Version:        0.15
Release:        0
Summary:        Physical quantities module
License:        BSD-3-Clause
URL:            https://github.com/hgrecco/pint
Source:         https://files.pythonhosted.org/packages/source/P/Pint/Pint-%{version}.tar.gz
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-importlib-metadata
Requires:       python-packaging
Requires:       python-uncertainties >= 3.0
Recommends:     python-numpy
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module importlib-metadata}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pytest >= 4.0}
BuildRequires:  %{python_module uncertainties >= 3.0}
# /SECTION
%python_subpackages

%description
Pint is Python module/package to define, operate and manipulate physical
quantities, the product of a numerical value and a unit of measurement.
It allows arithmetic operations between them and conversions from and
to different units.

It is distributed with a comprehensive list of physical units, prefixes
and constants. Due to it's modular design, you to extend (or even rewrite!)
the complete list without changing the source code.

%prep
%setup -q -n Pint-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Test assumes 64bit arch
# See: https://github.com/hgrecco/pint/issues/1006
%pytest -k 'not test_result_type_numpy_func'

%files %{python_files}
%license LICENSE
%doc AUTHORS CHANGES README.rst
%{_bindir}/pint-convert
%{python_sitelib}/Pint-0*-py*.egg-info
%{python_sitelib}/pint/

%changelog
