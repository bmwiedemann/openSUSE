#
# spec file for package python-redbaron
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           python-redbaron
Version:        0.9.2
Release:        0
Summary:        Python module for writing code that modifies source code
License:        LGPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://github.com/PyCQA/redbaron
Source:         https://files.pythonhosted.org/packages/source/r/redbaron/redbaron-%{version}.tar.gz
Patch0:         pytest4.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-baron >= 0.7
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module baron >= 0.7}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
RedBaron is a Python library and tool to write code that modifies
source code. This includes writing custom refactoring, generic
refactoring, tools, IDE or directly modifying source code in
IPython.

%prep
%setup -q -n redbaron-%{version}
%autopatch -p1

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
rm -r tests/__pycache__
# test_hightlight fails with current python-pygments
%pytest -k "not test_highlight"

%files %{python_files}
%doc CHANGELOG README.md
%{python_sitelib}/redbaron
%{python_sitelib}/redbaron-%{version}*-info

%changelog
