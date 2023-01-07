#
# spec file for package python-minio
#
# Copyright (c) 2023 SUSE LLC
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
Name:           python-minio
Version:        7.1.13
Release:        0
Summary:        Minio library for Amazon S3 compatible cloud storage
License:        Apache-2.0
URL:            https://github.com/minio/minio-py
Source:         https://files.pythonhosted.org/packages/source/m/minio/minio-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-certifi
Requires:       python-future
Requires:       python-python-dateutil
Requires:       python-pytz
Requires:       python-urllib3
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Faker}
BuildRequires:  %{python_module certifi}
BuildRequires:  %{python_module future}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module urllib3}
# /SECTION
%python_subpackages

%description
Minio library for Amazon S3 compatible cloud storage.

%prep
%setup -q -n minio-%{version}
%autopatch -p1
mv docs/zh_CN/API.md docs/API_zh_CN.md
sed -i -e '/configparser/d' setup.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# https://github.com/minio/minio-py/issues/1187
sed -i 's:import mock:import unittest.mock as mock:' tests/unit/*.py
%pytest

%files %{python_files}
%doc README*.md docs/API*.md examples/
%license LICENSE
%{python_sitelib}/*

%changelog
