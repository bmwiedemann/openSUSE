#
# spec file for package python-numcodecs
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


%{?sle15_python_module_pythons}
Name:           python-numcodecs
Version:        0.14.0
Release:        0
Summary:        Buffer compression and transformation codecs
License:        MIT
URL:            https://github.com/zarr-developers/numcodecs
Source:         https://files.pythonhosted.org/packages/source/n/numcodecs/numcodecs-%{version}.tar.gz
# PATCH-FEATURE-UPSTREAM numcodecs-pr569-systemlibs.patch gh#zarr-developers/numcodecs#569
Patch0:         numcodecs-pr569-systemlibs.patch
# PATCH-FIX-OPENSUSE numcodecs-blosc-snappy-test.patch code@bnavigator.de -- allow testing snappy from the systemlib c-blosc compressors
Patch1:         numcodecs-blosc-snappy-test.patch
# PATCH-FIX-UPSTREAM numcodecs-revert-subtract-pr584.patch -- gh#zarr-developers/numcodecs#584, gh#zarr-developers/numcodecs#653
Patch2:         numcodecs-revert-subtract-pr584.patch
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module base >= 3.10}
BuildRequires:  %{python_module numpy-devel >= 1.24}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pkgconfig}
BuildRequires:  %{python_module py-cpuinfo}
BuildRequires:  %{python_module setuptools > 64}
BuildRequires:  %{python_module setuptools_scm > 6.2}
BuildRequires:  %{python_module wheel}
BuildRequires:  blosc-devel >= 1.21.5
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(liblz4) >= 1.9.3
BuildRequires:  pkgconfig(libzstd) >= 1.5.5
BuildRequires:  pkgconfig(zlib) >= 1.2.13
Requires:       python-numpy >= 1.24
Suggests:       python-msgpack
Suggests:       python-pcodec
Suggests:       (python-zfpy >= 1 with python-numpy < 2)
# SECTION test requirements
BuildRequires:  %{python_module numpy >= 1.24}
BuildRequires:  %{python_module importlib-metadata}
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
# keep python310 for now. This will fail with the enablement of zarr3 tests
sed -i '/requires-python/ s/3.11/3.10/' pyproject.toml

%build
export CFLAGS="%{optflags}"
export NUMCODECS_USE_SYSTEM_LIBS=1
export DISABLE_NUMCODECS_AVX2=1
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# zarr 3 is not released yet, no crc32c in the distribution yet
%pytest_arch --pyargs numcodecs -rsfE --ignore=%{buildroot}%{$python_sitearch}/numcodecs/{zarr3.py,tests/test_zarr3_import.py,tests/test_checksum32.py}

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitearch}/numcodecs
%{python_sitearch}/numcodecs-%{version}.dist-info

%changelog
