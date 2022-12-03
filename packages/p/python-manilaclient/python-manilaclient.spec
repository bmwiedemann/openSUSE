#
# spec file for package python-manilaclient
#
# Copyright (c) 2022 SUSE LLC
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


Name:           python-manilaclient
Version:        4.2.0
Release:        0
Summary:        Client Library for OpenStack Share API
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/python-manilaclient
Source0:        https://files.pythonhosted.org/packages/source/p/python-manilaclient/python-manilaclient-4.2.0.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python3-ddt
BuildRequires:  python3-fixtures
BuildRequires:  python3-openstackclient
BuildRequires:  python3-osc-lib >= 1.10.0
BuildRequires:  python3-oslo.config >= 5.2.0
BuildRequires:  python3-oslo.log >= 3.36.0
BuildRequires:  python3-oslo.serialization >= 2.18.0
BuildRequires:  python3-oslo.utils >= 3.33.0
BuildRequires:  python3-stestr
BuildRequires:  python3-testrepository
BuildRequires:  python3-testtools
BuildArch:      noarch

%description
Client library and command line utility for interacting with Openstack
Share API.

%package -n python3-manilaclient
Summary:        Client Library for OpenStack Share API
Requires:       python3-Babel >= 2.3.4
Requires:       python3-PrettyTable >= 0.7.1
Requires:       python3-debtcollector >= 1.2.0
Requires:       python3-keystoneclient >= 3.8.0
Requires:       python3-osc-lib >= 1.10.0
Requires:       python3-oslo.config >= 5.2.0
Requires:       python3-oslo.log >= 3.36.0
Requires:       python3-oslo.serialization >= 2.18.0
Requires:       python3-oslo.utils >= 3.33.0
Requires:       python3-requests >= 2.14.2
Requires:       python3-simplejson >= 3.5.1
%if 0%{?suse_version}
Obsoletes:      python2-manilaclient < 2.0.0
%endif

%description -n python3-manilaclient
Client library and command line utility for interacting with Openstack
Share API.

%package -n python-manilaclient-doc
Summary:        Documentation for OpenStack Share API Client
Group:          Documentation/HTML
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-sphinxcontrib-programoutput

%description -n python-manilaclient-doc
Client library and command line utility for interacting with Openstack
Share API.
This package contains auto-generated documentation.

%prep
%autosetup -p1 -n python-manilaclient-4.2.0
%py_req_cleanup

%build
%{py3_build}

PBR_VERSION=4.2.0 %sphinx_build -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%{py3_install}
# bash completion
install -p -D -m 644 tools/manila.bash_completion %{buildroot}%{_sysconfdir}/bash_completion.d/manila.bash_completion

%check
# we don't want to depend on Tempest so remove the relevant tests
rm -f manilaclient/tests/unit/test_shell.py
rm -f manilaclient/tests/unit/test_functional_utils.py
rm -rf manilaclient/tests/functional
python3 -m stestr.cli run

%files -n python3-manilaclient
%doc README.rst
%license LICENSE
%{python3_sitelib}/manilaclient
%{python3_sitelib}/*.egg-info
%{_bindir}/manila
%{_sysconfdir}/bash_completion.d/manila.bash_completion

%files -n python-manilaclient-doc
%license LICENSE
%doc doc/build/html

%changelog
