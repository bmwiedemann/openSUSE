#
# spec file for package xar
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


# Apple xar build number (the actual upstream now that mackyle's fork is dead)
%define apple 503
%define sover 1
Name:           xar
Version:        1.8.0.0.%{apple}
Release:        0
Summary:        Extensible Archive Format Tools
License:        BSD-3-Clause
URL:            https://github.com/apple-oss-distributions/xar
Source:         https://github.com/apple-oss-distributions/xar/archive/%{name}-%{apple}.tar.gz#/%{name}-%{apple}.tar.gz
# Linux-build patch set, tracked by Gentoo (app-arch/xar) for the Apple lineage:
# PATCH-FIX-OPENSUSE ext2.patch — build the ext2 attribute support against e2fsprogs
Patch0:         xar-1.6.1-ext2.patch
# PATCH-FIX-OPENSUSE safe_dirname — provide a non-Darwin safe_dirname
Patch1:         xar-1.8-safe_dirname.patch
# PATCH-FIX-OPENSUSE build on arm/ppc
Patch2:         xar-1.8-arm-ppc.patch
# PATCH-FIX-OPENSUSE build against OpenSSL 1.1+
Patch3:         xar-1.8-openssl-1.1.patch
# PATCH-FIX-OPENSUSE Linux portability
Patch4:         xar-1.8.0.0.452-linux.patch
# PATCH-FIX-OPENSUSE drop remaining Darwin-only bits
Patch5:         xar-1.8.0.0.487-non-darwin.patch
# PATCH-FIX-OPENSUSE fix a variable-sized object
Patch6:         xar-1.8.0.0.487-variable-sized-object.patch
# PATCH-FIX-OPENSUSE add missing implicit declarations
Patch7:         xar-1.8.0.0.498-impl-decls.patch
# PATCH-FIX-OPENSUSE resolve an fd's path via /proc/self/fd where macOS F_GETPATH is unavailable
Patch8:         xar-1.8.0.0.503-linux-F_GETPATH.patch
BuildRequires:  autoconf
BuildRequires:  e2fsprogs-devel
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(libacl)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(zlib)

%description
The XAR project aims to provide an easily extensible archive format. Important
design decisions include an easily extensible XML table of contents for random
access to archived files, storing the toc at the beginning of the archive to
allow for efficient handling of streamed archives, the ability to handle files
of arbitrarily large sizes, the ability to choose independent encodings for
individual files in the archive, the ability to store checksums for individual
files in both compressed and uncompressed form, and the ability to query the
table of content's rich meta-data.

%package -n libxar%{sover}
Summary:        Extensive Archive Format Library

%description -n libxar%{sover}
The XAR project aims to provide an easily extensible archive format. Important
design decisions include an easily extensible XML table of contents for random
access to archived files, storing the toc at the beginning of the archive to
allow for efficient handling of streamed archives, the ability to handle files
of arbitrarily large sizes, the ability to choose independent encodings for
individual files in the archive, the ability to store checksums for individual
files in both compressed and uncompressed form, and the ability to query the
table of content's rich meta-data.

%package -n libxar-devel
Summary:        Extensive Archive Format Library
Requires:       libxar%{sover} = %{version}

%description -n libxar-devel
The XAR project aims to provide an easily extensible archive format. Important
design decisions include an easily extensible XML table of contents for random
access to archived files, storing the toc at the beginning of the archive to
allow for efficient handling of streamed archives, the ability to handle files
of arbitrarily large sizes, the ability to choose independent encodings for
individual files in the archive, the ability to store checksums for individual
files in both compressed and uncompressed form, and the ability to query the
table of content's rich meta-data.

%prep
%setup -q -n %{name}-%{name}-%{apple}
%patch -P 0 -p1 -d xar
%patch -P 1 -p1 -d xar
%patch -P 2 -p1 -d xar
%patch -P 3 -p1 -d xar
%patch -P 4 -p1 -d xar
%patch -P 5 -p1 -d xar
%patch -P 6 -p1 -d xar
%patch -P 7 -p1 -d xar
%patch -P 8 -p1 -d xar
pushd xar
# make the public headers reachable as <xar/...> and from src/ (they ship in lib/)
mv lib/*.h include/
ln -sf . include/xar
# drop the macOS @RPATH@ and the CommonCrypto path (use OpenSSL on Linux)
sed -i -e 's/@RPATH@//' src/Makefile.inc.in
echo ".PRECIOUS: @objroot@src/%.o" >> src/Makefile.inc.in
sed -i -e 's/__APPLE__/__NO_APPLE__/' include/archive.h lib/hash.c
popd

%build
pushd xar
# the shipped configure is stale vs the patched configure.ac -> regenerate
./autogen.sh --noconfigure
export LIBS="$(pkg-config --libs openssl)"
export CFLAGS="%{optflags} -Wno-unused-result"
%configure --disable-static
%make_build
popd

%install
pushd xar
%make_install
popd
find %{buildroot} -type f -name "*.la" -delete -print

%ldconfig_scriptlets -n libxar%{sover}

%files
%license xar/LICENSE
%doc xar/ChangeLog
%{_bindir}/xar
%{_mandir}/man1/xar.1%{?ext_man}

%files -n libxar%{sover}
%license xar/LICENSE
%{_libdir}/libxar.so.%{sover}*

%files -n libxar-devel
%license xar/LICENSE
%{_includedir}/xar
%{_libdir}/libxar.so

%changelog
