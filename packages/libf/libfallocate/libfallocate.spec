#
# spec file for package libfallocate
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


%define         somajor 0
Name:           libfallocate
Version:        0.1.1
Release:        0
Summary:        Filesystem preallocation interface library
License:        LGPL-2.1-or-later
Group:          System/Filesystems
Url:            http://libfallocate.sf.net/
Source:         libfallocate-%{version}.tar.bz2
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
libfallocate provides an interface for applications to tell filesystems
about the size of to-be-written files, so the filesystem can do a better
job in taking allocation decisions to avoid fragmentation.

libfallocate provides a wrapper for the fallocate() syscall in case your
glibc (<2.10) does not have it yet. It also provides linux_fallocate()
which will attempt the space reservation ioctl that xfs and ocfs2
provide in case fallocate() did not succeed.

It has an additional richer interface fallocate_with_fallback() that
allows you to instruct it to fallback to do preallocation by zeroing
things out (like posix_fallocate()) or to extend the file size by a sparse
write (like a successful fallocate() with mode==0 would have done).

%package -n libfallocate%{somajor}
Summary:        Filesystem preallocation interface library
Group:          System/Filesystems

%description -n libfallocate%{somajor}
libfallocate provides an interface for applications to tell filesystems
about the size of to-be-written files, so the filesystem can do a better
job in taking allocation decisions to avoid fragmentation.

libfallocate provides a wrapper for the fallocate() syscall in case your
glibc (<2.10) does not have it yet. It also provides linux_fallocate()
which will attempt the space reservation ioctl that xfs and ocfs2
provide in case fallocate() did not succeed.

It has an additional richer interface fallocate_with_fallback() that
allows you to instruct it to fallback to do preallocation by zeroing
things out (like posix_fallocate()) or to extend the file size by a sparse
write (like a successful fallocate() with mode==0 would have done).

%package devel
Summary:        Header and devel files for libfallocate
Group:          Development/Libraries/C and C++
Requires:       libfallocate%{somajor} = %{version}-%{release}

%description devel
This package contains the header file and the .so library to link
against for apps that want to use libfallocate.

%package devel-static
Summary:        Static library for libfallocate
Group:          Development/Libraries/C and C++
Requires:       libfallocate-devel = %{version}-%{release}

%description devel-static
This package contains the static library for apps
apps that want to use libfallocate statically.

%prep
%setup -q

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
autoreconf -fiv
%configure
make %{?_smp_mflags} RPM_OPT_FLAGS="%{optflags}"
make %{?_smp_mflags} RPM_OPT_FLAGS="%{optflags}" static

%check
make %{?_smp_mflags} check

%install
make install-lib install-static install-header DESTDIR=%{buildroot} PREFIX=%{_prefix} LIBDIR=%{_libdir} DOCDIR=%{_docdir}/libfallocate0

%post -n libfallocate%{somajor} -p /sbin/ldconfig

%postun -n libfallocate%{somajor} -p /sbin/ldconfig

%files -n libfallocate%{somajor}
%defattr(-,root,root)
%doc README TODO COPYING AUTHORS
%defattr(0755,root,root)
%{_libdir}/libfallocate.so.*

%files devel
%defattr(0755,root,root)
%{_libdir}/libfallocate.so
%defattr(0644,root,root)
%{_includedir}/fallocate.h

%files devel-static
%defattr(0644,root,root)
%{_libdir}/libfallocate.a

%changelog
