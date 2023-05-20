#
# spec file for package python-pyheif
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


%bcond_with x265
Name:           python-pyheif
Version:        0.7.1
Release:        0
Summary:        Python 3.6+ interface to libheif library
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://pypi.org/project/pyheif/
Source:         https://github.com/carsales/pyheif/archive/refs/tags/release-%{version}.tar.gz#/pyheif-%{version}.tar.gz
# PATCH-FIX-UPSTREAM pyheif-pr85-update-heif-h.patch gh#carsales/pyheif#85
Patch0:         pyheif-pr85-update-heif-h.patch
# PATCH-FIX-OPENSUSE remove-piexif.patch -- don't check exif tags with piexif, we don't have it, code@bnavigator.de
Patch1:         remove-piexif.patch
# PATCH-FIX-OPENSUSE dont-test-x265-files.patch code@bnavigator.de
Patch2:         dont-test-x265-files.patch
BuildRequires:  %{python_module Pillow >= 7.1}
BuildRequires:  %{python_module cffi >= 1.0.0}
BuildRequires:  %{python_module devel >= 3.6}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  libheif-devel >= 1.16
BuildRequires:  python-rpm-macros
Requires:       python-cffi >= 1.0.0
%python_subpackages

%description
libheif allows conversion of HEIC format images to other formats such as JPEG. pyheif is a python wrapper for libheif

%prep
%setup -q -n pyheif-release-%{version}
%patch0 -p1
%patch1 -p1
%if !%{with x265}
%patch2 -p1
%endif

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch

%files %{python_files}
%doc README.md
%{python_sitearch}/_libheif_cffi.*.so
%{python_sitearch}/pyheif
%{python_sitearch}/pyheif-%{version}.dist-info

%changelog
