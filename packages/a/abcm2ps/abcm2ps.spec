#
# spec file for package abcm2ps
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2007 by Edgar Aichinger
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


Name:           abcm2ps
Version:        8.14.14
Release:        0
Summary:        A program to typeset abc tunes into Postscript
License:        LGPL-3.0-or-later
Group:          Productivity/Publishing/Other
Summary(de):    Ein Werkzeug um ABC-Notationen in Postscript zu drucken
URL:            https://github.com/leesavide/abcm2ps/
Source0:        https://github.com/leesavide/abcm2ps/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        italian.fmt
Source2:        deco-guitar.fmt
Source3:        deco-marks.fmt
Source4:        renaissance.fmt
Source5:        thinlines.fmt
# PATCH-FIX-OPENSUSE compiler_flags.patch -- aloisio@gmx.com
Patch0:         compiler_flags.patch
BuildRequires:  pkgconfig
# for rst2man
BuildRequires:  python3-docutils
# for rendering non-latin characters in Postscript output
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(pangocairo)

%description
abcm2ps is a package which converts music tunes from ABC format to
PostScript. Based on abc2ps version 1.2.5, it was developed mainly to print
barock organ scores which have independent voices played on one or many
keyboards and a pedal board. abcm2ps introduces many extensions to the ABC
language that make it suitable for classical music.

%prep
%setup -q
%patch0 -p1
mv config.h.in config.h.sed
sed "s/\/\/#define A4_FORMAT/#define A4_FORMAT/" config.h.sed > config.h.in

%build
%configure
make %{?_smp_mflags}

%install
%make_install
# remove documentation and examples from wrong install path
rm -rf %{buildroot}/%{_datadir}/doc

%files
%license COPYING
%doc README.md *.abc sample3.eps
%{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/%{name}*

%changelog
