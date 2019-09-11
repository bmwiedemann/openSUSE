#
# spec file for package reiser4progs
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


Name:           reiser4progs
Version:        1.2.1
Release:        0
%define lsuf	-1_2-1
Summary:        Utilities for Managing the Reiser4 File System
License:        GPL-2.0-only
Group:          System/Filesystems
URL:            https://sf.net/projects/reiser4/

Source:         https://downloads.sf.net/reiser4/%name-%version.tar.gz
Patch1:         no-static.diff
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
Reiser4 support library implementing the main filesystem logic for
the reiser4progs utilities.

%package -n libreiser4-minimal%lsuf
Summary:        Minimal version of the Reiser4 filesystem library
Group:          System/Libraries

%description -n libreiser4-minimal%lsuf
libreiser4-minimal is a variant of the Reiser4 filesystem library
that uses a reduced footprint and which has certain features disabled
(plugin check, FNV1 hash, Rupasov hash, TEA hash and DEG hash). The
maximum supported path length in -minimal is 256 instead of 1024.

%package -n librepair%lsuf
Summary:        Repair library for the Reiser4 filesystem
Group:          System/Libraries

%description -n librepair%lsuf
Reiser4 support library implementing filesystem repair logic.

%package devel
Summary:        Headers for the Reiser4 File System tool libraries
Group:          Development/Libraries/C and C++
Requires:       libreiser4%lsuf = %version
Requires:       libreiser4-minimal%lsuf = %version
Requires:       librepair%lsuf = %version

%description devel
A set of header C files and static libraries for the Reiser4 file
system tools.

%prep
%autosetup -p1

%build
#
# Disabling hashes only affects the minimal library. The options are
# a recommendation from reiser4progs's shipped .spec file.
#
autoreconf -fi
%configure --disable-static --enable-libminimal --disable-fnv1-hash \
	--disable-rupasov-hash --disable-tea-hash --disable-deg-hash
make %{?_smp_mflags}

%install
# parallel install cause missing file
%make_install -j1
rm -f "%buildroot/%_libdir"/*.la

%post   -n libreiser4%lsuf -p /sbin/ldconfig
%postun -n libreiser4%lsuf -p /sbin/ldconfig
%post   -n libreiser4-minimal%lsuf -p /sbin/ldconfig
%postun -n libreiser4-minimal%lsuf -p /sbin/ldconfig
%post   -n librepair%lsuf -p /sbin/ldconfig
%postun -n librepair%lsuf -p /sbin/ldconfig

%files
%doc BUGS ChangeLog NEWS README TODO
%license COPYING
%_mandir/man8/*
%_sbindir/*reiser4

%files -n libreiser4%lsuf
%_libdir/libreiser4-1.2.so.1*

%files -n libreiser4-minimal%lsuf
%_libdir/libreiser4-minimal-1.2.so.1*

%files -n librepair%lsuf
%_libdir/librepair-1.2.so.1*

%files devel
%_includedir/reiser4/
%_includedir/repair/
%_libdir/lib*.so
%_datadir/aclocal/

%changelog
