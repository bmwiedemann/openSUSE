#
# spec file for package python-oslo.service
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


%if 0%{?rhel} || 0%{?fedora}
%global rdo 1
%endif
Name:           python-oslo.service
Version:        1.38.0
Release:        0
Summary:        OpenStack oslo.service library
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/oslo.service
Source0:        https://files.pythonhosted.org/packages/source/o/oslo.service/oslo.service-1.38.0.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  procps
BuildRequires:  python-devel
BuildRequires:  python2-Paste >= 2.0.2
BuildRequires:  python2-PasteDeploy >= 1.5.0
BuildRequires:  python2-Routes >= 2.3.1
BuildRequires:  python2-WebOb >= 1.7.1
BuildRequires:  python2-eventlet >= 0.18.2
BuildRequires:  python2-fixtures >= 3.0.0
BuildRequires:  python2-greenlet >= 0.4.10
BuildRequires:  python2-mock
BuildRequires:  python2-oslo.concurrency >= 3.25.0
BuildRequires:  python2-oslo.config >= 5.1.0
BuildRequires:  python2-oslo.i18n >= 3.15.3
BuildRequires:  python2-oslo.log >= 3.36.0
BuildRequires:  python2-oslo.utils >= 3.40.2
BuildRequires:  python2-oslotest
BuildRequires:  python2-pbr
BuildRequires:  python2-requests
BuildRequires:  python2-six >= 1.10.0
BuildRequires:  python2-stestr
BuildRequires:  python2-yappi
BuildRequires:  python3-Paste >= 2.0.2
BuildRequires:  python3-PasteDeploy >= 1.5.0
BuildRequires:  python3-Routes >= 2.3.1
BuildRequires:  python3-WebOb >= 1.7.1
BuildRequires:  python3-devel
BuildRequires:  python3-eventlet >= 0.18.2
BuildRequires:  python3-fixtures >= 3.0.0
BuildRequires:  python3-greenlet >= 0.4.10
BuildRequires:  python3-mock
BuildRequires:  python3-oslo.concurrency >= 3.25.0
BuildRequires:  python3-oslo.config >= 5.1.0
BuildRequires:  python3-oslo.i18n >= 3.15.3
BuildRequires:  python3-oslo.log >= 3.36.0
BuildRequires:  python3-oslo.utils >= 3.40.2
BuildRequires:  python3-oslotest
BuildRequires:  python3-pbr
BuildRequires:  python3-requests
BuildRequires:  python3-six >= 1.10.0
BuildRequires:  python3-stestr
BuildRequires:  python3-yappi
Requires:       python-Paste >= 2.0.2
Requires:       python-PasteDeploy >= 1.5.0
Requires:       python-Routes >= 2.3.1
Requires:       python-WebOb >= 1.7.1
Requires:       python-debtcollector >= 1.2.0
Requires:       python-eventlet >= 0.18.2
Requires:       python-fixtures >= 3.0.0
Requires:       python-greenlet >= 0.4.10
Requires:       python-oslo.concurrency >= 3.25.0
Requires:       python-oslo.config >= 5.1.0
Requires:       python-oslo.i18n >= 3.15.3
Requires:       python-oslo.log >= 3.36.0
Requires:       python-oslo.utils >= 3.40.2
Requires:       python-six >= 1.10.0
Requires:       python-yappi
BuildArch:      noarch
%python_subpackages

%description
oslo.service provides a framework for defining new long-running services using
the patterns established by other OpenStack applications. It also includes
utilities long-running applications might need for working with SSL or WSGI,
performing periodic operations, interacting with systemd, etc.

%package -n python-oslo.service-doc
Summary:        Documentation for OpenStack service library
Group:          Development/Languages/Python
BuildRequires:  python-Sphinx
BuildRequires:  python-openstackdocstheme

%description -n python-oslo.service-doc
oslo.service provides a framework for defining new long-running services using
the patterns established by other OpenStack applications. It also includes
utilities long-running applications might need for working with SSL or WSGI,
performing periodic operations, interacting with systemd, etc.
This package contains the documentation.

%prep
%autosetup -p1 -n oslo.service-1.38.0
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
%{python_sitelib}/oslo_service
%{python_sitelib}/*.egg-info

%files -n python-oslo.service-doc
%license LICENSE
%doc doc/build/html

%changelog
