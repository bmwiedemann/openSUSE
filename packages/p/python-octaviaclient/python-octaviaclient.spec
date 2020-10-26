#
# spec file for package python-octaviaclient
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


Name:           python-octaviaclient
Version:        2.2.0
Release:        0
Summary:        Octavia Plugin for the OpenStack Command-line Client
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/python-octaviaclient
Source0:        https://files.pythonhosted.org/packages/source/p/python-octaviaclient/python-octaviaclient-2.2.0.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python3-mock
BuildRequires:  python3-openstackclient >= 3.12.0
BuildRequires:  python3-oslotest
BuildRequires:  python3-requests-mock
BuildRequires:  python3-stestr
BuildRequires:  python3-testscenarios
BuildArch:      noarch

%description
The Python Octavia Client (python-octaviaclient) is a command-line client for
the OpenStack Load Balancing service.

%package -n python3-octaviaclient
Summary:        Octavia Plugin for the OpenStack Command-line Client
Group:          Development/Languages/Python
Requires:       python3-Babel
Requires:       python3-cliff >= 2.8.0
Requires:       python3-keystoneauth1 >= 3.4.0
Requires:       python3-netifaces
Requires:       python3-neutronclient >= 6.7.0
Requires:       python3-openstackclient >= 3.12.0
Requires:       python3-osc-lib >= 1.14.1
Requires:       python3-oslo.serialization >= 2.18.0
Requires:       python3-oslo.utils >= 3.33.0
Requires:       python3-requests >= 2.14.2
Requires:       python3-six

%description -n python3-octaviaclient
The Python Octavia Client (python-octaviaclient) is a command-line client for
the OpenStack Load Balancing service.

This package contains the Python 3.x module.

%package -n python-octaviaclient-doc
Summary:        Documentation for OpenStack Octavia API Client
Group:          Documentation/HTML
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-reno
BuildRequires:  python3-sphinxcontrib-svg2pdfconverter

%description -n python-octaviaclient-doc
The Python Octavia Client (python-octaviaclient) is a command-line client for
the OpenStack Load Balancing service.
This package contains auto-generated documentation.

%prep
%autosetup -p1 -n python-octaviaclient-2.2.0
%py_req_cleanup

%build
%{py3_build}

PBR_VERSION=2.2.0 %sphinx_build -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%{py3_install}

%check
# we don't want hacking
rm -f octaviaclient/tests/unit/test_hacking.py
python3 -m stestr.cli run

%files -n python3-octaviaclient
%doc README.rst
%license LICENSE
%{python3_sitelib}/octaviaclient
%{python3_sitelib}/*.egg-info

%files -n python-octaviaclient-doc
%license LICENSE
%doc doc/build/html

%changelog
