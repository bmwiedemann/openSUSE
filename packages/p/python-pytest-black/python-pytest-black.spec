#
# spec file for package python-pytest-black
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


Name:           python-pytest-black
Version:        0.6.0
Release:        0
Summary:        Black format checking plugin for pytest
License:        MIT
URL:            https://github.com/coherent-oss/pytest-black
Source:         https://files.pythonhosted.org/packages/source/p/pytest-black/pytest_black-%{version}.tar.gz
# PATCH-FIX-UPSTREAM Update pytest fixtures
Patch0:         https://github.com/coherent-oss/pytest-black/commit/75e0012.patch#/fix-pytest-makefile.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-black
Requires:       python-pytest >= 7
Requires:       python-toml
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module black}
BuildRequires:  %{python_module pytest >= 7}
BuildRequires:  %{python_module toml}
# /SECTION
%python_subpackages

%description
A pytest plugin to enable format checking with black.

%prep
%autosetup -p1 -n pytest_black-%{version}

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
%{python_sitelib}/pytest_black.py
%pycache_only %{python_sitelib}/__pycache__/pytest_black*.pyc
%{python_sitelib}/pytest_black-%{version}.dist-info

%changelog
