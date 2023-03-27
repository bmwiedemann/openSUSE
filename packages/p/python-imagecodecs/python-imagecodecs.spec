#
# spec file
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif

Name:           python-imagecodecs%{psuffix}
Version:        2023.3.16
Release:        0
Summary:        Image transformation, compression, and decompression codecs
License:        BSD-3-Clause
URL:            https://github.com/cgohlke/imagecodecs/
Source:         https://files.pythonhosted.org/packages/source/i/imagecodecs/imagecodecs-%{version}.tar.gz
Source1:        imagecodecs_distributor_setup.py
Patch0:         always-cythonize.patch
BuildRequires:  %{python_module Cython >= 0.29.19}
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-numpy
Requires(post): update-alternatives
Requires(postun):update-alternatives
Recommends:     python-Pillow
Recommends:     python-blosc
Recommends:     python-lz4
Recommends:     python-matplotlib >= 3.3
Recommends:     python-numcodecs
Recommends:     python-tifffile
Recommends:     python-zstd
%if %{with test}
BuildRequires:  %{python_module Brotli}
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module blosc}
BuildRequires:  %{python_module czifile}
BuildRequires:  %{python_module dask if %python-base < 3.11}
BuildRequires:  %{python_module dask-array if %python-base < 3.11}
BuildRequires:  %{python_module dask-delayed if %python-base < 3.11}
BuildRequires:  %{python_module imagecodecs >= %{version}}
BuildRequires:  %{python_module lz4}
BuildRequires:  %{python_module matplotlib >= 3.3}
BuildRequires:  %{python_module numcodecs}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-snappy}
BuildRequires:  %{python_module scikit-image}
BuildRequires:  %{python_module tifffile}
BuildRequires:  %{python_module zarr}
BuildRequires:  %{python_module zstd}
# libraries and python modules not (yet) available:
#BuildRequires:  %%{python_module bitshuffle}
#BuildRequires:  %%{python_module lzf}
# The zopfli library is linked. User can pip install zopflipy, if needed.
#BuildRequires:  %%{python_module zopflipy}
# The lzfse library is linked. User can pip install pyliblzfse, if needed.
#BuildRequires:  %%{python_module pyliblzfse}
%else
BuildRequires:  CharLS-devel
BuildRequires:  dav1d-devel
BuildRequires:  gcc-c++
BuildRequires:  giflib-devel
BuildRequires:  jxrlib-devel
BuildRequires:  libaec-devel
BuildRequires:  libaom-devel
BuildRequires:  libdeflate-devel
BuildRequires:  libzopfli-devel
BuildRequires:  lzfse-devel
BuildRequires:  lzham_codec-devel
BuildRequires:  pkgconfig
BuildRequires:  rav1e-devel
BuildRequires:  snappy-devel
BuildRequires:  sz2-devel
BuildRequires:  pkgconfig(blosc)
BuildRequires:  pkgconfig(blosc2) >= 2.7.1
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(cfitsio)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libbrotlicommon)
BuildRequires:  pkgconfig(libheif)
# Beta, not available in minimum version
#BuildRequires:  pkgconfig(libturbojpeg) >= 2.1.91
BuildRequires:  pkgconfig(libjxl) >= 0.8
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libopenjp2)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(zlib-ng)
%ifnarch %ix86 %arm
# Note that upstream deprecated 32-bit as a whole
# 64-bit only.
BuildRequires:  zfp-devel
BuildRequires:  pkgconfig(SvtAv1Dec)
BuildRequires:  pkgconfig(SvtAv1Enc)
# 32-bit tests fail
BuildRequires:  pkgconfig(libavif)
%endif
%endif
%python_subpackages

%description
Imagecodecs is a Python library that provides block-oriented, in-memory buffer
transformation, compression, and decompression functions for use in the
tifffile, czifile, and other scientific imaging modules.

Decode and/or encode functions are implemented for Zlib (DEFLATE), GZIP,
ZStandard (ZSTD), Blosc, Brotli, Snappy, LZMA, BZ2, LZ4, LZ4F, LZ4HC, LZW, LZF,
ZFP, AEC, LERC, NPY, PNG, GIF, TIFF, WebP, JPEG 8-bit, JPEG 12-bit, Lossless
JPEG (LJPEG, SOF3), JPEG 2000, JPEG LS, JPEG XR, JPEG XL, AVIF, PackBits, Packed
Integers, Delta, XOR Delta, Floating Point Predictor, Bitorder reversal,
Bitshuffle, and Float24 (24-bit floating point).

%prep
%setup -q -n imagecodecs-%{version}
# the patch from github requires unix line endings to apply
dos2unix tests/test_imagecodecs.py
%autopatch -p1

cp %SOURCE1 ./
dos2unix README.rst
# These libraries are not linked to, (check SOURCE1)
rm imagecodecs/licenses/LICENSE-brunsli
rm imagecodecs/licenses/LICENSE-jetraw
rm imagecodecs/licenses/LICENSE-lerc
rm imagecodecs/licenses/LICENSE-mozjpeg

%build
%if !%{with test}
export CFLAGS="%{optflags}"
export INCDIR="%{_includedir}"
%pyproject_wheel
%endif

%install
%if !%{with test}
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/imagecodecs
%{python_expand rm -rf %{buildroot}%{$python_sitearch}/imagecodecs/licenses/
%fdupes %{buildroot}%{$python_sitearch}
}
%endif

%check
%if %{with test}
# All heif tests fail because of unsupported filetypes (openSUSE does not ship patentend codec support with libheif)
donttest="heif"
# no webp and lerc support in libtiff, jpeg8 disabled in imagecodecs
donttest="$donttest or (test_tiff and (webp or lerc or jpeg))"
%ifarch %ix86 %arm32
donttest="$donttest or spng"
%endif
# no dask because of numba for python 3.11
python311_donttest="or imagecodecs.imagecodecs"
%pytest_arch -n auto tests -rsXfE --doctest-modules %{$python_sitearch}/imagecodecs/imagecodecs.py -k "not ($donttest ${$python_donttest})"
%endif

%if !%{with test}
%post
%python_install_alternative imagecodecs

%postun
%python_uninstall_alternative imagecodecs

%files %{python_files}
%license LICENSE imagecodecs/licenses/*
%doc README.rst
%python_alternative %{_bindir}/imagecodecs
%{python_sitearch}/imagecodecs-%{version}.dist-info/
%{python_sitearch}/imagecodecs/
%endif

%changelog
