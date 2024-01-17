#
# spec file for package mftrace
#
# Copyright (c) 2022 SUSE LLC
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


Name:           mftrace
Version:        1.2.20
Release:        0
Summary:        Scalable PostScript Fonts for MetaFont
License:        GPL-2.0-only
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://lilypond.org/mftrace/
Source0:        https://lilypond.org/download/sources/mftrace/%{name}-%{version}.tar.gz
Source1:        gf2pbm.1
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  potrace
Requires:       bitmap_tracing
Requires:       fontforge
Requires:       t1utils
Requires:       texlive
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Mftrace is a small Python program that lets you trace a TeX bitmap font
into a PFA or PFB font (A PostScript Type1 Scalable Font) or TTF
(TrueType) font.

%prep
%setup -q

%build
cp %{SOURCE1} .
autoreconf -fi
%configure \
	--with-pic
make CFLAGS="$RPM_OPT_FLAGS" %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
# remove files containing hardcoded rpath
rm -rf %{buildroot}%{_datadir}/mftrace/*.pyc

%files
%defattr(-, root, root)
%license COPYING
%doc ChangeLog README.txt
%{_bindir}/*
%{_datadir}/mftrace
%{_mandir}/man1/*

%changelog
