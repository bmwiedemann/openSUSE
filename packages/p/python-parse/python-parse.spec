#
# spec file for package python-parse
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
Name:           python-parse
Version:        1.15.0
Release:        0
Summary:        Python module for parsing strings using a "format" syntax
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/r1chardj0n3s/parse
Source0:        https://files.pythonhosted.org/packages/source/p/parse/parse-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Parse strings using a specification based on the Python format() syntax.

%prep
%setup -q -n parse-%{version}
chmod a-x README.rst

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec -m unittest discover -v

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
