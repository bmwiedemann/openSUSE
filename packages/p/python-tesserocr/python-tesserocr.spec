#
# spec file for package python-tesserocr
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
Name:           python-tesserocr
Version:        2.4.1
Release:        0
Summary:        A Python wrapper around tesseract-ocr
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/sirfz/tesserocr
Source:         https://files.pythonhosted.org/packages/source/t/tesserocr/tesserocr-%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  tesseract-ocr-traineddata-english
BuildRequires:  tesseract-ocr-traineddata-orientation_and_script_detection
BuildRequires:  pkgconfig(tesseract)
Requires:       tesseract-ocr-traineddata-english
Requires:       tesseract-ocr-traineddata-orientation_and_script_detection
Recommends:     python-Pillow
%python_subpackages

%description
A wrapper around the tesseract-ocr API for Optical Character
Recognition (OCR).

tesserocr integrates directly with Tesseract's C++ API using Cython
which allows for Pythonic source code. It enables real concurrent
execution when used with Python's threading module by releasing the
GIL while processing an image in tesseract.

%prep
%setup -q -n tesserocr-%{version}

%build
%python_build

%install
%python_install

%check
%python_exec setup.py develop --user
%python_exec -m pytest -v tests

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitearch}/*

%changelog
