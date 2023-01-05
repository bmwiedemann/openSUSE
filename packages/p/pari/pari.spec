#
# spec file for package pari
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


%global desc \
PARI/GP is a computer algebra system designed for computations\
in number theory (factorizations, algebraic number theory, elliptic\
curves) and other entities like matrices, polynomials,\
power series, algebraic numbers, and transcendental functions.\
%nil
# See
# http://pari.math.u-bordeaux.fr/archives/pari-dev-1211/msg00006.html
# for details on the SO versioning.
%global sover 8
%global lname   libpari-gmp-tls%sover
Name:           pari
Version:        2.15.2
Release:        0
Summary:        Computer Algebra System for computations in Number Theory
License:        GPL-2.0-only
Group:          Productivity/Scientific/Math
URL:            https://pari.math.u-bordeaux.fr
#Git-Clone:     https://pari.math.u-bordeaux.fr/git/pari.git
#Git-Web:       https://pari.math.u-bordeaux.fr/cgi-bin/gitweb.cgi
Source0:        %url/pub/pari/unix/pari-%version.tar.gz
Source2:        %url/pub/pari/unix/pari-%version.tar.gz.asc
BuildRequires:  fltk-devel
BuildRequires:  gmp-devel
BuildRequires:  pkg-config
BuildRequires:  readline-devel
BuildRequires:  texlive-latex
BuildRequires:  texlive-luatex
BuildRequires:  texlive-luatex-bin
BuildRequires:  texlive-luatexbase
BuildRequires:  texlive-tex-bin
BuildRequires:  xorg-x11-proto-devel
BuildRequires:  pkgconfig(x11)

%description
%desc

%package gp
Summary:        Frontend to the PARI Computer Algebra System
Group:          Productivity/Scientific/Math

%description gp
%desc

%package doc
Summary:        Documentation for the PARI Computer Algebra System
Group:          Documentation/Other
BuildArch:      noarch

%description doc
%desc

This package contains the documentation and examples for the PARI Computer Algebra System.

%package -n %lname
Summary:        Shared library for the PARI Computer Algebra System
# This is used by the data packages to avoid having a too-old version of libpari:
Group:          System/Libraries
Provides:       libpari-gmp = %version

%description -n %lname
%desc

This package contains shared library for the PARI CAS.

%package devel
Summary:        Development files for the PARI Computer Algebra System
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
%desc

This package contains development files for the PARI CAS.

%prep
%autosetup
# Kill __DATE__ from source, it’s pointless and can cause rebuilds.
sed -i -e 's/__DATE__/"today"/' src/language/paricfg.c
# Set proprer page dimensions
sed -i -e '27 i \\\else\\\pagewidth=11.69in\\\pageheight=8.26in' doc/refmacro.tex
# Don’t build DVI docs
sed -i -e 's/^\(doc all:\) .*/\1/' config/DOC_Make.SH

%build
./Configure \
	--prefix="%_prefix" \
	--bindir="%_bindir" \
	--includedir="%_includedir" \
	--libdir="%_libdir" \
	--sysdatadir="%_libdir" \
	--datadir="%_datadir/%name" \
	--mt=pthread
%make_build \
	CFLAGS="%optflags -fno-strict-aliasing" \
	STRIP=true \
	all
%make_build \
	PDFTEX=luatex \
	PDFLATEX=lualatex \
	docpdf

%install
%make_install
install -dm0755 %buildroot%_sysconfdir
install -m0644 misc/gprc.dft %buildroot%_sysconfdir/gprc

install -dm0755 %buildroot%_defaultdocdir/%name
install -Dm0644 doc/*.pdf %buildroot%_defaultdocdir/%name
rm -rf %buildroot%_datadir/%name/doc
mv %buildroot%_datadir/%name/examples %buildroot%_defaultdocdir/%name

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files gp
%doc AUTHORS CHANGES* README* NEW
%config %_sysconfdir/gprc
%_bindir/*
%_datadir/%name
%_libdir/%name.cfg
%_mandir/*/*.1%{?ext_man}

%files doc
%_defaultdocdir/%name/

%files -n %lname
%license COPYING
%_libdir/libpari-gmp-tls.so.%version
%_libdir/libpari-gmp-tls.so.%sover

%files devel
%_includedir/%name/
%_libdir/libpari.so

%changelog
