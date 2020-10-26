#
# spec file for package python-oslo.service
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


%if 0%{?rhel} || 0%{?fedora}
%global rdo 1
%endif
Name:           python-oslo.service
Version:        2.4.0
Release:        0
Summary:        OpenStack oslo.service library
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/oslo.service
Source0:        https://files.pythonhosted.org/packages/source/o/oslo.service/oslo.service-2.4.0.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  procps
BuildRequires:  python3-Paste >= 2.0.2
BuildRequires:  python3-PasteDeploy >= 1.5.0
BuildRequires:  python3-Routes >= 2.3.1
BuildRequires:  python3-WebOb >= 1.7.1
BuildRequires:  python3-eventlet >= 0.25.2
BuildRequires:  python3-fixtures >= 3.0.0
BuildRequires:  python3-greenlet >= 0.4.15
BuildRequires:  python3-mock
BuildRequires:  python3-oslo.concurrency >= 3.25.0
BuildRequires:  python3-oslo.config >= 5.1.0
BuildRequires:  python3-oslo.i18n >= 3.15.3
BuildRequires:  python3-oslo.log >= 3.36.0
BuildRequires:  python3-oslo.utils >= 3.40.2
BuildRequires:  python3-oslotest
BuildRequires:  python3-pbr
BuildRequires:  python3-requests
BuildRequires:  python3-six
BuildRequires:  python3-stestr
BuildRequires:  python3-yappi
BuildArch:      noarch

%description
oslo.service provides a framework for defining new long-running services using
the patterns established by other OpenStack applications. It also includes
utilities long-running applications might need for working with SSL or WSGI,
performing periodic operations, interacting with systemd, etc.

%package -n python3-oslo.service
Summary:        OpenStack oslo.service library
Group:          Development/Languages/Python
Requires:       python3-Paste >= 2.0.2
Requires:       python3-PasteDeploy >= 1.5.0
Requires:       python3-Routes >= 2.3.1
Requires:       python3-WebOb >= 1.7.1
Requires:       python3-debtcollector >= 1.2.0
Requires:       python3-eventlet >= 0.25.2
Requires:       python3-fixtures >= 3.0.0
Requires:       python3-greenlet >= 0.4.15
Requires:       python3-oslo.concurrency >= 3.25.0
Requires:       python3-oslo.config >= 5.1.0
Requires:       python3-oslo.i18n >= 3.15.3
Requires:       python3-oslo.log >= 3.36.0
Requires:       python3-oslo.utils >= 3.40.2
Requires:       python3-six
Requires:       python3-yappi

%description -n python3-oslo.service
oslo.service provides a framework for defining new long-running services using
the patterns established by other OpenStack applications. It also includes
utilities long-running applications might need for working with SSL or WSGI,
performing periodic operations, interacting with systemd, etc.

%package -n python-oslo.service-doc
Summary:        Documentation for OpenStack service library
Group:          Development/Languages/Python
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme

%description -n python-oslo.service-doc
oslo.service provides a framework for defining new long-running services using
the patterns established by other OpenStack applications. It also includes
utilities long-running applications might need for working with SSL or WSGI,
performing periodic operations, interacting with systemd, etc.
This package contains the documentation.

%prep
%autosetup -p1 -n oslo.service-2.4.0
%py_req_cleanup

%build
%{py3_build}

# generate html docs
PYTHONPATH=. PBR_VERSION=%{version} %sphinx_build -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%{py3_install}

%check
python3 -m stestr.cli run

%files -n python3-oslo.service
%license LICENSE
%doc README.rst ChangeLog
%{python3_sitelib}/oslo_service
%{python3_sitelib}/*.egg-info

%files -n python-oslo.service-doc
%license LICENSE
%doc doc/build/html

%changelog
