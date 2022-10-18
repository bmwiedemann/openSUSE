#
# spec file for package python-nest-asyncio
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
Name:           python-nest-asyncio
Version:        1.5.6
Release:        0
Summary:        Patch asyncio to allow nested event loops
License:        BSD-2-Clause
URL:            https://github.com/erdewit/nest_asyncio
Source:         https://files.pythonhosted.org/packages/source/n/nest_asyncio/nest_asyncio-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
By design asyncio `does not allow <https://bugs.python.org/issue22239>`_
its event loop to be nested. This presents a practical problem:
When in an environment where the event loop is
already running it's impossible to run tasks and wait
for the result. Trying to do so will give the error
"``RuntimeError: This event loop is already running``".

The issue pops up in various environments, such as web servers,
GUI applications and in Jupyter notebooks.

This module patches asyncio to allow nested use of ``asyncio.run`` and
``loop.run_until_complete``.

%prep
%setup -q -n nest_asyncio-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest -v tests.nest_test

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/nest_asyncio.py*
%pycache_only %{python_sitelib}/__pycache__/nest_asyncio*.pyc
%{python_sitelib}/nest_asyncio-%{version}*-info

%changelog
