#
# spec file
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


%define _lto_cflags %{nil}
%ifarch %{ix86}
%global rust_arch i686
%global _host i686-suse-linux-gnu
ExclusiveArch:  i586 i686
BuildArch:      i686
%{expand:%%global optflags %(echo "%optflags"|sed -e s/i586/i686/) -march=i686 -mtune=generic}
%endif

# upstream default is clang (to use gcc for large parts set to 0)
%define clang_build 0

%global major 102
# LTO - Enable in Release builds, but consider disabling for development as it increases compile time
%global build_with_lto    1
# Require tests to pass?
%global require_tests     0
# LTO is default since F33 and F32 package is backported as is, so no LTO there
# Big endian platforms
%ifarch ppc ppc64 s390 s390x
%global big_endian 1
%endif
Name:           mozjs%{major}
Version:        102.6.0
Release:        1%{?dist}
Summary:        SpiderMonkey JavaScript library
License:        MPL-2.0
Group:          System/Libraries
URL:            https://developer.mozilla.org/en-US/docs/Mozilla/Projects/SpiderMonkey
Source0:        https://ftp.mozilla.org/pub/firefox/releases/%{version}esr/source/firefox-%{version}esr.source.tar.xz
Source1:        https://ftp.mozilla.org/pub/firefox/releases/%{version}esr/source/firefox-%{version}esr.source.tar.xz.asc
Source2:        https://ftp.mozilla.org/pub/firefox/releases/%{version}esr/KEY#/mozilla.keyring
# Known failures with system libicu
Source3:        known_failures.txt

# Patches from mozjs78, rebased for mozjs91:
Patch01:        fix-soname.patch
Patch02:        copy-headers.patch
Patch03:        tests-increase-timeout.patch
Patch09:        icu_sources_data.py-Decouple-from-Mozilla-build-system.patch
Patch10:        icu_sources_data-Write-command-output-to-our-stderr.patch
# Build fixes - https://hg.mozilla.org/mozilla-central/rev/ca36a6c4f8a4a0ddaa033fdbe20836d87bbfb873
Patch12:        emitter.patch
# Build fixes
Patch13:        init_patch.patch
Patch14:        remove-sloppy-m4-detection-from-bundled-autoconf.patch
# TODO: Check with mozilla for cause of these fails and re-enable spidermonkey compile time checks if needed
Patch15:        spidermonkey_checks_disable.patch
# s390x/ppc64 fixes, TODO: file bug report upstream?
Patch18:        spidermonkey_style_check_disable_s390x.patch
Patch19:        0001-Skip-failing-tests-on-ppc64-and-s390x.patch
Patch20:        Fix-i586-float-math.patch

BuildRequires:  autoconf213
BuildRequires:  cargo
BuildRequires:  ccache
BuildRequires:  clang-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  llvm
BuildRequires:  llvm-devel
BuildRequires:  nasm
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-six
BuildRequires:  readline-devel
BuildRequires:  rust
BuildRequires:  pkgconfig(icu-i18n) >= 67.1
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(nspr)
BuildRequires:  pkgconfig(zlib)
%if 0%{?big_endian}
BuildRequires:  icu
%endif

%description
SpiderMonkey is the code-name for Mozilla Firefox's C++ implementation of
JavaScript. It is intended to be embedded in other applications
that provide host environments for JavaScript.

%package -n libmozjs-%{major}-0
Summary:        JavaScript's library
Group:          System/Libraries

%description -n libmozjs-%{major}-0
JavaScript is the Netscape-developed object scripting language used in millions
of web pages and server applications worldwide. Netscape's JavaScript is a
superset of the ECMA-262 Edition 3 (ECMAScript) standard scripting language,
with only mild differences from the published standard.

This package contains the JavaScript's library.

%package devel
Summary:        Development files and tools for %{name}
Group:          Development/Libraries/Other
Requires:       libmozjs-%{major}-0 = %{version}
Requires:       pkgconfig

%description devel
JavaScript is the Netscape-developed object scripting language used in millions
of web pages and server applications worldwide. Netscape's JavaScript is a
super set of the ECMA-262 Edition 3 (ECMAScript) standard scripting language,
with only mild differences from the published standard.

This package contains the header file and tools to develop with JavaScript.

%prep
%setup -q -n firefox-%{version}/js/src

pushd ../..
%patch01 -p1
%patch02 -p1
%patch03 -p1
%patch09 -p1
%patch10 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%ifarch s390x
%patch18 -p1
%endif
# Fixes for ppc64 and s390x, there is no need to keep it in ifarch here since mozilla tests support ifarch conditions
%patch19 -p1
%patch20 -p1

# Copy out the LICENSE file
cp LICENSE js/src/

# Copy out file containing known test failures with system libicu
cp %{SOURCE3} js/src/

