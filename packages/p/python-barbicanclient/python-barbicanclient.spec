#
# spec file for package python-barbicanclient
#
# Copyright (c) 2024 SUSE LLC
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
Version:        6.0.0
Release:        0
Summary:        Client for the Barbican Key Management API
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/python-barbicanclient
Source0:        https://files.pythonhosted.org/packages/source/p/python-barbicanclient/python-barbicanclient-6.0.0.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python3-cliff >= 2.8.0
BuildRequires:  python3-keystoneauth1 >= 5.1.1
BuildRequires:  python3-oslo.i18n >= 3.15.3
BuildRequires:  python3-oslo.serialization >= 2.18.0
BuildRequires:  python3-oslo.utils >= 3.33.0
BuildRequires:  python3-pbr >= 2.0.0
BuildRequires:  python3-requests >= 2.14.2
BuildRequires:  python3-requests-mock
BuildRequires:  python3-stestr
BuildRequires:  python3-testscenarios
BuildRequires:  python3-testtools
BuildArch:      noarch
%if 0%{?suse_version}
Requires(post): update-alternatives
Requires(postun): update-alternatives
%else
# on RDO, update-alternatives is in chkconfig
Requires(post): chkconfig
Requires(postun): chkconfig
%endif

%description
This is a client for the Barbican Key Management API. This package includes a
Python library for accessing the API (the barbicanclient module), and a
command-line script (barbican).

%package -n python3-barbicanclient
Summary:        Client for the Barbican Key Management API
Requires:       python3-cliff >= 2.8.0
Requires:       python3-keystoneauth1 >= 5.1.1
Requires:       python3-oslo.i18n >= 3.15.3
Requires:       python3-oslo.serialization >= 2.18.0
Requires:       python3-oslo.utils >= 3.33.0
Requires:       python3-pbr >= 2.0.0
Requires:       python3-requests >= 2.14.2
%if 0%{?suse_version}
Obsoletes:      python2-barbicanclient < 4.10.0
%endif

%description -n python3-barbicanclient
This is a client for the Barbican Key Management API. This package includes a
Python library for accessing the API (the barbicanclient module), and a
command-line script (barbican).

This package contains the Python 3.x module.

%package -n python-barbicanclient-doc
Summary:        Documentation for OpenStack Key Management API Client
Group:          Documentation/HTML
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-sphinxcontrib-svg2pdfconverter

%description -n python-barbicanclient-doc
Documentation for the client library for interacting with
Openstack Key Management API

%prep
%autosetup -p1 -n %{name}-%{version}
%py_req_cleanup

%build
%{py3_build}

# generate html docs
PBR_VERSION=%{version} %sphinx_build -b html doc/source doc/build/html
# Remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%{py3_install}

%check
%{openstack_stestr_run} \
    --exclude-regex 'barbicanclient.tests.test_barbican.WhenTestingBarbicanCLI.test_should_show_usage_with_help_flag'

%files -n python3-barbicanclient
%license LICENSE
%{python3_sitelib}/python_barbicanclient-%{version}-py?.*.egg-info
%{python3_sitelib}/barbicanclient
%{_bindir}/barbican

%files -n python-barbicanclient-doc
%doc README.rst doc/build/html
%license LICENSE

%changelog
