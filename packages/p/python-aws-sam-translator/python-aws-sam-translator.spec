#
# spec file for package python-aws-sam-translator
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-aws-sam-translator
Version:        1.11.0
Release:        0
Summary:        AWS SAM template to AWS CloudFormation template translator
License:        Apache-2.0
Group:          Development/Languages/Python
Url:            https://github.com/awslabs/serverless-application-model
Source:         https://github.com/awslabs/serverless-application-model/archive/v%{version}.tar.gz#/serverless-application-model-%{version}.tar.gz
Patch:          ast_drop-compatible-releases-operator.patch
%if 0%{?suse_version} < 1500
BuildRequires:  python
%endif
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module PyYAML >= 4.2}
BuildRequires:  %{python_module boto3 >= 1.5}
BuildRequires:  %{python_module coverage >= 4.4.0}
BuildRequires:  %{python_module jsonschema >= 2.6}
BuildRequires:  %{python_module mock >= 2.0.0}
BuildRequires:  %{python_module parameterized >= 0.6.1}
BuildRequires:  %{python_module py >= 1.4.33}
BuildRequires:  %{python_module pytest >= 3.0.7}
BuildRequires:  %{python_module pytest-cov >= 2.4.0}
BuildRequires:  %{python_module requests >= 2.20.0}
BuildRequires:  %{python_module six >= 1.11}
BuildRequires:  python-enum34 >= 1.1
# /SECTION
Requires:       python-PyYAML >= 4.2
Requires:       python-boto3 >= 1.5
Requires:       python-docopt >= 0.6.2
Requires:       python-jsonschema >= 2.6
Requires:       python-six >= 1.11
%ifpython2
Requires:       python-enum34 >= 1.1
%endif
BuildArch:      noarch

%python_subpackages

%description
AWS SAM Translator is a library that transform SAM
templates into AWS CloudFormation templates

%prep
%setup -q -n serverless-application-model-%{version}
%patch -p1
sed -i -e '1s|#!/usr/bin/env python2|#!/usr/bin/python3|' bin/sam-translate.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

mkdir -p %{buildroot}%{_bindir}
install -D -m 644 bin/sam-translate.py %{buildroot}%{_bindir}/sam-translate

%check
export LANG=en_US.UTF8
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%python3_only %{_bindir}/sam-translate
%{python_sitelib}/*

%changelog
