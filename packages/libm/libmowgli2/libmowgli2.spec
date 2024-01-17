#
# spec file for package libmowgli2
#
# Copyright (c) 2020 SUSE LLC
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


Name:           libmowgli2
%define lname	libmowgli-2-0
Version:        2.1.3
Release:        0
Summary:        A development framework for C (like GLib)
License:        ISC
Group:          Development/Libraries/C and C++
URL:            https://github.com/atheme/libmowgli-2

Source:         https://github.com/atheme/libmowgli-2/archive/v%version.tar.gz
BuildRequires:  pkgconfig(libssl)

%description
mowgli is a development framework for C (like GLib) which provides
flexible algorithms. It can be used as a suppliment to GLib to add
additional functions (dictionaries, hashes), or replace some of the
slow GLib list manipulation functions, or stand alone. It also
provides a hook system and convenient logging for code, as well as a
block allocator.

%package -n %lname
Summary:        The mowgli Gen2 development framework for C
Group:          System/Libraries

%description -n %lname
mowgli is a development framework for C (like GLib) which provides
flexible algorithms. It can be used as a suppliment to GLib to add
additional functions (dictionaries, hashes), or replace some of the
slow GLib list manipulation functions, or stand alone. It also
provides a hook system and convenient logging for code, as well as a
block allocator.

This package holds the shared library from libmowgli v2.

%package devel
Summary:        The development files for libmowgli v2
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
Requires:       glibc-devel

%description devel
mowgli is a development framework for C (like GLib) which provides
flexible algorithms. It can be used as a suppliment to GLib to add
additional functions (dictionaries, hashes), or replace some of the
slow GLib list manipulation functions, or stand alone. It also
provides a hook system and convenient logging for code, as well as a
block allocator.

This package holds the development files for libmowgli v2.

%prep
%autosetup -n libmowgli-2-%version -p1

%build
if [ ! -e configure ]; then
	./autogen.sh
fi
%configure
# They are still on so.0, but functions were added
echo 'V_%version { global: *; };' >mowgli2.sym
%make_build LDFLAGS="-Wl,--version-script=$PWD/mowgli2.sym"

%install
%make_install

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%_libdir/libmowgli-2.so.0*

%files devel
%doc doc/BOOST README
%license COPYING
%_includedir/libmowgli-2
%_libdir/libmowgli-2.so
%_libdir/pkgconfig/libmowgli-2.pc

%changelog
