#
# spec file for package python-chest
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


Name:           python-chest
Version:        0.2.3
Release:        0
Summary:        Spill-to-disk dictionary for Python
License:        BSD-3-Clause
URL:            https://github.com/ContinuumIO/chest
Source:         https://files.pythonhosted.org/packages/source/c/chest/chest-%{version}.tar.gz
Patch0:         support-python-310.patch
BuildRequires:  %{python_module HeapDict}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-HeapDict
BuildArch:      noarch
%python_subpackages

%description
A dictionary that spills to disk.
Chest acts like a dictionary, but it can write its contents to disk.
This is useful in the following two occasions:
1. Chest can hold datasets that are larger than memory
2. Chest persists and so can be saved and loaded for later use

%prep
%autosetup -p1 -n chest-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%{python_sitelib}/chest
%{python_sitelib}/chest-%{version}.dist-info

%changelog
