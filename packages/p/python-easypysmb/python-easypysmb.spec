#
# spec file for package python-easypysmb
#
# Copyright (c) 2020 SUSE LLC
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
Name:           python-easypysmb
Version:        1.4.4
Release:        0
Summary:        PySMB wrapper library
License:        GPL-3.0-only
Group:          Development/Languages/Python
URL:            https://github.com/pschmitt/easypysmb
Source:         https://files.pythonhosted.org/packages/source/e/easypysmb/easypysmb-%{version}.tar.gz
Source99:       https://raw.githubusercontent.com/pschmitt/easypysmb/master/LICENSE
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pysmb
BuildArch:      noarch

%python_subpackages

%description
easypysmb is a Python library that wraps around the pysmb library.

%prep
%setup -q -n easypysmb-%{version}
cp %{S:99} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
