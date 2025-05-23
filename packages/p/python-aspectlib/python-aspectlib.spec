#
# spec file for package python-aspectlib
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


%bcond_without python2
%{?sle15_python_module_pythons}
Name:           python-aspectlib
Version:        2.0.0
Release:        0
Summary:        Aspect-oriented programming
License:        BSD-2-Clause
URL:            https://github.com/ionelmc/python-aspectlib
Source:         https://files.pythonhosted.org/packages/source/a/aspectlib/aspectlib-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-fields
BuildArch:      noarch
BuildRequires:  %{python_module fields}
BuildRequires:  %{python_module process-tests}
BuildRequires:  %{python_module pytest}
%if %{with python2}
BuildRequires:  python-mock
BuildRequires:  python-trollius
%endif
%ifpython2
Requires:       python-trollius
%endif
%python_subpackages

%description
Aspectlib is an aspect-oriented programming, monkey-patch and
decorators library. It is useful when changing behavior in
existing code is desired. It includes tools for debugging and
testing: simple mock/record and a complete capture/replay
framework.

%prep
%autosetup -p1 -n aspectlib-%{version}

# both tests not working (the first skipped by design, the second needed old tornado)
# don't pull in tornado when not needed
rm tests/test_integrations.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# ignore deprecation warnings because of signature of throw() is deprecated
%pytest --ignore=src -W ignore::DeprecationWarning

%files %{python_files}
%license LICENSE
%doc AUTHORS.rst CHANGELOG.rst README.rst
%{python_sitelib}/aspectlib
%{python_sitelib}/aspectlib-%{version}*-info

%changelog
