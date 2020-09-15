#
# spec file for package python-cfn-lint
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
%bcond_without python2
Name:           python-cfn-lint
Version:        0.35.1
Release:        0
Summary:        Tool to checks cloudformation for practices and behaviour
License:        MIT
URL:            https://github.com/aws-cloudformation/cfn-python-lint
Source:         https://github.com/aws-cloudformation/cfn-python-lint/archive/v%{version}.tar.gz#/cfn-python-lint-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML
Requires:       python-aws-sam-translator >= 1.25.0
Requires:       python-importlib_resources >= 1.0.2
Requires:       python-jsonpatch
Requires:       python-jsonschema > 3.0
Requires:       python-junit-xml >= 1.9
Requires:       python-networkx >= 2.2
Requires:       python-requests >= 2.15.0
Requires:       python-six >= 1.11
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     python-pydot
Provides:       cfn-lint = %{version}
Obsoletes:      cfn-lint < %{version}
BuildArch:      noarch
%if 0%{?suse_version} < 1500
BuildRequires:  python
%endif
# SECTION test requirements
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module aws-sam-translator >= 1.25.0}
BuildRequires:  %{python_module importlib_resources >= 1.0.2}
BuildRequires:  %{python_module jsonpatch}
BuildRequires:  %{python_module jsonschema > 3.0}
BuildRequires:  %{python_module junit-xml >= 1.9}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module networkx >= 2.2}
BuildRequires:  %{python_module pydot}
BuildRequires:  %{python_module requests >= 2.15.0}
BuildRequires:  %{python_module six >= 1.11}
BuildRequires:  bash
%if %{with python2}
BuildRequires:  python-pathlib2 >= 2.3.0
%endif
# /SECTION
%ifpython2
Requires:       python-pathlib2 >= 2.3.0
%endif
%python_subpackages

%description
Validate CloudFormation yaml/json templates against the CloudFormation
spec and additional checks. Includes checking valid values for
resource properties and best practices.

%prep
%setup -q -n cfn-python-lint-%{version}
# do not hardcode versions
sed -i -e 's:~=:>=:g' setup.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/cfn-lint

%post
%python_install_alternative cfn-lint

%postun
%python_uninstall_alternative cfn-lint

%check
export LANG=en_US.UTF-8
export AWS_DEFAULT_REGION=us-east-1

# This is just faking as we use update-alternatives and don't have cfn-lint binary around during build
mkdir bin
pushd bin
ln -s %{buildroot}%{_bindir}/cfn-lint-%{python3_bin_suffix} ./cfn-lint
popd
export PATH="./bin:$PATH"

%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python -m unittest discover -s test -v

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%{python_sitelib}/*
%python_alternative %{_bindir}/cfn-lint

%changelog
