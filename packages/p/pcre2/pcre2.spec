#
# spec file for package pcre2
#
# Copyright (c) 2022 SUSE LLC
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


%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
Name:           pcre2
Version:        10.42
Release:        0
Summary:        A library for Perl-compatible regular expressions
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://www.pcre.org
Source0:        https://github.com/PhilipHazel/pcre2/releases/download/%{name}-%{version}/%{name}-%{version}.tar.bz2
Source2:        https://github.com/PhilipHazel/pcre2/releases/download/%{name}-%{version}/%{name}-%{version}.tar.bz2.sig
Source3:        %{name}.keyring
Source4:        baselibs.conf
#PATCH-FIX-OPENSUSE tchvatal@suse.cz upstream thinks it is good idea to use rpath, taken from RH
Patch1:         pcre2-10.10-multilib.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libbz2-devel
BuildRequires:  libedit-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(zlib)

%description
The PCRE2 library is a set of functions that implement regular
expression pattern matching using the same syntax and semantics
as Perl 5.

PCRE2 is a re-working of the original PCRE library to provide an entirely new
API.

%package        devel
Summary:        A library for Perl-compatible regular expressions
Group:          Development/Libraries/C and C++
Requires:       libpcre2-16-0 = %{version}
Requires:       libpcre2-32-0 = %{version}
Requires:       libpcre2-8-0 = %{version}
Requires:       libpcre2-posix3 = %{version}
Requires:       libstdc++-devel

%description devel
The PCRE2 library is a set of functions that implement regular
expression pattern matching using the same syntax and semantics
as Perl 5.

PCRE2 is a re-working of the original PCRE library to provide an entirely new
API.

%package        devel-static
Summary:        A library for Perl-compatible regular expressions
Group:          Development/Libraries/C and C++
Requires:       pcre2-devel = %{version}

%description devel-static
The PCRE2 library is a set of functions that implement regular
expression pattern matching using the same syntax and semantics
as Perl 5.

PCRE2 is a re-working of the original PCRE library to provide an entirely new
API.

This package contains static versions of the PCRE2 libraries.

%package -n libpcre2-8-0
Summary:        A library for Perl-compatible regular expressions
Group:          System/Libraries

%description -n libpcre2-8-0
The PCRE2 library is a set of functions that implement regular
expression pattern matching using the same syntax and semantics
as Perl 5.

PCRE2 is a re-working of the original PCRE library to provide an entirely new
API.

This PCRE2 library variant supports 8-bit and UTF-8 strings.
(See also libpcre2-16 and libpcre2-32)

%package -n libpcre2-16-0
Summary:        A library for Perl-compatible regular expressions
Group:          System/Libraries

%description -n libpcre2-16-0
The PCRE2 library is a set of functions that implement regular
expression pattern matching using the same syntax and semantics
as Perl 5.

PCRE2 is a re-working of the original PCRE library to provide an entirely new
API.

libpcre2-16 supports 16-bit and UTF-16 strings.

%package -n libpcre2-32-0
Summary:        A library for Perl-compatible regular expressions
Group:          System/Libraries

%description -n libpcre2-32-0
The PCRE2 library is a set of functions that implement regular
expression pattern matching using the same syntax and semantics
as Perl 5.

PCRE2 is a re-working of the original PCRE library to provide an entirely new
API.

libpcre2-32 supports 32-bit and UTF-32 strings.

%package -n libpcre2-posix3
Summary:        A library for Perl-compatible regular expressions
Group:          System/Libraries

%description -n libpcre2-posix3
The PCRE2 library is a set of functions that implement regular
expression pattern matching using the same syntax and semantics
as Perl 5.

PCRE2 is a re-working of the original PCRE library to provide an entirely new
API.

pcre2-posix provides a POSIX-compatible API to the PCRE2 engine.

%package doc
Summary:        A library for Perl-compatible regular expressions
Group:          Documentation/HTML
BuildArch:      noarch

%description doc
The PCRE2 library is a set of functions that implement regular
expression pattern matching using the same syntax and semantics
as Perl 5.

