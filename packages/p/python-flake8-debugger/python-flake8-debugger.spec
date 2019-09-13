#
# spec file for package python-flake8-debugger
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
Name:           python-flake8-debugger
Version:        3.1.0
Release:        0
Summary:        ipdb/pdb statement checker plugin for flake8
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/jbkahn/flake8-debugger
Source:         https://files.pythonhosted.org/packages/source/f/flake8-debugger/flake8-debugger-%{version}.tar.gz
Source1:        LICENSE
BuildRequires:  %{python_module pytest-runner}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module flake8 >= 1.5}
BuildRequires:  %{python_module pycodestyle}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
BuildArch:      noarch

%python_subpackages

%description
ipdb/pdb statement checker plugin for flake8

%prep
%setup -q -n flake8-debugger-%{version}
cp %{SOURCE1} LICENSE

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
