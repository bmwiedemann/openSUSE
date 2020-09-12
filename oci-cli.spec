#
# spec file for package oci-cli
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


# The testsuite currently requires an OCI account, see:
# https://github.com/oracle/oci-cli/issues/187,
# so we're not building the test flavor.
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
Name:           oci-cli%{psuffix}
Version:        2.12.10
Release:        0
Summary:        Oracle Cloud Infrastructure CLI
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.us-phoenix-1.oraclecloud.com/Content/API/SDKDocs/cli.htm
Source:         https://github.com/oracle/oci-cli/archive/v%{version}.tar.gz
Patch0:         oc_relax-python-depends.patch
Patch1:         oc_name-defaults_file-parameter.patch
BuildRequires:  fdupes
BuildRequires:  python3-PyJWT
BuildRequires:  python3-PyYAML >= 5.1.2
BuildRequires:  python3-arrow >= 0.14.7
BuildRequires:  python3-certifi
BuildRequires:  python3-click >= 6.7
BuildRequires:  python3-cryptography >= 2.8
BuildRequires:  python3-devel
BuildRequires:  python3-jmespath >= 0.9.4
BuildRequires:  python3-oci-sdk >= 2.21.3
BuildRequires:  python3-pyOpenSSL >= 18.0.0
BuildRequires:  python3-python-dateutil >= 2.5.3
BuildRequires:  python3-pytz >= 2016.10
BuildRequires:  python3-retrying >= 1.3.3
BuildRequires:  python3-setuptools
BuildRequires:  python3-six >= 1.14.0
BuildRequires:  python3-terminaltables >= 3.1.0
%if %{with test}
BuildRequires:  python3-Jinja2 >= 2.10.1
BuildRequires:  python3-Sphinx >= 1.6.4
BuildRequires:  python3-appdirs >= 1.4.3
BuildRequires:  python3-cffi >= 1.9.1
BuildRequires:  python3-coverage >= 4.5.2
BuildRequires:  python3-mock >= 2.0.0
BuildRequires:  python3-ndg-httpsclient >= 0.4.2
BuildRequires:  python3-packaging >= 16.8
BuildRequires:  python3-pluggy >= 0.4.0
BuildRequires:  python3-py >= 1.4.33
BuildRequires:  python3-pyasn1 >= 0.2.3
BuildRequires:  python3-pycparser >= 2.17
BuildRequires:  python3-pyparsing >= 2.2.0
BuildRequires:  python3-pytest >= 3.2.3
BuildRequires:  python3-pytest-cov >= 2.5.1
BuildRequires:  python3-pytest-forked >= 1.0.2
BuildRequires:  python3-pytest-xdist >= 1.22.2
BuildRequires:  python3-requests >= 2.21.0
BuildRequires:  python3-sphinx_rtd_theme >= 0.2.5
BuildRequires:  python3-tox >= 2.9.1
BuildRequires:  python3-vcrpy >= 1.13.0
BuildRequires:  python3-virtualenv >= 15.1.0
%endif
Requires:       python3-PyYAML >= 5.1.2
Requires:       python3-arrow >= 0.14.7
Requires:       python3-certifi
Requires:       python3-click >= 6.7
Requires:       python3-cryptography >= 2.8
Requires:       python3-jmespath >= 0.10.0
Requires:       python3-oci-sdk >= 2.21.3
Requires:       python3-pyOpenSSL >= 18.0.0
Requires:       python3-python-dateutil >= 2.5.3
Requires:       python3-pytz >= 2016.10
Requires:       python3-retrying >= 1.3.3
Requires:       python3-six >= 1.14.0
Requires:       python3-terminaltables >= 3.1.0

BuildArch:      noarch

%description
The CLI is a small footprint tool that you can use on its own or with the
Console to complete Oracle Cloud Infrastructure tasks. The CLI provides
the same core functionality as the Console, plus additional commands.
Some of these, such as the ability to run scripts, extend the Console's
functionality.

%prep
%setup -q -n oci-cli-%{version}
%patch0 -p1
%patch1 -p1
# Fix includes
sed -i 's/from oci._vendor //' src/oci_cli/*.py services/container_engine/src/oci_cli_container_engine/*.py services/object_storage/src/oci_cli_object_storage/object_storage_transfer_manager/*.py services/dts/src/oci_cli_dts/physical_appliance_control_plane/client/*.py services/dts/src/oci_cli_dts/*.py tests/*.py
sed -i 's/oci\._vendor\.//' src/oci_cli/*.py services/dts/src/oci_cli_dts/*.py services/container_engine/src/oci_cli_container_engine/*.py tests/*.py tests/vcr_mods/*.py

%build
python3 setup.py build

%check
%if %{with test}
export PYTHONDONTWRITEBYTECODE=1
export PYTHONPATH=%{buildroot}%{python3_sitelib}
py.test -s tests/unit
%endif

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot} --install-scripts=%{_bindir}
%fdupes %{buildroot}%{python3_sitelib}

%files
%doc CHANGELOG.rst README.rst
%license LICENSE.txt
%{_bindir}/oci
%{_bindir}/create_backup_from_onprem
%{python3_sitelib}/*

%changelog
