#
# spec file for package gc
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


Name:           gc
Version:        8.0.4
Release:        0
Summary:        A garbage collector for C and C++
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            http://www.hboehm.info/gc/

#Git-Clone:	git://github.com/ivmai/bdwgc
Source:         https://github.com/ivmai/bdwgc/releases/download/v%version/%name-%version.tar.gz
BuildRequires:  autoconf >= 2.64
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(atomic_ops)

%description
The Boehm-Demers-Weiser conservative garbage collector can be used as a
garbage collecting replacement for C malloc or C++ new. It allows you
to allocate memory basically as you normally would, without explicitly
deallocating memory that is no longer useful. The collector
automatically recycles memory when it determines that it can no longer
be otherwise accessed.

%package -n libgc1
Summary:        A garbage collector for C and C++
Group:          System/Libraries
%ifarch ppc64
# bug437293
Obsoletes:      boehm-gc-64bit
%endif

%description -n libgc1
The Boehm-Demers-Weiser conservative garbage collector can be used as a
garbage collecting replacement for C malloc or C++ new. It allows you
to allocate memory basically as you normally would, without explicitly
deallocating memory that is no longer useful. The collector
automatically recycles memory when it determines that it can no longer
be otherwise accessed.

%package devel
Summary:        A garbage collector for C and C++
Group:          Development/Libraries/C and C++
Provides:       gc:/usr/include/gc/gc.h
Requires:       glibc-devel
Requires:       libatomic_ops-devel
Requires:       libgc1 = %version

%description devel
The Boehm-Demers-Weiser conservative garbage collector can be used as a
garbage collecting replacement for C malloc or C++ new. It allows you
to allocate memory basically as you normally would, without explicitly
deallocating memory that is no longer useful. The collector
automatically recycles memory when it determines that it can no longer
be otherwise accessed.

%prep
%setup -q

%build
autoreconf -fi

# see bugzilla.redhat.com/689877
export CPPFLAGS="-DUSE_GET_STACKBASE_FOR_MAIN"
export CXXFLAGS="%optflags -std=gnu++98"
%configure --disable-static --docdir="%_docdir/%name" \
    --with-gnu-ld	    \
    --enable-cplusplus	    \
    --enable-large-config   \
    --enable-threads=posix  \
    --enable-parallel-mark \
    --with-libatomic-ops=yes
# --with-libatomic-ops=yes means to use the system library

make %{?_smp_mflags}

%install
%make_install
rm -Rf "%buildroot/%_datadir/gc" "%buildroot/%_libdir"/*.la
rm -f "%buildroot/%_docdir/%name"/README.{Mac,OS2,win32}

%check
%if !0%{?qemu_user_space_build}
make check
%endif

%post -n libgc1 -p /sbin/ldconfig
%postun -n libgc1 -p /sbin/ldconfig

%files -n libgc1
%defattr(-, root, root)
%_libdir/libcord.so.1*
%_libdir/libgc*.so.1*

%files devel
%defattr(-, root, root)
%_docdir/%name/
%_libdir/libcord.so
%_libdir/libgc*.so
%_libdir/pkgconfig/bdw-gc.pc
%_mandir/man3/gc.3*
%_includedir/gc.h
%_includedir/gc_cpp.h
%_includedir/gc/

%changelog
