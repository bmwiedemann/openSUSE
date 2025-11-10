#
# spec file for package python-octaviaclient
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


%global pythons %{primary_python}
Name:           python-octaviaclient
Version:        3.12.0
Release:        0
Summary:        Octavia Plugin for the OpenStack Command-line Client
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/python-octaviaclient
Source0:        https://files.pythonhosted.org/packages/source/p/python_octaviaclient/python_octaviaclient-%{version}.tar.gz
BuildRequires:  %{python_module openstackclient >= 3.12.0}
BuildRequires:  %{python_module oslotest}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module requests-mock}
BuildRequires:  %{python_module stestr}
BuildRequires:  %{python_module testscenarios}
BuildRequires:  %{python_module wheel}
BuildRequires:  openstack-macros
Requires:       python-Babel
Requires:       python-cliff >= 2.8.0
Requires:       python-keystoneauth1 >= 3.18.0
Requires:       python-netifaces
Requires:       python-neutronclient >= 6.7.0
Requires:       python-openstackclient >= 3.12.0
Requires:       python-osc-lib >= 1.14.1
Requires:       python-oslo.serialization >= 2.18.0
Requires:       python-oslo.utils >= 3.33.0
Requires:       python-requests >= 2.14.2
BuildArch:      noarch
%python_subpackages

%description
The Python Octavia Client (python-octaviaclient) is a command-line client for
the OpenStack Load Balancing service.

%package -n python3-octaviaclient-doc
Summary:        Documentation for OpenStack Octavia API Client
Group:          Documentation/HTML
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-reno
BuildRequires:  python3-sphinxcontrib-svg2pdfconverter

%description -n python3-octaviaclient-doc
The Python Octavia Client (python-octaviaclient) is a command-line client for
the OpenStack Load Balancing service.
This package contains auto-generated documentation.

%prep
%autosetup -p1 -n python_octaviaclient-%{version}

%build
%pyproject_wheel

PBR_VERSION=%{version} sphinx-build -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%pyproject_install

%check
# we don't want hacking
rm -f octaviaclient/tests/unit/test_hacking.py
%{openstack_stestr_run}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python3_sitelib}/octaviaclient
%{python3_sitelib}/python_octaviaclient-%{version}.dist-info

%files -n python3-octaviaclient-doc
%license LICENSE
%doc doc/build/html

%changelog
