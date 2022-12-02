#
# spec file
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
Version:        3.20.3
Release:        0
Summary:        Oracle Cloud Infrastructure CLI
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.us-phoenix-1.oraclecloud.com/Content/API/SDKDocs/cli.htm
Source:         https://github.com/oracle/oci-cli/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         oc_relax-python-depends.patch
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-PyJWT
BuildRequires:  python3-PyYAML >= 5.4.1
BuildRequires:  python3-arrow >= 1.0.0
BuildRequires:  python3-certifi
BuildRequires:  python3-click >= 8.0.4
BuildRequires:  python3-cryptography >= 3.2.1
BuildRequires:  python3-devel
BuildRequires:  python3-jmespath >= 0.10.0
BuildRequires:  python3-oci-sdk >= 2.88.2
BuildRequires:  python3-pyOpenSSL >= 19.1.0
BuildRequires:  python3-python-dateutil >= 2.5.3
BuildRequires:  python3-pytz >= 2016.10
BuildRequires:  python3-setuptools
BuildRequires:  python3-six >= 1.15.0
BuildRequires:  python3-terminaltables >= 3.1.0
%if %{with test}
BuildRequires:  python3-Jinja2 >= 2.11.3
BuildRequires:  python3-Sphinx >= 1.6.4
BuildRequires:  python3-appdirs >= 1.4.3
BuildRequires:  python3-cffi >= 1.9.1
BuildRequires:  python3-coverage >= 4.5.2
BuildRequires:  python3-ndg-httpsclient >= 0.4.2
BuildRequires:  python3-packaging >= 20.2
BuildRequires:  python3-pluggy >= 0.13.0
BuildRequires:  python3-py >= 1.10.0
BuildRequires:  python3-pyasn1 >= 0.2.3
BuildRequires:  python3-pycparser >= 2.20
BuildRequires:  python3-pyparsing >= 2.2.0
BuildRequires:  python3-pytest >= 3.2.3
BuildRequires:  python3-pytest-cov >= 2.5.1
BuildRequires:  python3-pytest-forked >= 1.0.2
BuildRequires:  python3-pytest-xdist >= 1.22.2
BuildRequires:  python3-requests >= 2.21.0
BuildRequires:  python3-sphinx_rtd_theme >= 0.4.3
BuildRequires:  python3-tox >= 3.23.0
BuildRequires:  python3-vcrpy >= 1.13.0
BuildRequires:  python3-virtualenv >= 16.7.10
%endif
Requires:       python3-PyYAML >= 5.4.1
Requires:       python3-arrow >= 1.0.0
Requires:       python3-certifi
Requires:       python3-click >= 8.0.4
Requires:       python3-cryptography >= 3.2.1
Requires:       python3-jmespath >= 0.10.0
Requires:       python3-oci-sdk >= 2.88.2
Requires:       python3-prompt_toolkit >= 3.0.29
Requires:       python3-pyOpenSSL >= 19.1.0
Requires:       python3-python-dateutil >= 2.5.3
Requires:       python3-pytz >= 2016.10
Requires:       python3-six >= 1.15.0
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
# Fix includes
find . -name "*.py" -exec sed -i 's/from oci\._vendor //' \{\} +
find . -name "*.py" -exec sed -i 's/oci\._vendor\.//' \{\} +

%build
%python3_build

%if %{with test}
%check
export PYTHONDONTWRITEBYTECODE=1
export PYTHONPATH=%{buildroot}%{python3_sitelib}
py.test -s tests/unit
%endif

%install
%python3_install
%fdupes %{buildroot}%{python3_sitelib}

%files
%doc CHANGELOG.rst README.rst
%license LICENSE.txt
%{_bindir}/oci
%{_bindir}/create_backup_from_onprem
%{python3_sitelib}/*

%changelog
