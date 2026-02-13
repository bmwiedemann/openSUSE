#
# spec file for package python-terminaltables3
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


%{?sle15_python_module_pythons}
Name:           python-terminaltables3
Version:        4.0.0
Release:        0
Summary:        Module for generating tables in terminals from a nested list of strings
License:        MIT
URL:            https://github.com/matthewdeanmartin/terminaltables3
Source:         https://github.com/matthewdeanmartin/terminaltables3/archive/refs/tags/v%{version}.tar.gz#/terminaltables3-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core >= 1.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module colorama >= 0.3.7}
BuildRequires:  %{python_module colorclass >= 2.2.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module termcolor >= 1.1.0}
# /SECTION
BuildArch:      noarch
Requires:       python-colorama >= 0.3.7
Requires:       python-colorclass >= 2.2.0
Requires:       python-termcolor >= 1.1.0
%python_subpackages

%description
terminaltables draws tables in terminal/console applications from a
list of lists of strings, and supports multi-line rows.

%prep
%setup -q -n terminaltables3-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Stop termcolor from attempting to detect whether the terminal supports color
export FORCE_COLOR=1
%pytest

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/terminaltables3
%{python_sitelib}/terminaltables3-%{version}.dist-info

%changelog
