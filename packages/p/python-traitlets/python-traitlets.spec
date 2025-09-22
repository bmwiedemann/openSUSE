#
# spec file for package python-traitlets
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
Name:           python-traitlets
Version:        5.14.3
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
BuildRequires:  %{python_module pytest >= 7}
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
# skip test_complete_custom_completers because of gh#ipython/traitlets#911
# test_complete_simple_app and test_complete_subcommands_subapp1 fail with Python 3.14 https://github.com/pytest-dev/pytest-cov/issues/719
%pytest --ignore tests/test_typing.py -k 'not (test_complete_custom_completers or test_complete_simple_app or test_complete_subcommands_subapp1)'

%files %{python_files}
%doc README.md
%doc examples/
%license LICENSE
%{python_sitelib}/traitlets/
%{python_sitelib}/traitlets-%{version}.dist-info

%changelog
