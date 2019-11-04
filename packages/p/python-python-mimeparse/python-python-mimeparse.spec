#
# spec file for package python-python-mimeparse
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
%define oldpython python
Name:           python-python-mimeparse
Version:        1.6.0
Release:        0
Summary:        Basic functions for parsing and matching mime-type names
License:        MIT
URL:            https://github.com/dbtsai/python-mimeparse
Source:         https://files.pythonhosted.org/packages/source/p/python-mimeparse/python-mimeparse-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%ifpython2
Obsoletes:      %{oldpython}-mimeparse < 0.1.4
Provides:       %{oldpython}-mimeparse = %{version}
%endif
%python_subpackages

%description
This module provides basic functions for handling mime-types. It can handle
matching mime-types against a list of media-ranges. See section 14.1 of
the HTTP specification [RFC 2616] for a complete explanation.

%prep
%setup -q -n python-mimeparse-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec mimeparse_test.py

%files %{python_files}
%license LICENSE
%doc README.rst
%pycache_only %{python_sitelib}/__pycache__
%{python_sitelib}/mimeparse.py*
%{python_sitelib}/python_mimeparse-%{version}-py%{python_version}.egg-info

%changelog
