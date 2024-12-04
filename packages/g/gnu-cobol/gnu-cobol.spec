#
# spec file for package gnu-cobol
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


%define         _lto_cflags      %{nil}
%define sover   4
%define _mver   3.1
Name:           gnu-cobol
Version:        3.1.2
Release:        0
Summary:        A COBOL compiler
License:        GPL-3.0-or-later AND LGPL-3.0-or-later
Group:          Development/Languages/Other
URL:            https://savannah.gnu.org/projects/gnucobol
Source0:        https://sourceforge.net/projects/open-cobol/files/gnu-cobol/%{_mver}/gnucobol-%{version}.tar.xz
Source1:        https://sourceforge.net/projects/open-cobol/files/gnu-cobol/%{_mver}/gnucobol-%{version}.tar.xz.sig
# PATCH-FIX-UPSTREAM fix_test_698.patch -- see https://sourceforge.net/p/gnucobol/bugs/695/
Patch1:         fix_test_698.patch
# PATCH-FIX-UPSTREAM gnucobol-3.1.2-C99.diff -- Missing include which causes compilation errors with GCC 14
Patch2:         gnucobol-3.1.2-C99.diff
BuildRequires:  autoconf
BuildRequires:  db-devel
BuildRequires:  dos2unix
BuildRequires:  gmp-devel
BuildRequires:  help2man
BuildRequires:  makeinfo
BuildRequires:  pkgconfig(json-c) >= 0.12
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(ncurses) >= 5.4
Requires(post): %{install_info_prereq}
Requires(preun): %{install_info_prereq}
Provides:       libcob-devel = %{version}
Provides:       opencobol = %{version}
Obsoletes:      libcob-devel <= 3.1.2

%description
GnuCOBOL (formerly OpenCOBOL) is a COBOL compiler.
cobc translates COBOL to executable using intermediate C sources,
providing full access to nearly all C libraries.

%package -n libcob%{sover}
Summary:        GnuCOBOL shared library
License:        LGPL-3.0-or-later
Group:          Development/Languages/Other

%description -n libcob%{sover}
GnuCOBOL (formerly OpenCOBOL) is a COBOL compiler.
cobc translates COBOL to executable using intermediate C sources,
providing full access to nearly all C libraries.

%prep
%autosetup -p1 -n gnucobol-%{version}

%build

%global optflags %{optflags} -Wno-error=incompatible-pointer-types
%configure \
        --enable-hardening \
        --enable-static=no
%make_build

%install
%make_install
%find_lang gnucobol
find %{buildroot} -type f -name "*.la" -delete -print

%check
%make_build check

%post
%install_info --info-dir=%{_infodir} %{_infodir}/gnucobol.info.gz

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/gnucobol.info.gz

%post -n libcob%{sover} -p /sbin/ldconfig
%postun -n libcob%{sover} -p /sbin/ldconfig

%files -f gnucobol.lang
%license COPYING COPYING.DOC
%doc ABOUT-NLS AUTHORS ChangeLog NEWS README THANKS TODO
%{_bindir}/cob-config
%{_bindir}/cobc
%{_bindir}/cobcrun
%{_datadir}/gnucobol
%{_infodir}/gnucobol.info%{?ext_info}
%{_libdir}/gnucobol
%{_libdir}/libcob.so
%{_includedir}/libcob.h
%{_includedir}/libcob
%{_mandir}/man1/cob-config.1%{ext_info}
%{_mandir}/man1/cobc.1%{ext_info}
%{_mandir}/man1/cobcrun.1%{ext_info}

%files -n libcob%{sover}
%license COPYING.LESSER
%{_libdir}/libcob.so.%{sover}*

%changelog
