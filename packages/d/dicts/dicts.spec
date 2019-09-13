#
# spec file for package dicts
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


Name:           dicts
BuildRequires:  fdupes
BuildRequires:  ispell
Version:        1.5
Release:        0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        Ispell Dictionary Files
License:        BSD-3-Clause and GPL-2.0+ and SUSE-Public-Domain
Group:          Productivity/Text/Spell
#
# Note: The hash table files depend on the architectures!
#       Not only on the little or big endianness of the
#       architecture but also on the natural pointer size.
#
##BuildArchitectures: noarch
Source:         prepare-dicts.tar.bz2
Source1:        hk2-deutsch.tar.bz2
Source2:        dutch96.tar.bz2
Source3:        espanol-1.5.tar.bz2
Source4:        francais-IREQ-1.4.tar.bz2
Source5:        idanish-1.2.1.tar.bz2
Source6:        iswedish-1.2.1.tar.bz2
Source7:        italian.tar.bz2
Source8:        ispell-norsk-2.0.tar.bz2
Source9:        portugues.tar.bz2
Source10:       ispellcat.tar.bz2
Source11:       sjp-ispell-pl-20140213.tar.bz2
Source12:       ispell-czech.tar.bz2
Source13:       ellhnika.tar.bz2
Source14:       rus-ispell.tar.bz2
Source15:       eo-spell.tar.bz2
Source16:       slovensko.tar.bz2
Source18:       br.ispell-2.4.tar.bz2
Source19:       finnish.tar.bz2
Source20:       estonian.tar.bz2
Source21:       dicts-rpmlintrc
Patch:          prepare-dicts.dif

%description
This package contains sources for 14 ispell dictionaries:

for German	 (already compiled for ispell in package ispell-german)

for Danish	 (already compiled for ispell in package ispell-danish)

for Spanish	 (already compiled for ispell in package
ispell-spanish)

for French	 (already compiled for ispell in package ispell-french)

for Italian	 (already compiled for ispell in package
ispell-italian)

for Dutch	 (already compiled for ispell in package ispell-dutch)

for Swedish	 (already compiled for ispell in package
ispell-swedish)

for Norwegian	 (already compiled for ispell in package ispell-norsk)

for Portuguese	 (already compiled for ispell in package
ispell-portuguese)

for Catalan	 (already compiled for ispell in package
ispell-catalan)

for Czech	 (already compiled for ispell in package ispell-czech)

for Polish	 (already compiled for ispell in package ispell-polish)

for Greek	 (already compiled for ispell in package ispell-greek)

for Russian	 (already compiled for ispell in package
ispell-russian)

for Brazilian	 (already compiled for ispell in package
ispell-brazilian)

for Finnish	 (already compiled for ispell in package
ispell-finnish)

for Estonian	 (already compiled for ispell in package
ispell-estonian)

Read the READMEs under /usr/src/dicts.


%package     -n ispell-german
Summary:        German ispell dictionary
License:        BSD-3-Clause
Group:          Productivity/Text/Spell
Provides:       igerman
Provides:       ispell_dictionary
Provides:       locale(ispell:de;de_DE)
Obsoletes:      igerman

%description -n ispell-german
This package includes a ready German dictionary for ispell. A short
usage description is given in /usr/share/doc/packages/ispell/README of
the package ispell. The sources for this dictionary are included in
the package dicts.

%package     -n ispell-danish
Summary:        Danish ispell dictionary
License:        GPL-2.0+
Group:          Productivity/Text/Spell
Provides:       idanish
Provides:       ispell_dictionary
Provides:       locale(ispell:da)
Obsoletes:      idanish

%description -n ispell-danish
This package includes a ready Danish dictionary for ispell. A short
usage description for ispell is given in
/usr/share/doc/packages/ispell/README of the package ispell. The
sources for this dictionary are included in the package dicts.

%package     -n ispell-spanish
Summary:        Spanish ispell dictionary
License:        GPL-2.0+
Group:          Productivity/Text/Spell
Provides:       ispanish
Provides:       ispell_dictionary
Provides:       locale(ispell:es;an_ES)
Obsoletes:      ispanish

%description -n ispell-spanish
This package includes a ready Spanish dictionary for ispell. A short
usage description for ispell is given in
/usr/share/doc/packages/ispell/README of the package ispell. The
sources for this dictionary are included in the package dicts.

%package     -n ispell-french
Summary:        French ispell dictionary
License:        GPL-2.0+
Group:          Productivity/Text/Spell
Provides:       ifrench
Provides:       ispell_dictionary
Provides:       locale(ispell:fr;br_FR)
Obsoletes:      ifrench
Conflicts:      ispell-french-gutenberg

%description -n ispell-french
This package includes a ready French dictionary for ispell. A short
usage description for ispell is given in
/usr/share/doc/packages/ispell/README of the package ispell. The
sources for this dictionary are included in the package dicts.

