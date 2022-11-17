#
# spec file for package python-awscrt
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-awscrt
Version:        0.14.7
Release:        0
Summary:        Common runtime for AWS Python projects
License:        Apache-2.0
URL:            https://github.com/awslabs/aws-crt-python
Source:         https://files.pythonhosted.org/packages/source/a/awscrt/awscrt-%{version}.tar.gz
Source1:        testdata.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  ca-certificates-mozilla
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  python-rpm-macros
Requires:       ca-certificates-mozilla
%python_subpackages

%description
A common runtime for AWS Python projects.

%prep
%setup -q -n awscrt-%{version}
tar -xzf %{SOURCE1}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# test_delegate_provider_exception fails in tearDown with a resource leak detected, possibly related to network not being present
# http_client_test and test_h2_client require network
%pytest_arch -rs -k 'not (http_client_test or test_h2_client or test_delegate_provider_exception)'

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitearch}/_awscrt*
%{python_sitearch}/awscrt*

%changelog
