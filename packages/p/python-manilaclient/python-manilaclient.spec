#
# spec file for package python-manilaclient
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
Name:           python-manilaclient
Version:        5.6.0
Release:        0
Summary:        Client Library for OpenStack Share API
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/python-manilaclient
Source0:        https://files.pythonhosted.org/packages/source/p/python_manilaclient/python_manilaclient-%{version}.tar.gz
BuildRequires:  %{python_module ddt}
BuildRequires:  %{python_module fixtures}
BuildRequires:  %{python_module openstackclient}
BuildRequires:  %{python_module osc-lib >= 1.10.0}
BuildRequires:  %{python_module oslo.config >= 5.2.0}
BuildRequires:  %{python_module oslo.log >= 3.36.0}
BuildRequires:  %{python_module oslo.serialization >= 2.20.0}
BuildRequires:  %{python_module oslo.utils >= 3.33.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module stestr}
BuildRequires:  %{python_module testrepository}
BuildRequires:  %{python_module testtools}
BuildRequires:  %{python_module wheel}
BuildRequires:  openstack-macros
Requires:       python-Babel >= 2.5.0
Requires:       python-PrettyTable >= 0.7.1
Requires:       python-debtcollector >= 1.2.0
Requires:       python-keystoneclient >= 3.8.0
Requires:       python-osc-lib >= 1.10.0
Requires:       python-oslo.config >= 5.2.0
Requires:       python-oslo.log >= 3.36.0
Requires:       python-oslo.serialization >= 2.20.0
Requires:       python-oslo.utils >= 3.33.0
Requires:       python-requests >= 2.14.2
Requires:       python-simplejson
BuildArch:      noarch
%python_subpackages

%description
Client library and command line utility for interacting with Openstack
Share API.

%package -n python3-manilaclient-doc
Summary:        Documentation for OpenStack Share API Client
Group:          Documentation/HTML
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-sphinxcontrib-programoutput

%description -n python3-manilaclient-doc
Client library and command line utility for interacting with Openstack
Share API.
This package contains auto-generated documentation.

%prep
%autosetup -p1 -n python_manilaclient-%{version}

%build
%pyproject_wheel

PBR_VERSION=%{version} sphinx-build -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%pyproject_install
# bash completion
install -p -D -m 644 tools/manila.bash_completion %{buildroot}%{_sysconfdir}/bash_completion.d/manila.bash_completion

%check
# we don't want to depend on Tempest so remove the relevant tests
rm -f manilaclient/tests/unit/test_shell.py
rm -f manilaclient/tests/unit/test_functional_utils.py
rm -rf manilaclient/tests/functional
%{openstack_stestr_run}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/manilaclient
%{python_sitelib}/python_manilaclient-%{version}.dist-info
%{_bindir}/manila
%{_sysconfdir}/bash_completion.d/manila.bash_completion

%files -n python3-manilaclient-doc
%license LICENSE
%doc doc/build/html

%changelog
