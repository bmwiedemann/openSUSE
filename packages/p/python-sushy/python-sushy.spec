#
# spec file for package python-sushy
#
# Copyright (c) 2024 SUSE LLC
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


Name:           python-sushy
Version:        5.1.0
Release:        0
Summary:        Python library to communicate with Redfish based systems
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/sushy
Source0:        https://files.pythonhosted.org/packages/source/s/sushy/sushy-5.1.0.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python3-oslotest
BuildRequires:  python3-pbr >= 2.0.0
BuildRequires:  python3-python-dateutil >= 2.7.0
BuildRequires:  python3-python-subunit
BuildRequires:  python3-reno
BuildRequires:  python3-requests >= 2.14.2
BuildRequires:  python3-stestr
BuildRequires:  python3-stevedore >= 1.29.0
BuildRequires:  python3-testscenarios
BuildRequires:  python3-testtools
BuildArch:      noarch

%description
Sushy is a Python library to communicate with `Redfish` based systems.

%package -n python3-sushy
Summary:        Python library to communicate with Redfish based systems
Requires:       python3-pbr >= 2.0.0
Requires:       python3-python-dateutil >= 2.7.0
Requires:       python3-requests >= 2.14.2
Requires:       python3-stevedore >= 1.29.0

%description -n python3-sushy
Sushy is a Python library to communicate with `Redfish` based systems.

%package -n python-sushy-doc
Summary:        Documentation for OpenStack sushy
Group:          Documentation/HTML
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-sphinxcontrib-apidoc

%description -n python-sushy-doc
Sushy is a Python library to communicate with `Redfish` based systems.
This package contains the documentation.

%prep
%autosetup -p1 -n sushy-5.1.0
%py_req_cleanup

%build
%{py3_build}
PBR_VERSION=%{version} %sphinx_build -b html doc/source doc/build/html
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%{py3_install}

%check
%{openstack_stestr_run}

%files -n python3-sushy
%license LICENSE
%doc AUTHORS ChangeLog README.rst
%{python3_sitelib}/sushy*
%{python3_sitelib}/*.egg-info

%files -n python-sushy-doc
%doc doc/build/html
%license LICENSE

%changelog
