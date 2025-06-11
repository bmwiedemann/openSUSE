#
# spec file for package python-pylint-ignore
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


%bcond_without libalternatives
Name:           python-pylint-ignore
Version:        2022.1025
Release:        0
Summary:        Start with silence, not with noise But do start!
License:        MIT
URL:            https://github.com/mbarkhau/pylint-ignore
Source:         https://files.pythonhosted.org/packages/source/p/pylint-ignore/pylint-ignore-%{version}.tar.gz
# PATCH-FIX-UPSTREAM gh#mbarkhau/pylint-ignore#15
Patch0:         no-more-pathlib2.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
Requires:       python-astroid > 2.1.0
Requires:       python-pylev
Requires:       python-pylint > 2.4
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pylev}
BuildRequires:  %{python_module pylint > 2.4}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module typing_extensions}
# /SECTION
%python_subpackages

%description
Start with silence, not with noise. But do start!

Pylint-ignore is a wrapper around Pylint that maintains a pylint-ignore.md file.
This file is used to ignore Pylint messages without adding comments to the
source code itself. It's similar to Rupocop's .rubocop_todo.yml.

%prep
%autosetup -p1 -n pylint-ignore-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/pylint-ignore
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_expand sed -i 's,%{_bindir}/env python,,' %{buildroot}%{$python_sitelib}/pylint_ignore/__main__.py

%check
%pytest

%pre
%python_libalternatives_reset_alternative pylint-ignore

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%python_alternative %{_bindir}/pylint-ignore
%{python_sitelib}/pylint_ignore
%{python_sitelib}/pylint_ignore-%{version}*-info

%changelog