%package     -n ispell-italian
Summary:        Italian ispell dictionary
License:        GPL-2.0+
Group:          Productivity/Text/Spell
Provides:       iitalian
Provides:       ispell_dictionary
Provides:       locale(ispell:it)
Obsoletes:      iitalian

%description -n ispell-italian
This package includes a ready Italian dictionary for ispell. A short
usage description for ispell is given in
/usr/share/doc/packages/ispell/README of the package ispell. The
sources for this dictionary are included in the package dicts.

%package     -n ispell-dutch
Summary:        Dutch ispell dictionary
License:        SUSE-Permissive
Group:          Productivity/Text/Spell
Provides:       idutch
Provides:       ispell_dictionary
Provides:       locale(ispell:nl)
Obsoletes:      idutch

%description -n ispell-dutch
This package includes a ready Dutch dictionary for ispell. A short
usage description for ispell is given in
/usr/share/doc/packages/ispell/README of the package ispell. The
sources for this dictionary are included in the package dicts.

%package     -n ispell-swedish
Summary:        Swedish ispell dictionary
License:        GPL-2.0+
Group:          Productivity/Text/Spell
Provides:       ispell_dictionary
Provides:       iswedish
Provides:       locale(ispell:sv)
Obsoletes:      iswedish

%description -n ispell-swedish
This package includes a ready Swedish dictionary for ispell. A short
usage description for ispell is given in
/usr/share/doc/packages/ispell/README of the package ispell. The
sources for this dictionary are included in the package dicts.

%package     -n ispell-norsk
Summary:        Norwegian ispell dictionary
License:        GPL-2.0+
Group:          Productivity/Text/Spell
Provides:       inorsk
Provides:       ispell_dictionary
Provides:       locale(ispell:nb;nn;no;se_NO)
Obsoletes:      inorsk

%description -n ispell-norsk
This package includes a ready Norwegian dictionary for ispell. A
short usage description for ispell is given in
/usr/share/doc/packages/ispell/README of the package ispell. The
sources for this dictionary are included in the package dicts.

%package     -n ispell-portuguese
Summary:        Portuguese ispell dictionary
License:        GPL-2.0+
Group:          Productivity/Text/Spell
Provides:       iportug
Provides:       ispell_dictionary
Provides:       locale(ispell:pt;pt_PT)
Obsoletes:      iportug

%description -n ispell-portuguese
This package includes a ready Portuguese dictionary for ispell. A
short usage description for ispell is given in
/usr/share/doc/packages/ispell/README of the package ispell. The
sources for this dictionary are included in the package dicts.

%package     -n ispell-catalan
Summary:        Catalan ispell dictionary
License:        SUSE-Permissive
Group:          Productivity/Text/Spell
Provides:       icatalan
Provides:       ispell_dictionary
Provides:       locale(ispell:ca)
Obsoletes:      icatalan

%description -n ispell-catalan
This package includes a ready Catalan dictionary for ispell. A short
usage description for ispell is given in
/usr/share/doc/packages/ispell/README of the package ispell. The
sources for this dictionary are included in the package dicts.

%package     -n ispell-czech
Summary:        Czech ispell dictionary
License:        BSD-3-Clause
Group:          Productivity/Text/Spell
Provides:       iczech
Provides:       ispell_dictionary
Provides:       locale(ispell:cs;sk)
Obsoletes:      iczech

%description -n ispell-czech
This package includes a ready Czech dictionary for ispell. A short
usage description is given in /usr/share/doc/packages/ispell/README of
the package ispell. The sources for this dictionary are included in
the package dicts.

%package     -n ispell-polish
Summary:        Polish ispell dictionary
License:        GPL-2.0 and LGPL-2.1 and MPL-1.1 and CC-BY-SA-1.0
Group:          Productivity/Text/Spell
Provides:       ipolish
Provides:       ispell_dictionary
Provides:       locale(ispell:pl)
Obsoletes:      ipolish

%description -n ispell-polish
This package includes a ready Polish dictionary for ispell. A short
usage description is given in /usr/share/doc/packages/ispell/README of
the package ispell. The sources for this dictionary are included in
the package dicts.

%package     -n ispell-greek
Summary:        Greek ispell dictionary
License:        BSD-3-Clause and GPL-2.0+
Group:          Productivity/Text/Spell
Provides:       igreek
Provides:       ispell_dictionary
Provides:       locale(ispell:el)
Obsoletes:      igreek

%description -n ispell-greek
This package includes a ready Greek dictionary for ispell. A short
usage description is given in /usr/share/doc/packages/ispell/README of
the package ispell. The sources for this dictionary are included in
the package dicts.

