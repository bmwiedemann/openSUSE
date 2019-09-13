#
# spec file for package igerman98
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define ispell_dict_dir %(ispell -vv|grep LIBDIR|sed \"s/.*\=//;s/^ //g\" |tr -d \\")
%define ispell_emacs_lib_dir %{_prefix}/lib/ispell/emacs
Name:           igerman98
Version:        20161207
Release:        0
Summary:        German Spell Check Dictionaries
# According to Documentation/Copyright we can distribute program under GPL-2.0
# or GPL-3.0. We have choosed GPL-2.0.
License:        GPL-2.0
Group:          Productivity/Text/Spell
Url:            http://www.j3e.de/ispell/igerman98/dict/
Source0:        https://www.j3e.de/ispell/igerman98/dict/%{name}-%{version}.tar.bz2
Source2:        fix8bit.c
Source3:        austrian.el
Source4:        german.el
Source5:        swiss.el
Patch0:         %{name}-ispell-sort.patch
BuildRequires:  ispell

%description
A meta package for German, Swiss, and Austrian dictionaries for the ispell 
and myspell spell checkers.

%package doc
Summary:        Documentation for German dictionaries
License:        GPL-2.0+
Group:          Productivity/Text/Spell
BuildArch:      noarch

%description doc
Documentation for German, Swiss, and Austrian dictionaries for the ispell 
and myspell spell checkers.

%package -n ispell-ngerman
Summary:        New German ispell dictionary
License:        BSD-3-Clause
Group:          Productivity/Text/Spell
Provides:       ispell_dictionary
Provides:       locale(ispell:de;de_DE)

%description -n ispell-ngerman
This package includes a ready German dictionary for ispell. A short
usage description is given in %{_docdir}/ispell/README of
the package ispell.

%package -n ispell-nswiss
Summary:        New Swiss ispell dictionary
License:        GPL-2.0+
Group:          Productivity/Text/Spell
Provides:       ispell_dictionary
Provides:       locale(ispell:de_CH)

%description -n ispell-nswiss
This package includes a ready Swiss dictionary for ispell according
the new spelling rules.  The name of the dictionary is nswiss to be able
to distinguish it from those of the German packages. A short usage
description is given in %{_docdir}/ispell/README of the
package ispell.

%package -n ispell-naustrian
Summary:        New Austrian ispell dictionary
License:        GPL-2.0+
Group:          Productivity/Text/Spell
Provides:       ispell_dictionary
Provides:       locale(ispell:de_AT)

%description -n ispell-naustrian
This package includes a ready Austrian dictionary for ispell according
the new spelling rules.  The name of the dictionary is naustrian to be able
to distinguish it from those of the German packages. A short usage
description is given in %{_docdir}/ispell/README of the
package ispell.

%prep
%setup -q
%patch0 -p1

%build

# prepare ispell dictionary
cp %{SOURCE2} .
gcc -O2 -o fix8bit fix8bit.c
mv ispell/de_DE.aff.in ispell/de_DE.aff.in-bj
./fix8bit -8 < ispell/de_DE.aff.in-bj > ispell/de_DE.aff.in

for l in DE AT CH; do
  make %{?_smp_mflags} ispell/de_$l.{aff,hash}
done

make %{?_smp_mflags} ligature/rmligs

%install
mkdir -p %{buildroot}%{_docdir}/%{name}

# ispell
mkdir -p %{buildroot}%{ispell_dict_dir}
install -m 644 ispell/de_??.{aff,hash} %{buildroot}%{ispell_dict_dir}
mkdir -p %{buildroot}%{_bindir}
install -m 755 ligature/rmligs %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
install -m 644 ligature/rmligs.1 %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{ispell_emacs_lib_dir}
install -m 644 %{SOURCE3} %{SOURCE4} %{SOURCE5} %{buildroot}%{ispell_emacs_lib_dir}
for ext in aff hash; do
  ln -s %{ispell_dict_dir}/de_DE.$ext %{buildroot}%{ispell_dict_dir}/german.$ext
  ln -s %{ispell_dict_dir}/de_CH.$ext %{buildroot}%{ispell_dict_dir}/swiss.$ext
  ln -s %{ispell_dict_dir}/de_AT.$ext %{buildroot}%{ispell_dict_dir}/austrian.$ext
done

%files doc
%doc Documentation/*

%files -n ispell-ngerman
%{ispell_dict_dir}/de_DE.aff
%{ispell_dict_dir}/de_DE.hash
%{ispell_dict_dir}/german.aff
%{ispell_dict_dir}/german.hash
%{ispell_emacs_lib_dir}/german.el
%{_bindir}/rmligs
%{_mandir}/man1/rmligs.1%{ext_man}

%files -n ispell-nswiss
%{ispell_dict_dir}/de_CH.aff
%{ispell_dict_dir}/de_CH.hash
%{ispell_dict_dir}/swiss.aff
%{ispell_dict_dir}/swiss.hash
%{ispell_emacs_lib_dir}/swiss.el

%files -n ispell-naustrian
%{ispell_dict_dir}/de_AT.aff
%{ispell_dict_dir}/de_AT.hash
%{ispell_dict_dir}/austrian.aff
%{ispell_dict_dir}/austrian.hash
%{ispell_emacs_lib_dir}/austrian.el

%changelog
