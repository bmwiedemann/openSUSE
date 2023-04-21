#
# spec file
#
# Copyright (c) 2023 SUSE LLC
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif

%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
%{?sle15_python_module_pythons}
Name:           python-pep517%{psuffix}
Version:        0.13.0
Release:        0
Summary:        Wrappers to build Python packages using PEP 517 hooks
License:        MIT
URL:            https://github.com/pypa/pep517
Source:         https://files.pythonhosted.org/packages/source/p/pep517/pep517-%{version}.tar.gz
BuildRequires:  %{python_module flit-core >= 2}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module pep517 = %{version}}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools >= 30}
BuildRequires:  %{python_module testpath}
BuildRequires:  %{python_module wheel}
%endif
%if 0%{?python_version_nodots} < 311
Requires:       python-tomli >= 1.1.0
%endif
%if 0%{?python_version_nodots} < 38
Requires:       python-importlib-metadata
Requires:       python-zipp
%endif
%python_subpackages

%description
Wrappers to build Python packages using PEP 517 hooks.

%prep
%setup -q -n pep517-%{version}
sed -i -e '/--flake8/d' -e '/--strict/d' pytest.ini

# Remove what appears to be overly cautious flag
# that causes tests to require internet, both here
# and the test suites of any dependencies. Tracking at:
# https://github.com/pypa/pep517/issues/101
sed -i "s/'--ignore-installed',//" pep517/envbuild.py

%if ! %{with test}
%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
%pytest
%endif

%if ! %{with test}
%files %{python_files}
%doc README.rst doc/*.rst
%license LICENSE
%{python_sitelib}/pep517
%{python_sitelib}/pep517-%{version}*-info
%endif

%changelog
