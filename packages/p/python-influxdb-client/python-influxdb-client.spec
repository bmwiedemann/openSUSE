#
# spec file for package python-influxdb-client
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


Name:           python-influxdb-client
Version:        1.41.0
Release:        0
Summary:        InfluxDB 2.0 Python client library
License:        MIT
URL:            https://github.com/influxdata/influxdb-client-python
Source:         https://github.com/influxdata/influxdb-client-python/archive/refs/tags/v%{version}.tar.gz#/influxdb_client-%{version}-gh.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-certifi >= 14.05.14
Requires:       python-python-dateutil >= 2.5.3
Requires:       python-reactivex >= 4.0.4
Requires:       python-setuptools >= 21.0.0
Requires:       python-urllib3 >= 1.26.0
Suggests:       python-aiocsv >= 1.2.2
Suggests:       python-aiohttp >= 3.8.1
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module aiocsv >= 1.2.2}
BuildRequires:  %{python_module aiohttp >= 3.8.1}
BuildRequires:  %{python_module aioresponses >= 0.7.3}
BuildRequires:  %{python_module certifi >= 14.05.14}
BuildRequires:  %{python_module httpretty >= 1.0.5}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module pluggy >= 0.3.1}
BuildRequires:  %{python_module psutil >= 5.6.3}
BuildRequires:  %{python_module py >= 1.4.31}
BuildRequires:  %{python_module pytest >= 5.0.0}
BuildRequires:  %{python_module pytest-timeout >= 2.1.0}
BuildRequires:  %{python_module python-dateutil >= 2.5.3}
BuildRequires:  %{python_module reactivex >= 4.0.4}
BuildRequires:  %{python_module urllib3 >= 1.26.0}
BuildRequires:  curl
BuildRequires:  influxdb2
# /SECTION
%python_subpackages

%description
The Python client library for use with InfluxDB 2.x and Flux.
InfluxDB 3.x users should instead use the lightweight v3 client library.
InfluxDB 1.x users should use the v1 client library.

The API of the influxdb-client-python is not the backwards-compatible with
the old one - influxdb-python.

%prep
%autosetup -p1 -n influxdb-client-python-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# setup local influxdb server
export INFLUXD_HTTP_BIND_ADDRESS=":8086"
influxd &
trap "kill $! || true" EXIT
sleep 2
curl -i -X POST http://localhost:8086/api/v2/setup -H 'accept: application/json' \
    -d '{
            "username": "my-user",
            "password": "my-password",
            "org": "my-org",
            "bucket": "my-bucket",
            "token": "my-token"
        }'
# /setup
# double requests found. This may be due to our custom test setup without docker container
donttest="(InfluxDBClientTestMock and test_redacted_auth_header)"
donttest="$donttest or (BucketsClientTest and test_pagination)"
donttest="$donttest or (WriteApiTestMock and test_data_class)"
donttest="$donttest or (WriteApiTestMock and test_named_tuple)"
donttest="$donttest or (WriteApiTestMock and test_redirect)"
donttest="$donttest or (WriteApiTestMock and test_writes_asynchronous_without_retry)"
donttest="$donttest or (WriteApiTestMock and test_writes_default_tags_dict_without_tag)"
donttest="$donttest or (WriteApiTestMock and test_writes_synchronous_without_retry)"
donttest="$donttest or BatchingWriteTest"
donttest="$donttest or test_gzip"
donttest="$donttest or test_query_and_debug"
%pytest tests -k "not ($donttest)"

%files %{python_files}
%{python_sitelib}/influxdb_client
%{python_sitelib}/influxdb_client-%{version}.dist-info

%changelog
