#
# spec file for package python-desktop-entry-lib
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
Name:           python-desktop-entry-lib
Version:        5.0
Release:        0
Summary:        A library for working with .desktop files
License:        BSD-2-Clause
URL:            https://pypi.org/project/desktop-entry-lib
Source:         https://files.pythonhosted.org/packages/source/d/desktop_entry_lib/desktop_entry_lib-%{version}.tar.gz
# PATCH-FIX-UPSTREAM https://codeberg.org/JakobDev/desktop-entry-lib/pulls/19
Patch0:         support-pytest-9.patch
BuildRequires:  %{python_module jeepney}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pyfakefs}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest-subtests if %python-pytest < 9}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildArch:      noarch

%python_subpackages

%description
desktop-entry-lib allows reading and writing .desktop files according to the
Desktop Entry Specification.

%prep
%autosetup -p1 -n desktop_entry_lib-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Exclude tests that require data files not included in the release
%pytest tests --ignore=tests/test_data.py --ignore=tests/test_collection.py

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/desktop_entry_lib
%{python_sitelib}/desktop_entry_lib-%{version}.dist-info

%changelog
