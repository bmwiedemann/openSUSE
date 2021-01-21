#
# spec file for package python-aiocontextvars
#
# Copyright (c) 2021 SUSE LLC
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
%if 0%{suse_version} <= 1500
%define pythons python3
%else
%define pythons python36
%endif
Name:           python-aiocontextvars
Version:        0.2.2
Release:        0
Summary:        Asyncio support for PEP-567 contextvars backport
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/fantix/aiocontextvars
Source0:        https://files.pythonhosted.org/packages/source/a/aiocontextvars/aiocontextvars-%{version}.tar.gz
# PATCH-FIX-OPENSUSE opensuse-clean-setup.patch -- remove deprecated test suite declarations from setup.py
Patch0:         opensuse-clean-setup.patch
BuildRequires:  %{python_module contextvars}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# for rpm/pythondisteps.py
BuildRequires:  python3-setuptools
Requires:       python-contextvars
#BuildArch:      noarch
%python_subpackages

%description
In Python 3.5 and 3.6, this package added asyncio support to the PEP-567 backport
package also named contextvars, in a very different way than Python 3.7
contextvars implementation.

In Python 3.7 this package is 100% replaced by contextvars.

%prep
%autosetup -p1 -n aiocontextvars-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.rst AUTHORS.rst CONTRIBUTING.rst
%{python_sitelib}/aiocontextvars.py
%{python_sitelib}/__pycache__/aiocontextvars*.pyc
%{python_sitelib}/aiocontextvars-%{version}*-info

%changelog
