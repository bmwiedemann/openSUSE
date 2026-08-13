#
# spec file for package python-jxlpy
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define         modname jxlpy
Name:           python-jxlpy
Version:        0.9.5
Release:        0
Summary:        Cython bindings and Pillow plugin for JPEG XL
License:        MIT
URL:            https://github.com/olokelo/jxlpy
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(libjxl)
%python_subpackages

%description
This module introduces reading and writing support for JPEG XL directly from
Python 3.

JXLPy is based on JPEG XL implementation in imagecodecs but doesn't it require
Numpy and any external dependencies besides Cython and libjxl.

It also provides support for Pillow via plugin.

%prep
%autosetup -n %{modname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitearch}/%{modname}
%{python_sitearch}/%{modname}-%{version}.dist-info
%{python_sitearch}/_%{modname}.cpython-%{python_version_nodots}-%{_arch}-linux-gnu.so

%changelog
