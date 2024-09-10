#
# spec file for package python-python-mimeparse
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


%{?sle15_python_module_pythons}
Name:           python-python-mimeparse
Version:        2.0.0
Release:        0
Summary:        Basic functions for parsing and matching mime-type names
License:        MIT
URL:            https://github.com/dbtsai/python-mimeparse
Source:         https://files.pythonhosted.org/packages/source/p/python-mimeparse/python_mimeparse-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
This module provides basic functions for handling mime-types. It can handle
matching mime-types against a list of media-ranges. See section 14.1 of
the HTTP specification [RFC 2616] for a complete explanation.

%prep
%autosetup -p1 -n python_mimeparse-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec mimeparse_test.py

%files %{python_files}
%license LICENSE
%doc README.rst
%pycache_only %{python_sitelib}/__pycache__
%{python_sitelib}/mimeparse.py*
%{python_sitelib}/python_mimeparse-%{version}.dist-info

%changelog
