#
# spec file for package python-autopage
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


%global skip_python2 1
Name:           python-autopage
Version:        0.5.1
Release:        0
Summary:        A library to provide automatic paging for console output
License:        Apache-2.0
URL:            https://github.com/zaneb/autopage
Source:         https://files.pythonhosted.org/packages/source/a/autopage/autopage-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module fixtures}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Autopage is a Python library to
automatically display terminal output from a program
in a pager (like `less`)

%prep
%autosetup -p1 -n autopage-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
# Do not distribute tests with the package
%python_expand rm -rf %{buildroot}%{$python_sitelib}/autopage/tests

%check
unset LESS
rm -v autopage/tests/test_end_to_end.py
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/autopage
%{python_sitelib}/autopage-%{version}*-info

%changelog
