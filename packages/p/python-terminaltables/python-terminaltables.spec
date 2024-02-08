#
# spec file for package python-terminaltables
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-terminaltables
Version:        3.1.10
Release:        0
Summary:        Module for generating tables in terminals from a nested list of strings
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/matthewdeanmartin/terminaltables
Source:         https://files.pythonhosted.org/packages/source/t/terminaltables/terminaltables-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/matthewdeanmartin/terminaltables/v%{version}/LICENSE
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry >= 0.12}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
Requires:       python-colorama >= 0.3.7
Requires:       python-colorclass >= 2.2.0
Requires:       python-termcolor >= 1.1.0

%python_subpackages

%description
terminaltables draws tables in terminal/console applications from a
list of lists of strings, and supports multi-line rows.

%prep
%setup -q -n terminaltables-%{version}

%build
cp %SOURCE1 LICENSE
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/*

%changelog
