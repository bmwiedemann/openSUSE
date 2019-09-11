#
# spec file for package python-minio
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
Name:           python-minio
Version:        4.0.18
Release:        0
Summary:        Minio library for Amazon S3 compatible cloud storage
License:        Apache-2.0
Group:          Development/Languages/Python
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
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module urllib3}
# /SECTION
%python_subpackages

%description
Minio library for Amazon S3 compatible cloud storage.

%prep
%setup -q -n minio-%{version}
mv docs/zh_CN/API.md docs/API_zh_CN.md

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test --test-suite=tests

%files %{python_files}
%doc README*.md docs/API*.md examples/
%license LICENSE
%{python_sitelib}/*

%changelog
