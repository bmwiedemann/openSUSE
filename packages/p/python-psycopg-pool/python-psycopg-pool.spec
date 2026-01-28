#
# spec file for package python-psycopg-pool
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Name:           python-psycopg-pool
Version:        3.3.0
Release:        0
Summary:        Connection Pool for Psycopg
License:        LGPL-3.0-only
URL:            https://psycopg.org/psycopg3/
Source:         https://files.pythonhosted.org/packages/source/p/psycopg-pool/psycopg_pool-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 49.2.0}
BuildRequires:  %{python_module wheel >= 0.37}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-typing-extensions >= 4.6
BuildArch:      noarch
%python_subpackages

%description
Connection Pool for Psycopg

%prep
%autosetup -p1 -n psycopg_pool-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# Tested in python-psycopg

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/psycopg_pool
%{python_sitelib}/psycopg_pool-%{version}.dist-info

%changelog
