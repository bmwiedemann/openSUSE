#
# spec file for package python-backports.tempfile
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
%define skip_python3 1
Name:           python-backports.tempfile
Version:        1.0
Release:        0
Summary:        Backport of new features in Python's tempfile module
License:        Python-2.0
Group:          Development/Languages/Python
URL:            https://github.com/pjdelport/backports.tempfile
Source:         https://files.pythonhosted.org/packages/source/b/backports.tempfile/backports.tempfile-%{version}.tar.gz
BuildRequires:  %{python_module backports.test.support}
BuildRequires:  %{python_module backports.weakref}
# NOTE:
# %%{python_sitelib}/backports is a namespace package, and so under python 2 it must have a proper namespace __init__.py
# python-backports provides this __init__.py to prevent backports packages from conflicting.
# Please see:
#    https://pypi.python.org/pypi/backports/
#    https://www.python.org/dev/peps/pep-0420/%23namespace-packages-today
# If you need to link, the python-backports package is built as a subpackage of python-configparser
BuildRequires:  %{python_module backports}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-backports
Requires:       python-backports.weakref
BuildArch:      noarch
%python_subpackages

%description
This package provides backports of new features in Python's tempfile module
under the backports namespace.

%prep
%setup -q -n backports.tempfile-%{version}

%build
%python_build

%install
%python_install
%python_expand rm %{buildroot}%{$python_sitelib}/backports/__init__.py*
%python_expand rm -f %{buildroot}%{$python_sitelib}/backports/__pycache__/__init__*.py*
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Store and restore 'backports', so check logic doesnt alter install before rpm is pressed
%{python_expand cp -r %{buildroot}%{$python_sitelib}/backports/ %{buildroot}%{$python_sitelib}/backports.orig
cp %{$python_sitelib}/backports/*.py %{buildroot}%{$python_sitelib}/backports/
PYTHONPATH=%{buildroot}%{$python_sitelib} $python -m pytest
rm -r %{buildroot}%{$python_sitelib}/backports/
mv %{buildroot}%{$python_sitelib}/backports.orig/ %{buildroot}%{$python_sitelib}/backports
}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/backports.tempfile-*-py*.egg-info
%{python_sitelib}/backports/tempfile.py*
%pycache_only %dir %{python_sitelib}/backports/__pycache__/
%pycache_only %{python_sitelib}/backports/__pycache__/tempfile*.py*

%changelog
