#
# spec file for package xz
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


# avoid bootstrapping problem
%define _binary_payload w9.bzdio
Name:           xz
Version:        5.2.10
Release:        0
Summary:        A Program for Compressing Files with the Lempel–Ziv–Markov algorithm
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND SUSE-Public-Domain
Group:          Productivity/Archiving/Compression
URL:            https://tukaani.org/xz/
Source0:        https://tukaani.org/xz/%{name}-%{version}.tar.gz
Source1:        https://tukaani.org/xz/%{name}-%{version}.tar.gz.sig
Source2:        baselibs.conf
# from http://tukaani.org/misc/lasse_collin_pubkey.txt#/xz.keyring
Source3:        xz.keyring
Source4:        xznew
Source5:        xznew.1
BuildRequires:  pkgconfig
Provides:       lzma = %{version}
Obsoletes:      lzma < %{version}

%description
The xz command is a program for compressing files.
* Average compression ratio of LZMA is about 30%% better than that of
  gzip, and 15%% better than that of bzip2.
* Decompression speed is only little slower than that of gzip, being
  two to five times faster than bzip2.
* In fast mode, compresses faster than bzip2 with a comparable
  compression ratio.
* Achieving the best compression ratios takes four to even twelve
  times longer than with bzip2. However, this does not affect
  decompressing speed.
* Very similar command line interface to what gzip and bzip2 have.

%lang_package

%package -n liblzma5
Summary:        Lempel–Ziv–Markov chain algorithm compression library
License:        SUSE-Public-Domain
Group:          System/Libraries

%description -n liblzma5
Library for encoding/decoding LZMA files.

%package devel
Summary:        Development package for the LZMA library
License:        SUSE-Public-Domain
Group:          Development/Libraries/C and C++
Requires:       liblzma5 = %{version}
Provides:       lzma-devel = %{version}
Obsoletes:      lzma-devel < %{version}
Provides:       lzma-alpha-devel = %{version}
Obsoletes:      lzma-alpha-devel < %{version}

%description devel
This package contains the header files and libraries needed for
compiling programs using the LZMA library.

%prep
%autosetup

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
export CFLAGS="%{optflags} -D_REENTRANT -pipe -fPIE"
export LDFLAGS="-Wl,-z,relro,-z,now -pie"
%configure \
  --with-pic \
  --docdir=%{_docdir}/%{name} \
  --disable-static
%if 0%{?do_profiling}
  %make_build CFLAGS="${CFLAGS} %{cflags_profile_generate}"
  %make_build
  %make_build clean
  %make_build CFLAGS="${CFLAGS} %{cflags_profile_feedback}"
%else
  %make_build
%endif

%check
%make_build check

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name} --all-name --with-man
install -Dpm 0755 %{SOURCE4} %{buildroot}%{_bindir}/xznew
install -Dpm 0644 %{SOURCE5} %{buildroot}%{_mandir}/man1/xznew.1
rm -vf %{buildroot}%{_docdir}/%{name}/{COPYING,COPYING.GPLv2}

%post -n liblzma5 -p /sbin/ldconfig
%postun -n liblzma5 -p /sbin/ldconfig

%files lang -f %{name}.lang
%dir %{_mandir}/fr
%dir %{_mandir}/de

%files
%license COPYING COPYING.GPLv2
%{_docdir}/%{name}
%{_bindir}/lzcat
%{_bindir}/lzcmp
%{_bindir}/lzdiff
%{_bindir}/lzegrep
%{_bindir}/lzfgrep
%{_bindir}/lzgrep
%{_bindir}/lzless
%{_bindir}/lzma
%{_bindir}/lzmadec
%{_bindir}/lzmainfo
%{_bindir}/lzmore
%{_bindir}/unlzma
%{_bindir}/unxz
%{_bindir}/xz
%{_bindir}/xzcat
%{_bindir}/xzcmp
%{_bindir}/xzdec
%{_bindir}/xzdiff
%{_bindir}/xzegrep
%{_bindir}/xzfgrep
%{_bindir}/xzgrep
%{_bindir}/xzless
%{_bindir}/xzmore
%{_bindir}/xznew
%{_mandir}/man1/lzcat.1%{ext_man}
%{_mandir}/man1/lzcmp.1%{ext_man}
%{_mandir}/man1/lzdiff.1%{ext_man}
%{_mandir}/man1/lzegrep.1%{ext_man}
%{_mandir}/man1/lzfgrep.1%{ext_man}
%{_mandir}/man1/lzgrep.1%{ext_man}
%{_mandir}/man1/lzless.1%{ext_man}
%{_mandir}/man1/lzma.1%{ext_man}
%{_mandir}/man1/lzmadec.1%{ext_man}
%{_mandir}/man1/lzmainfo.1%{ext_man}
%{_mandir}/man1/lzmore.1%{ext_man}
%{_mandir}/man1/unlzma.1%{ext_man}
%{_mandir}/man1/unxz.1%{ext_man}
%{_mandir}/man1/xz.1%{ext_man}
%{_mandir}/man1/xzcat.1%{ext_man}
%{_mandir}/man1/xzcmp.1%{ext_man}
%{_mandir}/man1/xzdec.1%{ext_man}
%{_mandir}/man1/xzdiff.1%{ext_man}
%{_mandir}/man1/xzegrep.1%{ext_man}
%{_mandir}/man1/xzfgrep.1%{ext_man}
%{_mandir}/man1/xzgrep.1%{ext_man}
%{_mandir}/man1/xzless.1%{ext_man}
%{_mandir}/man1/xzmore.1%{ext_man}
%{_mandir}/man1/xznew.1%{ext_man}

%files -n liblzma5
%{_libdir}/liblzma.so.5*

%files devel
%{_includedir}/lzma.h
%dir %{_includedir}/lzma/
%{_includedir}/lzma/*
%{_libdir}/liblzma.so
%{_libdir}/pkgconfig/liblzma.pc

%changelog
