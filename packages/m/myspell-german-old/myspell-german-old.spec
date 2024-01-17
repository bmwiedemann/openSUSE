#
# spec file for package myspell-german-old
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           myspell-german-old
Version:        20030428
Release:        0
Summary:        Old German Dictionary for MySpell
License:        GPL-2.0+
Group:          Productivity/Text/Spell
Url:            http://j3e.de/myspell/
Source0:        de_OLDSPELL.tar.bz2
Source1:        Nwordlist.tgz
Source2:        hyph_de_OLDSPELL.zip
BuildRequires:  unzip
Provides:       myspell-dictionary
Provides:       myspell-german-dictionary
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
# myspell-german: before 13.2
Conflicts:      myspell-german
Conflicts:      myspell-de

%description
This dictionary supports spell checking according to the old German spelling
rules.

MySpell dictionaries are compatible with MySpell and Hunspell spell-checker.
They are used by various desktop applications, for example, LibreOffice,
Mozilla Thunderbird, and Mozilla Firefox.

%prep
%setup -q -c -a 1 -a 2

%build
# add the Novell jargon into dictionary bnc#306333
# the file Nwordlist needs to contain extra newline on the beginning!
cat Nwordlist >> de_OLDSPELL.dic

%install
install -m 755 -d %{buildroot}%{_datadir}/hunspell/
install -m 644 de_OLDSPELL.dic %{buildroot}%{_datadir}/hunspell/de_DE.dic
install -m 644 de_OLDSPELL.aff %{buildroot}%{_datadir}/hunspell/de_DE.aff
install -m 755 -d %{buildroot}%{_datadir}/hyphen/
install -m 644 hyph_de_OLD.dic %{buildroot}%{_datadir}/hyphen/hyph_de_DE.dic
install -m 755 -d %{buildroot}%{_datadir}/myspell/
ln -s %{_datadir}/hunspell/de_DE.dic %{buildroot}%{_datadir}/myspell/de_DE.dic
ln -s %{_datadir}/hunspell/de_DE.aff %{buildroot}%{_datadir}/myspell/de_DE.aff
ln -s %{_datadir}/hyphen/hyph_de_DE.dic %{buildroot}%{_datadir}/myspell/hyph_de_DE.dic

%files
%defattr(-,root,root)
%dir %{_datadir}/hunspell/
%{_datadir}/hunspell/de_DE.dic
%{_datadir}/hunspell/de_DE.aff
%dir %{_datadir}/hyphen/
%{_datadir}/hyphen/hyph_de_DE.dic
%dir %{_datadir}/myspell/
%{_datadir}/myspell/de_DE.dic
%{_datadir}/myspell/de_DE.aff
%{_datadir}/myspell/hyph_de_DE.dic

%changelog
