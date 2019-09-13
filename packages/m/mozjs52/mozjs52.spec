#
# spec file for package mozjs52
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


%global		major 52
Name:           mozjs%{major}
Version:        52.6.0
Release:        0%{?dist}
Summary:        JavaScript interpreter and libraries
License:        MPL-2.0
Group:          Development/Libraries/Other
Url:            https://developer.mozilla.org/en-US/docs/Mozilla/Projects/SpiderMonkey/Releases/52
Source0:        https://ftp.mozilla.org/pub/firefox/releases/%{version}esr/source/firefox-%{version}esr.source.tar.xz
Source1:        LICENSE.txt
# This should be removed when bmo#1322212 and bmo#1264836 are resolved:
# Missing ICU big-endian data file in firefox source:
Source2:        icudt58b.dat.xz

Patch1:         bmo1176787.patch
Patch2:         fix_armv6_build.patch
Patch3:         mozilla-s390-bigendian.patch
Patch4:         xulrunner-24.0-s390-inlines.patch
BuildRequires:  autoconf213
BuildRequires:  gcc-c++
BuildRequires:  libicu-devel
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

%package -n libmozjs-%{major}
Summary:        JavaScript library
Group:          System/Libraries

%description -n libmozjs-%{major}
JavaScript is the Netscape-developed object scripting language used in millions
of web pages and server applications worldwide. Netscape's JavaScript is a
superset of the ECMA-262 Edition 3 (ECMAScript) standard scripting language,
with only mild differences from the published standard.

%package devel
Summary:        Header files, libraries and development documentation for %{name}
Group:          Development/Libraries/Other
Requires:       libmozjs-%{major} = %{version}-%{release}
Requires:       pkgconfig

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -q -n firefox-%{version}esr
pushd js/src
popd
%patch1 -p1
%patch2 -p1
%ifarch s390x ppc64
%patch3 -p1
%patch4 -p1
%endif

# Remove zlib directory (to assure using the system version)
rm -rf modules/zlib

cd js/src
# Fix release number
head -n -1 ../../config/milestone.txt > ../../config/milestone.txt
echo "%{version}" >> ../../config/milestone.txt
# Make mozjs these functions visible:
# JS::UTF8CharsToNewTwoByteCharsZ and JS::LossyUTF8CharsToNewTwoByteCharsZ
sed -i 's|^\(TwoByteCharsZ\)$|JS_PUBLIC_API\(\1\)|g' vm/CharacterEncoding.cpp
sed -i 's|^extern\ \(TwoByteCharsZ\)$|JS_PUBLIC_API\(\1\)|g' ../public/CharacterEncoding.h
# Also make visible js::DisableExtraThreads()
sed -i '/^void$/{$!{N;s/^\(void\)\n\(js\:\:DisableExtraThreads()\)$/JS_PUBLIC_API\(\1\)\n\2/;ty;P;D;:y}}'  vm/Runtime.cpp
sed -i 's|\(void\) \(DisableExtraThreads()\)|JS_PUBLIC_API\(\1\) \2|g'  vm/Runtime.h

# This should be removed when bmo#1322212 and bmo#1264836 are resolved:
xz -dk %{SOURCE2}
DATFILE=%{SOURCE2}
DATFILE="${DATFILE%.xz}"
mv -v ${DATFILE} ../../config/external/icu/data/

%build
cd js/src
# no need to add build time to binaries
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
# Disable null pointer gcc6 optimization in gcc6 (rhbz#1328045)
export CFLAGS="%{optflags} -fno-tree-vrp -fno-strict-aliasing -fno-delete-null-pointer-checks -Wno-format-overflow ${XTRA_CFLAGS}"
export CXXFLAGS=$CFLAGS
autoconf-2.13
./configure \
 --prefix=%{_prefix} \
 --libdir=%{_libdir} \
 --includedir=%{_includedir} \
 --enable-optimize \
 --enable-pie \
 --enable-posix-nspr-emulation \
 --enable-readline \
 --enable-release \
 --enable-shared-js \
 --with-intl-api \
 --with-pthreads \
%if 0%{?suse_version} > 1320
 --without-system-icu \
%endif
 --with-system-zlib

# Without adding these sources resulted library has weak symbols
#echo "CPPSRCS += \$(DEPTH)/mfbt/Unified_cpp_mfbt0.cpp \$(DEPTH)/../../mfbt/Compression.cpp \$(DEPTH)/../../mfbt/decimal/Decimal.cpp" >> js/src/backend.mk
#echo "STATIC_LIBS += \$(DEPTH)/mfbt/libmfbt.a" >> js/src/backend.mk

make %{?_smp_mflags}

%install
cd js/src
%make_install
chmod a-x  %{buildroot}%{_libdir}/pkgconfig/*.pc
# Do not install static libraries
rm -f %{buildroot}%{_libdir}/*.a %{buildroot}%{_libdir}/*.ajs %{buildroot}%{_bindir}/js-config
#mv %{buildroot}%{_bindir}/js %{buildroot}%{_bindir}/js%{major}
# Install files, not symlinks to build directory
pushd %{buildroot}%{_includedir}
    for link in `find . -type l`; do
	header=`readlink $link`
	rm -f $link
	cp -p $header $link
    done
popd
cp -p js/src/js-config.h %{buildroot}%{_includedir}/mozjs-%{major}
# Install license file
cp %{SOURCE1} .

%check
cd js/src
# Run SpiderMonkey tests
tests/jstests.py -d -s -t 1800 --no-progress ../../js/src/js/src/shell/js \
%ifnarch s390 s390x ppc %{power64}
;
%else
|| :
%endif

# Run basic JIT tests. JIT is disabled on s390 and ppc (see bmo#1415360 comment 6)
%ifnarch s390 s390x ppc %{power64}
jit-test/jit_test.py -s -t 1800 --no-progress ../../js/src/js/src/shell/js basic
%endif

%post -n libmozjs-%{major} -p /sbin/ldconfig
%postun -n libmozjs-%{major} -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc README.txt js/src/LICENSE.txt
%{_bindir}/js%{major}

%files -n libmozjs-%{major}
%defattr(-,root,root,-)
%{_libdir}/*.so

%files devel
%defattr(-,root,root,-)
%{_bindir}/js%{major}-config
%{_libdir}/pkgconfig/*.pc
%{_includedir}/mozjs-%{major}

%changelog
