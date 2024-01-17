#
# spec file for package python-cftime
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


%{?sle15_python_module_pythons}
Name:           python-cftime
Version:        1.6.3
Release:        0
Summary:        Time-handling functionality from netcdf4-python
License:        MIT
URL:            https://github.com/Unidata/cftime
Source:         https://files.pythonhosted.org/packages/source/c/cftime/cftime-%{version}.tar.gz
BuildRequires:  %{python_module Cython >= 0.29.20}
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools >= 18.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Cython >= 0.29.20
Requires:       python-numpy
%python_subpackages

%description
Time-handling functionality from netcdf4-python.
Was split out from netcfd4-python in 2016.

%prep
%autosetup -p1 -n cftime-%{version}
# do not require cov/xdist/etc
rm setup.cfg

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%python_expand PYTHONPATH="%{buildroot}%{$python_sitearch}" py.test-%{$python_bin_suffix} -v

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitearch}/*

%changelog
