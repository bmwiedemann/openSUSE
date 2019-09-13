#
# spec file for package python-oslo.middleware
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


Name:           python-oslo.middleware
Version:        3.37.1
Release:        0
Summary:        OpenStack oslo.middleware library
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/oslo.middleware
Source0:        https://files.pythonhosted.org/packages/source/o/oslo.middleware/oslo.middleware-3.37.1.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python-devel
BuildRequires:  python2-Jinja2 >= 2.10
BuildRequires:  python2-WebOb >= 1.7.1
BuildRequires:  python2-debtcollector >= 1.2.0
BuildRequires:  python2-fixtures
BuildRequires:  python2-mock
BuildRequires:  python2-oslo.config >= 5.2.0
BuildRequires:  python2-oslo.context >= 2.19.2
BuildRequires:  python2-oslo.i18n >= 3.15.3
BuildRequires:  python2-oslo.serialization
BuildRequires:  python2-oslo.utils >= 3.33.0
BuildRequires:  python2-oslotest
BuildRequires:  python2-pbr >= 2.0.0
BuildRequires:  python2-six >= 1.10.0
BuildRequires:  python2-statsd >= 3.2.1
BuildRequires:  python2-stestr
BuildRequires:  python2-stevedore >= 1.20.0
BuildRequires:  python2-testtools
BuildRequires:  python3-Jinja2 >= 2.10
BuildRequires:  python3-WebOb >= 1.7.1
BuildRequires:  python3-debtcollector >= 1.2.0
BuildRequires:  python3-devel
BuildRequires:  python3-fixtures
BuildRequires:  python3-mock
BuildRequires:  python3-oslo.config >= 5.2.0
BuildRequires:  python3-oslo.context >= 2.19.2
BuildRequires:  python3-oslo.i18n >= 3.15.3
BuildRequires:  python3-oslo.serialization
BuildRequires:  python3-oslo.utils >= 3.33.0
BuildRequires:  python3-oslotest
BuildRequires:  python3-pbr >= 2.0.0
BuildRequires:  python3-six >= 1.10.0
BuildRequires:  python3-statsd >= 3.2.1
BuildRequires:  python3-stestr
BuildRequires:  python3-stevedore >= 1.20.0
BuildRequires:  python3-testtools
Requires:       python-Jinja2 >= 2.10
Requires:       python-WebOb >= 1.7.1
Requires:       python-debtcollector >= 1.2.0
Requires:       python-oslo.config >= 5.2.0
Requires:       python-oslo.context >= 2.19.2
Requires:       python-oslo.i18n >= 3.15.3
Requires:       python-oslo.serialization
Requires:       python-oslo.utils >= 3.33.0
Requires:       python-six >= 1.10.0
Requires:       python-statsd >= 3.2.1
Requires:       python-stevedore >= 1.20.0
BuildArch:      noarch
%python_subpackages

%description
Oslo middleware library includes components that can be injected into wsgi
pipelines to intercept request/response flows. The base class can be enhanced
with functionality like add/delete/modification of http headers and support
for limiting size/connection etc.

%package -n python-oslo-middleware-doc
Summary:        Documentation for OpenStack middleware library
Group:          Development/Languages/Python
BuildRequires:  python-Sphinx
BuildRequires:  python-openstackdocstheme
BuildRequires:  python-reno

%description -n python-oslo-middleware-doc
Oslo middleware library includes components that can be injected into wsgi
pipelines to intercept request/response flows. The base class can be enhanced
with functionality like add/delete/modification of http headers and support
for limiting size/connection etc.
This package contains the documentation.

%prep
%autosetup -p1 -n oslo.middleware-3.37.1
%py_req_cleanup

%build
%{python_build}

# generate html docs
%{__python2} setup.py build_sphinx
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%{python_install}

%check
%python_exec -m stestr.cli run

%files %{python_files}
%license LICENSE
%doc README.rst ChangeLog
%{python_sitelib}/oslo_middleware
%{python_sitelib}/*.egg-info

%files -n python-oslo-middleware-doc
%license LICENSE
%doc doc/build/html

%changelog
