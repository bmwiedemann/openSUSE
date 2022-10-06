#
# spec file for package python-pyee
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
Name:           python-pyee
Version:        9.0.4
Release:        0
Summary:        A port of node.js's EventEmitter to python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/jfhbrook/pyee
Source:         https://files.pythonhosted.org/packages/source/p/pyee/pyee-%{version}.tar.gz
BuildRequires:  %{python_module PyHamcrest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module vcversioner}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Twisted}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-trio if %python-base >= 3.7}
BuildRequires:  %{python_module trio if %python-base >= 3.7}
# /SECTION
%python_subpackages

%description
pyee supplies an ``EventEmitter`` object similar to the ``EventEmitter``
from Node.js.

%prep
%setup -q -n pyee-%{version}
sed -i 's/^from mock import/from unittest.mock import/' tests/test_*.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/pyee
%{python_sitelib}/pyee-%{version}*-info

%changelog
