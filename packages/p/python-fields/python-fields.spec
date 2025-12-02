#
# spec file for package python-fields
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
Name:           python-fields
Version:        5.0.0
Release:        0
Summary:        Container class boilerplate killer
License:        BSD-2-Clause
URL:            https://github.com/ionelmc/python-fields
Source:         https://files.pythonhosted.org/packages/source/f/fields/fields-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Container class boilerplate killer.
Features:
  * Human-readable ``__repr__``
  * Complete set of comparison methods
  * Keyword and positional argument support. Works like a normal class - you can override just about anything in the
    subclass (eg: a custom ``__init__``). In contrast, `hynek/characteristic <https://github.com/hynek/characteristic>`_
    forces different call schematics and calls your ``__init__`` with different arguments.

%prep
%setup -q -n fields-%{version}
# do not do benchmark tests, in virtual they don't make much sense and we
# avoid cycle with pytest-benchmark
sed -i -e '/--benchmark-disable/d' setup.cfg
# do not run doctests, needless dependencies pulled in that way
sed -i -e '/doctest/d' setup.cfg
sed -i -e 's/\[pytest\]/\[tools:pytest\]/g' setup.cfg
rm tests/test_perf.py
# only required for python 2 support, breaks with pytest 9
rm conftest.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc AUTHORS.rst CHANGELOG.rst README.rst
%{python_sitelib}/fields
%{python_sitelib}/fields-%{version}.dist-info

%changelog
