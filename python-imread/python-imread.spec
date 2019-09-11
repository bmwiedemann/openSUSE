#
# spec file for package python-imread
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-imread
Version:        0.7.1
Release:        0
Summary:        Image reading library
License:        MIT
Group:          Development/Languages/Python
Url:            http://luispedro.org/software/imread
Source:         https://files.pythonhosted.org/packages/source/i/imread/imread-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  c++_compiler
BuildRequires:  fdupes
BuildRequires:  giflib-devel
BuildRequires:  libtiff-devel
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libwebp)
# SECTION test requirements
BuildRequires:  %{python_module nose}
# /SECTION
BuildRequires:  python-numpy
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
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

%build
export EXCLUDE_WEBP=0
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%python_exec setup.py test

%files %{python_files}
%defattr(-,root,root,-)
%doc ChangeLog README.rst
%license COPYING.MIT
%{python_sitearch}/*

%changelog
