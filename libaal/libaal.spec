#
# spec file for package libaal
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


Name:           libaal
Summary:        Application abstraction mechanism library used by reiser4progs
License:        GPL-2.0-only
Group:          System/Filesystems
Version:        1.0.7
Release:        0
URL:            https://sf.net/projects/reiser4/

Source:         https://downloads.sf.net/reiser4/libaal-%version.tar.gz
Patch1:         libaal-1.0.5-rpmoptflags.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

%description
libaal includes device abstraction, libc independence code, and more.

%package -n libaal-1_0-7
Summary:        Application abstraction mechanism library used by reiser4progs
License:        GPL-2.0-only
Group:          System/Libraries

%description -n libaal-1_0-7
libaal includes device abstraction, libc independence code, and more.

%package -n libaal-minimal0
Summary:        Application abstraction mechanism library used by reiser4progs
License:        GPL-2.0-only
Group:          System/Libraries

%description -n libaal-minimal0
libaal includes device abstraction, libc independence code, and more.

%package devel
Summary:        Header files for reiser4progs's application abstraction mechanism library
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
Requires:       libaal-1_0-7 = %version
Requires:       libaal-minimal0 = %version

%description devel
libaal includes device abstraction, libc independence code, and more.

%prep
%autosetup -p1

%build
autoreconf -fi
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la

%post   -n libaal-1_0-7 -p /sbin/ldconfig
%postun -n libaal-1_0-7 -p /sbin/ldconfig
%post   -n libaal-minimal0 -p /sbin/ldconfig
%postun -n libaal-minimal0 -p /sbin/ldconfig

%files -n libaal-1_0-7
%license COPYING
%_libdir/libaal-1.0.so.7*

%files -n libaal-minimal0
%_libdir/libaal-minimal.so.0*

%files devel
%doc BUGS ChangeLog README TODO
%_libdir/libaal*.so
%_includedir/aal
%_datadir/aclocal

%changelog
