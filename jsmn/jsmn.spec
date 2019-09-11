#
# spec file for package jsmn
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           jsmn
Version:        20180125
Release:        0
Summary:        Minimalistic JSON parser library in C
License:        MIT
Group:          Development/Libraries/C and C++
Url:            http://zserge.com/jsmn.html
Source:         %{name}-%{version}.tar.xz
Source2:        CMakeLists.txt
BuildRequires:  cmake

%description
jsmn (pronounced like ‘jasmine’) is a minimalistic JSON parser in C with a
focus on simplicity and efficiency.

%package -n libjsmn0
Summary:        Minimalistic JSON parser library in C
Group:          System/Libraries

%description -n libjsmn0
jsmn (pronounced like ‘jasmine’) is a minimalistic JSON parser in C with a
focus on simplicity and efficiency.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       libjsmn0 = %{version}

%description devel
jsmn (pronounced like ‘jasmine’) is a minimalistic JSON parser in C with a
focus on simplicity and efficiency.

This package contains development files for %{name}.

%prep
%setup -q
cp %{SOURCE2} .
rm Makefile

%build
%cmake
make %{?_smp_mflags}

%install
%cmake_install

%post -n libjsmn0 -p /sbin/ldconfig
%postun -n libjsmn0 -p /sbin/ldconfig

%files -n libjsmn0
%doc LICENSE README.md
%{_libdir}/libjsmn.so.0
%{_libdir}/libjsmn.so.0.0.0

%files devel
%doc LICENSE README.md example/
%{_includedir}/jsmn.h
%{_libdir}/libjsmn.so

%changelog
