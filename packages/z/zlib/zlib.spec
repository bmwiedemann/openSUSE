#
# spec file for package zlib
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


Name:           zlib
Version:        1.2.11
Release:        0
Summary:        Library implementing the DEFLATE compression algorithm
License:        Zlib
URL:            http://www.zlib.net/
Source0:        http://zlib.net/zlib-%{version}.tar.gz
Source1:        http://zlib.net/zlib-%{version}.tar.gz.asc
Source2:        %{name}.keyring
Source4:        LICENSE
Source5:        baselibs.conf
Source6:        zlib-rpmlintrc
#PATCH-FIX-SUSE: fate#314093, sent upstream by IBM
Patch0:         zlib-1.2.11-optimized-s390.patch
#PATCH-FIX-SUSE: compiler check of varguments passed to gzprintf
Patch1:         zlib-format.patch
#PATCH-FIX-UPSTREAM do not store negative values in uInt
Patch2:         0001-Do-not-try-to-store-negative-values-in-unsigned-int.patch
#PATCH-FIX-UPSTREAM https://github.com/madler/zlib/pull/335
Patch3:         zlib-power8-fate325307.patch
#PATCH-FIX-UPSTREAM https://github.com/madler/zlib/pull/410
Patch4:         410.patch
#PATCH-FIX-SUSE do not check exact version match as the lib can be updated
#               we should simply rely on soname versioning to protect us
Patch5:         zlib-no-version-check.patch
Patch6:         bsc1174736-DFLTCC_LEVEL_MASK-set-to-0x1ff.patch
Patch7:         bsc1174551-fxi-imcomplete-raw-streams.patch
Patch8:         zlib-compression-switching.patch
#PATCH-FIX-SUSE: bsc#1176201, sent upstream by IBM
Patch9:         zlib-s390x-z15-fix-hw-compression.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig

%description
zlib is a general-purpose lossless data-compression library,
implementing an API for the DEFLATE algorithm, the latter of
which is being used by, for example, gzip and the ZIP archive
format.

%package -n libz1
Summary:        Library implementing the DEFLATE compression algorithm
Provides:       %{name} = %{version}-%{release}
Obsoletes:      %{name} < %{version}-%{release}

%description -n libz1
zlib is a general-purpose lossless data-compression library,
implementing an API for the DEFLATE algorithm, the latter of
which is being used by, for example, gzip and the ZIP archive
format.

%package devel
Summary:        Development files for zlib, a data compression library
Requires:       glibc-devel
Requires:       libz1 = %{version}

%description devel
zlib is a general-purpose lossless data-compression library,
implementing an API for the DEFLATE algorithm, the latter of
which is being used by, for example, gzip and the ZIP archive
format.

This subpackage holds the development headers for the library.

The zlib data format is itself portable across platforms. Unlike the
LZW compression method used in unix compress(1) and in the GIF image
format, the compression method currently used in zlib essentially
never expands the data. (LZW can double or triple the file size in
extreme cases.) zlib's memory footprint is also independent of the
input data and can be reduced, if necessary, at some cost in
compression.

%package devel-static
Summary:        Static library for zlib
Requires:       %{name}-devel = %{version}
Provides:       %{name}-devel:%{_libdir}/libz.a

%description devel-static
zlib is a general-purpose lossless data-compression library,
implementing an API for the DEFLATE algorithm, the latter of
which is being used by, for example, gzip and the ZIP archive
format.

This subpackage contains the static version of the library
used for development.

%package -n libminizip1
Summary:        Library for manipulation with .zip archives

%description -n libminizip1
Minizip is a library for manipulation with files from .zip archives.

%package -n minizip-devel
Summary:        Development files for the minizip library
Requires:       %{name}-devel = %{version}
Requires:       libminizip1 = %{version}
Requires:       pkgconfig

%description -n minizip-devel
This package contains the libraries and header files needed for
developing applications which use minizip.

%package testsuite
Summary:        Provide the test examples to reproduce test suite
Requires:       libz1 = %{version}

%description testsuite
To run the testsuite, execute %{_libexecdir}/%{name}/testsuite

It should exit 0

%prep
%setup -q
%patch0
%patch1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
cp %{SOURCE4} .

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
export LDFLAGS="-Wl,-z,relro,-z,now"
%ifarch s390x s390
  export CFLAGS="%{optflags} -DDFLTCC_LEVEL_MASK=0x7e"
%else
  export CFLAGS="%{optflags}"
%endif
# For sure not autotools build
CC="cc" ./configure \
    --shared \
    --prefix=%{_prefix} \
    --libdir=%{_libdir} \
%ifarch s390x s390
    --dfltcc \
%endif
    %{nil}

%if %{do_profiling}
  make %{?_smp_mflags} CFLAGS="%{optflags} %{cflags_profile_generate}"
  make check %{?_smp_mflags}
  make %{?_smp_mflags} clean
  make %{?_smp_mflags} CFLAGS="%{optflags} %{cflags_profile_feedback}"
%else
  make %{?_smp_mflags}
%endif

# And build minizip
cd contrib/minizip
autoreconf -fvi
%configure \
    --disable-static \
    --disable-silent-rules
make %{?_smp_mflags}

%check
make check %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_libdir}
%make_install
# manpage
install -m 644 zlib.3 %{buildroot}%{_mandir}/man3
install -m 644 zutil.h %{buildroot}%{_includedir}
# examples
mkdir -p %{buildroot}%{_docdir}/%{name}
cp -r examples/ %{buildroot}%{_docdir}/%{name}/

install -D examplesh %{buildroot}%{_libexecdir}/%{name}/testsuite

# Install minizip
cd contrib/minizip
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libz1 -p /sbin/ldconfig
%postun -n libz1 -p /sbin/ldconfig
%post -n libminizip1 -p /sbin/ldconfig
%postun -n libminizip1 -p /sbin/ldconfig

%files -n libz1
%license LICENSE
%{_libdir}/libz.so.1.2.*
%{_libdir}/libz.so.1

%files devel
%doc README ChangeLog
%dir %{_docdir}/%{name}/
%dir %{_docdir}/%{name}/examples
%{_docdir}/%{name}/examples/*
%{_mandir}/man3/zlib.3%{?ext_man}
%{_includedir}/zlib.h
%{_includedir}/zconf.h
%{_includedir}/zutil.h
%{_libdir}/libz.so
%{_libdir}/pkgconfig/zlib.pc

%files -n libminizip1
%doc contrib/minizip/MiniZip64_info.txt contrib/minizip/MiniZip64_Changes.txt
%{_libdir}/libminizip.so.*

%files -n minizip-devel
%dir %{_includedir}/minizip
%{_includedir}/minizip/*.h
%{_libdir}/libminizip.so
%{_libdir}/pkgconfig/minizip.pc

%files devel-static
%{_libdir}/libz.a

%files testsuite
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/testsuite

%changelog
