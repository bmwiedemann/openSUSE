#
# spec file for package python-blosc2
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


Name:           python-blosc2
Version:        2.1.1
Release:        0
Summary:        Python wrapper for the C-Blosc2 library
License:        BSD-3-Clause
URL:            https://github.com/Blosc/python-blosc2
Source:         https://files.pythonhosted.org/packages/source/b/blosc2/blosc2-%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel >= 3.8}
BuildRequires:  %{python_module numpy-devel >= 1.20.3}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module scikit-build}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  c++_compiler
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(blosc2)
Requires:       python-msgpack
Requires:       python-ndindex >= 1.4
Requires:       python-numpy >= 1.20.3
Requires:       python-py-cpuinfo
Requires:       python-rich
# SECTION test requirements
BuildRequires:  %{python_module msgpack}
BuildRequires:  %{python_module ndindex >= 1.4}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module py-cpuinfo}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module rich}
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
%autosetup -p1 -n blosc2-%{version}
# https://github.com/Blosc/python-blosc2/commit/f5fbba3a4f6b935da53563a6a0001f917dc407ab
sed -i /pytest/d requirements-runtime.txt

%build
export CFLAGS="%{optflags}"
export CPPFLAGS="%{optflags}"
# debundle c-blosc2
export SKBUILD_CONFIGURE_OPTIONS="-DUSE_SYSTEM_BLOSC2:BOOL=ON"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
mv blosc2 blosc2-src
donttest="dummyprefix"
%ifarch %ix86 %arm32
# too large for address memory
donttest="$donttest or (test_pack and int64)"
%endif
%pytest_arch -k "not ($donttest)"

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitearch}/blosc2
%{python_sitearch}/blosc2-%{version}.dist-info

%changelog
