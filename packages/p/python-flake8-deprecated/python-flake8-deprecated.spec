#
# spec file for package python-flake8-deprecated
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
Name:           python-flake8-deprecated
Version:        2.2.1
Release:        0
Summary:        Flake8 deprecations plugin
License:        GPL-2.0-only
Group:          Development/Languages/Python
URL:            https://github.com/gforcada/flake8-deprecated
Source:         https://files.pythonhosted.org/packages/source/f/flake8-deprecated/flake8_deprecated-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-flake8 >= 5.0.4
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module flake8 >= 5.0.4}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
This flake8 plugin helps you keeping up with method deprecations and giving hints about what
they should be replaced with.

%prep
%setup -q -n flake8_deprecated-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest run_tests.py

%files %{python_files}
%license LICENSE
%doc CHANGES.rst README.rst
%{python_sitelib}/flake8_deprecated.py
%pycache_only %{python_sitelib}/__pycache__/*
%{python_sitelib}/flake8_deprecated-%{version}.dist-info

%changelog
