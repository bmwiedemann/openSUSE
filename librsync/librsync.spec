#
# spec file for package librsync
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define lname   librsync2
Name:           librsync
Version:        1.0.0
Release:        0
Summary:        A Library for Generating Network Deltas
License:        LGPL-2.1+
Group:          Development/Libraries/C and C++
Url:            http://librsync.sourceforge.net/
Source:         https://github.com/librsync/%{name}/archive/v%{version}.tar.gz
Patch0:         librsync-0.9.7-strictalias.diff
Patch1:         librsync-man-example.diff
Patch2:         librsync-0.9.7-getopt.patch
Patch3:         librsync-exports.patch
Patch4:         blake2-config.patch
BuildRequires:  libbz2-devel
BuildRequires:  libtool
BuildRequires:  popt-devel
BuildRequires:  zlib-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
librsync implements the "rsync" algorithm, which allows remote
differencing of binary files.  librsync computes a delta relative to a
file's checksum, so the two files need not both be present to generate
a delta.

%package -n %{lname}
Summary:        A Library for Generating Network Deltas
Group:          System/Libraries
# O/P added 2011-11-26
Obsoletes:      librsync < %{version}-%{release}
Provides:       librsync = %{version}-%{release}

%description -n %{lname}
librsync implements the "rsync" algorithm, which allows remote
differencing of binary files.  librsync computes a delta relative to a
file's checksum, so the two files need not both be present to generate
a delta.

%package devel
Summary:        Development files for librsync
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
librsync implements the "rsync" algorithm, which allows remote
differencing of binary files.  librsync computes a delta relative to a
file's checksum, so the two files need not both be present to generate
a delta.

%package -n rdiff
Summary:        Frontend to rsync's delta algorithm
Group:          Productivity/Archiving/Backup

%description -n rdiff
rdiff computes and applies signature-based file differences.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
autoreconf -fvi
%configure \
   --enable-shared \
   --disable-static \
   --with-pic
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
rm %{buildroot}%{_libdir}/*.la

%check
make %{?_smp_mflags} check

%post -n %{lname} -p /sbin/ldconfig

%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%defattr(-,root,root)
%{_libdir}/librsync.so.*
%doc AUTHORS COPYING NEWS README.md THANKS TODO.md

%files devel
%defattr(-,root,root)
%{_libdir}/librsync.so
%{_mandir}/man3/*
%{_includedir}/*.h

%files -n rdiff
%defattr(-,root,root)
%{_bindir}/rdiff
%{_mandir}/man1/*

%changelog
