#
# spec file for package python-parse
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


Name:           python-parse
Version:        1.20.2
Release:        0
Summary:        Python module for parsing strings using a "format" syntax
License:        MIT
URL:            https://github.com/r1chardj0n3s/parse
Source0:        https://files.pythonhosted.org/packages/source/p/parse/parse-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
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
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/parse.py
%pycache_only %{python_sitelib}/__pycache__/parse.*
%{python_sitelib}/parse-%{version}.dist-info

%changelog
