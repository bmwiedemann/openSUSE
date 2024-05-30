#
# spec file for package python-parsy
#
# Copyright (c) 2024 SUSE LLC
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


Name:           python-parsy
Version:        2.1
Release:        0
Summary:        Python parser combinators
License:        MIT
URL:            https://github.com/python-parsy/parsy
Source:         https://files.pythonhosted.org/packages/source/p/parsy/parsy-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Easy-to-use parser combinators, for parsing in pure Python.

%prep
%setup -q -n parsy-%{version}
touch tests/__init__.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest -v

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/parsy
%{python_sitelib}/parsy-%{version}*-info

%changelog
