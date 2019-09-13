#
# spec file for package python-sushy
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


Name:           python-sushy
Version:        1.8.1
Release:        0
Summary:        Python library to communicate with Redfish based systems
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/sushy
Source0:        https://files.pythonhosted.org/packages/source/s/sushy/sushy-1.8.1.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python2-oslotest
BuildRequires:  python2-pbr >= 2.0.0
BuildRequires:  python2-python-dateutil >= 2.7.0
BuildRequires:  python2-python-subunit
BuildRequires:  python2-reno
BuildRequires:  python2-requests >= 2.14.2
BuildRequires:  python2-setuptools
BuildRequires:  python2-six >= 1.10.0
BuildRequires:  python2-stestr
BuildRequires:  python2-testscenarios
BuildRequires:  python2-testtools
BuildRequires:  python3-oslotest
BuildRequires:  python3-pbr >= 2.0.0
BuildRequires:  python3-python-dateutil >= 2.7.0
BuildRequires:  python3-python-subunit
BuildRequires:  python3-reno
BuildRequires:  python3-requests >= 2.14.2
BuildRequires:  python3-setuptools
BuildRequires:  python3-six >= 1.10.0
BuildRequires:  python3-stestr
BuildRequires:  python3-testscenarios
BuildRequires:  python3-testtools
Requires:       python-pbr >= 2.0.0
Requires:       python-python-dateutil >= 2.7.0
Requires:       python-requests >= 2.14.2
Requires:       python-six >= 1.10.0
BuildArch:      noarch
%python_subpackages

%description
Sushy is a Python library to communicate with `Redfish` based systems.

%package -n python-sushy-doc
Summary:        Documentation for OpenStack sushy
Group:          Documentation/HTML
BuildRequires:  python-Sphinx
BuildRequires:  python-openstackdocstheme

%description -n python-sushy-doc
Sushy is a Python library to communicate with `Redfish` based systems.
This package contains the documentation.

%prep
%autosetup -p1 -n sushy-1.8.1
%py_req_cleanup
sed -i 's/^warning-is-error.*/warning-is-error = 0/g' setup.cfg

%build
%{python_build}
%{__python2} setup.py build_sphinx --builder=html,man
rm -rf html/.{doctrees,buildinfo}

%install
%{python_install}

%check
%python_exec -m stestr.cli run

%files %{python_files}
%license LICENSE
%doc AUTHORS ChangeLog README.rst
%{python_sitelib}/sushy*
%{python_sitelib}/*.egg-info

%files -n python-sushy-doc
%doc doc/build/html
%license LICENSE

%changelog
