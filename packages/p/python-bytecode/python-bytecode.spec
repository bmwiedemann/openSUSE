#
# spec file for package python-bytecode
#
# Copyright (c) 2022 SUSE LLC
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
%define skip_python2 1
Name:           python-bytecode
Version:        0.14.0
Release:        0
Summary:        Python module to generate and modify bytecode
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/vstinner/bytecode
Source:         https://files.pythonhosted.org/packages/source/b/bytecode/bytecode-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module typing_extensions}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-aenum >= 2.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module aenum}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Python module to generate and modify bytecode

%prep
%setup -q -n bytecode-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license COPYING
%{python_sitelib}/*

%changelog
