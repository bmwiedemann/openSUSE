#
# spec file for package python-cfn-lint
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
Name:           python-cfn-lint
Version:        0.21.4
Release:        0
Summary:        Tool to checks cloudformation for practices and behaviour
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/aws-cloudformation/cfn-python-lint
Source:         https://github.com/aws-cloudformation/cfn-python-lint/archive/v%{version}.tar.gz#/cfn-python-lint-%{version}.tar.gz
Patch0:         cl_drop-compatible-releases-operator.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML
Requires:       python-aws-sam-translator >= 1.10.0
Requires:       python-jsonpatch
Requires:       python-jsonschema > 2.6
Requires:       python-requests >= 2.15.0
Requires:       python-six > 1.11
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module aws-sam-translator >= 1.10.0}
BuildRequires:  %{python_module jsonpatch}
BuildRequires:  %{python_module jsonschema > 2.6}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module requests >= 2.15.0}
BuildRequires:  %{python_module six > 1.11}
BuildRequires:  bash
BuildRequires:  python-enum34 >= 1.1
BuildRequires:  python-pathlib2 >= 2.3.0
# /SECTION
%ifpython2
Requires:       python-pathlib2 >= 2.3.0
%endif
%ifpython3
Requires:       cfn-lint = %{version}
%endif
%python_subpackages

%description
Validate CloudFormation yaml/json templates against the CloudFormation
spec and additional checks. Includes checking valid values for
resource properties and best practices.

# This is primarily a command-line tool, but some packages, like python-moto
# make use of the python API it provides

%package     -n cfn-lint
Summary:        Tool to checks cloudformation for practices and behaviour
Group:          Development/Tools/Other
Requires:       python3-cfn-lint

%description -n cfn-lint
Validate CloudFormation yaml/json templates against the CloudFormation
spec and additional checks. Includes checking valid values for
resource properties and best practices.

%prep
%setup -q -n cfn-python-lint-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
export AWS_DEFAULT_REGION=us-east-1
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python -m unittest discover -s test

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%{python_sitelib}/*

%files -n cfn-lint
%license LICENSE
%{_bindir}/cfn-lint

%changelog
