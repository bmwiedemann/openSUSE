#
# spec file for package python-pyipp
#
# Copyright (c) 2025 SUSE LLC
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


%{?sle15_python_module_pythons}
Name:           python-pyipp
Version:        0.17.0
Release:        0
Summary:        Asynchronous Python client for Internet Printing Protocol (IPP)
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/ctalkington/python-ipp
Source0:        https://files.pythonhosted.org/packages/source/p/pyipp/pyipp-%{version}.tar.gz
Source1:        https://github.com/ctalkington/python-ipp/archive/%{version}.tar.gz#/pyipp-%{version}-gh-tests.tar.gz
BuildRequires:  %{python_module aiohttp >= 3.6.2}
BuildRequires:  %{python_module async-timeout}
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module covdefaults}
BuildRequires:  %{python_module deepmerge >= 0.1.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module syrupy}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module yarl >= 1.4.2}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-aiohttp >= 3.6.2
Requires:       python-deepmerge >= 0.1.0
Requires:       python-yarl >= 1.4.2
BuildArch:      noarch
%python_subpackages

%description
Asynchronous Python client for Internet Printing Protocol (IPP).

%prep
%autosetup -p1 -n pyipp-%{version} -a1
ln -s python-ipp-%{version}/tests/ tests
rm tests/test_client.py  tests/test_interface.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/pyipp
%{python_sitelib}/pyipp-%{version}.dist-info

%changelog
