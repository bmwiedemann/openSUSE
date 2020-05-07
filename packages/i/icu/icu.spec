#
# spec file for package icu
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


%define lname	libicu67
%define amajor   67
%define aversion 67
%ifarch %armb hppa mips mips64 ppc ppc64 %sparc s390 s390x m68k
%define be_platform 1
%else
%define be_platform 0
%endif
# icu-versioning.diff needs update for new Version too
Name:           icu
Version:        67.1
Release:        0
Summary:        International Components for Unicode
License:        ICU
Group:          Development/Libraries/C and C++
URL:            http://icu-project.org/

#Git-Clone:	https://github.com/unicode-org/icu.git
Source:         https://github.com/unicode-org/icu/releases/download/release-67-1/icu4c-67_1-src.tgz
Source2:        https://github.com/unicode-org/icu/releases/download/release-67-1/icu4c-67_1-src.tgz.asc
Source3:        https://github.com/unicode-org/icu/releases/download/release-67-1/icu4c-67_1-docs.zip
Source4:        https://github.com/unicode-org/icu/releases/download/release-67-1/icu4c-67_1-docs.zip.asc
Source5:        %name.keyring
Source100:      baselibs.conf
Patch4:         icu-fix-install-mode-files.diff
Patch6:         icu-error-reporting.diff
Patch7:         icu-avoid-x87-excess-precision.diff
Patch8:         locale.diff
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkg-config
BuildRequires:  python3-base
BuildRequires:  unzip
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
ICU is a set of C and C++ libraries that provide extensive Unicode and locale
support, such as calendar, conversions for many character sets, language
sensitive collation, date and time formatting, support for many locales,
message catalogs and resources, message formatting, normalization, number and
currency formatting, time zone support, transliteration, and word, line, and
sentence breaking.
/
This subpackage contains the runtime programs for interacting with ICU.

%package -n %lname
Summary:        International Components for Unicode
Group:          System/Libraries
Requires:       timezone
%if %be_platform
Requires:       libicu%aversion-bedata = %version
%else
Requires:       libicu%aversion-ledata = %version
%endif

%description -n %lname
ICU is a set of C and C++ libraries that provide extensive Unicode
and locale support.
This package contains the runtime libraries for ICU.

%package -n libicu%aversion-bedata
Summary:        Rule databases and tables for ICU
Group:          System/Libraries
%if 0%{?suse_version} >= 1210
BuildArch:      noarch
%endif

%description -n libicu%aversion-bedata
ICU is a set of C and C++ libraries that provide extensive Unicode
and locale support.

ICU makes use of a wide variety of data tables to provide many of its
services: converter mapping tables, collation rules, transliteration
rules, break iterator rules and dictionaries.

This subpackage contains these data tables, in big-endian format.

%package -n libicu%aversion-ledata
Summary:        Rule databases and tables for ICU
Group:          System/Libraries
%if 0%{?suse_version} >= 1210
BuildArch:      noarch
%endif

%description -n libicu%aversion-ledata
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
%setup -qn icu
%autopatch -p1
# docs are special
mkdir html
pushd html/
unzip %SOURCE3
popd

%build
cd source
mkdir -p data/out/tmp # build procedure forgets to do this on its own
export CXXFLAGS="%optflags -DICU_DATA_DIR=\\\"%_datadir/icu/%version/\\\""
export CFLAGS="$CXXFLAGS"
%configure \
	--disable-static \
	--enable-shared \
	--disable-samples \
	--with-data-packaging=archive
make %{?_smp_mflags} VERBOSE=1
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
mkdir -p "%buildroot/%_docdir/%name"
cp -a html "%buildroot/%_docdir/%name/"
cp -a license.html readme.html "%buildroot/%_docdir/%name/"

find . -name CVS -type d -exec rm -Rf "{}" "+"
cd source

make DESTDIR="%buildroot" install %{?_smp_mflags}
cp data/out/icudt*.dat "%buildroot/%_datadir/icu/%version/"

#
# ICU's "pkgdata" utility is really fragile, so icu-versioning.diff
# does as few actions as possible, but that means we need some additional
# cleanup in the spec file now.
#
pushd "%buildroot/%_libdir/"
for i in *.so.[0-9]*; do
	echo "Looking at $i"
	if [ "${i##*.so.}" != "%version" ]; then
		rm -fv "$i"
		continue
	fi
	# Because U_ICU_VERSION_SHORT is "51_2" and not "51.2",
	# create some symlinks.
	ln -s "$i" "${i%%%version}%aversion"
done
popd

# /usr/lib/rpm/elfdeps requires +x bit and not all files had it at one point.
# - OpenBSD for example is known to have patched their libtool program
# to kill the x bit on install :(
chmod a+rx "%buildroot/%_libdir"/lib*.so.*

# install uncompiled source data:
mkdir -p "%buildroot/%_datadir/icu/%version/unidata"
install -m 644 data/unidata/*.txt "%buildroot/%_datadir/icu/%version/unidata"
ln -s unidata/UnicodeData.txt "%buildroot/%_datadir/icu/%version/"

rm "%buildroot/%_datadir/icu/%version/install-sh"
# Seems unused
rm -Rf "%buildroot/%_datadir/icu/%version/unidata/" \
	"%buildroot/%_datadir/icu/%version/UnicodeData.txt" \
	"%buildroot/%_libdir/icu/current" \
	"%buildroot/%_libdir/icu/Makefile.inc" \
	"%buildroot/%_libdir/icu/pkgdata.inc"

%fdupes %buildroot/%_prefix

%check
# s390x see: https://ssl.icu-project.org/trac/ticket/13095
cd source
%if !0%{?qemu_user_space_build:1}
# Checks disabled in qemu because of races happening when we emulate
# multi-threaded programs, and some check tests atomic instructions in
# multi-threaded icu invocations
ICU_DATA="%buildroot/%_datadir/icu/%version" make check %{?_smp_mflags} VERBOSE=1
%endif

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files
%defattr(-,root,root)
%_bindir/derb
%_bindir/gen*
%_bindir/icuinfo
%_bindir/makeconv
%_bindir/pkgdata
%_bindir/uconv
%_sbindir/*
%_mandir/man*/*
%dir %_datadir/icu
%dir %_datadir/icu/%version
%_datadir/icu/%version/LICENSE
%dir %_docdir/%name/
%_docdir/%name/license.html
%_docdir/%name/readme.html

%files -n %lname
%defattr(-, root, root)
%_libdir/libicu*.so.*

%files -n libicu%aversion-bedata
%defattr(-,root,root)
%dir %_datadir/icu
%dir %_datadir/icu/%version
%_datadir/icu/%version/icudt%{amajor}b.dat

%files -n libicu%aversion-ledata
%defattr(-,root,root)
%dir %_datadir/icu
%dir %_datadir/icu/%version
%_datadir/icu/%version/icudt%{amajor}l.dat

%files -n libicu-devel
%defattr(-, root, root)
%_libdir/libicu*.so
%_includedir/unicode/
%dir %_libdir/icu/
%dir %_libdir/icu/%version/
%_libdir/icu/%version/Makefile.inc
%_libdir/icu/%version/pkgdata.inc
%_libdir/pkgconfig/icu-*.pc
%_bindir/icu-config
%dir %_datadir/icu/
%dir %_datadir/icu/%version/
%_datadir/icu/%version/mkinstalldirs
%_datadir/icu/%version/config/

%files -n libicu-doc
%defattr(-,root,root)
%dir %_docdir/%name/
%_docdir/%name/html/

%changelog
