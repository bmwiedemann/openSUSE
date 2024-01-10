#
# spec file for package python-requirements-parser
#
# Copyright (c) 2023 SUSE LLC
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
Name:           python-requirements-parser
Version:        0.5.0
Release:        0
Summary:        Pip requirement file parser
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/davidfischer/requirements-parser
Source:         https://github.com/davidfischer/requirements-parser/archive/v%{version}.tar.gz#/requirements-parser-%{version}.tar.gz
Patch1:         dont-install-readme.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description
A Pip requirement file parser.

%prep
%autosetup -p1 -n requirements-parser-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc AUTHORS.rst README.md
%{python_sitelib}/requirements
%{python_sitelib}/requirements_parser-%{version}.dist-info

%changelog
