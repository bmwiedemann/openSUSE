#
# spec file for package aspell-dictionaries
#
# Copyright (c) 2024 SUSE LLC
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


%define dict_langs af agal ar az am ast be bg bn br ca cs csb cy da de el eo es et fa fi fo fr fy ga gd gl grc gu gv he hi hil hr hsb hu hus hy ia id is it kn ku ky la lt lv mg mi mk ml mn mr ms mt nb nds nl nn ny or pa pl pt_PT pt_BR qu ro ru rw sc sk sl sr sv sw ta te tet tk tl tn tr uk uz vi wa yi zu
%define aspell_dict_dir %(aspell dump config dict-dir)
%define aspell_data_dir %(aspell dump config data-dir)

Name:           aspell-dictionaries
Version:        0.50.6
Release:        0
Summary:        The Source Package for Official Aspell Dictionaries
License:        LGPL-2.1-or-later
Group:          Productivity/Text/Spell
URL:            http://aspell.net/
#
#  PLEASE keep aspell-lang-ver.tar.bz2 pattern in SourceN: fields!
#
#    I know it means repacking sometimes, but it helps
#    maintainging this package as a whole.
#
#    If you don't want have so_much_work, please notify me
#    about new version of a dictionary, I will update it.
#    pgajdos@suse.com
#
Source0:        aspell-da-1.6.36.tar.bz2
Source1:        aspell-ast-0.01.tar.bz2
Source2:        aspell-el-0.08-0.tar.bz2
Source3:        aspell-es-1.11-2.tar.bz2
Source4:        aspell-fo-0.2.16-1.tar.bz2
Source5:        aspell-fr-0.50-3.tar.bz2
Source6:        aspell-pt_PT-20190329.tar.bz2
Source7:        aspell-sk-2.01-2.tar.bz2
Source8:        aspell-sv-0.51-0.tar.bz2
Source9:        aspell-cy-0.50-3.tar.bz2
Source10:       aspell-ga-4.5-0.tar.bz2
Source11:       aspell-nn-0.50.1-1.tar.bz2
Source12:       aspell-pl-6.0_20150428-0.tar.bz2
Source13:       aspell-ru-0.99f7-1.tar.bz2
Source14:       aspell-ro-3.3-2.tar.bz2
Source15:       aspell-uk-1.4.0.tar.bz2
Source16:       aspell-ca-2.1.5-1.tar.bz2
Source17:       aspell-br-0.50-2.tar.bz2
Source18:       aspell-bg-4.1.tar.bz2
Source19:       aspell-af-0.50-0.tar.bz2
Source20:       aspell-eo-2.1.20000225a-1.tar.bz2
Source21:       aspell-hr-0.51-0.tar.bz2
Source22:       aspell-is-0.51.1-0.tar.bz2
Source23:       aspell-it-2.2_20050523-0.tar.bz2
Source24:       aspell-nb-0.50.1-0.tar.bz2
Source25:       aspell-mt-0.50-0.tar.bz2
Source26:       aspell-am-0.03-1.tar.bz2
Source27:       aspell-be-0.01.tar.bz2
Source28:       aspell-bn-0.01.1-1.tar.bz2
Source29:       aspell-csb-0.02-0.tar.bz2
Source30:       aspell-et-0.1.21-1.tar.bz2
Source31:       aspell-fa-0.11-0.tar.bz2
Source32:       aspell-he-1.0-0.tar.bz2
Source33:       aspell-fi-0.7-0.tar.bz2
Source34:       aspell-gd-0.1.1-1.tar.bz2
Source35:       aspell-gl-0.5a-2.tar.bz2
Source36:       aspell-gv-0.50-0.tar.bz2
Source37:       aspell-hi-0.02-0.tar.bz2
Source38:       aspell-hil-0.11-0.tar.bz2
Source39:       aspell-hsb-0.02-0.tar.bz2
Source40:       aspell-hu-0.99.4.2-0.tar.bz2
Source41:       aspell-ia-0.50-1.tar.bz2
Source42:       aspell-id-1.2-0.tar.bz2
Source43:       aspell-ku-0.20-1.tar.bz2
Source44:       aspell-lt-1.2.1-0.tar.bz2
Source45:       aspell-lv-0.5.5-1.tar.bz2
Source46:       aspell-la-20020503-0.tar.bz2
Source47:       aspell-mi-0.50-0.tar.bz2
Source48:       aspell-mk-0.50-0.tar.bz2
Source49:       aspell-mn-0.06-2.tar.bz2
Source50:       aspell-mg-0.03-0.tar.bz2
Source51:       aspell-mr-0.10-0.tar.bz2
Source52:       aspell-ms-0.50-0.tar.bz2
Source53:       aspell-no-0.50-2.tar.bz2
Source54:       aspell-ny-0.01-0.tar.bz2
Source55:       aspell-or-0.03-1.tar.bz2
Source56:       aspell-pa-0.01-1.tar.bz2
Source57:       aspell-qu-0.02-0.tar.bz2
Source58:       aspell-rw-0.50-0.tar.bz2
Source59:       aspell-sl-0.50-0.tar.bz2
Source60:       aspell-sc-1.0.tar.bz2
Source61:       aspell-sw-0.50-0.tar.bz2
Source62:       aspell-ta-20040424-1.tar.bz2
Source63:       aspell-tet-0.1.1.tar.bz2
Source64:       aspell-tl-0.02-1.tar.bz2
Source65:       aspell-tn-1.0.1-0.tar.bz2
Source66:       aspell-tr-0.50-0.tar.bz2
Source67:       aspell-uz-0.6-0.tar.bz2
Source68:       aspell-vi-0.01.1-1.tar.bz2
Source69:       aspell-wa-0.50-0.tar.bz2
Source70:       aspell-yi-0.01.1-1.tar.bz2
Source71:       aspell-zu-0.50-0.tar.bz2
Source72:       aspell-az-0.02-0.tar.bz2
Source73:       aspell-ar-1.2-0.tar.bz2
Source74:       aspell-sr-0.02.tar.bz2
Source75:       aspell-nl-1.00-G.tar.bz2
Source76:       aspell-cs-20040614-1.tar.bz2
Source77:       aspell-gu-0.03-0.tar.bz2
Source78:       aspell-hy-0.10.0-0.tar.bz2
Source79:       aspell-nds-0.01-20071031.tar.bz2
Source80:       aspell-te-0.01-2.tar.bz2
Source81:       aspell-fy-0.12-0.tar.bz2
Source82:       aspell-pt_BR-20131030-12-0.tar.bz2
Source83:       aspell-ml-0.03-1.tar.bz2
Source84:       aspell-tk-0.01-0.tar.bz2
Source85:       aspell-agal-0.50-1.tar.bz2
Source86:       aspell-grc-0.02-0.tar.bz2
Source87:       aspell-ky-0.01-0.tar.bz2
Source88:       aspell-kn-0.01-1.tar.bz2
Source89:       aspell-hus-0.03-1.tar.bz2
Source90:       aspell-de-20161207-7-0.tar.bz2
Source999:      aspell-dictionaries-rpmlintrc
# PATCH-FIX-OPENSUSE aspell-dansk.patch -- Patch needed for new dansk dictionary
Patch0:         aspell-dansk.patch
BuildRequires:  aspell
BuildRequires:  fdupes

