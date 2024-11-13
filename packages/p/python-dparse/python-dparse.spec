#
# spec file for package python-dparse
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


%bcond_without  test
Name:           python-dparse
Version:        0.6.4
Release:        0
Summary:        Python dependency file parser
License:        MIT
URL:            https://github.com/jayfk/dparse
Source:         https://files.pythonhosted.org/packages/source/d/dparse/dparse-%{version}.tar.gz
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML
Requires:       python-packaging
Requires:       (python-tomli if python-base < 3.11)
Recommends:     python-pipenv
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pytest}
%endif
%python_subpackages

%description
A parser for Python dependency files.

%prep
%autosetup -p1 -n dparse-%{version}
# Note vendor/toml.py could be unvendored

%build
%pyproject_wheel

%install
%pyproject_install
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
%{python_sitelib}/dparse
%{python_sitelib}/dparse-%{version}.dist-info

%changelog
