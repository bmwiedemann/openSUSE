#
# spec file for package python-aws-sam-translator
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
# Disable tests on SLE-12 due to issues with Python 3.4
# see: https://github.com/awslabs/serverless-application-model/issues/1255
%if 0%{?suse_version} < 1500
%bcond_with test
%else
%bcond_without test
%endif
%bcond_without python2
Name:           python-aws-sam-translator
Version:        1.22.0
Release:        0
Summary:        AWS SAM template to AWS CloudFormation template translator
License:        Apache-2.0
URL:            https://github.com/awslabs/serverless-application-model
Source:         https://github.com/awslabs/serverless-application-model/archive/v%{version}.tar.gz#/serverless-application-model-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML >= 4.2
Requires:       python-boto3 >= 1.5
Requires:       python-docopt >= 0.6.2
Requires:       python-jsonschema >= 3.0
Requires:       python-six >= 1.11
BuildArch:      noarch
%if 0%{?suse_version} < 1500
BuildRequires:  python
%endif
# SECTION test requirements
BuildRequires:  %{python_module PyYAML >= 5.1}
BuildRequires:  %{python_module boto3 >= 1.5}
BuildRequires:  %{python_module coverage >= 4.4.0}
BuildRequires:  %{python_module docopt >= 0.6.2}
BuildRequires:  %{python_module jsonschema >= 3.0}
BuildRequires:  %{python_module mock >= 2.0.0}
BuildRequires:  %{python_module parameterized >= 0.6.1}
BuildRequires:  %{python_module pytest >= 3.0.7}
BuildRequires:  %{python_module pytest-cov >= 2.4.0}
BuildRequires:  %{python_module requests >= 2.20.0}
BuildRequires:  %{python_module six >= 1.11}
%if %{with python2}
BuildRequires:  python-enum34 >= 1.1
%endif
# /SECTION
%ifpython2
Requires:       python-enum34 >= 1.1
%endif
%python_subpackages

%description
AWS SAM Translator is a library that transform SAM
templates into AWS CloudFormation templates

%prep
%setup -q -n serverless-application-model-%{version}
sed -i -e '1s|#!%{_bindir}/env python2|#!%{_bindir}/python3|' bin/sam-translate.py
sed -i -e 's:~=:>=:g' requirements/base.txt

%build
%python_build

%install
%python_install
%python_expand rm -r %{buildroot}%{$python_sitelib}/tests/
%python_expand %fdupes %{buildroot}%{$python_sitelib}

mkdir -p %{buildroot}%{_bindir}
install -D -m 755 bin/sam-translate.py %{buildroot}%{_bindir}/sam-translate

%if %{with test}
%check
export LANG=en_US.UTF8
%pytest
%endif

%files %{python_files}
%doc README.md
%license LICENSE
%python3_only %{_bindir}/sam-translate
%{python_sitelib}/*

%changelog
