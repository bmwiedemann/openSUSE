#
# spec file for package python-hanzidentifier
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%{?sle15_python_module_pythons}
Name:           python-hanzidentifier
Version:        1.1.0
Release:        0
License:        MIT
Summary:        Python module that identifies Chinese text as Simplified or Traditional
URL:            https://github.com/tsroten/hanzidentifier
Group:          Development/Languages/Python
Source:         https://github.com/tsroten/hanzidentifier/archive/v%{version}.tar.gz#/hanzidentifier-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module zhon >= 1.1.3}
# /SECTION
BuildRequires:  fdupes
Requires:       python-zhon >= 1.1.3
BuildArch:      noarch

%python_subpackages

%description
Python module that identifies Chinese text as Simplified or Traditional.

%prep
%setup -q -n hanzidentifier-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest discover -v

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/*

%changelog
