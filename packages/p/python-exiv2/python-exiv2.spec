#
# spec file for package python-exiv2
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


Name:           python-exiv2
Version:        0.14.1
Release:        0
Summary:        Python3 bindings for the exiv2 library
License:        GPL-3.0-only
Group:          Development/Languages/Python
URL:            https://launchpad.net/py3exiv2
Source:         https://github.com/jim-easterbrook/python-exiv2/archive/refs/tags/%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libboost_python3-devel
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(exiv2)
%python_subpackages

%description
python3-exiv2 is a Python 3 binding to exiv2, the C++ library for manipulation
of EXIF, IPTC and XMP image metadata. It is a python 3 module that allows your
scripts to read and write metadata (EXIF, IPTC, XMP, thumbnails) embedded in
image files (JPEG, TIFF, ...).

It is designed as a high-level interface to the functionalities offered by
libexiv2. Using python’s built-in data types and standard modules, it provides
easy manipulation of image metadata.

%prep
%autosetup -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%files %{python_files}
%{python_sitearch}/exiv2
%{python_sitearch}/exiv2-%{version}*-info

%changelog
