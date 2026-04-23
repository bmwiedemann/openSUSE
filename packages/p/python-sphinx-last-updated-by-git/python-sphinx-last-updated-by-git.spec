#
# spec file for package python-sphinx-last-updated-by-git
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           python-sphinx-last-updated-by-git
Version:        0.3.8
Release:        0
Summary:        Get the "last updated" time for each Sphinx page from Git
License:        BSD-2-Clause
URL:            https://github.com/mgeier/sphinx-last-updated-by-git/
Source:         https://files.pythonhosted.org/packages/source/s/sphinx-last-updated-by-git/sphinx_last_updated_by_git-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 40.8.0}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module Sphinx >= 1.8}
BuildRequires:  %{python_module pytest}
BuildRequires:  git-core
BuildRequires:  unzip
# /SECTION
BuildRequires:  fdupes
Requires:       python-Sphinx >= 1.8
BuildArch:      noarch
%python_subpackages

%description
Get the "last updated" time for each Sphinx page from Git

%prep
%autosetup -p1 -n sphinx_last_updated_by_git-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Most of the testsuite requires two submodules exactly checked out
%pytest -k "test_without_git_repo"

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/sphinx_last_updated_by_git.py
%pycache_only %{python_sitelib}/__pycache__/sphinx_last_updated_by_git.*.pyc
%{python_sitelib}/sphinx_last_updated_by_git-%{version}.dist-info

%changelog
