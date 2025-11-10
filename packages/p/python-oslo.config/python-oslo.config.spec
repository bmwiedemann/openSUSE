#
# spec file for package python-oslo.config
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


Name:           python-oslo.config
Version:        10.0.0
Release:        0
Summary:        OpenStack common configuration library
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/oslo.config
Source0:        https://files.pythonhosted.org/packages/source/o/oslo_config/oslo_config-%{version}.tar.gz
BuildRequires:  %{python_module PyYAML >= 5.1}
BuildRequires:  %{python_module debtcollector >= 1.2.0}
BuildRequires:  %{python_module fixtures}
BuildRequires:  %{python_module importlib-metadata}
BuildRequires:  %{python_module netaddr >= 0.7.18}
BuildRequires:  %{python_module oslo.i18n >= 3.15.3}
BuildRequires:  %{python_module oslotest}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module requests >= 2.18.0}
BuildRequires:  %{python_module requests-mock}
BuildRequires:  %{python_module rfc3986 >= 1.2.0}
BuildRequires:  %{python_module stestr}
BuildRequires:  %{python_module stevedore >= 1.20.0}
BuildRequires:  %{python_module testscenarios}
BuildRequires:  %{python_module testtools}
BuildRequires:  %{python_module wheel}
BuildRequires:  openstack-macros
Requires:       python-PyYAML >= 5.1
Requires:       python-debtcollector >= 1.2.0
Requires:       python-fixtures
Requires:       python-importlib-metadata
Requires:       python-netaddr >= 0.7.18
Requires:       python-oslo.i18n >= 3.15.3
Requires:       python-requests >= 2.18.0
Requires:       python-rfc3986 >= 1.2.0
Requires:       python-stevedore >= 1.20.0
BuildArch:      noarch
%if "python%{python_nodots_ver}" == "%{primary_python}"
Obsoletes:      python3-oslo.config < %{version}
%else
Conflicts:      python3-oslo.config < %{version}
%endif
%python_subpackages

%description
The Oslo project intends to produce a python library containing
infrastructure code shared by OpenStack projects. The APIs provided
by the project should be high quality, stable, consistent and generally
useful.

The oslo-config library is a command line and configuration file
parsing library from the Oslo project.

%package -n python-oslo.config-doc
Summary:        Documentation for OpenStack common configuration library
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-sphinxcontrib-apidoc

%description -n python-oslo.config-doc
Documentation for the oslo-config library.

%prep
%autosetup -p1 -n oslo_config-%{version}

%build
%pyproject_wheel

PBR_VERSION=%{version} PYTHONPATH=. \
    %{sphinx_build} -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%pyproject_install

%python_clone -a %{buildroot}%{_bindir}/oslo-config-generator
%python_clone -a %{buildroot}%{_bindir}/oslo-config-validator

%pre
# If libalternatives is used: Removing old update-alternatives entries.
%python_libalternatives_reset_alternative oslo-config-generator
%python_libalternatives_reset_alternative oslo-config-validator

%post
%python_install_alternative oslo-config-generator
%python_install_alternative oslo-config-validator

%postun
%python_uninstall_alternative oslo-config-generator
%python_uninstall_alternative oslo-config-validator

%check
# Requires oslo.log which we can't depend on for build cycle reasons
rm -v oslo_config/tests/test_cfg.py
%{openstack_stestr_run}

%files %{python_files}
%license LICENSE
%python_alternative %{_bindir}/oslo-config-generator
%python_alternative %{_bindir}/oslo-config-validator
%{python_sitelib}/oslo_config
%{python_sitelib}/oslo_config-%{version}.dist-info

%files -n python-oslo.config-doc
%doc doc/build/html README.rst
%license LICENSE

%changelog
