#
# spec file for package python-cfn-lint
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


%{?sle15_python_module_pythons}
Name:           python-cfn-lint
Version:        0.87.9
Release:        0
Summary:        Tool to checks cloudformation for practices and behaviour
License:        MIT
URL:            https://github.com/aws-cloudformation/cfn-python-lint
Source:         https://github.com/aws-cloudformation/cfn-python-lint/archive/v%{version}.tar.gz#/cfn-lint-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module regex}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module sympy}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       git-core
Requires:       python-PyYAML >= 5.4
Requires:       python-aws-sam-translator >= 1.89.0
Requires:       python-jschema-to-python >= 1.2.3
Requires:       python-jsonpatch
Requires:       python-junit-xml >= 1.9
Requires:       python-networkx >= 2.4
Requires:       python-regex
Requires:       python-sarif-om >= 1.0.4
Requires:       python-sympy >= 1.0.0
Requires:       (python-jsonschema > 3.0 with python-jsonschema < 5)
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     python-pydot
Provides:       cfn-lint = %{version}
Obsoletes:      cfn-lint < %{version}
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module PyYAML >= 5.4}
BuildRequires:  %{python_module aws-sam-translator >= 1.89.0}
BuildRequires:  %{python_module jschema-to-python >= 1.2.3}
BuildRequires:  %{python_module jsonpatch}
BuildRequires:  %{python_module jsonschema > 3.0 with %python-jsonschema < 5}
BuildRequires:  %{python_module junit-xml >= 1.9}
BuildRequires:  %{python_module networkx >= 2.4}
BuildRequires:  %{python_module pydot}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module sarif-om >= 1.0.4}
BuildRequires:  bash
BuildRequires:  git-core
# /SECTION
%python_subpackages

%description
Validate CloudFormation yaml/json templates against the CloudFormation
spec and additional checks. Includes checking valid values for
resource properties and best practices.

%prep
%setup -q -n cfn-lint-%{version}
# do not hardcode versions
sed -i -e 's:~=:>=:g' setup.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/cfn-lint

%check
export LANG=en_US.UTF-8
export AWS_DEFAULT_REGION=us-east-1
# the code calls git grep, need to be inside git repo
git init
git add src/cfnlint/rules
# deselect online tests
donttest="test_sarif_formatter"
donttest="$donttest or test_update_resource_specs_python_2"
donttest="$donttest or test_update_resource_specs_python_3"
donttest="$donttest or test_bad_config"
donttest="$donttest or test_override_parameters"
donttest="$donttest or test_positional_template_parameters"
donttest="$donttest or test_template_config"
%pytest -s test -v -k "not ($donttest)"

%post
%python_install_alternative cfn-lint

%postun
%python_uninstall_alternative cfn-lint

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%python_alternative %{_bindir}/cfn-lint
%{python_sitelib}/cfnlint
%{python_sitelib}/cfn_lint-%{version}*-info

%changelog
