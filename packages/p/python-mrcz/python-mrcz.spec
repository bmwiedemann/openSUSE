#
# spec file for package python-mrcz
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
%bcond_without python2
Name:           python-mrcz
Version:        0.5.6
Release:        0
Summary:        MRCZ meta-compressed image file-format library
License:        BSD-3-Clause
URL:            https://github.com/em-MRCZ/python-mrcz
Source:         https://github.com/em-MRCZ/python-mrcz/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module blosc}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-blosc
Requires:       python-numpy
BuildArch:      noarch
%if %{with python2}
BuildRequires:  python-enum34
BuildRequires:  python-futures
%endif
%ifpython2
Requires:       python-enum34
Requires:       python-futures
%endif
%python_subpackages

%description
mrcz is a package designed to supplement the venerable MRC image file
format with a highly efficient compressed variant, using the blosc
meta-compressor library to shrink files on disk and greatly accelerate
file input/output for the era of "Big Data" in electron and optical
microscopy.

%prep
%setup -q

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc AUTHORS.txt README.rst
%license LICENSE.txt
%dir %{python_sitelib}/mrcz/
%pycache_only %{python_sitelib}/mrcz-%{version}-py%{python_version}.egg-info/
%pycache_only %{python_sitelib}/mrcz/*.py
%pycache_only %{python_sitelib}/mrcz/__pycache__/

%changelog
