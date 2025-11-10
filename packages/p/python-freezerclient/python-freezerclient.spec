#
# spec file for package python-freezerclient
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
Name:           python-freezerclient
Version:        6.1.0
Release:        0
Summary:        Python API and CLI for OpenStack Freezer
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/python-freezerclient
Source0:        https://files.pythonhosted.org/packages/source/p/python-freezerclient/python_freezerclient-%{version}.tar.gz
BuildRequires:  %{python_module cliff >= 2.8.0}
BuildRequires:  %{python_module fixtures}
BuildRequires:  %{python_module keystoneauth1 >= 3.4.0}
BuildRequires:  %{python_module oslo.serialization >= 2.25.0}
BuildRequires:  %{python_module oslo.utils >= 3.33.0}
BuildRequires:  %{python_module oslotest}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module python-subunit}
BuildRequires:  %{python_module stestr}
BuildRequires:  %{python_module testtools}
BuildRequires:  %{python_module wheel}
BuildRequires:  openstack-macros
Requires:       python-cliff >= 2.8.0
Requires:       python-keystoneauth1 >= 3.4.0
Requires:       python-oslo.serialization >= 2.25.0
Requires:       python-oslo.utils >= 3.33.0
Requires:       python-pbr >= 2.0.0
BuildArch:      noarch
%python_subpackages

%description
Client library for Freezer built on the Freezer API. It provides a Python API
(the freezerclient module) and a command-line tool (freezer).

%package -n python-freezerclient-doc
Summary:        Documentation for OpenStack Freezer API client libary
Group:          Documentation/HTML
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme

%description -n python-freezerclient-doc
Client library for Freezer built on the Freezer API. It provides a Python API
(the freezerclient module) and a command-line tool (freezer).
This package contains the documentation.

%prep
%autosetup -p1 -n python_freezerclient-%{version}

%build
%pyproject_wheel

# Build HTML docs and man page
PBR_VERSION=%{version} %sphinx_build -b html doc/source doc/build/html
rm -r doc/build/html/.{doctrees,buildinfo}

%install
%pyproject_install

%check
%{openstack_stestr_run}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python3_sitelib}/freezerclient
%{python3_sitelib}/python_freezerclient-%{version}.dist-info
%{_bindir}/freezer

%files -n python-freezerclient-doc
%doc doc/build/html
%license LICENSE

%changelog
