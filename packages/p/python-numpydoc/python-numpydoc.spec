#
# spec file for package python-numpydoc
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


%{?!python_module:%define python_module() python3-%{**}}
Name:           python-numpydoc
Version:        1.5.0
Release:        0
Summary:        Sphinx extension to support docstrings in Numpy format
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/numpy/numpydoc
Source:         https://files.pythonhosted.org/packages/source/n/numpydoc/numpydoc-%{version}.tar.gz
# https://docs.python.org/3/objects.inv (changes from time to time, accessed 2021-02-23)
Source1:        python-objects.inv
BuildRequires:  %{python_module Jinja2 >= 2.10}
BuildRequires:  %{python_module Sphinx >= 4.2}
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Jinja2 >= 2.10
Requires:       python-Sphinx >= 4.2
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Numpy's documentation uses several custom extensions to Sphinx.  These
are shipped in this numpydoc package, in case you want to make use
of them in third-party projects.

%prep
%setup -q -n numpydoc-%{version}
# remove interpreter line. This script has no main section
sed -i '1 {/env python/ d}' numpydoc/validate.py
# don't check coverage
sed -i 's/--cov.*$//' setup.cfg
# provide the python doc inventory locally
sed -i "\|https://docs.python.org/3| s|None|'%{SOURCE1}'|" numpydoc/tests/tinybuild/conf.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# ignore doc: gh#numpy/numpydoc#296
%pytest --ignore doc/

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%{python_sitelib}/numpydoc/
%{python_sitelib}/numpydoc-%{version}-py*.egg-info

%changelog