%description
This source package contains dictionaries from http://aspell.net/ that
are distributable under the GPL license.

%package -n aspell-af
Version:        0.50.0
Release:        0
Summary:        Afrikaans Dictionary for Aspell
License:        LGPL-2.1-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:af)

%description -n aspell-af
An Afrikaans dictionary for the aspell spell checker.

%package -n aspell-agal
Version:        0.50.0
Release:        0
Summary:        Galician-portuguese (galego-portugués) Dictionary for Aspell
License:        GPL-2.0-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:gl)

%description -n aspell-agal
A Galician-portuguese (galego-portugués) dictionary for the aspell spell checker.

%package -n aspell-am
Version:        0.03.1
Release:        0
Summary:        Amharic (አማርኛ) Dictionary for Aspell
License:        SUSE-Public-Domain
Group:          Productivity/Text/Spell
Provides:       locale(aspell:am)

%description -n aspell-am
An Amharic (አማርኛ) dictionary for the aspell spell checker.

%package -n aspell-ar
Version:        1.2.0
Release:        0
Summary:        Arabic (العربية) Dictionary for Aspell
License:        GPL-2.0-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:ar)

%description -n aspell-ar
An Arabic (العربية) dictionary for the aspell spell checker.

%package -n aspell-az
Version:        0.02
Release:        0
Summary:        Azerbaijani (تورکجه) Dictionary for Aspell
License:        GPL-2.0-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:az)

%description -n aspell-az
An Azerbaijani (تورکجه) dictionary for the aspell spell checker.

%package -n aspell-be
Version:        0.01
Release:        0
Summary:        Belarusian (беларуская мова) Dictionary for Aspell
License:        GPL-2.0-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:be)

%description -n aspell-be
A Belarusian (беларуская мова) dictionary for the aspell spell checker.

%package -n aspell-bg
Version:        4.1
Release:        0
Summary:        Bulgarian (български) Dictionary for Aspell
License:        GPL-2.0-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:bg)

%description -n aspell-bg
A Bulgarian (български) dictionary for the aspell spell checker.

%package -n aspell-bn
Version:        0.01.1
Release:        0
Summary:        Bengali (বাংলা) Dictionary for Aspell
License:        GPL-2.0-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:bn)

%description -n aspell-bn
A Bengali (বাংলা) dictionary for the aspell spell checker.

%package -n aspell-br
Version:        0.50.2
Release:        0
Summary:        Breton (brezhoneg) Dictionary for Aspell
License:        GPL-2.0-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:br)

%description -n aspell-br
A Breton (brezhoneg) dictionary for the aspell spell checker.

%package -n aspell-ca
Version:        0.60.1.20090722
Release:        0
Summary:        Catalan (català) Dictionary for Aspell
License:        GPL-2.0-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:ca)

%description -n aspell-ca
A Catalan (català) dictionary for the aspell spell checker.

%package -n aspell-cs
Version:        0.60.0.20040614
Release:        0
Summary:        Czech (čeština) Dictionary for Aspell
License:        GPL-2.0-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:cs)

%description -n aspell-cs
A Czech (český) dictionary for the aspell spell checker.

%package -n aspell-csb
Version:        0.02.0
Release:        0
Summary:        Kashubian (kaszëbsczi) Dictionary for Aspell
License:        GPL-2.0-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:csb)

%description -n aspell-csb
A Kashubian (kaszëbsczi) dictionary for the aspell spell checker.

%package -n aspell-cy
Version:        0.50.3
Release:        0
Summary:        Welsh (Cymraeg) Dictionary for Aspell
License:        GPL-2.0-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:cy)

%description -n aspell-cy
A Welsh (Cymraeg) dictionary for the aspell spell checker.

%package -n aspell-da
Version:        1.6.20
Release:        0
URL:            http://da.speling.org/
Summary:        Danish (dansk) Dictionary for Aspell
License:        GPL-2.0-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:da)

%description -n aspell-da
A Danish (dansk) dictionary for the aspell spell checker.

%package -n aspell-de
Version:        20161207.7.0
Release:        0
Summary:        German (deutsch) Dictionary for Aspell
License:        GPL-2.0-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:de)

%description -n aspell-de
A German (deutsch) dictionary for the aspell spell checker.

%package -n aspell-ast
Version:        0.01
Release:        0
Summary:        Asturian (asturianu) Dictionary for Aspell
License:        GPL-2.0-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:ast)

%description -n aspell-ast
An Asturian (asturianu) dictionary for the aspell spell checker.

