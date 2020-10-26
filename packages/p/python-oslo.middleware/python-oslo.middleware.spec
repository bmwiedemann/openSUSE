#
# spec file for package python-oslo.middleware
#
# Copyright (c) 2020 SUSE LLC
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
Version:        4.1.1
Release:        0
Summary:        OpenStack oslo.middleware library
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/oslo.middleware
Source0:        https://files.pythonhosted.org/packages/source/o/oslo.middleware/oslo.middleware-4.1.1.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python3-Jinja2 >= 2.10
BuildRequires:  python3-WebOb >= 1.8.0
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
BuildRequires:  python3-six
BuildRequires:  python3-statsd >= 3.2.1
BuildRequires:  python3-stestr
BuildRequires:  python3-stevedore >= 1.20.0
BuildRequires:  python3-testtools
BuildArch:      noarch

%description
Oslo middleware library includes components that can be injected into wsgi
pipelines to intercept request/response flows. The base class can be enhanced
with functionality like add/delete/modification of http headers and support
for limiting size/connection etc.

%package -n python3-oslo.middleware
Summary:        OpenStack oslo.middleware library
Group:          Development/Languages/Python
Requires:       python3-Jinja2 >= 2.10
Requires:       python3-WebOb >= 1.8.0
Requires:       python3-debtcollector >= 1.2.0
Requires:       python3-oslo.config >= 5.2.0
Requires:       python3-oslo.context >= 2.19.2
Requires:       python3-oslo.i18n >= 3.15.3
Requires:       python3-oslo.serialization
Requires:       python3-oslo.utils >= 3.33.0
Requires:       python3-six
Requires:       python3-statsd >= 3.2.1
Requires:       python3-stevedore >= 1.20.0

%description -n python3-oslo.middleware
Oslo middleware library includes components that can be injected into wsgi
pipelines to intercept request/response flows. The base class can be enhanced
with functionality like add/delete/modification of http headers and support
for limiting size/connection etc.

This package contains the Python 3.x module.

%package -n python3-oslo.middleware-doc
Summary:        Documentation for OpenStack middleware library
Group:          Development/Languages/Python
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme

%description -n python3-oslo.middleware-doc
Oslo middleware library includes components that can be injected into wsgi
pipelines to intercept request/response flows. The base class can be enhanced
with functionality like add/delete/modification of http headers and support
for limiting size/connection etc.
This package contains the documentation.

%prep
%autosetup -p1 -n oslo.middleware-4.1.1
%py_req_cleanup

%build
%py3_build

# generate html docs
PBR_VERSION=%{version} %sphinx_build -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%py3_install

%check
python3 -m stestr.cli run

%files -n python3-oslo.middleware
%license LICENSE
%doc README.rst ChangeLog
%{python3_sitelib}/oslo_middleware
%{python3_sitelib}/*.egg-info

%files -n python3-oslo.middleware-doc
%license LICENSE
%doc doc/build/html

%changelog
