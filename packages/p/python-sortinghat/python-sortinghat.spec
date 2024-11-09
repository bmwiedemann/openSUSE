#
# spec file for package python-sortinghat
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


Name:           python-sortinghat
Version:        1.5.0
Release:        0
Summary:        A tool to manage identities
License:        GPL-3.0-only
URL:            https://github.com/grimoirelab/sortinghat
Source:         https://github.com/chaoss/grimoirelab-sortinghat/archive/refs/tags/%{version}.tar.gz#/sortinghat-%{version}.tar.gz
# PATCH-FIX-OPENSUSE Allow overridding the database config
Patch0:         allow-database-config-overrides.patch
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 4.2
Requires:       python-Jinja2 >= 3.1
Requires:       python-PyJWT
Requires:       python-PyMySQL >= 0.7.0
Requires:       python-PyYAML >= 3.12
Requires:       python-SQLAlchemy >= 1.2
Requires:       python-click >= 7.1
Requires:       python-django-cors-headers >= 3.7
Requires:       python-django-graphql-jwt >= 0.3
Requires:       python-django-rq >= 2.3
Requires:       python-django-treebeard >= 4.5
Requires:       python-graphene >= 2.1.5
Requires:       python-graphene-django
Requires:       python-grimoirelab-toolkit >= 0.3
Requires:       python-importlib-resources
Requires:       python-mysqlclient >= 2.0
Requires:       python-numpy
Requires:       python-pandas >= 1.3
Requires:       python-python-dateutil >= 2.8.0
Requires:       python-requests >= 2.7
Requires:       python-rq
Requires:       python-setuptools
Requires:       python-sgqlc
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Jinja2 >= 3.1}
BuildRequires:  %{python_module Django >= 4.2}
BuildRequires:  %{python_module PyMySQL >= 0.7.0}
BuildRequires:  %{python_module PyYAML >= 3.12}
BuildRequires:  %{python_module SQLAlchemy >= 1.2}
BuildRequires:  %{python_module click >= 7.1}
BuildRequires:  %{python_module django-cors-headers >= 3.7}
BuildRequires:  %{python_module django-graphql-jwt >= 0.3}
BuildRequires:  %{python_module django-rq >= 2.3}
BuildRequires:  %{python_module django-treebeard >= 4.5}
BuildRequires:  %{python_module fakeredis}
BuildRequires:  %{python_module graphene >= 2.1.5}
BuildRequires:  %{python_module grimoirelab-toolkit >= 0.3}
BuildRequires:  %{python_module httpretty >= 0.9.5}
BuildRequires:  %{python_module importlib-resources}
BuildRequires:  %{python_module mysqlclient >= 2.0}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pandas >= 1.3}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil >= 2.8.0}
BuildRequires:  %{python_module requests >= 2.7}
BuildRequires:  %{python_module rq}
BuildRequires:  %{python_module sgqlc}
BuildRequires:  mariadb-rpm-macros
# /SECTION
%python_subpackages

%description
A tool to manage identities.

Sorting Hat maintains an SQL database with identities coming
(potentially) from different sources. Identities corresponding to the
same real person can be merged in the same unique identity, with a
unique uuid. For each unique identity, a profile can be defined, with
the name and other data to show for the corresponding person by default.

In addition, each unique identity can be related to one or more
affiliations, for different time periods. This will usually correspond
to different organizations in which the person was employed during those
time periods.

Sorting Hat is a part of the GrimoireLab
toolset <https://grimoirelab.github.io>, which provides for Python
modules and scripts to analyze data sources with information about
software development, and allows to produce interactive dashboards to
visualize that information.

In the context of GrimoireLab, Sorting Hat is usually run after data is
retrieved with Perceval <https://github.com/grimmoirelab/perceval>,
to store the identities obtained into its database, and later merge them
into unique identities (and maybe affiliate them).

%prep
%autosetup -p1 -n grimoirelab-sortinghat-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/sortinghat
%python_clone -a %{buildroot}%{_bindir}/sortinghat-admin
%python_clone -a %{buildroot}%{_bindir}/sortinghatw
%python_clone -a %{buildroot}%{_bindir}/sortinghatd
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
exit_code=0
user='auth_db_user'
pass='auth_db_pass'
port=63306
run_dir=/tmp/mysql
#
# start the mariadb server
#
%mysql_testserver_start -u $user -p $pass -t $port
#
# running the test
#
export TEST_SORTINGHAT_DB_PORT=$port
export TEST_SORTINGHAT_DB_USER=$user
export TEST_SORTINGHAT_DB_PASSWORD=$pass
# Broken tests
rm tests/test_jobs.py
%python_exec manage.py test --settings=config.settings.config_testing
%python_exec manage.py test --settings=config.settings.config_testing_tenant
#
# stopping mariadb
#
%mysql_testserver_stop
exit $exit_code

%post
%python_install_alternative sortinghat sortinghat-admin sortinghatw sortinghatd

%postun
%python_uninstall_alternative sortinghat sortinghat-admin sortinghatw sortinghatd

%files %{python_files}
%doc NEWS README.md
%python_alternative %{_bindir}/sortinghat
%python_alternative %{_bindir}/sortinghatw
%python_alternative %{_bindir}/sortinghatd
%python_alternative %{_bindir}/sortinghat-admin
%{python_sitelib}/sortinghat
%{python_sitelib}/sortinghat-%{version}.dist-info

%changelog
