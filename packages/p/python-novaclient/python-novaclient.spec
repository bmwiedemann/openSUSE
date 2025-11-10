#
# spec file for package python-novaclient
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
Name:           python-novaclient
Version:        18.11.0
Release:        0
Summary:        Python API and CLI for OpenStack Nova
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/python-novaclient
Source0:        https://files.pythonhosted.org/packages/source/p/python-novaclient/python_novaclient-%{version}.tar.gz
BuildRequires:  %{python_module ddt}
BuildRequires:  %{python_module fixtures}
BuildRequires:  %{python_module openstacksdk}
BuildRequires:  %{python_module os-client-config}
BuildRequires:  %{python_module osprofiler}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module requests-mock}
BuildRequires:  %{python_module stestr}
BuildRequires:  %{python_module testscenarios}
BuildRequires:  %{python_module testtools}
BuildRequires:  %{python_module wheel}
BuildRequires:  openssl
BuildRequires:  openstack-macros
Requires:       python-Babel
Requires:       python-PrettyTable >= 0.7.2
Requires:       python-openstacksdk
Requires:       python-oslo.i18n >= 3.15.3
Requires:       python-oslo.serialization >= 2.20.0
Requires:       python-oslo.utils >= 3.33.0
Requires:       python-simplejson
BuildArch:      noarch
%python_subpackages

%description
This is a client for the OpenStack Nova API. There's a Python API (the
novaclient module), and a command-line script (nova). Each implements 100% of
the OpenStack Nova API.

%package -n python3-novaclient-doc
Summary:        Documentation for OpenStack Nova API Client
Group:          Documentation/HTML
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-reno
BuildRequires:  python3-sphinxcontrib-apidoc

%description -n python3-novaclient-doc
This is a client for the OpenStack Nova API. There's a Python API (the
novaclient module), and a command-line script (nova). Each implements 100% of
the OpenStack Nova API.

This package contains auto-generated documentation.

%prep
%autosetup -p1 -n python_novaclient-%{version}

%build
%pyproject_wheel

PBR_VERSION=%{version} %sphinx_build -b html -d doc/build/doctrees doc/source doc/build/html
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.doctrees doc/build/html/.buildinfo

%install
%pyproject_install

%check
export OS_TEST_PATH=novaclient/tests/unit
%{openstack_stestr_run}

%files %{python_files}
%license LICENSE
%{_bindir}/nova
%{python_sitelib}/novaclient
%{python_sitelib}/python_novaclient-%{version}.dist-info

%files -n python3-novaclient-doc
%doc README.rst doc/build/html
%license LICENSE

%changelog
