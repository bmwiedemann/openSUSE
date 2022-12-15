#
# spec file for package python-importlib-resources
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


%{?!python_module:%define python3-%{**}}
%define skip_python2 1
Name:           python-importlib-resources
Version:        5.10.1
Release:        0
Summary:        Read resources from Python packages
License:        Apache-2.0
URL:            https://importlib-resources.readthedocs.io/
Source:         https://files.pythonhosted.org/packages/source/i/importlib_resources/importlib_resources-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest >= 6}
BuildRequires:  %{python_module setuptools_scm >= 3.4.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module testsuite}
BuildRequires:  %{python_module toml}
BuildRequires:  %{python_module wheel}
# Breaking the depcycle; not absolutely needed as ZipReader is not executed in tests.
# BuildRequires:  %%{python_module zipp >= 3.1.0 if %%python-base < 3.10}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Provides:       python-importlib_resources = %{version}
Obsoletes:      python-importlib_resources < %{version}
BuildArch:      noarch
%if 0%{python_version_nodots} < 310
Requires:       python-zipp >= 3.1.0
%endif
%python_subpackages

%description
importlib_resources is a backport of Python standard library
importlib.resources module for older Pythons. Users of Python 3.9 and
beyond should use the standard library module, since for these versions,
importlib_resources just delegates to that module.

The key goal of this module is to replace parts of pkg_resources with a
solution in Python’s stdlib that relies on well-defined APIs. This makes
reading resources included in packages easier, with more stable and
consistent semantics.

%prep
%setup -q -n importlib_resources-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# create pycache so that update-zips.py does not fail with ValueError
python3 -m compileall $PWD/importlib_resources/tests/
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/importlib_resources
%{python_sitelib}/importlib_resources-%{version}*-info

%changelog
