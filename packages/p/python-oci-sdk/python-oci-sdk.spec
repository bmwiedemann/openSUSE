#
# spec file for package python-oci-sdk
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
%bcond_without python2
Name:           python-oci-sdk
Version:        2.23.0
Release:        0
Summary:        Oracle Cloud Infrastructure Python SDK
License:        UPL-1.0 OR Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/oracle/oci-python-sdk
Source:         https://github.com/oracle/oci-python-sdk/archive/v%{version}.tar.gz
Patch0:         ops_relax-python-depends.patch
Patch1:         ops_fixture-order.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyJWT
Requires:       python-certifi
Requires:       python-cryptography >= 2.8
Requires:       python-httpsig_cffi
Requires:       python-pyOpenSSL >= 17.5.0
Requires:       python-python-dateutil < 3.0.0
Requires:       python-python-dateutil >= 2.5.3
Requires:       python-pytz >= 2016.10
Requires:       python-requests
Requires:       python-six
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module PyJWT}
BuildRequires:  %{python_module certifi}
BuildRequires:  %{python_module cryptography >= 2.8}
BuildRequires:  %{python_module httpsig_cffi}
BuildRequires:  %{python_module pyOpenSSL >= 18.0.0}
BuildRequires:  %{python_module pytest > 4.1.0}
BuildRequires:  %{python_module python-dateutil < 3.0.0}
BuildRequires:  %{python_module python-dateutil >= 2.5.3}
BuildRequires:  %{python_module pytz >= 2016.10}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module vcrpy >= 2.0.1}
%if %{with python2}
BuildRequires:  python-configparser >= 4.0.2
%endif
# /SECTION
%ifpython2
Requires:       python-configparser >= 4.0.2
%endif
%python_subpackages

%description
Python SDK for Oracle Cloud Infrastructure. Python 2.7+ and 3.5+ are supported.

%prep
%setup -q -n oci-python-sdk-%{version}
%patch0 -p1
%patch1 -p1
# Remove vendored packages
rm -rf src/oci/_vendor/
# Fix includes
sed -i 's/from \._vendor //' src/oci/*.py
sed -i 's/from oci._vendor //' src/oci/*.py src/oci/analytics/*.py src/oci/apigateway/*.py src/oci/application_migration/*.py src/oci/announcements_service/*.py src/oci/audit/*.py src/oci/auth/*.py src/oci/auth/signers/*.py src/oci/autoscaling/*.py src/oci/bds/*.py src/oci/blockchain/*.py src/oci/budget/*.py src/oci/cims/*.py src/oci/container_engine/*.py src/oci/dns/*.py src/oci/cloud_guard/*.py src/oci/core/*.py src/oci/database/*.py src/oci/data_catalog/*.py src/oci/data_flow/*.py src/oci/data_integration/*.py src/oci/data_safe/*.py src/oci/data_science/*.py src/oci/dts/*.py src/oci/email/*.py src/oci/events/*.py src/oci/file_storage/*.py src/oci/functions/*.py src/oci/healthchecks/*.py src/oci/integration/*.py src/oci/key_management/*.py src/oci/marketplace/*.py src/oci/limits/*.py src/oci/load_balancer/*.py src/oci/log_analytics/*.py src/oci/logging/*.py src/oci/loggingingestion/*.py src/oci/loggingsearch/*.py src/oci/management_agent/*.py src/oci/management_dashboard/*.py src/oci/monitoring/*.py src/oci/mysql/*.py src/oci/nosql/*.py src/oci/oda/*.py src/oci/object_storage/*.py src/oci/oce/*.py src/oci/ons/*.py src/oci/object_storage/transfer/*.py src/oci/object_storage/transfer/internal/*.py src/oci/ocvp/*.py src/oci/os_management/*.py src/oci/resource_manager/*.py src/oci/sch/*.py src/oci/streaming/*.py src/oci/identity/*.py src/oci/resource_search/*.py src/oci/secrets/*.py src/oci/usage_api/*.py src/oci/vault/*.py src/oci/waas/*.py src/oci/work_requests/*.py tests/*.py
sed -i 's/ oci._vendor.jwt as//' src/oci/auth/*.py
sed -i 's/oci\._vendor\.//' src/oci/*.py src/oci/auth/signers/*.py src/oci/retry/*.py src/oci/object_storage/transfer/internal/*.py tests/*.py
sed -i 's/from . import vcr_mods//' tests/test_config_container.py

%build
%python_build

%check
export PYTHONDONTWRITEBYTECODE=1
%pytest tests/unit tests/integ -s

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc CHANGELOG.rst README.rst
%license LICENSE.txt
%{python_sitelib}/*

%changelog
