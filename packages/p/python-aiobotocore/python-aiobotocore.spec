#
# spec file for package python-aiobotocore
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
%define         skip_python2 1
Name:           python-aiobotocore
Version:        1.1.1
Release:        0
Summary:        Async client for aws services
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/aio-libs/aiobotocore
Source:         https://files.pythonhosted.org/packages/source/a/aiobotocore/aiobotocore-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module aiohttp >= 3.3.1}
BuildRequires:  %{python_module aioitertools >= 0.5.1}
BuildRequires:  %{python_module botocore >= 1.17.44}
BuildRequires:  %{python_module wrapt >= 1.10.10}
# /SECTION
Requires:       python-aiohttp >= 3.3.1
Requires:       python-async_generator >= 1.10
Requires:       python-botocore >= 1.17.44
Requires:       python-wrapt >= 1.10.10
Recommends:     awscli >= 1.18.121
Recommends:     python-boto3 >= 1.14.44
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
%doc CHANGES.rst README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