%package -n aspell-el
# Add 0.50.3 in front of the version since the old version numbering was greater than the new one (0.50.3 compared to 0.08)
Version:        0.50.3+0.08
Release:        0
Summary:        Greek (ελληνικά) Dictionary for Aspell
License:        GPL-2.0-or-later
Group:          Productivity/Text/Spell
URL:            http://elspell.math.upatras.gr/?section=aspell
Provides:       locale(aspell:el)

%description -n aspell-el
A Greek (ελληνικά) dictionary for the aspell spell checker.

%package -n aspell-eo
Version:        2.1.20000225
Release:        0
Summary:        Esperanto Dictionary for Aspell
License:        GPL-2.0-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:eo)

%description -n aspell-eo
An Esperanto dictionary for the aspell spell checker.

%package -n aspell-es
Version:        1.11.2
Release:        0
Summary:        Spanish (español) Dictionary for Aspell
License:        GPL-2.0-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:es)

%description -n aspell-es
A Spanish (español) dictionary for the aspell spell checker.

%package -n aspell-et
Version:        0.1.21
Release:        0
Summary:        Estonian (eesti) Dictionary for Aspell
License:        LGPL-2.1-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:et)

%description -n aspell-et
An Estonian (eesti) dictionary for the aspell spell checker.

%package -n aspell-fa
Version:        0.11.0
Release:        0
Summary:        Persian (فارسی) Dictionary for Aspell
License:        GPL-2.0-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:fa)

%description -n aspell-fa
A Persian (فارسی) dictionary for the aspell spell checker.

%package -n aspell-fi
Version:        0.7
Release:        0
Summary:        Finnish (suomi) Dictionary for Aspell
License:        GPL-2.0-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:fi)

%description -n aspell-fi
A Finnish (suomi) dictionary for the aspell spell checker.

%package -n aspell-fy
Version:        0.12
Release:        0
Summary:        Frisian (Frysk) Dictionary for Aspell
License:        GPL-2.0-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:fy)

%description -n aspell-fy
A Frisian (Frysk) dictionary for the aspell spell checker.

%package -n aspell-fo
Version:        0.2.16
Release:        0
Summary:        Faroese (føroyskt) Dictionary for Aspell
License:        GPL-2.0-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:fo)

%description -n aspell-fo
A Faroese (føroyskt) dictionary for the aspell spell checker.

%package -n aspell-fr
Version:        0.50.3
Release:        0
Summary:        French (français) Dictionary for Aspell
License:        GPL-2.0-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:fr)

%description -n aspell-fr
A French (français) dictionary for the aspell spell checker.

%package -n aspell-ga
Version:        4.5.0
Release:        0
Summary:        Irish (Gaeilge) Dictionary for Aspell
License:        GPL-2.0-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:ga)

%description -n aspell-ga
An Irish (Gaeilge) dictionary for the aspell spell checker.

%package -n aspell-gd
Version:        0.7.1.1.1
Release:        0
Summary:        Scottish (Gàidhlig) Gaelic Dictionary for Aspell
License:        GPL-2.0-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:gd)

%description -n aspell-gd
A Scottish (Gàidhlig) Gaelic dictionary for the aspell spell checker.

%package -n aspell-gl
Version:        0.50a
Release:        0
Summary:        Galician Gaelic (galego) Dictionary for Aspell
License:        GPL-2.0-only
Group:          Productivity/Text/Spell
Provides:       locale(aspell:gl)

%description -n aspell-gl
A Galician Gaelic (galego) dictionary for the aspell spell checker.

%package -n aspell-grc
Version:        0.02.0
Release:        0
Summary:        Ancient Greek (Ἑλληνική) Dictionary for Aspell
License:        GPL-3.0-only
Group:          Productivity/Text/Spell
Provides:       locale(aspell:grc)

%description -n aspell-grc
An Ancient Greek (Ἑλληνική) dictionary for the aspell spell checker.

%package -n aspell-gu
Version:        0.03
Release:        0
Summary:        Gujarati (ગુજરાતી) Dictionary for Aspell
License:        LGPL-2.1-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:gu)

%description -n aspell-gu
A Gujarati (ગુજરાતી) dictionary for the aspell spell checker.

%package -n aspell-gv
Version:        0.50
Release:        0
Summary:        Manx Gaelic (Gaelg) Dictionary for Aspell
License:        GPL-2.0-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:gv)

%description -n aspell-gv
A Manx Gaelic (Gaelg) dictionary for the aspell spell checker.

%package -n aspell-he
Version:        1.0.0
Release:        0
Summary:        Hebrew (עברית) Dictionary for Aspell
License:        GPL-2.0-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:he)

%description -n aspell-he
A Hebrew (עברית) dictionary for the aspell spell checker.

%package -n aspell-hi
Version:        0.02
Release:        0
Summary:        Hindi (हिंदी) Dictionary for Aspell
License:        GPL-2.0-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:hi)
# u-deva.cmap and u-deva.cset files are also provided by aspell-mr
Conflicts:      aspell-mr

%description -n aspell-hi
A Hindi (हिंदी) dictionary for the aspell spell checker.

%package -n aspell-hil
Version:        0.11
Release:        0
Summary:        Hiligaynon Dictionary for Aspell
License:        GPL-2.0-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:hil)

%description -n aspell-hil
A Hiligaynon dictionary for the aspell spell checker.

%package -n aspell-hr
Version:        0.51.0
Release:        0
Summary:        Croatian (hrvatski) Dictionary for Aspell
License:        LGPL-2.1-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:hr)

%description -n aspell-hr
A Croatian (hrvatski) dictionary for the aspell spell checker.

%package -n aspell-hsb
Version:        0.02.0
Release:        0
Summary:        Upper Sorbian (hornjoserbsce) Dictionary for Aspell
License:        GPL-2.0-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:hsb)

%description -n aspell-hsb
An Upper Sorbian (hornjoserbsce) dictionary for the aspell spell checker.

%package -n aspell-hu
Version:        0.99.4.2
Release:        0
Summary:        Hungarian (magyar) Dictionary for Aspell
License:        GPL-2.0-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:hu)

