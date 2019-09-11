#
# spec file for package python-castellan
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


Name:           python-castellan
Version:        1.2.2
Release:        0
Summary:        Generic Key Manager interface for OpenStack
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/castellan
Source0:        https://files.pythonhosted.org/packages/source/c/castellan/castellan-1.2.2.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python2-barbicanclient >= 4.5.2
BuildRequires:  python2-cryptography >= 2.1
BuildRequires:  python2-keystoneauth1 >= 3.4.0
BuildRequires:  python2-oslo.config >= 6.4.0
BuildRequires:  python2-oslo.log >= 3.36.0
BuildRequires:  python2-oslotest
BuildRequires:  python2-pifpaf
BuildRequires:  python2-python-subunit
BuildRequires:  python2-reno
BuildRequires:  python2-setuptools
BuildRequires:  python2-stestr
BuildRequires:  python2-testscenarios
BuildRequires:  python2-testtools
BuildRequires:  python3-barbicanclient >= 4.5.2
BuildRequires:  python3-cryptography >= 2.1
BuildRequires:  python3-keystoneauth1 >= 3.4.0
BuildRequires:  python3-oslo.config >= 6.4.0
BuildRequires:  python3-oslo.log >= 3.36.0
BuildRequires:  python3-oslotest
BuildRequires:  python3-pifpaf
BuildRequires:  python3-python-subunit
BuildRequires:  python3-reno
BuildRequires:  python3-setuptools
BuildRequires:  python3-stestr
BuildRequires:  python3-testscenarios
BuildRequires:  python3-testtools
Requires:       python-Babel >= 2.3.4
Requires:       python-barbicanclient >= 4.5.2
Requires:       python-cryptography >= 2.1
Requires:       python-keystoneauth1 >= 3.4.0
Requires:       python-oslo.config >= 6.4.0
Requires:       python-oslo.context >= 2.19.2
Requires:       python-oslo.i18n >= 3.15.3
Requires:       python-oslo.log >= 3.36.0
Requires:       python-oslo.utils >= 3.33.0
Requires:       python-stevedore >= 1.20.0
BuildArch:      noarch
%python_subpackages

%description
Generic Key Manager interface for OpenStack.

%package -n python-castellan-doc
Summary:        Documentation for castellan
Group:          Documentation/HTML
BuildRequires:  python-Sphinx
BuildRequires:  python-openstackdocstheme

%description -n python-castellan-doc
Castellan is a generic Key Manager interface for OpenStack.
This package contains the documentation

%prep
%autosetup -p1 -n castellan-1.2.2
%py_req_cleanup

%build
%{python_build}
# generate html docs
%{__python2} setup.py build_sphinx
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%{python_install}

%check
%python_exec -m stestr.cli run

%files %{python_files}
%license LICENSE
%{python_sitelib}/castellan
%{python_sitelib}/*.egg-info

%files -n python-castellan-doc
%license LICENSE
%doc README.rst doc/build/html

%changelog
