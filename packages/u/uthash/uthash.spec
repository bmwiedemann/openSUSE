#
# spec file for package uthash
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define sover 2
Name:           uthash
Version:        2.0.1
Release:        0
Summary:        Inline hash table for C structures
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Url:            https://github.com/troydhanson/uthash
Source:         https://github.com/troydhanson/uthash/archive/v%{version}/%{name}-%{version}.tar.gz
Patch1:         uthash-proceed_with_tests_without_prompt.patch
Patch2:         uthash-optflags.patch
Patch3:         libut-shared.patch
BuildRequires:  pkgconfig
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
uthash implements a hash table for C structures. It requires adding
a UT_hash_handle-typed member to your existing structure definition.

%package devel
Summary:        Development headers for uthash
Group:          Development/Libraries/C and C++
Requires:       libut%{sover} = %{version}
Obsoletes:      uthash <= 1.9.9

%description devel
This package provides development headers for uthash, a hash table
implementation for C structures.

%package -n libut2
Summary:        Inline hash table for C structures
Group:          System/Libraries

%description -n libut2
uthash implements a hash table for C structures. It requires adding
a UT_hash_handle-typed member to your existing structure definition.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
pushd libut
make DESTDIR=%{buildroot} LIBDIR=%{_libdir} OPTFLAGS="%{optflags}"
popd

%install
pushd libut
make install DESTDIR=%{buildroot} LIBDIR=%{_libdir} OPTFLAGS="%{optflags}"
popd
find %{buildroot} -type f -name "*.a" -delete -print

%check
pushd libut/tests
make OPTFLAGS="%{optflags}"
popd
pushd tests
OPTFLAGS="%{optflags}" \
./all_funcs
popd

%post -n libut%{sover} -p /sbin/ldconfig

%postun -n libut%{sover} -p /sbin/ldconfig

%files -n libut%{sover}
%defattr(-,root,root)
%doc LICENSE README.md
%{_libdir}/libut.so.%{version}
%{_libdir}/libut.so.%{sover}

%files devel
%defattr(-,root,root)
%{_includedir}/*.h
%{_libdir}/libut.so
%{_libdir}/pkgconfig/uthash.pc

%changelog
