#
# spec file for package uthash
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2012 Pascal Bleser <pascal.bleser@opensuse.org>
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


Name:           uthash
Version:        2.1.0
Release:        0
Summary:        Inline hash table for C structures
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://github.com/troydhanson/uthash
Source:         https://github.com/troydhanson/uthash/archive/v%{version}/%{name}-%{version}.tar.gz
Patch1:         uthash-proceed_with_tests_without_prompt.patch
Patch2:         uthash-optflags.patch
BuildRequires:  pkgconfig
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
uthash implements a hash table for C structures. It requires adding
a UT_hash_handle-typed member to your existing structure definition.

%package devel
Summary:        Development headers for uthash
Group:          Development/Libraries/C and C++
Obsoletes:      uthash <= 1.9.9

%description devel
This package provides development headers for uthash, a hash table
implementation for C structures.

%prep
%autosetup -p1

%build

%install
b="%buildroot"
mkdir -p "$b/%_includedir"
cp -a src/*.h "$b/%_includedir/"

%check
pushd tests
OPTFLAGS="%{optflags}" \
#./all_funcs
popd

%files devel
%defattr(-,root,root)
%{_includedir}/*.h
%doc LICENSE README.md

%changelog
