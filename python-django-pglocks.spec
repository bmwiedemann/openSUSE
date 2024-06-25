#
# spec file for package python-django-pglocks
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
Name:           python-django-pglocks
Version:        1.0.4
Release:        0
Summary:        PostgreSQL Advisory Locks for Django
License:        MIT
URL:            https://github.com/Xof/django-pglocks
Source:         https://files.pythonhosted.org/packages/source/d/django-pglocks/django-pglocks-%{version}.tar.gz
BuildRequires:  %{python_module Django}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module psycopg2}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django
Requires:       python-psycopg2
Requires:       python-six
BuildArch:      noarch
%python_subpackages

%description
django-pglocks provides a useful context manager to manage PostgreSQL advisory
locks. It requires Django (tested with 1.5), PostgreSQL, and (probably) psycopg2.

Advisory locks are application-level locks that are acquired and released purely
by the client of the database; PostgreSQL never acquires them on its own. They
are very useful as a way of signalling to other sessions that a higher-level
resource than a single row is in use, without having to lock an entire table or
some other structure.

It's entirely up to the application to correctly acquire the right lock.

Advisory locks are either session locks or transaction locks. A session lock is
held until the database session disconnects (or is reset); a transaction lock is
held until the transaction terminates.

Currently, the context manager only creates session locks, as the behavior of a
lock persisting after the context body has been exited is surprising, and
there's no way of releasing a transaction-scope advisory lock except to exit
the transaction.

%prep
%setup -q -n django-pglocks-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# Here could be unittests, but we don't want to spool up a PostgreSQL server
# at this point.

%files %{python_files}
%doc CHANGES.txt
%license LICENSE.txt
%{python_sitelib}/django_pglocks
%{python_sitelib}/django_pglocks-%{version}.dist-info

%changelog
