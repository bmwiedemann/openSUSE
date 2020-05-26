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
%define         skip_python2 1
Name:           python-imagecodecs
Version:        2019.5.22
Release:        0
Summary:        Image transformation, compression, and decompression codecs
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://www.lfd.uci.edu/~gohlke/
Source:         https://files.pythonhosted.org/packages/source/i/imagecodecs/imagecodecs-%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module blosc}
BuildRequires:  %{python_module lz4}
BuildRequires:  %{python_module matplotlib >= 2.2}
BuildRequires:  %{python_module numpy-devel >= 1.11.3}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scikit-image}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module zstd}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  jxrlib-devel
BuildRequires:  libjpeg62-devel
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(blosc)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libopenjp2)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(zlib)
Requires:       python-numpy >= 1.11.3
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     python-Pillow
Recommends:     python-blosc
Recommends:     python-lz4
Recommends:     python-matplotlib >= 2.2
Recommends:     python-zstd
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
dos2unix README.rst
# prevent ImportError in CLI due to missing tifffile
sed -i '/from tifffile import imshow/d' imagecodecs/__main__.py

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/imagecodecs
%{python_expand rm -rf %{buildroot}%{$python_sitearch}/imagecodecs/licenses/
%fdupes %{buildroot}%{$python_sitearch}
}

%check
mv imagecodecs __imagecodecs
# Should add --doctest-modules %%{buildroot}%%{$python_sitearch}/imagecodecs/imagecodecs.py
# however doctests are currently broken
%pytest_arch tests
mv __imagecodecs imagecodecs

%post
%python_install_alternative imagecodecs

%postun
%python_uninstall_alternative imagecodecs

%files %{python_files}
%license LICENSE imagecodecs/licenses/*
%doc README.rst
%python_alternative %{_bindir}/imagecodecs
%{python_sitearch}/*

%changelog
