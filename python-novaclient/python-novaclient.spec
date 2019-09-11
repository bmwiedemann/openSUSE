#
# spec file for package python-novaclient
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


Name:           python-novaclient
Version:        13.0.1
Release:        0
Summary:        Python API and CLI for OpenStack Nova
License:        Apache-2.0
Group:          Development/Languages/Python
Source0:        https://files.pythonhosted.org/packages/source/p/python-novaclient/python-novaclient-13.0.1.tar.gz
BuildRequires:  openssl
BuildRequires:  openstack-macros
BuildRequires:  python2-cinderclient
BuildRequires:  python2-ddt
BuildRequires:  python2-fixtures
BuildRequires:  python2-glanceclient
BuildRequires:  python2-keystoneclient
BuildRequires:  python2-mock
BuildRequires:  python2-os-client-config
BuildRequires:  python2-osprofiler
BuildRequires:  python2-pbr >= 2.0.0
BuildRequires:  python2-requests-mock
BuildRequires:  python2-setuptools
BuildRequires:  python2-stestr
BuildRequires:  python2-testscenarios
BuildRequires:  python2-testtools
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
BuildRequires:  python3-setuptools
BuildRequires:  python3-stestr
BuildRequires:  python3-testscenarios
BuildRequires:  python3-testtools
Requires:       openssl
Requires:       python-Babel >= 2.3.4
Requires:       python-PrettyTable >= 0.7.2
Requires:       python-iso8601 >= 0.1.11
Requires:       python-keystoneauth1 >= 3.5.0
Requires:       python-oslo.i18n >= 3.15.3
Requires:       python-oslo.serialization >= 2.18.0
Requires:       python-oslo.utils >= 3.33.0
Requires:       python-pbr >= 2.0.0
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
This is a client for the OpenStack Nova API. There's a Python API (the
novaclient module), and a command-line script (nova). Each implements 100% of
the OpenStack Nova API.

%package -n python-novaclient-doc
Summary:        Documentation for OpenStack Nova API Client
Group:          Documentation/HTML
BuildRequires:  python-Sphinx
BuildRequires:  python-openstackdocstheme
BuildRequires:  python-reno
BuildRequires:  python-sphinxcontrib-apidoc

%description -n python-novaclient-doc
This is a client for the OpenStack Nova API. There's a Python API (the
novaclient module), and a command-line script (nova). Each implements 100% of
the OpenStack Nova API.

This package contains auto-generated documentation.

%prep
%autosetup -p1 -n %{name}-%{version}
%py_req_cleanup

%build
%{python_build}

PBR_VERSION=13.0.1 sphinx-build -b html -d doc/build/doctrees doc/source doc/build/html
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.doctrees doc/build/html/.buildinfo

%install
%{python_install}
%python_clone -a %{buildroot}%{_bindir}/nova

%post
%python_install_alternative nova

%postun
%python_uninstall_alternative nova

%check
export OS_TEST_PATH=novaclient/tests/unit
%python_exec -m stestr.cli run

%files %{python_files}
%license LICENSE
%python_alternative %{_bindir}/nova
%{python_sitelib}/novaclient
%{python_sitelib}/*.egg-info

%files -n python-novaclient-doc
%doc README.rst doc/build/html
%license LICENSE

%changelog
