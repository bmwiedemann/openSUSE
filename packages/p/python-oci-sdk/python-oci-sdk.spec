#
# spec file for package python-oci-sdk
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-oci-sdk
Version:        2.9.0
Release:        0
License:        UPL-1.0 or Apache-2.0
Summary:        Oracle Cloud Infrastructure Python SDK
Url:            https://github.com/oracle/oci-python-sdk
Group:          Development/Languages/Python
Source:         https://github.com/oracle/oci-python-sdk/archive/v%{version}.tar.gz
Patch0:         ops_relax-python-depends.patch
Patch1:         ops_fixture-order.patch
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
# SECTION test requirements
BuildRequires:  %{python_module certifi}
%ifpython2
BuildRequires:  python-configparser >= 3.5.0
%endif
BuildRequires:  %{python_module cryptography >= 2.1.4}
BuildRequires:  %{python_module PyJWT}
BuildRequires:  %{python_module pyOpenSSL >= 17.5.0}
BuildRequires:  %{python_module python-dateutil >= 2.5.3}
BuildRequires:  %{python_module python-dateutil < 3.0.0}
BuildRequires:  %{python_module pytz >= 2016.10}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module httpsig_cffi}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module vcrpy}
# /SECTION
BuildRequires:  fdupes
Requires:       python-certifi
%ifpython2
Requires:       python-configparser >= 3.5.0
%endif
Requires:       python-cryptography >= 2.1.4
Requires:       python-PyJWT
Requires:       python-pyOpenSSL >= 17.5.0
Requires:       python-python-dateutil >= 2.5.3
Requires:       python-python-dateutil < 3.0.0
Requires:       python-pytz >= 2016.10
Requires:       python-requests
Requires:       python-httpsig_cffi
Requires:       python-six
BuildArch:      noarch

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
sed -i 's/from oci._vendor //' src/oci/*.py src/oci/analytics/*.py src/oci/apigateway/*.py src/oci/announcements_service/*.py src/oci/audit/*.py src/oci/auth/*.py src/oci/auth/signers/*.py src/oci/autoscaling/*.py src/oci/budget/*.py src/oci/container_engine/*.py src/oci/dns/*.py src/oci/core/*.py src/oci/database/*.py src/oci/dts/*.py src/oci/email/*.py src/oci/events/*.py src/oci/file_storage/*.py src/oci/functions/*.py src/oci/healthchecks/*.py src/oci/integration/*.py src/oci/key_management/*.py src/oci/marketplace/*.py src/oci/limits/*.py src/oci/load_balancer/*.py src/oci/monitoring/*.py src/oci/oda/*.py src/oci/object_storage/*.py src/oci/oce/*.py src/oci/ons/*.py src/oci/object_storage/transfer/*.py src/oci/object_storage/transfer/internal/*.py src/oci/os_management/*.py src/oci/resource_manager/*.py src/oci/streaming/*.py src/oci/identity/*.py src/oci/resource_search/*.py src/oci/waas/*.py src/oci/work_requests/*.py tests/*.py
sed -i 's/ oci._vendor.jwt as//' src/oci/auth/*.py
sed -i 's/oci\._vendor\.//' src/oci/*.py src/oci/retry/*.py src/oci/object_storage/transfer/internal/*.py tests/*.py
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
