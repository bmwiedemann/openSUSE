#
# spec file for package python-interegular
#
# Copyright (c) 2026 SUSE LLC
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
Name:           python-interegular
Version:        0.3.3
Release:        0
Summary:        A regex intersection checker
License:        MIT
URL:            https://github.com/MegaIng/interegular
Source:         https://files.pythonhosted.org/packages/source/i/interegular/interegular-%{version}.tar.gz
BuildRequires:  %{python_module pip}
# Test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
A library to check a subset of Python regexes for intersections, based on
greenery. It parses regular expressions into finite state machines and
computes whether two or more patterns can match a common string, focusing
on speed and compatibility with the Python re syntax.

%prep
%autosetup -p1 -n interegular-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE.txt
%doc README.md
%{python_sitelib}/interegular
%{python_sitelib}/interegular-%{version}.dist-info

%changelog
