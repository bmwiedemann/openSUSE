#
# spec file for package hunspell
#
# Copyright (c) 2023 SUSE LLC
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


%define ver     1.7
%define libname lib%{name}-1_7-0
Name:           hunspell
Version:        1.7.2
Release:        0
Summary:        A spell checker and morphological analyzer library
License:        (GPL-2.0-or-later OR LGPL-2.1-or-later OR MPL-1.1+) AND LGPL-2.1-or-later
Group:          Productivity/Office/Other
URL:            https://hunspell.github.io
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  gcc-c++
BuildRequires:  libstdc++-devel
BuildRequires:  libtool
BuildRequires:  ncurses-devel >= 5.0
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
Recommends:     %{name}-tools
Recommends:     unzip
# bsc#1193627
Requires:       myspell-en_US

%description
Hunspell is a spell checker and morphological analyzer library and
program designed for languages with rich morphology and complex word
compounding or character encoding. Hunspell interfaces: Ispell-like
terminal interface using Curses library, Ispell pipe interface,
LibreOffice or OpenOffice.org UNO module.

%package -n %{libname}
Summary:        A spell checker and morphological analyzer library
# same libname, support migration
Group:          System/Libraries
Conflicts:      hunspell = 1.4.0

%description -n %{libname}
Hunspell is a spell checker and morphological analyzer library and
program designed for languages with rich morphology and complex word
compounding or character encoding. Hunspell interfaces: Ispell-like
terminal interface using Curses library, Ispell pipe interface,
LibreOffice or OpenOffice.org UNO module.

This package contains the shared library.

%package tools
Summary:        Hunspell tools
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}

%description tools
This package contains the munch and unmunch programs.

%package devel
Summary:        Files for developing with hunspell
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}-%{release}
Requires:       libstdc++-devel

%description devel
Includes and definitions for developing with hunspell.

%prep
%setup -q

%build
# latest released tarball does not contain generated configure
autoreconf -fiv
%configure \
	--disable-silent-rules \
	--enable-nls \
	--disable-static \
	--disable-rpath \
	--with-ui \
	--with-readline
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
rm -f %{buildroot}%{_bindir}/example
install -p -m 644 src/tools/{,un}munch.h %{buildroot}%{_includedir}
ln -sf %{_libdir}/libhunspell-%{ver}.so.0.0.1 %{buildroot}%{_libdir}/libhunspell.so

%check
make check %{?_smp_mflags}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files
%license COPYING license.hunspell license.myspell
%doc README README.md AUTHORS THANKS
%attr(755,root,root) %{_bindir}/hunspell
%dir %{_mandir}/hu
%dir %{_mandir}/hu/man1
%{_mandir}/man1/hunspell.1%{?ext_man}
%lang(hu) %{_mandir}/hu/man1/hunspell.1*

%files -n %{libname}
%{_libdir}/libhunspell-%{ver}.so.*

%files tools
%{_bindir}/analyze
%{_bindir}/chmorph
%{_bindir}/munch
%{_bindir}/unmunch
%{_bindir}/hunzip
%{_bindir}/hzip
%{_bindir}/affixcompress
%{_bindir}/ispellaff2myspell
%{_bindir}/makealias
%{_bindir}/wordforms
%{_bindir}/wordlist2hunspell
%{_mandir}/man1/hunzip.1%{?ext_man}
%{_mandir}/man1/hzip.1%{?ext_man}

%files devel
%{_libdir}/libhunspell-%{ver}.so
%{_libdir}/libhunspell.so
%{_mandir}/man3/hunspell.3%{?ext_man}
%{_mandir}/man5/hunspell.5%{?ext_man}
%{_includedir}/%{name}
%{_includedir}/munch.h
%{_includedir}/unmunch.h
%{_libdir}/pkgconfig/hunspell.pc

%changelog
