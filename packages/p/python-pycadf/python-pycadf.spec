#
# spec file for package python-pycadf
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


%global oldpython python
Name:           python-pycadf
Version:        4.0.1
Release:        0
Summary:        DMTF Cloud Audit (CADF) data model
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/pycadf
Source0:        https://files.pythonhosted.org/packages/source/p/pycadf/pycadf-4.0.1.tar.gz
BuildRequires:  %{python_module fixtures}
BuildRequires:  %{python_module oslo.config >= 5.2.0}
BuildRequires:  %{python_module oslo.serialization >= 2.18.0}
BuildRequires:  %{python_module oslotest}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module stestr}
BuildRequires:  %{python_module testscenarios}
BuildRequires:  %{python_module testtools}
BuildRequires:  %{python_module wheel}
BuildRequires:  openstack-macros
Requires:       python-debtcollector
Requires:       python-oslo.config >= 5.2.0
Requires:       python-oslo.serialization >= 2.18.0
Requires:       python-pytz
Requires:       python-six
Requires:       python3-pycadf-common = %{version}
BuildArch:      noarch
%python_subpackages

%description
DMTF Cloud Audit (CADF) data model

%package -n python3-pycadf-doc
Summary:        Documentation for the DMTF Cloud Audit (CADF) data model
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-sphinxcontrib-apidoc
Provides:       %{oldpython}-pycadf-doc = %{version}
Obsoletes:      %{oldpython}-pycadf-doc <= 4.0.1

%description -n python3-pycadf-doc
Documentation for the DMTF Cloud Audit (CADF) data model.

%package -n python3-pycadf-common
Summary:        Common files for the DMTF Cloud Audit (CADF) data model
Provides:       %{oldpython}-pycadf-common = %{version}
Obsoletes:      %{oldpython}-pycadf-common <= 4.0.1

%description -n python3-pycadf-common
Configuration files for the DMTF Cloud Audit (CADF) data model.

%prep
%autosetup -n pycadf-%{version}

%build
%pyproject_wheel

# generate html docs
sphinx-build -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%pyproject_install
# FIXME: pbr/wheel bug installing onfiguration files in /usr/etc
mkdir -p %{buildroot}/%{_sysconfdir}
mv %{buildroot}%{_prefix}%{_sysconfdir}/pycadf %{buildroot}/%{_sysconfdir}/

%check
%{openstack_stestr_run}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/pycadf
%{python_sitelib}/pycadf-%{version}.dist-info

%files -n python3-pycadf-common
%license LICENSE
%dir %{_sysconfdir}/pycadf
%config(noreplace) %{_sysconfdir}/pycadf/*.conf

%files -n python3-pycadf-doc
%license LICENSE
%doc doc/build/html

%changelog