%description -n aspell-hu
A Hungarian (magyar) dictionary for the aspell spell checker.

%package -n aspell-hus
Version:        0.03.1
Release:        0
Summary:        Huastec (wastek) dictionary for Aspell
License:        GPL-3.0-only
Group:          Productivity/Text/Spell
Provides:       locale(aspell:hus)

%description -n aspell-hus
A Huastec (wastek) dictionary for Aspell.

%package -n aspell-hy
Version:        0.10.0
Release:        0
Summary:        Armenian (Հայերեն) Dictionary for Aspell
License:        GPL-2.0-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:hy)

%description -n aspell-hy
An Armenian (Հայերեն) dictionary for the aspell spell checker.

%package -n aspell-ia
Version:        0.50
Release:        0
Summary:        Interlingua Dictionary for Aspell
License:        LGPL-2.1-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:ia)

%description -n aspell-ia
An Interlingua dictionary for the aspell spell checker.

%package -n aspell-id
Version:        1.2
Release:        0
Summary:        Indonesian (Bahasa Indonesia) Dictionary for Aspell
License:        GPL-2.0-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:id)

%description -n aspell-id
An Indonesian (Bahasa Indonesia) dictionary for the aspell spell checker.

%package -n aspell-is
Version:        0.51.10
Release:        0
Summary:        Icelandic (Íslenska) Dictionary for Aspell
License:        GPL-2.0-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:is)

%description -n aspell-is
An Icelandic (Íslenska) dictionary for the aspell spell checker.

%package -n aspell-it
Version:        2.2_20050523
Release:        0
Summary:        Italian (italiano) Dictionary for Aspell
License:        GPL-2.0-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:it)

%description -n aspell-it
An Italian (italiano) dictionary for the aspell spell checker.

%package -n aspell-kn
Version:        0.01.1
Release:        0
Summary:        Kannada (ಕನ್ನಡ) Dictionary for Aspell
License:        GPL-2.0-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:kn)

%description -n aspell-kn
A Kannada (ಕನ್ನಡ) dictionary for the aspell spell checker.

%package -n aspell-ku
Version:        0.20.1
Release:        0
Summary:        Kurdi (Kurdî, كوردی‎) Dictionary for Aspell
License:        GPL-2.0-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:ku)

%description -n aspell-ku
A Kurdi (Kurdî, كوردی‎) dictionary for the aspell spell checker.

%package -n aspell-ky
Version:        0.01.0
Release:        0
Summary:        Kirghiz (Кыргызча) Dictionary for Aspell
License:        GPL-2.0-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:ky)

%description -n aspell-ky
A Kirghiz (Кыргызча) dictionary for the aspell spell checker.

%package -n aspell-la
Version:        20020503
Release:        0
Summary:        Latin (latine) Dictionary for Aspell
License:        GPL-2.0-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:la)

%description -n aspell-la
A Latin (latine) dictionary for the aspell spell checker.

%package -n aspell-lt
Version:        1.2.1
Release:        0
Summary:        Lithuanian (lietuvių) Dictionary for Aspell
License:        BSD-3-Clause
Group:          Productivity/Text/Spell
Provides:       locale(aspell:lt)

%description -n aspell-lt
A Lithuanian ((lietuvių) dictionary for the aspell spell checker.

%package -n aspell-lv
Version:        1.2.1
Release:        0
Summary:        Latvian (latviešu) Dictionary for Aspell
License:        GPL-2.0-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:lv)

%description -n aspell-lv
A Latvian (latviešu) dictionary for the aspell spell checker.

%package -n aspell-mg
Version:        20040807
Release:        0
Summary:        Malagasy Dictionary for Aspell
License:        GPL-2.0-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:mg)

%description -n aspell-mg
A Malagasy dictionary for the aspell spell checker.

%package -n aspell-mi
Version:        0.50
Release:        0
Summary:        Maori (Māori) Dictionary for Aspell
License:        LGPL-2.1-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:mi)

%description -n aspell-mi
A Maori (Māori) dictionary for the aspell spell checker.

%package -n aspell-mk
Version:        0.50
Release:        0
Summary:        Macedonian (македонски) Dictionary for Aspell
License:        GPL-2.0-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:mk)

%description -n aspell-mk
A Macedonian (македонски) dictionary for the aspell spell checker.

%package -n aspell-ml
Version:        0.03
Release:        0
Summary:        Malayalam (മലയാളം) Dictionary for Aspell
License:        GPL-3.0-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:ml)

%description -n aspell-ml
A Malayalam (മലയാളം) dictionary for the aspell spell checker.

%package -n aspell-mn
Version:        0.06.2
Release:        0
Summary:        Mongolian (Монгол) Dictionary for Aspell
License:        GPL-2.0-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:mn)

%description -n aspell-mn
A Mongolian (Монгол) dictionary for the aspell spell checker.

%package -n aspell-mr
Version:        0.10
Release:        0
Summary:        Marathi (मराठी) Dictionary for Aspell
License:        GPL-2.0-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:mr)
# u-deva.cmap and u-deva.cset files are also provided by aspell-hi
Conflicts:      aspell-hi

%description -n aspell-mr
A Marathi (मराठी) dictionary for the aspell spell checker.

%package -n aspell-ms
Version:        0.50
Release:        0
Summary:        Malay (bahasa Melayu, بهاس ملايو‎) Dictionary for Aspell
License:        GFDL-1.2-only
Group:          Productivity/Text/Spell
Provides:       locale(aspell:ms)

%description -n aspell-ms
A Malay (bahasa Melayu, بهاس ملايو‎) dictionary for the aspell spell checker.

%package -n aspell-mt
Version:        0.50
Release:        0
Summary:        Maltese (Malti) Dictionary for Aspell
License:        LGPL-2.1-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:mt)

%description -n aspell-mt
A Maltese (Malti) dictionary for the aspell spell checker.

