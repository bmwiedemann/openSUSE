#
# spec file for package gnucobol
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


%define         _lto_cflags      %{nil}
%define sover   4
%define _mver   3.2
Name:           gnucobol
Version:        3.2
Release:        0
Summary:        A COBOL compiler
License:        GPL-3.0-or-later AND LGPL-3.0-or-later
Group:          Development/Languages/Other
URL:            https://www.gnu.org/software/gnucobol/
Source0:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz
Source1:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz.sig
Source2:        https://ftp.gnu.org/gnu/gnu-keyring.gpg#/%{name}.keyring
Source3:        https://sourceforge.net/projects/%{name}/files/contrib/esql/%{name}-sql-3.0.tar.gz
Source4:        https://gnucobol.sourceforge.io/files/newcob.val.tar.gz
# PATCH-FIX-UPSTREAM gnucobol-3.1.2-C99.diff -- Missing include which causes compilation errors with GCC 14
Patch1:         gnucobol-3.1.2-C99.diff
# PATCH-FIX-UPSTREAM move_packed_decimal.patch -- see https://sourceforge.net/p/gnucobol/bugs/904/
Patch2:         move_packed_decimal.patch
# PATCH-FIX-UPSTREAM patch-errno.patch  -- see https://git.adelielinux.org/adelie/packages/-/issues/1045#note_13472
Patch3:         fix-errno.patch
BuildRequires:  autoconf
BuildRequires:  db-devel
BuildRequires:  dos2unix
BuildRequires:  gmp-devel
BuildRequires:  gpg2
BuildRequires:  help2man
BuildRequires:  makeinfo
BuildRequires:  pkgconfig(json-c) >= 0.12
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(ncurses) >= 5.4
# esql
BuildRequires:  unixODBC-devel
BuildRequires:  gcc-c++
Requires:       gcc
Requires(post): %{install_info_prereq}
Requires(preun): %{install_info_prereq}
Provides:       gnu-cobol = %{version}
Provides:       libcob-devel = %{version}-%{release}
Provides:       opencobol = %{version}
Obsoletes:      gnu-cobol < %{version}
Obsoletes:      libcob-devel < %{version}-%{release}

%description
GnuCOBOL is a COBOL compiler which implements a substantial part of
the COBOL 85, COBOL 2002 and COBOL 2014 standards, as well as many
extensions included in other COBOL compilers.

GnuCOBOL translates COBOL into C and compiles the translated code
using a native C compiler. cobc translates COBOL to executable using
intermediate C sources, providing full access to nearly all C
libraries.

%package -n libcob%{sover}
Summary:        GnuCOBOL shared library
License:        LGPL-3.0-or-later
Group:          Development/Languages/Other

%description -n libcob%{sover}
GnuCOBOL (formerly OpenCOBOL) is a COBOL compiler.
cobc translates COBOL to executable using intermediate C sources,
providing full access to nearly all C libraries.

%package -n esql
Summary:        ESQL for GnuCOBOL
License:        GPL-3.0-or-later AND LGPL-3.0-or-later

%description -n esql
Provides the possibility to use Cobol code in combination with databases.

%package -n esql-devel
Summary:        Devel package for ESQL
License:        GPL-3.0-or-later AND LGPL-3.0-or-later
Requires:       unixODBC

%description -n esql-devel
ESQL Devel package for GnuCOBOL

%prep
%autosetup -p1 -n %{name}-%{version}
cp %{SOURCE4} tests/cobol85/

%build
CFLAGS="%{optflags} -Wno-error=incompatible-pointer-types"
%if 0%{?suse_version} > 1600
CFLAGS="$CFLAGS -std=gnu17"
%endif
export CFLAGS
%configure \
        --with-db \
        --with-xml2 \
        --with-curses=ncursesw \
        --with-json=json-c \
        --enable-hardening \
        --enable-static=no
%make_build

tar -xzvf %{SOURCE3}
cd gnucobol-sql-3.0/
%configure --enable-static=no
%make_build
cd -

%install
%make_install

cd gnucobol-sql-3.0/
%make_install
cd -

find %{buildroot} -type f -name "*.la" -delete -print
%find_lang gnucobol

%check
(make check CFLAGS="%optflags -O" || make check TESTSUITEFLAGS="--recheck --verbose" || echo "Warning, unexpected results")
make -j4 test

%post
%install_info --info-dir=%{_infodir} %{_infodir}/gnucobol.info.gz

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/gnucobol.info.gz

%ldconfig_scriptlets -n libcob%{sover}
%ldconfig_scriptlets -n esql

%files -f gnucobol.lang
%license COPYING COPYING.DOC
%doc ABOUT-NLS AUTHORS ChangeLog NEWS README THANKS TODO HACKING DEPENDENCIES.md
%{_bindir}/cob-config
%{_bindir}/cobc
%{_bindir}/cobcrun
%{_datadir}/gnucobol
%{_infodir}/gnucobol.info%{?ext_info}
%{_libdir}/libcob.so
%dir %{_libdir}/gnucobol/
%{_libdir}/gnucobol/CBL_OC_DUMP.so
%{_includedir}/libcob.h
%dir %{_includedir}/libcob
%{_includedir}/libcob/cobgetopt.h
%{_includedir}/libcob/common.h
%{_includedir}/libcob/exception-io.def
%{_includedir}/libcob/exception.def
%{_includedir}/libcob/statement.def
%{_includedir}/libcob/version.h
%{_mandir}/man1/cob-config.1%{ext_info}
%{_mandir}/man1/cobc.1%{ext_info}
%{_mandir}/man1/cobcrun.1%{ext_info}

%files -n libcob%{sover}
%license COPYING.LESSER
%{_libdir}/libcob.so.%{sover}*

%files -n esql
%license COPYING COPYING.LESSER
%doc README AUTHORS NEWS ChangeLog
%{_bindir}/esqlOC
%{_libdir}/libocsql.so.2*

%files -n esql-devel
%{_libdir}/libocsql.so

%changelog
