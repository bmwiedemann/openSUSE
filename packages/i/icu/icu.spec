#
# spec file for package icu
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


# what icu thinks the package is
%define amajor 76
%define aversion 76.1
# for the rare case that SUSE needs to workaround ABI breaks:
%define sonum %amajor
# like sonum, but with underscore
%define lname libicu%amajor

%ifarch %armb hppa mips mips64 ppc ppc64 %sparc s390 s390x m68k
%define be_platform 1
%else
%define be_platform 0
%endif
# icu-versioning.diff needs update for new Version too
Name:           icu
Version:        76.1
Release:        0
Summary:        International Components for Unicode
License:        ICU
Group:          Development/Libraries/C and C++
URL:            https://icu.unicode.org/
Source:         https://github.com/unicode-org/icu/releases/download/release-76-1/icu4c-76_1-src.tgz
Source2:        https://github.com/unicode-org/icu/releases/download/release-76-1/icu4c-76_1-src.tgz.asc
Source3:        https://github.com/unicode-org/icu/releases/download/release-76-1/icu4c-76_1-docs.zip
Source4:        https://github.com/unicode-org/icu/releases/download/release-76-1/icu4c-76_1-docs.zip.asc
Source5:        %name.keyring
Source100:      baselibs.conf
Patch4:         icu-fix-install-mode-files.diff
Patch6:         icu-error-reporting.diff
Patch7:         icu-avoid-x87-excess-precision.diff
Patch8:         locale.diff
Patch9:         nan-undefined-conversion.patch
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkg-config
BuildRequires:  python3-base
BuildRequires:  unzip
Provides:       bundled(timezone) = 2024b

%description
ICU is a set of C and C++ libraries that provide extensive Unicode and locale
support, such as calendar, conversions for many character sets, language
sensitive collation, date and time formatting, support for many locales,
message catalogs and resources, message formatting, normalization, number and
currency formatting, time zone support, transliteration, and word, line, and
sentence breaking.

This subpackage contains the runtime programs for interacting with ICU.

%package -n %lname
Summary:        International Components for Unicode
Group:          System/Libraries
Requires:       timezone
Provides:       libicu = %version
%if %be_platform
Requires:       libicu%sonum-bedata = %version
%else
Requires:       libicu%sonum-ledata = %version
%endif

%description -n %lname
ICU is a set of C and C++ libraries that provide extensive Unicode
and locale support.
This package contains the runtime libraries for ICU.

%package -n libicu%sonum-bedata
Summary:        Rule databases and tables for ICU
Group:          System/Libraries
BuildArch:      noarch

%description -n libicu%sonum-bedata
ICU is a set of C and C++ libraries that provide extensive Unicode
and locale support.

ICU makes use of a wide variety of data tables to provide many of its
services: converter mapping tables, collation rules, transliteration
rules, break iterator rules and dictionaries.

This subpackage contains these data tables, in big-endian format.

%package -n libicu%sonum-ledata
Summary:        Rule databases and tables for ICU
Group:          System/Libraries
BuildArch:      noarch

%description -n libicu%sonum-ledata
ICU is a set of C and C++ libraries that provide extensive Unicode
and locale support.

ICU makes use of a wide variety of data tables to provide many of its
services: converter mapping tables, collation rules, transliteration
rules, break iterator rules and dictionaries.

This subpackage contains these data tables, in little-endian format.

%package -n libicu-devel
Summary:        Development files for the ICU library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description -n libicu-devel
ICU is a set of C and C++ libraries that provide extensive Unicode
and locale support.
This package contains the headers for ICU.

%package -n libicu-doc
Summary:        Documentation for the ICU library
Group:          Documentation/HTML

%description -n libicu-doc
ICU is a set of C and C++ libraries that provide extensive Unicode
and locale support.
This package contains the HTML documentation.

%prep
%autosetup -p1 -n icu

# docs are special
mkdir html
pushd html/
unzip %SOURCE3
popd

