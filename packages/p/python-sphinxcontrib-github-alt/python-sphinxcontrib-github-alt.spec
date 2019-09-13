#
# spec file for package python-sphinxcontrib-github-alt
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
%bcond_with     test
Name:           python-sphinxcontrib-github-alt
Version:        1.1
Release:        0
Summary:        Sphinx extension to link to GitHub issues, pull requests, commits and users
License:        BSD-2-Clause
Group:          Development/Languages/Python
Url:            http://github.com/Calysto/octave_kernel
Source0:        https://files.pythonhosted.org/packages/source/s/sphinxcontrib_github_alt/sphinxcontrib_github_alt-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Sphinx
Requires:       python-docutils
BuildArch:      noarch

%python_subpackages

%description
A Sphinx extension to link to GitHub issues, pull requests, commits
and users for a particular project.

To use this extension, add it to the extensions list in conf.py,
and set the variable github_project_url:

%prep
%setup -q -n sphinxcontrib_github_alt-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license COPYING.md
%doc README.rst
%{python_sitelib}/sphinxcontrib_github_alt*
%pycache_only %{python_sitelib}/__pycache__/sphinxcontrib_github_alt*.py*

%changelog