%package     -n ispell-russian
Summary:        Russian ispell dictionary
License:        SUSE-Permissive
Group:          Productivity/Text/Spell
Provides:       irussian
Provides:       ispell_dictionary
Provides:       locale(ispell:ru)
Obsoletes:      irussian

%description -n ispell-russian
This package includes a ready Russian dictionary for ispell. A short
usage description is given in /usr/share/doc/packages/ispell/README of
the package ispell. The sources for this dictionary are included in
the package dicts.

%package     -n ispell-esperanto
Summary:        Esperanto ispell dictionary
License:        GPL-2.0+
Group:          Productivity/Text/Spell
Provides:       iesperan
Provides:       ispell_dictionary
Obsoletes:      iesperan

%description -n ispell-esperanto
This package includes a ready Esperanto dictionary for ispell. A short
usage description is given in /usr/share/doc/packages/ispell/README of
the package ispell. The sources for this dictionary are included in
the package dicts.

%package     -n ispell-slovene
Summary:        Slovenian ispell dictionary
License:        BSD-3-Clause and GPL-2.0+
Group:          Productivity/Text/Spell
Provides:       islovene
Provides:       ispell_dictionary
Provides:       locale(ispell:sl)
Obsoletes:      islovene

%description -n ispell-slovene
This package includes a ready Slovenian dictionary for ispell. A short
usage description is given in /usr/share/doc/packages/ispell/README of
the package ispell. The sources for this dictionary are included in
the package dicts.

%package     -n ispell-brazilian
Summary:        Brazilian ispell dictionary
License:        GPL-2.0+
Group:          Productivity/Text/Spell
Provides:       ispell_dictionary
Provides:       locale(ispell:pt_BR)

%description -n ispell-brazilian
This package includes a ready Brazilian dictionary for ispell. A short
usage description is given in /usr/share/doc/packages/ispell/README of
the package ispell. The sources for this dictionary are included in
the package dicts.

%package     -n ispell-finnish
Summary:        Finnish ispell dictionary
License:        GPL-2.0+
Group:          Productivity/Text/Spell
Provides:       ispell_dictionary
Provides:       locale(ispell:fi)

%description -n ispell-finnish
This package includes a ready Finnish dictionary for ispell. A short
usage description is given in /usr/share/doc/packages/ispell/README of
the package ispell. The sources for this dictionary are included in
the package dicts.

%package     -n ispell-estonian
Summary:        Estonian ispell dictionary
License:        LGPL-2.1+
Group:          Productivity/Text/Spell
Provides:       ispell_dictionary
Provides:       locale(ispell:et)

%description -n ispell-estonian
This package includes a ready Estonian dictionary for ispell. A short
usage description is given in /usr/share/doc/packages/ispell/README of
the package ispell. The sources for this dictionary are included in
the package dicts.

%prep
  for a in $RPM_SOURCE_DIR/*.tar.gz  \
           $RPM_SOURCE_DIR/*.tar.bz2 \
           $RPM_SOURCE_DIR/*.tgz
  do
      test -e "$a"       || continue
      test -e "${a##*/}" && continue
      ln -sf "$a" .
  done
%setup -n prepare-dicts
  cat $RPM_SOURCE_DIR/prepare-dicts.dif | \
    sed -n "/^--- Makefile.Linux/,/^---/p" | \
  patch -s -p0
  make -f Makefile.Linux extract
  rm Makefile.Linux
%patch

# unify the permissions of all files, to make fdupes working again (bnc#784670)
find . -type f -exec chmod 0644 {} +

%build
  PATH=$PATH:$PWD
  export PATH
  make -f Makefile.Linux compile

%install
  make -f Makefile.Linux DESTDIR=$RPM_BUILD_ROOT install
  %fdupes $RPM_BUILD_ROOT/usr/src/dicts

%files -n ispell-german
%defattr(-, root, root)
/usr/lib/ispell/emacs/deutsch.el
/usr/lib/ispell/deutsch.aff
/usr/lib/ispell/deutsch.hash
/usr/lib/ispell/deutschlxg.hash
/usr/lib/ispell/deutschmed.hash
%doc /usr/share/doc/packages/ispell-german/

%files -n ispell-danish
%defattr(-, root, root)
/usr/lib/ispell/emacs/dansk.el
/usr/lib/ispell/dansk.aff
/usr/lib/ispell/dansk.hash
%doc /usr/share/doc/packages/ispell-danish/

%files -n ispell-spanish
%defattr(-, root, root)
/usr/lib/ispell/emacs/espanol.el
/usr/lib/ispell/espanol.aff
/usr/lib/ispell/espanol.hash
/usr/lib/ispell/spanish.aff
/usr/lib/ispell/spanish.hash
%doc /usr/share/doc/packages/ispell-spanish/

%files -n ispell-french
%defattr(-, root, root)
/usr/lib/ispell/emacs/francais.el
/usr/lib/ispell/francais.aff
/usr/lib/ispell/francais.hash
%doc /usr/share/doc/packages/ispell-french/

