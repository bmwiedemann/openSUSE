#
# spec file for package python-parted
#
# Copyright (c) 2025 SUSE LLC
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


%define srcname pyparted
Name:           python-parted
Version:        3.13.0
Release:        0
Summary:        Python module for GNU parted
License:        GPL-2.0-or-later
URL:            https://github.com/dcantrell/pyparted/
Source0:        https://github.com/dcantrell/pyparted/archive/v%{version}.tar.gz#/%{srcname}-%{version}.tar.gz
# catch exception for unknown 'disk flag', kkaempf@suse.de
Patch0:         pyparted-3.10.patch
Patch1:         python-parted-parted-binary.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module wheel}
# tests requires
BuildRequires:  e2fsprogs
BuildRequires:  fdupes
BuildRequires:  parted
BuildRequires:  parted-devel
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
Requires:       parted
%python_subpackages

%description
Python module for the parted library.  It is used for manipulating
partition tables.

%prep
%autosetup -p1 -n %{srcname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pyunittest_arch -v

%files %{python_files}
%license LICENSE
%doc AUTHORS NEWS README.md TODO
%{python_sitearch}/_ped*.so
%{python_sitearch}/parted
%{python_sitearch}/%{srcname}-%{version}*-info

%changelog
