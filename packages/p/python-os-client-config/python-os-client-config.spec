#
# spec file for package python-os-client-config
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


%global sname os-client-config
%bcond_with test
%bcond_with docs
Name:           python-os-client-config
Version:        1.32.0
Release:        0
Summary:        OpenStack Client Configuration Library
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/%{sname}
Source0:        https://files.pythonhosted.org/packages/source/o/%{sname}/%{sname}-%{version}.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python2-pbr
BuildRequires:  python2-setuptools
BuildRequires:  python3-pbr
BuildRequires:  python3-setuptools
Requires:       python-PyYAML
Requires:       python-appdirs
Requires:       python-keystoneauth1
Requires:       python-requestsexceptions
BuildArch:      noarch
%if %{with test}
BuildRequires:  python-extras
BuildRequires:  python-fixtures
BuildRequires:  python-glanceclient
BuildRequires:  python-jsonschema
BuildRequires:  python-keystoneclient
BuildRequires:  python-mock
BuildRequires:  python-oslotest
BuildRequires:  python-python-subunit
BuildRequires:  python-testrepository
BuildRequires:  python-testscenarios
BuildRequires:  python-testtools
%endif
%python_subpackages

%description
os-client-config is a library for collecting client configuration for
using an OpenStack cloud in a consistent and comprehensive manner.
It will find cloud config for as few as 1 cloud and as many as you want
to put in a config file. It will read environment variables and config
files, and it also contains some vendor specific default values so that
you don't have to know extra info to use OpenStack.

%if %{with docs}
%package -n python-os-client-config-doc
Summary:        Documentation for OpenStack client configuration library
Group:          Development/Languages/Python
BuildRequires:  python-Sphinx
BuildRequires:  python-openstackdocstheme
BuildRequires:  python-reno

%description -n python-os-client-config-doc
Documentation for the os-client-config library.
%endif

%prep
%autosetup -n %{sname}-%{version}
%py_req_cleanup
sed -i 's/^warning-is-error.*/warning-is-error = 0/g' setup.cfg

%build
%python_build
%if %{with docs}
# generate html docs
%{__python2} setup.py build_sphinx
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%python_install

%if %{with test}
%check
export PYTHONPATH="%{python2_sitearch}:%{python2_sitelib}:%{buildroot}%{python2_sitelib}"
testr init && testr run
%endif

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/os_client_config
%{python_sitelib}/*.egg-info

%if %{with docs}
%files -n python-os-client-config-doc
%doc doc/build/html
%license LICENSE
%endif

%changelog
