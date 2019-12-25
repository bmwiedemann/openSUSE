#
# spec file for package mozjs60
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2018 Luciano Santos <luc14n0@linuxmail.org>.
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


%global major   60
Name:           mozjs%{major}
Version:        60.9.0
Release:        0
Summary:        MozJS, or SpiderMonkey, is Mozilla's JavaScript engine written in C and C++
License:        MPL-2.0
Group:          Development/Libraries/Other
URL:            https://developer.mozilla.org/en-US/docs/Mozilla/Projects/SpiderMonkey
Source0:        https://ftp.mozilla.org/pub/firefox/releases/%{version}esr/source/firefox-%{version}esr.source.tar.xz
Source1:        LICENSE.txt
# This should be removed when bmo#1322212 and bmo#1264836 are resolved:
# Missing ICU big-endian data file in firefox source:
Source2:        icudt60b.dat.xz
Patch0:         mozjs60-fix-armv6-build.patch
Patch1:         mozjs60-mozilla-s390-bigendian.patch
Patch2:         riscv-support.patch
Patch3:         Always-use-the-equivalent-year-to-determine-the-time-zone.patch
# Build fixes - https://hg.mozilla.org/mozilla-central/rev/ca36a6c4f8a4a0ddaa033fdbe20836d87bbfb873
Patch4:         emitter.patch
Patch5:         emitter_test.patch
Patch6:         init_patch.patch
# s390x fixes:
# https://salsa.debian.org/gnome-team/mozjs60/blob/debian/master/debian/patches/enddianness.patch
Patch7:         enddianness.patch
# https://salsa.debian.org/gnome-team/mozjs60/blob/debian/master/debian/patches/jsproperty-endian.patch
Patch8:         jsproperty-endian.patch
# aarch64 fixes for -O2
Patch9:         Save-x28-before-clobbering-it-in-the-regex-compiler.patch
Patch10:        Save-and-restore-non-volatile-x28-on-ARM64-for-generated-unboxed-object-constructor.patch

BuildRequires:  autoconf213
BuildRequires:  gcc-c++
BuildRequires:  memory-constraints
BuildRequires:  pkgconfig
BuildRequires:  python-devel
BuildRequires:  python-pip
BuildRequires:  readline-devel
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(zlib)

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
%patch0 -p1
%ifarch s390 s390x ppc ppc64 m68k
%patch1 -p1
%endif
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1

# Remove zlib directory to make sure the use of zlib from distro:
rm -rf modules/zlib

cd js/src
# FIX-ME: This should be removed when bmo#1322212 and bmo#1264836 are resolved:
xz -dk %{SOURCE2}
DATFILE=%{SOURCE2}
DATFILE="${DATFILE%.xz}"
mv -v ${DATFILE} ../../config/external/icu/data/

%build
cd js/src
# No need to add build time to the binaries:
modified="$(sed -n '/^----/n;s/ - .*$//;p;q' "%{_sourcedir}/%{name}.changes")"
DATE="\"$(date -d "${modified}" "+%%b %%e %%Y")\""
TIME="\"$(date -d "${modified}" "+%%R")\""
find . -regex ".*\.c\|.*\.cpp\|.*\.h" -exec sed -i "s/__DATE__/${DATE}/g;s/__TIME__/${TIME}/g" {} +
#
# Add extra cflags for Power8 ppc64le compiling with gcc7+ (bmo#1399248)
%ifarch ppc64le
GCCVER=`gcc --version | sed "s/.* \([0-9]\.[0-9]\.[0-9]\).*/\1/" | head -n1`
if [ ${GCCVER} > "7.0" ]; then
XTRA_CFLAGS="-mcpu=power7 -mtune=power7"
fi
%endif
#
# Disable null pointer gcc6 optimization in gcc6 (rhbz#1328045):
export CFLAGS="%{optflags} -fno-tree-vrp -fno-strict-aliasing -fno-delete-null-pointer-checks ${XTRA_CFLAGS}"
export CXXFLAGS=$CFLAGS
autoconf-2.13
# An out of source directory build is wanted here to prevent failures:
mkdir build_OPT.OBJ
cd build_OPT.OBJ
../configure \
    --prefix=%{_prefix} \
    --libdir=%{_libdir} \
    --includedir=%{_includedir} \
    --enable-optimize \
    --enable-pie \
    --enable-posix-nspr-emulation \
    --enable-readline \
    --enable-shared-js \
    --enable-release \
    --with-intl-api \
    --with-pthreads \
    --disable-jemalloc \
    --without-system-icu \
    --with-system-zlib \

# Without adding these sources resulted library has weak symbols:
#echo "CPPSRCS += \$(DEPTH)/mfbt/Unified_cpp_mfbt0.cpp \$(DEPTH)/../../mfbt/Compression.cpp \$(DEPTH)/../../mfbt/decimal/Decimal.cpp" >> js/src/backend.mk
#echo "STATIC_LIBS += \$(DEPTH)/mfbt/libmfbt.a" >> js/src/backend.mk

# do not eat all memory
%limit_build -m 1300

%make_build

%install
cd js/src/build_OPT.OBJ
%make_install
# Remove unneeded executable bits:
chmod a-x  %{buildroot}%{_libdir}/pkgconfig/*.pc \
%{buildroot}%{_includedir}/mozjs-%{major}/unicode/selfmt.h \
%{buildroot}%{_includedir}/mozjs-%{major}/js-config.h
# Do not install static libraries:
rm -f %{buildroot}%{_libdir}/*.a %{buildroot}%{_libdir}/*.ajs %{buildroot}%{_bindir}/js-config
# Install files, not symlinks to build directory:
pushd %{buildroot}%{_includedir}
    for link in `find . -type l`; do
	header=`readlink $link`
	rm -f $link
	cp -p $header $link
    done
popd
install -m 755 dist/bin/js-gdb.py %{buildroot}%{_bindir}
# Install license file
install -m 644 %{SOURCE1} .

%check
## Tests are currently (60.1.0) failing
#cd js/src/build_OPT.OBJ
# Run SpiderMonkey tests:
#../tests/jstests.py -d -s -t 1800 --no-progress ../build_OPT.OBJ/js/src/shell/js \
%ifnarch s390 s390x ppc %{power64}
#;
%else
#|| :
%endif

# Run basic JIT tests. JIT is disabled on s390 and ppc (see bmo#1415360 comment 6):
%ifnarch s390 s390x ppc %{power64}
#../jit-test/jit_test.py -s -t 1800 --no-progress ../build_OPT.OBJ/js/src/shell/js basic
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
%{_bindir}/js-gdb.py
%{_libdir}/pkgconfig/*.pc
%{_includedir}/mozjs-%{major}

%changelog
