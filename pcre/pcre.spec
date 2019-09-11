#
# spec file for package pcre
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


Name:           pcre
Version:        8.42
Release:        0
Summary:        A library for Perl-compatible regular expressions
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Url:            http://www.pcre.org/
#SVN-Clone:	svn://vcs.exim.org/pcre/code/trunk
Source:         ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/%{name}-%{version}.tar.bz2
Source2:        ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/%{name}-%{version}.tar.bz2.sig
Source3:        %{name}.keyring
Source4:        baselibs.conf
#PATCH-FIX-UPSTREAM crrodriguez@opensuse.org http://bugs.exim.org/show_bug.cgi?id=1173
Patch0:         pcre-8.32-visibility.patch
#PATCH-FIX-OPENSUSE tchvatal@suse.cz upstream thinks it is good idea to use rpath, taken from RH
Patch1:         pcre-8.21-multilib.patch
#PATCH-FIX-OPENSUSE kstreitova@suse.com fix pcre stack frame size detection https://bugs.exim.org/show_bug.cgi?id=2173
Patch2:         pcre-8.41-stack_frame_size_detection.patch
#Patch 3: see: https://sources.debian.net/patches/pcre3/2:8.39-2/pcreposix.patch/ and cyrus imapd issue  #1731
Patch3:         pcre-8.42-pcreposix.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig

%description
The PCRE library is a set of functions that implement regular
expression pattern matching using the same syntax and semantics
as Perl 5.

%package        devel
Summary:        A library for Perl-compatible regular expressions
Group:          Development/Libraries/C and C++
Requires:       libpcre1 = %{version}
Requires:       libpcre16-0 = %{version}
Requires:       libpcrecpp0 = %{version}
Requires:       libpcreposix0 = %{version}
Requires:       libstdc++-devel

%description devel
The PCRE library is a set of functions that implement regular
expression pattern matching using the same syntax and semantics
as Perl 5.

%package        devel-static
Summary:        A library for Perl-compatible regular expressions
Group:          Development/Libraries/C and C++
Requires:       pcre-devel = %{version}

%description devel-static
The PCRE library is a set of functions that implement regular
expression pattern matching using the same syntax and semantics
as Perl 5.
This package contains static versions of the PCRE libraries.

%package -n libpcre1
Summary:        A library for Perl-compatible regular expressions
Group:          System/Libraries
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}

%description -n libpcre1
The PCRE library is a set of functions that implement regular
expression pattern matching using the same syntax and semantics
as Perl 5.

This PCRE library variant supports 8-bit and UTF-8 strings.
(See also libpcre16.)

%package -n libpcre16-0
Summary:        A library for Perl-compatible regular expressions
Group:          System/Libraries

%description -n libpcre16-0
The PCRE library is a set of functions that implement regular
expression pattern matching using the same syntax and semantics
as Perl 5.

libpcre16 supports 16-bit and UTF-16 strings.

%package -n libpcreposix0
Summary:        A library for Perl-compatible regular expressions
Group:          System/Libraries

%description -n libpcreposix0
The PCRE library is a set of functions that implement regular
expression pattern matching using the same syntax and semantics
as Perl 5.

pcreposix provides a POSIX-compatible API to the PCRE engine.

%package -n libpcrecpp0
Summary:        A library for Perl-compatible regular expressions
Group:          System/Libraries

%description -n libpcrecpp0
The PCRE library is a set of functions that implement regular
expression pattern matching using the same syntax and semantics
as Perl 5.

pcrecpp provides a C++ API to the PCRE engine.

%package doc
Summary:        A library for Perl-compatible regular expressions
Group:          Documentation/HTML
%if 0%{?suse_version} >= 1120
BuildArch:      noarch
%endif

%description doc
The PCRE library is a set of functions that implement regular
expression pattern matching using the same syntax and semantics
as Perl 5.

%package tools
Summary:        A library for Perl-compatible regular expressions
Group:          Productivity/Text/Utilities
Recommends:     %{name}-doc

%description tools
The PCRE library is a set of functions that implement regular
expression pattern matching using the same syntax and semantics
as Perl 5.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
# Available JIT archs see sljit/sljitConfig.h
autoreconf -fiv
%configure \
%ifarch %{ix86} x86_64 %{arm} aarch64 ppc ppc64 ppc64le mips sparc
  --enable-jit \
%endif
  --enable-static \
  --with-link-size=2 \
  --with-match-limit=10000000 \
  --enable-newline-is-lf \
  --enable-pcre16 \
  --enable-utf8 \
  --enable-unicode-properties
%if 0%{?do_profiling}
  # RunTest test 2 needs lots of stack, if it ever segfaults
  # try increasing this
  ulimit -s $((16*1024))
  make %{?_smp_mflags} CFLAGS="%{optflags} %{cflags_profile_generate}" V=1
  make CFLAGS="%{optflags} %{cflags_profile_generate}" check
  make %{?_smp_mflags} clean
  make %{?_smp_mflags} CFLAGS="%{optflags} %{cflags_profile_feedback}" V=1
%else
  make %{?_smp_mflags} CFLAGS="%{optflags}"
%endif

%install
%make_install
mkdir -p %{buildroot}/%{_defaultdocdir}
mv %{buildroot}%{_datadir}/doc/pcre %{buildroot}/%{_defaultdocdir}/pcre-doc
#empty dependecy_libs
find %{buildroot} -type f -name "*.la" -delete -print

%check
# RunTest test 2 needs lots of stack, if it ever segfaults
# try increasing this
ulimit -s $((16*1024))
make %{?_smp_mflags} check

%post -n libpcre1 -p /sbin/ldconfig
%postun -n libpcre1 -p /sbin/ldconfig
%post -n libpcre16-0 -p /sbin/ldconfig
%postun -n libpcre16-0 -p /sbin/ldconfig
%post -n libpcrecpp0 -p /sbin/ldconfig
%postun -n libpcrecpp0 -p /sbin/ldconfig
%post -n libpcreposix0 -p /sbin/ldconfig
%postun -n libpcreposix0 -p /sbin/ldconfig

%files -n libpcre1
%license COPYING LICENCE
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/libpcre.so.*

%files -n libpcre16-0
%{_libdir}/libpcre16.so.*

%files -n libpcrecpp0
%{_libdir}/libpcrecpp.so.*

%files -n libpcreposix0
%{_libdir}/libpcreposix.so.*

%files tools
%{_bindir}/pcregrep
%{_bindir}/pcretest
%{_mandir}/man1/pcregrep.1%{ext_man}
%{_mandir}/man1/pcretest.1%{ext_man}

%files doc
%license COPYING LICENCE
%doc AUTHORS ChangeLog NEWS README
%doc doc/html doc/*.txt
%doc %{_defaultdocdir}/pcre-doc

%files devel
%{_bindir}/pcre-config
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libpcre.pc
%{_libdir}/pkgconfig/libpcre16.pc
%{_libdir}/pkgconfig/libpcrecpp.pc
%{_libdir}/pkgconfig/libpcreposix.pc
%{_mandir}/man1/pcre-config.1%{ext_man}
%{_mandir}/man3/pcre*.3*%{ext_man}

%files devel-static
%{_libdir}/*.a

%changelog
