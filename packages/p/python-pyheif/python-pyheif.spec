#
# spec file for package python-pyheif
#
# Copyright (c) 2022 SUSE LLC
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


%define modname pyheif
%define skip_python2 1
%bcond_with x265
Name:           python-pyheif
Version:        0.7.0
Release:        0
Summary:        Python 3.6+ interface to libheif library
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://pypi.org/project/pyheif/
Source:         https://github.com/carsales/%{modname}/archive/refs/tags/release-%{version}.tar.gz#/%{modname}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE remove-piexif.patch -- don't check exif tags with piexif, we don't have it, code@bnavigator.de
Patch0:         remove-piexif.patch
# PATCH-FIX-OPENSUSE dont-test-x265-files.patch code@bnavigator.de
Patch1:         dont-test-x265-files.patch
BuildRequires:  %{python_module Pillow >= 7.1}
BuildRequires:  %{python_module cffi}
BuildRequires:  %{python_module devel >= 3.6}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  libheif-devel
BuildRequires:  python-rpm-macros
%python_subpackages

%description
libheif allows conversion of HEIC format images to other formats such as JPEG. pyheif is a python wrapper for libheif

%prep
%setup -q -n %{modname}-release-%{version}
%patch0 -p1
%if !%{with x265}
%patch1 -p1
%endif

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch

%files %{python_files}
%doc README.md
%{python_sitearch}/_libheif_cffi.*.so
%{python_sitearch}/%{modname}
%{python_sitearch}/%{modname}-%{version}*-info

%changelog
