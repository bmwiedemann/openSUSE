#
# spec file for package python-aliyun-python-sdk-core
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
%if 0%{?suse_version} >= 1500
%define skip_python2 1
%endif
Name:           python-aliyun-python-sdk-core
Version:        2.15.0
Release:        0
Summary:        The core module of Aliyun Python SDK
License:        Apache-2.0
URL:            https://github.com/aliyun/aliyun-openapi-python-sdk
Source:         https://files.pythonhosted.org/packages/source/a/aliyun-python-sdk-core/aliyun-python-sdk-core-%{version}.tar.gz
Source1:        ChangeLog.txt
Patch1:         0001_Dont-use-vendored-dependencies.patch
Patch2:         0002_Relax-jmespath-version-constraint.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module cryptography >= 2.9.2}
BuildRequires:  %{python_module jmespath >= 0.9.3}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module six}
# /SECTION
BuildRequires:  fdupes
Requires:       python-cryptography >= 2.9.2
Requires:       python-jmespath >= 0.9.3
Requires:       python-requests
Requires:       python-six
BuildArch:      noarch
%python_subpackages

%description
The core module of Aliyun Python SDK.

%prep
%setup -q -n aliyun-python-sdk-core-%{version}
%patch1 -p1
%patch2 -p1
cp %{SOURCE1} ChangeLog.txt
rm -rf aliyunsdkcore/vendored

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc ChangeLog.txt README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
