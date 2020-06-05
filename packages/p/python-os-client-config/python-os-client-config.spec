#
# spec file for package python-os-client-config
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


%global sname os-client-config
%bcond_with test
%bcond_with docs
Name:           python-os-client-config
Version:        2.1.0
Release:        0
Summary:        OpenStack Client Configuration Library
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/%{name}
Source0:        https://files.pythonhosted.org/packages/source/o/os-client-config/os-client-config-2.1.0.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python3-pbr
BuildRequires:  python3-setuptools
BuildArch:      noarch
%if %{with test}
BuildRequires:  python3-extras
BuildRequires:  python3-fixtures
BuildRequires:  python3-glanceclient
BuildRequires:  python3-jsonschema
BuildRequires:  python3-keystoneclient
BuildRequires:  python3-mock
BuildRequires:  python3-oslotest
BuildRequires:  python3-python-subunit
BuildRequires:  python3-stestr
BuildRequires:  python3-testscenarios
BuildRequires:  python3-testtools
%endif

%description
os-client-config is a library for collecting client configuration for
using an OpenStack cloud in a consistent and comprehensive manner.
It will find cloud config for as few as 1 cloud and as many as you want
to put in a config file. It will read environment variables and config
files, and it also contains some vendor specific default values so that
you don't have to know extra info to use OpenStack.

%package -n python3-os-client-config
Summary:        OpenStack Client Configuration Library
Group:          Development/Languages/Python
Requires:       python3-PyYAML
Requires:       python3-appdirs
Requires:       python3-keystoneauth1
Requires:       python3-requestsexceptions

%description -n python3-os-client-config
os-client-config is a library for collecting client configuration for
using an OpenStack cloud in a consistent and comprehensive manner.
It will find cloud config for as few as 1 cloud and as many as you want
to put in a config file. It will read environment variables and config
files, and it also contains some vendor specific default values so that
you don't have to know extra info to use OpenStack.

This package contains the Python 3.x module.

%if %{with docs}
%package -n python-os-client-config-doc
Summary:        Documentation for OpenStack client configuration library
Group:          Development/Languages/Python
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-reno

%description -n python-os-client-config-doc
Documentation for the os-client-config library.
%endif

%prep
%autosetup -p1 -n %{sname}-%{version}
%py_req_cleanup

%build
%py3_build
%if %{with docs}
# generate html docs
PBR_VERSION=%{version} %sphinx_build -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif

%install
%py3_install

%if %{with test}
%check
export PYTHONPATH="%{python3_sitearch}:%{python3_sitelib}:%{buildroot}%{python3_sitelib}"
python3 -m stestr.cli run
%endif

%files -n python3-os-client-config
%license LICENSE
%doc README.rst
%{python3_sitelib}/os_client_config
%{python3_sitelib}/*.egg-info

%if %{with docs}
%files -n python-os-client-config-doc
%doc doc/build/html
%license LICENSE
%endif

%changelog
