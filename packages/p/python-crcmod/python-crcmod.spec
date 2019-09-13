#
# spec file for package python-crcmod
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-crcmod
Version:        1.7
Release:        0
Summary:        CRC Generator
License:        MIT
Group:          Development/Languages/Python
Url:            http://crcmod.sourceforge.net/
Source:         https://files.pythonhosted.org/packages/source/c/crcmod/crcmod-%{version}.tar.gz
BuildRequires:  %{python_module base}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
The software in this package is a Python module for generating objects that
compute the Cyclic Redundancy Check (CRC).  There is no attempt in this package
to explain how the CRC works.  There are a number of resources on the web that
give a good explanation of the algorithms.  Just do a Google search for "crc
calculation" and browse till you find what you need.  Another resource can be
found in chapter 20 of the book "Numerical Recipes in C" by Press et. al.

This package allows the use of any 8, 16, 24, 32, or 64 bit CRC.  You can
generate a Python function for the selected polynomial or an instance of the
Crc class which provides the same interface as the ``md5`` and ``sha`` modules
from the Python standard library.  A ``Crc`` class instance can also generate
C/C++ source code that can be used in another application.

%prep
%setup -q -n crcmod-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}/crcmod

%files %{python_files}
%doc LICENSE README changelog
%{python_sitearch}/*

%changelog
