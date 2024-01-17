#
# spec file for package ghostscript-fonts-grops
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


Name:           ghostscript-fonts-grops
Version:        1.22.2
Release:        0
Summary:        Ghostscript fonts imported to groff for use with grops
License:        GPL-2.0-only
Group:          Productivity/Publishing/Troff
URL:            https://www.gnu.org/software/groff/groff.html
Source:         gsalias.txt
Source1:        zzz-groff-gs.sh
Source2:        zzz-groff-gs.csh
# In version 9.26, the ghostscript package doesn't provide a COPYING file
# anymore. So providing it:
Source3:        COPYING
BuildRequires:  fontforge
BuildRequires:  ghostscript
BuildRequires:  groff-full
%requires_eq    groff
Provides:       locale(groff:pl)
BuildArch:      noarch
%if 0%{?suse_version} > 1320
BuildRequires:  ghostscript-fonts-std
%endif

%description
A version of PostScript® driver for Groff to support characters outside ISO Latin 1 character set.

%prep

%build
%define gs_fonts %{_datadir}/ghostscript/fonts
%define gs_version %(gs --version)
%if %{lua:print(rpm.vercmp(rpm.expand("%{gs_version}"), "9.50"))} >= 0
%define import_font() ln -s -T "%{gs_fonts}/%{1}.afm" "%{2}.afm" && gs -P- -dNOSAFER -dNODISPLAY -- pfbtopfa.ps %{gs_fonts}/%{1}.pfb devps/%{1}.pfa
%else
%define import_font() ln -s -T "%{gs_fonts}/%{1}.afm" "%{2}.afm" && pfbtopfa %{gs_fonts}/%{1}.pfb devps/%{1}.pfa
%endif
%define gs_docdir %(if [ -d "%{_datadir}/ghostscript/%{gs_version}/doc" ] ; then echo "%{_datadir}/ghostscript/%{gs_version}/doc" ; else echo "%{_datadir}/doc/ghostscript/%{gs_version}"; fi)
cp %{SOURCE3} .
mkdir devps
while read fn fa
# Grops font generator expects conventional font file names;
# the substitutes provided by ghostscript must be linked accordingly.
# The link is needed only at build time.
# Ghostscript substitutes stripped fonts, full fonts must be embedded in the printout.
# Groff only knows how to embed PFA fonts.
do %{import_font $fn $fa}
done < '%{SOURCE0}'
cd devps
#ln -s -t. '%{_datadir}/groff/current/font/devps/generate'
mkdir output
mkdir generate
cp -r %{_datadir}/groff/current/font/devps/generate/* ./generate
cp %{_datadir}/groff/current/font/devps/DESC .
cp %{_datadir}/groff/current/font/devps/text.enc .
cp %{_datadir}/groff/current/font/devps/symbolsl.ps .
cp ./generate/zapfdr.sed ./generate/apfdr.sed
if [ -f %{_datadir}/groff/current/font/devps/symbolsl.afm ]; then
cp %{_datadir}/groff/current/font/devps/symbolsl.afm output/
cp %{_datadir}/groff/current/font/devps/zapfdr.afm output/
fi
cp %{_datadir}/groff/current/font/devps/freeeuro.afm .
ln -sf output/symbol.afm .
make -fgenerate/Makefile afmdir=.. \
  OUTDIR=output
if [ -h symbol.afm ]; then
  rm symbol.afm
  for f in output/* ; do
    cp ${f} .
  done
fi
rm -rf output
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
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
install -c -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/profile.d
install -c -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/profile.d

%files
%license COPYING
%{_datadir}/*
%config %{_sysconfdir}/profile.d/*

%changelog
