#
# spec file for package python-moto
#
# Copyright (c) 2021 SUSE LLC
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
Name:           python-moto
Version:        1.3.16
Release:        0
Summary:        Library to mock out the boto library
License:        Apache-2.0
URL:            https://github.com/spulec/moto
Source:         https://files.pythonhosted.org/packages/source/m/moto/moto-%{version}.tar.gz
# PATCH-FIX-UPSTREAM moto-pr3273-escape-sequences.patch gh#spulec/moto#3273 fix escape sequences so that subsequent patches apply without rebase
Patch0:         https://github.com/spulec/moto/pull/3273.patch#/moto-pr3273-escape-sequences.patch
# PATCH-FIX-UPSTREAM moto-pr3308-fix-test_s3.patch gh#spulec/moto#3308 -- fix test failure
Patch1:         https://github.com/spulec/moto/pull/3308.patch#/moto-pr3308-fix-test_s3.patch
# PATCH-FEATURE-UPSTREAM remove_nose.patch gh#spulec/moto#3361 mcepl@suse.com
# Port test suite from nose to pytest
Patch2:         remove_nose.patch
# PATCH-FEATURE-UPSTREAM denose_exceptions.patch gh#spulec/moto#3361 mcepl@suse.com
# Continuation of the previous patch
Patch3:         denose_exceptions.patch
# PATCH-FIX-UPSTREAM moto-pr3412-fix-cfn-lint.patch -- gh#spulec/moto#3412 Fix failures with newer cfn-lint
Patch4:         https://github.com/spulec/moto/pull/3412.patch#/moto-pr3412-fix-cfn-lint.patch
# PATCH-FIX-UPSTREAM moto-pr3444-fix-docker.patch -- gh#spulec/moto#3444 Fix docker failure in test
Patch5:         https://github.com/spulec/moto/pull/3444.patch#/moto-pr3444-fix-docker.patch
# PATCH-FIX-UPSTREAM moto-pr3575-managedblockchain-botocore-api.patch -- gh#spulec/moto#3575 Support change botocore api
Patch6:         https://github.com/spulec/moto/pull/3575.patch#/moto-pr3575-managedblockchain-botocore-api.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Jinja2 >= 2.10.1
Requires:       python-PyYAML >= 5.1
Requires:       python-Werkzeug
Requires:       python-aws-xray-sdk >= 0.93
Requires:       python-boto >= 2.36.0
Requires:       python-boto3 >= 1.9.201
Requires:       python-botocore >= 1.12.201
Requires:       python-cfn-lint >= 0.4.0
Requires:       python-cryptography >= 2.3.0
Requires:       python-docker >= 2.5.1
Requires:       python-idna >= 2.5
Requires:       python-jsondiff >= 1.1.2
Requires:       python-mock
Requires:       python-python-dateutil >= 2.1
Requires:       python-python-jose
Requires:       python-pytz
Requires:       python-requests >= 2.5
Requires:       python-responses >= 0.9.0
Requires:       python-six > 1.9
Requires:       python-sshpubkeys >= 3.1.0
Requires:       python-xmltodict
%if %{python_version_nodots} < 37
# gh#spulec/moto#3576
Requires:       python-importlib-resources
%endif
Requires(post): update-alternatives
Requires(preun): update-alternatives
Recommends:     python-Flask
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Flask}
BuildRequires:  %{python_module Jinja2 >= 2.10.1}
BuildRequires:  %{python_module PyYAML >= 5.1}
BuildRequires:  %{python_module Werkzeug}
BuildRequires:  %{python_module aws-xray-sdk >= 0.93}
BuildRequires:  %{python_module boto >= 2.36.0}
BuildRequires:  %{python_module boto3 >= 1.9.201}
BuildRequires:  %{python_module botocore >= 1.12.201}
BuildRequires:  %{python_module cfn-lint >= 0.4.0}
BuildRequires:  %{python_module cryptography >= 2.3.0}
BuildRequires:  %{python_module docker >= 2.5.1}
BuildRequires:  %{python_module freezegun}
BuildRequires:  %{python_module idna >= 2.5}
# For Python versions without importlib.resources, but it does not hurt to install the package for all flavors.
BuildRequires:  %{python_module importlib-resources}
BuildRequires:  %{python_module jsondiff >= 1.1.2}
BuildRequires:  %{python_module jsonpickle}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module parameterized}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil >= 2.1}
BuildRequires:  %{python_module python-jose}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module requests >= 2.5}
BuildRequires:  %{python_module responses >= 0.9.0}
BuildRequires:  %{python_module six > 1.9}
BuildRequires:  %{python_module sshpubkeys >= 3.1.0}
BuildRequires:  %{python_module sure}
BuildRequires:  %{python_module xmltodict}
%if %{with python2}
BuildRequires:  python-backports.tempfile
%endif
# /SECTION
%ifpython2
Requires:       python-backports.tempfile
%endif
%python_subpackages

%description
A library that allows your python tests to mock out the boto
library.

%prep
%setup -q -n moto-%{version}
%autopatch -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%python_clone -a %{buildroot}%{_bindir}/moto_server

%check
# skipped tests require network connection
export BOTO_CONFIG=/dev/null
%pytest -k 'not network' tests/

%post
%python_install_alternative moto_server

%preun
%python_uninstall_alternative moto_server

%files %{python_files}
%doc AUTHORS.md README.md
%license LICENSE
%python_alternative %{_bindir}/moto_server
%{python_sitelib}/*

%changelog
