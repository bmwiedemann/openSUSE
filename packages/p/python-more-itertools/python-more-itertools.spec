#
# spec file for package python-more-itertools
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


%{?sle15_python_module_pythons}
Name:           python-more-itertools
Version:        10.3.0
Release:        0
Summary:        More routines for operating on iterables, beyond itertools
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/erikrose/more-itertools
Source:         https://files.pythonhosted.org/packages/source/m/more-itertools/more-itertools-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Additional building blocks, recipes, and routines for working with
Python iterables.

%prep
%setup -q -n more-itertools-%{version}
chmod -x more_itertools/more.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest -v

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/more_itertools/
%{python_sitelib}/more_itertools-%{version}*-info/

%changelog
