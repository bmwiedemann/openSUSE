#
# spec file for package reiserfs
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


Name:           reiserfs
BuildRequires:  acl-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libcom_err-devel
BuildRequires:  libtool
BuildRequires:  libuuid-devel
BuildRequires:  linux-kernel-headers
BuildRequires:  pkg-config
BuildRequires:  xz
# Git-url:	git://git.kernel.org/pub/scm/linux/kernel/git/jeffm/reiserfsprogs.git
Url:            https://www.kernel.org/pub/linux/kernel/people/jeffm/reiserfsprogs
Conflicts:      libreiserfs-progs
Supplements:    filesystem(reiserfs)
Version:        3.6.27
Release:        0
Summary:        Reiser File System utilities
License:        GPL-2.0-or-later
Group:          System/Filesystems
Source:         reiserfsprogs-%{version}.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Patch1:         silent-rules.patch
Requires:       libreiserfscore0 = %{version}

%description
This package includes utilities for making the file system
(mkreiserfs), checking for consistency (reiserfsck), and resizing
(resize_reiserfs).

%package -n libreiserfscore-devel
Summary:        Reiser File System Core Library Development Files
Group:          Development/Libraries/C and C++
Requires:       libcom_err-devel
Requires:       libreiserfscore0 = %{version}
Requires:       libuuid-devel

%description -n libreiserfscore-devel
This package contains the headers and linkable libraries for
libreiserfscore, which is used to provide reiserfs services for external
programs.

%package -n libreiserfscore0
Summary:        Reiser File System Core Library
Group:          System/Filesystems
Conflicts:      reiserfs < %{version}

%description -n libreiserfscore0
This package contains the library that provides core functionality
for the reiserfs file system.

%prep
%setup -q -n reiserfsprogs-%{version}
%patch1 -p1

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
autoreconf -fiv
export CFLAGS="%optflags -D_GNU_SOURCE"
%configure --exec-prefix=/ --bindir=/bin --sbindir=/sbin
%make_build

%install
install	-d	${RPM_BUILD_ROOT}/sbin
make DESTDIR=${RPM_BUILD_ROOT} install
cd ${RPM_BUILD_ROOT}/sbin

%files
%defattr(-, root, root)
/sbin/*
%doc %{_mandir}/man8/*
%if 0%{?suse_version} < 1210
%doc COPYING
%else
%license COPYING
%endif

%files -n libreiserfscore-devel
%defattr(-, root, root)
%dir %{_includedir}/reiserfs
%{_includedir}/reiserfs/*.h
%{_libdir}/pkgconfig/reiserfscore.pc
%{_libdir}/libreiserfscore.a
%{_libdir}/libreiserfscore.la
%{_libdir}/libreiserfscore.so
%{_libdir}/libreiserfscore.so.0

%files -n libreiserfscore0
%defattr(-, root, root)
%{_libdir}/libreiserfscore.so.0.0.0

%post -n libreiserfscore0 -p /sbin/ldconfig
%postun -n libreiserfscore0 -p /sbin/ldconfig

%changelog
