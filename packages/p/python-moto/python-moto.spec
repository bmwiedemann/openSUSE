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


%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
Name:           python-moto
Version:        2.2.2
Release:        0
Summary:        Library to mock out the boto library
License:        Apache-2.0
URL:            https://github.com/spulec/moto
Source:         https://files.pythonhosted.org/packages/source/m/moto/moto-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Jinja2 >= 2.10.1
Requires:       python-Werkzeug
Requires:       python-boto3 >= 1.9.201
Requires:       python-botocore >= 1.12.201
Requires:       python-cryptography >= 3.3.1
Requires:       python-importlib_metadata
Requires:       python-more-itertools
Requires:       python-python-dateutil >= 2.1
Requires:       python-pytz
Requires:       python-requests >= 2.5
Requires:       python-responses >= 0.9.0
Requires:       python-xmltodict
Requires:       python-zipp
Requires(post): update-alternatives
Requires(preun):update-alternatives
Recommends:     python-moto-all
Suggests:       python-moto-server
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Flask}
BuildRequires:  %{python_module Flask-Cors}
BuildRequires:  %{python_module Jinja2 >= 2.10.1}
BuildRequires:  %{python_module PyYAML >= 5.1}
BuildRequires:  %{python_module Werkzeug}
BuildRequires:  %{python_module aws-xray-sdk >= 0.93}
BuildRequires:  %{python_module boto3 >= 1.9.201}
BuildRequires:  %{python_module botocore >= 1.12.201}
# old boto is still imported in test files, but not a runtime requirement anymore.
BuildRequires:  %{python_module boto}
BuildRequires:  %{python_module cryptography >= 3.3.1}
BuildRequires:  %{python_module docker >= 2.5.1}
BuildRequires:  %{python_module freezegun}
BuildRequires:  %{python_module idna >= 2.5}
BuildRequires:  %{python_module importlib_metadata}
BuildRequires:  %{python_module jsondiff >= 1.1.2}
BuildRequires:  %{python_module jsonpickle}
BuildRequires:  %{python_module more-itertools}
BuildRequires:  %{python_module parameterized}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil >= 2.1}
BuildRequires:  %{python_module python-jose}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module requests >= 2.5}
BuildRequires:  %{python_module responses >= 0.9.0}
BuildRequires:  %{python_module sshpubkeys >= 3.1.0}
BuildRequires:  %{python_module sure}
BuildRequires:  %{python_module xmltodict}
BuildRequires:  %{python_module zipp}
BuildRequires:  %{python_module cfn-lint >= 0.4.0 if (%python-base without python36-base)}
# /SECTION
%python_subpackages

%description
A library that allows your python tests to mock out the boto
library.

%package all
Summary:        Library to mock out the boto library -- all extras
Requires:       python-PyYAML >= 5.1
Requires:       python-aws-xray-sdk >= 0.93
%if "%python_flavor" != "python36"
Requires:       python-cfn-lint >= 0.4.0
%endif
Requires:       python-docker >= 2.5.1
Requires:       python-idna >= 2.5
Requires:       python-jsondiff >= 1.1.2
Requires:       python-moto = %{version}
Requires:       python-python-jose
Requires:       python-sshpubkeys >= 3.1.0

%description all
A library that allows your python tests to mock out the boto
library. Meta package to install all extras (moto[all])

%package server
Summary:        Library to mock out the boto library -- all extras
Requires:       python-Flask
Requires:       python-Flask-Cors
Requires:       python-moto-all = %{version}

%description server
A library that allows your python tests to mock out the boto
library. Meta package to install server extras (moto[server])

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
export BOTO_CONFIG=/dev/null
# no online tests on obs
donttest="network"
# no connection -- no such file -- we don't have the test containers
donttest+=" or test_terminate_job"
donttest+=" or (test_batch_jobs and (test_dependencies or test_container_overrides))"
# no  python2.7 on TW
donttest+=" or test_invoke_function_from_sqs_exception"
donttest+=" or test_rotate_secret_lambda_invocations"
# https://github.com/boto/botocore/issues/2355
if [ $(getconf LONG_BIT) -eq 32 ]; then
  donttest+=" or test_describe_certificate"
fi
# no cfn-lint for python36
python36_donttest+=" or (test_cloudformation and (validate or invalid_missing))"
%pytest -k "not ($donttest ${$python_donttest})" tests/

%post
%python_install_alternative moto_server

%preun
%python_uninstall_alternative moto_server

%files %{python_files}
%doc AUTHORS.md README.md
%license LICENSE
%python_alternative %{_bindir}/moto_server
%{python_sitelib}/moto
%{python_sitelib}/moto-%{version}*-info

%files %{python_files all}
%license LICENSE

%files %{python_files server}
%license LICENSE

%changelog
