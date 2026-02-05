#
# spec file for package python-pyproject-examples
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Name:           python-pyproject-examples
Version:        2023.6.30
Release:        0
Summary:        Example pyproject.toml configs for testing
License:        MIT
URL:            https://github.com/repo-helper/pyproject-examples
Source:         https://files.pythonhosted.org/packages/source/p/pyproject-examples/pyproject_examples-%{version}.tar.gz
# PATCH-FIX-UPSTREAM fix_regex.patch -- based on PR
Patch0:         fix_regex.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module whey}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-coincidence >= 0.4.0
Requires:       python-dom-toml >= 0.4.0
Requires:       python-packaging >= 21.3
Requires:       python-pytest >= 6.2.3
BuildArch:      noarch
%python_subpackages

%description
Example pyproject.toml configs for testing.

%prep
%autosetup -p1 -n pyproject_examples-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# No testsuite
exit 0

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/pyproject_examples
%{python_sitelib}/pyproject_examples-%{version}.dist-info

%changelog
