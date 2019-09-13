#
# spec file for package python-aiobotocore
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         skip_python2 1
Name:           python-aiobotocore
Version:        0.10.0
Release:        0
License:        Apache-2.0
Summary:        Async client for aws services
Url:            https://github.com/aio-libs/aiobotocore
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/a/aiobotocore/aiobotocore-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
# SECTION test requirements
BuildRequires:  %{python_module aiohttp >= 3.3.1}
BuildRequires:  %{python_module botocore >= 1.12.49}
BuildRequires:  %{python_module wrapt >= 1.10.10}
# /SECTION
Requires:       python-aiohttp >= 3.3.1
Requires:       python-botocore >= 1.12.49
Requires:       python-wrapt >= 1.10.10
Recommends:     python-awscli >= 1.16.59
Recommends:     python-boto3 >= 1.9.49
BuildArch:      noarch

%python_subpackages

%description
Async Python client for aws services.

%prep
%setup -q -n aiobotocore-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc CHANGES.txt README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
