#
# spec file for package python-funcy
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
Name:           python-funcy
Version:        2.0
Release:        0
Summary:        Functional tools for Python
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/Suor/funcy
Source:         https://files.pythonhosted.org/packages/source/f/funcy/funcy-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module whatever}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
A collection of functional tools focused on practicality.

Inspired by clojure, underscore and the author's own abstractions.

%prep
%setup -q -n funcy-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
rm -r tests/__pycache__
%pytest

%files %{python_files}
%doc CHANGELOG README.rst
%license LICENSE
%{python_sitelib}/funcy
%{python_sitelib}/funcy-%{version}.dist-info

%changelog
