#
# spec file for package python-pycadf
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


%global oldpython python
Name:           python-pycadf
Version:        2.9.0
Release:        0
Summary:        DMTF Cloud Audit (CADF) data model
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/pycadf
Source0:        https://files.pythonhosted.org/packages/source/p/pycadf/pycadf-2.9.0.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python2-fixtures
BuildRequires:  python2-oslo.config >= 5.2.0
BuildRequires:  python2-oslo.serialization >= 2.18.0
BuildRequires:  python2-oslotest
BuildRequires:  python2-pbr
BuildRequires:  python2-setuptools
BuildRequires:  python2-stestr
BuildRequires:  python2-testscenarios
BuildRequires:  python2-testtools
BuildRequires:  python3-fixtures
BuildRequires:  python3-oslo.config >= 5.2.0
BuildRequires:  python3-oslo.serialization >= 2.18.0
BuildRequires:  python3-oslotest
BuildRequires:  python3-pbr
BuildRequires:  python3-setuptools
BuildRequires:  python3-stestr
BuildRequires:  python3-testscenarios
BuildRequires:  python3-testtools
Requires:       %{oldpython}-pycadf-common
Requires:       python-debtcollector >= 1.2.0
Requires:       python-oslo.config >= 5.2.0
Requires:       python-oslo.serialization >= 2.18.0
Requires:       python-pytz >= 2013.6
Requires:       python-six >= 1.10.0
BuildArch:      noarch
%python_subpackages

%description
DMTF Cloud Audit (CADF) data model

%package -n python-pycadf-doc
Summary:        Documentation for the DMTF Cloud Audit (CADF) data model
Group:          Development/Languages/Python
BuildRequires:  python-Sphinx
BuildRequires:  python-openstackdocstheme

%description -n python-pycadf-doc
Documentation for the DMTF Cloud Audit (CADF) data model.

%package -n python-pycadf-common
Summary:        Common files for the DMTF Cloud Audit (CADF) data model
Group:          Development/Languages/Python

%description -n python-pycadf-common
Configuration files for the DMTF Cloud Audit (CADF) data model.

%prep
%autosetup -n pycadf-2.9.0
sed -i 's/^warning-is-error.*/warning-is-error = 0/g' setup.cfg
%py_req_cleanup

%build
%{python_build}

# generate html docs
%{__python2} setup.py build_sphinx
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%{python_install}
# FIXME: pbr/wheel bug installing onfiguration files in /usr/etc
mkdir -p %{buildroot}/%{_sysconfdir}
mv %{buildroot}%{_prefix}%{_sysconfdir}/pycadf %{buildroot}/%{_sysconfdir}/

%check
%python_exec -m stestr.cli run

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/pycadf
%{python_sitelib}/pycadf-*-py?.?.egg-info

%files -n python-pycadf-common
%license LICENSE
%dir %{_sysconfdir}/pycadf
%config(noreplace) %{_sysconfdir}/pycadf/*.conf

%files -n python-pycadf-doc
%license LICENSE
%doc doc/build/html

%changelog
