#
# spec file for package python-astunparse
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
Name:           python-astunparse
Version:        1.6.2
Release:        0
Summary:        An AST unparser for Python
License:        BSD-3-Clause AND Python-2.0
Group:          Development/Languages/Python
URL:            https://github.com/simonpercivall/astunparse
Source:         https://files.pythonhosted.org/packages/source/a/astunparse/astunparse-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six >= 1.6.1}
BuildRequires:  %{python_module wheel >= 0.23.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six >= 1.6.1
Requires:       python-wheel >= 0.23.0
BuildArch:      noarch
%python_subpackages

%description
This is a factored out version of ``unparse`` found in the Python
source distribution; under Demo/parser in Python 2 and under
Tools/parser in Python 3.

This library is single-source compatible with Python 2.6 through
Python 3.5. It is authored by the Python core developers; I have
simply merged the Python 2.7 and the Python 3.5 source and test
suites, and added a wrapper. This factoring out is to provide a
library implementation that supports both versions.

Added to this is a pretty-printing dump utility function.

%prep
%setup -q -n astunparse-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%doc AUTHORS.rst README.rst HISTORY.rst
%license LICENSE
%{python_sitelib}/*

%changelog
