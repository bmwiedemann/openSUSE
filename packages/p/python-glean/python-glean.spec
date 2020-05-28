#
# spec file for package python-glean
#
# Copyright (c) 2020 SUSE LLC
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-glean
Version:        1.15.0
Release:        0
Summary:        Program to write static config from config-drive
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://www.openstack.org/
Source:         https://files.pythonhosted.org/packages/source/g/glean/glean-%{version}.tar.gz
BuildRequires:  %{python_module pbr}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Sphinx >= 1.1.2}
BuildRequires:  %{python_module mock >= 1.0}
BuildRequires:  %{python_module oslosphinx}
BuildRequires:  %{python_module oslotest >= 1.1.0.0a1}
BuildRequires:  %{python_module python-subunit}
BuildRequires:  %{python_module testrepository >= 0.0.18}
BuildRequires:  %{python_module testscenarios >= 0.4}
BuildRequires:  %{python_module testtools >= 0.9.34}
# /SECTION
%python_subpackages

%description
Glean is a program intended to configure a system based on configuration
provided in a configuration drive.
Different cloud providers have different ways of providing networking and
other configuration to guest virtual-machines. Many use DHCP but others,
notably Rackspace, use configuration provided via a configuration drive.

%prep
%setup -q -n glean-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/glean-install
%python_clone -a %{buildroot}%{_bindir}/glean
%python_clone -a %{buildroot}%{_bindir}/glean.sh
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%{python_expand rm -rf .testrepository
export PYTHON=$python
$python setup.py test
}

%post
%python_install_alternative glean-install
%python_install_alternative glean
%python_install_alternative glean.sh

%postun
%python_uninstall_alternative glean-install
%python_uninstall_alternative glean
%python_uninstall_alternative glean.sh

%files %{python_files}
%doc AUTHORS ChangeLog README.rst
%license LICENSE
%python_alternative %{_bindir}/glean.sh
%python_alternative %{_bindir}/glean
%python_alternative %{_bindir}/glean-install
%{python_sitelib}/*

%changelog