%package -n aspell-nb
Version:        0.50.10
Release:        0
Summary:        Norwegian Bokmaal (Norsk bokmål) Dictionary for Aspell
License:        GPL-2.0-or-later
Group:          Productivity/Text/Spell
Provides:       aspell-no
Provides:       locale(aspell:nb)
Obsoletes:      aspell-no

%description -n aspell-nb
A Norwegian Bokmaal (Norsk bokmål) dictionary for the aspell spell checker.

%package -n aspell-nds
Version:        0.01
Release:        0
Summary:        Low Saxon (Plattdüütsch) Dictionary for Aspell
License:        LGPL-2.1-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:nds)

%description -n aspell-nds
A Low Saxon (Plattdüütsch) dictionary for the aspell spell checker.

%package -n aspell-nl
Version:        1.00.7
Release:        0
Summary:        Dutch (Nederlands) Dictionary for Aspell
License:        LGPL-2.1-or-later
Group:          Productivity/Text/Spell
URL:            http://www.opentaal.org
Provides:       locale(aspell:nl)

%description -n aspell-nl
A Dutch (Nederlands) dictionary for the aspell spell checker.

%package -n aspell-nn
Version:        0.50.11
Release:        0
Summary:        Norwegian Nynorsk (Norsk nynorsk) Dictionary for Aspell
License:        GPL-2.0-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:nn)

%description -n aspell-nn
A Norwegian Nynorsk (Norsk nynorsk) dictionary for the aspell spell checker.

%package -n aspell-ny
Version:        0.01
Release:        0
Summary:        Chichewa Dictionary for Aspell
License:        GPL-2.0-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:ny)

%description -n aspell-ny
A Chichewa dictionary for the aspell spell checker.

%package -n aspell-or
Version:        0.03
Release:        0
Summary:        Oriya (ଓଡ଼ିଆ) Dictionary for Aspell
License:        GPL-2.0-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:or)

%description -n aspell-or
An Oriya (ଓଡ଼ିଆ) dictionary for the aspell spell checker.

%package -n aspell-pa
Version:        0.01
Release:        0
Summary:        Punjabi (ਪੰਜਾਬੀ, پنجابی‎) Dictionary for Aspell
License:        GPL-2.0-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:pa)

%description -n aspell-pa
A Punjabi (ਪੰਜਾਬੀ, پنجابی‎) dictionary for the aspell spell checker.

%package -n aspell-pl
Version:        0.60.2015.04.28
Release:        0
Summary:        Polish (polszczyzna) Dictionary for Aspell
License:        CC-BY-SA-1.0 AND GPL-2.0-only AND LGPL-2.1-only AND MPL-1.1
Group:          Productivity/Text/Spell
URL:            http://www.sjp.pl/slownik/en/
Provides:       locale(aspell:pl)

%description -n aspell-pl
A Polish (polszczyzna) dictionary for the aspell spell checker.

%package -n aspell-pt_BR
Version:        20131030.12.0
Release:        0
Summary:        Brazilian Portuguese (Português brasileira) Dictionary for Aspell
License:        LGPL-2.1-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:pt_BR)

%description -n aspell-pt_BR
A Brazilian Portuguese (Português brasileira) dictionary for the aspell spell checker.

%package -n aspell-pt_PT
Version:        20190329
Release:        0
Summary:        Portuguese (Português) Dictionary for Aspell
License:        GPL-2.0-or-later
Group:          Productivity/Text/Spell
URL:            http://natura.di.uminho.pt/download/sources/Dictionaries/aspell6/
Provides:       locale(aspell:pt)

%description -n aspell-pt_PT
A Portuguese (Português) dictionary for the aspell spell checker.

%package -n aspell-qu
Version:        0.02
Release:        0
Summary:        Quechua (Runasimi (qheshwa)) Dictionary for Aspell
License:        GPL-2.0-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:qu)

%description -n aspell-qu
A Quechua (Runasimi (qheshwa)) dictionary for the aspell spell checker.

%package -n aspell-ro
Version:        3.3.2
Release:        0
Summary:        Romanian (română) Dictionary for Aspell
License:        GPL-2.0-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:ro)

%description -n aspell-ro
A Romanian (română) dictionary for the aspell spell checker.

%package -n aspell-ru
Version:        0.99.f7.1
Release:        0
Summary:        Russian (русский) Dictionary for Aspell
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND SUSE-Permissive-Modify-By-Patch
Group:          Productivity/Text/Spell
Provides:       locale(aspell:ru)

%description -n aspell-ru
A Russian  (русский) dictionary for the aspell spell checker.

%package -n aspell-rw
Version:        0.50
Release:        0
Summary:        Kinyarwanda (Ikinyarwanda) Dictionary for Aspell
License:        GPL-2.0-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:rw)

%description -n aspell-rw
A Kinyarwanda (Ikinyarwanda) dictionary for the aspell spell checker.

%package -n aspell-sc
Version:        1.0
Release:        0
Summary:        Sardinian (Sardu) Dictionary for Aspell
License:        GPL-2.0-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:sc)

%description -n aspell-sc
A Sardinian (Sardu) dictionary for the aspell spell checker.

%package -n aspell-sk
Version:        2.01
Release:        0
Summary:        Slovak (slovenský) Dictionary for Aspell
License:        GPL-2.0-only OR LGPL-2.1-only OR MPL-1.1
Group:          Productivity/Text/Spell
Provides:       locale(aspell:sk)

%description -n aspell-sk
A Slovak (slovenský) dictionary for the aspell spell checker.

%package -n aspell-sl
Version:        0.50
Release:        0
Summary:        Slovenian (slovenski) Dictionary for Aspell
License:        GPL-2.0-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:sl)

%description -n aspell-sl
A Slovenian (slovenski) dictionary for the aspell spell checker.

%package -n aspell-sr
Version:        0.02
Release:        0
Summary:        Serbian (српски) Dictionary for Aspell
License:        LGPL-2.1-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:sr)

%description -n aspell-sr
A Serbian (српски) dictionary for the aspell spell checker.

