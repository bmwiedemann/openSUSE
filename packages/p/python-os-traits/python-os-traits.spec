#
# spec file for package python-os-traits
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


Name:           python-os-traits
Version:        3.6.0
Release:        0
Summary:        Library containing standardized trait strings.
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/os-traits
Source0:        https://files.pythonhosted.org/packages/source/o/os_traits/os_traits-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module oslotest}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module python-subunit}
BuildRequires:  %{python_module stestr}
BuildRequires:  %{python_module testscenarios}
BuildRequires:  %{python_module testtools}
BuildRequires:  %{python_module wheel}
BuildRequires:  openstack-macros
Requires:       python-pbr
Requires:       python-six
BuildArch:      noarch
%python_subpackages

%description
Traits are strings that represent a feature of some resource provider.  This
library contains the catalog of constants that have been standardized in the
OpenStack community to refer to a particular hardware, virtualization, storage,
network, or device trait.

%package -n python3-os-traits-doc
Summary:        Documentation for OpenStack traits Library
Group:          Documentation/HTML
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme

%description -n python3-os-traits-doc
Traits are strings that represent a feature of some resource provider.  This
library contains the catalog of constants that have been standardized in the
OpenStack community to refer to a particular hardware, virtualization, storage,
network, or device trait.

This package contains the documentation.

%prep
%autosetup -p1 -n os_traits-%{version}

%build
%pyproject_wheel

PYTHONPATH=. PBR_VERSION=%{version} %{sphinx_build} -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%pyproject_install

%check
%{openstack_stestr_run}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/os_traits
%{python_sitelib}/os_traits-%{version}.dist-info

%files -n python3-os-traits-doc
%doc doc/build/html
%license LICENSE

%changelog
