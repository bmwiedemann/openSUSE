#
# spec file for package python-pylint-ignore
#
# Copyright (c) 2022 SUSE LLC
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
Name:           python-pylint-ignore
Version:        2021.1024
Release:        0
Summary:        Start with silence, not with noise But do start!
License:        MIT
URL:            https://github.com/mbarkhau/pylint-ignore
Source:         https://files.pythonhosted.org/packages/source/p/pylint-ignore/pylint-ignore-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pathlib2}
BuildRequires:  %{python_module pylev}
BuildRequires:  %{python_module pylint > 2.4}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-astroid > 2.1.0
Requires:       python-pathlib2
Requires:       python-pylev
Requires:       python-pylint > 2.4
BuildArch:      noarch
%python_subpackages

%description
Start with silence, not with noise. But do start!

Pylint-ignore is a wrapper around Pylint that maintains a pylint-ignore.md file.
This file is used to ignore Pylint messages without adding comments to the
source code itself. It's similar to Rupocop's .rubocop_todo.yml.

%prep
%setup -q -n pylint-ignore-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/pylint-ignore
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_expand sed -i 's,/usr/bin/env python,,' %{buildroot}%{$python_sitelib}/pylint_ignore/__main__.py

%check
%pytest

%post
%python_install_alternative pylint-ignore

%postun
%python_uninstall_alternative pylint-ignore

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%python_alternative %{_bindir}/pylint-ignore
%{python_sitelib}/*

%changelog
