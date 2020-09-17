#
# spec file for package python-dparse
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%bcond_without  test
%define skip_python2 1
Name:           python-dparse
Version:        0.5.1
Release:        0
Summary:        Python dependency file parser
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/jayfk/dparse
Source:         https://files.pythonhosted.org/packages/source/d/dparse/dparse-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML
Requires:       python-packaging
Recommends:     python-pipenv
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module toml}
%endif
%python_subpackages

%description
A parser for Python dependency files.

%prep
%setup -q -n dparse-%{version}
# Note vendor/toml.py could be unvendored

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with test}
%check
# There is a bug in the pipenv support, related to writing a new toml file.
# Both dparse and pipenv have a vendored copy of different toml libraries.
# and even more, we do not have pipenv in our distribution
%pytest --deselect 'tests/test_updater.py::test_update_pipfile'
%endif

%files %{python_files}
%license LICENSE
%doc README.rst HISTORY.rst
%{python_sitelib}/*

%changelog
