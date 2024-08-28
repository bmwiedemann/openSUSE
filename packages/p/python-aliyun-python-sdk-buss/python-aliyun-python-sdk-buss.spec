#
# spec file for package python-aliyun-python-sdk-buss
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


%{?sle15_python_module_pythons}
Name:           python-aliyun-python-sdk-buss
Version:        1.0.0
Release:        0
Summary:        The buss module of Aliyun Python SDK
License:        Apache-2.0
URL:            http://develop.aliyun.com/sdk/python
Source:         https://files.pythonhosted.org/packages/source/a/aliyun-python-sdk-buss/aliyun-python-sdk-buss-%{version}.tar.gz
Source1:        ChangeLog.txt
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module aliyun-python-sdk-core >= 2.11.5}
BuildRequires:  fdupes
Requires:       python-aliyun-python-sdk-core >= 2.11.5
BuildArch:      noarch
%python_subpackages

%description
The buss module of Aliyun Python SDK.

%prep
%autosetup -p1 -n aliyun-python-sdk-buss-%{version}
cp %{SOURCE1} ChangeLog.txt

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc ChangeLog.txt README.rst
%license LICENSE
%{python_sitelib}/aliyunsdkbuss
%{python_sitelib}/aliyun_python_sdk_buss-%{version}.dist-info

%changelog
