#
# spec file for package python-numcodecs
#
# Copyright (c) 2021 SUSE LLC
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
%define skip_python2 1
%define skip_python36 1
Name:           python-numcodecs
Version:        0.7.3
Release:        0
Summary:        Buffer compression and transformation codecs
License:        MIT
URL:            https://github.com/zarr-developers/numcodecs
Source:         https://files.pythonhosted.org/packages/source/n/numcodecs/numcodecs-%{version}.tar.gz
# PATCH-FEATURE-UPSTREAM unbundle-libs.patch -- unbundle system libs
Patch0:         unbundle-libs.patch
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module setuptools > 18.0}
BuildRequires:  %{python_module setuptools_scm > 1.5.4}
BuildRequires:  blosc-devel
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(zlib)
Requires:       python-numpy >= 1.7
Suggests:       python-msgpack
# SECTION test requirements
BuildRequires:  %{python_module numpy >= 1.7}
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

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitearch}/numcodecs
%{python_sitearch}/numcodecs-%{version}*-info

%changelog
