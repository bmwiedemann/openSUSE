#
# spec file for package cedilla
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           cedilla
Version:        0.7
Release:        0
Summary:        A Best-Effort Text Printer (Works in UTF-8 and Can Replace a2ps)
License:        GPL-2.0+
Group:          Productivity/Publishing/PS
Url:            http://www.pps.jussieu.fr/~jch/software/cedilla/
Source0:        http://www.pps.jussieu.fr/~jch/software/files/%{name}-%{version}.tar.gz
Source1:        cedilla-pipe
Patch0:         cedilla-destdir.patch
# PATCH-FIX-UPSTREAM marguerite@opensuse.org - fix font path in config.lisp
Patch1:         cedilla-0.7-resources-path.patch
BuildRequires:  clisp
Requires:       clisp
Requires:       ghostscript-fonts-std
Requires:       texlive
Requires:       xorg-x11-fonts
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
ExcludeArch:    ppc64 ppc64le

%description
Cedilla is a "best-effort" text printer that uses Unicode internally.

Using Unicode means that the set of characters that can appear in the
input is very large and the user may very well have no font available
that contains glyphs for the characters that the user wants to print.
Cedilla attempts to at least partially solve this problem using a
number of techniques:

1. Cedilla can use an arbitrary number of downloadable fonts. For
   any given print job, only the necessary fonts are downloaded.

2. Cedilla uses its own built-in font, which contains a number of
   useful glyphs that are missing from standard fonts.

3. Cedilla modifies existing glyphs in order to, for example, remove
   dots or add bars.

4. Cedilla attempts to build composite glyphs (for accented
   characters, for example) on the fly.

5. Cedilla uses fallbacks for characters that are not supported by the
   available fonts.

%prep
%setup -q
%patch0 -p 1 -b .destdir
%patch1 -p1

%build
./compile-cedilla

%install
TARGET=%{buildroot} ./install-cedilla
install -m 755 $RPM_SOURCE_DIR/cedilla-pipe %{buildroot}%{_bindir}/

%files
%defattr(-, root,root)
%doc COPYING NEWS README* vietnamese-sample.text
%config %{_sysconfdir}/*
%{_bindir}/*
%{_prefix}/lib/cedilla/
%{_mandir}/man1/*

%changelog
