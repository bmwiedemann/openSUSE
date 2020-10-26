#
# spec file for package python-novaclient
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


Name:           python-novaclient
Version:        17.2.1
Release:        0
Summary:        Python API and CLI for OpenStack Nova
License:        Apache-2.0
Group:          Development/Languages/Python
Source0:        https://files.pythonhosted.org/packages/source/p/python-novaclient/python-novaclient-17.2.1.tar.gz
BuildRequires:  openssl
BuildRequires:  openstack-macros
BuildRequires:  python3-cinderclient
BuildRequires:  python3-ddt
BuildRequires:  python3-fixtures
BuildRequires:  python3-glanceclient
BuildRequires:  python3-keystoneclient
BuildRequires:  python3-mock
BuildRequires:  python3-os-client-config
BuildRequires:  python3-osprofiler
BuildRequires:  python3-pbr >= 2.0.0
BuildRequires:  python3-requests-mock
BuildRequires:  python3-stestr
BuildRequires:  python3-testscenarios
BuildRequires:  python3-testtools
BuildArch:      noarch

%description
This is a client for the OpenStack Nova API. There's a Python API (the
novaclient module), and a command-line script (nova). Each implements 100% of
the OpenStack Nova API.

%package -n python3-novaclient
Summary:        Python API and CLI for OpenStack Nova
Group:          Development/Languages/Python
Requires:       openssl
Requires:       python3-Babel
Requires:       python3-PrettyTable >= 0.7.2
Requires:       python3-iso8601 >= 0.1.11
Requires:       python3-keystoneauth1 >= 3.5.0
Requires:       python3-oslo.i18n >= 3.15.3
Requires:       python3-oslo.serialization >= 2.18.0
Requires:       python3-oslo.utils >= 3.33.0
Requires:       python3-pbr >= 2.0.0
Requires:       python3-simplejson >= 3.5.1
Requires:       python3-six
%if 0%{?suse_version}
Obsoletes:      python2-novaclient < 16.0.0
%endif

%description -n python3-novaclient
This is a client for the OpenStack Nova API. There's a Python API (the
novaclient module), and a command-line script (nova). Each implements 100% of
the OpenStack Nova API.

%package -n python-novaclient-doc
Summary:        Documentation for OpenStack Nova API Client
Group:          Documentation/HTML
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-reno
BuildRequires:  python3-sphinxcontrib-apidoc

%description -n python-novaclient-doc
This is a client for the OpenStack Nova API. There's a Python API (the
novaclient module), and a command-line script (nova). Each implements 100% of
the OpenStack Nova API.

This package contains auto-generated documentation.

%prep
%autosetup -p1 -n %{name}-%{version}
%py_req_cleanup

%build
%{py3_build}

PBR_VERSION=17.2.1 %sphinx_build -b html -d doc/build/doctrees doc/source doc/build/html
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.doctrees doc/build/html/.buildinfo

%install
%{py3_install}

%check
export OS_TEST_PATH=novaclient/tests/unit
python3 -m stestr.cli run

%files -n python3-novaclient
%license LICENSE
%{_bindir}/nova
%{python3_sitelib}/novaclient
%{python3_sitelib}/*.egg-info

%files -n python-novaclient-doc
%doc README.rst doc/build/html
%license LICENSE

%changelog
