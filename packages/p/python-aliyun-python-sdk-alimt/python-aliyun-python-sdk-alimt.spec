#
# spec file for package python-aliyun-python-sdk-alimt
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
Name:           python-aliyun-python-sdk-alimt
Version:        3.2.0
Release:        0
Summary:        The alimt module of Aliyun Python SDK
License:        Apache-2.0
URL:            http://develop.aliyun.com/sdk/python
Source:         https://files.pythonhosted.org/packages/source/a/aliyun-python-sdk-alimt/aliyun-python-sdk-alimt-%{version}.tar.gz
Source1:        ChangeLog.txt
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module aliyun-python-sdk-core >= 2.11.5}
# /SECTION
BuildRequires:  fdupes
Requires:       python-aliyun-python-sdk-core >= 2.11.5
%if 0%{?sle_version} >= 150400
Obsoletes:      python3-aliyun-python-sdk-alimt < 3.2.0
%endif
BuildArch:      noarch
%python_subpackages

%description
The alimt module of Aliyun Python SDK.

%prep
%setup -q -n aliyun-python-sdk-alimt-%{version}
cp %{SOURCE1} ChangeLog.txt

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc ChangeLog.txt README.rst
%license LICENSE
%{python_sitelib}/aliyunsdkalimt
%{python_sitelib}/aliyun_python_sdk_alimt-%{version}.dist-info

%changelog
