#
# spec file for package python-pyvmomi
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2014 LISA GmbH, Bingen, Germany.
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
Name:           python-pyvmomi
Version:        7.0.1
Release:        0
Summary:        VMware vSphere Python SDK
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/vmware/pyvmomi
Source:         https://github.com/vmware/pyvmomi/archive/v%{version}.tar.gz#/pyvmomi-%{version}.tar.gz
BuildRequires:  %{python_module fixtures >= 1.3.0}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module requests >= 2.3.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six >= 1.7.3}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module testtools >= 0.9.34}
BuildRequires:  %{python_module tox}
BuildRequires:  %{python_module vcrpy}
# /SECTION
Requires:       python-requests >= 2.3.0
Requires:       python-six >= 1.7.3
Recommends:     python-pyOpenSSL
Recommends:     python-lxml
BuildArch:      noarch
%python_subpackages

%description
pyVmomi is the Python SDK for the VMware vSphere API that allows you to manage
ESX, ESXi, and vCenter.

%prep
%setup -q -n pyvmomi-%{version}%{?version_suffix}
dos2unix README.rst LICENSE.txt NOTICE.txt

# https://github.com/vmware/pyvmomi/pull/750
# Unpin vcrpy; the fix was released
sed -i 's/vcrpy<2/vcrpy/' test-requirements.txt

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%license LICENSE.txt
%doc NOTICE.txt README.rst
%{python_sitelib}/pyVim
%{python_sitelib}/pyVmomi
%{python_sitelib}/pyvmomi-%{version}*-py*.egg-info

%changelog
