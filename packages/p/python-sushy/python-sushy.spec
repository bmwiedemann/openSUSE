#
# spec file for package python-sushy
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


Name:           python-sushy
Version:        5.8.0
Release:        0
Summary:        Python library to communicate with Redfish based systems
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/sushy
Source0:        https://files.pythonhosted.org/packages/source/s/sushy/sushy-%{version}.tar.gz
BuildRequires:  %{python_module oslotest}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil >= 2.7.0}
BuildRequires:  %{python_module requests >= 2.14.2}
BuildRequires:  %{python_module stevedore >= 1.29.0}
BuildRequires:  %{python_module wheel}
Requires:       python-python-dateutil >= 2.7.0
Requires:       python-requests >= 2.14.2
Requires:       python-stevedore >= 1.29.0
BuildArch:      noarch
%python_subpackages

%description
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
%autosetup -p1 -n sushy-%{version}

%build
%pyproject_wheel
PBR_VERSION=%{version} sphinx-build -b html doc/source doc/build/html
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%pyproject_install

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/sushy
%{python_sitelib}/sushy-%{version}.dist-info

%files -n python-sushy-doc
%doc doc/build/html
%license LICENSE

%changelog
