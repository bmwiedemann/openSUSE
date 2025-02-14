#
# spec file for package python-pycomposefile
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
Name:           python-pycomposefile
Version:        0.0.32
Release:        0
Summary:        Structured deserialization of Docker Compose files
License:        MIT
URL:            https://github.com/smurawski/pycomposefile
Source:         https://files.pythonhosted.org/packages/source/p/pycomposefile/pycomposefile-%{version}.tar.gz
# PATCH-FIX-UPSTREAM p_fix-version-number.patch
# https://github.com/smurawski/pycomposefile/issues/29
Patch:          p_fix-version-number.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module PyYAML}
# /SECTION
BuildRequires:  fdupes
Requires:       python-PyYAML
BuildArch:      noarch
%python_subpackages

%description
Structured deserialization of Docker Compose files.

%prep
%autosetup -p1 -n pycomposefile-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# Tests currently fail due to missing files in PyPi tarball
# see: https://github.com/smurawski/pycomposefile/issues/28
#%%check
#%%pyunittest -v

%files %{python_files}
%doc README.md
%exclude %{python_sitelib}/tests
%{python_sitelib}/pycomposefile
%{python_sitelib}/pycomposefile-%{version}.dist-info

%changelog
