#
# spec file for package python-importlib-resources
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
Name:           python-importlib-resources
Version:        3.3.0
Release:        0
Summary:        Read resources from Python packages
License:        Apache-2.0
URL:            https://importlib-resources.readthedocs.io/
Source:         https://files.pythonhosted.org/packages/source/i/importlib_resources/importlib_resources-%{version}.tar.gz
BuildRequires:  %{python_module setuptools_scm >= 3.4.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module testsuite}
BuildRequires:  %{python_module toml}
BuildRequires:  (python3-zipp >= 0.4 if python3-base < 3.8)
BuildRequires:  (python36-zipp >= 0.4 if python36-base)
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Provides:       python-importlib_resources = %{version}
Obsoletes:      python-importlib_resources < %{version}
BuildArch:      noarch
%if %{?suse_version} <= 1500
BuildRequires:  python2-contextlib2
BuildRequires:  python2-pathlib2
BuildRequires:  python2-singledispatch
BuildRequires:  python2-typing
BuildRequires:  python2-zipp >= 0.4
%endif
%ifpython2
Requires:       python-pathlib2
Requires:       python-singledispatch
Requires:       python-typing
Requires:       python-zipp >= 0.4
%endif
%if "%{python_flavor}" == "python36"
Requires:       python36-zipp >= 0.4
%endif
%if "%{python_flavor}" == "python3" && %{python3_version_nodots} < 38
Requires:       python3-zipp >= 0.4
%endif
%python_subpackages

%description
importlib_resources is a library which provides for access to resources in
Python packages. It provides functionality similar to pkg_resources Basic
Resource Access API, but without all of the overhead and performance problems of
pkg_resources.

importlib_resources is a backport of Python 3.9’s standard library
importlib.resources module for Python 2.7, and 3.5 through 3.8. Users of Python
3.9 and beyond are encouraged to use the standard library module. Developers
looking fo

%prep
%setup -q -n importlib_resources-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest -v

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/importlib_resources
%{python_sitelib}/importlib_resources-%{version}*-info

%changelog
