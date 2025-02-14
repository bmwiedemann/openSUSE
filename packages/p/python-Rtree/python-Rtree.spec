#
# spec file for package python-Rtree
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
Name:           python-Rtree
Version:        1.3.0
Release:        0
Summary:        R-Tree spatial index for Python GIS
License:        MIT
URL:            https://github.com/Toblerity/rtree
Source:         https://files.pythonhosted.org/packages/source/R/Rtree/rtree-%{version}.tar.gz
Source99:       python-Rtree-rpmlintrc
# PATCH-FIX-OPENSUSE Rtree-opensuse-noarch.patch -- we don't put spatialindex into a wheel so the module is kept pure. <code@bnavigator.de>
Patch0:         Rtree-opensuse-noarch.patch
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
# only for the shlib requirement, no headers needed
BuildRequires:  spatialindex-devel
BuildRequires:  python-rpm-macros
# Since this is noarch, _libdir doesn't work for 64 bit arches
Requires:       %(rpm -q --queryformat "%%{NAME}" -f $(readlink -f /usr/lib*/libspatialindex.so))
Provides:       python-rtree = %{version}-%{release}
BuildArch:      noarch
%python_subpackages

%description
A ctypes Python wrapper of libspatialindex that provides a number of advanced
spatial indexing features for the spatially curious Python user.

* Nearest neighbor search
* Intersection search
* Multi-dimensional indexes
* Clustered indexes (store Python pickles directly with index entries)
* Bulk loading
* Deletion
* Disk serialization
* Custom storage implementation (to implement spatial indexing in ZODB,
  for example)

%prep
%autosetup -p1 -n rtree-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE.txt
%{python_sitelib}/rtree
%{python_sitelib}/Rtree-%{version}.dist-info

%changelog
