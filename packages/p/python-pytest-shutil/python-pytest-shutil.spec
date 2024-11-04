#
# spec file for package python-pytest-shutil
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
Name:           python-pytest-shutil
Version:        1.8.0
Release:        0
Summary:        A goodie-bag of unix shell and environment tools for pytest
License:        MIT
URL:            https://github.com/man-group/pytest-plugins
Source:         https://files.pythonhosted.org/packages/source/p/pytest-shutil/pytest-shutil-%{version}.tar.gz
BuildRequires:  %{python_module execnet}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module termcolor}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-execnet
Requires:       python-pytest
Requires:       python-six
Requires:       python-termcolor
BuildArch:      noarch

%python_subpackages

%description
This library is a goodie-bag of Unix shell and environment management
tools for automated tests.

%prep
%autosetup -p2 -n pytest-shutil-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Disable test_pretty_formatter test that fails in osc build but it works when
# run manually. It should be something related to the shell and termcolor
%pytest -k "not test_pretty_formatter"

%files %{python_files}
%doc README.md CHANGES.md
%license LICENSE
%{python_sitelib}/pytest_shutil
%{python_sitelib}/pytest_shutil-%{version}.dist-info

%changelog
