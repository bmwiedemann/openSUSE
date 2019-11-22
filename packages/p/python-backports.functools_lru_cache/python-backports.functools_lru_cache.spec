#
# spec file for package python-backports.functools_lru_cache
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
%if %{python3_version_nodots} >= 33
%define skip_python3 1
%endif
Name:           python-backports.functools_lru_cache
Version:        1.6.1
Release:        0
Summary:        Backported functools.lru_cache
License:        MIT
URL:            https://github.com/jaraco/backports.functools_lru_cache
Source:         https://files.pythonhosted.org/packages/source/b/backports.functools_lru_cache/backports.functools_lru_cache-%{version}.tar.gz
# NOTE:
# %%{python_sitelib}/backports is a namespace package, and so under python 2 it must have a proper namespace __init__.py
# python-backports provides this __init__.py to prevent backports packages from conflicting.
# Please see:
#    https://pypi.python.org/pypi/backports/
#    https://www.python.org/dev/peps/pep-0420/%23namespace-packages-today
# If you need to link, the python-backports package is built as a subpackage of python-configparser
BuildRequires:  %{python_module backports}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-backports
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Backport of functools.lru_cache from Python 3.3 as published at
ActiveState.

%prep
%setup -q -n backports.functools_lru_cache-%{version}
rm -r backports.functools_lru_cache.egg-info
rm pytest.ini

%build
%python_build

%install
%python_install
%python_expand rm %{buildroot}%{$python_sitelib}/backports/__init__.py*
%python_expand rm -rf %{buildroot}%{$python_sitelib}/backports/__pycache__/
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
mv backports backports_temp
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}
ln -s %{$python_sitelib}/backports/__init__.py %{buildroot}%{$python_sitelib}/backports/
py.test-%{$python_bin_suffix} -v tests
rm -r %{buildroot}%{$python_sitelib}/backports/__init__.py*
rm -rf %{buildroot}%{$python_sitelib}/backports/__pycache__/
}
mv backports_temp backports

%files %{python_files}
%license LICENSE
%doc CHANGES.rst README.rst
%{python_sitelib}/backports.functools_lru_cache-%{version}-py*.egg-info
%{python_sitelib}/backports/functools_lru_cache.py*

%changelog
