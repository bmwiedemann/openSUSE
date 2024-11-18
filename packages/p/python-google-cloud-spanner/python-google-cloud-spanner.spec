#
# spec file for package python-google-cloud-spanner
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif

%{?sle15_python_module_pythons}
Name:           python-google-cloud-spanner%{psuffix}
Version:        3.50.1
Release:        0
Summary:        Google Cloud Spanner API client library
License:        Apache-2.0
URL:            https://github.com/googleapis/python-spanner
Source:         https://files.pythonhosted.org/packages/source/g/google_cloud_spanner/google_cloud_spanner-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
%if %{with test}
BuildRequires:  %{python_module google-cloud-spanner = %{version}}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest}
%endif
# /SECTION
BuildRequires:  fdupes
Requires:       python-google-api-core >= 1.34.0
Requires:       python-google-cloud-core >= 1.4.4
Requires:       python-grpc-google-iam-v1 >= 0.12.4
Requires:       python-grpc-interceptor >= 0.15.4
Requires:       python-proto-plus >= 1.22.0
Requires:       python-protobuf >= 3.20.2
Requires:       python-sqlparse >= 0.4.4
Suggests:       python-libcst >= 0.2.5
Suggests:       python-opentelemetry-api >= 1.22.0
Suggests:       python-opentelemetry-sdk >= 1.22.0
Suggests:       python-opentelemetry-instrumentation >= 0.20b0
BuildArch:      noarch
%python_subpackages

%description
Google Cloud Spanner API client library

%prep
%autosetup -p1 -n google_cloud_spanner-%{version}

# don't use python-mock
for i in $(find tests -name "*.py")
do
  sed -i 's/^import mock/from unittest import mock/g' $i
done

%build
%pyproject_wheel

%install
%if %{without test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
mkdir -p $HOME/.config/gcloud
cat > $HOME/.config/gcloud/application_default_credentials.json <<EOF
{
  "client_id": "111111111111-1qq1q1qq1qqq111qq1qqqq11q1qqqqqq.apps.googleusercontent.com",
  "client_secret": "d-XXXXXXXXXXXXXXXXXXXXXX",
  "refresh_token": "1//1111111111111111111111111111-XXXXXXXXX-AAAAAAAAAAA_BBBBBBBBBBBBBBBBBBBBBB-CCCCCCCCCCCCCCCCCCCCCCCCCC",
  "type": "authorized_user"
}
EOF
export GOOGLE_CLOUD_PROJECT="PROJECT"
%pytest -x tests/unit
%endif

%if %{without test}
%files %{python_files}
%doc README.rst
%license LICENSE
%pycache_only %{python_sitelib}/google/cloud/__pycache__
%dir %{python_sitelib}/google
%dir %{python_sitelib}/google/cloud
%{python_sitelib}/google/cloud/spanner*
%{python_sitelib}/google_cloud_spanner-%{version}.dist-info
%endif

%changelog
