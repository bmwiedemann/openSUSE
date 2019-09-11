#
# spec file for package reiser4progs
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           reiser4progs
Version:        1.2.1
Release:        0
%define lsuf	-1_2-1
Summary:        Utilities for Managing the Reiser4 File System
License:        GPL-2.0
Group:          System/Filesystems
Url:            http://sf.net/projects/reiser4/

Source:         http://downloads.sf.net/reiser4/%name-%version.tar.gz
Patch1:         no-static.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  automake
BuildRequires:  libaal-devel >= 1.0.7
BuildRequires:  libtool
BuildRequires:  libuuid-devel
BuildRequires:  readline-devel
BuildRequires:  xz

%description
A set of commands for using the Reiser4 file system, including
mkfs.reiser4.

%package -n libreiser4%lsuf
Summary:        Reiser4 filesystem library
Group:          System/Libraries

%description -n libreiser4%lsuf

%package -n libreiser4-minimal%lsuf
Summary:        Minimal version of the Reiser4 filesystem library
Group:          System/Libraries

%description -n libreiser4-minimal%lsuf
libreiser4-minimal is a variant of the Reiser4 filesystem library
that uses a reduced footprint and which has certain features disabled
(plugin check, FNV1 hash, Rupasov hash, TEA hash and DEG hash). The
maximum supported path length in -minimal is 256 instead of 1024.

In openSUSE, all tunable features remain of libreiser4-minimal enabled.

%package -n librepair%lsuf
Summary:        Repair library for the Reiser4 filesystem
Group:          System/Libraries

%description -n librepair%lsuf

%package devel
Summary:        Header C files and static libs for the Reiser4 File System tools
Group:          Development/Libraries/C and C++
Requires:       libreiser4%lsuf = %version
Requires:       libreiser4-minimal%lsuf = %version
Requires:       librepair%lsuf = %version

%description devel
A set of header C files and static libraries for the Reiser4 file
system tools.

%prep
%setup -q
%patch -P 1 -p1

%build
#
# Disabling hashes only affects minimal library. The options are
# a recommendation from reiser4progs's shipped .spec file.
#
autoreconf -fi
%configure --disable-static --enable-libminimal --disable-fnv1-hash \
	--disable-rupasov-hash --disable-tea-hash --disable-deg-hash
make %{?_smp_mflags}

%install
# paralel install cause missing file
make install DESTDIR="%buildroot"
rm -f "%buildroot/%_libdir"/*.la

%post   -n libreiser4%lsuf -p /sbin/ldconfig
%postun -n libreiser4%lsuf -p /sbin/ldconfig
%post   -n libreiser4-minimal%lsuf -p /sbin/ldconfig
%postun -n libreiser4-minimal%lsuf -p /sbin/ldconfig
%post   -n librepair%lsuf -p /sbin/ldconfig
%postun -n librepair%lsuf -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc BUGS COPYING ChangeLog NEWS README TODO
%_mandir/man8/*
%_sbindir/*reiser4

%files -n libreiser4%lsuf
%defattr(-,root,root)
%_libdir/libreiser4-1.2.so.1*

%files -n libreiser4-minimal%lsuf
%defattr(-,root,root)
%_libdir/libreiser4-minimal-1.2.so.1*

%files -n librepair%lsuf
%defattr(-,root,root)
%_libdir/librepair-1.2.so.1*

%files devel
%defattr(-,root,root)
%_includedir/reiser4/
%_includedir/repair/
%_libdir/lib*.so
%_datadir/aclocal/

%changelog
