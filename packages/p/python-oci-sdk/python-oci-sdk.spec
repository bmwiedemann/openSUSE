#
# spec file for package python-oci-sdk
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


%bcond_without python2
%{?sle15_python_module_pythons}
Name:           python-oci-sdk
Version:        2.128.0
Release:        0
Summary:        Oracle Cloud Infrastructure Python SDK
License:        Apache-2.0 OR UPL-1.0
Group:          Development/Languages/Python
URL:            https://github.com/oracle/oci-python-sdk
Source:         %{url}/archive/v%{version}.tar.gz#/oci-python-sdk-%{version}.tar.gz
Source99:       python-oci-sdk.rpmlintrc
Patch0:         ops_relax-python-depends.patch
# PATCH-FIX-OPENSUSE pytest-740.patch gh#oracle/oci-python-sdk#566
Patch1:         pytest-740.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-certifi
Requires:       python-circuitbreaker >= 1.3.1
Requires:       python-cryptography >= 3.2.1
Requires:       python-pyOpenSSL >= 17.5.0
Requires:       python-python-dateutil >= 2.5.3
Requires:       python-pytz >= 2016.10
# SECTION devendored packages
Requires:       python-PyJWT
Requires:       python-httpsig_cffi
Requires:       python-requests
Requires:       python-six
Requires:       python-sseclient
Requires:       python-urllib3 < 2
# /SECTION
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module PyJWT}
BuildRequires:  %{python_module certifi}
BuildRequires:  %{python_module circuitbreaker >= 1.3.1}
BuildRequires:  %{python_module cryptography >= 3.2.1}
BuildRequires:  %{python_module httpsig_cffi}
BuildRequires:  %{python_module pyOpenSSL >= 17.5.0}
BuildRequires:  %{python_module pytest > 4.1.0}
BuildRequires:  %{python_module python-dateutil >= 2.5.3}
BuildRequires:  %{python_module pytz >= 2016.10}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module sseclient}
BuildRequires:  %{python_module urllib3 < 2}
BuildRequires:  %{python_module vcrpy >= 2.0.1}
%if %{with python2}
BuildRequires:  python-configparser >= 4.0.2
%endif
# /SECTION
%ifpython2
Requires:       python-configparser >= 4.0.2
%endif
# The PyPI name is just oci
Provides:       python-oci = %{version}-%{release}
%python_subpackages

%description
Python SDK for Oracle Cloud Infrastructure. Python 2.7+ and 3.5+ are supported.

%prep
%autosetup -p1 -n oci-python-sdk-%{version}
# Remove vendored packages
rm -rf src/oci/_vendor/
# Fix includes
find . -name "*.py" -exec sed -i 's/from oci._vendor //' \{\} +
sed -i 's/from \._vendor //' src/oci/*.py
sed -i 's/ oci._vendor.jwt as//' src/oci/auth/*.py
sed -i 's/oci\._vendor\.//' src/oci/*.py src/oci/auth/*.py src/oci/auth/signers/*.py src/oci/retry/*.py src/oci/object_storage/transfer/internal/*.py tests/*.py
sed -i 's/from . import vcr_mods//' tests/test_config_container.py

%build
%pyproject_wheel

%check
%pytest tests/unit tests/integ -s -rs

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc CHANGELOG.rst README.rst
%license LICENSE.txt
%{python_sitelib}/oci
%{python_sitelib}/oci-%{version}*-info

%changelog
