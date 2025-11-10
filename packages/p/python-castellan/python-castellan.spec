#
# spec file for package python-castellan
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
Name:           python-castellan
Version:        5.4.1
Release:        0
Summary:        Generic Key Manager interface for OpenStack
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/castellan
Source0:        https://files.pythonhosted.org/packages/source/c/castellan/castellan-%{version}.tar.gz
BuildRequires:  %{python_module barbicanclient >= 5.5.0}
BuildRequires:  %{python_module cryptography >= 2.7}
BuildRequires:  %{python_module keystoneauth1 >= 3.4.0}
BuildRequires:  %{python_module oslo.config >= 6.4.0}
BuildRequires:  %{python_module oslo.log >= 3.36.0}
BuildRequires:  %{python_module oslotest}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module requests >= 2.18.0}
BuildRequires:  %{python_module requests-mock}
BuildRequires:  %{python_module stestr}
BuildRequires:  %{python_module testscenarios}
BuildRequires:  %{python_module testtools}
BuildRequires:  %{python_module wheel}
BuildRequires:  openstack-macros
Requires:       python-Babel
Requires:       python-barbicanclient >= 5.5.0
Requires:       python-cryptography >= 2.7
Requires:       python-keystoneauth1 >= 3.4.0
Requires:       python-oslo.config >= 6.4.0
Requires:       python-oslo.context >= 2.19.2
Requires:       python-oslo.i18n >= 3.15.3
Requires:       python-oslo.log >= 3.36.0
Requires:       python-oslo.utils >= 3.33.0
Requires:       python-requests >= 2.18.0
Requires:       python-stevedore >= 1.20.0
BuildArch:      noarch
%python_subpackages

%description
Generic Key Manager interface for OpenStack.

%package -n python3-castellan-doc
Summary:        Documentation for castellan
Group:          Documentation/HTML
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-sphinxcontrib-svg2pdfconverter

%description -n python3-castellan-doc
Castellan is a generic Key Manager interface for OpenStack.
This package contains the documentation

%prep
%autosetup -p1 -n castellan-%{version}

%build
%pyproject_wheel

# generate html docs
PBR_VERSION=%{version} %sphinx_build -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%pyproject_install

%check
%{openstack_stestr_run}

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/castellan
%{python_sitelib}/castellan-%{version}.dist-info

%files -n python3-castellan-doc
%license LICENSE
%doc README.rst doc/build/html

%changelog