PCRE2 is a re-working of the original PCRE library to provide an entirely new
API.

%package tools
Summary:        A library for Perl-compatible regular expressions
Group:          Productivity/Text/Utilities
Recommends:     %{name}-doc

%description tools
The PCRE2 library is a set of functions that implement regular
expression pattern matching using the same syntax and semantics
as Perl 5.

PCRE2 is a re-working of the original PCRE library to provide an entirely new
API.

%prep
%autosetup -p1

%build
%define _lto_cflags %{nil}
# Available JIT archs see sljit/sljitConfig.h
autoreconf -fiv
export LDFLAGS="-Wl,-z,relro,-z,now"
%configure \
%ifarch %{ix86} x86_64 aarch64 %{arm} ppc ppc64 ppc64le mips sparc s390x
	    --enable-jit \
%endif
	    --enable-static \
	    --with-link-size=2 \
	    --with-match-limit=10000000 \
	    --enable-newline-is-lf \
	    --enable-pcre2-16 \
	    --enable-pcre2-32 \
	    --enable-pcre2grep-libz \
	    --enable-pcre2grep-libbz2 \
	    --enable-pcre2test-libedit \
	    --enable-unicode

%if 0%{?do_profiling}
  %make_build CFLAGS="%{optflags} %{cflags_profile_generate}"
  export LANG=POSIX
  # do not run profiling in parallel for reproducible builds (boo#1040589 boo#1102408)
  %make_build -j1 CFLAGS="%{optflags} %{cflags_profile_generate}" check
  %make_build clean
  %make_build CFLAGS="%{optflags} %{cflags_profile_feedback}"
%else
  %make_build CFLAGS="%{optflags}"
%endif

%install
%make_install
mkdir -p %{buildroot}/%{_defaultdocdir}
mv %{buildroot}%{_datadir}/doc/pcre2 %{buildroot}/%{_defaultdocdir}/pcre2-doc
#empty dependecy_libs
find %{buildroot} -type f -name "*.la" -delete -print

%check
export LANG=POSIX
%make_build check -j1

%post -n libpcre2-8-0 -p /sbin/ldconfig
%postun -n libpcre2-8-0 -p /sbin/ldconfig
%post -n libpcre2-16-0 -p /sbin/ldconfig
%postun -n libpcre2-16-0 -p /sbin/ldconfig
%post -n libpcre2-32-0 -p /sbin/ldconfig
%postun -n libpcre2-32-0 -p /sbin/ldconfig
%post -n libpcre2-posix3 -p /sbin/ldconfig
%postun -n libpcre2-posix3 -p /sbin/ldconfig

%files -n libpcre2-8-0
%license COPYING LICENCE
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/libpcre2-8.so.*

%files -n libpcre2-16-0
%license LICENCE
%{_libdir}/libpcre2-16.so.*

%files -n libpcre2-32-0
%license LICENCE
%{_libdir}/libpcre2-32.so.*

%files -n libpcre2-posix3
%license LICENCE
%{_libdir}/libpcre2-posix.so.*

%files tools
%license LICENCE
%{_bindir}/pcre2grep
%{_bindir}/pcre2test
%{_mandir}/man1/pcre2grep.1%{?ext_man}
%{_mandir}/man1/pcre2test.1%{?ext_man}

%files doc
%license COPYING LICENCE
%doc AUTHORS ChangeLog NEWS README
%doc doc/html doc/*.txt
%doc %{_defaultdocdir}/pcre2-doc

%files devel
%license LICENCE
%{_bindir}/pcre2-config
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libpcre2-8.pc
%{_libdir}/pkgconfig/libpcre2-16.pc
%{_libdir}/pkgconfig/libpcre2-32.pc
%{_libdir}/pkgconfig/libpcre2-posix.pc
%{_mandir}/man1/pcre2-config.1%{?ext_man}
%{_mandir}/man3/*%{ext_man}

%files devel-static
%{_libdir}/*.a

%changelog