popd

# Remove zlib directory (to be sure using system version)
rm -rf ../../modules/zlib

%build
%if 0%{?clang_build} == 0
export CC=gcc
export CXX=g++
%ifarch ppc64 ppc64le
export CFLAGS="$CFLAGS -mminimal-toc"
%endif
%endif
%ifarch %arm %ix86
# Limit RAM usage during link
export LDFLAGS="${LDFLAGS} -Wl,--no-keep-memory -Wl,--reduce-memory-overheads"
%endif

# Workaround
# error: options `-C embed-bitcode=no` and `-C lto` are incompatible
# error: could not compile `jsrust`.
# https://github.com/japaric/cargo-call-stack/issues/25
export RUSTFLAGS="-C embed-bitcode"

%if 0%{?build_with_lto}
# https://github.com/ptomato/mozjs/commit/36bb7982b41e0ef9a65f7174252ab996cd6777bd
export CARGO_PROFILE_RELEASE_LTO=true
%endif

export CFLAGS="%{optflags}"
export CXXFLAGS="$CFLAGS"
export LINKFLAGS="%{?__global_ldflags}"
export PYTHON="python3"

autoconf-2.13
%configure \
	--with-system-icu \
	--with-system-zlib \
	--disable-tests \
	--disable-strip \
	--with-intl-api \
	--enable-readline \
	--enable-shared-js \
	--enable-optimize \
	--disable-debug \
	--enable-pie \
	--disable-jemalloc

%if 0%{?big_endian}
echo "Generate big endian version of config/external/icu/data/icud71l.dat"
pushd ../..
  /usr/sbin/icupkg -tb config/external/icu/data/icudt71l.dat config/external/icu/data/icudt71b.dat
  rm config/external/icu/data/icudt*l.dat
popd
%endif

%make_build

%install
%make_install

# Fix permissions
chmod -x %{buildroot}%{_libdir}/pkgconfig/*.pc

# Avoid multilib conflicts
case `uname -i` in
  i386 | ppc | s390 | sparc )
    wordsize="32"
    ;;
  x86_64 | ppc64 | s390x | sparc64 )
    wordsize="64"
    ;;
  *)
    wordsize=""
    ;;
esac

if test -n "$wordsize"
then
  mv %{buildroot}%{_includedir}/mozjs-%{major}/js-config.h \
     %{buildroot}%{_includedir}/mozjs-%{major}/js-config-$wordsize.h

  cat >%{buildroot}%{_includedir}/mozjs-%{major}/js-config.h <<EOF
#ifndef JS_CONFIG_H_MULTILIB
#define JS_CONFIG_H_MULTILIB

#include <bits/wordsize.h>

#if __WORDSIZE == 32
# include "js-config-32.h"
#elif __WORDSIZE == 64
# include "js-config-64.h"
#else
# error "unexpected value for __WORDSIZE macro"
#endif

#endif
EOF

fi

# Remove unneeded files
rm %{buildroot}%{_bindir}/js%{major}-config
rm %{buildroot}%{_libdir}/libjs_static.ajs

# Rename library and create symlinks, following fix-soname.patch
mv %{buildroot}%{_libdir}/libmozjs-%{major}.so \
   %{buildroot}%{_libdir}/libmozjs-%{major}.so.0.0.0
ln -s libmozjs-%{major}.so.0.0.0 %{buildroot}%{_libdir}/libmozjs-%{major}.so.0
ln -s libmozjs-%{major}.so.0 %{buildroot}%{_libdir}/libmozjs-%{major}.so

%check
# Run SpiderMonkey tests
%if 0%{?require_tests}
PYTHONPATH=tests/lib python3 tests/jstests.py -d -s -t 1800 --exclude-file=known_failures.txt --no-progress --wpt=disabled ../../js/src/dist/bin/js%{major}
%else
PYTHONPATH=tests/lib python3 tests/jstests.py -d -s -t 1800 --exclude-file=known_failures.txt --no-progress --wpt=disabled ../../js/src/dist/bin/js%{major} || :
%endif

# Run basic JIT tests
%if 0%{?require_tests}
PYTHONPATH=tests/lib python3 jit-test/jit_test.py -s -t 1800 --no-progress ../../js/src/dist/bin/js%{major} basic
%else
PYTHONPATH=tests/lib python3 jit-test/jit_test.py -s -t 1800 --no-progress ../../js/src/dist/bin/js%{major} basic || :
%endif

%ldconfig_scriptlets -n libmozjs-%{major}-0

%files
%doc README.html
%{_bindir}/js%{major}

%files -n libmozjs-%{major}-0
%license LICENSE
%{_libdir}/libmozjs-%{major}.so.0*

%files devel
%{_libdir}/libmozjs-%{major}.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/mozjs-%{major}/

%changelog
