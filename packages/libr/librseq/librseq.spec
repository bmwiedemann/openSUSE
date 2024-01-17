#
# spec file for package librseq
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


Name:           librseq
%define lname   librseq0
Version:        0~git159.313af7c
Release:        0
Summary:        Library for Restartable Sequences
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/compudj/librseq

Source:         %name-%version.tar.xz
BuildRequires:  automake >= 1.10
BuildRequires:  c++_compiler
BuildRequires:  libtool >= 2.2
BuildRequires:  linux-glibc-devel >= 4.19
BuildRequires:  pkg-config

%description
RSEQ allows to determine when a thread is preempted while executing a
critical section, after which the thread can retry its operation.

%package -n %lname
Summary:        Library for Restartable Sequences
Group:          System/Libraries

%description -n %lname
RSEQ allows to determine when a thread is preempted while executing a
critical section, after which the thread can retry its operation.

%package devel
Summary:        Development for librseq, a library for restartable sequences
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
RSEQ allows to determine when a thread is preempted while executing a
critical section, after which the thread can retry its operation.

This package contains headers for the library.

%prep
%autosetup -p1

%build
autoreconf -fi
mkdir obj
pushd obj/
%define _configure ../configure
%configure --includedir="%_includedir/%name" --disable-static
%make_build
popd

%install
b="%buildroot"
%make_install -C obj
rm -Rf "%buildroot/%_libdir"/*.la "%buildroot/%_datadir/doc/%name"

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%_libdir/librseq.so.0*

%files devel
%_includedir/%name/
%_libdir/*.so
%_libdir/pkgconfig/*.pc
%_mandir/man?/*.2*
%license LICENSE

%changelog
