#
# spec file for package lcdf-typetools
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Summary:        Programs to manipulate OpenType and multiple-master fonts

Name:           lcdf-typetools
Version:        2.106
Release:        0
License:        GPL-2.0
Url:            http://www.lcdf.org/type/
Group:          System/X11/Fonts
Source:         http://www.lcdf.org/type/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  gcc-c++
BuildRequires:  libstdc++-devel
BuildRequires:  texlive

%description
This package contains four tools for working with OpenType fonts:

 cfftot1    allows you to translate Compact Font Format (CFF) or
            PostScript-flavored OpenType fonts into PostScript
            Type 1 font format

 otfinfo    reports information about OpenType fonts, such as the
            features they support and the contents of their ``size''
            optical size option

 otftotfm   allows you to create TeX font metrics and encodings for
            using OpenType fonts

 t1dotlessj creates a Type 1 font with a single character --
            the dotless j corresponding to the specified design

 t1lint     checks a Type 1 font for correctness (preliminary)

 t1reencode reencodes a Type 1 font, replacing its internal encoding with
            one you specify

 t1testpage creates a PostScript test page for a specified
            font file (preliminary)

The package now includes programs for working with multiple-master
fonts formerly distributed as mminstance.  These tools allow you to
use multiple-master fonts with programs that require single-master
fonts (afm2tfm, ps2pk, fontinst, etc.).  Both programs work fine with
fonts that contain intermediate masters (e.g., Adobe Jenson MM and
Adobe Kepler MM).

mmafm        creates an AFM (Adobe font metric) file corresponding to
             a single instance of a multiple-master font.  It reads
             (and therefore requires) the AMFM and AFM files
             distributed with the font.

mmpfb        creates a normal, single-master font program that looks
             like an instance of a multiple-master font.  It reads
             the multiple-master font program in PFA or PFB format.

%prep
%setup -q

%build
%configure \
--without-kpathsea \
--disable-selfauto-set \

make %{?_smp_mflags}

%install
%makeinstall

%files
%defattr(-,root,root)
%{_bindir}/cfftot1
%{_bindir}/mmafm
%{_bindir}/mmpfb
%{_bindir}/otfinfo
%{_bindir}/otftotfm
%{_bindir}/t1dotlessj
%{_bindir}/t1lint
%{_bindir}/t1reencode
%{_bindir}/t1testpage
%{_bindir}/ttftotype42
%{_bindir}/t1rawafm

%{_mandir}/man*/*
%{_datadir}/lcdf-typetools/

%changelog
