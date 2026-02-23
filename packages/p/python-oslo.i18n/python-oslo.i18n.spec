#
# spec file for package python-oslo.i18n
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Version:        6.7.2
Release:        0
Summary:        OpenStack i18n library
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/oslo.i18n
Source0:        https://files.pythonhosted.org/packages/source/o/oslo_i18n/oslo_i18n-%{version}.tar.gz
BuildRequires:  %{python_module oslotest}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module stestr}
BuildRequires:  %{python_module testscenarios}
BuildRequires:  %{python_module wheel}
BuildRequires:  openstack-macros
BuildArch:      noarch
%if "python%{python_nodots_ver}" == "%{primary_python}"
Obsoletes:      python3-oslo.i18n < %{version}
%endif
%python_subpackages

%description
The oslo.i18n library contain utilities for working with internationalization
(i18n) features, especially translation for text strings in an application
or library.

%package -n python-oslo.i18n-doc
Summary:        Documentation for OpenStack i18n library
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-sphinxcontrib-apidoc

%description -n python-oslo.i18n-doc
Documentation for the oslo.i18n library.

%prep
%autosetup -p1 -n oslo_i18n-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

# generate html docs
PBR_VERSION=%{version} %{sphinx_build} -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%check
%{openstack_stestr_run}

%files %{python_files}
%license LICENSE
%{python_sitelib}/oslo_i18n
%{python_sitelib}/oslo_i18n-%{version}.dist-info

%files -n python-oslo.i18n-doc
%doc doc/build/html ChangeLog CONTRIBUTING.rst README.rst
%license LICENSE

%changelog
