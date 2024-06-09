#
# spec file for package python-glean
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-glean
Version:        1.24.0
Release:        0
Summary:        Program to write static config from config-drive
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://opendev.org/opendev/glean
Source:         https://files.pythonhosted.org/packages/source/g/glean/glean-%{version}.tar.gz
BuildRequires:  %{python_module pbr}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
# The OpenStack package oslotest is only available for the primary python3 flavor on TW.
# On Leap (backports at least), the python2 package conflicts with the python3 package.
BuildRequires:  python3-oslotest >= 1.1.0.0a1
BuildRequires:  python3-python-subunit
BuildRequires:  python3-testrepository >= 0.0.18
BuildRequires:  python3-testscenarios >= 0.4
BuildRequires:  python3-testtools >= 0.9.34
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
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/glean
%python_clone -a %{buildroot}%{_bindir}/glean-install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# only test the primary python3 flavor
export PYTHON=%{_bindir}/python3
python3 setup.py testr

%post
%python_install_alternative glean glean-install

%postun
%python_uninstall_alternative glean glean-install

%files %{python_files}
%doc AUTHORS ChangeLog README.rst
%license LICENSE
%python_alternative %{_bindir}/glean
%python_alternative %{_bindir}/glean-install
%{python_sitelib}/glean
%{python_sitelib}/glean-%{version}.dist-info

%changelog
