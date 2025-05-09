#
# spec file for package python-Chameleon
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
Name:           python-Chameleon
Version:        4.6.0
Release:        0
Summary:        Fast HTML/XML Template Compiler
License:        BSD-3-Clause AND BSD-4-Clause AND Python-2.0 AND ZPL-2.1
URL:            https://github.com/malthe/chameleon
Source:         https://github.com/malthe/chameleon/archive/%{version}.tar.gz#/Chameleon-%{version}.tar.gz
BuildRequires:  %{python_module devel >= 3.8}
BuildRequires:  %{python_module importlib-metadata}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %{python_version_nodots} < 310
Requires:       python-importlib-metadata
%endif
BuildArch:      noarch
%python_subpackages

%description
Chameleon is an HTML/XML template engine for Python. It uses the
*page templates* language.

You can use it in any Python web application with just about any
version of Python (2.5 and up, including 3.x and pypy).

%prep
%setup -q -n chameleon-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
# Don't ship testsuite
%python_expand rm -r %{buildroot}%{$python_sitelib}/chameleon/tests
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# doctest have not run at all so far
# AttributeError: '_DocTestSuite' object has no attribute 'test_exc'
%pytest -k 'not doctest'

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%{python_sitelib}/chameleon
%{python_sitelib}/[Cc]hameleon-%{version}.dist-info

%changelog
