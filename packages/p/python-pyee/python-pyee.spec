#
# spec file for package python-pyee
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
%bcond_without test
Name:           python-pyee
Version:        6.0.0
Release:        0
Summary:        A port of node.js's EventEmitter to python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/jfhbrook/pyee
Source:         https://files.pythonhosted.org/packages/source/p/pyee/pyee-%{version}.tar.gz
Source99:       https://raw.githubusercontent.com/jfhbrook/pyee/master/LICENSE
# PATCH-FIX-UPSTREAM fix-build-requirements.patch
Patch0:         fix-build-requirements.patch
BuildRequires:  %{python_module PyHamcrest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module vcversioner}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test requirements
%if %{with test}
BuildRequires:  %{python_module Twisted}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest-runner}
BuildRequires:  python3-pytest-asyncio
%endif
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

%if %{with test} && 0%{?suse_version} >= 1500
%check
# Only run tests for python3
%{python_expand #
if [ "${python_flavor}" == "python3" ]; then
    python3 setup.py test
fi
}
%endif

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
