#
# spec file for package python-fire
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


%{?sle15_python_module_pythons}
Name:           python-fire
Version:        0.7.1
Release:        0
Summary:        A library for automatically generating command line interfaces
License:        Apache-2.0
URL:            https://github.com/google/python-fire
Source:         https://files.pythonhosted.org/packages/source/f/fire/fire-%{version}.tar.gz
# PATCH-FIX-UPSTREAM gh#google/python-fire#623
Patch0:         support-python-314.patch
# Based on https://github.com/google/python-fire/pull/265/files
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-termcolor
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Levenshtein}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module termcolor}
# /SECTION
%python_subpackages

%description
Python Fire is a library for automatically generating command line
interfaces (CLIs) from a Python object.

%prep
%autosetup -p1 -n fire-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/fire
%{python_sitelib}/fire-%{version}.dist-info

%changelog
