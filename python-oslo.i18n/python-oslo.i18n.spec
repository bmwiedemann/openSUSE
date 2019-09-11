#
# spec file for package python-oslo.i18n
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


Name:           python-oslo.i18n
Version:        3.23.1
Release:        0
Summary:        OpenStack i18n library
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/oslo.i18n
Source0:        https://files.pythonhosted.org/packages/source/o/oslo.i18n/oslo.i18n-3.23.1.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python2-Babel >= 2.3.4
BuildRequires:  python2-mock
BuildRequires:  python2-oslotest
BuildRequires:  python2-pbr >= 2.0.0
BuildRequires:  python2-stestr
BuildRequires:  python2-testscenarios
BuildRequires:  python3-Babel >= 2.3.4
BuildRequires:  python3-mock
BuildRequires:  python3-oslotest
BuildRequires:  python3-pbr >= 2.0.0
BuildRequires:  python3-stestr
BuildRequires:  python3-testscenarios
Requires:       python-Babel >= 2.3.4
Requires:       python-six >= 1.10.0
BuildArch:      noarch
%python_subpackages

%description
The oslo.i18n library contain utilities for working with internationalization
(i18n) features, especially translation for text strings in an application
or library.

%package -n python-oslo.i18n-doc
Summary:        Documentation for OpenStack i18n library
Group:          Development/Languages/Python
BuildRequires:  python-Sphinx
BuildRequires:  python-openstackdocstheme

%description -n python-oslo.i18n-doc
Documentation for the oslo.i18n library.

%prep
%autosetup -p1 -n oslo.i18n-3.23.1
%py_req_cleanup

%build
%{python_build}

%install
%{python_install}

# generate html docs
%{__python2} setup.py build_sphinx
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%check
%python_exec -m stestr.cli run

%files %{python_files}
%license LICENSE
%{python_sitelib}/oslo_i18n
%{python_sitelib}/*egg-info

%files -n python-oslo.i18n-doc
%doc doc/build/html ChangeLog CONTRIBUTING.rst README.rst
%license LICENSE

%changelog
