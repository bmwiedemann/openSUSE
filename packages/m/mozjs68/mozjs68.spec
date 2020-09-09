#
# spec file for package mozjs68
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


%global major   68
Name:           mozjs%{major}
Version:        68.12.0
Release:        0
Summary:        MozJS, or SpiderMonkey, is Mozilla's JavaScript engine written in C and C++
License:        MPL-2.0
Group:          Development/Libraries/Other
URL:            https://developer.mozilla.org/en-US/docs/Mozilla/Projects/SpiderMonkey
Source0:        https://ftp.mozilla.org/pub/firefox/releases/%{version}esr/source/firefox-%{version}esr.source.tar.xz
Source1:        LICENSE.txt

Patch0:         Don-t-run-non262-extensions-clone-errors.js-on-s390x.patch
Patch1:         Skip-some-i18n-tests-because-we-are-now-using-system-ICU.patch
Patch3:         Update-to-ICU-65-Part-3-Update-tests.patch
Patch4:         tests-increase-timeout.patch
Patch5:         jstests_python-3.patch
Patch6:         time-zone-path-test-Update-for-what-our-system-ICU-return.patch
Patch7:         tests-Adapt-formatted-strings-results-to-system-ICU.patch
Patch8:         TestingFunctions-Update-ICU-s-default-tz-when-setting-TZ.patch
Patch9:         Skip-time-zone-tests-that-fails-with-system-ICU.patch
Patch10:        Skip-tests-expected-fail-i586-ppc64.patch
Patch12:        mozilla-disable-wasm-emulate-arm-unaligned-fp-access.patch
Patch13:        Remove-unused-LLVM-and-Rust-build-dependencies.patch
Patch14:        Drop_backwards_test-Nuuk.patch

BuildRequires:  autoconf213
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  python
BuildRequires:  python-xml
BuildRequires:  python3-base
BuildRequires:  readline-devel
BuildRequires:  pkgconfig(icu-i18n) >= 63.1
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(zlib)
%ifarch ppc ppc64 ppc64le
BuildRequires:  memory-constraints
%endif

%description
JavaScript is the Netscape-developed object scripting language used in millions
of web pages and server applications worldwide. Netscape's JavaScript is a
super set of the ECMA-262 Edition 3 (ECMAScript) standard scripting language,
with only mild differences from the published standard.

This package contains the JavaScript's executable.

%package -n libmozjs-%{major}
Summary:        JavaScript's library
Group:          System/Libraries

%description -n libmozjs-%{major}
JavaScript is the Netscape-developed object scripting language used in millions
of web pages and server applications worldwide. Netscape's JavaScript is a
superset of the ECMA-262 Edition 3 (ECMAScript) standard scripting language,
with only mild differences from the published standard.

This package contains the JavaScript's library.

%package devel
Summary:        Development files and tools for %{name}
Group:          Development/Libraries/Other
Requires:       libmozjs-%{major} = %{version}
Requires:       pkgconfig

%description devel
JavaScript is the Netscape-developed object scripting language used in millions
of web pages and server applications worldwide. Netscape's JavaScript is a
super set of the ECMA-262 Edition 3 (ECMAScript) standard scripting language,
with only mild differences from the published standard.

This package contains the header file and tools to develop with JavaScript.

%prep
%setup -q -n firefox-%{version}
%autopatch -p1

# make sure we don't ever accidentally link against bundled security libs
rm -rf security/

# Remove zlib directory to make sure the use of zlib from distro:
rm -rf modules/zlib

%build
cd js/src

# Prefer GCC, because clang doesn't support -fstack-clash-protection yet
export CC=gcc
export CXX=g++

export AR=%{_bindir}/gcc-ar
export RANLIB=%{_bindir}/gcc-ranlib
export NM=%{_bindir}/gcc-nm

export CFLAGS="%{optflags}"
export CXXFLAGS=$CFLAGS
# An out of source directory build is wanted here to prevent failures:
mkdir build_OPT.OBJ
cd build_OPT.OBJ
../configure \
    --prefix=%{_prefix} \
    --libdir=%{_libdir} \
    --includedir=%{_includedir} \
    --with-system-icu \
    --enable-posix-nspr-emulation \
    --with-system-zlib \
    --enable-tests \
    --disable-strip \
    --with-intl-api \
    --enable-readline \
    --enable-shared-js \
    --enable-optimize \
    --disable-jemalloc \
    --enable-unaligned-private-values \
    --enable-posix-nspr-emulation \

# do not eat all memory
%ifarch ppc ppc64 ppc64le
%limit_build -m 1300
%endif

%make_build

%install
cd js/src/build_OPT.OBJ
%make_install
# Do not install static libraries:
rm -f %{buildroot}%{_libdir}/*.a %{buildroot}%{_libdir}/*.ajs %{buildroot}%{_bindir}/js-config
# Install license file
install -m 644 %{SOURCE1} .

%check
# NEVER DISABLE THOSE TESTS : if they aren't passing, something is wrong,
# don't submit with tests disabled
cd js/src/build_OPT.OBJ
# Run SpiderMonkey tests:
PYTHONPATH=../tests/lib ../tests/jstests.py -d -s -t 1800 --no-progress --wpt=disabled ./dist/bin/js%{major} \
%ifnarch s390
;
%else
|| :
%endif

# this test doesn't pass on i586, kill it
%ifarch i586
rm -f ../jit-test/tests/basic/bug653153.js
%endif
# Run basic JIT tests. JIT is disabled on s390 (see bmo#1415360 comment 6):
%ifnarch s390
PYTHONPATH=../tests/lib ../jit-test/jit_test.py -s -t 1800 --no-progress  ./dist/bin/js%{major} basic
%endif

%post -n libmozjs-%{major} -p /sbin/ldconfig
%postun -n libmozjs-%{major} -p /sbin/ldconfig

%files
%license js/src/build_OPT.OBJ/LICENSE.txt
%doc README.txt
%{_bindir}/js%{major}

%files -n libmozjs-%{major}
%{_libdir}/*.so

%files devel
%{_bindir}/js%{major}-config
%{_libdir}/pkgconfig/*.pc
%{_includedir}/mozjs-%{major}

%changelog
