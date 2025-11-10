#
# spec file for package python-oslo.middleware
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Version:        6.6.0
Release:        0
Summary:        OpenStack oslo.middleware library
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/oslo.middleware
Source0:        https://files.pythonhosted.org/packages/source/o/oslo-middleware/oslo_middleware-%{version}.tar.gz
BuildRequires:  %{python_module Jinja2 >= 2.10}
BuildRequires:  %{python_module WebOb >= 1.8.0}
BuildRequires:  %{python_module bcrypt >= 3.1.3}
BuildRequires:  %{python_module debtcollector >= 1.2.0}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module fixtures}
BuildRequires:  %{python_module oslo.config >= 5.2.0}
BuildRequires:  %{python_module oslo.context >= 2.19.2}
BuildRequires:  %{python_module oslo.i18n >= 3.15.3}
BuildRequires:  %{python_module oslo.serialization}
BuildRequires:  %{python_module oslo.utils >= 3.33.0}
BuildRequires:  %{python_module oslotest}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module statsd >= 3.2.1}
BuildRequires:  %{python_module stestr}
BuildRequires:  %{python_module stevedore >= 1.20.0}
BuildRequires:  %{python_module testtools}
BuildRequires:  %{python_module wheel}
BuildRequires:  openstack-macros
Requires:       python-Jinja2 >= 2.10
Requires:       python-WebOb >= 1.8.0
Requires:       python-bcrypt >= 3.1.3
Requires:       python-debtcollector >= 1.2.0
Requires:       python-oslo.config >= 5.2.0
Requires:       python-oslo.context >= 2.19.2
Requires:       python-oslo.i18n >= 3.15.3
Requires:       python-oslo.serialization
Requires:       python-oslo.utils >= 3.33.0
Requires:       python-statsd >= 3.2.1
Requires:       python-stevedore >= 1.20.0
BuildArch:      noarch
%python_subpackages

%description
Oslo middleware library includes components that can be injected into wsgi
pipelines to intercept request/response flows. The base class can be enhanced
with functionality like add/delete/modification of http headers and support
for limiting size/connection etc.

%package -n python3-oslo.middleware-doc
Summary:        Documentation for OpenStack middleware library
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme

%description -n python3-oslo.middleware-doc
Oslo middleware library includes components that can be injected into wsgi
pipelines to intercept request/response flows. The base class can be enhanced
with functionality like add/delete/modification of http headers and support
for limiting size/connection etc.
This package contains the documentation.

%prep
%autosetup -p1 -n oslo_middleware-%{version}

%build
%pyproject_wheel

# generate html docs
PBR_VERSION=%{version} %sphinx_build -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%pyproject_install

%check
%{openstack_stestr_run}

%files %{python_files}
%license LICENSE
%doc README.rst ChangeLog
%{python_sitelib}/oslo_middleware
%{python_sitelib}/oslo_middleware-%{version}.dist-info

%files -n python3-oslo.middleware-doc
%license LICENSE
%doc doc/build/html

%changelog
