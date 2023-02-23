#
# spec file for package python-sqlalchemy-migrate
#
# Copyright (c) 2023 SUSE LLC
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
Name:           python-sqlalchemy-migrate
Version:        0.13.0
Release:        0
Summary:        Database schema migration for SQLAlchemy
License:        MIT
Group:          Development/Libraries/Python
URL:            https://pypi.python.org/pypi/sqlalchemy-migrate
Source:         https://files.pythonhosted.org/packages/source/s/sqlalchemy-migrate/sqlalchemy-migrate-%{version}.tar.gz
Patch0:         support-sphinx-4.patch
# Test requirements:
#BuildRequires:  python-ScriptTest >= 1.0
BuildRequires:  %{python_module Tempita >= 0.4}
BuildRequires:  %{python_module decorator}
BuildRequires:  %{python_module pbr}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# Documentation requirements:
BuildRequires:  python3-SQLAlchemy >= 0.9.6
BuildRequires:  python3-Sphinx
Requires:       python-SQLAlchemy >= 0.7.8
Requires:       python-Tempita >= 0.4
Requires:       python-decorator
Requires:       python-six >= 1.7.0
Requires:       python-sqlparse
Requires(post): update-alternatives
Requires(preun):update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Inspired by Ruby on Rails' migrations, Migrate provides a way to deal with
database schema changes in SQLAlchemy projects.

Migrate extends SQLAlchemy to have database changeset handling. It provides a
database change repository mechanism which can be used from the command line as
well as from inside python code.

%package -n python-sqlalchemy-migrate-doc
Summary:        Documentation for %{name}
Group:          Documentation/Other
Provides:       %{python_module sqlalchemy-migrate-doc = %{version}}

%description -n python-sqlalchemy-migrate-doc
Inspired by Ruby on Rails' migrations, Migrate provides a way to deal with
database schema changes in SQLAlchemy projects.

Migrate extends SQLAlchemy to have database changeset handling. It provides a
database change repository mechanism which can be used from the command line as
well as from inside python code.

This package contains the documentation.

%prep
%setup -q -n sqlalchemy-migrate-%{version}
%autopatch -p1
find . -type f -name "*.py" -o -name "*.py_tmpl" | xargs sed -i "/#!/d" # Remove shebang from non-executable scripts
sed -i "s/, 'sphinxcontrib.issuetracker'//g" doc/source/conf.py # No internet access please

%build
%python_build
sphinx-build -b html doc/source doc/build/html && rm doc/build/html/.buildinfo && rm -r doc/build/html/.doctrees # Build HTML documentation

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/migrate
%python_clone -a %{buildroot}%{_bindir}/migrate-repository
%python_expand %fdupes %{buildroot}%{$python_sitelib}

#NOTE(saschpe): enable tests later, there are one or two upstream issues
#%%check
#python setup.py test

%post
%python_install_alternative migrate
%python_install_alternative migrate-repository

%postun
%python_uninstall_alternative migrate
%python_uninstall_alternative migrate-repository

%files %{python_files}
%license COPYING
%doc README.rst
%python_alternative %{_bindir}/migrate
%python_alternative %{_bindir}/migrate-repository
%{python_sitelib}/migrate
%{python_sitelib}/sqlalchemy_migrate-*

%files -n python-sqlalchemy-migrate-doc
%license COPYING
%doc doc/build/html

%changelog