%package -n aspell-sv
Version:        0.51.0
Release:        0
Summary:        Swedish (Svenska) Dictionary for Aspell
License:        LGPL-2.1-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:sv)
Obsoletes:      aspell-se
Provides:       aspell-se

%description -n aspell-sv
A Swedish (Svenska) dictionary for the aspell spell checker.

%package -n aspell-sw
#wrong version, should be 0.50-0
Version:        1.0
Release:        0
Summary:        Swahili (Kiswahili) Dictionary for Aspell
License:        LGPL-2.1-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:sw)

%description -n aspell-sw
A Swahili (Kiswahili) dictionary for the aspell spell checker.

%package -n aspell-ta
Version:        20040424
Release:        0
Summary:        Tamil (தமிழ்) Dictionary for Aspell
License:        GPL-2.0-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:ta)

%description -n aspell-ta
A Tamil (தமிழ்) dictionary for the aspell spell checker.

%package -n aspell-te
Version:        0.01.2
Release:        0
Summary:        Telugu (తెలుగు) Dictionary for Aspell
License:        GPL-2.0-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:te)

%description -n aspell-te
A Telugu (తెలుగు) dictionary for the aspell spell checker.

%package -n aspell-tet
Version:        0.1.1
Release:        0
Summary:        Tetum (Tetun) Dictionary for Aspell
License:        GPL-2.0-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:tet)

%description -n aspell-tet
A Tetum (Tetun) dictionary for the aspell spell checker.

%package -n aspell-tk
Version:        0.01
Release:        0
Summary:        Turkmen (Türkmençe) Dictionary for Aspell
License:        GPL-2.0-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:tk)

%description -n aspell-tk
A Turkmen (Türkmençe) dictionary for the aspell spell checker.

%package -n aspell-tl
Version:        0.02
Release:        0
Summary:        Tagalog Dictionary for Aspell
License:        GPL-2.0-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:tl)

%description -n aspell-tl
A Tagalog dictionary for the aspell spell checker.

%package -n aspell-tn
Version:        1.0.1
Release:        0
Summary:        Setswana Dictionary for Aspell
License:        GPL-2.0-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:tn)

%description -n aspell-tn
A Setswana dictionary for the aspell spell checker.

%package -n aspell-tr
Version:        0.50
Release:        0
Summary:        Turkish (Türkçe) Dictionary for Aspell
License:        GPL-2.0-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:tr)

%description -n aspell-tr
A Turkish (Türkçe) dictionary for the aspell spell checker.

%package -n aspell-uk
Version:        1.4.0
Release:        0
Summary:        Ukrainian (українська) Dictionary for Aspell
License:        GPL-2.0-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:uk)

%description -n aspell-uk
An Ukrainian (українська) dictionary for the aspell spell checker.

%package -n aspell-uz
Version:        0.6.0
Release:        0
Summary:        Uzbek (Ўзбекча) Dictionary for Aspell
License:        GPL-2.0-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:uz)

%description -n aspell-uz
An Uzbek (Ўзбекча) dictionary for the aspell spell checker.

%package -n aspell-vi
Version:        0.01.1
Release:        0
Summary:        Vietnamese (Tiếng Việt) Dictionary for Aspell
License:        GPL-2.0-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:vi)

%description -n aspell-vi
A Vietnamese (Tiếng Việt) dictionary for the aspell spell checker.

%package -n aspell-wa
Version:        0.50
Release:        0
Summary:        Walloon (walon) Dictionary for Aspell
License:        GPL-2.0-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:wa)

%description -n aspell-wa
A Walloon (walon) Dictionarydictionary for the aspell spell checker.

%package -n aspell-yi
Version:        0.01.1
Release:        0
Summary:        Yiddish (ייִדיש) Dictionary for Aspell
License:        GPL-2.0-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:yi)

%description -n aspell-yi
A Yiddish (ייִדיש) dictionary for the aspell spell checker.

%package -n aspell-zu
Version:        0.50
Release:        0
Summary:        Zulu (isiZulu) Dictionary Package for Aspell
License:        LGPL-2.1-or-later
Group:          Productivity/Text/Spell
Provides:       locale(aspell:zu)

%description -n aspell-zu
A Zulu (isiZulu) dictionary for the aspell spell checker.

%prep
%setup -q -c -n aspell-dictionaries -a0 -a1 -a2 -a3 -a4 -a5 -a6 -a7 -a8 -a9 -a10 -a11 -a12 -a13 -a14 -a15 -a16 -a17 -a18 -a19 -a20 -a21 -a22 -a23 -a24 -a25 -a26 -a27 -a28 -a29 -a30 -a31 -a32 -a33 -a34 -a35 -a36 -a37 -a38 -a39 -a40 -a41 -a42 -a43 -a44 -a45 -a46 -a47 -a48 -a49 -a50 -a51 -a52 -a54 -a55 -a56 -a57 -a58 -a59 -a60 -a61 -a62 -a63 -a64 -a65 -a66 -a67 -a68 -a69 -a70 -a71 -a72 -a73 -a74 -a75 -a76 -a77 -a78 -a79 -a80 -a81 -a82 -a83 -a84 -a85 -a86 -a87 -a88 -a89 -a90
#
find -name "*~" -type f | xargs -r rm -v
#
mv aspell-cs-20040614-1/doc/README.orig aspell-cs-20040614-1/doc/README.cs
#%%patch -P 0
# Fix "wrong-file-end-of-line-encoding" rpmlint warning
sed -i 's/\r$//' aspell-ia-*/doc/README_ia.txt
sed -i 's/\r$//' aspell-it-*/doc/README.txt
sed -i 's/\r$//' aspell-lv-*/doc/changelog.txt
sed -i 's/\r$//' aspell-lv-*/doc/version.txt
sed -i 's/\r$//' aspell-mk-*/Copyright
sed -i 's/\r$//' aspell-sc-*/doc/gpl_it.txt

