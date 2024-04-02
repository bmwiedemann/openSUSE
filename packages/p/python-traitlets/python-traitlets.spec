#
# spec file for package python-traitlets
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
Name:           python-traitlets
Version:        5.14.2
Release:        0
Summary:        Traitlets Python configuration system
License:        BSD-3-Clause
URL:            https://github.com/ipython/traitlets
Source:         https://files.pythonhosted.org/packages/source/t/traitlets/traitlets-%{version}.tar.gz
Source99:       python-traitlets.rpmlintrc
BuildRequires:  %{python_module argcomplete >= 3.0.3}
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module hatchling >= 1.5}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest >= 7 with %python-pytest < 8.1}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
A configuration system for Python applications.

%prep
%autosetup -p1 -n traitlets-%{version}
sed -i 's/"--color=yes",//' pyproject.toml

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# no mypy testing in Ring1
%pytest --ignore tests/test_typing.py

%files %{python_files}
%doc README.md
%doc examples/
%license LICENSE
%{python_sitelib}/traitlets/
%{python_sitelib}/traitlets-%{version}*-info

%changelog
