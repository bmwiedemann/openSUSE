#
# spec file for package python-hiredis
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
Name:           python-hiredis
Version:        1.0.0
Release:        0
Summary:        Python wrapper for hiredis
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/redis/hiredis-py
Source:         https://github.com/redis/hiredis-py/archive/v%{version}.tar.gz
Patch0:         0001-Use-system-libhiredis.patch
Patch1:         fix_build_dir_in_tests.patch
Patch2:         drop-vendor-sources.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  hiredis-devel >= 0.13.3
BuildRequires:  python-rpm-macros
%python_subpackages

%description
Python wrapper for hiredis C connector.

%prep
%setup -q -n hiredis-py-%{version}
%autopatch -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%python_exec test.py

%files %{python_files}
%license COPYING
%{python_sitearch}/*

%changelog
