#
# spec file for package python-chest
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-chest
Version:        0.2.3
Release:        0
Summary:        Spill-to-disk dictionary for Python
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/ContinuumIO/chest
Source:         https://files.pythonhosted.org/packages/source/c/chest/chest-%{version}.tar.gz
BuildRequires:  %{python_module HeapDict}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
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
%setup -q -n chest-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%{python_sitelib}/*

%changelog
