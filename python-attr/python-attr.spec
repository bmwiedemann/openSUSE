#
# spec file for package python-attr
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-attr
Version:        0.3.1
Release:        0
Summary:        Python module for setting attributes of target functions or classes
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/denis-ryzhkov/attr
Source:         https://files.pythonhosted.org/packages/source/a/attr/attr-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch

%python_subpackages

%description
A decorator to set attributes of target function or class in a DRY way.

%prep
%setup -q -n attr-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check 
%python_exec dry_attr.py

%files %{python_files}
%doc README.md
%{python_sitelib}/*

%changelog
