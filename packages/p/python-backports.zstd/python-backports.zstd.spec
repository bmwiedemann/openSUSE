#
# spec file for package python-backports.zstd
#
# Copyright (c) 2025 SUSE LLC and contributors
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


# Only supported with Python <= 3.13
%define skip_python314 1
Name:           python-backports.zstd
Version:        1.0.0
Release:        0
Summary:        Backport of compressionzstd
License:        BSD-3-Clause
URL:            https://github.com/rogdham/backports.zstd
Source:         https://files.pythonhosted.org/packages/source/b/backports.zstd/backports_zstd-%{version}.tar.gz
# PATCH-FIX-UPSTREAM Based on gh#Rogdham/backports.zstd#54
Patch0:         do-not-abort-with-python313.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
Backport of compression.zstd

%prep
%autosetup -p1 -n backports_zstd-%{version}

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
rm -v tests/test/test_tarfile.py
%pytest_arch

%files %{python_files}
%doc README.md
%license LICENSE.txt LICENSE_zstd.txt LICENSE.txt LICENSE_zstd.txt
%{python_sitearch}/backports
%{python_sitearch}/backports_zstd-%{version}.dist-info

%changelog
