#
# spec file for package python-jupyter-packaging
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


Name:           python-jupyter-packaging
Version:        0.12.3
Release:        0
Summary:        Jupyter Packaging Utilities
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/jupyter/jupyter-packaging
Source:         https://files.pythonhosted.org/packages/source/j/jupyter_packaging/jupyter_packaging-%{version}.tar.gz
# PATCH-FIX-UPSTREAM jupyter-packaging-pr178-ignoredeprecations.patch gh#jupyter/jupyter-packaging#178
Patch0:         https://github.com/jupyter/jupyter-packaging/pull/178.patch#/jupyter-packaging-pr178-ignoredeprecations.patch
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module deprecation}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 60.2}
BuildRequires:  %{python_module tomlkit}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-deprecation
Requires:       python-packaging
Requires:       python-setuptools >= 60.2
Requires:       python-tomlkit
Requires:       python-wheel
Provides:       python-jupyter_packaging = %{version}-%{release}
# SECTION test requirements
BuildRequires:  %{python_module build}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest}
#/SECTION
BuildArch:      noarch
%python_subpackages

%description
This package contains utilities for making Python packages
with and without accompanying JavaScript packages

%prep
%autosetup -p1 -n jupyter_packaging-%{version}
sed -i 's/\r$//' README.md
sed -i -e '/^#!\//, 1d' jupyter_packaging/*.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# tests call pip which wants to check the online cache
donttest="test_install or test_datafiles_install"
donttest+=" or test_build_api and (test_build_package or test_deprecated_metadata)"
# want to write into system sitelib
donttest+=" or test_create_cmdclass"
# calls python (=python2)
donttest+=" or test_run"
%pytest -k "not ($donttest)"

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/jupyter_packaging
%{python_sitelib}/jupyter_packaging-%{version}*-info

%changelog
