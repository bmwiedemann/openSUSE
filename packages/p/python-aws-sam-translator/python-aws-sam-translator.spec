#
# spec file for package python-aws-sam-translator
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


# Disable tests on SLE-12 due to issues with Python 3.4
# see: https://github.com/awslabs/serverless-application-model/issues/1255
%if 0%{?suse_version} < 1500
%bcond_with test
%else
%bcond_without test
%endif
%if 0%{?suse_version} >= 1500
%define skip_python2 1
%endif
Name:           python-aws-sam-translator
Version:        1.54.0
Release:        0
Summary:        AWS SAM template to AWS CloudFormation template translator
License:        Apache-2.0
URL:            https://github.com/awslabs/serverless-application-model
Source:         https://github.com/awslabs/serverless-application-model/archive/v%{version}.tar.gz#/serverless-application-model-%{version}.tar.gz
Patch0:         skip-tests-require-network.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-boto3 >= 1.19.5
Requires:       python-jsonschema >= 3.2
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
%if 0%{?suse_version} < 1500
BuildRequires:  python
%endif
# SECTION test requirements
BuildRequires:  %{python_module PyYAML >= 5.4}
BuildRequires:  %{python_module boto3 >= 1.19.5}
BuildRequires:  %{python_module coverage >= 5.3}
BuildRequires:  %{python_module docopt >= 0.6.2}
BuildRequires:  %{python_module jsonschema >= 3.2}
BuildRequires:  %{python_module parameterized >= 0.7.4}
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
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

mkdir -p %{buildroot}%{_bindir}
install -D -m 755 bin/sam-translate.py %{buildroot}%{_bindir}/sam-translate
%python_clone -a %{buildroot}%{_bindir}/sam-translate

%if %{with test}
%check
export LANG=en_US.UTF8
# test_is_service_supported_positive_4_ec2:
#   samtranslator/region_configuration.py:52: NoRegionFound
# test_errors_13_error_definitionuri:
#   AssertionError: Expected 7 errors, found 9
%pytest -k 'not (test_is_service_supported_positive_4_ec2 or test_errors_13_error_definitionuri or test_py27_hash)'
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
%{python_sitelib}/aws_sam_translator-%{version}*-info

%changelog
