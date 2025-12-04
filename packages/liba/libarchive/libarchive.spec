#
# spec file for package libarchive
#
# Copyright (c) 2025 SUSE LLC and contributors
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define somajor 13
%define libname libarchive%{somajor}
Name:           libarchive
Version:        3.8.3
Release:        0
Summary:        Utility and C library to create and read several streaming archive formats
License:        BSD-2-Clause
Group:          Productivity/Archiving/Compression
URL:            https://www.libarchive.org/
Source0:        https://github.com/libarchive/libarchive/releases/download/v%{version}/libarchive-%{version}.tar.xz
Source1:        https://github.com/libarchive/libarchive/releases/download/v%{version}/libarchive-%{version}.tar.xz.asc
Source2:        libarchive.keyring
Source1000:     baselibs.conf
BuildRequires:  cmake
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(ext2fs)
BuildRequires:  pkgconfig(libacl)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(zlib) >= 1.2.1

%description
Libarchive is a programming library that can create and read several
different streaming archive formats, including most popular tar
variants and several cpio formats. It can also write shar archives and
read ISO-9660 CDROM images. The bsdtar program is an implementation of
tar(1) that is built on top of libarchive. It started as a test
harness, but has grown and is now the standard system tar for FreeBSD 5
and 6.

This package contains the bsdtar cmdline utility.

%package -n bsdtar
Summary:        Utility to read several different streaming archive formats
Group:          Productivity/Archiving/Compression
Requires:       %{libname} >= %{version}

%description -n bsdtar
This package contains the bsdtar cmdline utility.

%package -n %{libname}
Summary:        Library to work with several different streaming archive formats
Group:          System/Libraries

%description -n %{libname}
Libarchive is a programming library that can create and read several
different streaming archive formats, including most popular tar
variants and several cpio formats. It can also write shar archives and
read ISO-9660 CDROM images. The bsdtar program is an implementation of
tar(1) that is built on top of libarchive. It started as a test
harness, but has grown and is now the standard system tar for FreeBSD 5
and 6.

The libarchive library offers a number of features that make it both
very flexible and very powerful.

- Automatic format detection: libarchive can automatically determine
   both the compression and the archive format, regardless of the
   data source. Most tar implementations do not automatically detect
   the compression format, few implementation that can correctly do
   this when reading from stdin or a socket. (The tar program
   included with Gunnar Ritter's heirloom collection also does full
   automatic format detection.)

- Writes POSIX formats: libarchive writes POSIX-standard formats,
   including "ustar," "pax interchange format," and the POSIX "cpio"
   format.

- Supports pax interchange format: Pax interchange format (which,
   despite the name, is really an extended tar format) eliminates
   almost all limitations of historic tar formats and provides a
   standard method for incorporating vendor-specific extensions.
   libarchive exploits this extension mechanism to support ACLs and
   file flags, for example. (Joerg Schilling's star archiver is
   another open-source tar program that supports pax interchange
   format.)

- Reads popular formats: libarchive can read GNU tar, ustar, pax
   interchange format, cpio, and older tar variants. The internal
   architecture is easily extensible. The only requirement for
   support is that it be possible to read the format without seeking
   in the file. (For example, a format that includes a compressed
   size field before the data cannot be correctly written without
   seeking.)

- High-Level API: the libarchive API makes it fairly simple to build
   an archive from a list of filenames or to extract the entries
   from an archive. However, the API also provides extreme
   flexibility with regards to data sources. For example, there are
   generic hooks that allow you to write an archive to a socket or
   read data from an archive entry into a memory buffer.

- Extensible. The internal design uses generic interfaces for
compression, archive format detection and decoding, and archive data
I/O. It should be very easy to add new formats, new compression
methods, or new ways of reading/writing archives.

%package devel
Summary:        Development files for libarchive
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
Libarchive is a programming library that can create and read several
different streaming archive formats, including most popular tar
variants and several cpio formats. It can also write shar archives and
read ISO-9660 CDROM images. The bsdtar program is an implementation of
tar(1) that is built on top of libarchive. It started as a test
harness, but has grown and is now the standard system tar for FreeBSD 5
and 6.

This package contains the development files.

%prep
%autosetup -p1

%build
%define __builder ninja
%cmake
%cmake_build

%install
%cmake_install
rm "%{buildroot}%{_mandir}/man5/"{tar,cpio,mtree}.5*
rm "%{buildroot}%{_libdir}/libarchive.a"

%check
exclude=""
%ifarch %{arm} %{ix86} ppc s390
exclude="-E test_write_filter"
%endif
%ctest $exclude

%ldconfig_scriptlets -n %{libname}

%files -n bsdtar
%license COPYING
%{_bindir}/bsdcat
%{_bindir}/bsdcpio
%{_bindir}/bsdtar
%{_bindir}/bsdunzip
%{_mandir}/man1/*.1%{?ext_man}
%{_mandir}/man5/*.5%{?ext_man}

%files -n %{libname}
%license COPYING
%doc NEWS
%{_libdir}/libarchive.so.%{somajor}{,.*}

%files devel
%license COPYING
%doc examples/
%{_mandir}/man3/*.3%{?ext_man}
%{_libdir}/libarchive.so
%{_includedir}/archive*
%{_libdir}/pkgconfig/libarchive.pc

%changelog
