#
# spec file for package python-s3transfer
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%if 0%{?suse_version} >= 1500
%define skip_python2 1
%endif
Name:           python-s3transfer
Version:        0.4.2
Release:        0
Summary:        Python S3 transfer manager
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/boto/s3transfer
Source0:        https://files.pythonhosted.org/packages/source/s/s3transfer/s3transfer-%{version}.tar.gz
Patch1:         no-bundled-packages.patch
BuildRequires:  %{python_module botocore >= 1.12.36}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module urllib3}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if 0%{?suse_version} < 1500
BuildRequires:  %{python_module scandir}
BuildRequires:  python
%endif
%if %{with python2}
BuildRequires:  python2-futures >= 2.2.0
%endif
Requires:       python-botocore <= 2.0.0
Requires:       python-botocore >= 1.12.36
Requires:       python-requests
Requires:       python-urllib3
BuildArch:      noarch
%ifpython2
Requires:       python-futures <= 4.0.0
Requires:       python-futures >= 2.2.0
%endif
%python_subpackages

%description
A transfer manager for Amazon Web Services S3

%prep
%setup -q -n s3transfer-%{version}
%patch1 -p1
# remove integration tests that need running s3
rm -rf tests/integration

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_download_futures_fail_triggers_shutdown - https://github.com/boto/s3transfer/pull/162
%pytest -k 'not test_download_futures_fail_triggers_shutdown'

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%{python_sitelib}/s3transfer/
%{python_sitelib}/s3transfer-%{version}-py*.egg-info

%changelog
