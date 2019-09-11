#
# spec file for package python-backports.weakref
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-backports.weakref
Version:        1.0.post1
Release:        0
Summary:        Backport of new features in Python's weakref module
License:        Python-2.0
Group:          Development/Languages/Python
Url:            https://github.com/pjdelport/backports.weakref
Source:         https://files.pythonhosted.org/packages/source/b/backports.weakref/backports.weakref-%{version}.tar.gz
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# NOTE:
# %%{python_sitelib}/backports is a namespace package, and so under python 2 it must have a proper namespace __init__.py
# python-backports provides this __init__.py to prevent backports packages from conflicting.
# Please see:
#    https://pypi.python.org/pypi/backports/
#    https://www.python.org/dev/peps/pep-0420/%23namespace-packages-today
# If you need to link, the python-backports package is built as a subpackage of python-configparser
BuildRequires:  %{python_module backports}
Requires:       python-backports

%if %{python3_version_nodots} >= 33
%define skip_python3 1
%endif

%python_subpackages

%description
This package provides backports of new features in Python's weakref module
under the backports namespace.

%prep
%setup -q -n backports.weakref-%{version}

%build
%python_build

%install
%python_install
%python_expand rm %{buildroot}%{$python_sitelib}/backports/__init__.py*
%python_expand rm -f %{buildroot}%{$python_sitelib}/backports/__pycache__/__init__*.py*
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/backports.weakref-*-py*.egg-info
%{python_sitelib}/backports/weakref.py*
%pycache_only %dir %{python_sitelib}/backports/__pycache__/
%pycache_only %{python_sitelib}/backports/__pycache__/weakref*.py*

%changelog
