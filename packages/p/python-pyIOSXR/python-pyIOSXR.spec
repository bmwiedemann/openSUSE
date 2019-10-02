#
# spec file for package python-pyIOSXR
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2017, Martin Hauke <mardnh@gmx.de>
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
Name:           python-pyIOSXR
Version:        0.53
Release:        0
Summary:        Python API to interact with network devices running IOS-XR
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/fooelisa/pyiosxr/
Source:         https://github.com/fooelisa/pyiosxr/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module lxml >= 3.2.4}
BuildRequires:  %{python_module netmiko >= 1.4.1}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-lxml >= 3.2.4
Requires:       python-netmiko >= 1.4.1
BuildArch:      noarch
%python_subpackages

%description
pyIOSXR is a Python library that facilitates communication with Cisco
devices running IOS-XR through the XML agent.

%prep
%setup -q -n pyiosxr-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python test/test.py

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/*

%changelog
