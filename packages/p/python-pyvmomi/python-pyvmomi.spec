#
# spec file for package python-pyvmomi
#
# Copyright (c) 2025 SUSE LLC
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


%{?sle15_python_module_pythons}
Name:           python-pyvmomi
Version:        9.0.0.0
Release:        0
Summary:        VMware vSphere Python SDK
License:        Apache-2.0
URL:            https://github.com/vmware/pyvmomi
Source:         https://github.com/vmware/pyvmomi/archive/v%{version}.tar.gz#/pyvmomi-%{version}.tar.gz
#Patch0:         0001-pyVmomi-pinned-certificates-support.patch
BuildRequires:  %{python_module fixtures >= 1.3.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module requests >= 2.3.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module testtools >= 0.9.34}
BuildRequires:  %{python_module vcrpy}
# /SECTION
Requires:       python-requests >= 2.3.0
Recommends:     python-lxml
Recommends:     python-pyOpenSSL < 24.3.0
BuildArch:      noarch
%python_subpackages

%description
pyVmomi is the Python SDK for the VMware vSphere API that allows you to manage
ESX, ESXi, and vCenter.

%prep
%autosetup -p1 -n pyvmomi-%{version}%{?version_suffix}
dos2unix README.rst LICENSE.txt NOTICE.txt

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
rm tests/test_json.py
rm tests/test_connect.py
rm tests/test_pbm_check_compatibility.py
%pyunittest discover -v

%files %{python_files}
%license LICENSE.txt
%doc NOTICE.txt README.rst
%{python_sitelib}/pyVim
%{python_sitelib}/pyVmomi
%{python_sitelib}/vsanapiutils.py
%{python_sitelib}/vsanmgmtObjects.py
%{python_sitelib}/pyvmomi-%{version}.dist-info
%pycache_only %{python_sitelib}/__pycache__

%changelog
