#
# spec file for package python-robotframework-pythonlibcore
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

%{?sle15_python_module_pythons}
Name:           python-robotframework-pythonlibcore
Version:        4.4.1
Release:        0
Summary:        Tools to ease creating larger test libraries for Robot Framework using Python
License:        Apache-2.0
URL:            https://github.com/robotframework/PythonLibCore
Source:         https://files.pythonhosted.org/packages/source/r/robotframework-pythonlibcore/robotframework-pythonlibcore-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description
Tools to ease creating larger test libraries for Robot Framework using Python.

%prep
%autosetup -p1 -n robotframework-pythonlibcore-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.md
%license LICENSE.txt
%pycache_only %{python_sitelib}/__pycache__
%{python_sitelib}/__pycache__/*
%{python_sitelib}/robotlibcore.py
%{python_sitelib}/robotframework_pythonlibcore-%{version}.dist-info

%changelog
