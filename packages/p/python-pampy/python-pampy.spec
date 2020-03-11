#
# spec file for package python-pampy
#
# Copyright (c) 2020 SUSE LLC
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


%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pampy
Version:        0.3.0
Release:        0
Summary:        An alternate pattern matching for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/santinic/pampy
Source:         https://files.pythonhosted.org/packages/source/p/pampy/pampy-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/santinic/pampy/master/LICENSE
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
For patterns, a developer can use any Python type, any class, or any Python value.

The operator `_` and built-in types like `int` or `str`, extract
variables that are passed to functions.

Types and Classes are matched via `instanceof(value, pattern)`.

`Iterable` Patterns match recursively through all their elements.  The
same goes for dictionaries.

%prep
%setup -q -n pampy-%{version}
cp %{SOURCE1} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_expand rm -rf %{buildroot}%{$python_sitelib}/tests

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python -m unittest discover -s tests

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
