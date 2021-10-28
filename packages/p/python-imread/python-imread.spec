#
# spec file for package python-imread
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
%define skip_python36 1
Name:           python-imread
Version:        0.7.4
Release:        0
Summary:        Image reading library
License:        MIT
URL:            http://luispedro.org/software/imread
Source:         https://files.pythonhosted.org/packages/source/i/imread/imread-%{version}.tar.gz
# https://github.com/luispedro/imread/issues/39
Patch0:         python-imread-remove-nose.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  c++_compiler
BuildRequires:  fdupes
BuildRequires:  giflib-devel
BuildRequires:  libtiff-devel
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libwebp)
Requires:       python-numpy
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Mahotas-imread is a simple module with a small number of functions:

imread
    Reads an image file
imread_multi
    Reads an image file with multiple images. Currently, TIFF and STK (a TIFF
    sub-based format) support this function.
imsave
    Writes an image file

%prep
%setup -q -n imread-%{version}
%patch0 -p1

%build
export EXCLUDE_WEBP=0
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
find -name '_imread.*.so' -exec cp {} imread \;
pushd imread
%pytest_arch

%files %{python_files}
%doc ChangeLog README.rst
%license COPYING.MIT
%{python_sitearch}/*

%changelog
