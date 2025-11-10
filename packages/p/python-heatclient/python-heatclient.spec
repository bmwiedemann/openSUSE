#
# spec file for package python-heatclient
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
Name:           python-heatclient
Version:        4.3.0
Release:        0
Summary:        Python API and CLI for OpenStack Heat
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/python-heatclient
Source0:        https://files.pythonhosted.org/packages/source/p/python_heatclient/python_heatclient-%{version}.tar.gz
BuildRequires:  %{python_module PyYAML >= 3.13}
BuildRequires:  %{python_module cliff >= 2.8.0}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module fixtures}
BuildRequires:  %{python_module openstackclient}
BuildRequires:  %{python_module osc-lib >= 1.14.0}
BuildRequires:  %{python_module oslo.serialization >= 2.18.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module requests-mock}
BuildRequires:  %{python_module stestr}
BuildRequires:  %{python_module swiftclient}
BuildRequires:  %{python_module testscenarios}
BuildRequires:  %{python_module testtools}
BuildRequires:  %{python_module wheel}
BuildRequires:  openstack-macros
Requires:       python-Babel
Requires:       python-PrettyTable >= 0.7.2
Requires:       python-PyYAML >= 3.13
Requires:       python-cliff >= 2.8.0
Requires:       python-iso8601 >= 0.1.11
Requires:       python-openstackclient
Requires:       python-osc-lib >= 1.14.0
Requires:       python-oslo.i18n >= 3.15.3
Requires:       python-oslo.serialization >= 2.18.0
Requires:       python-oslo.utils >= 3.33.0
Requires:       python-requests >= 2.14.2
Requires:       python-swiftclient
BuildArch:      noarch
%python_subpackages

%description
This is a client for the OpenStack Heat API. There's a Python API (the
heatclient module), and a command-line script (heat). Each implements 100% of
the OpenStack Heat API.

%package -n python3-heatclient-doc
Summary:        Documentation for OpenStack Heat API Client
Group:          Documentation/HTML
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme

%description -n python3-heatclient-doc
This is a client for the OpenStack Heat API. There's a Python API (the
heatclient module), and a command-line script (heat). Each implements 100% of
the OpenStack Heat API.
This package contains auto-generated documentation.

%prep
%autosetup -p1 -n python_heatclient-%{version}
%py_req_cleanup

%build
%pyproject_wheel

PBR_VERSION=%{version} sphinx-build -b html doc/source doc/build/html
PBR_VERSION=%{version} sphinx-build -b man doc/source doc/build/man
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%pyproject_install
# man page
install -p -D -m 644 doc/build/man/heat.1 %{buildroot}%{_mandir}/man1/heat.1
# bash completion
install -p -D -m 644 tools/heat.bash_completion %{buildroot}%{_sysconfdir}/bash_completion.d/heat.bash_completion

%check
%{openstack_stestr_run}

%files %{python_files}
%license LICENSE
%{python_sitelib}/heatclient
%{python_sitelib}/python_heatclient-%{version}.dist-info
%{_bindir}/heat
%{_mandir}/man1/heat.1*
%{_sysconfdir}/bash_completion.d/heat.bash_completion

%files -n python3-heatclient-doc
%license LICENSE
%doc doc/build/html README.rst

%changelog
