#
# spec file for package python-barbicanclient
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


Name:           python-barbicanclient
Version:        4.8.1
Release:        0
Summary:        Client for the Barbican Key Management API
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/python-barbicanclient
Source0:        https://files.pythonhosted.org/packages/source/p/python-barbicanclient/python-barbicanclient-4.8.1.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python-devel
BuildRequires:  python2-cliff >= 2.8.0
BuildRequires:  python2-keystoneauth1 >= 3.4.0
BuildRequires:  python2-mock
BuildRequires:  python2-oslo.i18n >= 3.15.3
BuildRequires:  python2-oslo.serialization >= 2.18.0
BuildRequires:  python2-oslo.utils >= 3.33.0
BuildRequires:  python2-pbr >= 2.0.0
BuildRequires:  python2-requests >= 2.14.2
BuildRequires:  python2-requests-mock
BuildRequires:  python2-stestr
BuildRequires:  python2-testscenarios
BuildRequires:  python2-testtools
BuildRequires:  python3-cliff >= 2.8.0
BuildRequires:  python3-devel
BuildRequires:  python3-keystoneauth1 >= 3.4.0
BuildRequires:  python3-mock
BuildRequires:  python3-oslo.i18n >= 3.15.3
BuildRequires:  python3-oslo.serialization >= 2.18.0
BuildRequires:  python3-oslo.utils >= 3.33.0
BuildRequires:  python3-pbr >= 2.0.0
BuildRequires:  python3-requests >= 2.14.2
BuildRequires:  python3-requests-mock
BuildRequires:  python3-stestr
BuildRequires:  python3-testscenarios
BuildRequires:  python3-testtools
Requires:       python-cliff >= 2.8.0
Requires:       python-keystoneauth1 >= 3.4.0
Requires:       python-oslo.i18n >= 3.15.3
Requires:       python-oslo.serialization >= 2.18.0
Requires:       python-oslo.utils >= 3.33.0
Requires:       python-pbr >= 2.0.0
Requires:       python-requests >= 2.14.2
Requires:       python-six >= 1.10.0
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
OpenStack Key Management API client - Python 2.x
This is a client for the Barbican Key Management API. This package includes a
Python library for accessing the API (the barbicanclient module), and a
command-line script (barbican).

This package contains the Python 2.x module.

%package -n python-barbicanclient-doc
Summary:        Documentation for OpenStack Key Management API Client
Group:          Documentation/HTML
BuildRequires:  python-Sphinx
BuildRequires:  python-openstackdocstheme

%description -n python-barbicanclient-doc
Documentation for the client library for interacting with
Openstack Key Management API

%prep
%autosetup -p1 -n %{name}-%{version}
%py_req_cleanup

# Remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%build
%{python_build}
%{__python2} setup.py build_sphinx

%install
%{python_install}
%python_clone -a %{buildroot}%{_bindir}/barbican

%check
%python_exec -m stestr.cli run

%files %{python_files}
%license LICENSE
%{python_sitelib}/python_barbicanclient-%{version}-py?.?.egg-info
%{python_sitelib}/barbicanclient
%python_alternative %{_bindir}/barbican

%files -n python-barbicanclient-doc
%doc README.rst doc/build/html
%license LICENSE

%changelog
