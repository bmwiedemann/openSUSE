#
# spec file for package python-manilaclient
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


Name:           python-manilaclient
Version:        1.27.0
Release:        0
Summary:        Client Library for OpenStack Share API
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/python-manilaclient
Source0:        https://files.pythonhosted.org/packages/source/p/python-manilaclient/python-manilaclient-1.27.0.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python-devel
BuildRequires:  python2-ddt
BuildRequires:  python2-fixtures
BuildRequires:  python2-mock
BuildRequires:  python2-openstackclient
BuildRequires:  python2-stestr
BuildRequires:  python2-testrepository
BuildRequires:  python2-testtools
BuildRequires:  python3-ddt
BuildRequires:  python3-devel
BuildRequires:  python3-fixtures
BuildRequires:  python3-mock
BuildRequires:  python3-openstackclient
BuildRequires:  python3-stestr
BuildRequires:  python3-testrepository
BuildRequires:  python3-testtools
Requires:       python-Babel >= 2.3.4
Requires:       python-PrettyTable >= 0.7.1
Requires:       python-debtcollector >= 1.2.0
Requires:       python-keystoneclient >= 3.8.0
Requires:       python-oslo.config >= 5.2.0
Requires:       python-oslo.log >= 3.36.0
Requires:       python-oslo.serialization >= 2.18.0
Requires:       python-oslo.utils >= 3.33.0
Requires:       python-requests >= 2.14.2
Requires:       python-simplejson >= 3.5.1
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
Client library and command line utility for interacting with Openstack
Share API.

%package -n python-manilaclient-doc
Summary:        Documentation for OpenStack Share API Client
Group:          Documentation/HTML
BuildRequires:  python-Sphinx
BuildRequires:  python-openstackdocstheme
BuildRequires:  python-sphinxcontrib-programoutput

%description -n python-manilaclient-doc
Client library and command line utility for interacting with Openstack
Share API.
This package contains auto-generated documentation.

%prep
%autosetup -p1 -n python-manilaclient-1.27.0
%py_req_cleanup

%build
%{python_build}

PBR_VERSION=1.27.0 sphinx-build -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%{python_install}
# bash completion
install -p -D -m 644 tools/manila.bash_completion %{buildroot}%{_sysconfdir}/bash_completion.d/manila.bash_completion
%python_clone -a %{buildroot}%{_bindir}/manila
%python_clone -a %{buildroot}%{_sysconfdir}/bash_completion.d/manila.bash_completion

%post
%{python_install_alternative manila %{_sysconfdir}/bash_completion.d/manila.bash_completion}

%postun
%python_uninstall_alternative manila

%check
# we dont want to depend on Tempest so remove the relevant tests
rm -f manilaclient/tests/unit/test_shell.py
rm -f manilaclient/tests/unit/test_functional_utils.py
rm -rf manilaclient/tests/functional
%python_exec -m stestr.cli run

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/manilaclient
%{python_sitelib}/*.egg-info
%python_alternative %{_bindir}/manila
%python_alternative %{_sysconfdir}/bash_completion.d/manila.bash_completion

%files -n python-manilaclient-doc
%license LICENSE
%doc doc/build/html

%changelog
