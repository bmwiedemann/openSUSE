#
# spec file for package python-oslo.service
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


Name:           python-oslo.service
Version:        4.3.0
Release:        0
Summary:        OpenStack oslo.service library
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/oslo.service
Source0:        https://files.pythonhosted.org/packages/source/o/oslo-service/oslo_service-%{version}.tar.gz
BuildRequires:  %{python_module Paste >= 2.0.2}
BuildRequires:  %{python_module PasteDeploy >= 1.5.0}
BuildRequires:  %{python_module Routes >= 2.3.1}
BuildRequires:  %{python_module WebOb >= 1.7.1}
BuildRequires:  %{python_module cotyledon}
BuildRequires:  %{python_module eventlet >= 0.27.0}
BuildRequires:  %{python_module fixtures}
BuildRequires:  %{python_module futurist}
BuildRequires:  %{python_module greenlet >= 0.4.15}
BuildRequires:  %{python_module oslo.concurrency >= 3.25.0}
BuildRequires:  %{python_module oslo.config >= 5.1.0}
BuildRequires:  %{python_module oslo.i18n >= 3.15.3}
BuildRequires:  %{python_module oslo.log >= 3.36.0}
BuildRequires:  %{python_module oslo.utils >= 3.40.2}
BuildRequires:  %{python_module oslotest}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module stestr}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module yappi}
BuildRequires:  openstack-macros
BuildRequires:  procps
Requires:       python-Paste >= 2.0.2
Requires:       python-PasteDeploy >= 1.5.0
Requires:       python-Routes >= 2.3.1
Requires:       python-WebOb >= 1.7.1
Requires:       python-cotyledon
Requires:       python-debtcollector >= 1.2.0
Requires:       python-eventlet >= 0.27.0
Requires:       python-fixtures
Requires:       python-futurist
Requires:       python-greenlet >= 0.4.15
Requires:       python-oslo.concurrency >= 3.25.0
Requires:       python-oslo.config >= 5.1.0
Requires:       python-oslo.i18n >= 3.15.3
Requires:       python-oslo.log >= 3.36.0
Requires:       python-oslo.utils >= 3.40.2
Requires:       python-yappi
%if "python%{python_nodots_ver}" == "%{primary_python}"
Obsoletes:      python3-oslo.service < %{version}
%endif
BuildArch:      noarch
%python_subpackages

%description
oslo.service provides a framework for defining new long-running services using
the patterns established by other OpenStack applications. It also includes
utilities long-running applications might need for working with SSL or WSGI,
performing periodic operations, interacting with systemd, etc.

%package -n python-oslo.service-doc
Summary:        Documentation for OpenStack service library
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme

%description -n python-oslo.service-doc
oslo.service provides a framework for defining new long-running services using
the patterns established by other OpenStack applications. It also includes
utilities long-running applications might need for working with SSL or WSGI,
performing periodic operations, interacting with systemd, etc.
This package contains the documentation.

%prep
%autosetup -p1 -n oslo_service-%{version}

%build
%pyproject_wheel

# generate html docs
PYTHONPATH=. PBR_VERSION=%{version} %sphinx_build -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%pyproject_install

%check
%{openstack_stestr_run}

%files %{python_files}
%license LICENSE
%doc README.rst ChangeLog
%{python_sitelib}/oslo_service
%{python_sitelib}/oslo_service-%{version}.dist-info

%files -n python-oslo.service-doc
%license LICENSE
%doc doc/build/html

%changelog
