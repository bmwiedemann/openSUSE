#
# spec file for package python-imagecodecs
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
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%define         skip_python2 1
Name:           python-imagecodecs%{psuffix}
Version:        2020.5.30
Release:        0
Summary:        Image transformation, compression, and decompression codecs
License:        BSD-3-Clause
URL:            https://www.lfd.uci.edu/~gohlke/
Source:         https://files.pythonhosted.org/packages/source/i/imagecodecs/imagecodecs-%{version}.tar.gz
Patch0:         always-cythonize.patch
Patch1:         zopfli-headers.patch
BuildRequires:  %{python_module Cython >= 0.29.19}
BuildRequires:  %{python_module numpy-devel >= 1.15.1}
BuildRequires:  %{python_module setuptools >= 18.0}
BuildRequires:  dos2unix
BuildRequires:  fdupes
Requires:       python-numpy >= 1.15.1
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     python-Pillow
Recommends:     python-blosc
Recommends:     python-lz4
Recommends:     python-matplotlib >= 3.1
Recommends:     python-tifffile >= 2020.5.25
Recommends:     python-zstd
%if %{with test}
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module blosc}
BuildRequires:  %{python_module imagecodecs >= %{version}}
BuildRequires:  %{python_module lz4}
BuildRequires:  %{python_module matplotlib >= 3.1}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scikit-image}
BuildRequires:  %{python_module tifffile >= 2020.5.25}
BuildRequires:  %{python_module zstd}
%else
BuildRequires:  gcc-c++
BuildRequires:  giflib-devel
BuildRequires:  jxrlib-devel
BuildRequires:  libaec-devel
BuildRequires:  libzopfli-devel
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  snappy-devel
BuildRequires:  pkgconfig(blosc)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libbrotlicommon)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libopenjp2)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(zlib)
%endif
%python_subpackages

%description
Imagecodecs is a Python library that provides block-oriented, in-memory buffer
transformation, compression, and decompression functions for use in the
tifffile, czifile, and other scientific imaging modules.

Decode and/or encode functions are currently implemented for Zlib DEFLATE,
ZStandard, Blosc, LZMA, BZ2, LZ4, LZW, LZF, ZFP, NPY, PNG, WebP, JPEG 8-bit,
JPEG 12-bit, JPEG SOF3, JPEG LS, JPEG 2000, JPEG XR, PackBits, Packed Integers,
Delta, XOR Delta, Floating Point Predictor, and Bitorder reversal.

%prep
%setup -q -n imagecodecs-%{version}
%autopatch -p1

dos2unix README.rst

%build
%if !%{with test}
export CFLAGS="%{optflags}"
%python_build
%endif

%install
%if !%{with test}
%python_install
%python_clone -a %{buildroot}%{_bindir}/imagecodecs
%{python_expand rm -rf %{buildroot}%{$python_sitearch}/imagecodecs/licenses/
%fdupes %{buildroot}%{$python_sitearch}
}
%endif

%check
%if %{with test}
mv imagecodecs __imagecodecs
# Should add --doctest-modules %%{buildroot}%%{$python_sitearch}/imagecodecs/imagecodecs.py
# however doctests are currently broken
%pytest_arch tests
mv __imagecodecs imagecodecs
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
%{python_sitearch}/*
%endif

%changelog
