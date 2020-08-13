#
# spec file for package python-libarchive
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
%define oldpython python
Name:           python-libarchive
Version:        0.4.7
Release:        0
Summary:        Python adapter for universal, libarchive-based archive access
License:        GPL-2.0-only
URL:            https://github.com/dsoprea/PyEasyArchive
Source:         https://files.pythonhosted.org/packages/source/l/libarchive/libarchive-%{version}.tar.gz
# PATCH-FEATURE-UPSTREAM denose_tests.patch gh#dsoprea/PyEasyArchive#44 mcepl@suse.com
# Removes the need for nose test requirement
Patch0:         denose_tests.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  libarchive-devel
BuildRequires:  python-rpm-macros
Requires:       libarchive-devel
Conflicts:      python-libarchive-c
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
%ifpython2
Conflicts:      %{oldpython}-libarchive-c
%endif
%python_subpackages

%description
A ctypes-based adapter to libarchive.
7-Zip is supported for both reading and writing.

%prep
%setup -q -n libarchive-%{version}
%autopatch -p1

%build
%python_build

%check
export LANG=en_US.UTF8
# test_read_symlinks expects README.rst to be symlink
ln -sf libarchive/resources/README.rst README.rst
%pytest

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