%build
cd source
mkdir -p data/out/tmp # build procedure forgets to do this on its own
export CXXFLAGS="%optflags -DICU_DATA_DIR=\\\"%_datadir/icu/%version/\\\" -fexcess-precision=fast"
export CFLAGS="$CXXFLAGS"
%configure \
	--disable-static \
	--enable-shared \
	--disable-samples \
	--with-data-packaging=archive
%make_build VERBOSE=1
# Build the other endianess, too.
pushd data/
%if %be_platform
cp in/icudt%{amajor}l.dat out/
%else
LD_LIBRARY_PATH="../lib:../stubdata:../tools/ctestfw:$LD_LIBRARY_PATH" \
	../bin/icupkg -tb in/icudt%{amajor}l.dat out/icudt%{amajor}b.dat
! cmp in/icudt%{amajor}l.dat out/icudt%{amajor}b.dat
%endif
popd

%install
b="%buildroot"
mkdir -p "$b/%_docdir/%name"
cp -a html "$b/%_docdir/%name/"
cp -a license.html readme.html "$b/%_docdir/%name/"

find . -name CVS -type d -exec rm -Rf "{}" "+"
cd source

%make_install
cp data/out/icudt*.dat "$b/%_datadir/icu/%aversion/"

# /usr/lib/rpm/elfdeps requires +x bit and not all files had it at one point.
# - OpenBSD for example is known to have patched their libtool program
# to kill the x bit on install :(
chmod a+rx "$b/%_libdir"/lib*.so.*

# install uncompiled source data:
mkdir -p "$b/%_datadir/icu/%aversion/unidata"
install -m 644 data/unidata/*.txt "$b/%_datadir/icu/%aversion/unidata"
ln -s unidata/UnicodeData.txt "$b/%_datadir/icu/%aversion/"

rm "$b/%_datadir/icu/%aversion/install-sh"
# Seems unused
rm -Rf "$b/%_datadir/icu/%aversion/unidata/" \
	"$b/%_datadir/icu/%aversion/UnicodeData.txt" \
	"$b/%_libdir/icu/current" \
	"$b/%_libdir/icu/Makefile.inc" \
	"$b/%_libdir/icu/pkgdata.inc"

%fdupes %buildroot/%_prefix

%check
# s390x see: https://ssl.icu-project.org/trac/ticket/13095
cd source
if ! ICU_DATA="%buildroot/%_datadir/icu/%aversion" %make_build check VERBOSE=1; then
	# oddly fails since 74
	# did they mess up --with-data-packaging=archive
	:
fi

%ldconfig_scriptlets -n %lname

%files
%_bindir/derb
%_bindir/gen*
%_bindir/icuinfo
%_bindir/makeconv
%_bindir/pkgdata
%_bindir/uconv
%_bindir/icuexportdata
%_sbindir/*
%_mandir/man*/*
%dir %_datadir/icu
%dir %_datadir/icu/%aversion
%_datadir/icu/%aversion/LICENSE
%dir %_docdir/%name/
%_docdir/%name/license.html
%_docdir/%name/readme.html

%files -n %lname
%_libdir/libicu*.so.*

%files -n libicu%sonum-bedata
%dir %_datadir/icu
%dir %_datadir/icu/%aversion
%_datadir/icu/%aversion/icudt%{amajor}b.dat

%files -n libicu%sonum-ledata
%dir %_datadir/icu
%dir %_datadir/icu/%aversion
%_datadir/icu/%aversion/icudt%{amajor}l.dat

%files -n libicu-devel
%_libdir/libicu*.so
%_includedir/unicode/
%dir %_libdir/icu/
%dir %_libdir/icu/%aversion/
%_libdir/icu/%aversion/Makefile.inc
%_libdir/icu/%aversion/pkgdata.inc
%_libdir/pkgconfig/icu-*.pc
%_bindir/icu-config
%dir %_datadir/icu/
%dir %_datadir/icu/%aversion/
%_datadir/icu/%aversion/mkinstalldirs
%_datadir/icu/%aversion/config/

%files -n libicu-doc
%dir %_docdir/%name/
%_docdir/%name/html/

%changelog
