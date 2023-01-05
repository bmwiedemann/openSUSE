#
# spec file for package python-glanceclient
#
# Copyright (c) 2023 SUSE LLC
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


Name:           python-glanceclient
Version:        4.2.0
Release:        0
Epoch:          0
Summary:        Python API and CLI for OpenStack Glance
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/python-glanceclient
Source0:        https://files.pythonhosted.org/packages/source/p/python-glanceclient/python-glanceclient-4.2.0.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python3-PrettyTable >= 0.7.1
BuildRequires:  python3-ddt
BuildRequires:  python3-fixtures
BuildRequires:  python3-keystoneclient
BuildRequires:  python3-os-client-config
BuildRequires:  python3-oslo.utils >= 3.33.0
BuildRequires:  python3-pbr >= 2.0.0
BuildRequires:  python3-pyOpenSSL >= 17.1.0
BuildRequires:  python3-requests-mock
BuildRequires:  python3-stestr
BuildRequires:  python3-testscenarios
BuildRequires:  python3-testtools
BuildRequires:  python3-warlock >= 1.2.0
BuildArch:      noarch

%description
This is a client for the OpenStack Glance API. There's a Python API (the
glanceclient module), and a command-line script (glance). Each implements
100% of the OpenStack Glance API.

%package -n python3-glanceclient
Summary:        Python API and CLI for OpenStack Glance
Requires:       python3-PrettyTable >= 0.7.1
Requires:       python3-keystoneauth1 >= 3.6.2
Requires:       python3-oslo.i18n >= 3.15.3
Requires:       python3-oslo.utils >= 3.33.0
Requires:       python3-pbr >= 2.0.0
Requires:       python3-pyOpenSSL >= 17.1.0
Requires:       python3-requests >= 2.14.2
Requires:       python3-warlock >= 1.2.0
Requires:       python3-wrapt >= 1.7.0
%if 0%{?suse_version}
Obsoletes:      python2-glanceclient < 2.18.0
%endif

%description -n python3-glanceclient
This is a client for the OpenStack Glance API. There's a Python API (the
glanceclient module), and a command-line script (glance). Each implements
100% of the OpenStack Glance API.

%package -n python-glanceclient-doc
Summary:        Documentation for OpenStack Glance API Client
Group:          Documentation/HTML
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-reno
BuildRequires:  python3-sphinxcontrib-apidoc

%description -n python-glanceclient-doc
This is a client for the OpenStack Glance API. There's a Python API (the
glanceclient module), and a command-line script (glance). Each implements
100% of the OpenStack Glance API.
This package contains auto-generated documentation.

%prep
%autosetup -p1 -n python-glanceclient-4.2.0
%py_req_cleanup

%build
%py3_build

# generate html docs
PBR_VERSION=4.2.0 %sphinx_build -b html doc/source doc/build/html
PBR_VERSION=4.2.0 %sphinx_build -b man doc/source doc/build/man
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
rm -rf doc/build/man/.{doctrees,buildinfo}

%install
%py3_install
#man pages
install -p -D -m 644 doc/build/man/glance.1 %{buildroot}%{_mandir}/man1/glance.1

%check
python3 -m stestr.cli run

%files -n python3-glanceclient
%license LICENSE
%doc README.rst ChangeLog
%{_bindir}/glance
%{_mandir}/man1/glance.1*
%{python3_sitelib}/glanceclient
%{python3_sitelib}/*.egg-info

%files -n python-glanceclient-doc
%license LICENSE
%doc doc/build/html

%changelog
