#
# spec file for package python-itypes
#
# Copyright (c) 2023 SUSE LLC
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
Name:           python-itypes
Version:        1.2.0
Release:        0
Summary:        Basic immutable container types for Python
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/tomchristie/itypes
Source:         itypes-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Basic immutable container types for Python.

A simple implementation that's designed for simplicity over performance.

Use these in circumstances where it may result in more comprehensible code, or
when you want to create custom types with restricted, immutable interfaces.

%prep
%autosetup -p1 -n itypes-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest tests.py

%files %{python_files}
%license LICENSE.md
%{python_sitelib}/itypes.py*
%{python_sitelib}/itypes-%{version}-py*.egg-info
%pycache_only %{python_sitelib}/__pycache__

%changelog