%files -n ispell-italian
%defattr(-, root, root)
/usr/lib/ispell/emacs/italian.el
/usr/lib/ispell/italian.aff
/usr/lib/ispell/italian.hash
%doc /usr/share/doc/packages/ispell-italian/

%files -n ispell-dutch
%defattr(-, root, root)
/usr/lib/ispell/emacs/nederlands.el
/usr/lib/ispell/nederlands.aff
/usr/lib/ispell/nederlands.hash
%doc /usr/share/doc/packages/ispell-dutch/

%files -n ispell-swedish
%defattr(-, root, root)
/usr/lib/ispell/emacs/svenska.el
/usr/lib/ispell/svenska.aff
/usr/lib/ispell/svenska.hash
%doc /usr/share/doc/packages/ispell-swedish/

%files -n ispell-norsk
%defattr(-, root, root)
/usr/bin/inorsk-compwordsmaybe
/usr/bin/inorsk-hyphenmaybe
/usr/lib/ispell/emacs/norsk.el
/usr/lib/ispell/norsk.aff
/usr/lib/ispell/norsk.hash
/usr/lib/ispell/nynorsk.aff
/usr/lib/ispell/nynorsk.hash
%doc /usr/share/doc/packages/ispell-norsk/

%files -n ispell-portuguese
%defattr(-, root, root)
/usr/lib/ispell/emacs/portugues.el
/usr/lib/ispell/portugues.aff
/usr/lib/ispell/portugues.hash
%doc /usr/share/doc/packages/ispell-portuguese/

%files -n ispell-catalan
%defattr(-, root, root)
/usr/lib/ispell/emacs/catala.el
/usr/lib/ispell/catala.aff
/usr/lib/ispell/catala.hash
/usr/lib/ispell/catalan.aff
/usr/lib/ispell/catalan.hash
%doc /usr/share/doc/packages/ispell-catalan/

%files -n ispell-czech
%defattr(-, root, root)
/usr/lib/ispell/emacs/czech.el
/usr/lib/ispell/czech.aff
/usr/lib/ispell/czech.hash
%doc /usr/share/doc/packages/ispell-czech/

%files -n ispell-polish
%defattr(-, root, root)
/usr/lib/ispell/emacs/polish.el
/usr/lib/ispell/polish.aff
/usr/lib/ispell/polish.hash
%doc /usr/share/doc/packages/ispell-polish/

%files -n ispell-greek
%defattr(-, root, root)
/usr/lib/ispell/emacs/ellhnika.el
/usr/lib/ispell/ellhnika.aff
/usr/lib/ispell/ellhnika.hash
%doc /usr/share/doc/packages/ispell-greek/

%files -n ispell-russian
%defattr(-, root, root)
/usr/lib/ispell/emacs/russian.el
/usr/lib/ispell/russian.aff
/usr/lib/ispell/russian.hash
#/usr/lib/ispell/rmakedict
%doc /usr/share/doc/packages/ispell-russian/

%files -n ispell-esperanto
%defattr(-, root, root)
/usr/lib/ispell/emacs/esperanto.el
/usr/lib/ispell/esperanto.aff
/usr/lib/ispell/esperanto.hash
%doc /usr/share/doc/packages/ispell-esperanto/

%files -n ispell-slovene
%defattr(-, root, root)
/usr/lib/ispell/emacs/slovensko.el
/usr/lib/ispell/slovensko.aff
/usr/lib/ispell/slovensko.hash
%doc /usr/share/doc/packages/ispell-slovene/

%files -n ispell-brazilian
%defattr(-, root, root)
/usr/bin/conjugue
/usr/lib/ispell/emacs/brazilian.el
/usr/lib/ispell/br.aff
/usr/lib/ispell/br.hash
/usr/lib/ispell/brazilian.aff
/usr/lib/ispell/brazilian.hash
/usr/lib/ispell-brazilian/
%doc /usr/share/doc/packages/ispell-brazilian/
%dir /usr/share/man/pt_BR/
%dir /usr/share/man/pt_BR/man1/
%doc /usr/share/man/pt_BR/man1/conjugue.1.gz

%files -n ispell-finnish
%defattr(-, root, root)
/usr/lib/ispell/emacs/finnish.el
/usr/lib/ispell/finnish.aff
/usr/lib/ispell/finnish.hash
%doc /usr/share/doc/packages/ispell-finnish/

%files -n ispell-estonian
%defattr(-, root, root)
/usr/lib/ispell/emacs/estonian.el
/usr/lib/ispell/estonian.aff
/usr/lib/ispell/estonian.hash
%doc /usr/share/doc/packages/ispell-estonian/

%files
%defattr(-, root, root)
/usr/src/dicts/
%doc /usr/share/doc/packages/dicts/

%changelog
