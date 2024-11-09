#
# spec file for package python-aws-sam-translator
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


# Disable tests on SLE-12 due to issues with Python 3.4
# see: https://github.com/awslabs/serverless-application-model/issues/1255
%if 0%{?suse_version} < 1500
%bcond_with test
%else
%bcond_without test
%endif
%{?sle15_python_module_pythons}
Name:           python-aws-sam-translator
Version:        1.92.0
Release:        0
Summary:        AWS SAM template to AWS CloudFormation template translator
License:        Apache-2.0
URL:            https://github.com/awslabs/serverless-application-model
Source:         https://github.com/awslabs/serverless-application-model/archive/v%{version}.tar.gz#/serverless-application-model-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-boto3 >= 1.19.5
Requires:       python-jsonschema >= 3.2
Requires:       python-pydantic >= 1.8
Requires:       python-typing_extensions >= 4.4.0
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%if 0%{?suse_version} < 1500
BuildRequires:  python
%endif
%if 0%{?sle_version} >= 150400
Obsoletes:      python3-aws-sam-translator < %{version}
%endif
# SECTION test requirements
BuildRequires:  %{python_module PyYAML >= 5.4}
BuildRequires:  %{python_module boto3 >= 1.19.5}
BuildRequires:  %{python_module coverage >= 5.3}
BuildRequires:  %{python_module docopt >= 0.6.2}
BuildRequires:  %{python_module jsonschema >= 3.2}
BuildRequires:  %{python_module parameterized >= 0.7.4}
BuildRequires:  %{python_module pydantic >= 1.8}
BuildRequires:  %{python_module pytest >= 3.0.7}
BuildRequires:  %{python_module pytest-cov >= 2.10.1}
BuildRequires:  %{python_module pytest-rerunfailures}
BuildRequires:  %{python_module requests >= 2.24.0}
%python_subpackages

%description
AWS SAM Translator is a library that transform SAM
templates into AWS CloudFormation templates

%prep
%autosetup -p1 -n serverless-application-model-%{version}
sed -i -e 's:~=:>=:g' requirements/base.txt
# Remove the __init__.py file from bin to avoid installation of this
# folder in python_sitelib
# https://github.com/aws/serverless-application-model/issues/2588
rm bin/__init__.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

mkdir -p %{buildroot}%{_bindir}
install -D -m 755 bin/sam-translate.py %{buildroot}%{_bindir}/sam-translate
%python_clone -a %{buildroot}%{_bindir}/sam-translate

%if %{with test}
%check
export LANG=en_US.UTF8
donttest="test_plugin_accepts_different_sar_client or test_plugin_accepts_flags or"
donttest="$donttest test_plugin_accepts_parameters or test_plugin_default_values or"
donttest="$donttest test_plugin_invalid_configuration_raises_exception or test_plugin_must_setup_correct_name or"
donttest="$donttest test_must_process_applications or test_must_process_applications_validate or"
donttest="$donttest test_process_invalid_applications or test_process_invalid_applications_validate or"
donttest="$donttest test_resolve_intrinsics or test_sar_service_calls or test_sar_success_one_app or"
donttest="$donttest test_sar_throttling_doesnt_stop_processing or test_sleep_between_sar_checks or"
donttest="$donttest test_unexpected_sar_error_stops_processing or test_time_limit_exceeds_between_combined_sar_calls or"
donttest="$donttest test_is_service_supported_positive_4_ec2"
PYTHONPATH="${PWD}" %pytest  -k "not ($donttest)"
%endif

%post
%python_install_alternative sam-translate

%postun
%python_uninstall_alternative sam-translate

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/sam-translate
%{python_sitelib}/samtranslator
%{python_sitelib}/aws_sam_translator-%{version}.dist-info

%changelog
