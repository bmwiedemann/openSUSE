#
# spec file for package python-pillow-heif
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


%bcond_with     x265
%bcond_with     libde265
%define         BUILD_ORIG 0
Name:           python-pillow-heif
Version:        0.16.0
Release:        0
Summary:        Python interface for libheif library
License:        BSD-3-Clause
URL:            https://github.com/bigcat88/pillow_heif
Source:         https://files.pythonhosted.org/packages/source/p/pillow-heif/pillow_heif-%{version}.tar.gz#/python-pillow-heif-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 67.8}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(aom) >= 3.3.0
BuildRequires:  pkgconfig(libavif)
BuildRequires:  pkgconfig(libheif) >= 1.17.0
%if %{with x265}
BuildRequires:  pkgconfig(libde265} >= 1.0.8
BuildRequires:  pkgconfig(x265)
%endif
# SECTION test requirements
BuildRequires:  %{python_module Pillow >= 9.5.0}
BuildRequires:  %{python_module Pympler}
BuildRequires:  %{python_module defusedxml}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module opencv}
BuildRequires:  %{python_module pytest >= 6.0.0}
# /SECTION
Requires:       python-Pillow >= 9.5.0
%python_subpackages

%description
Python interface for libheif library

%prep
%autosetup -p1 -n pillow_heif-%{version}

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%if 0%{BUILD_ORIG}
# tests need nonfree codecs
%check
%pytest
%endif

%files %{python_files}
%{python_sitearch}/pillow_heif
%{python_sitearch}/pillow_heif-%{version}.dist-info
%{python_sitearch}/_pillow_heif.cpython-*.so

%changelog