%build
cd aspell-da-*
./configure
cd ..
for lang in %{dict_langs} ; do
  (
    cd aspell*-$lang-*
    ./configure
    make
  ) || true
done

%install
#
%if "%{aspell_dict_dir}" != "%{aspell_data_dir}"
ASPELL_DICT_DIRS="%{aspell_dict_dir} %{aspell_data_dir}"
%else
ASPELL_DICT_DIRS="%{aspell_dict_dir}"
%endif
#
# install data files
for lang in %{dict_langs} ; do
  (
    cd aspell*-$lang-*
    make DESTDIR=%{buildroot} install
  ) || true
  #
  # create file list and save data files to another directory
  rm -f files-$lang.orig
  for data_dir in $ASPELL_DICT_DIRS ; do
    find %{buildroot}${data_dir}/* >>files-$lang.orig
    mkdir -p %{buildroot}${data_dir}-${lang}
    mv %{buildroot}${data_dir}/* %{buildroot}${data_dir}-${lang}/
  done
  sed "s|%{buildroot}||" files-$lang.orig >files-$lang
done
#
# copy all saved data files back to valid destination
for lang in %{dict_langs} ; do
  for data_dir in $ASPELL_DICT_DIRS ; do
    mv %{buildroot}${data_dir}-${lang}/* %{buildroot}${data_dir}/
    rmdir %{buildroot}${data_dir}-${lang}/
  done
done
#
# documentation
for lang in %{dict_langs} ; do
  install -m 755 -d %{buildroot}%{_defaultdocdir}/aspell-$lang/
  (
    cd aspell*-$lang-*
    install -m 644 COPYING Copyright README %{buildroot}%{_defaultdocdir}/aspell-$lang
    if [ -d doc ] ; then
      install -m 755 -d %{buildroot}%{_defaultdocdir}/aspell-$lang/doc
      install -m 644 doc/* %{buildroot}%{_defaultdocdir}/aspell-$lang/doc
    fi
  ) || true
done
# installing extra dictionaries with Novell jargon; bug #371
# no need to add this for ja CN_*. The spell checking is unusable for these languages
pwd
for lang in de es fr it pt_BR hu cs pl ru fi da nb sv nl sk ; do
(
  cd aspell-$lang-*
  install -m 644 ./"$lang"Novellwords %{buildroot}/%{aspell_dict_dir}/
) || true
done
#
rm %{buildroot}%{_docdir}/aspell-ta/doc/tamil.txt
# Fix "zero-length" rpmlint warning
rm -f %{buildroot}%{_defaultdocdir}/aspell-ast/Copyright
rm -f %{buildroot}%{_defaultdocdir}/aspell-ms/doc/ms_MY.aff
# Fix "install-file-in-docs" rpmlint warning
rm -f %{buildroot}%{_defaultdocdir}/aspell-br/doc/INSTALL
# Fix "waste of space" warnings
%fdupes -s %{buildroot}%{_libdir}
%fdupes -s %{buildroot}%{_datadir}

%files -n aspell-af -f files-af
%doc %{_defaultdocdir}/aspell-af

%files -n aspell-agal -f files-agal
%doc %{_defaultdocdir}/aspell-agal

%files -n aspell-ar -f files-ar
%doc %{_defaultdocdir}/aspell-ar

%files -n aspell-ast -f files-ast
%doc %{_defaultdocdir}/aspell-ast

%files -n aspell-az -f files-az
%doc %{_defaultdocdir}/aspell-az

%files -n aspell-bg -f files-bg
%doc %{_defaultdocdir}/aspell-bg

%files -n aspell-br -f files-br
%doc %{_defaultdocdir}/aspell-br

%files -n aspell-ca -f files-ca
%doc %{_defaultdocdir}/aspell-ca

%files -n aspell-cy -f files-cy
%doc %{_defaultdocdir}/aspell-cy

%files -n aspell-da -f files-da
%doc %{_defaultdocdir}/aspell-da

%files -n aspell-de -f files-de
%doc %{_defaultdocdir}/aspell-de

%files -n aspell-el -f files-el
%doc %{_defaultdocdir}/aspell-el

%files -n aspell-eo -f files-eo
%doc %{_defaultdocdir}/aspell-eo

%files -n aspell-es -f files-es
%doc %{_defaultdocdir}/aspell-es

%files -n aspell-fo -f files-fo
%doc %{_defaultdocdir}/aspell-fo

%files -n aspell-fr -f files-fr
%doc %{_defaultdocdir}/aspell-fr

%files -n aspell-fy -f files-fy
%doc %{_defaultdocdir}/aspell-fy

%files -n aspell-ga -f files-ga
%doc %{_defaultdocdir}/aspell-ga

%files -n aspell-hr -f files-hr
%doc %{_defaultdocdir}/aspell-hr

%files -n aspell-is -f files-is
%doc %{_defaultdocdir}/aspell-is

%files -n aspell-it -f files-it
%doc %{_defaultdocdir}/aspell-it

%files -n aspell-mt -f files-mt
%doc %{_defaultdocdir}/aspell-mt

%files -n aspell-nb -f files-nb
%doc %{_defaultdocdir}/aspell-nb

%files -n aspell-nn -f files-nn
%doc %{_defaultdocdir}/aspell-nn

%files -n aspell-pl -f files-pl
%doc %{_defaultdocdir}/aspell-pl

%files -n aspell-pt_PT -f files-pt_PT
%doc %{_defaultdocdir}/aspell-pt_PT

%files -n aspell-pt_BR -f files-pt_BR
%doc %{_defaultdocdir}/aspell-pt_BR

%files -n aspell-ro -f files-ro
%doc %{_defaultdocdir}/aspell-ro

%files -n aspell-ru -f files-ru
%doc %{_defaultdocdir}/aspell-ru

%files -n aspell-sk -f files-sk
%doc %{_defaultdocdir}/aspell-sk

%files -n aspell-sr -f files-sr
%doc %{_defaultdocdir}/aspell-sr

%files -n aspell-sv -f files-sv
%doc %{_defaultdocdir}/aspell-sv

%files -n aspell-uk -f files-uk
%doc %{_defaultdocdir}/aspell-uk

%files -n aspell-am -f files-am
%doc %{_defaultdocdir}/aspell-am

%files -n aspell-be -f files-be
%doc %{_defaultdocdir}/aspell-be

%files -n aspell-bn -f files-bn
%doc %{_defaultdocdir}/aspell-bn

%files -n aspell-csb -f files-csb
%doc %{_defaultdocdir}/aspell-csb

%files -n aspell-et -f files-et
%doc %{_defaultdocdir}/aspell-et

%files -n aspell-fa -f files-fa
%doc %{_defaultdocdir}/aspell-fa

%files -n aspell-he -f files-he
%doc %{_defaultdocdir}/aspell-he

%files -n aspell-fi -f files-fi
%doc %{_defaultdocdir}/aspell-fi

%files -n aspell-gd -f files-gd
%doc %{_defaultdocdir}/aspell-gd

%files -n aspell-gl -f files-gl
%doc %{_defaultdocdir}/aspell-gl

%files -n aspell-grc -f files-grc
%doc %{_defaultdocdir}/aspell-grc

%files -n aspell-gv -f files-gv
%doc %{_defaultdocdir}/aspell-gv

%files -n aspell-hi -f files-hi
%doc %{_defaultdocdir}/aspell-hi

%files -n aspell-hil -f files-hil
%doc %{_defaultdocdir}/aspell-hil

%files -n aspell-hsb -f files-hsb
%doc %{_defaultdocdir}/aspell-hsb

%files -n aspell-hu -f files-hu
%doc %{_defaultdocdir}/aspell-hu

%files -n aspell-hus -f files-hus
%doc %{_defaultdocdir}/aspell-hus

%files -n aspell-ia -f files-ia
%doc %{_defaultdocdir}/aspell-ia

%files -n aspell-id -f files-id
%doc %{_defaultdocdir}/aspell-id

%files -n aspell-kn -f files-kn
%doc %{_defaultdocdir}/aspell-kn

%files -n aspell-ku -f files-ku
%doc %{_defaultdocdir}/aspell-ku

%files -n aspell-ky -f files-ky
%doc %{_defaultdocdir}/aspell-ky

%files -n aspell-la -f files-la
%doc %{_defaultdocdir}/aspell-la

%files -n aspell-lt -f files-lt
%doc %{_defaultdocdir}/aspell-lt

%files -n aspell-lv -f files-lv
%doc %{_defaultdocdir}/aspell-lv

%files -n aspell-mg -f files-mg
%doc %{_defaultdocdir}/aspell-mg

%files -n aspell-mi -f files-mi
%doc %{_defaultdocdir}/aspell-mi

%files -n aspell-mk -f files-mk
%doc %{_defaultdocdir}/aspell-mk

%files -n aspell-ml -f files-ml
%doc %{_defaultdocdir}/aspell-ml

%files -n aspell-mn -f files-mn
%doc %{_defaultdocdir}/aspell-mn

%files -n aspell-mr -f files-mr
%doc %{_defaultdocdir}/aspell-mr

%files -n aspell-ms -f files-ms
%doc %{_defaultdocdir}/aspell-ms

%files -n aspell-ny -f files-ny
%doc %{_defaultdocdir}/aspell-ny

%files -n aspell-or -f files-or
%doc %{_defaultdocdir}/aspell-or

%files -n aspell-pa -f files-pa
%doc %{_defaultdocdir}/aspell-pa

%files -n aspell-qu -f files-qu
%doc %{_defaultdocdir}/aspell-qu

%files -n aspell-rw -f files-rw
%doc %{_defaultdocdir}/aspell-rw

%files -n aspell-sl -f files-sl
%doc %{_defaultdocdir}/aspell-sl

%files -n aspell-sc -f files-sc
%doc %{_defaultdocdir}/aspell-sc

%files -n aspell-sw -f files-sw
%doc %{_defaultdocdir}/aspell-sw

%files -n aspell-ta -f files-ta
%doc %{_defaultdocdir}/aspell-ta

%files -n aspell-tet -f files-tet
%doc %{_defaultdocdir}/aspell-tet

%files -n aspell-tk -f files-tk
%doc %{_defaultdocdir}/aspell-tk

%files -n aspell-tl -f files-tl
%doc %{_defaultdocdir}/aspell-tl

%files -n aspell-tn -f files-tn
%doc %{_defaultdocdir}/aspell-tn

%files -n aspell-tr -f files-tr
%doc %{_defaultdocdir}/aspell-tr

%files -n aspell-uz -f files-uz
%doc %{_defaultdocdir}/aspell-uz

%files -n aspell-vi -f files-vi
%doc %{_defaultdocdir}/aspell-vi

%files -n aspell-wa -f files-wa
%doc %{_defaultdocdir}/aspell-wa

%files -n aspell-yi -f files-yi
%doc %{_defaultdocdir}/aspell-yi

%files -n aspell-zu -f files-zu
%doc %{_defaultdocdir}/aspell-zu

%files -n aspell-nl -f files-nl
%dir %{_defaultdocdir}/aspell-nl
%doc %{_defaultdocdir}/aspell-nl/*

%files -n aspell-gu -f files-gu
%doc %{_defaultdocdir}/aspell-gu

%files -n aspell-hy -f files-hy
%doc %{_defaultdocdir}/aspell-hy

%files -n aspell-nds -f files-nds
%doc %{_defaultdocdir}/aspell-nds
#conflicting files with aspell package
%exclude %{aspell_data_dir}/iso-8859-15.cmap
%exclude %{aspell_data_dir}/iso-8859-15.cset

%files -n aspell-cs -f files-cs
%dir %{_defaultdocdir}/aspell-cs
%doc %{_defaultdocdir}/aspell-cs/*

%files -n aspell-te -f files-te
%doc %{_defaultdocdir}/aspell-te

%changelog
