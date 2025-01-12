#
# spec file for package python-minio
#
# Copyright (c) 2025 SUSE LLC
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
Name:           python-minio
Version:        7.2.14
Release:        0
Summary:        Minio library for Amazon S3 compatible cloud storage
License:        Apache-2.0
URL:            https://github.com/minio/minio-py
Source:         https://files.pythonhosted.org/packages/source/m/minio/minio-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-argon2-cffi
Requires:       python-certifi
Requires:       python-pycryptodome
Requires:       python-typing-extensions
Requires:       python-urllib3
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module certifi}
BuildRequires:  %{python_module argon2-cffi}
BuildRequires:  %{python_module pycryptodome}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module typing-extensions}
BuildRequires:  %{python_module urllib3}
# /SECTION
%python_subpackages

%description
Minio library for Amazon S3 compatible cloud storage.

%prep
%autosetup -p1 -n minio-%{version}
mv docs/zh_CN/API.md docs/API_zh_CN.md
sed -i -e '/configparser/d' setup.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README*.md docs/API*.md examples/
%license LICENSE
%{python_sitelib}/minio
%{python_sitelib}/minio-%{version}.dist-info

%changelog
