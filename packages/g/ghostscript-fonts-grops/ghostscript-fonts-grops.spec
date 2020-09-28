#
# spec file for package ghostscript-fonts-grops
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           ghostscript-fonts-grops
Version:        1.22.2
Release:        0
Url:            http://www.gnu.org/software/groff/groff.html
Summary:        Ghostscript fonts imported to groff for use with grops
License:        GPL-2.0-only
Group:          Productivity/Publishing/Troff
Provides:       locale(groff:pl)
Source:         gsalias.txt
Source1:        zzz-groff-gs.sh
Source2:        zzz-groff-gs.csh
# In version 9.26, the ghostscript package doesn't provide a COPYING file
# anymore. So providing it:
Source3:        COPYING
BuildArch:      noarch
BuildRequires:  fontforge
BuildRequires:  ghostscript
%if 0%{?suse_version} > 1320
BuildRequires:  ghostscript-fonts-std
%endif
BuildRequires:  groff-full
%requires_eq    groff

%description
A version of PostScript® driver for Groff to support characters outside ISO Latin 1 character set.

%prep

%build
%define gs_fonts %{_datadir}/ghostscript/fonts
%define gs_version %(gs --version)
%define gs_ver %(gs --version | sed "s/\\.//")
%if %{gs_ver} >= 950
%define import_font() ln -s -T "%{gs_fonts}/%1.afm" "%2.afm" && gs -P- -dNOSAFER -dNODISPLAY -- pfbtopfa.ps %{gs_fonts}/%1.pfb devps/%1.pfa
%else
%define import_font() ln -s -T "%{gs_fonts}/%1.afm" "%2.afm" && pfbtopfa %{gs_fonts}/%1.pfb devps/%1.pfa
%endif
%define gs_docdir %(if [ -d "%{_datadir}/ghostscript/%{gs_version}/doc" ] ; then echo "%{_datadir}/ghostscript/%{gs_version}/doc" ; else echo "%{_datadir}/doc/ghostscript/%{gs_version}"; fi)
cp %{S:3} .
mkdir devps
while read fn fa
# Grops font generator expects conventional font file names; 
# the substitutes provided by ghostscript must be linked accordingly.
# The link is needed only at build time.
# Ghostscript substitutes stripped fonts, full fonts must be embedded in the printout.
# Groff only knows how to embed PFA fonts.
do %{import_font $fn $fa}
done < '%{S:0}'
cd devps
ln -s -t. '%{_datadir}/groff/current/font/devps/generate'
make -fgenerate/Makefile afmdir=..
# Register fonts to be embedded
cd ..
for f in *.afm
do pf="$(readlink "${f}")"
pf="${pf##*/}"
pf="${pf:0:-4}.pfa" 
read<"devps/${pf}" decl fn ver
echo "${fn}" "${pf}"
done >>devps/download

%install
%define groff_version %(groff -v | head -n 1 | sed 's/.*\s//')
target="%{buildroot}%{_datadir}/groff/%{groff_version}/font/gs"
install -d "${target}"
mv "-t${target}" devps
mkdir -p %{buildroot}/etc/profile.d
install -c -m 0644 %{S:1} %{buildroot}/etc/profile.d
install -c -m 0644 %{S:2} %{buildroot}/etc/profile.d

%files
%defattr(-,root,root)
%doc COPYING
%{_datadir}/*
%config /etc/profile.d/*

%changelog
