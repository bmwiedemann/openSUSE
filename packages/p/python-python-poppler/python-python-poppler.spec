#
# spec file for package python-python-poppler
#
# Copyright (c) 2025 SUSE LLC
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


Name:           python-python-poppler
Version:        0.4.1
Release:        0
Summary:        Python binding to the poppler-cpp library
License:        GPL-2.0-only
URL:            https://github.com/cbrunet/python-poppler
Source:         https://github.com/cbrunet/python-poppler/archive/refs/tags/v%{version}.tar.gz#/python-poppler-%{version}.tar.gz
# PATCH-FEATURE-OPENSUSE Build against system pybind11
Patch0:         use-system-pybind11.patch
# PATCH-FIX-UPSTREAM gh#cbrunet/python-poppler#92
Patch1:         support-poppler-25.01.patch
BuildRequires:  %{python_module devel >= 3.7}
BuildRequires:  %{python_module meson-python}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pybind11-devel}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
BuildRequires:  c++_compiler
BuildRequires:  fdupes
BuildRequires:  ninja
BuildRequires:  pkg-config
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(poppler)
# some tests require this
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
rm -rf subprojects

%build
export CXXFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch tests

%files %{python_files}
%license LICENSE.txt
%doc README.md
%{python_sitearch}/poppler
%{python_sitearch}/python_poppler-%{version}.dist-info

%changelog
