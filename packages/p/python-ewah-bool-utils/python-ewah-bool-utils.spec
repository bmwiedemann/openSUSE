#
# spec file for package python-ewah-bool-utils
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


Name:           python-ewah-bool-utils
Version:        1.1.0
Release:        0
Summary:        EWAH Bool Array utils for yt
License:        BSD-3-Clause
URL:            https://github.com/yt-project/ewah_bool_utils
Source:         https://files.pythonhosted.org/packages/source/e/ewah-bool-utils/ewah_bool_utils-%{version}.tar.gz
# PATCH-FIX-UPSTREAM build-suse.patch gh#yt-project/ewah_bool_utils#41 mcepl@suse.com
# Fix weird problems with import paths
BuildRequires:  python-rpm-macros
BuildRequires:  gcc-c++
BuildRequires:  %{python_module Cython >= 3}
BuildRequires:  %{python_module numpy-devel >= 1.17.3}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 61.2}
BuildRequires:  %{python_module wheel >= 0.36.2}
BuildRequires:  %{python_module pytest}
BuildRequires:  fdupes
Requires:       python-numpy >= 1.17.3
%python_subpackages

%description
EWAH Bool Array utils for yt

* EWAH Bool Array compression stores integer arrays efficient in memory.
* Can be used for indexing arrays.

%package devel
Summary:        Development files for ewah-bool-utils
Requires:       %{name} = %{version}

%description devel
This package contains files for developing applications using
ewah-bool-utils.

%prep
%autosetup -p1 -n ewah_bool_utils-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
export PYTEST_ADDOPTS="--import-mode=append"
%pytest_arch

%files %{python_files}
%license LICENSE
%doc AUTHORS.rst CONTRIBUTING.rst HISTORY.rst README.rst
%{python_sitearch}/ewah_bool_utils
%exclude %{python_sitearch}/ewah_bool_utils/cpp/*
%{python_sitearch}/ewah_bool_utils-%{version}*-info

%files %{python_files devel}
%license LICENSE
%{python_sitearch}/ewah_bool_utils/cpp/*

%changelog
