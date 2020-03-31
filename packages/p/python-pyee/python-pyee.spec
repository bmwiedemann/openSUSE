#
# spec file for package python-pyee
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
Name:           python-pyee
Version:        7.0.1
Release:        0
Summary:        A port of node.js's EventEmitter to python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/jfhbrook/pyee
Source:         https://files.pythonhosted.org/packages/source/p/pyee/pyee-%{version}.tar.gz
Source99:       https://raw.githubusercontent.com/jfhbrook/pyee/master/LICENSE
# test_async.py: import asyncio.exception.TimeoutError
# https://github.com/jfhbrook/pyee/issues/68
Patch0:         python-pyee-import-asyncio.exceptions.patch
BuildRequires:  %{python_module PyHamcrest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module vcversioner}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Twisted}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest-runner}
BuildRequires:  python3-pytest-asyncio
BuildRequires:  python3-pytest-trio
# /SECTION
%python_subpackages

%description
pyee supplies an ``EventEmitter`` object similar to the ``EventEmitter``
from Node.js.

%prep
%setup -q -n pyee-%{version}
%patch0 -p1
# https://github.com/jfhbrook/pyee/issues/58
cp %{SOURCE99} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Only run tests for python3 (see test requirements)
%{python_expand #
if [ "${python_flavor}" == "python3" ]; then
    python3 setup.py test
fi
}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
