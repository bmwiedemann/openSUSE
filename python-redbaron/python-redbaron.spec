#
# spec file for package python-redbaron
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
Name:           python-redbaron
Version:        0.9.2
Release:        0
Summary:        Python module for writing code that modifies source code
License:        LGPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://github.com/PyCQA/redbaron
Source:         https://files.pythonhosted.org/packages/source/r/redbaron/redbaron-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
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

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
rm -r tests/__pycache__
%pytest

%files %{python_files}
%doc CHANGELOG README.md
%{python_sitelib}/*

%changelog
