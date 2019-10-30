#
# spec file for package python-s3fs
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
%define skip_python2 1
Name:           python-s3fs
Version:        0.3.5
Release:        0
Summary:        Python filesystem interface over S3
License:        BSD-3-Clause
URL:            https://github.com/dask/s3fs/
Source:         https://files.pythonhosted.org/packages/source/s/s3fs/s3fs-%{version}.tar.gz
BuildRequires:  %{python_module boto3 >= 1.9.91}
BuildRequires:  %{python_module botocore >= 1.12.91}
BuildRequires:  %{python_module fsspec >= 0.2.2}
BuildRequires:  %{python_module moto >= 1.3.12}
BuildRequires:  %{python_module pytest >= 4.2.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-boto3 >= 1.9.91
Requires:       python-botocore >= 1.12.91
Requires:       python-fsspec >= 0.2.2
BuildArch:      noarch
%python_subpackages

%description
S3FS builds on boto3 to provide a Python filesystem
interface for S3.

%prep
%setup -q -n s3fs-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_anonymous_access - online test
%pytest -k 'not test_anonymous_access'

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/*

%changelog
