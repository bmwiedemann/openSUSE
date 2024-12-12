#
# spec file for package rhash
#
# Copyright (c) 2024 SUSE LLC
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


%define major   1
Name:           rhash
Version:        1.4.5
Release:        0
Summary:        Recursive Hasher
License:        0BSD
URL:            https://github.com/rhash/RHash
Source0:        https://github.com/rhash/RHash/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(openssl)

%description
RHash (Recurcive Hasher) is a console utility for computing and
verifying magnet links and hash sums of files.
It supports CRC32, MD4, MD5, SHA1/SHA2, Tiger, DC++ TTH, BitTorrent
BTIH, AICH, eDonkey hash, GOST R 34.11-94, RIPEMD-160, HAS-160, EDON-R,
Whirlpool and Snefru hash algorithms. Hash sums are used to ensure and
verify integrity of large volumes of data for a long-term storing or
transferring.

Program features:
 * Calculation of Magnet links and EDonkey 2000 links.
 * Output in a predefined (SFV, BSD-like) or a user-defined format.
 * Updating crc files (adding hash sums of files missing in the crc
   file).
 * Ability to process directories recursively.

%package -n librhash%{major}
Summary:        LibRHash Shared Library

%description -n librhash%{major}
LibRHash is a professional, portable, thread-safe C library for
computing a wide variety of hash sums, such as CRC32, MD4, MD5, SHA1,
SHA256, SHA512, AICH, ED2K, Tiger, DC++ TTH, BitTorrent BTIH, GOST R
34.11-94, RIPEMD-160 HAS-160, EDON-R, Whirlpool and Snefru.
Hash sums are used to ensure and verify integrity of large volumes of
data for a long-term storing or transferring.

%package devel
Summary:        Headers and Static Library for LibRHash
Requires:       librhash%{major} = %{version}
Provides:       librhash-devel = %{version}
Obsoletes:      librhash-devel < 1.3.1

%description devel
LibRHash is a professional, portable, thread-safe C library for
computing a wide variety of hash sums, such as CRC32, MD4, MD5, SHA1,
SHA256, SHA512, AICH, ED2K, Tiger, DC++ TTH, BitTorrent BTIH, GOST R
34.11-94, RIPEMD-160 HAS-160, EDON-R, Whirlpool and Snefru.
Hash sums are used to ensure and verify integrity of large volumes of
data for a long-term storing or transferring.

This package includes LibRHash development files.

%lang_package

%prep
%autosetup -n RHash-%{version} -p1

%build
# repleace unwanted fomit-frame pointer with desirable optflags
sed -i "s|-fomit-frame-pointer|%{optflags}|g" configure
# not a autotools configure
./configure \
  --prefix=%{_prefix} \
  --exec-prefix=%{_prefix} \
  --bindir=%{_bindir} \
  --sysconfdir=%{_sysconfdir} \
  --libdir=%{_libdir} \
  --mandir=%{_mandir} \
  --enable-lib-shared \
  --enable-gettext
%make_build

%install
%make_install install-lib-so-link install-lib-headers install-gmo
%find_lang %{name} %{?no_lang_C}

%check
%make_build test

%post -n librhash%{major} -p /sbin/ldconfig
%postun -n librhash%{major} -p /sbin/ldconfig

%files
%license COPYING
%doc ChangeLog README.md
%config(noreplace) %{_sysconfdir}/rhashrc
%{_bindir}/ed2k-link
%{_bindir}/edonr256-hash
%{_bindir}/edonr512-hash
%{_bindir}/gost12-256-hash
%{_bindir}/gost12-512-hash
%{_bindir}/has160-hash
%{_bindir}/magnet-link
%{_bindir}/rhash
%{_bindir}/sfv-hash
%{_bindir}/tiger-hash
%{_bindir}/tth-hash
%{_bindir}/whirlpool-hash
%{_mandir}/man1/ed2k-link.1%{?ext_man}
%{_mandir}/man1/edonr256-hash.1%{?ext_man}
%{_mandir}/man1/edonr512-hash.1%{?ext_man}
%{_mandir}/man1/gost12-256-hash.1%{?ext_man}
%{_mandir}/man1/gost12-512-hash.1%{?ext_man}
%{_mandir}/man1/has160-hash.1%{?ext_man}
%{_mandir}/man1/magnet-link.1%{?ext_man}
%{_mandir}/man1/rhash.1%{?ext_man}
%{_mandir}/man1/sfv-hash.1%{?ext_man}
%{_mandir}/man1/tiger-hash.1%{?ext_man}
%{_mandir}/man1/tth-hash.1%{?ext_man}
%{_mandir}/man1/whirlpool-hash.1%{?ext_man}

%files -n librhash%{major}
%{_libdir}/librhash.so.%{major}*

%files devel
%license COPYING
%doc ChangeLog README.md
%{_includedir}/rhash.h
%{_includedir}/rhash_torrent.h
%{_libdir}/librhash.so

%files lang -f %{name}.lang

%changelog
