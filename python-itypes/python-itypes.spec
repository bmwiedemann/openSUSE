#
# spec file for package python-itypes
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
Name:           python-itypes
Version:        1.1.0
Release:        0
Summary:        Basic immutable container types for Python
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/tomchristie/itypes
Source:         https://files.pythonhosted.org/packages/source/i/itypes/itypes-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/tomchristie/itypes/master/LICENSE.md
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
%setup -q -n itypes-%{version}
cp %{SOURCE1} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE.md
%{python_sitelib}/itypes.py*
%{python_sitelib}/itypes-%{version}-py*.egg-info
%pycache_only %{python_sitelib}/__pycache__

%changelog
