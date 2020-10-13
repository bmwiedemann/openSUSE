#
# spec file for package python-python-poppler
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2020 LISA GmbH ,Bingen, Germany
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
Name:           python-python-poppler
Version:        0.2.2
Release:        0
Summary:        Python binding to the poppler-cpp library
License:        GPL-2.0-only
Group:          Development/Libraries/Python
URL:            https://github.com/cbrunet/python-poppler
Source:         python-poppler-%{version}.tar.xz
Patch:          use-system-pybind11.patch
BuildRequires:  python3
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pybind11-devel}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  pkg-config
BuildRequires:  c++_compiler
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(poppler)
# some tests require this this
BuildRequires:  poppler-data
%python_subpackages

%description
python-poppler is a Python binding to the poppler-cpp library. It allows to
read, render, or modify PDF documents. More specifically, it currently allows
to:
    read an modify document meta data;
    list and read embedded documents;
    list the fonts used by the document;
    search or extract text on a given page of the document;
    render a page to a raw image;
    get info about transitions effects between the pages;
    read the table of contents of the document.

%prep
%autosetup -p1 -n python-poppler-%version
sed -i -e 's/-j2/%{?_smp_mflags}/' setup.py

%build
export CXXFLAGS="%{optflags}"
%python_build --debug

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch tests

%files %{python_files}
%license LICENSE.txt
%doc README.md 
%{python_sitearch}/

%changelog
