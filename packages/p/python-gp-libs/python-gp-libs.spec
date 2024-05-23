#
# spec file for package python-gp-libs
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


%{?sle15_python_module_pythons}
Name:           python-gp-libs
Version:        0.0.7
Release:        0
Summary:        Internal utilities for projects following git-pull python package spec
License:        MIT
URL:            https://gp-libs.git-pull.com
Source:         https://files.pythonhosted.org/packages/source/g/gp-libs/gp_libs-%{version}.tar.gz
BuildRequires:  %{python_module docutils >= 0.20.1}
BuildRequires:  %{python_module myst-parser >= 2.0.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core >= 1.0.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytest-rerunfailures}
# /SECTION
BuildRequires:  fdupes
Requires:       python-docutils >= 0.20.1
Requires:       python-myst-parser >= 2.0.0
BuildArch:      noarch
%python_subpackages

%description
Incubating / dogfooding some sphinx extensions and pytest plugins on git-pull projects, e.g. cihai, vcs-python, or tmux-python.

%prep
%autosetup -p1 -n gp_libs-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Move src to a different path to do not use in tests
mv src src.bak

ignore="--ignore=tests/test_doctest_docutils.py"
ignore+=" --ignore=tests/test_linkify_issues.py"
%pytest $ignore

mv src.bak src

%files %{python_files}
%{python_sitelib}/doctest_docutils.py
%{python_sitelib}/docutils_compat.py
%{python_sitelib}/gp_libs.py
%{python_sitelib}/linkify_issues.py
%{python_sitelib}/pytest_doctest_docutils.py
%{python_sitelib}/gp_libs-%{version}.dist-info
%pycache_only %{python_sitelib}/__pycache__/*

%changelog
