#
# spec file for package python-pyvmomi
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%bcond_without test
Name:           python-pyvmomi
Version:        6.7.1.2018.12
Release:        0
Summary:        VMware vSphere Python SDK
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/vmware/pyvmomi
Source:         https://github.com/vmware/pyvmomi/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         python-pyvmomi-fix-incompatibility-with-vcrpy2.patch
BuildRequires:  %{python_module fixtures >= 1.3.0}
BuildRequires:  %{python_module requests >= 2.3.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six >= 1.7.3}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-requests >= 2.3.0
Requires:       python-six >= 1.7.3
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module testtools >= 0.9.34}
BuildRequires:  %{python_module tox}
BuildRequires:  %{python_module vcrpy}
%endif
%python_subpackages

%description
pyVmomi is the Python SDK for the VMware vSphere API that allows you to manage
ESX, ESXi, and vCenter.

%prep
%setup -q -n pyvmomi-%{version}%{?version_suffix}
%patch0 -p1
# we don't want to install any of these
sed -i '/   data_files/,+1d' setup.py
# fix line breaks in text files
sed -i 's/\r//' *.txt
# do not hardcode vrcpy version
#sed -i -e 's:==:>=:g' test-requirements.txt

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with test}
%check
%python_exec setup.py test
%endif

%files %{python_files}
%license LICENSE.txt
%doc NOTICE.txt README.rst
%{python_sitelib}/pyVim
%{python_sitelib}/pyVmomi
%{python_sitelib}/pyvmomi-%{version}*-py%{py_ver}.egg-info

%changelog
