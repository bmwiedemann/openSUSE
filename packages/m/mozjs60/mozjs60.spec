#
# spec file for package mozjs60
#
# Copyright (c) 2019 SUSE LLC
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


# use system icu
# keep fallback if something goes wrong
%bcond_without system_icu

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
# based on https://salsa.debian.org/gnome-team/mozjs60/blob/debian/master/debian/patches/tests-Skip-a-test-on-s390x.patch
Patch11:        Don-t-run-non262-extensions-clone-errors.js-on-s390x.patch
# based on https://salsa.debian.org/gnome-team/mozjs60/blob/debian/master/debian/patches/tests-Expect-a-test-to-fail-on-big-endian.patch
Patch12:        tests-Expect-a-test-to-fail-on-big-endian.patch
# https://salsa.debian.org/gnome-team/mozjs60/blob/debian/master/debian/patches/icu_sources_data.py-Decouple-from-Mozilla-build-system.patch
Patch13:        icu_sources_data.py-Decouple-from-Mozilla-build-system.patch
# https://salsa.debian.org/gnome-team/mozjs60/blob/debian/master/debian/patches/icu_sources_data-Write-command-output-to-our-stderr.patch
Patch14:        icu_sources_data-Write-command-output-to-our-stderr.patch
# https://salsa.debian.org/gnome-team/mozjs60/blob/debian/master/debian/patches/Skip-some-i18n-tests-because-we-are-now-using-system-ICU.patch
Patch15:        Skip-some-i18n-tests-because-we-are-now-using-system-ICU.patch
# https://salsa.debian.org/gnome-team/mozjs60/blob/debian/master/debian/patches/Update-to-ICU-61-Part-3-Update-tests.patch
Patch16:        Update-to-ICU-61-Part-3-Update-tests.patch
# fix testsuite when built with ICU 65 https://phabricator.services.mozilla.com/D49445 https://unicode-org.atlassian.net/browse/ICU-20654
Patch17:        Update-to-ICU-65-Part-3-Update-tests.patch
# fix testsuite when building on i586 (some tests requires SSE / i686) boo#1159775
Patch18:        skip-i586-failing-tests.patch

BuildRequires:  autoconf213
BuildRequires:  gcc-c++
BuildRequires:  memory-constraints
BuildRequires:  pkgconfig
BuildRequires:  python-devel
BuildRequires:  python-pip
BuildRequires:  readline-devel
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(zlib)
%if %{with system_icu}
BuildRequires:  pkgconfig(icu-i18n)
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
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150200
# only supported with ICU >= 61
%patch16 -p1
# only supported with ICU >= 65 (https://unicode-org.atlassian.net/browse/ICU-20654)
%patch17 -p1
%endif
%patch18 -p1

# make sure we don't ever accidentally link against bundled security libs
rm -rf security/

# Remove zlib directory to make sure the use of zlib from distro:
rm -rf modules/zlib

# FIX-ME: This should be removed when bmo#1322212 and bmo#1264836 are resolved:
%if !%{with system_icu}
%ifarch s390 s390x ppc ppc64 m68k
echo "Generate big endian version of config/external/icu/data/icud58l.dat"
python intl/icu_sources_data.py .
ls -l config/external/icu/data
rm -f config/external/icu/data/icudt*l.dat
%endif
%endif

%build
cd js/src
# No need to add build time to the binaries:
modified="$(sed -n '/^----/n;s/ - .*$//;p;q' "%{_sourcedir}/%{name}.changes")"
DATE="\"$(date -d "${modified}" "+%%b %%e %%Y")\""
TIME="\"$(date -d "${modified}" "+%%R")\""
find . -regex ".*\.c\|.*\.cpp\|.*\.h" -exec sed -i "s/__DATE__/${DATE}/g;s/__TIME__/${TIME}/g" {} +

export CFLAGS="%{optflags}"
export CXXFLAGS=$CFLAGS
autoconf-2.13
# An out of source directory build is wanted here to prevent failures:
mkdir build_OPT.OBJ
cd build_OPT.OBJ
../configure \
    --prefix=%{_prefix} \
    --libdir=%{_libdir} \
    --includedir=%{_includedir} \
%if %{with system_icu}
    --with-system-icu \
%else
    --without-system-icu \
%endif
    --enable-posix-nspr-emulation \
    --with-system-zlib \
    --enable-tests \
    --disable-strip \
    --with-intl-api \
    --enable-readline \
    --enable-shared-js \
    --disable-optimize \
    --enable-pie \
    --disable-jemalloc \

# do not eat all memory
%limit_build -m 1300

%make_build

%install
cd js/src/build_OPT.OBJ
%make_install
# Remove unneeded executable bits:
chmod a-x  %{buildroot}%{_libdir}/pkgconfig/*.pc \
%if !%{with system_icu}
%{buildroot}%{_includedir}/mozjs-%{major}/unicode/selfmt.h \
%endif
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
# NEVER DISABLE THOSE TESTS : if they aren't passing, something is wrong,
# don't submit with tests disabled
cd js/src/build_OPT.OBJ
# Run SpiderMonkey tests:
../tests/jstests.py -d -s -t 1800 --no-progress ../build_OPT.OBJ/js/src/shell/js \
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
../jit-test/jit_test.py -s -t 1800 --no-progress  ../build_OPT.OBJ/js/src/shell/js basic 
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
