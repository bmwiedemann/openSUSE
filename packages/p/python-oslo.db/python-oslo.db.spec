#
# spec file for package python-oslo.db
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


Name:           python-oslo.db
Version:        4.45.0
Release:        0
Summary:        OpenStack oslo.db library
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/oslo.db
Source0:        https://files.pythonhosted.org/packages/source/o/oslo.db/oslo.db-4.45.0.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python-devel
BuildRequires:  python2-PyMySQL
BuildRequires:  python2-alembic >= 0.9.6
BuildRequires:  python2-debtcollector >= 1.2.0
BuildRequires:  python2-eventlet
BuildRequires:  python2-fixtures
BuildRequires:  python2-mock
BuildRequires:  python2-oslo.config >= 5.2.0
BuildRequires:  python2-oslo.context
BuildRequires:  python2-oslo.i18n >= 3.15.3
BuildRequires:  python2-oslo.utils >= 3.33.0
BuildRequires:  python2-oslotest
BuildRequires:  python2-pbr >= 2.0.0
BuildRequires:  python2-psycopg2
BuildRequires:  python2-python-subunit
BuildRequires:  python2-reno
BuildRequires:  python2-six >= 1.10.0
BuildRequires:  python2-sqlalchemy-migrate >= 0.11.0
BuildRequires:  python2-stestr
BuildRequires:  python2-testresources >= 2.0.0
BuildRequires:  python2-testscenarios >= 0.4
BuildRequires:  python2-testtools
BuildRequires:  python3-PyMySQL
BuildRequires:  python3-alembic >= 0.9.6
BuildRequires:  python3-debtcollector >= 1.2.0
BuildRequires:  python3-devel
BuildRequires:  python3-eventlet
BuildRequires:  python3-fixtures
BuildRequires:  python3-mock
BuildRequires:  python3-oslo.config >= 5.2.0
BuildRequires:  python3-oslo.context
BuildRequires:  python3-oslo.i18n >= 3.15.3
BuildRequires:  python3-oslo.utils >= 3.33.0
BuildRequires:  python3-oslotest
BuildRequires:  python3-pbr >= 2.0.0
BuildRequires:  python3-psycopg2
BuildRequires:  python3-python-subunit
BuildRequires:  python3-reno
BuildRequires:  python3-six >= 1.10.0
BuildRequires:  python3-sqlalchemy-migrate >= 0.11.0
BuildRequires:  python3-stestr
BuildRequires:  python3-testresources >= 2.0.0
BuildRequires:  python3-testscenarios >= 0.4
BuildRequires:  python3-testtools
Requires:       python-PyMySQL
Requires:       python-SQLAlchemy >= 1.0.10
Requires:       python-alembic >= 0.9.6
Requires:       python-debtcollector >= 1.2.0
Requires:       python-oslo.config >= 5.2.0
Requires:       python-oslo.context
Requires:       python-oslo.i18n >= 3.15.3
Requires:       python-oslo.utils >= 3.33.0
Requires:       python-psycopg2
Requires:       python-six >= 1.10.0
Requires:       python-sqlalchemy-migrate >= 0.11.0
Requires:       python-stevedore >= 1.20.0
Requires:       python-testresources >= 2.0.0
Requires:       python-testscenarios >= 0.4
BuildArch:      noarch
%python_subpackages

%description
The OpenStack Oslo database handling library. Provides database connectivity
to the different backends and helper utils.
* Documentation: https://docs.openstack.org/developer/oslo.db
* Source: http://git.openstack.org/cgit/openstack/oslo.db
* Bugs: https://bugs.launchpad.net/oslo

%package -n python-oslo.db-doc
Summary:        Documentation for the Oslo database handling library
Group:          Documentation/HTML
BuildRequires:  python-Sphinx
BuildRequires:  python2-openstackdocstheme
BuildRequires:  python3-openstackdocstheme

%description -n python-oslo.db-doc
Documentation for the Oslo database handling library.

%prep
%autosetup -p1 -n oslo.db-4.45.0
%py_req_cleanup

%build
%{python_build}

# generate html docs
PBR_VERSION=%{version} sphinx-build -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%{python_install}

%check
%python_exec -m stestr.cli run

%files %{python_files}
%license LICENSE
%doc README.rst ChangeLog
%{python_sitelib}/oslo_db
%{python_sitelib}/*.egg-info

%files -n python-oslo.db-doc
%license LICENSE
%doc doc/build/html

%changelog
