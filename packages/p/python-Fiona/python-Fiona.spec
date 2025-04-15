#
# spec file for package python-Fiona
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
Name:           python-Fiona
Version:        1.10.1
Release:        0
Summary:        Module for reading and writing spatial data files
License:        BSD-3-Clause
URL:            https://github.com/Toblerity/Fiona
Source:         https://files.pythonhosted.org/packages/source/f/fiona/fiona-%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel >= 3.9}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gdal
BuildRequires:  libgdal-devel
BuildRequires:  proj
BuildRequires:  proj-devel
BuildRequires:  python-rpm-macros
Requires:       python-attrs >= 19.2
Requires:       python-certifi
Requires:       python-click >= 8.0
Requires:       python-click-plugins
Requires:       python-cligj >= 0.5
Recommends:     python-Shapely
Recommends:     python-boto3
Recommends:     python-pyparsing
# SECTION test requirements
BuildRequires:  %{python_module Shapely}
BuildRequires:  %{python_module aiohttp}
BuildRequires:  %{python_module attrs >= 19.2}
BuildRequires:  %{python_module boto3}
BuildRequires:  %{python_module click >= 8.0}
BuildRequires:  %{python_module click-plugins}
BuildRequires:  %{python_module cligj >= 0.5}
BuildRequires:  %{python_module fsspec}
BuildRequires:  %{python_module pyparsing}
BuildRequires:  %{python_module pyproj}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytz}
# /SECTION
Recommends:     fiona-fio
%python_subpackages

%description
Fiona is OGR's spatial data API for Python programmers.

%package     -n fiona-fio
Summary:        Program for reading and writing spatial data files
Group:          Productivity/Scientific/Other
Requires:       python3-Fiona = %{version}
Conflicts:      fio
BuildArch:      noarch

%description -n fiona-fio
Command-line interface for reading and writing spatial data
using OGR's Fiona package.

%prep
%autosetup -p1 -n fiona-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# The following require network
skiptests="wheel or test_open_zip_https or test_open_http or test_collection_http or test_collection_zip_http or test_opener_fsspec_zip_http_fs"
# Reason for this failure not recorded
skiptests="$skiptests or GPSTrackMaker"
# December 2022: test_no_append_driver_cannot_append has started failing for FlatGeobuf and GeoJSONSeq only
skiptests="$skiptests or (test_no_append_driver_cannot_append and (FlatGeobuf or GeoJSONSeq))"

mv fiona fiona_temp
export GDAL_DATA=$(pkg-config --variable=datadir gdal)
export PROJ_LIB=$(pkg-config --variable=datadir proj)
export LANG=en_US.UTF-8
%pytest_arch -rs -k "not ($skiptests)"
mv fiona_temp fiona

%files %{python_files}
%doc CHANGES.txt CREDITS.txt README.rst
%license LICENSE.txt
%{python_sitearch}/fiona
%{python_sitearch}/fiona-%{version}.dist-info

%files -n fiona-fio
%license LICENSE.txt
%{_bindir}/fio

%changelog
