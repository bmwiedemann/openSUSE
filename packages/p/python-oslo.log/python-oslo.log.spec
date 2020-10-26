#
# spec file for package python-oslo.log
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


Name:           python-oslo.log
Version:        4.4.0
Release:        0
Summary:        OpenStack log library
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/oslo.log
Source0:        https://files.pythonhosted.org/packages/source/o/oslo.log/oslo.log-4.4.0.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python3-mock
BuildRequires:  python3-monotonic
BuildRequires:  python3-oslo.config >= 5.2.0
BuildRequires:  python3-oslo.context >= 2.20.0
BuildRequires:  python3-oslo.i18n >= 3.20.0
BuildRequires:  python3-oslo.serialization >= 2.25.0
BuildRequires:  python3-oslo.utils >= 3.36.0
BuildRequires:  python3-oslotest
BuildRequires:  python3-pbr >= 3.1.1
BuildRequires:  python3-pyinotify >= 0.9.6
BuildRequires:  python3-python-dateutil >= 2.7.0
BuildRequires:  python3-six
BuildRequires:  python3-stestr
BuildRequires:  python3-testtools
BuildArch:      noarch

%description
OpenStack logging configuration library provides standardized configuration
for all openstack projects.It also provides custom formatters, handlers and
support for context specific logging (like resource id's etc).

%package -n python3-oslo.log
Summary:        OpenStack log library
Group:          Development/Languages/Python
Requires:       python3-debtcollector >= 1.19.0
Requires:       python3-monotonic
Requires:       python3-oslo.config >= 5.2.0
Requires:       python3-oslo.context >= 2.20.0
Requires:       python3-oslo.i18n >= 3.20.0
Requires:       python3-oslo.serialization >= 2.25.0
Requires:       python3-oslo.utils >= 3.36.0
Requires:       python3-pyinotify >= 0.9.6
Requires:       python3-python-dateutil >= 2.7.0
Requires:       python3-six
Requires:       python3-systemd
%if 0%{?suse_version}
Obsoletes:      python2-oslo.log < 4.0.0
%endif

%description -n python3-oslo.log
OpenStack logging configuration library provides standardized configuration
for all openstack projects.It also provides custom formatters, handlers and
support for context specific logging (like resource id's etc).

This package contains the Python 3.x module.

%package -n python-oslo.log-doc
Summary:        Documentation for OpenStack log library
Group:          Development/Languages/Python
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme

%description -n python-oslo.log-doc
Documentation for the oslo.log library.

%prep
%autosetup -p1 -n oslo.log-4.4.0
%py_req_cleanup

%build
%{py3_build}

# generate html docs
PYTHONPATH=. PBR_VERSION=4.4.0 %sphinx_build -b html doc/source doc/build/html
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%{py3_install}

%check
python3 -m stestr.cli run

%files -n python3-oslo.log
%license LICENSE
%doc ChangeLog README.rst
%{python3_sitelib}/oslo_log
%{python3_sitelib}/*.egg-info
%{_bindir}/convert-json

%files -n python-oslo.log-doc
%license LICENSE
%doc doc/build/html

%changelog
