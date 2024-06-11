#
# spec file for package python-zipp
#
# Copyright (c) 2024 SUSE LLC
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
%{?sle15_python_module_pythons}
Name:           python-zipp%{psuffix}
Version:        3.19.2
Release:        0
Summary:        Pathlib-compatible object wrapper for zip files
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/jaraco/zipp
Source:         https://files.pythonhosted.org/packages/source/z/zipp/zipp-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 56}
BuildRequires:  %{python_module setuptools_scm >= 3.4.1}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module jaraco.functools}
BuildRequires:  %{python_module jaraco.itertools}
BuildRequires:  %{python_module jaraco.test}
BuildRequires:  %{python_module more-itertools}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module zipp >= %{version}}
%endif
%python_subpackages

%description
A pathlib-compatible Zipfile object wrapper.

%prep
%setup -q -n zipp-%{version}
sed -i '/addopts/ s/--doctest-modules//' pytest.ini
# People still want this for 15.X despite Python 3.6 is not supported upstream anymore
sed -i 's/python_requires = >=3.7/python_requires = >=3.6/' setup.cfg
rm -r zipp.egg-info

%build
%pyproject_wheel

%install
%if !%{with test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
%pytest
%endif

%if !%{with test}
%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/zipp
%{python_sitelib}/zipp-%{version}*-info
%endif

%changelog
