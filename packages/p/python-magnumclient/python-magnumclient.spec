#
# spec file for package python-magnumclient
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
Name:           python-magnumclient
Version:        4.9.0
Release:        0
Summary:        Python API and CLI for OpenStack Magnum
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/python-magnumclient
Source0:        https://files.pythonhosted.org/packages/source/p/python-magnumclient/python_magnumclient-%{version}.tar.gz
BuildRequires:  %{python_module PrettyTable >= 0.7.2}
BuildRequires:  %{python_module cryptography >= 3.0}
BuildRequires:  %{python_module decorator >= 3.4.0}
BuildRequires:  %{python_module fixtures}
BuildRequires:  %{python_module keystoneauth1 >= 3.4.0}
BuildRequires:  %{python_module openstackclient}
BuildRequires:  %{python_module osc-lib >= 1.8.0}
BuildRequires:  %{python_module oslo.i18n >= 3.15.3}
BuildRequires:  %{python_module oslo.serialization >= 2.18.0}
BuildRequires:  %{python_module oslo.utils >= 3.33.0}
BuildRequires:  %{python_module oslotest}
BuildRequires:  %{python_module osprofiler}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module python-subunit}
BuildRequires:  %{python_module stestr}
BuildRequires:  %{python_module testscenarios}
BuildRequires:  %{python_module testtools}
BuildRequires:  %{python_module wheel}
BuildRequires:  openstack-macros
Requires:       python-PrettyTable >= 0.7.2
Requires:       python-cryptography >= 3.0
Requires:       python-decorator >= 3.4.0
Requires:       python-keystoneauth1 >= 3.4.0
Requires:       python-osc-lib >= 1.8.0
Requires:       python-oslo.i18n >= 3.15.3
Requires:       python-oslo.log >= 3.36.0
Requires:       python-oslo.serialization >= 2.18.0
Requires:       python-oslo.utils >= 3.33.0
Requires:       python-pbr >= 2.0.0
Requires:       python-requests >= 2.14.2
Requires:       python-stevedore >= 1.20.0
BuildArch:      noarch
%python_subpackages

%description
Client library for Magnum built on the Magnum API. It provides a Python API
(the magnumclient module) and a command-line tool (magnum).

%package -n python3-magnumclient-doc
Summary:        Documentation for OpenStack Magnum API client libary
Group:          Documentation/HTML
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme

%description -n python3-magnumclient-doc
Client library for Magnum built on the Magnum API. It provides a Python API
(the magnumclient module) and a command-line tool (magnum).
This package contains the documentation.

%prep
%autosetup -p1 -n python_magnumclient-%{version}

%build
%pyproject_wheel

# Build HTML docs and man page
PBR_VERSION=%{version} %sphinx_build -b html doc/source doc/build/html
PBR_VERSION=%{version} %sphinx_build -b man doc/source doc/build/man
rm -r doc/build/html/.{doctrees,buildinfo}

%install
%pyproject_install
# man page
install -p -D -m 644 doc/build/man/python-magnumclient.1 %{buildroot}%{_mandir}/man1/magnum.1
# Install bash completion
install -p -D -m 644 tools/magnum.bash_completion %{buildroot}%{_sysconfdir}/bash_completion.d/magnum.bash_completion

%check
%{openstack_stestr_run}

%files %{python_files}
%license LICENSE
%{python_sitelib}/magnumclient
%{python_sitelib}/python_magnumclient-%{version}.dist-info
%{_bindir}/magnum
%{_mandir}/man1/magnum.1.*
%{_sysconfdir}/bash_completion.d/magnum.bash_completion

%files -n python3-magnumclient-doc
%doc README.rst doc/build/html
%license LICENSE

%changelog
