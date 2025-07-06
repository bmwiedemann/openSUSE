#
# spec file for package python-numericalunits
#
# Copyright (c) 2025 SUSE LLC
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


Name:           python-numericalunits
Version:        1.26
Release:        0
Summary:        Python module for defining quantities with units
License:        MIT
URL:            https://github.com/sbyrnes321/numericalunits
Source:         https://files.pythonhosted.org/packages/source/n/numericalunits/numericalunits-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/sbyrnes321/numericalunits/master/tests/tests.py
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Units and dimensional analysis compatible with everything

This package implements units and dimensional analysis in an unconventional
way with unique advantages:

* Compatible with everything
* Zero storage overhead
* Zero calculation overhead

%prep
%setup -q -n numericalunits-%{version}
dos2unix numericalunits.py
cp %{SOURCE1} .

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest discover -v tests/

%files %{python_files}
%license LICENSE.txt
%doc Changes.txt README.rst
%{python_sitelib}/numericalunits.py
%pycache_only %{python_sitelib}/__pycache__/numericalunits*.pyc
%{python_sitelib}/numericalunits-%{version}.dist-info

%changelog
