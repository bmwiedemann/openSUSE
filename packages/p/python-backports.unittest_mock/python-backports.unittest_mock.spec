#
# spec file for package python-backports.unittest_mock
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
Name:           python-backports.unittest_mock
Version:        1.5
Release:        0
Summary:        Backports of unittest_mock
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/jaraco/backports.unittest_mock
Source:         https://files.pythonhosted.org/packages/source/b/backports.unittest_mock/backports.unittest_mock-%{version}.tar.gz
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
Requires:       python-mock
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Provides a function "install()" which makes the "mock" module
available as "unittest.mock" on Python 3.2 and earlier.
Also advertises a pytest plugin which configures unittest.mock
automatically.

%prep
%setup -q -n backports.unittest_mock-%{version}
rm -rf backports.unittest_mock.egg-info
rm -f pytest.ini

%build
%python_build

%install
%python_install
%python_expand rm %{buildroot}%{$python_sitelib}/backports/__init__.py*
%python_expand rm -rf %{buildroot}%{$python_sitelib}/backports/__pycache__/
%python_expand %fdupes %{buildroot}%{$python_sitelib}/backports/unittest_mock/

%check
mv backports backports_temp
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}
ln -s %{$python_sitelib}/backports/__init__.py %{buildroot}%{$python_sitelib}/backports/
py.test-%{$python_bin_suffix} -v
rm -r %{buildroot}%{$python_sitelib}/backports/__init__.py*
rm -rf %{buildroot}%{$python_sitelib}/backports/__pycache__/
}
mv backports_temp backports

%files %{python_files}
%doc CHANGES.rst README.rst
%license LICENSE
%{python_sitelib}/backports/unittest_mock/
%{python_sitelib}/backports.unittest_mock-*

%changelog
