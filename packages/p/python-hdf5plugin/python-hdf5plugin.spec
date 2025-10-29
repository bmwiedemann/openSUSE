#
# spec file for package python-hdf5plugin
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%bcond_without systemlibs
Name:           python-hdf5plugin
Version:        6.0.0
Release:        0
Summary:        Compression filters for h5py
License:        BSD-2-Clause AND MIT AND BSD-3-Clause AND CC-BY-3.0 AND Zlib
URL:            https://github.com/silx-kit/hdf5plugin
Source:         https://files.pythonhosted.org/packages/source/h/hdf5plugin/hdf5plugin-%{version}.tar.gz
# PATCH-FIX-UPSTREAM fix-bzip2-name.patch https://github.com/silx-kit/hdf5plugin/pull/367
Patch0:         fix-bzip2-name.patch
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module blosc2}
BuildRequires:  %{python_module h5py >= 3.0.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pkgconfig}
BuildRequires:  %{python_module py-cpuinfo >= 8.0.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel >= 0.34.0}
BuildRequires:  fdupes
BuildRequires:  hdf5-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(blosc)
BuildRequires:  pkgconfig(blosc2)
BuildRequires:  pkgconfig(bzip2)
# Cannot unbundle charls: fcidecomp expects charls < 2 with interface.h
# BuildRequires:  pkgconfig(charls)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  c++_compiler
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(snappy)
BuildRequires:  pkgconfig(zlib)
Requires:       python-h5py >= 3.0.0
# not for 32-bit
ExcludeArch:    %ix86 %arm
%python_subpackages

%description
hdf5plugin provides HDF5 compression filters
(namely: Blosc, Blosc2, BitShuffle, BZip2, FciDecomp, LZ4, SZ, SZ3, Zfp, ZStd)
and makes them usable from h5py.

%prep
%autosetup -p1 -n hdf5plugin-%{version}
sed -i '1{/^#/d}' src/hdf5plugin/_version.py
%if %{with systemlibs}
rm -r lib/hdf5
rm -r lib/bzip2
rm -r lib/c-blosc
rm -r lib/c-blosc2
rm -r lib/snappy
%endif

%build
export CFLAGS="%{optflags}"
export HDF5PLUGIN_HDF5_DIR=%{_prefix}
export HDF5PLUGIN_OPENMP=False
export HDF5PLUGIN_NATIVE=False
export HDF5PLUGIN_CPP11=True
export HDF5PLUGIN_CPP14=True
export HDF5PLUGIN_SSE3=False
export HDF5PLUGIN_AVX512=False
# Note: it is possible to remove all filters from embedding and make this a pure API package,
# But registering system provided filters for consumers like python-fabio is not straight forward
# gh#silx-kit/hdf5plugin#162, gh#silx-kit/hdf5plugin#169, gh#silx-kit/hdf5plugin#188
# export HDF5PLUGIN_STRIP=all
# Full set: bzip2,lz4,bshuffle,blosc,blosc2,fcidecomp,zfp,zstd,sz,sz3

%if %{with systemlibs}
export HDF5PLUGIN_SYSTEM_LIBRARIES=blosc,blosc2,bzip2,lz4,snappy,zlib,zstd
%endif
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}
for l in \
%if !%{with systemlibs}
  lib/bzip2/LICENSE
  lib/c-blosc/LICENSES/*
  lib/c-blosc2/LICENSES/*
  lib/charls/src/License.txt \
  lib/snappy/COPYING
  lib/LZ4/COPYING \
  lib/LZ4/LICENSE \
%endif
  lib/bitshuffle/LICENSE \
  lib/hdf5-blosc/LICENSES/* \
  lib/PyTables/LICENSE.txt \
  lib/fcidecomp/LICENSE \
  lib/SZ/copyright-and-BSD-license.txt \
  lib/SZ3/copyright-and-BSD-license.txt \
  lib/H5Z-ZFP/LICENSE \
  lib/zfp/LICENSE \
  lib/HDF5Plugin-Zstandard/LICENSE
do
  d=$(dirname $l)
  mkdir -p pluginlicenses/$d
  cp $l pluginlicenses/$d
done

%check
export PYTHONDONTWRITEBYTECODE=1
%{python_expand export PYTHONPATH=%{buildroot}/%{$python_sitearch}
$python test/test.py
}

%files %{python_files}
%doc CHANGELOG.rst README.rst
%license LICENSE pluginlicenses
%{python_sitearch}/hdf5plugin
%{python_sitearch}/hdf5plugin-%{version}.dist-info

%changelog
