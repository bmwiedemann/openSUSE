#
# spec file for package python-aiobotocore
#
# Copyright (c) 2022 SUSE LLC
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
Name:           python-aiobotocore
Version:        2.3.4
Release:        0
Summary:        Async client for aws services
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/aio-libs/aiobotocore
Source:         https://github.com/aio-libs/aiobotocore/archive/refs/tags/%{version}.tar.gz#/aiobotocore-%{version}-gh.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module Flask-Cors}
BuildRequires:  %{python_module Flask}
BuildRequires:  %{python_module aiohttp >= 3.3.1}
BuildRequires:  %{python_module aioitertools >= 0.5.1}
BuildRequires:  %{python_module botocore >= 1.24.21}
BuildRequires:  %{python_module dill}
BuildRequires:  %{python_module docker}
BuildRequires:  %{python_module docutils}
BuildRequires:  %{python_module moto-all}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wrapt >= 1.10.10}
%if 0%{?suse_version} < 1550
BuildRequires:  %{python_module async_generator}
%endif
# /SECTION
Requires:       python-aiohttp >= 3.3.1
Requires:       python-aioitertools >= 0.5.1
Requires:       python-botocore >= 1.24.21
Requires:       python-wrapt >= 1.10.10
%if 0%{?python_version_nodots} < 37
Requires:       python-async_generator
%endif
Recommends:     aws-cli >= 1.22.76
Recommends:     python-boto3 >= 1.21.21
BuildArch:      noarch

%python_subpackages

%description
Async Python client for aws services.

%prep
%setup -q -n aiobotocore-%{version}
# unpin and hope for the best
sed -E 's/(botocore>=.*),<[0-9.]*/\1/' -i setup.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# import tests from local dir
export PYTHONPATH=":x"
export BOTO_CONFIG=/dev/null
# different versions, different digest hash
donttest="test_patches or test_version"
# docker image not successful
donttest+=" or test_run_lambda"
# no connection to httpbin.org
donttest+=" or test_publish_to_http"
# no awslambda dynamodb backend in mock available
donttest+=" or test_dynamodb"
# s3client fails with KeyError for resp['Contents'] -- https://github.com/spulec/moto/issues/5030
donttest+=" or test_can_delete_urlencoded_object"
# fail to fetch fake AWS credentials https://github.com/aio-libs/aiobotocore/issues/948
donttest+=" or (test_credentials and (sso or test_required_config_not_set))"

%pytest -m moto -n auto -k "not ($donttest)"

%files %{python_files}
%doc CHANGES.rst README.rst
%license LICENSE
%{python_sitelib}/aiobotocore
%{python_sitelib}/aiobotocore-%{version}*-info

%changelog
