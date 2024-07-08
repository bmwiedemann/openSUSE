#
# spec file for package python-netCDF4
#
# Copyright (c) 2024 SUSE LLC
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


Name:           python-netCDF4
Version:        1.7.1.post1
Release:        0
Summary:        Python interface to netCDF 3 and 4
License:        HPND AND MIT
URL:            https://github.com/Unidata/netcdf4-python
Source:         https://files.pythonhosted.org/packages/source/n/netcdf4/netcdf4-%{version}.tar.gz
Source99:       python-netCDF4.rpmlintrc
BuildRequires:  %{python_module Cython >= 0.29}
BuildRequires:  %{python_module certifi}
BuildRequires:  %{python_module cftime}
BuildRequires:  %{python_module devel >= 3.7}
BuildRequires:  %{python_module numpy-devel >= 1.10.0 with %python-numpy-devel < 2}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 61}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  hdf5-devel >= 1.8.4
BuildRequires:  libcurl-devel
BuildRequires:  libjpeg-devel
BuildRequires:  netcdf-devel >= 4.2
BuildRequires:  python-rpm-macros
Requires:       hdf5 >= 1.8.4
Requires:       netcdf >= 4.2
Requires:       python-certifi
Requires:       python-cftime
Requires:       (python-numpy >= 1.10.0 with python-numpy < 2)
Requires(post): update-alternatives
Requires(postun): update-alternatives
# SECTION tests
BuildRequires:  %{python_module pytest}
BuildRequires:  netcdf
# /SECTION
%python_subpackages

%description
netCDF version 4 has many features not found in earlier versions of
the library and is implemented on  top of HDF5. This module can read
and write files in both the new netCDF 4 and the old netCDF 3
format, and can create files that are readable by HDF5 clients. The
API modelled after Scientific.IO.NetCDF, and should be familiar to
users of that module.

Most new features of netCDF 4 are implemented, such as multiple unlimited
dimensions, groups and zlib data compression. All the new numeric data types
(such as 64 bit and unsigned integer types) are implemented. Compound and
variable length (vlen) data types are supported, but the enum and opaque data
types are not. Mixtures of compound and vlen data types (compound types
containing vlens, and vlens containing compound types) are not supported.

%prep
%autosetup -p1 -n netcdf4-%{version}

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/ncinfo
%python_clone -a %{buildroot}%{_bindir}/nc4tonc3
%python_clone -a %{buildroot}%{_bindir}/nc3tonc4
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
pushd test
export NO_NET=1

# Broken test in s390x, gh#Unidata/netcdf4-python#1124
%ifarch s390x
rm tst_compoundvar.py
%endif

%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitearch}
$python run_all.py
}
popd

%post
%python_install_alternative ncinfo
%python_install_alternative nc4tonc3
%python_install_alternative nc3tonc4

%postun
%python_uninstall_alternative ncinfo
%python_uninstall_alternative nc4tonc3
%python_uninstall_alternative nc3tonc4

%files %{python_files}
%doc Changelog README.md
%license LICENSE
%python_alternative %{_bindir}/nc3tonc4
%python_alternative %{_bindir}/nc4tonc3
%python_alternative %{_bindir}/ncinfo
%{python_sitearch}/netCDF4
%{python_sitearch}/netCDF4-%{version}.dist-info

%changelog
