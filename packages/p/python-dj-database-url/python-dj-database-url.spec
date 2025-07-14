#
# spec file for package python-dj-database-url
#
# Copyright (c) 2025 SUSE LLC
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
Name:           python-dj-database-url
Version:        3.0.1
Release:        0
Summary:        Utility to use database URLs in Django applications
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/jazzband/dj-database-url
Source:         https://files.pythonhosted.org/packages/source/d/dj-database-url/dj_database_url-%{version}.tar.gz
BuildRequires:  %{python_module Django > 4.2}
BuildRequires:  %{python_module devel >= 3.9}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django > 4.2
BuildArch:      noarch
%python_subpackages

%description
This Django utility allows you to utilize the 12factor inspired
DATABASE_URL environment variable to configure Django applications.

The `dj_database_url.config` method returns a Django database connection
dictionary, populated with all the data specified in your URL. There is
also a `conn_max_age` argument to easily enable Django's connection pool.

If you'd rather not use an environment variable, you can pass a URL in directly
instead to ``dj_database_url.parse``.

Supported Databases
-------------------

Support currently exists for PostgreSQL, PostGIS, MySQL, MySQL (GIS),
Oracle, Oracle (GIS), and SQLite.

%prep
%setup -q -n dj_database_url-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/dj_database_url
%{python_sitelib}/dj_database_url-%{version}.dist-info

%changelog
