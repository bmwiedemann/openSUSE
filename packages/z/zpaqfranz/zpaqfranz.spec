#
# spec file for package zpaqfranz
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           zpaqfranz
Version:        65.5
Release:        0
Summary:        A journaling, incremental, deduplicating archiver
# Legal-Review-Notice: zpaqfranz is a single-translation-unit program that
# embeds a large amount of third-party code. Upstream enumerates every piece
# in the "Credits and copyrights and licenses" block of zpaqfranz.cpp
# (28 entries); the tag below is the union of what that block declares,
# after electing the permissive side of the two dual-licensed pieces:
#  - zpaqfranz itself and libdivsufsort, Embedded Artistry, nilsimsa, zsfx
#    and ascii-art: MIT (LICENSE is the MIT text),
#  - zpaq, libtomcrypt AES, salsa20, unzpaq206, the encode.su modifications,
#    Whirlpool, SHA-Intrinsics and the man page: public domain,
#  - Crc32, hash-library (MD5/SHA-3) and crc32c: Zlib,
#  - wyhash: Unlicense,
#  - xxHash and LZ4: BSD-2-Clause,
#  - HighwayHash: Apache-2.0, and BLAKE3 is "CC0-1.0 OR Apache-2.0" - we
#    elect Apache-2.0, which is already required by HighwayHash, so no
#    CC0-1.0 obligation is taken on,
#  - the libtomcrypt AES is "public domain OR WTFPL" - we elect public domain,
#  - Twofish by Niels Ferguson: Ferguson-Twofish.
#  - zstd 1.5.7 (65.5, entry 28), the -m8 backend: BSD-3-Clause.
# The bundled curl.h is licensed under the curl licence, but only the header
# is present: libcurl and libssh are dlopened at run time and no curl or
# libssh code is linked into the binary, so it is not part of this tag.
# The Sha1Opt.asm / 7zAsm.asm public-domain code (entry 5) is Windows-only
# and never compiled here.
# Entries 25 (libfuse, LGPL) and 26 (WinFsp, GPL-3.0 with a FLOSS exception)
# belong to the new "mount" command, which exists only under -DZPAQMOUNT.
# That is not defined below, so no FUSE code is compiled and neither entry
# is part of this tag.
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND MIT AND SUSE-Public-Domain AND Zlib AND Unlicense AND Ferguson-Twofish
URL:            https://github.com/fcorbelli/zpaqfranz
Source0:        https://github.com/fcorbelli/zpaqfranz/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Upstream's tag 65.5 still points at the 65.4 commit; the 65.5 code is
# published only as a release asset.
Source1:        https://github.com/fcorbelli/zpaqfranz/releases/download/%{version}/%{name}.cpp
BuildRequires:  gcc-c++
# libcurl and libssh are dlopened by name at run time for the URL and SFTP
# features; the binary does not link them, so these stay weak dependencies.
Recommends:     libcurl4
Recommends:     libssh4
# Third-party code bundled into the single zpaqfranz.cpp translation unit.
Provides:       bundled(blake3)
Provides:       bundled(highwayhash)
Provides:       bundled(libdivsufsort-lite) = 2.00
Provides:       bundled(lz4)
Provides:       bundled(xxhash)
Provides:       bundled(zstd) = 1.5.7

%description
Swiss army knife for backup and disaster recovery, like 7z or RAR on
steroids,with deduplicated "snapshots" (versions). Conceptually similar to Mac
time machine, but much more efficiently.

%prep
%autosetup -p1
# The tag archive still carries the 65.4 zpaqfranz.cpp; the release asset
# is the 65.5 one.
cp %{SOURCE1} zpaqfranz.cpp
# Upstream ships these two with CRLF line endings, which rpmlint rejects.
sed -i 's/\r$//' CHANGELOG.md COPYING

%build
%{set_build_flags}
# Upstream's Makefile does not know about s390x and strips the executable, so
# the single translation unit is compiled directly.
g++ $CXXFLAGS $LDFLAGS \
    -Dunix \
    -DIPV6 \
%ifarch %{ix86}
    -DHWSHA2 \
%else
    -DNOJIT \
%endif
%ifarch s390x
    -DBIG \
%else
    -DSFTP \
%endif
    zpaqfranz.cpp -o zpaqfranz -pthread -ldl -lm

%install
install -Dpm 0755 zpaqfranz %{buildroot}%{_bindir}/%{name}
install -Dpm 0644 man/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%check
# Upstream's built-in self test, then a create/verify round trip. Both run
# against the build directory copy, which is still unstripped - upstream notes
# that stripping the binary loses the autotest capability. -all is upstream's
# own test target (Makefile and every CI job), not the hobbled subset the
# binary runs by default.
./zpaqfranz autotest -all
./zpaqfranz a test.zpaq LICENSE
./zpaqfranz v test.zpaq

%files
%doc CHANGELOG.md README.md TODO.md
%license LICENSE COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
