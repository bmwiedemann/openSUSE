#
# spec file for package python-crayons
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
Name:           python-crayons
Version:        0.2.0 
Release:        0
Summary:        Colored strings for terminal usage
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/kennethreitz/httpbin
Source:         https://files.pythonhosted.org/packages/source/c/crayons/crayons-%{version}.tar.gz
Source1:        LICENSE
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
Requires:       python-colorama
BuildArch:      noarch
%python_subpackages

%description

%prep
%setup -q -n crayons-%{version}
cp %{SOURCE1} .

%build
%python_build

%install
%python_install

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
