#
# spec file for package python-Fiona
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
Name:           python-Fiona
Version:        1.8.6
Release:        0
Summary:        Module for reading and writing spatial data files
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            http://github.com/Toblerity/Fiona
Source:         https://files.pythonhosted.org/packages/source/F/Fiona/Fiona-%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gdal
BuildRequires:  libgdal-devel
BuildRequires:  proj
BuildRequires:  proj-devel
BuildRequires:  python-rpm-macros
Requires:       python-attrs >= 17
Requires:       python-click >= 4.0
Requires:       python-click-plugins >= 1.0
Requires:       python-cligj
Requires:       python-gdal
Requires:       python-munch
Requires:       python-six >= 1.7
Recommends:     python-Shapely
Recommends:     python-boto3
# SECTION test requirements
BuildRequires:  %{python_module Shapely}
BuildRequires:  %{python_module attrs >= 17}
BuildRequires:  %{python_module boto3}
BuildRequires:  %{python_module click >= 4.0}
BuildRequires:  %{python_module click-plugins >= 1.0}
BuildRequires:  %{python_module cligj}
BuildRequires:  %{python_module munch}
BuildRequires:  %{python_module pyproj}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module six >= 1.7}
BuildRequires:  python-enum34
BuildRequires:  python-mock
# /SECTION
%ifpython3
Recommends:     fiona-fio
%endif
%ifpython2
Requires:       python-enum34
%endif
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
%setup -q -n Fiona-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
mv fiona fiona_temp
export GDAL_DATA=$(pkg-config --variable=datadir gdal)
export PROJ_LIB=$(pkg-config --variable=libdir proj)
export LANG=en_US.UTF-8
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitearch}
py.test-%{$python_bin_suffix} -m "not wheel" \
                              -k "not test_open_zip_https and not test_open_http and not test_collection_http and not test_collection_zip_http and not test_encoding_option_warning" \
                              --ignore=_build.python2 --ignore=_build.python3 --ignore=_build.pypy3 -v
}
mv fiona_temp fiona

%files %{python_files}
%doc CHANGES.txt CREDITS.txt README.rst
%license LICENSE.txt
%{python_sitearch}/*

%files -n fiona-fio
%license LICENSE.txt
%{_bindir}/fio

%changelog
