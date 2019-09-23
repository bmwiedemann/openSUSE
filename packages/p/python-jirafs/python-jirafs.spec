#
# spec file for package python-jirafs
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
Name:           python-jirafs
Version:        1.17.3
Release:        0
Summary:        Library for editing JIRA issues as local text files
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/coddingtonbear/jirafs
Source:         https://files.pythonhosted.org/packages/source/j/jirafs/jirafs-%{version}.tar.gz
Patch0:         capitalization.patch
BuildRequires:  %{python_module PrettyTable}
BuildRequires:  %{python_module behave}
BuildRequires:  %{python_module blessings}
BuildRequires:  %{python_module environmental-override}
BuildRequires:  %{python_module ipdb}
BuildRequires:  %{python_module jira}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module tox}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PrettyTable
Requires:       python-blessings
Requires:       python-environmental-override
Requires:       python-ipdb
Requires:       python-jira
Requires:       python-six
BuildArch:      noarch
%python_subpackages

%description
This library lets the user stay out of JIRA by letting them edit JIRA
issues as a collection of text files using an interface inspired by
`git` and `hg`.

%prep
%setup -q -n jirafs-%{version}
%autopatch -p1

%build
%python_build

%install
%python_install
%{python_expand rm -r %{buildroot}%{$python_sitelib}/tests
%fdupes %{buildroot}%{$python_sitelib}
}

%check
# tests require running JIRA instance
#%%python_exec -m unittest discover -v

%files %{python_files}
%python3_only %{_bindir}/jirafs
%{python_sitelib}/*

%changelog
