#
# spec file for package python-s3transfer
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
Name:           python-s3transfer
Version:        0.10.2
Release:        0
Summary:        Python S3 transfer manager
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/boto/s3transfer
Source0:        https://files.pythonhosted.org/packages/source/s/s3transfer/s3transfer-%{version}.tar.gz
BuildRequires:  %{python_module botocore >= 1.33.2}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-requests
Requires:       (python-botocore >= 1.33.2 with python-botocore <= 2.0.0)
BuildArch:      noarch
%if 0%{?sle_version} >= 150400
Obsoletes:      python3-s3transfer < %{version}
%endif
%python_subpackages

%description
A transfer manager for Amazon Web Services S3

%prep
%setup -q -n s3transfer-%{version}
# remove integration tests that need running s3
rm -rf tests/integration

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_download_futures_fail_triggers_shutdown - https://github.com/boto/s3transfer/pull/162
%pytest -k 'not test_download_futures_fail_triggers_shutdown'

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%{python_sitelib}/s3transfer/
%{python_sitelib}/s3transfer-%{version}*-info

%changelog
