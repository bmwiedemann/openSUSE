#
# spec file for package libcue
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           libcue
%define lname	libcue2
Version:        2.2.1
Release:        0
Summary:        CUE sheet parsing library
License:        GPL-2.0-only
Group:          Development/Libraries/C and C++
URL:            https://github.com/lipnitsk/libcue

Source:         https://github.com/lipnitsk/libcue/archive/v%version.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  flex
BuildRequires:  pkg-config

%description
libcue parses so-called cue sheets from a char string or a FILE
pointer. This project is meant as a fork of (defunct) cuetools.

%package -n %lname
Summary:        CUE sheet parsing library
Group:          System/Libraries

%description -n %lname
libcue parses so-called cue sheets from a char string or a FILE
pointer.

%package devel
Summary:        Development files for libcue, a CUE sheet parsing library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
libcue parses so-called cue sheets from a char string or a FILE
pointer.

This package contains the development library symlink and header
files.

%prep
%autosetup -p1

%build
%cmake
make %{?_smp_mflags}

%install
%cmake_install
rm -f "%buildroot/%_libdir"/*.la

%check
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:%buildroot/%_libdir"
# %%ctest macro unknown to SLE11_SP4, do it explicitly
cd build
ctest --output-on-failure --force-new-ctest-process

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%_libdir/libcue.so.2*

%files devel
%_includedir/libcue.h
%_includedir/libcue*/
%_libdir/libcue.so
%_libdir/pkgconfig/*.pc

%changelog
