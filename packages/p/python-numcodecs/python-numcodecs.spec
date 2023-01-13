#
# spec file for package python-numcodecs
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


Name:           python-numcodecs
Version:        0.11.0
Release:        0
Summary:        Buffer compression and transformation codecs
License:        MIT
URL:            https://github.com/zarr-developers/numcodecs
Source:         https://files.pythonhosted.org/packages/source/n/numcodecs/numcodecs-%{version}.tar.gz
# PATCH-FEATURE-UPSTREAM unbundle-libs.patch -- unbundle system libs gh#zarr-developers/numcodecs#264
Patch0:         unbundle-libs.patch
# PATCH-FIX-UPSTREAM numcodecs-pr417-raggednumpy.patch gh#zarr-developers/numcodecs#417
Patch1:         numcodecs-pr417-raggednumpy.patch
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module py-cpuinfo}
BuildRequires:  %{python_module setuptools > 64}
BuildRequires:  %{python_module setuptools_scm > 6.2}
BuildRequires:  %{python_module wheel}
BuildRequires:  blosc-devel
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(zlib)
Requires:       python-entrypoints
Requires:       python-numpy >= 1.7
Suggests:       python-msgpack
Suggests:       python-zfpy >= 1
# SECTION test requirements
BuildRequires:  %{python_module numpy >= 1.7}
BuildRequires:  %{python_module entrypoints}
BuildRequires:  %{python_module msgpack}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
A Python package providing buffer compression and transformation codecs for use
in data storage and communication applications.

%prep
%autosetup -p1 -n numcodecs-%{version}
# use system libraries instead of bundled ones
rm -r c-blosc
sed -i 's/--cov=numcodecs --cov-report xml//' pyproject.toml

%build
export CFLAGS="%{optflags}"
export DISABLE_NUMCODECS_AVX2=1
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch --pyargs numcodecs -rsfE

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitearch}/numcodecs
%{python_sitearch}/numcodecs-%{version}*-info

%changelog
