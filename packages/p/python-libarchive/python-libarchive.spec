#
# spec file for package python-libarchive
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
%define oldpython python
Name:           python-libarchive
Version:        0.4.7
Release:        0
Summary:        Python adapter for universal, libarchive-based archive access
License:        GPL-2.0-only
Group:          Development/Languages/Python
URL:            https://github.com/dsoprea/PyEasyArchive
Source:         https://files.pythonhosted.org/packages/source/l/libarchive/libarchive-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  libarchive-devel
BuildRequires:  python-rpm-macros
Requires:       libarchive-devel
Conflicts:      python-libarchive-c
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module nose}
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

%build
%python_build

%check
# https://github.com/dsoprea/PyEasyArchive/issues/33
%python_expand nosetests-%{$python_bin_suffix} -e test_read_symlinks

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
