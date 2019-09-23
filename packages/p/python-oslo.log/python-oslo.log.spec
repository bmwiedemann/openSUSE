#
# spec file for package python-oslo.log
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


Name:           python-oslo.log
Version:        3.42.3
Release:        0
Summary:        OpenStack log library
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/oslo.log
Source0:        https://files.pythonhosted.org/packages/source/o/oslo.log/oslo.log-3.42.3.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python-devel
BuildRequires:  python2-mock
BuildRequires:  python2-monotonic >= 1.4
BuildRequires:  python2-oslo.config >= 5.2.0
BuildRequires:  python2-oslo.context >= 2.20.0
BuildRequires:  python2-oslo.i18n >= 3.20.0
BuildRequires:  python2-oslo.serialization >= 2.25.0
BuildRequires:  python2-oslo.utils >= 3.36.0
BuildRequires:  python2-oslotest
BuildRequires:  python2-pbr >= 3.1.1
BuildRequires:  python2-pyinotify >= 0.9.6
BuildRequires:  python2-python-dateutil >= 2.7.0
BuildRequires:  python2-python-subunit
BuildRequires:  python2-six >= 1.11.0
BuildRequires:  python2-stestr
BuildRequires:  python2-testscenarios
BuildRequires:  python2-testtools
BuildRequires:  python3-devel
BuildRequires:  python3-mock
BuildRequires:  python3-monotonic >= 1.4
BuildRequires:  python3-oslo.config >= 5.2.0
BuildRequires:  python3-oslo.context >= 2.20.0
BuildRequires:  python3-oslo.i18n >= 3.20.0
BuildRequires:  python3-oslo.serialization >= 2.25.0
BuildRequires:  python3-oslo.utils >= 3.36.0
BuildRequires:  python3-oslotest
BuildRequires:  python3-pbr >= 3.1.1
BuildRequires:  python3-pyinotify >= 0.9.6
BuildRequires:  python3-python-dateutil >= 2.7.0
BuildRequires:  python3-python-subunit
BuildRequires:  python3-six >= 1.11.0
BuildRequires:  python3-stestr
BuildRequires:  python3-testscenarios
BuildRequires:  python3-testtools
Requires:       python-debtcollector >= 1.19.0
Requires:       python-monotonic >= 1.4
Requires:       python-oslo.config >= 5.2.0
Requires:       python-oslo.context >= 2.20.0
Requires:       python-oslo.i18n >= 3.20.0
Requires:       python-oslo.serialization >= 2.25.0
Requires:       python-oslo.utils >= 3.36.0
Requires:       python-pyinotify >= 0.9.6
Requires:       python-python-dateutil >= 2.7.0
Requires:       python-six >= 1.11.0
BuildArch:      noarch
%if 0%{?suse_version}
Requires(post): update-alternatives
Requires(postun): update-alternatives
%else
# on RDO, update-alternatives is in chkconfig
Requires(post): chkconfig
Requires(postun): chkconfig
%endif
%python_subpackages

%description
OpenStack logging configuration library provides standardized configuration
for all openstack projects.It also provides custom formatters, handlers and
support for context specific logging (like resource id's etc).

%package -n python-oslo.log-doc
Summary:        Documentation for OpenStack log library
Group:          Development/Languages/Python
BuildRequires:  python-Sphinx
BuildRequires:  python-openstackdocstheme

%description -n python-oslo.log-doc
Documentation for the oslo.log library.

%prep
%autosetup -p1 -n oslo.log-3.42.3
%py_req_cleanup

%build
%{python_build}

# generate html docs
PYTHONPATH=. PBR_VERSION=3.42.3 sphinx-build -b html doc/source doc/build/html
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%{python_install}
%python_clone -a %{buildroot}%{_bindir}/convert-json

%post
%python_install_alternative convert-json

%postun
%python_uninstall_alternative convert-json

%files %{python_files}
%license LICENSE
%doc ChangeLog README.rst
%{python_sitelib}/oslo_log
%{python_sitelib}/*.egg-info
%python_alternative %{_bindir}/convert-json

%files -n python-oslo.log-doc
%license LICENSE
%doc doc/build/html

%changelog
