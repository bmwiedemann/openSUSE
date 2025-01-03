#
# spec file for package python-jirafs
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


# missing ipdb
%global skip_python313 1
%{?sle15_python_module_pythons}
Name:           python-jirafs
Version:        2.3.1
Release:        0
Summary:        Library for editing JIRA issues as local text files
License:        MIT
URL:            https://github.com/coddingtonbear/jirafs
Source:         https://github.com/coddingtonbear/jirafs/archive/refs/tags/%{version}.tar.gz#/jirafs-%{version}.tar.gz
# PATCH-FIX-UPSTREAM gh#coddingtonbear/jirafs#70
Patch0:         remove-mock.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       git-core
Requires:       python-Jinja2 >= 2.10.3
Requires:       python-Pillow
Requires:       python-PrettyTable >= 0.7.2
Requires:       python-blessings >= 1.5.1
Requires:       python-environmental-override >= 0.1.2
Requires:       python-jira >= 3.1.1
Requires:       python-prettytable >= 0.7.2
Requires:       python-python-dateutil >= 2.8.1
Requires:       python-watchdog >= 0.9.0
Requires(post): update-alternatives
Requires(postun): update-alternatives
Suggests:       python-ipdb
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Jinja2 >= 2.10.3}
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module PrettyTable >= 0.7.2}
BuildRequires:  %{python_module behave}
BuildRequires:  %{python_module blessings >= 1.5.1}
BuildRequires:  %{python_module environmental-override >= 0.1.2}
BuildRequires:  %{python_module ipdb}
BuildRequires:  %{python_module jira >= 3.1.1}
BuildRequires:  %{python_module prettytable >= 0.7.2}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil >= 2.8.1}
BuildRequires:  %{python_module watchdog >= 0.9.0}
BuildRequires:  git-core
# /SECTION
%python_subpackages

%description
This library lets the user stay out of JIRA by letting them edit JIRA
issues as a collection of text files using an interface inspired by
`git` and `hg`.

%prep
%autosetup -p1 -n jirafs-%{version}

# Remove upper pins
sed -i 's/,<[0-9.][0-9.]*//' requirements.txt
rm jirafs/.pre-commit-config.yaml

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/jirafs

%check
git config --global user.name "John Doe"
git config --global user.email johndoe@example.com
%pytest -rs

%post
%python_install_alternative jirafs

%postun
%python_uninstall_alternative jirafs

%files %{python_files}
%python_alternative %{_bindir}/jirafs
%{python_sitelib}/jirafs
%{python_sitelib}/jirafs-%{version}.dist-info

%changelog
