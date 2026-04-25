#
# spec file for package python-blosc2
#
# Copyright (c) 2026 SUSE LLC and contributors
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
# See CMakeLists.txt
%define miniexpr_commit 37bf6982bf9619036b47f095b7005bc3c87a7447
%define minicc_commit 41208bdc85612042f363f425cda4601b3ed90d64
Name:           python-blosc2
Version:        4.1.2
Release:        0
Summary:        Python wrapper for the C-Blosc2 library
License:        BSD-3-Clause
URL:            https://github.com/Blosc/python-blosc2
Source:         https://files.pythonhosted.org/packages/source/b/blosc2/blosc2-%{version}.tar.gz
Source1:        https://github.com/Blosc/miniexpr/archive/%{miniexpr_commit}.tar.gz#/miniexpr-%{miniexpr_commit}.tar.gz
# PATCH-FIX-OPENSUSE miniexpr-no-license-install.patch code@bnavigator.de -- Don't the license files into python platlib
Patch0:         miniexpr-no-license-install.patch
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel >= 3.10}
BuildRequires:  %{python_module numpy-devel >= 1.26}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module scikit-build-core}
BuildRequires:  c++_compiler
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(blosc2) >= 2.14.1
Requires:       python-msgpack
Requires:       python-ndindex
Requires:       python-numexpr >= 2.14.1
Requires:       python-numpy >= 1.26
Requires:       python-requests
# SECTION test requirements
BuildRequires:  %{python_module msgpack}
BuildRequires:  %{python_module ndindex}
BuildRequires:  %{python_module numexpr >= 2.14.1}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
# /SECTION
%python_subpackages

%description
Blosc (https://blosc.org) is a high performance compressor optimized
for binary data. It has been designed to transmit data to the processor
cache faster than the traditional, non-compressed, direct memory fetch
approach via a memcpy() OS call.

Blosc works well for compressing numerical arrays that contains data
with relatively low entropy, like sparse data, time series, grids with
regular-spaced values, etc.

python-blosc2 is a Python package that wraps C-Blosc2, the newest version
of the Blosc compressor. Currently python-blosc2 already reproduces the
API of python-blosc, so the former can be used as a drop-in replacement
for the later.

%prep
%autosetup -p1 -n blosc2-%{version} -a1

%build
export CFLAGS="%{optflags}"
export CPPFLAGS="%{optflags}"
# debundle c-blosc2
export USE_SYSTEM_BLOSC2=1
# See the CMakeLists.txt files for the repos and their commit hashes
SKBUILD_CMAKE_DEFINE="FETCHCONTENT_SOURCE_DIR_MINIEXPR=$PWD/miniexpr-%{miniexpr_commit}"
# This bundles libtcc.so and .h weirdly into python platlib. See also the PyPI wheels. Don't do that.
SKBUILD_CMAKE_DEFINE="${SKBUILD_CMAKE_DEFINE};MINIEXPR_ENABLE_TCC_JIT=OFF"
SKBUILD_CMAKE_DEFINE="${SKBUILD_CMAKE_DEFINE};MINIEXPR_USE_SLEEF=OFF"
export SKBUILD_CMAKE_DEFINE
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# segfault without TCC_JIT
donttest="test_dsl_save_clamp"
%ifarch %ix86 %arm32
# too large for address memory
donttest="$donttest or (test_pack and int64)"
%endif
# https://lists.opensuse.org/archives/list/buildservice@lists.opensuse.org/thread/WZC3YN2NFHGJJPUTFBF4LFYXDM7MJEZT
# Don't test on Python 3.14, it crashes on OBS, disable and test locally to be sure it works for users.
python314_donttest="--setup-only"
%pytest_arch -k "not ($donttest)" ${$python_donttest}

%files %{python_files}
%doc README.rst
%license LICENSE.txt miniexpr-%{miniexpr_commit}/LICENSE miniexpr-%{miniexpr_commit}/LICENSE-TINYEXPR miniexpr-%{miniexpr_commit}/THIRD_PARTY_NOTICES.md
%{python_sitearch}/blosc2
%{python_sitearch}/blosc2-%{version}.dist-info

%changelog
