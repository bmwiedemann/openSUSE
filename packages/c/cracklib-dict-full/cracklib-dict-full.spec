#
# spec file for package cracklib-dict-full
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           cracklib-dict-full
BuildRequires:  cracklib
BuildRequires:  gzip
Url:            http://sourceforge.net/projects/cracklib
Version:        2.8.12
Release:        0
Provides:       cracklib-dict
Provides:       cracklib:/usr/share/cracklib/pw_dict.pwd
Conflicts:      cracklib-dict-small
Summary:        A Password-Checking Library
License:        LGPL-2.1-only
Group:          System/Libraries
Source1:        http://prdownloads.sourceforge.net/cracklib/cracklib-words-20080507.gz
Source10:       ftp://ftp.cerias.purdue.edu/pub/dict/wordlists/computer/Domains.gz
Source11:       ftp://ftp.cerias.purdue.edu/pub/dict/wordlists/computer/Dosref.gz
Source12:       ftp://ftp.cerias.purdue.edu/pub/dict/wordlists/computer/Ftpsites.gz
Source13:       ftp://ftp.cerias.purdue.edu/pub/dict/wordlists/computer/Jargon.gz
Source14:       ftp://ftp.cerias.purdue.edu/pub/dict/wordlists/computer/common-passwords.txt.gz
Source15:       ftp://ftp.cerias.purdue.edu/pub/dict/wordlists/computer/etc-hosts.gz
Source16:       ftp://ftp.cerias.purdue.edu/pub/dict/wordlists/movieTV/Movies.gz
Source17:       ftp://ftp.cerias.purdue.edu/pub/dict/wordlists/movieTV/Python.gz
Source18:       ftp://ftp.cerias.purdue.edu/pub/dict/wordlists/movieTV/Trek.gz
Source19:       ftp://ftp.cerias.purdue.edu/pub/dict/wordlists/literature/LCarrol.gz
Source20:       ftp://ftp.cerias.purdue.edu/pub/dict/wordlists/literature/Paradise.Lost.gz
Source21:       ftp://ftp.cerias.purdue.edu/pub/dict/wordlists/literature/cartoon.gz
Source22:       ftp://ftp.cerias.purdue.edu/pub/dict/wordlists/literature/myths-legends.gz
Source23:       ftp://ftp.cerias.purdue.edu/pub/dict/wordlists/literature/sf.gz
Source24:       ftp://ftp.cerias.purdue.edu/pub/dict/wordlists/literature/shakespeare.gz
Source25:       ftp://ftp.cerias.purdue.edu/pub/dict/wordlists/names/ASSurnames.gz
Source26:       ftp://ftp.cerias.purdue.edu/pub/dict/wordlists/names/Congress.gz
Source27:       ftp://ftp.cerias.purdue.edu/pub/dict/wordlists/names/Family-Names.gz
Source28:       ftp://ftp.cerias.purdue.edu/pub/dict/wordlists/names/Given-Names.gz
Source29:       ftp://ftp.cerias.purdue.edu/pub/dict/wordlists/names/famous.gz
Source30:       ftp://ftp.cerias.purdue.edu/pub/dict/wordlists/names/fast-names.gz
Source31:       ftp://ftp.cerias.purdue.edu/pub/dict/wordlists/names/female-names.gz
Source32:       ftp://ftp.cerias.purdue.edu/pub/dict/wordlists/names/male-names.gz
Source33:       ftp://ftp.cerias.purdue.edu/pub/dict/wordlists/names/names.french.gz
Source34:       ftp://ftp.cerias.purdue.edu/pub/dict/wordlists/names/names.hp.gz
Source35:       ftp://ftp.cerias.purdue.edu/pub/dict/wordlists/names/other-names.gz
Source36:       ftp://ftp.cerias.purdue.edu/pub/dict/wordlists/names/surnames.finnish.gz
Source37:       pt_BR-wordlist.gz
Source38:       es-wordlist.gz
Source39:       ftp://ftp.cerias.purdue.edu/pub/dict/wordlists/german/germanl.gz
Source40:       ftp://ftp.cerias.purdue.edu/pub/dict/wordlists/german/words.german.gz
Source41:       john.gz
Source42:       cain.gz
Source43:       500-worst-passwords.gz
Source44:       twitter-banned.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
# don't build as noarch for now
# probably little/big-endian dependent (x86 and x86_64 are the same)
# need to investigate further
# BuildArch:      noarch

%description
CrackLib tests passwords to determine whether they match certain
security-oriented characteristics. You can use CrackLib to stop users
from choosing passwords that are easy to guess.



%prep
mkdir cracklib-dicts
cp -f %{SOURCE10} %{SOURCE11} %{SOURCE12} %{SOURCE13} %{SOURCE14} \
      %{SOURCE15} %{SOURCE16} %{SOURCE17} %{SOURCE18} %{SOURCE19} \
      %{SOURCE20} %{SOURCE21} %{SOURCE22} %{SOURCE23} %{SOURCE24} \
      %{SOURCE25} %{SOURCE26} %{SOURCE27} %{SOURCE28} %{SOURCE29} \
      %{SOURCE30} %{SOURCE31} %{SOURCE32} %{SOURCE33} %{SOURCE34} \
      %{SOURCE35} %{SOURCE36} %{SOURCE37} %{SOURCE38} %{SOURCE1}  \
      %{SOURCE39} %{SOURCE40} %{SOURCE41} %{SOURCE42} %{SOURCE43} %{SOURCE44} \
      cracklib-dicts/
gunzip cracklib-dicts/*

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/cracklib/
/usr/sbin/cracklib-format cracklib-dicts/* | \
/usr/sbin/cracklib-packer $RPM_BUILD_ROOT/%{_datadir}/cracklib/pw_dict
#
# using zip'ed dict takes too long for a check. But the support
# for this is still in the lib.
#
#gzip $RPM_BUILD_ROOT/%{_datadir}/cracklib/pw_dict.pwd

%files 
%defattr(-,root,root)
%dir %{_datadir}/cracklib
%{_datadir}/cracklib/pw_dict.hwm
%{_datadir}/cracklib/pw_dict.pwd
%{_datadir}/cracklib/pw_dict.pwi

%changelog
