#
# spec file for package oci-cli
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

%if 0%{?suse_version} >= 1600
%define pythons %{primary_python}
%else
%define pythons python311
%endif
%global _sitelibdir %{%{pythons}_sitelib}

Name:           oci-cli%{psuffix}
Version:        3.43.1
Release:        0
Summary:        Oracle Cloud Infrastructure CLI
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.us-phoenix-1.oraclecloud.com/Content/API/SDKDocs/cli.htm
Source:         https://github.com/oracle/oci-cli/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         oc_relax-python-depends.patch
BuildRequires:  %{pythons}-PyJWT
BuildRequires:  %{pythons}-PyYAML >= 5.4.1
BuildRequires:  %{pythons}-arrow >= 1.0.0
BuildRequires:  %{pythons}-certifi
BuildRequires:  %{pythons}-click >= 8.0.4
BuildRequires:  %{pythons}-cryptography >= 3.2.1
BuildRequires:  %{pythons}-devel
BuildRequires:  %{pythons}-jmespath >= 0.10.0
BuildRequires:  %{pythons}-oci-sdk >= 2.128.1
BuildRequires:  %{pythons}-pip
BuildRequires:  %{pythons}-pyOpenSSL >= 22.1.0
BuildRequires:  %{pythons}-python-dateutil >= 2.5.3
BuildRequires:  %{pythons}-pytz >= 2016.10
BuildRequires:  %{pythons}-setuptools
BuildRequires:  %{pythons}-six >= 1.15.0
BuildRequires:  %{pythons}-terminaltables >= 3.1.10
BuildRequires:  %{pythons}-wheel
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %{with test}
BuildRequires:  %{pythons}-Jinja2 >= 2.11.3
BuildRequires:  %{pythons}-Sphinx >= 1.6.4
BuildRequires:  %{pythons}-appdirs >= 1.4.3
BuildRequires:  %{pythons}-cffi >= 1.9.1
BuildRequires:  %{pythons}-coverage >= 4.5.2
BuildRequires:  %{pythons}-ndg-httpsclient >= 0.4.2
BuildRequires:  %{pythons}-packaging >= 20.2
BuildRequires:  %{pythons}-pluggy >= 0.13.0
BuildRequires:  %{pythons}-py >= 1.11.0
BuildRequires:  %{pythons}-pyasn1 >= 0.2.3
BuildRequires:  %{pythons}-pycparser >= 2.20
BuildRequires:  %{pythons}-pyparsing >= 2.2.0
BuildRequires:  %{pythons}-pytest-cov >= 2.5.1
BuildRequires:  %{pythons}-pytest-forked >= 1.0.2
BuildRequires:  %{pythons}-pytest-xdist >= 1.22.2
BuildRequires:  %{pythons}-requests >= 2.21.0
BuildRequires:  %{pythons}-sphinx_rtd_theme >= 0.4.3
BuildRequires:  %{pythons}-tox >= 3.23.0
BuildRequires:  %{pythons}-vcrpy >= 4.2.1
BuildRequires:  %{pythons}-virtualenv >= 16.7.10
BuildRequires:  (%{pythons}-vcrpy >= 1.13.0 if python-base <= 3.9)
BuildRequires:  (%{pythons}-vcrpy >= 4.2.1 if python-base >= 3.10)
BuildRequires:  (%{pythons}-vcrpy >= 4.6.10 if python-base <= 3.9)
BuildRequires:  (%{pythons}-vcrpy >= 7.1.2 if python-base >= 3.10)
%endif
Requires:       %{pythons}-PyYAML >= 5.4.1
Requires:       %{pythons}-arrow >= 1.0.0
Requires:       %{pythons}-certifi
Requires:       %{pythons}-click >= 8.0.4
Requires:       %{pythons}-cryptography >= 3.2.1
Requires:       %{pythons}-jmespath >= 0.10.0
Requires:       %{pythons}-oci-sdk >= 2.128.1
Requires:       %{pythons}-prompt_toolkit >= 3.0.38
Requires:       %{pythons}-pyOpenSSL >= 22.1.0
Requires:       %{pythons}-python-dateutil >= 2.5.3
Requires:       %{pythons}-pytz >= 2016.10
Requires:       %{pythons}-six >= 1.15.0
Requires:       %{pythons}-terminaltables >= 3.1.10

BuildArch:      noarch

%description
The CLI is a small footprint tool that you can use on its own or with the
Console to complete Oracle Cloud Infrastructure tasks. The CLI provides
the same core functionality as the Console, plus additional commands.
Some of these, such as the ability to run scripts, extend the Console's
functionality.

%prep
%autosetup -p1 -n oci-cli-%{version}

# Fix includes
find . -name "*.py" -exec sed -i 's/from oci\._vendor //' \{\} +
find . -name "*.py" -exec sed -i 's/oci\._vendor\.//' \{\} +

%build
%pyproject_wheel

%if %{with test}
%check
export PYTHONDONTWRITEBYTECODE=1
export PYTHONPATH=%{buildroot}%{_sitelibdir}
py.test -s tests/unit
%endif

%install
%pyproject_install
%fdupes %{buildroot}%{_sitelibdir}

%files
%doc CHANGELOG.rst README.rst
%license LICENSE.txt
%{_bindir}/oci
%{_bindir}/create_backup_from_onprem
%{_sitelibdir}/*

%changelog
