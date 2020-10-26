#
# spec file for package python-pycadf
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


Name:           python-pycadf
Version:        3.1.1
Release:        0
Summary:        DMTF Cloud Audit (CADF) data model
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/pycadf
Source0:        https://files.pythonhosted.org/packages/source/p/pycadf/pycadf-3.1.1.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python3-fixtures
BuildRequires:  python3-oslo.config >= 5.2.0
BuildRequires:  python3-oslo.serialization >= 2.18.0
BuildRequires:  python3-oslotest
BuildRequires:  python3-pbr
BuildRequires:  python3-stestr
BuildRequires:  python3-testscenarios
BuildRequires:  python3-testtools
BuildArch:      noarch

%description
DMTF Cloud Audit (CADF) data model

%package -n python3-pycadf
Summary:        DMTF Cloud Audit (CADF) data model
Group:          Development/Languages/Python
Requires:       python-pycadf-common
Requires:       python3-debtcollector >= 1.2.0
Requires:       python3-oslo.config >= 5.2.0
Requires:       python3-oslo.serialization >= 2.18.0
Requires:       python3-pytz >= 2013.6
Requires:       python3-six >= 1.10.0

%description -n python3-pycadf
DMTF Cloud Audit (CADF) data model

This package contains the Python 3.x module.

%package -n python-pycadf-doc
Summary:        Documentation for the DMTF Cloud Audit (CADF) data model
Group:          Development/Languages/Python
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-sphinxcontrib-apidoc

%description -n python-pycadf-doc
Documentation for the DMTF Cloud Audit (CADF) data model.

%package -n python-pycadf-common
Summary:        Common files for the DMTF Cloud Audit (CADF) data model
Group:          Development/Languages/Python

%description -n python-pycadf-common
Configuration files for the DMTF Cloud Audit (CADF) data model.

%prep
%autosetup -n pycadf-3.1.1
%py_req_cleanup

%build
%{py3_build}

# generate html docs
PBR_VERSION=3.1.1 %sphinx_build -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%{py3_install}
# FIXME: pbr/wheel bug installing onfiguration files in /usr/etc
mkdir -p %{buildroot}/%{_sysconfdir}
mv %{buildroot}%{_prefix}%{_sysconfdir}/pycadf %{buildroot}/%{_sysconfdir}/

%check
python3 -m stestr.cli run

%files -n python3-pycadf
%doc README.rst
%license LICENSE
%{python3_sitelib}/pycadf
%{python3_sitelib}/pycadf-*-py?.?.egg-info

%files -n python-pycadf-common
%license LICENSE
%dir %{_sysconfdir}/pycadf
%config(noreplace) %{_sysconfdir}/pycadf/*.conf

%files -n python-pycadf-doc
%license LICENSE
%doc doc/build/html

%changelog
