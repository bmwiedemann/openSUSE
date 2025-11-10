#
# spec file for package python-osc-lib
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


Name:           python-osc-lib
Version:        4.2.0
Release:        0
Summary:        OpenStackClient Library
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/developer/osc-lib
Source0:        https://files.pythonhosted.org/packages/source/o/osc_lib/osc_lib-%{version}.tar.gz
BuildRequires:  %{python_module cliff >= 4.9.0}
BuildRequires:  %{python_module fixtures}
BuildRequires:  %{python_module keystoneauth1 >= 5.10.0}
BuildRequires:  %{python_module openstacksdk >= 4.7.1}
BuildRequires:  %{python_module oslo.i18n >= 6.6.0}
BuildRequires:  %{python_module oslo.utils >= 9.1.0}
BuildRequires:  %{python_module oslotest}
BuildRequires:  %{python_module osprofiler}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module platformdirs}
BuildRequires:  %{python_module requests-mock}
BuildRequires:  %{python_module simplejson}
BuildRequires:  %{python_module stestr}
BuildRequires:  %{python_module stevedore >= 1.20.0}
BuildRequires:  %{python_module testtools}
BuildRequires:  %{python_module wheel}
BuildRequires:  openstack-macros
Requires:       python-cliff >= 4.9.0
Requires:       python-keystoneauth1 >= 5.10.0
Requires:       python-openstacksdk >= 4.7.1
Requires:       python-oslo.i18n >= 6.6.0
Requires:       python-oslo.utils >= 9.1.0
Requires:       python-pbr >= 2.0.0
Requires:       python-platformdirs
Requires:       python-simplejson
Requires:       python-stevedore >= 1.20.0
%if "python%{python_nodots_ver}" == "%{primary_python}"
Obsoletes:      python3-osc-lib < %{version}
%endif
BuildArch:      noarch
%python_subpackages

%description
OpenStackClient (aka OSC) is a command-line client for OpenStack.  osc-lib
is a package of common support modules for writing OSC plugins.

%package -n python-osc-lib-doc
Summary:        Documentation for the OpenStack client library
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-reno
BuildRequires:  python3-sphinxcontrib-apidoc

%description -n python-osc-lib-doc
Documentation for the OpenStack client library.

%prep
%autosetup -p1 -n osc_lib-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

# generate html docs
PBR_VERSION=%{version} PYTHONPATH=. %sphinx_build -a -E -d doc/build/doctrees -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%check
%{openstack_stestr_run}

%files %{python_files}
%license LICENSE
%doc README.rst ChangeLog
%{python_sitelib}/osc_lib
%{python_sitelib}/osc_lib-%{version}.dist-info

%files -n python-osc-lib-doc
%license LICENSE
%doc doc/build/html

%changelog
