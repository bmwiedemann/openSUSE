#
# spec file for package python-storm
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define skip_python3 1

%define modname storm
%{?!python_module:%define python_module() python-%{**} python3-%{**}}

Name:           python-%{modname}
Version:        0.20
Release:        0
Summary:        An object-relational mapper (ORM) for Python
License:        LGPL-2.0-or-later
Group:          Development/Languages/Python
URL:            https://storm.canonical.com
Source:         https://files.pythonhosted.org/packages/source/s/storm/storm-%{version}.tar.gz
Patch:          storm-0.20-remove-ez_setup.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-%{modname}-backend = %{version}
%python_subpackages

%description
Storm is an object-relational mapper (ORM) for Python developed at
Canonical. The project has been in development for more than a year
for use in Canonical projects such as [WWW] Launchpad, and has
recently been released as an open-source product.

Highlights:

 * Clean and lightweight API offers a short learning curve and
   long-term maintainability.
 * Storm is developed in a test-driven manner. An untested line of
   code is considered a bug.
 * Storm needs no special class constructors, nor imperative base
   classes.
 * Storm is well designed (different classes have very clear
   boundaries, with small and clean public APIs).
 * Designed from day one to work both with thin relational databases,
   such as SQLite, and big iron systems like PostgreSQL and MySQL.
 * Storm is easy to debug, since its code is written with a KISS
   principle, and thus is easy to understand.
 * Designed from day one to work both at the low end, with trivial
   small databases, and the high end, with applications accessing
   billion row tables and committing to multiple database backends.
 * It's very easy to write and support backends for Storm (current
   backends have around 100 lines of code).

%package django
Summary:        Django support for the Storm ORM
Group:          Development/Languages/Python
Requires:       %{name} = %{version}
Requires:       python-django
Provides:       %{python_module %{modname}-backend = %{version}}
Provides:       %{python_module django = %{version}}

%description django
The python-storm-django package contains the Django support for the Storm ORM.

%package mysql
Summary:        MySQL backend for the Storm ORM
Group:          Development/Languages/Python
Provides:       %{python_module %{modname}-backend = %{version}}
Provides:       %{python_module mysql = %{version}}
Requires:       %{name} = %{version}

%description mysql
This package contains the MySQL database backend for the Storm ORM.

%package postgresql
Summary:        PostgreSQL backend for the Storm ORM
Group:          Development/Languages/Python
Provides:       %{python_module %{modname}-backend = %{version}}
Provides:       %{python_module postgresql = %{version}}
Requires:       %{name} = %{version}
Requires:       python-psycopg2

%description postgresql
The python-storm-postgresql package contains the PostgreSQL database
backend for Storm ORM.

%package twisted
Summary:        Twisted support for the Storm ORM
Group:          Development/Languages/Python
Requires:       %{name} = %{version}
Requires:       python-Twisted
Provides:       %{python_module twisted = %{version}}

%description twisted
This package contains the Django support for the Storm ORM.

%prep
%setup -q -n %{modname}-%{version}
%patch -p1

%build
%python_build

%install
%python_install
%python_expand rm -rfv %{buildroot}%{$python_sitearch}/tests
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%files %{python_files}
%license LICENSE
%doc NEWS README TODO tests/tutorial.txt
%{python_sitearch}/%{modname}*
%exclude %{python_sitearch}/%{modname}/cextensions.c
%exclude %{python_sitearch}/%{modname}/databases/mysql.*
%exclude %{python_sitearch}/%{modname}/databases/postgres.*
%exclude %{python_sitearch}/%{modname}/django
%exclude %{python_sitearch}/%{modname}/twisted

%files %{python_files django}
%{python_sitearch}/%{modname}/django

%files %{python_files mysql}
%{python_sitearch}/%{modname}/databases/mysql.*

%files %{python_files postgresql}
%{python_sitearch}/%{modname}/databases/postgres.*

%files %{python_files twisted}
%{python_sitearch}/%{modname}/twisted

%changelog
