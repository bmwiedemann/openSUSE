#
# spec file for package python-numericalunits
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
Name:           python-numericalunits
Version:        1.23
Release:        0
Summary:        Python module for defining quantities with units
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/sbyrnes321/numericalunits
Source:         https://files.pythonhosted.org/packages/source/n/numericalunits/numericalunits-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/sbyrnes321/numericalunits/master/tests/tests.py
BuildRequires:  %{python_module setuptools}
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
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test --test-suite=tests

%files %{python_files}
%license LICENSE.txt
%doc Changes.txt README.rst
%{python_sitelib}/numericalunits-%{version}*egg-info/
%{python_sitelib}/numericalunits.py*
%pycache_only %{python_sitelib}/__pycache__/numericalunits.*

%changelog
