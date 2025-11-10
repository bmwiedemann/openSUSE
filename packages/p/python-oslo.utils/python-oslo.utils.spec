#
# spec file for package python-oslo.utils
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


Name:           python-oslo.utils
Version:        9.1.0
Release:        0
Summary:        OpenStack Utils Library
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/oslo.utils
Source0:        https://files.pythonhosted.org/packages/source/o/oslo_utils/oslo_utils-%{version}.tar.gz
BuildRequires:  %{python_module Babel}
BuildRequires:  %{python_module ddt}
BuildRequires:  %{python_module debtcollector >= 1.2.0}
BuildRequires:  %{python_module eventlet}
BuildRequires:  %{python_module fixtures}
BuildRequires:  %{python_module iso8601 >= 0.1.11}
BuildRequires:  %{python_module netaddr >= 0.10.0}
BuildRequires:  %{python_module oslo.i18n >= 3.15.3}
BuildRequires:  %{python_module oslotest}
BuildRequires:  %{python_module pbr >= 6.1.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pyparsing >= 2.1.0}
BuildRequires:  %{python_module stestr}
BuildRequires:  %{python_module testscenarios}
BuildRequires:  %{python_module testtools}
BuildRequires:  %{python_module wheel}
BuildRequires:  openstack-macros
BuildRequires:  qemu-img
Requires:       python-PyYAML
Requires:       python-debtcollector >= 3.0.0
Requires:       python-iso8601 >= 0.1.11
Requires:       python-netaddr >= 0.10.0
Requires:       python-oslo.i18n >= 3.15.3
Requires:       python-psutil
Requires:       python-pyparsing >= 2.1.0
Requires:       python-tzdata
BuildArch:      noarch
%if "python%{python_nodots_ver}" == "%{primary_python}"
Obsoletes:      python3-oslo.utils < %{version}
%endif
%python_subpackages

%description
The oslo.utils library provides support for common utility type functions,
such as encoding, exception handling, string manipulation, and time handling.

%package -n python3-oslo.utils
Summary:        OpenStack Utils Library

%description -n python3-oslo.utils
The oslo.utils library provides support for common utility type functions,
such as encoding, exception handling, string manipulation, and time handling.

This package contains the Python 3.x module.

%package -n python-oslo.utils-doc
Summary:        Documentation for OpenStack utils library
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme

%description -n python-oslo.utils-doc
Documentation for OpenStack utils library.

%prep
%autosetup -p1 -n oslo_utils-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

# generate html docs
PBR_VERSION=%{version} %{sphinx_build} -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%check
%{openstack_stestr_run}  --exclude-regex test_is_valid_ip

%files %{python_files}
%license LICENSE
%doc ChangeLog README.rst
%{python_sitelib}/oslo_utils
%{python_sitelib}/oslo_utils-%{version}.dist-info

%files -n python-oslo.utils-doc
%doc doc/build/html
%license LICENSE

%changelog
