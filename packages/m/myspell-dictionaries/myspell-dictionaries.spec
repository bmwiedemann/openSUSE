#
# spec file for package myspell-dictionaries
#
# Copyright (c) 2020 SUSE LLC
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


###################################################################
## DO NOT EDIT THIS SPEC FILE
## Generate: sh update.sh
###################################################################
Name:           myspell-dictionaries
Version:        20201005
Release:        0
Summary:        A Source Package for Dictionaries Used by MySpell
License:        AGPL-3.0-only AND BSD-2-Clause AND BSD-3-Clause AND BSD-4-Clause AND CC-BY-SA-1.0 AND CC-BY-SA-3.0 AND GFDL-1.1-only AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND GPL-3.0-or-later AND LGPL-2.0-only AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND LGPL-3.0-or-later AND MPL-1.1
URL:            https://cgit.freedesktop.org/libreoffice/dictionaries/
Source0:        dictionaries.tar.xz
Source1:        update.sh
Source2:        myspell-dictionaries.spec.in
BuildRequires:  dos2unix
BuildRequires:  xz
Obsoletes:      libreoffice-hyphen
Obsoletes:      libreoffice-thesaurus-bg
Obsoletes:      libreoffice-thesaurus-ca
Obsoletes:      libreoffice-thesaurus-cs
Obsoletes:      libreoffice-thesaurus-da
Obsoletes:      libreoffice-thesaurus-de
Obsoletes:      libreoffice-thesaurus-de-AT
Obsoletes:      libreoffice-thesaurus-de-CH
Obsoletes:      libreoffice-thesaurus-el
Obsoletes:      libreoffice-thesaurus-en-AU
Obsoletes:      libreoffice-thesaurus-en-GB
Obsoletes:      libreoffice-thesaurus-en-US
Obsoletes:      libreoffice-thesaurus-es
Obsoletes:      libreoffice-thesaurus-es-AR
Obsoletes:      libreoffice-thesaurus-es-VE
Obsoletes:      libreoffice-thesaurus-fr
Obsoletes:      libreoffice-thesaurus-ga
Obsoletes:      libreoffice-thesaurus-hu
Obsoletes:      libreoffice-thesaurus-it
Obsoletes:      libreoffice-thesaurus-nb
Obsoletes:      libreoffice-thesaurus-ne
Obsoletes:      libreoffice-thesaurus-pl
Obsoletes:      libreoffice-thesaurus-pt
Obsoletes:      libreoffice-thesaurus-ro
Obsoletes:      libreoffice-thesaurus-ru
Obsoletes:      libreoffice-thesaurus-sk
Obsoletes:      libreoffice-thesaurus-sl
Obsoletes:      libreoffice-thesaurus-sv
Obsoletes:      myspell-african
Obsoletes:      myspell-albanian
Obsoletes:      myspell-armenian
Obsoletes:      myspell-assamese
Obsoletes:      myspell-asturian
Obsoletes:      myspell-chichewa
Obsoletes:      myspell-coptic
Obsoletes:      myspell-esperanto
Obsoletes:      myspell-faroese
Obsoletes:      myspell-friulian
Obsoletes:      myspell-gaelic-scots
Obsoletes:      myspell-haitian
Obsoletes:      myspell-indonese
Obsoletes:      myspell-irish
Obsoletes:      myspell-kazakh
Obsoletes:      myspell-khmer
Obsoletes:      myspell-kichwa
Obsoletes:      myspell-kikuyu
Obsoletes:      myspell-kinyarwanda
Obsoletes:      myspell-korean
Obsoletes:      myspell-kurdish
Obsoletes:      myspell-latin
Obsoletes:      myspell-lower-sorbian
Obsoletes:      myspell-macedonian
Obsoletes:      myspell-maithili
Obsoletes:      myspell-malagasy
Obsoletes:      myspell-malay
Obsoletes:      myspell-malayalam
Obsoletes:      myspell-maory
Obsoletes:      myspell-marathi
Obsoletes:      myspell-ndebele
Obsoletes:      myspell-new-zealand
Obsoletes:      myspell-persian
Obsoletes:      myspell-setswana
Obsoletes:      myspell-sotho-northern
Obsoletes:      myspell-swati
Obsoletes:      myspell-swedish-finland
Obsoletes:      myspell-tagalog
Obsoletes:      myspell-tsonga
Obsoletes:      myspell-venda
Obsoletes:      myspell-welsh
Obsoletes:      myspell-xhosa
Obsoletes:      myspell-yiddish

%description
This source package contains dictionaries for MySpell.

The MySpell spell-checker is used by the Libreoffice office suite,
the Mozilla Composer, and the Mozilla Mail message composition window.

%package -n myspell-af_NA
Summary:        MySpell af_NA Dictionary
Requires:       myspell-af_ZA
Requires:       myspell-dictionaries
Provides:       myspell-dictionary
Provides:       locale(libreoffice:af_NA)
Provides:       locale(seamonkey-spellchecker:af_NA)
BuildArch:      noarch

%description -n myspell-af_NA
Afrikaans spelling dictionary, and hyphenation rules.

%package -n myspell-af_ZA
Summary:        MySpell af_ZA Dictionary
Requires:       myspell-dictionaries
Provides:       myspell-african
Provides:       myspell-dictionary
Provides:       locale(libreoffice:af_ZA)
Provides:       locale(seamonkey-spellchecker:af_ZA)
BuildArch:      noarch

%description -n myspell-af_ZA
Afrikaans spelling dictionary, and hyphenation rules.

%package -n myspell-an
Summary:        MySpell an Dictionary
Requires:       myspell-an_ES
Requires:       myspell-dictionaries
Provides:       myspell-dictionary
Provides:       locale(libreoffice:an)
Provides:       locale(seamonkey-spellchecker:an)
BuildArch:      noarch

%description -n myspell-an
Aragonese spelling dictionary.

%package -n myspell-an_ES
Summary:        MySpell an_ES Dictionary
Requires:       myspell-dictionaries
Provides:       myspell-dictionary
Provides:       locale(libreoffice:an_ES)
Provides:       locale(seamonkey-spellchecker:an_ES)
BuildArch:      noarch

%description -n myspell-an_ES
Aragonese spelling dictionary.

%package -n myspell-ar_IQ
Summary:        MySpell ar_IQ Dictionary
Requires:       myspell-ar
Requires:       myspell-dictionaries
Provides:       myspell-dictionary
Provides:       locale(libreoffice:ar_IQ)
Provides:       locale(seamonkey-spellchecker:ar_IQ)
BuildArch:      noarch

%description -n myspell-ar_IQ
Arabic spelling dictionary, and thesaurus Ayaspell.

%package -n myspell-ar_QA
Summary:        MySpell ar_QA Dictionary
Requires:       myspell-ar
Requires:       myspell-dictionaries
Provides:       myspell-dictionary
Provides:       locale(libreoffice:ar_QA)
Provides:       locale(seamonkey-spellchecker:ar_QA)
BuildArch:      noarch

%description -n myspell-ar_QA
Arabic spelling dictionary, and thesaurus Ayaspell.

%package -n myspell-ar_EG
Summary:        MySpell ar_EG Dictionary
Requires:       myspell-ar
Requires:       myspell-dictionaries
Provides:       myspell-dictionary
Provides:       locale(libreoffice:ar_EG)
Provides:       locale(seamonkey-spellchecker:ar_EG)
BuildArch:      noarch

%description -n myspell-ar_EG
Arabic spelling dictionary, and thesaurus Ayaspell.

%package -n myspell-ar
Summary:        MySpell ar Dictionary
Requires:       myspell-dictionaries
Provides:       myspell-arabic
Provides:       myspell-dictionary
Provides:       locale(libreoffice:ar)
Provides:       locale(seamonkey-spellchecker:ar)
BuildArch:      noarch

%description -n myspell-ar
Arabic spelling dictionary, and thesaurus Ayaspell.

%package -n myspell-ar_DZ
Summary:        MySpell ar_DZ Dictionary
Requires:       myspell-ar
Requires:       myspell-dictionaries
Provides:       myspell-dictionary
Provides:       locale(libreoffice:ar_DZ)
Provides:       locale(seamonkey-spellchecker:ar_DZ)
BuildArch:      noarch

%description -n myspell-ar_DZ
Arabic spelling dictionary, and thesaurus Ayaspell.

%package -n myspell-ar_BH
Summary:        MySpell ar_BH Dictionary
Requires:       myspell-ar
Requires:       myspell-dictionaries
Provides:       myspell-dictionary
Provides:       locale(libreoffice:ar_BH)
Provides:       locale(seamonkey-spellchecker:ar_BH)
BuildArch:      noarch

%description -n myspell-ar_BH
Arabic spelling dictionary, and thesaurus Ayaspell.

%package -n myspell-ar_YE
Summary:        MySpell ar_YE Dictionary
Requires:       myspell-ar
Requires:       myspell-dictionaries
Provides:       myspell-dictionary
Provides:       locale(libreoffice:ar_YE)
Provides:       locale(seamonkey-spellchecker:ar_YE)
BuildArch:      noarch

%description -n myspell-ar_YE
Arabic spelling dictionary, and thesaurus Ayaspell.

%package -n myspell-ar_JO
Summary:        MySpell ar_JO Dictionary
Requires:       myspell-ar
Requires:       myspell-dictionaries
Provides:       myspell-dictionary
Provides:       locale(libreoffice:ar_JO)
Provides:       locale(seamonkey-spellchecker:ar_JO)
BuildArch:      noarch

%description -n myspell-ar_JO
Arabic spelling dictionary, and thesaurus Ayaspell.

%package -n myspell-ar_MA
Summary:        MySpell ar_MA Dictionary
Requires:       myspell-ar
Requires:       myspell-dictionaries
Provides:       myspell-dictionary
Provides:       locale(libreoffice:ar_MA)
Provides:       locale(seamonkey-spellchecker:ar_MA)
BuildArch:      noarch

%description -n myspell-ar_MA
Arabic spelling dictionary, and thesaurus Ayaspell.

%package -n myspell-ar_KW
Summary:        MySpell ar_KW Dictionary
Requires:       myspell-ar
Requires:       myspell-dictionaries
Provides:       myspell-dictionary
Provides:       locale(libreoffice:ar_KW)
Provides:       locale(seamonkey-spellchecker:ar_KW)
BuildArch:      noarch

%description -n myspell-ar_KW
Arabic spelling dictionary, and thesaurus Ayaspell.

%package -n myspell-ar_SA
Summary:        MySpell ar_SA Dictionary
Requires:       myspell-ar
Requires:       myspell-dictionaries
Provides:       myspell-dictionary
Provides:       locale(libreoffice:ar_SA)
Provides:       locale(seamonkey-spellchecker:ar_SA)
BuildArch:      noarch

%description -n myspell-ar_SA
Arabic spelling dictionary, and thesaurus Ayaspell.

%package -n myspell-ar_SD
Summary:        MySpell ar_SD Dictionary
Requires:       myspell-ar
Requires:       myspell-dictionaries
Provides:       myspell-dictionary
Provides:       locale(libreoffice:ar_SD)
Provides:       locale(seamonkey-spellchecker:ar_SD)
BuildArch:      noarch

%description -n myspell-ar_SD
Arabic spelling dictionary, and thesaurus Ayaspell.

%package -n myspell-ar_LB
Summary:        MySpell ar_LB Dictionary
Requires:       myspell-ar
Requires:       myspell-dictionaries
Provides:       myspell-dictionary
Provides:       locale(libreoffice:ar_LB)
Provides:       locale(seamonkey-spellchecker:ar_LB)
BuildArch:      noarch

%description -n myspell-ar_LB
Arabic spelling dictionary, and thesaurus Ayaspell.

%package -n myspell-ar_LY
Summary:        MySpell ar_LY Dictionary
Requires:       myspell-ar
Requires:       myspell-dictionaries
Provides:       myspell-dictionary
Provides:       locale(libreoffice:ar_LY)
Provides:       locale(seamonkey-spellchecker:ar_LY)
BuildArch:      noarch

%description -n myspell-ar_LY
Arabic spelling dictionary, and thesaurus Ayaspell.

%package -n myspell-ar_OM
Summary:        MySpell ar_OM Dictionary
Requires:       myspell-ar
Requires:       myspell-dictionaries
Provides:       myspell-dictionary
Provides:       locale(libreoffice:ar_OM)
Provides:       locale(seamonkey-spellchecker:ar_OM)
BuildArch:      noarch

%description -n myspell-ar_OM
Arabic spelling dictionary, and thesaurus Ayaspell.

%package -n myspell-ar_SY
Summary:        MySpell ar_SY Dictionary
Requires:       myspell-ar
Requires:       myspell-dictionaries
Provides:       myspell-dictionary
Provides:       locale(libreoffice:ar_SY)
Provides:       locale(seamonkey-spellchecker:ar_SY)
BuildArch:      noarch

%description -n myspell-ar_SY
Arabic spelling dictionary, and thesaurus Ayaspell.

%package -n myspell-ar_AE
Summary:        MySpell ar_AE Dictionary
Requires:       myspell-ar
Requires:       myspell-dictionaries
Provides:       myspell-dictionary
Provides:       locale(libreoffice:ar_AE)
Provides:       locale(seamonkey-spellchecker:ar_AE)
BuildArch:      noarch

%description -n myspell-ar_AE
Arabic spelling dictionary, and thesaurus Ayaspell.

%package -n myspell-ar_TN
Summary:        MySpell ar_TN Dictionary
Requires:       myspell-ar
Requires:       myspell-dictionaries
Provides:       myspell-dictionary
Provides:       locale(libreoffice:ar_TN)
Provides:       locale(seamonkey-spellchecker:ar_TN)
BuildArch:      noarch

%description -n myspell-ar_TN
Arabic spelling dictionary, and thesaurus Ayaspell.

%package -n myspell-be_BY
Summary:        MySpell be_BY Dictionary
Requires:       myspell-dictionaries
Provides:       myspell-belarusian
Provides:       myspell-dictionary
Provides:       locale(libreoffice:be_BY)
Provides:       locale(seamonkey-spellchecker:be_BY)
BuildArch:      noarch

%description -n myspell-be_BY
Belarusian spelling dictionary and hyphenation.

%package -n myspell-bg_BG
Summary:        MySpell bg_BG Dictionary
Requires:       myspell-dictionaries
Provides:       libreoffice-thesaurus-bg
Provides:       myspell-bulgarian
Provides:       myspell-dictionary
Provides:       locale(libreoffice:bg_BG)
Provides:       locale(seamonkey-spellchecker:bg_BG)
BuildArch:      noarch

%description -n myspell-bg_BG
Bulgarian spelling dictionary, hyphenation rules, and thesaurus.

%package -n myspell-bn_BD
Summary:        MySpell bn_BD Dictionary
Requires:       myspell-dictionaries
Provides:       myspell-bengali
Provides:       myspell-dictionary
Provides:       locale(libreoffice:bn_BD)
Provides:       locale(seamonkey-spellchecker:bn_BD)
BuildArch:      noarch

%description -n myspell-bn_BD
Bengali spelling dictionary.

%package -n myspell-bn_IN
Summary:        MySpell bn_IN Dictionary
Requires:       myspell-bn_BD
Requires:       myspell-dictionaries
Provides:       myspell-dictionary
Provides:       locale(libreoffice:bn_IN)
Provides:       locale(seamonkey-spellchecker:bn_IN)
BuildArch:      noarch

%description -n myspell-bn_IN
Bengali spelling dictionary.

%package -n myspell-bo_IN
Summary:        MySpell bo_IN Dictionary
Requires:       myspell-bo
Requires:       myspell-dictionaries
Provides:       myspell-dictionary
Provides:       locale(libreoffice:bo_IN)
Provides:       locale(seamonkey-spellchecker:bo_IN)
BuildArch:      noarch

%description -n myspell-bo_IN
Classical Tibetan syllable spellchecker for Hunspell.

%package -n myspell-bo_CN
Summary:        MySpell bo_CN Dictionary
Requires:       myspell-bo
Requires:       myspell-dictionaries
Provides:       myspell-dictionary
Provides:       locale(libreoffice:bo_CN)
Provides:       locale(seamonkey-spellchecker:bo_CN)
BuildArch:      noarch

%description -n myspell-bo_CN
Classical Tibetan syllable spellchecker for Hunspell.

%package -n myspell-bo
Summary:        MySpell bo Dictionary
Requires:       myspell-dictionaries
Provides:       myspell-dictionary
Provides:       locale(libreoffice:bo)
Provides:       locale(seamonkey-spellchecker:bo)
BuildArch:      noarch

%description -n myspell-bo
Classical Tibetan syllable spellchecker for Hunspell.

%package -n myspell-br_FR
Summary:        MySpell br_FR Dictionary
Requires:       myspell-dictionaries
Provides:       myspell-breton
Provides:       myspell-dictionary
Provides:       locale(libreoffice:br_FR)
Provides:       locale(seamonkey-spellchecker:br_FR)
BuildArch:      noarch

%description -n myspell-br_FR
Breton spelling dictionary.

%package -n myspell-bs
Summary:        MySpell bs Dictionary
Requires:       myspell-bs_BA
Requires:       myspell-dictionaries
Provides:       myspell-dictionary
Provides:       locale(libreoffice:bs)
Provides:       locale(seamonkey-spellchecker:bs)
BuildArch:      noarch

%description -n myspell-bs
Bosnian spelling dictionary.

%package -n myspell-bs_BA
Summary:        MySpell bs_BA Dictionary
Requires:       myspell-dictionaries
Provides:       myspell-dictionary
Provides:       locale(libreoffice:bs_BA)
Provides:       locale(seamonkey-spellchecker:bs_BA)
BuildArch:      noarch

%description -n myspell-bs_BA
Bosnian spelling dictionary.

%package -n myspell-ca_FR
Summary:        MySpell ca_FR Dictionary
Requires:       myspell-ca
Requires:       myspell-dictionaries
Provides:       myspell-dictionary
Provides:       locale(libreoffice:ca_FR)
Provides:       locale(seamonkey-spellchecker:ca_FR)
BuildArch:      noarch

%description -n myspell-ca_FR
Catalan spelling dictionary, hyphenation rules, and thesaurus.

%package -n myspell-ca_AD
Summary:        MySpell ca_AD Dictionary
Requires:       myspell-ca
Requires:       myspell-dictionaries
Provides:       myspell-dictionary
Provides:       locale(libreoffice:ca_AD)
Provides:       locale(seamonkey-spellchecker:ca_AD)
BuildArch:      noarch

%description -n myspell-ca_AD
Catalan spelling dictionary, hyphenation rules, and thesaurus.

%package -n myspell-ca_IT
Summary:        MySpell ca_IT Dictionary
Requires:       myspell-ca
Requires:       myspell-dictionaries
Provides:       myspell-dictionary
Provides:       locale(libreoffice:ca_IT)
Provides:       locale(seamonkey-spellchecker:ca_IT)
BuildArch:      noarch

%description -n myspell-ca_IT
Catalan spelling dictionary, hyphenation rules, and thesaurus.

%package -n myspell-ca_ES_valencia
Summary:        MySpell ca_ES_valencia Dictionary
Requires:       myspell-ca
Requires:       myspell-dictionaries
Provides:       myspell-dictionary
Provides:       myspell-valencian
Provides:       locale(libreoffice:ca_ES_valencia)
Provides:       locale(seamonkey-spellchecker:ca_ES_valencia)
BuildArch:      noarch

%description -n myspell-ca_ES_valencia
Catalan spelling dictionary, hyphenation rules, and thesaurus.

%package -n myspell-ca
Summary:        MySpell ca Dictionary
Requires:       myspell-dictionaries
Provides:       libreoffice-thesaurus-ca
Provides:       myspell-catalan
Provides:       myspell-dictionary
Provides:       locale(libreoffice:ca)
Provides:       locale(seamonkey-spellchecker:ca)
BuildArch:      noarch

%description -n myspell-ca
Catalan spelling dictionary, hyphenation rules, and thesaurus.

%package -n myspell-ca_ES
Summary:        MySpell ca_ES Dictionary
Requires:       myspell-ca
Requires:       myspell-dictionaries
Provides:       myspell-dictionary
Provides:       locale(libreoffice:ca_ES)
Provides:       locale(seamonkey-spellchecker:ca_ES)
BuildArch:      noarch

%description -n myspell-ca_ES
Catalan spelling dictionary, hyphenation rules, and thesaurus.

%package -n myspell-cs_CZ
Summary:        MySpell cs_CZ Dictionary
Requires:       myspell-dictionaries
Provides:       libreoffice-thesaurus-cs
Provides:       myspell-czech
Provides:       myspell-dictionary
Provides:       locale(libreoffice:cs_CZ)
Provides:       locale(seamonkey-spellchecker:cs_CZ)
BuildArch:      noarch

%description -n myspell-cs_CZ
Czech spell check dictionary, hyphenation rules and thesaurus.

%package -n myspell-da_DK
Summary:        MySpell da_DK Dictionary
Requires:       myspell-dictionaries
Provides:       libreoffice-thesaurus-da
Provides:       myspell-danish
Provides:       myspell-dictionary
Provides:       locale(libreoffice:da_DK)
Provides:       locale(seamonkey-spellchecker:da_DK)
BuildArch:      noarch

%description -n myspell-da_DK
Danish spelling dictionary, hyphenation rules, and thesaurus.

%package -n myspell-de_CH
Summary:        MySpell de_CH Dictionary
Requires:       myspell-de
Requires:       myspell-dictionaries
Provides:       myspell-dictionary
Provides:       myspell-nswiss
Provides:       locale(libreoffice:de_CH)
Provides:       locale(seamonkey-spellchecker:de_CH)
BuildArch:      noarch

%description -n myspell-de_CH
German (Austria, Germany, Switzerland) spelling dictionaries, hyphenation rules, and thesaurus.

%package -n myspell-de
Summary:        MySpell de Dictionary
Requires:       myspell-dictionaries
Recommends:     myspell-de_DE
Provides:       myspell-dictionary
Provides:       locale(libreoffice:de)
Provides:       locale(seamonkey-spellchecker:de)
BuildArch:      noarch

%description -n myspell-de
German (Austria, Germany, Switzerland) spelling dictionaries, hyphenation rules, and thesaurus.

%package -n myspell-de_DE
Summary:        MySpell de_DE Dictionary
Requires:       myspell-de
Requires:       myspell-dictionaries
Provides:       myspell-dictionary
Provides:       myspell-german
Provides:       locale(libreoffice:de_DE)
Provides:       locale(seamonkey-spellchecker:de_DE)
BuildArch:      noarch

%description -n myspell-de_DE
German (Austria, Germany, Switzerland) spelling dictionaries, hyphenation rules, and thesaurus.

%package -n myspell-de_AT
Summary:        MySpell de_AT Dictionary
Requires:       myspell-de
Requires:       myspell-de_DE
Requires:       myspell-dictionaries
Provides:       myspell-austrian
Provides:       myspell-dictionary
Provides:       locale(libreoffice:de_AT)
Provides:       locale(seamonkey-spellchecker:de_AT)
BuildArch:      noarch

%description -n myspell-de_AT
German (Austria, Germany, Switzerland) spelling dictionaries, hyphenation rules, and thesaurus.

%package -n myspell-el_GR
Summary:        MySpell el_GR Dictionary
Requires:       myspell-dictionaries
Provides:       libreoffice-thesaurus-el
Provides:       myspell-dictionary
Provides:       myspell-greek
Provides:       locale(libreoffice:el_GR)
Provides:       locale(seamonkey-spellchecker:el_GR)
BuildArch:      noarch

%description -n myspell-el_GR
Greek spelling dictionary, and hyphenation rules.

%package -n myspell-en_AU
Summary:        MySpell en_AU Dictionary
Requires:       myspell-dictionaries
Requires:       myspell-en
Requires:       myspell-en_GB
Requires:       myspell-en_US
Recommends:     myspell-lightproof-en
Provides:       libreoffice-thesaurus-en-AU
Provides:       myspell-australian
Provides:       myspell-dictionary
Provides:       locale(libreoffice:en_AU)
Provides:       locale(seamonkey-spellchecker:en_AU)
BuildArch:      noarch

%description -n myspell-en_AU
English spelling dictionaries, hyphenation rules, thesaurus, and grammar checker.

%package -n myspell-en_BZ
Summary:        MySpell en_BZ Dictionary
Requires:       myspell-dictionaries
Requires:       myspell-en
Requires:       myspell-en_GB
Requires:       myspell-en_US
Recommends:     myspell-lightproof-en
Provides:       myspell-dictionary
Provides:       locale(libreoffice:en_BZ)
Provides:       locale(seamonkey-spellchecker:en_BZ)
BuildArch:      noarch

%description -n myspell-en_BZ
English spelling dictionaries, hyphenation rules, thesaurus, and grammar checker.

%package -n myspell-en_JM
Summary:        MySpell en_JM Dictionary
Requires:       myspell-dictionaries
Requires:       myspell-en
Requires:       myspell-en_GB
Requires:       myspell-en_US
Recommends:     myspell-lightproof-en
Provides:       myspell-dictionary
Provides:       locale(libreoffice:en_JM)
Provides:       locale(seamonkey-spellchecker:en_JM)
BuildArch:      noarch

%description -n myspell-en_JM
English spelling dictionaries, hyphenation rules, thesaurus, and grammar checker.

%package -n myspell-en_CA
Summary:        MySpell en_CA Dictionary
Requires:       myspell-dictionaries
Requires:       myspell-en
Requires:       myspell-en_GB
Requires:       myspell-en_US
Recommends:     myspell-lightproof-en
Provides:       myspell-canadian
Provides:       myspell-dictionary
Provides:       locale(libreoffice:en_CA)
Provides:       locale(seamonkey-spellchecker:en_CA)
BuildArch:      noarch

%description -n myspell-en_CA
English spelling dictionaries, hyphenation rules, thesaurus, and grammar checker.

%package -n myspell-en_BS
Summary:        MySpell en_BS Dictionary
Requires:       myspell-dictionaries
Requires:       myspell-en
Requires:       myspell-en_GB
Requires:       myspell-en_US
Recommends:     myspell-lightproof-en
Provides:       myspell-dictionary
Provides:       locale(libreoffice:en_BS)
Provides:       locale(seamonkey-spellchecker:en_BS)
BuildArch:      noarch

%description -n myspell-en_BS
English spelling dictionaries, hyphenation rules, thesaurus, and grammar checker.

%package -n myspell-en_MW
Summary:        MySpell en_MW Dictionary
Requires:       myspell-dictionaries
Requires:       myspell-en
Requires:       myspell-en_GB
Requires:       myspell-en_US
Requires:       myspell-en_ZA
Recommends:     myspell-lightproof-en
Provides:       myspell-dictionary
Provides:       locale(libreoffice:en_MW)
Provides:       locale(seamonkey-spellchecker:en_MW)
BuildArch:      noarch

%description -n myspell-en_MW
English spelling dictionaries, hyphenation rules, thesaurus, and grammar checker.

%package -n myspell-en_ZW
Summary:        MySpell en_ZW Dictionary
Requires:       myspell-dictionaries
Requires:       myspell-en
Requires:       myspell-en_GB
Requires:       myspell-en_US
Requires:       myspell-en_ZA
Recommends:     myspell-lightproof-en
Provides:       myspell-dictionary
Provides:       locale(libreoffice:en_ZW)
Provides:       locale(seamonkey-spellchecker:en_ZW)
BuildArch:      noarch

%description -n myspell-en_ZW
English spelling dictionaries, hyphenation rules, thesaurus, and grammar checker.

%package -n myspell-en_NZ
Summary:        MySpell en_NZ Dictionary
Requires:       myspell-dictionaries
Requires:       myspell-en
Requires:       myspell-en_GB
Requires:       myspell-en_US
Recommends:     myspell-lightproof-en
Provides:       myspell-dictionary
Provides:       myspell-new-zaeland
Provides:       locale(libreoffice:en_NZ)
Provides:       locale(seamonkey-spellchecker:en_NZ)
BuildArch:      noarch

%description -n myspell-en_NZ
English spelling dictionaries, hyphenation rules, thesaurus, and grammar checker.

%package -n myspell-en_PH
Summary:        MySpell en_PH Dictionary
Requires:       myspell-dictionaries
Requires:       myspell-en
Requires:       myspell-en_US
Recommends:     myspell-lightproof-en
Provides:       myspell-dictionary
Provides:       locale(libreoffice:en_PH)
Provides:       locale(seamonkey-spellchecker:en_PH)
BuildArch:      noarch

%description -n myspell-en_PH
English spelling dictionaries, hyphenation rules, thesaurus, and grammar checker.

%package -n myspell-en_ZA
Summary:        MySpell en_ZA Dictionary
Requires:       myspell-dictionaries
Requires:       myspell-en
Requires:       myspell-en_GB
Requires:       myspell-en_US
Recommends:     myspell-lightproof-en
Provides:       myspell-dictionary
Provides:       myspell-south-african-english
Provides:       locale(libreoffice:en_ZA)
Provides:       locale(seamonkey-spellchecker:en_ZA)
BuildArch:      noarch

%description -n myspell-en_ZA
English spelling dictionaries, hyphenation rules, thesaurus, and grammar checker.

%package -n myspell-en_GH
Summary:        MySpell en_GH Dictionary
Requires:       myspell-dictionaries
Requires:       myspell-en
Requires:       myspell-en_GB
Requires:       myspell-en_US
Recommends:     myspell-lightproof-en
Provides:       myspell-dictionary
Provides:       locale(libreoffice:en_GH)
Provides:       locale(seamonkey-spellchecker:en_GH)
BuildArch:      noarch

%description -n myspell-en_GH
English spelling dictionaries, hyphenation rules, thesaurus, and grammar checker.

%package -n myspell-en_NA
Summary:        MySpell en_NA Dictionary
Requires:       myspell-dictionaries
Requires:       myspell-en
Requires:       myspell-en_GB
Requires:       myspell-en_US
Requires:       myspell-en_ZA
Recommends:     myspell-lightproof-en
Provides:       myspell-dictionary
Provides:       locale(libreoffice:en_NA)
Provides:       locale(seamonkey-spellchecker:en_NA)
BuildArch:      noarch

%description -n myspell-en_NA
English spelling dictionaries, hyphenation rules, thesaurus, and grammar checker.

%package -n myspell-en_GB
Summary:        MySpell en_GB Dictionary
Requires:       myspell-dictionaries
Requires:       myspell-en
Recommends:     myspell-lightproof-en
Provides:       libreoffice-thesaurus-en-GB
Provides:       myspell-british
Provides:       myspell-dictionary
Provides:       locale(libreoffice:en_GB)
Provides:       locale(seamonkey-spellchecker:en_GB)
BuildArch:      noarch

%description -n myspell-en_GB
English spelling dictionaries, hyphenation rules, thesaurus, and grammar checker.

%package -n myspell-en
Summary:        MySpell en Dictionary
Requires:       myspell-dictionaries
Recommends:     myspell-en_US
Recommends:     myspell-lightproof-en
Provides:       myspell-dictionary
Provides:       locale(libreoffice:en)
Provides:       locale(seamonkey-spellchecker:en)
BuildArch:      noarch

%description -n myspell-en
English spelling dictionaries, hyphenation rules, thesaurus, and grammar checker.

%package -n myspell-en_IN
Summary:        MySpell en_IN Dictionary
Requires:       myspell-dictionaries
Requires:       myspell-en
Requires:       myspell-en_GB
Requires:       myspell-en_US
Recommends:     myspell-lightproof-en
Provides:       myspell-dictionary
Provides:       locale(libreoffice:en_IN)
Provides:       locale(seamonkey-spellchecker:en_IN)
BuildArch:      noarch

%description -n myspell-en_IN
English spelling dictionaries, hyphenation rules, thesaurus, and grammar checker.

%package -n myspell-en_IE
Summary:        MySpell en_IE Dictionary
Requires:       myspell-dictionaries
Requires:       myspell-en
Requires:       myspell-en_GB
Requires:       myspell-en_US
Recommends:     myspell-lightproof-en
Provides:       myspell-dictionary
Provides:       locale(libreoffice:en_IE)
Provides:       locale(seamonkey-spellchecker:en_IE)
BuildArch:      noarch

%description -n myspell-en_IE
English spelling dictionaries, hyphenation rules, thesaurus, and grammar checker.

%package -n myspell-en_TT
Summary:        MySpell en_TT Dictionary
Requires:       myspell-dictionaries
Requires:       myspell-en
Requires:       myspell-en_GB
Requires:       myspell-en_US
Recommends:     myspell-lightproof-en
Provides:       myspell-dictionary
Provides:       locale(libreoffice:en_TT)
Provides:       locale(seamonkey-spellchecker:en_TT)
BuildArch:      noarch

%description -n myspell-en_TT
English spelling dictionaries, hyphenation rules, thesaurus, and grammar checker.

%package -n myspell-en_US
Summary:        MySpell en_US Dictionary
Requires:       myspell-dictionaries
Requires:       myspell-en
Recommends:     myspell-lightproof-en
Provides:       libreoffice-thesaurus-US
Provides:       myspell-american
Provides:       myspell-dictionary
Provides:       locale(libreoffice:en_US)
Provides:       locale(seamonkey-spellchecker:en_US)
BuildArch:      noarch

%description -n myspell-en_US
English spelling dictionaries, hyphenation rules, thesaurus, and grammar checker.

%package -n myspell-lightproof-en
Summary:        Lightproof for en
Requires:       myspell-en

%description -n myspell-lightproof-en
Lightproof grammar checker information for en.

%package -n myspell-es_CR
Summary:        MySpell es_CR Dictionary
Requires:       myspell-dictionaries
Requires:       myspell-es
Provides:       myspell-dictionary
Provides:       myspell-spanish-costa-rican
Provides:       locale(libreoffice:es_CR)
Provides:       locale(seamonkey-spellchecker:es_CR)
BuildArch:      noarch

%description -n myspell-es_CR
Spanish spelling dictionary, hyphenation rules, and thesaurus for Spain and Latin America.

%package -n myspell-es_CU
Summary:        MySpell es_CU Dictionary
Requires:       myspell-dictionaries
Requires:       myspell-es
Provides:       myspell-dictionary
Provides:       locale(libreoffice:es_CU)
Provides:       locale(seamonkey-spellchecker:es_CU)
BuildArch:      noarch

%description -n myspell-es_CU
Spanish spelling dictionary, hyphenation rules, and thesaurus for Spain and Latin America.

%package -n myspell-es_MX
Summary:        MySpell es_MX Dictionary
Requires:       myspell-dictionaries
Requires:       myspell-es
Provides:       myspell-dictionary
Provides:       myspell-mexican
Provides:       locale(libreoffice:es_MX)
Provides:       locale(seamonkey-spellchecker:es_MX)
BuildArch:      noarch

%description -n myspell-es_MX
Spanish spelling dictionary, hyphenation rules, and thesaurus for Spain and Latin America.

%package -n myspell-es_PA
Summary:        MySpell es_PA Dictionary
Requires:       myspell-dictionaries
Requires:       myspell-es
Provides:       myspell-dictionary
Provides:       myspell-spanish-panamanian
Provides:       locale(libreoffice:es_PA)
Provides:       locale(seamonkey-spellchecker:es_PA)
BuildArch:      noarch

%description -n myspell-es_PA
Spanish spelling dictionary, hyphenation rules, and thesaurus for Spain and Latin America.

%package -n myspell-es_PE
Summary:        MySpell es_PE Dictionary
Requires:       myspell-dictionaries
Requires:       myspell-es
Provides:       myspell-dictionary
Provides:       myspell-spanish-peruvian
Provides:       locale(libreoffice:es_PE)
Provides:       locale(seamonkey-spellchecker:es_PE)
BuildArch:      noarch

%description -n myspell-es_PE
Spanish spelling dictionary, hyphenation rules, and thesaurus for Spain and Latin America.

%package -n myspell-es_PY
Summary:        MySpell es_PY Dictionary
Requires:       myspell-dictionaries
Requires:       myspell-es
Provides:       myspell-dictionary
Provides:       myspell-spanish-paraguayan
Provides:       locale(libreoffice:es_PY)
Provides:       locale(seamonkey-spellchecker:es_PY)
BuildArch:      noarch

%description -n myspell-es_PY
Spanish spelling dictionary, hyphenation rules, and thesaurus for Spain and Latin America.

%package -n myspell-es_PR
Summary:        MySpell es_PR Dictionary
Requires:       myspell-dictionaries
Requires:       myspell-es
Provides:       myspell-dictionary
Provides:       myspell-spanish-puerto-rican
Provides:       locale(libreoffice:es_PR)
Provides:       locale(seamonkey-spellchecker:es_PR)
BuildArch:      noarch

%description -n myspell-es_PR
Spanish spelling dictionary, hyphenation rules, and thesaurus for Spain and Latin America.

%package -n myspell-es_CL
Summary:        MySpell es_CL Dictionary
Requires:       myspell-dictionaries
Requires:       myspell-es
Provides:       myspell-dictionary
Provides:       myspell-spanish-chilean
Provides:       locale(libreoffice:es_CL)
Provides:       locale(seamonkey-spellchecker:es_CL)
BuildArch:      noarch

%description -n myspell-es_CL
Spanish spelling dictionary, hyphenation rules, and thesaurus for Spain and Latin America.

%package -n myspell-es_CO
Summary:        MySpell es_CO Dictionary
Requires:       myspell-dictionaries
Requires:       myspell-es
Provides:       myspell-dictionary
Provides:       myspell-spanish-colombian
Provides:       locale(libreoffice:es_CO)
Provides:       locale(seamonkey-spellchecker:es_CO)
BuildArch:      noarch

%description -n myspell-es_CO
Spanish spelling dictionary, hyphenation rules, and thesaurus for Spain and Latin America.

%package -n myspell-es_ES
Summary:        MySpell es_ES Dictionary
Requires:       myspell-dictionaries
Requires:       myspell-es
Provides:       myspell-dictionary
Provides:       myspell-spanish
Provides:       locale(libreoffice:es_ES)
Provides:       locale(seamonkey-spellchecker:es_ES)
BuildArch:      noarch

%description -n myspell-es_ES
Spanish spelling dictionary, hyphenation rules, and thesaurus for Spain and Latin America.

%package -n myspell-es_DO
Summary:        MySpell es_DO Dictionary
Requires:       myspell-dictionaries
Requires:       myspell-es
Provides:       myspell-dictionary
Provides:       myspell-spanish-dominican
Provides:       locale(libreoffice:es_DO)
Provides:       locale(seamonkey-spellchecker:es_DO)
BuildArch:      noarch

%description -n myspell-es_DO
Spanish spelling dictionary, hyphenation rules, and thesaurus for Spain and Latin America.

%package -n myspell-es_EC
Summary:        MySpell es_EC Dictionary
Requires:       myspell-dictionaries
Requires:       myspell-es
Provides:       myspell-dictionary
Provides:       myspell-spanish-ecuadorian
Provides:       locale(libreoffice:es_EC)
Provides:       locale(seamonkey-spellchecker:es_EC)
BuildArch:      noarch

%description -n myspell-es_EC
Spanish spelling dictionary, hyphenation rules, and thesaurus for Spain and Latin America.

%package -n myspell-es_NI
Summary:        MySpell es_NI Dictionary
Requires:       myspell-dictionaries
Requires:       myspell-es
Provides:       myspell-dictionary
Provides:       myspell-spanish-nicaraguan
Provides:       locale(libreoffice:es_NI)
Provides:       locale(seamonkey-spellchecker:es_NI)
BuildArch:      noarch

%description -n myspell-es_NI
Spanish spelling dictionary, hyphenation rules, and thesaurus for Spain and Latin America.

%package -n myspell-es_GT
Summary:        MySpell es_GT Dictionary
Requires:       myspell-dictionaries
Requires:       myspell-es
Provides:       myspell-dictionary
Provides:       myspell-spanish-guatemalan
Provides:       locale(libreoffice:es_GT)
Provides:       locale(seamonkey-spellchecker:es_GT)
BuildArch:      noarch

%description -n myspell-es_GT
Spanish spelling dictionary, hyphenation rules, and thesaurus for Spain and Latin America.

%package -n myspell-es_HN
Summary:        MySpell es_HN Dictionary
Requires:       myspell-dictionaries
Requires:       myspell-es
Provides:       myspell-dictionary
Provides:       myspell-spanish-honduran
Provides:       locale(libreoffice:es_HN)
Provides:       locale(seamonkey-spellchecker:es_HN)
BuildArch:      noarch

%description -n myspell-es_HN
Spanish spelling dictionary, hyphenation rules, and thesaurus for Spain and Latin America.

%package -n myspell-es_SV
Summary:        MySpell es_SV Dictionary
Requires:       myspell-dictionaries
Requires:       myspell-es
Provides:       myspell-dictionary
Provides:       myspell-spanish-salvadorean
Provides:       locale(libreoffice:es_SV)
Provides:       locale(seamonkey-spellchecker:es_SV)
BuildArch:      noarch

%description -n myspell-es_SV
Spanish spelling dictionary, hyphenation rules, and thesaurus for Spain and Latin America.

%package -n myspell-es_BO
Summary:        MySpell es_BO Dictionary
Requires:       myspell-dictionaries
Requires:       myspell-es
Provides:       myspell-dictionary
Provides:       myspell-spanish-bolivian
Provides:       locale(libreoffice:es_BO)
Provides:       locale(seamonkey-spellchecker:es_BO)
BuildArch:      noarch

%description -n myspell-es_BO
Spanish spelling dictionary, hyphenation rules, and thesaurus for Spain and Latin America.

%package -n myspell-es_AR
Summary:        MySpell es_AR Dictionary
Requires:       myspell-dictionaries
Requires:       myspell-es
Provides:       myspell-dictionary
Provides:       myspell-spanish-argentine
Provides:       locale(libreoffice:es_AR)
Provides:       locale(seamonkey-spellchecker:es_AR)
BuildArch:      noarch

%description -n myspell-es_AR
Spanish spelling dictionary, hyphenation rules, and thesaurus for Spain and Latin America.

%package -n myspell-es
Summary:        MySpell es Dictionary
Requires:       myspell-dictionaries
Recommends:     myspell-es_ES
Provides:       myspell-dictionary
Provides:       locale(libreoffice:es)
Provides:       locale(seamonkey-spellchecker:es)
BuildArch:      noarch

%description -n myspell-es
Spanish spelling dictionary, hyphenation rules, and thesaurus for Spain and Latin America.

%package -n myspell-es_UY
Summary:        MySpell es_UY Dictionary
Requires:       myspell-dictionaries
Requires:       myspell-es
Provides:       myspell-dictionary
Provides:       myspell-spanish-uruguayan
Provides:       locale(libreoffice:es_UY)
Provides:       locale(seamonkey-spellchecker:es_UY)
BuildArch:      noarch

%description -n myspell-es_UY
Spanish spelling dictionary, hyphenation rules, and thesaurus for Spain and Latin America.

%package -n myspell-es_VE
Summary:        MySpell es_VE Dictionary
Requires:       myspell-dictionaries
Requires:       myspell-es
Provides:       myspell-dictionary
Provides:       myspell-spanish-venezuelan
Provides:       locale(libreoffice:es_VE)
Provides:       locale(seamonkey-spellchecker:es_VE)
BuildArch:      noarch

%description -n myspell-es_VE
Spanish spelling dictionary, hyphenation rules, and thesaurus for Spain and Latin America.

%package -n myspell-et_EE
Summary:        MySpell et_EE Dictionary
Requires:       myspell-dictionaries
Provides:       myspell-dictionary
Provides:       myspell-estonian
Provides:       locale(libreoffice:et_EE)
Provides:       locale(seamonkey-spellchecker:et_EE)
BuildArch:      noarch

%description -n myspell-et_EE
Estonian spelling dictionary, and hyphenation rules.

%package -n myspell-fr_LU
Summary:        MySpell fr_LU Dictionary
Requires:       myspell-dictionaries
Requires:       myspell-fr_FR
Provides:       myspell-dictionary
Provides:       locale(libreoffice:fr_LU)
Provides:       locale(seamonkey-spellchecker:fr_LU)
BuildArch:      noarch

%description -n myspell-fr_LU
French spelling dictionary, hyphenation rules, and thesaurus.

%package -n myspell-fr_BE
Summary:        MySpell fr_BE Dictionary
Requires:       myspell-dictionaries
Requires:       myspell-fr_FR
Provides:       myspell-dictionary
Provides:       locale(libreoffice:fr_BE)
Provides:       locale(seamonkey-spellchecker:fr_BE)
BuildArch:      noarch

%description -n myspell-fr_BE
French spelling dictionary, hyphenation rules, and thesaurus.

%package -n myspell-fr_MC
Summary:        MySpell fr_MC Dictionary
Requires:       myspell-dictionaries
Requires:       myspell-fr_FR
Provides:       myspell-dictionary
Provides:       locale(libreoffice:fr_MC)
Provides:       locale(seamonkey-spellchecker:fr_MC)
BuildArch:      noarch

%description -n myspell-fr_MC
French spelling dictionary, hyphenation rules, and thesaurus.

%package -n myspell-fr_CH
Summary:        MySpell fr_CH Dictionary
Requires:       myspell-dictionaries
Requires:       myspell-fr_FR
Provides:       myspell-dictionary
Provides:       locale(libreoffice:fr_CH)
Provides:       locale(seamonkey-spellchecker:fr_CH)
BuildArch:      noarch

%description -n myspell-fr_CH
French spelling dictionary, hyphenation rules, and thesaurus.

%package -n myspell-fr_CA
Summary:        MySpell fr_CA Dictionary
Requires:       myspell-dictionaries
Requires:       myspell-fr_FR
Provides:       myspell-dictionary
Provides:       locale(libreoffice:fr_CA)
Provides:       locale(seamonkey-spellchecker:fr_CA)
BuildArch:      noarch

%description -n myspell-fr_CA
French spelling dictionary, hyphenation rules, and thesaurus.

%package -n myspell-fr_FR
Summary:        MySpell fr_FR Dictionary
Requires:       myspell-dictionaries
Provides:       libreoffice-thesaurus-fr
Provides:       myspell-dictionary
Provides:       myspell-french
Provides:       locale(libreoffice:fr_FR)
Provides:       locale(seamonkey-spellchecker:fr_FR)
BuildArch:      noarch

%description -n myspell-fr_FR
French spelling dictionary, hyphenation rules, and thesaurus.

%package -n myspell-gd_GB
Summary:        MySpell gd_GB Dictionary
Requires:       myspell-dictionaries
Provides:       myspell-dictionary
Provides:       myspell-gaelic
Provides:       locale(libreoffice:gd_GB)
Provides:       locale(seamonkey-spellchecker:gd_GB)
BuildArch:      noarch

%description -n myspell-gd_GB
Scottish Gaelic spell checker.

%package -n myspell-gl
Summary:        MySpell gl Dictionary
Requires:       myspell-dictionaries
Provides:       myspell-dictionary
Provides:       myspell-galician
Provides:       locale(libreoffice:gl)
Provides:       locale(seamonkey-spellchecker:gl)
BuildArch:      noarch

%description -n myspell-gl
Galician spelling dictionary, hyphenation rules, and thesaurus.

%package -n myspell-gl_ES
Summary:        MySpell gl_ES Dictionary
Requires:       myspell-dictionaries
Requires:       myspell-gl
Provides:       myspell-dictionary
Provides:       locale(libreoffice:gl_ES)
Provides:       locale(seamonkey-spellchecker:gl_ES)
BuildArch:      noarch

%description -n myspell-gl_ES
Galician spelling dictionary, hyphenation rules, and thesaurus.

%package -n myspell-gug
Summary:        MySpell gug Dictionary
Requires:       myspell-dictionaries
Provides:       myspell-dictionary
Provides:       locale(libreoffice:gug)
Provides:       locale(seamonkey-spellchecker:gug)
BuildArch:      noarch

%description -n myspell-gug
Guarani thesaurus and spell checker.

%package -n myspell-gug_PY
Summary:        MySpell gug_PY Dictionary
Requires:       myspell-dictionaries
Requires:       myspell-gug
Provides:       myspell-dictionary
Provides:       locale(libreoffice:gug_PY)
Provides:       locale(seamonkey-spellchecker:gug_PY)
BuildArch:      noarch

%description -n myspell-gug_PY
Guarani thesaurus and spell checker.

%package -n myspell-gu_IN
Summary:        MySpell gu_IN Dictionary
Requires:       myspell-dictionaries
Provides:       myspell-dictionary
Provides:       myspell-gujarati
Provides:       locale(libreoffice:gu_IN)
Provides:       locale(seamonkey-spellchecker:gu_IN)
BuildArch:      noarch

%description -n myspell-gu_IN
Gujarati spelling dictionary.

%package -n myspell-he_IL
Summary:        MySpell he_IL Dictionary
Requires:       myspell-dictionaries
Provides:       myspell-dictionary
Provides:       myspell-hebrew
Provides:       locale(libreoffice:he_IL)
Provides:       locale(seamonkey-spellchecker:he_IL)
BuildArch:      noarch

%description -n myspell-he_IL
Hebrew spelling dictionary.

%package -n myspell-hi_IN
Summary:        MySpell hi_IN Dictionary
Requires:       myspell-dictionaries
Provides:       myspell-dictionary
Provides:       myspell-hindi
Provides:       locale(libreoffice:hi_IN)
Provides:       locale(seamonkey-spellchecker:hi_IN)
BuildArch:      noarch

%description -n myspell-hi_IN
Hindi spelling dictionary.

%package -n myspell-hr_HR
Summary:        MySpell hr_HR Dictionary
Requires:       myspell-dictionaries
Provides:       myspell-croatian
Provides:       myspell-dictionary
Provides:       locale(libreoffice:hr_HR)
Provides:       locale(seamonkey-spellchecker:hr_HR)
BuildArch:      noarch

%description -n myspell-hr_HR
Croatian spelling dictionary, and hyphenation rules.

%package -n myspell-hu_HU
Summary:        MySpell hu_HU Dictionary
Requires:       myspell-dictionaries
Recommends:     myspell-lightproof-hu_HU
Provides:       libreoffice-thesaurus-hu
Provides:       myspell-dictionary
Provides:       myspell-hungarian
Provides:       locale(libreoffice:hu_HU)
Provides:       locale(seamonkey-spellchecker:hu_HU)
BuildArch:      noarch

%description -n myspell-hu_HU
Hungarian spelling dictionary, hyphenation rules, thesaurus, and grammar checker FSF.hu Foundation.

%package -n myspell-lightproof-hu_HU
Summary:        Lightproof for hu_HU
Requires:       myspell-hu_HU

%description -n myspell-lightproof-hu_HU
Lightproof grammar checker information for hu_HU.

%package -n myspell-id
Summary:        MySpell id Dictionary
Requires:       myspell-dictionaries
Provides:       myspell-dictionary
Provides:       locale(libreoffice:id)
Provides:       locale(seamonkey-spellchecker:id)
BuildArch:      noarch

%description -n myspell-id
Indonesian spelling dictionary, hyphenation rules, and thesaurus.

%package -n myspell-id_ID
Summary:        MySpell id_ID Dictionary
Requires:       myspell-dictionaries
Requires:       myspell-id
Provides:       myspell-dictionary
Provides:       locale(libreoffice:id_ID)
Provides:       locale(seamonkey-spellchecker:id_ID)
BuildArch:      noarch

%description -n myspell-id_ID
Indonesian spelling dictionary, hyphenation rules, and thesaurus.

%package -n myspell-is_IS
Summary:        MySpell is_IS Dictionary
Requires:       myspell-dictionaries
Requires:       myspell-is
Provides:       myspell-dictionary
Provides:       locale(libreoffice:is_IS)
Provides:       locale(seamonkey-spellchecker:is_IS)
BuildArch:      noarch

%description -n myspell-is_IS
Icelandic spelling dictionary, hyphenation rules and thesaurus.

%package -n myspell-is
Summary:        MySpell is Dictionary
Requires:       myspell-dictionaries
Provides:       myspell-dictionary
Provides:       myspell-icelandic
Provides:       locale(libreoffice:is)
Provides:       locale(seamonkey-spellchecker:is)
BuildArch:      noarch

%description -n myspell-is
Icelandic spelling dictionary, hyphenation rules and thesaurus.

%package -n myspell-it_IT
Summary:        MySpell it_IT Dictionary
Requires:       myspell-dictionaries
Provides:       libreoffice-thesaurus-it
Provides:       myspell-dictionary
Provides:       myspell-italian
Provides:       locale(libreoffice:it_IT)
Provides:       locale(seamonkey-spellchecker:it_IT)
BuildArch:      noarch

%description -n myspell-it_IT
Italian spelling dictionary, hyphenation rules, and thesaurus.

%package -n myspell-kmr_Latn_TR
Summary:        MySpell kmr_Latn_TR Dictionary
Requires:       myspell-dictionaries
Requires:       myspell-kmr_Latn
Provides:       myspell-dictionary
Provides:       locale(libreoffice:kmr_Latn_TR)
Provides:       locale(seamonkey-spellchecker:kmr_Latn_TR)
BuildArch:      noarch

%description -n myspell-kmr_Latn_TR
Kurdish (Turkey) spelling dictionary.

%package -n myspell-kmr_Latn
Summary:        MySpell kmr_Latn Dictionary
Requires:       myspell-dictionaries
Provides:       myspell-dictionary
Provides:       locale(libreoffice:kmr_Latn)
Provides:       locale(seamonkey-spellchecker:kmr_Latn)
BuildArch:      noarch

%description -n myspell-kmr_Latn
Kurdish (Turkey) spelling dictionary.

%package -n myspell-kmr_Latn_SY
Summary:        MySpell kmr_Latn_SY Dictionary
Requires:       myspell-dictionaries
Requires:       myspell-kmr_Latn
Provides:       myspell-dictionary
Provides:       locale(libreoffice:kmr_Latn_SY)
Provides:       locale(seamonkey-spellchecker:kmr_Latn_SY)
BuildArch:      noarch

%description -n myspell-kmr_Latn_SY
Kurdish (Turkey) spelling dictionary.

%package -n myspell-lo_LA
Summary:        MySpell lo_LA Dictionary
Requires:       myspell-dictionaries
Provides:       myspell-dictionary
Provides:       locale(libreoffice:lo_LA)
Provides:       locale(seamonkey-spellchecker:lo_LA)
BuildArch:      noarch

%description -n myspell-lo_LA
Lao spelling dictionary.

%package -n myspell-lt_LT
Summary:        MySpell lt_LT Dictionary
Requires:       myspell-dictionaries
Provides:       myspell-dictionary
Provides:       myspell-lithuanian
Provides:       locale(libreoffice:lt_LT)
Provides:       locale(seamonkey-spellchecker:lt_LT)
BuildArch:      noarch

%description -n myspell-lt_LT
Lithuanian spelling dictionary, and hyphenation rules.

%package -n myspell-lv_LV
Summary:        MySpell lv_LV Dictionary
Requires:       myspell-dictionaries
Provides:       myspell-dictionary
Provides:       myspell-latvian
Provides:       locale(libreoffice:lv_LV)
Provides:       locale(seamonkey-spellchecker:lv_LV)
BuildArch:      noarch

%description -n myspell-lv_LV
Latvian spelling dictionary, and hyphenation rules.

%package -n myspell-ne_NP
Summary:        MySpell ne_NP Dictionary
Requires:       myspell-dictionaries
Provides:       myspell-dictionary
Provides:       locale(libreoffice:ne_NP)
Provides:       locale(seamonkey-spellchecker:ne_NP)
BuildArch:      noarch

%description -n myspell-ne_NP
Nepali spelling dictionary, and thesaurus.

%package -n myspell-nl_NL
Summary:        MySpell nl_NL Dictionary
Requires:       myspell-dictionaries
Provides:       myspell-dictionary
Provides:       myspell-dutch
Provides:       locale(libreoffice:nl_NL)
Provides:       locale(seamonkey-spellchecker:nl_NL)
BuildArch:      noarch

%description -n myspell-nl_NL
Dutch spelling dictionary, and hyphenation rules.

%package -n myspell-nl_BE
Summary:        MySpell nl_BE Dictionary
Requires:       myspell-dictionaries
Requires:       myspell-nl_NL
Provides:       myspell-dictionary
Provides:       locale(libreoffice:nl_BE)
Provides:       locale(seamonkey-spellchecker:nl_BE)
BuildArch:      noarch

%description -n myspell-nl_BE
Dutch spelling dictionary, and hyphenation rules.

%package -n myspell-no
Summary:        MySpell no Dictionary
Requires:       myspell-dictionaries
Recommends:     myspell-nb_NO
Provides:       myspell-dictionary
Provides:       locale(libreoffice:no)
Provides:       locale(seamonkey-spellchecker:no)
BuildArch:      noarch

%description -n myspell-no
Norwegian (Nynorsk and Bokmål) spelling dictionary, hyphenation rules, and thesaurus.

%package -n myspell-nb_NO
Summary:        MySpell nb_NO Dictionary
Requires:       myspell-dictionaries
Requires:       myspell-no
Provides:       myspell-dictionary
Provides:       myspell-norsk-bokmaal
Provides:       locale(libreoffice:nb_NO)
Provides:       locale(seamonkey-spellchecker:nb_NO)
BuildArch:      noarch

%description -n myspell-nb_NO
Norwegian (Nynorsk and Bokmål) spelling dictionary, hyphenation rules, and thesaurus.

%package -n myspell-nn_NO
Summary:        MySpell nn_NO Dictionary
Requires:       myspell-dictionaries
Requires:       myspell-no
Provides:       myspell-dictionary
Provides:       myspell-norsk-nynorsk
Provides:       locale(libreoffice:nn_NO)
Provides:       locale(seamonkey-spellchecker:nn_NO)
BuildArch:      noarch

%description -n myspell-nn_NO
Norwegian (Nynorsk and Bokmål) spelling dictionary, hyphenation rules, and thesaurus.

%package -n myspell-oc_FR
Summary:        MySpell oc_FR Dictionary
Requires:       myspell-dictionaries
Provides:       myspell-dictionary
Provides:       myspell-occitan-lengadocian
Provides:       locale(libreoffice:oc_FR)
Provides:       locale(seamonkey-spellchecker:oc_FR)
BuildArch:      noarch

%description -n myspell-oc_FR
Occitan spelling dictionary.

%package -n myspell-pl_PL
Summary:        MySpell pl_PL Dictionary
Requires:       myspell-dictionaries
Provides:       libreoffice-thesaurus-pl
Provides:       myspell-dictionary
Provides:       myspell-polish
Provides:       locale(libreoffice:pl_PL)
Provides:       locale(seamonkey-spellchecker:pl_PL)
BuildArch:      noarch

%description -n myspell-pl_PL
Polish spelling dictionary, hyphenation rules, and thesaurus.

%package -n myspell-pt_BR
Summary:        MySpell pt_BR Dictionary
Requires:       myspell-dictionaries
Recommends:     myspell-lightproof-pt_BR
Provides:       libreoffice-thesaurus-pt
Provides:       myspell-brazilian
Provides:       myspell-dictionary
Provides:       locale(libreoffice:pt_BR)
Provides:       locale(seamonkey-spellchecker:pt_BR)
BuildArch:      noarch

%description -n myspell-pt_BR
Spelling, hyphenation and grammar checking tools for Brazilian Portuguese.

%package -n myspell-lightproof-pt_BR
Summary:        Lightproof for pt_BR
Requires:       myspell-pt_BR

%description -n myspell-lightproof-pt_BR
Lightproof grammar checker information for pt_BR.

%package -n myspell-pt_PT
Summary:        MySpell pt_PT Dictionary
Requires:       myspell-dictionaries
Provides:       myspell-dictionary
Provides:       myspell-portuguese
Provides:       locale(libreoffice:pt_PT)
Provides:       locale(seamonkey-spellchecker:pt_PT)
BuildArch:      noarch

%description -n myspell-pt_PT
European Portuguese spelling dictionary, hyphenation rules, and thesaurus.

%package -n myspell-pt_AO
Summary:        MySpell pt_AO Dictionary
Requires:       myspell-dictionaries
Requires:       myspell-pt_PT
Provides:       myspell-dictionary
Provides:       locale(libreoffice:pt_AO)
Provides:       locale(seamonkey-spellchecker:pt_AO)
BuildArch:      noarch

%description -n myspell-pt_AO
European Portuguese spelling dictionary, hyphenation rules, and thesaurus.

%package -n myspell-ro_RO
Summary:        MySpell ro_RO Dictionary
Requires:       myspell-dictionaries
Requires:       myspell-ro
Provides:       myspell-dictionary
Provides:       locale(libreoffice:ro_RO)
Provides:       locale(seamonkey-spellchecker:ro_RO)
BuildArch:      noarch

%description -n myspell-ro_RO
rospell Romanian spelling dictionary, hyphenation rules, and thesaurus.

%package -n myspell-ro
Summary:        MySpell ro Dictionary
Requires:       myspell-dictionaries
Recommends:     myspell-ro_RO
Provides:       libreoffice-thesaurus-ro
Provides:       myspell-dictionary
Provides:       myspell-romanian
Provides:       locale(libreoffice:ro)
Provides:       locale(seamonkey-spellchecker:ro)
BuildArch:      noarch

%description -n myspell-ro
rospell Romanian spelling dictionary, hyphenation rules, and thesaurus.

%package -n myspell-ru_RU
Summary:        MySpell ru_RU Dictionary
Requires:       myspell-dictionaries
Recommends:     myspell-lightproof-ru_RU
Provides:       libreoffice-thesaurus-ru
Provides:       myspell-dictionary
Provides:       myspell-russian
Provides:       locale(libreoffice:ru_RU)
Provides:       locale(seamonkey-spellchecker:ru_RU)
BuildArch:      noarch

%description -n myspell-ru_RU
Russian spelling dictionary, hyphenation rules, thesaurus, and grammar checker.

%package -n myspell-lightproof-ru_RU
Summary:        Lightproof for ru_RU
Requires:       myspell-ru_RU

%description -n myspell-lightproof-ru_RU
Lightproof grammar checker information for ru_RU.

%package -n myspell-si_LK
Summary:        MySpell si_LK Dictionary
Requires:       myspell-dictionaries
Provides:       myspell-dictionary
Provides:       myspell-sinhala
Provides:       locale(libreoffice:si_LK)
Provides:       locale(seamonkey-spellchecker:si_LK)
BuildArch:      noarch

%description -n myspell-si_LK
Sinhala spelling dictionary.

%package -n myspell-sk_SK
Summary:        MySpell sk_SK Dictionary
Requires:       myspell-dictionaries
Provides:       libreoffice-thesaurus-sk
Provides:       myspell-dictionary
Provides:       myspell-slovak
Provides:       locale(libreoffice:sk_SK)
Provides:       locale(seamonkey-spellchecker:sk_SK)
BuildArch:      noarch

%description -n myspell-sk_SK
Slovak spelling dictionary, hyphenation rules, and thesaurus.

%package -n myspell-sl_SI
Summary:        MySpell sl_SI Dictionary
Requires:       myspell-dictionaries
Provides:       libreoffice-thesaurus-sl
Provides:       myspell-dictionary
Provides:       myspell-slovene
Provides:       locale(libreoffice:sl_SI)
Provides:       locale(seamonkey-spellchecker:sl_SI)
BuildArch:      noarch

%description -n myspell-sl_SI
Slovenian spelling dictionary, hyphenation rules, and thesaurus.

%package -n myspell-sq_AL
Summary:        MySpell sq_AL Dictionary
Requires:       myspell-dictionaries
Provides:       myspell-dictionary
Provides:       locale(libreoffice:sq_AL)
Provides:       locale(seamonkey-spellchecker:sq_AL)
BuildArch:      noarch

%description -n myspell-sq_AL
Albanian spelling dictionary.

%package -n myspell-sr_Latn_CS
Summary:        MySpell sr_Latn_CS Dictionary
Requires:       myspell-dictionaries
Requires:       myspell-sr
Provides:       myspell-dictionary
Provides:       locale(libreoffice:sr_Latn_CS)
Provides:       locale(seamonkey-spellchecker:sr_Latn_CS)
BuildArch:      noarch

%description -n myspell-sr_Latn_CS
Serbian (Cyrillic and Latin) spelling dictionary, and hyphenation rules.

%package -n myspell-sr_CS
Summary:        MySpell sr_CS Dictionary
Requires:       myspell-dictionaries
Requires:       myspell-sr
Provides:       myspell-dictionary
Provides:       locale(libreoffice:sr_CS)
Provides:       locale(seamonkey-spellchecker:sr_CS)
BuildArch:      noarch

%description -n myspell-sr_CS
Serbian (Cyrillic and Latin) spelling dictionary, and hyphenation rules.

%package -n myspell-sr
Summary:        MySpell sr Dictionary
Requires:       myspell-dictionaries
Provides:       myspell-dictionary
Provides:       myspell-serbian-cyrillic
Provides:       myspell-serbian-latin
Provides:       locale(libreoffice:sr)
Provides:       locale(seamonkey-spellchecker:sr)
BuildArch:      noarch

%description -n myspell-sr
Serbian (Cyrillic and Latin) spelling dictionary, and hyphenation rules.

%package -n myspell-sr_Latn_RS
Summary:        MySpell sr_Latn_RS Dictionary
Requires:       myspell-dictionaries
Requires:       myspell-sr
Provides:       myspell-dictionary
Provides:       locale(libreoffice:sr_Latn_RS)
Provides:       locale(seamonkey-spellchecker:sr_Latn_RS)
BuildArch:      noarch

%description -n myspell-sr_Latn_RS
Serbian (Cyrillic and Latin) spelling dictionary, and hyphenation rules.

%package -n myspell-sr_RS
Summary:        MySpell sr_RS Dictionary
Requires:       myspell-dictionaries
Requires:       myspell-sr
Provides:       myspell-dictionary
Provides:       locale(libreoffice:sr_RS)
Provides:       locale(seamonkey-spellchecker:sr_RS)
BuildArch:      noarch

%description -n myspell-sr_RS
Serbian (Cyrillic and Latin) spelling dictionary, and hyphenation rules.

%package -n myspell-sv_SE
Summary:        MySpell sv_SE Dictionary
Requires:       myspell-dictionaries
Provides:       libreoffice-thesaurus-sv
Provides:       myspell-dictionary
Provides:       myspell-swedish
Provides:       locale(libreoffice:sv_SE)
Provides:       locale(seamonkey-spellchecker:sv_SE)
BuildArch:      noarch

%description -n myspell-sv_SE
Swedish Dictionary.

%package -n myspell-sv_FI
Summary:        MySpell sv_FI Dictionary
Requires:       myspell-dictionaries
Requires:       myspell-sv_SE
Provides:       myspell-dictionary
Provides:       locale(libreoffice:sv_FI)
Provides:       locale(seamonkey-spellchecker:sv_FI)
BuildArch:      noarch

%description -n myspell-sv_FI
Swedish Dictionary.

%package -n myspell-sw_TZ
Summary:        MySpell sw_TZ Dictionary
Requires:       myspell-dictionaries
Provides:       myspell-dictionary
Provides:       myspell-kiswahili
Provides:       locale(libreoffice:sw_TZ)
Provides:       locale(seamonkey-spellchecker:sw_TZ)
BuildArch:      noarch

%description -n myspell-sw_TZ
Swahili spelling dictionary.

%package -n myspell-te
Summary:        MySpell te Dictionary
Requires:       myspell-dictionaries
Requires:       myspell-te_IN
Provides:       myspell-dictionary
Provides:       locale(libreoffice:te)
Provides:       locale(seamonkey-spellchecker:te)
BuildArch:      noarch

%description -n myspell-te
Telugu spelling dictionary, and hyphenation rules.

%package -n myspell-te_IN
Summary:        MySpell te_IN Dictionary
Requires:       myspell-dictionaries
Provides:       myspell-dictionary
Provides:       locale(libreoffice:te_IN)
Provides:       locale(seamonkey-spellchecker:te_IN)
BuildArch:      noarch

%description -n myspell-te_IN
Telugu spelling dictionary, and hyphenation rules.

%package -n myspell-th_TH
Summary:        MySpell th_TH Dictionary
Requires:       myspell-dictionaries
Provides:       myspell-dictionary
Provides:       myspell-thai
Provides:       locale(libreoffice:th_TH)
Provides:       locale(seamonkey-spellchecker:th_TH)
BuildArch:      noarch

%description -n myspell-th_TH
Thai spelling dictionary.

%package -n myspell-tr
Summary:        MySpell tr Dictionary
Requires:       myspell-dictionaries
Requires:       myspell-tr_TR
Provides:       myspell-dictionary
Provides:       locale(libreoffice:tr)
Provides:       locale(seamonkey-spellchecker:tr)
BuildArch:      noarch

%description -n myspell-tr
Turkish Spellcheck Dictionary.

%package -n myspell-tr_TR
Summary:        MySpell tr_TR Dictionary
Requires:       myspell-dictionaries
Provides:       myspell-dictionary
Provides:       locale(libreoffice:tr_TR)
Provides:       locale(seamonkey-spellchecker:tr_TR)
BuildArch:      noarch

%description -n myspell-tr_TR
Turkish Spellcheck Dictionary.

%package -n myspell-uk_UA
Summary:        MySpell uk_UA Dictionary
Requires:       myspell-dictionaries
Provides:       myspell-dictionary
Provides:       myspell-ukrainian
Provides:       locale(libreoffice:uk_UA)
Provides:       locale(seamonkey-spellchecker:uk_UA)
BuildArch:      noarch

%description -n myspell-uk_UA
Ukrainian spelling dictionary, hyphenation rules, and thesaurus.

%package -n myspell-vi
Summary:        MySpell vi Dictionary
Requires:       myspell-dictionaries
Recommends:     myspell-vi_VN
Provides:       myspell-dictionary
Provides:       myspell-vietnamese
Provides:       locale(libreoffice:vi)
Provides:       locale(seamonkey-spellchecker:vi)
BuildArch:      noarch

%description -n myspell-vi
Vietnamese spelling dictionary.

%package -n myspell-vi_VN
Summary:        MySpell vi_VN Dictionary
Requires:       myspell-dictionaries
Requires:       myspell-vi
Provides:       myspell-dictionary
Provides:       locale(libreoffice:vi_VN)
Provides:       locale(seamonkey-spellchecker:vi_VN)
BuildArch:      noarch

%description -n myspell-vi_VN
Vietnamese spelling dictionary.

%package -n myspell-zu_ZA
Summary:        MySpell zu_ZA Dictionary
Requires:       myspell-dictionaries
Provides:       myspell-dictionary
Provides:       myspell-zulu
Provides:       locale(libreoffice:zu_ZA)
Provides:       locale(seamonkey-spellchecker:zu_ZA)
BuildArch:      noarch

%description -n myspell-zu_ZA
Zulu hyphenation rules.

%prep
%setup -q -n dictionaries

%build

%install
mkdir -p %{buildroot}%{_datadir}/hunspell
mkdir -p %{buildroot}%{_datadir}/hyphen
mkdir -p %{buildroot}%{_datadir}/mythes
mkdir -p %{buildroot}%{_datadir}/myspell
mkdir -p %{buildroot}%{_libdir}/libreoffice
mkdir -p %{buildroot}%{_libdir}/libreoffice/share
mkdir -p %{buildroot}%{_libdir}/libreoffice/share/extensions
ln -s %{_datadir}/hunspell/af_ZA.aff %{buildroot}%{_datadir}/hunspell/af_NA.aff
ln -s %{_datadir}/hunspell/af_NA.aff %{buildroot}%{_datadir}/myspell/af_NA.aff
cp -P af_ZA/af_ZA.aff %{buildroot}%{_datadir}/hunspell/af_ZA.aff
ln -s %{_datadir}/hunspell/af_ZA.aff %{buildroot}%{_datadir}/myspell/af_ZA.aff
ln -s %{_datadir}/hunspell/af_ZA.dic %{buildroot}%{_datadir}/hunspell/af_NA.dic
ln -s %{_datadir}/hunspell/af_NA.dic %{buildroot}%{_datadir}/myspell/af_NA.dic
cp -P af_ZA/af_ZA.dic %{buildroot}%{_datadir}/hunspell/af_ZA.dic
ln -s %{_datadir}/hunspell/af_ZA.dic %{buildroot}%{_datadir}/myspell/af_ZA.dic
ln -s %{_datadir}/hyphen/hyph_af_ZA.dic %{buildroot}%{_datadir}/hyphen/hyph_af_NA.dic
ln -s %{_datadir}/hyphen/hyph_af_NA.dic %{buildroot}%{_datadir}/myspell/hyph_af_NA.dic
cp -P af_ZA/hyph_af_ZA.dic %{buildroot}%{_datadir}/hyphen/hyph_af_ZA.dic
ln -s %{_datadir}/hyphen/hyph_af_ZA.dic %{buildroot}%{_datadir}/myspell/hyph_af_ZA.dic
mkdir -p %{buildroot}%{_docdir}/myspell-af_ZA
cp -P af_ZA/README_af_ZA.txt %{buildroot}%{_docdir}/myspell-af_ZA/README_af_ZA.txt
cp -P af_ZA/description.xml %{buildroot}%{_docdir}/myspell-af_ZA/description.xml
cp -P af_ZA/dictionaries.xcu %{buildroot}%{_docdir}/myspell-af_ZA/dictionaries.xcu
ln -s %{_datadir}/hunspell/an_ES.aff %{buildroot}%{_datadir}/hunspell/an.aff
ln -s %{_datadir}/hunspell/an.aff %{buildroot}%{_datadir}/myspell/an.aff
cp -P an_ES/an_ES.aff %{buildroot}%{_datadir}/hunspell/an_ES.aff
ln -s %{_datadir}/hunspell/an_ES.aff %{buildroot}%{_datadir}/myspell/an_ES.aff
ln -s %{_datadir}/hunspell/an_ES.dic %{buildroot}%{_datadir}/hunspell/an.dic
ln -s %{_datadir}/hunspell/an.dic %{buildroot}%{_datadir}/myspell/an.dic
cp -P an_ES/an_ES.dic %{buildroot}%{_datadir}/hunspell/an_ES.dic
ln -s %{_datadir}/hunspell/an_ES.dic %{buildroot}%{_datadir}/myspell/an_ES.dic
mkdir -p %{buildroot}%{_docdir}/myspell-an_ES
cp -P an_ES/LICENSES-en.txt %{buildroot}%{_docdir}/myspell-an_ES/LICENSES-en.txt
cp -P an_ES/description.xml %{buildroot}%{_docdir}/myspell-an_ES/description.xml
cp -P an_ES/dictionaries.xcu %{buildroot}%{_docdir}/myspell-an_ES/dictionaries.xcu
ln -s %{_datadir}/hunspell/ar.aff %{buildroot}%{_datadir}/hunspell/ar_SA.aff
ln -s %{_datadir}/hunspell/ar_SA.aff %{buildroot}%{_datadir}/myspell/ar_SA.aff
ln -s %{_datadir}/hunspell/ar.aff %{buildroot}%{_datadir}/hunspell/ar_DZ.aff
ln -s %{_datadir}/hunspell/ar_DZ.aff %{buildroot}%{_datadir}/myspell/ar_DZ.aff
ln -s %{_datadir}/hunspell/ar.aff %{buildroot}%{_datadir}/hunspell/ar_BH.aff
ln -s %{_datadir}/hunspell/ar_BH.aff %{buildroot}%{_datadir}/myspell/ar_BH.aff
ln -s %{_datadir}/hunspell/ar.aff %{buildroot}%{_datadir}/hunspell/ar_EG.aff
ln -s %{_datadir}/hunspell/ar_EG.aff %{buildroot}%{_datadir}/myspell/ar_EG.aff
ln -s %{_datadir}/hunspell/ar.aff %{buildroot}%{_datadir}/hunspell/ar_IQ.aff
ln -s %{_datadir}/hunspell/ar_IQ.aff %{buildroot}%{_datadir}/myspell/ar_IQ.aff
ln -s %{_datadir}/hunspell/ar.aff %{buildroot}%{_datadir}/hunspell/ar_JO.aff
ln -s %{_datadir}/hunspell/ar_JO.aff %{buildroot}%{_datadir}/myspell/ar_JO.aff
ln -s %{_datadir}/hunspell/ar.aff %{buildroot}%{_datadir}/hunspell/ar_KW.aff
ln -s %{_datadir}/hunspell/ar_KW.aff %{buildroot}%{_datadir}/myspell/ar_KW.aff
ln -s %{_datadir}/hunspell/ar.aff %{buildroot}%{_datadir}/hunspell/ar_LB.aff
ln -s %{_datadir}/hunspell/ar_LB.aff %{buildroot}%{_datadir}/myspell/ar_LB.aff
ln -s %{_datadir}/hunspell/ar.aff %{buildroot}%{_datadir}/hunspell/ar_LY.aff
ln -s %{_datadir}/hunspell/ar_LY.aff %{buildroot}%{_datadir}/myspell/ar_LY.aff
ln -s %{_datadir}/hunspell/ar.aff %{buildroot}%{_datadir}/hunspell/ar_MA.aff
ln -s %{_datadir}/hunspell/ar_MA.aff %{buildroot}%{_datadir}/myspell/ar_MA.aff
ln -s %{_datadir}/hunspell/ar.aff %{buildroot}%{_datadir}/hunspell/ar_OM.aff
ln -s %{_datadir}/hunspell/ar_OM.aff %{buildroot}%{_datadir}/myspell/ar_OM.aff
ln -s %{_datadir}/hunspell/ar.aff %{buildroot}%{_datadir}/hunspell/ar_QA.aff
ln -s %{_datadir}/hunspell/ar_QA.aff %{buildroot}%{_datadir}/myspell/ar_QA.aff
ln -s %{_datadir}/hunspell/ar.aff %{buildroot}%{_datadir}/hunspell/ar_SD.aff
ln -s %{_datadir}/hunspell/ar_SD.aff %{buildroot}%{_datadir}/myspell/ar_SD.aff
ln -s %{_datadir}/hunspell/ar.aff %{buildroot}%{_datadir}/hunspell/ar_SY.aff
ln -s %{_datadir}/hunspell/ar_SY.aff %{buildroot}%{_datadir}/myspell/ar_SY.aff
ln -s %{_datadir}/hunspell/ar.aff %{buildroot}%{_datadir}/hunspell/ar_TN.aff
ln -s %{_datadir}/hunspell/ar_TN.aff %{buildroot}%{_datadir}/myspell/ar_TN.aff
ln -s %{_datadir}/hunspell/ar.aff %{buildroot}%{_datadir}/hunspell/ar_AE.aff
ln -s %{_datadir}/hunspell/ar_AE.aff %{buildroot}%{_datadir}/myspell/ar_AE.aff
ln -s %{_datadir}/hunspell/ar.aff %{buildroot}%{_datadir}/hunspell/ar_YE.aff
ln -s %{_datadir}/hunspell/ar_YE.aff %{buildroot}%{_datadir}/myspell/ar_YE.aff
cp -P ar/ar.aff %{buildroot}%{_datadir}/hunspell/ar.aff
ln -s %{_datadir}/hunspell/ar.aff %{buildroot}%{_datadir}/myspell/ar.aff
ln -s %{_datadir}/hunspell/ar.dic %{buildroot}%{_datadir}/hunspell/ar_SA.dic
ln -s %{_datadir}/hunspell/ar_SA.dic %{buildroot}%{_datadir}/myspell/ar_SA.dic
ln -s %{_datadir}/hunspell/ar.dic %{buildroot}%{_datadir}/hunspell/ar_DZ.dic
ln -s %{_datadir}/hunspell/ar_DZ.dic %{buildroot}%{_datadir}/myspell/ar_DZ.dic
ln -s %{_datadir}/hunspell/ar.dic %{buildroot}%{_datadir}/hunspell/ar_BH.dic
ln -s %{_datadir}/hunspell/ar_BH.dic %{buildroot}%{_datadir}/myspell/ar_BH.dic
ln -s %{_datadir}/hunspell/ar.dic %{buildroot}%{_datadir}/hunspell/ar_EG.dic
ln -s %{_datadir}/hunspell/ar_EG.dic %{buildroot}%{_datadir}/myspell/ar_EG.dic
ln -s %{_datadir}/hunspell/ar.dic %{buildroot}%{_datadir}/hunspell/ar_IQ.dic
ln -s %{_datadir}/hunspell/ar_IQ.dic %{buildroot}%{_datadir}/myspell/ar_IQ.dic
ln -s %{_datadir}/hunspell/ar.dic %{buildroot}%{_datadir}/hunspell/ar_JO.dic
ln -s %{_datadir}/hunspell/ar_JO.dic %{buildroot}%{_datadir}/myspell/ar_JO.dic
ln -s %{_datadir}/hunspell/ar.dic %{buildroot}%{_datadir}/hunspell/ar_KW.dic
ln -s %{_datadir}/hunspell/ar_KW.dic %{buildroot}%{_datadir}/myspell/ar_KW.dic
ln -s %{_datadir}/hunspell/ar.dic %{buildroot}%{_datadir}/hunspell/ar_LB.dic
ln -s %{_datadir}/hunspell/ar_LB.dic %{buildroot}%{_datadir}/myspell/ar_LB.dic
ln -s %{_datadir}/hunspell/ar.dic %{buildroot}%{_datadir}/hunspell/ar_LY.dic
ln -s %{_datadir}/hunspell/ar_LY.dic %{buildroot}%{_datadir}/myspell/ar_LY.dic
ln -s %{_datadir}/hunspell/ar.dic %{buildroot}%{_datadir}/hunspell/ar_MA.dic
ln -s %{_datadir}/hunspell/ar_MA.dic %{buildroot}%{_datadir}/myspell/ar_MA.dic
ln -s %{_datadir}/hunspell/ar.dic %{buildroot}%{_datadir}/hunspell/ar_OM.dic
ln -s %{_datadir}/hunspell/ar_OM.dic %{buildroot}%{_datadir}/myspell/ar_OM.dic
ln -s %{_datadir}/hunspell/ar.dic %{buildroot}%{_datadir}/hunspell/ar_QA.dic
ln -s %{_datadir}/hunspell/ar_QA.dic %{buildroot}%{_datadir}/myspell/ar_QA.dic
ln -s %{_datadir}/hunspell/ar.dic %{buildroot}%{_datadir}/hunspell/ar_SD.dic
ln -s %{_datadir}/hunspell/ar_SD.dic %{buildroot}%{_datadir}/myspell/ar_SD.dic
ln -s %{_datadir}/hunspell/ar.dic %{buildroot}%{_datadir}/hunspell/ar_SY.dic
ln -s %{_datadir}/hunspell/ar_SY.dic %{buildroot}%{_datadir}/myspell/ar_SY.dic
ln -s %{_datadir}/hunspell/ar.dic %{buildroot}%{_datadir}/hunspell/ar_TN.dic
ln -s %{_datadir}/hunspell/ar_TN.dic %{buildroot}%{_datadir}/myspell/ar_TN.dic
ln -s %{_datadir}/hunspell/ar.dic %{buildroot}%{_datadir}/hunspell/ar_AE.dic
ln -s %{_datadir}/hunspell/ar_AE.dic %{buildroot}%{_datadir}/myspell/ar_AE.dic
ln -s %{_datadir}/hunspell/ar.dic %{buildroot}%{_datadir}/hunspell/ar_YE.dic
ln -s %{_datadir}/hunspell/ar_YE.dic %{buildroot}%{_datadir}/myspell/ar_YE.dic
cp -P ar/ar.dic %{buildroot}%{_datadir}/hunspell/ar.dic
ln -s %{_datadir}/hunspell/ar.dic %{buildroot}%{_datadir}/myspell/ar.dic
ln -s %{_datadir}/mythes/th_ar.dat %{buildroot}%{_datadir}/mythes/th_ar_SA_v2.dat
ln -s %{_datadir}/mythes/th_ar_SA_v2.dat %{buildroot}%{_datadir}/myspell/th_ar_SA_v2.dat
ln -s %{_datadir}/mythes/th_ar.dat %{buildroot}%{_datadir}/mythes/th_ar_DZ_v2.dat
ln -s %{_datadir}/mythes/th_ar_DZ_v2.dat %{buildroot}%{_datadir}/myspell/th_ar_DZ_v2.dat
ln -s %{_datadir}/mythes/th_ar.dat %{buildroot}%{_datadir}/mythes/th_ar_BH_v2.dat
ln -s %{_datadir}/mythes/th_ar_BH_v2.dat %{buildroot}%{_datadir}/myspell/th_ar_BH_v2.dat
ln -s %{_datadir}/mythes/th_ar.dat %{buildroot}%{_datadir}/mythes/th_ar_EG_v2.dat
ln -s %{_datadir}/mythes/th_ar_EG_v2.dat %{buildroot}%{_datadir}/myspell/th_ar_EG_v2.dat
ln -s %{_datadir}/mythes/th_ar.dat %{buildroot}%{_datadir}/mythes/th_ar_IQ_v2.dat
ln -s %{_datadir}/mythes/th_ar_IQ_v2.dat %{buildroot}%{_datadir}/myspell/th_ar_IQ_v2.dat
ln -s %{_datadir}/mythes/th_ar.dat %{buildroot}%{_datadir}/mythes/th_ar_JO_v2.dat
ln -s %{_datadir}/mythes/th_ar_JO_v2.dat %{buildroot}%{_datadir}/myspell/th_ar_JO_v2.dat
ln -s %{_datadir}/mythes/th_ar.dat %{buildroot}%{_datadir}/mythes/th_ar_KW_v2.dat
ln -s %{_datadir}/mythes/th_ar_KW_v2.dat %{buildroot}%{_datadir}/myspell/th_ar_KW_v2.dat
ln -s %{_datadir}/mythes/th_ar.dat %{buildroot}%{_datadir}/mythes/th_ar_LB_v2.dat
ln -s %{_datadir}/mythes/th_ar_LB_v2.dat %{buildroot}%{_datadir}/myspell/th_ar_LB_v2.dat
ln -s %{_datadir}/mythes/th_ar.dat %{buildroot}%{_datadir}/mythes/th_ar_LY_v2.dat
ln -s %{_datadir}/mythes/th_ar_LY_v2.dat %{buildroot}%{_datadir}/myspell/th_ar_LY_v2.dat
ln -s %{_datadir}/mythes/th_ar.dat %{buildroot}%{_datadir}/mythes/th_ar_MA_v2.dat
ln -s %{_datadir}/mythes/th_ar_MA_v2.dat %{buildroot}%{_datadir}/myspell/th_ar_MA_v2.dat
ln -s %{_datadir}/mythes/th_ar.dat %{buildroot}%{_datadir}/mythes/th_ar_OM_v2.dat
ln -s %{_datadir}/mythes/th_ar_OM_v2.dat %{buildroot}%{_datadir}/myspell/th_ar_OM_v2.dat
ln -s %{_datadir}/mythes/th_ar.dat %{buildroot}%{_datadir}/mythes/th_ar_QA_v2.dat
ln -s %{_datadir}/mythes/th_ar_QA_v2.dat %{buildroot}%{_datadir}/myspell/th_ar_QA_v2.dat
ln -s %{_datadir}/mythes/th_ar.dat %{buildroot}%{_datadir}/mythes/th_ar_SD_v2.dat
ln -s %{_datadir}/mythes/th_ar_SD_v2.dat %{buildroot}%{_datadir}/myspell/th_ar_SD_v2.dat
ln -s %{_datadir}/mythes/th_ar.dat %{buildroot}%{_datadir}/mythes/th_ar_SY_v2.dat
ln -s %{_datadir}/mythes/th_ar_SY_v2.dat %{buildroot}%{_datadir}/myspell/th_ar_SY_v2.dat
ln -s %{_datadir}/mythes/th_ar.dat %{buildroot}%{_datadir}/mythes/th_ar_TN_v2.dat
ln -s %{_datadir}/mythes/th_ar_TN_v2.dat %{buildroot}%{_datadir}/myspell/th_ar_TN_v2.dat
ln -s %{_datadir}/mythes/th_ar.dat %{buildroot}%{_datadir}/mythes/th_ar_AE_v2.dat
ln -s %{_datadir}/mythes/th_ar_AE_v2.dat %{buildroot}%{_datadir}/myspell/th_ar_AE_v2.dat
ln -s %{_datadir}/mythes/th_ar.dat %{buildroot}%{_datadir}/mythes/th_ar_YE_v2.dat
ln -s %{_datadir}/mythes/th_ar_YE_v2.dat %{buildroot}%{_datadir}/myspell/th_ar_YE_v2.dat
cp -P ar/th_ar.dat %{buildroot}%{_datadir}/mythes/th_ar.dat
ln -s %{_datadir}/mythes/th_ar.dat %{buildroot}%{_datadir}/myspell/th_ar.dat
ln -s %{_datadir}/mythes/th_ar.idx %{buildroot}%{_datadir}/mythes/th_ar_SA_v2.idx
ln -s %{_datadir}/mythes/th_ar_SA_v2.idx %{buildroot}%{_datadir}/myspell/th_ar_SA_v2.idx
ln -s %{_datadir}/mythes/th_ar.idx %{buildroot}%{_datadir}/mythes/th_ar_DZ_v2.idx
ln -s %{_datadir}/mythes/th_ar_DZ_v2.idx %{buildroot}%{_datadir}/myspell/th_ar_DZ_v2.idx
ln -s %{_datadir}/mythes/th_ar.idx %{buildroot}%{_datadir}/mythes/th_ar_BH_v2.idx
ln -s %{_datadir}/mythes/th_ar_BH_v2.idx %{buildroot}%{_datadir}/myspell/th_ar_BH_v2.idx
ln -s %{_datadir}/mythes/th_ar.idx %{buildroot}%{_datadir}/mythes/th_ar_EG_v2.idx
ln -s %{_datadir}/mythes/th_ar_EG_v2.idx %{buildroot}%{_datadir}/myspell/th_ar_EG_v2.idx
ln -s %{_datadir}/mythes/th_ar.idx %{buildroot}%{_datadir}/mythes/th_ar_IQ_v2.idx
ln -s %{_datadir}/mythes/th_ar_IQ_v2.idx %{buildroot}%{_datadir}/myspell/th_ar_IQ_v2.idx
ln -s %{_datadir}/mythes/th_ar.idx %{buildroot}%{_datadir}/mythes/th_ar_JO_v2.idx
ln -s %{_datadir}/mythes/th_ar_JO_v2.idx %{buildroot}%{_datadir}/myspell/th_ar_JO_v2.idx
ln -s %{_datadir}/mythes/th_ar.idx %{buildroot}%{_datadir}/mythes/th_ar_KW_v2.idx
ln -s %{_datadir}/mythes/th_ar_KW_v2.idx %{buildroot}%{_datadir}/myspell/th_ar_KW_v2.idx
ln -s %{_datadir}/mythes/th_ar.idx %{buildroot}%{_datadir}/mythes/th_ar_LB_v2.idx
ln -s %{_datadir}/mythes/th_ar_LB_v2.idx %{buildroot}%{_datadir}/myspell/th_ar_LB_v2.idx
ln -s %{_datadir}/mythes/th_ar.idx %{buildroot}%{_datadir}/mythes/th_ar_LY_v2.idx
ln -s %{_datadir}/mythes/th_ar_LY_v2.idx %{buildroot}%{_datadir}/myspell/th_ar_LY_v2.idx
ln -s %{_datadir}/mythes/th_ar.idx %{buildroot}%{_datadir}/mythes/th_ar_MA_v2.idx
ln -s %{_datadir}/mythes/th_ar_MA_v2.idx %{buildroot}%{_datadir}/myspell/th_ar_MA_v2.idx
ln -s %{_datadir}/mythes/th_ar.idx %{buildroot}%{_datadir}/mythes/th_ar_OM_v2.idx
ln -s %{_datadir}/mythes/th_ar_OM_v2.idx %{buildroot}%{_datadir}/myspell/th_ar_OM_v2.idx
ln -s %{_datadir}/mythes/th_ar.idx %{buildroot}%{_datadir}/mythes/th_ar_QA_v2.idx
ln -s %{_datadir}/mythes/th_ar_QA_v2.idx %{buildroot}%{_datadir}/myspell/th_ar_QA_v2.idx
ln -s %{_datadir}/mythes/th_ar.idx %{buildroot}%{_datadir}/mythes/th_ar_SD_v2.idx
ln -s %{_datadir}/mythes/th_ar_SD_v2.idx %{buildroot}%{_datadir}/myspell/th_ar_SD_v2.idx
ln -s %{_datadir}/mythes/th_ar.idx %{buildroot}%{_datadir}/mythes/th_ar_SY_v2.idx
ln -s %{_datadir}/mythes/th_ar_SY_v2.idx %{buildroot}%{_datadir}/myspell/th_ar_SY_v2.idx
ln -s %{_datadir}/mythes/th_ar.idx %{buildroot}%{_datadir}/mythes/th_ar_TN_v2.idx
ln -s %{_datadir}/mythes/th_ar_TN_v2.idx %{buildroot}%{_datadir}/myspell/th_ar_TN_v2.idx
ln -s %{_datadir}/mythes/th_ar.idx %{buildroot}%{_datadir}/mythes/th_ar_AE_v2.idx
ln -s %{_datadir}/mythes/th_ar_AE_v2.idx %{buildroot}%{_datadir}/myspell/th_ar_AE_v2.idx
ln -s %{_datadir}/mythes/th_ar.idx %{buildroot}%{_datadir}/mythes/th_ar_YE_v2.idx
ln -s %{_datadir}/mythes/th_ar_YE_v2.idx %{buildroot}%{_datadir}/myspell/th_ar_YE_v2.idx
cp -P ar/th_ar.idx %{buildroot}%{_datadir}/mythes/th_ar.idx
ln -s %{_datadir}/mythes/th_ar.idx %{buildroot}%{_datadir}/myspell/th_ar.idx
mkdir -p %{buildroot}%{_docdir}/myspell-ar
cp -P ar/AUTHORS.txt %{buildroot}%{_docdir}/myspell-ar/AUTHORS.txt
cp -P ar/COPYING.txt %{buildroot}%{_docdir}/myspell-ar/COPYING.txt
cp -P ar/README_ar.txt %{buildroot}%{_docdir}/myspell-ar/README_ar.txt
cp -P ar/description.xml %{buildroot}%{_docdir}/myspell-ar/description.xml
cp -P ar/dictionaries.xcu %{buildroot}%{_docdir}/myspell-ar/dictionaries.xcu
cp -P be_BY/be_BY.aff %{buildroot}%{_datadir}/hunspell/be_BY.aff
ln -s %{_datadir}/hunspell/be_BY.aff %{buildroot}%{_datadir}/myspell/be_BY.aff
cp -P be_BY/be_BY.dic %{buildroot}%{_datadir}/hunspell/be_BY.dic
ln -s %{_datadir}/hunspell/be_BY.dic %{buildroot}%{_datadir}/myspell/be_BY.dic
cp -P be_BY/hyph_be_BY.dic %{buildroot}%{_datadir}/hyphen/hyph_be_BY.dic
ln -s %{_datadir}/hyphen/hyph_be_BY.dic %{buildroot}%{_datadir}/myspell/hyph_be_BY.dic
mkdir -p %{buildroot}%{_docdir}/myspell-be_BY
cp -P be_BY/README_be_BY.txt %{buildroot}%{_docdir}/myspell-be_BY/README_be_BY.txt
cp -P be_BY/description.xml %{buildroot}%{_docdir}/myspell-be_BY/description.xml
cp -P be_BY/dictionaries.xcu %{buildroot}%{_docdir}/myspell-be_BY/dictionaries.xcu
cp -P bg_BG/bg_BG.aff %{buildroot}%{_datadir}/hunspell/bg_BG.aff
ln -s %{_datadir}/hunspell/bg_BG.aff %{buildroot}%{_datadir}/myspell/bg_BG.aff
cp -P bg_BG/bg_BG.dic %{buildroot}%{_datadir}/hunspell/bg_BG.dic
ln -s %{_datadir}/hunspell/bg_BG.dic %{buildroot}%{_datadir}/myspell/bg_BG.dic
cp -P bg_BG/hyph_bg_BG.dic %{buildroot}%{_datadir}/hyphen/hyph_bg_BG.dic
ln -s %{_datadir}/hyphen/hyph_bg_BG.dic %{buildroot}%{_datadir}/myspell/hyph_bg_BG.dic
cp -P bg_BG/th_bg_BG_v2.dat %{buildroot}%{_datadir}/mythes/th_bg_BG_v2.dat
ln -s %{_datadir}/mythes/th_bg_BG_v2.dat %{buildroot}%{_datadir}/myspell/th_bg_BG_v2.dat
cp -P bg_BG/th_bg_BG_v2.idx %{buildroot}%{_datadir}/mythes/th_bg_BG_v2.idx
ln -s %{_datadir}/mythes/th_bg_BG_v2.idx %{buildroot}%{_datadir}/myspell/th_bg_BG_v2.idx
mkdir -p %{buildroot}%{_docdir}/myspell-bg_BG
cp -P bg_BG/COPYING %{buildroot}%{_docdir}/myspell-bg_BG/COPYING
cp -P bg_BG/README_hyph_bg_BG.txt %{buildroot}%{_docdir}/myspell-bg_BG/README_hyph_bg_BG.txt
cp -P bg_BG/README_th_bg_BG_v2.txt %{buildroot}%{_docdir}/myspell-bg_BG/README_th_bg_BG_v2.txt
cp -P bg_BG/description.xml %{buildroot}%{_docdir}/myspell-bg_BG/description.xml
cp -P bg_BG/dictionaries.xcu %{buildroot}%{_docdir}/myspell-bg_BG/dictionaries.xcu
ln -s %{_datadir}/hunspell/bn_BD.aff %{buildroot}%{_datadir}/hunspell/bn_IN.aff
ln -s %{_datadir}/hunspell/bn_IN.aff %{buildroot}%{_datadir}/myspell/bn_IN.aff
cp -P bn_BD/bn_BD.aff %{buildroot}%{_datadir}/hunspell/bn_BD.aff
ln -s %{_datadir}/hunspell/bn_BD.aff %{buildroot}%{_datadir}/myspell/bn_BD.aff
ln -s %{_datadir}/hunspell/bn_BD.dic %{buildroot}%{_datadir}/hunspell/bn_IN.dic
ln -s %{_datadir}/hunspell/bn_IN.dic %{buildroot}%{_datadir}/myspell/bn_IN.dic
cp -P bn_BD/bn_BD.dic %{buildroot}%{_datadir}/hunspell/bn_BD.dic
ln -s %{_datadir}/hunspell/bn_BD.dic %{buildroot}%{_datadir}/myspell/bn_BD.dic
mkdir -p %{buildroot}%{_docdir}/myspell-bn_BD
cp -P bn_BD/COPYING %{buildroot}%{_docdir}/myspell-bn_BD/COPYING
cp -P bn_BD/description.xml %{buildroot}%{_docdir}/myspell-bn_BD/description.xml
cp -P bn_BD/dictionaries.xcu %{buildroot}%{_docdir}/myspell-bn_BD/dictionaries.xcu
ln -s %{_datadir}/hunspell/bo.aff %{buildroot}%{_datadir}/hunspell/bo_CN.aff
ln -s %{_datadir}/hunspell/bo_CN.aff %{buildroot}%{_datadir}/myspell/bo_CN.aff
ln -s %{_datadir}/hunspell/bo.aff %{buildroot}%{_datadir}/hunspell/bo_IN.aff
ln -s %{_datadir}/hunspell/bo_IN.aff %{buildroot}%{_datadir}/myspell/bo_IN.aff
cp -P bo/bo.aff %{buildroot}%{_datadir}/hunspell/bo.aff
ln -s %{_datadir}/hunspell/bo.aff %{buildroot}%{_datadir}/myspell/bo.aff
ln -s %{_datadir}/hunspell/bo.dic %{buildroot}%{_datadir}/hunspell/bo_CN.dic
ln -s %{_datadir}/hunspell/bo_CN.dic %{buildroot}%{_datadir}/myspell/bo_CN.dic
ln -s %{_datadir}/hunspell/bo.dic %{buildroot}%{_datadir}/hunspell/bo_IN.dic
ln -s %{_datadir}/hunspell/bo_IN.dic %{buildroot}%{_datadir}/myspell/bo_IN.dic
cp -P bo/bo.dic %{buildroot}%{_datadir}/hunspell/bo.dic
ln -s %{_datadir}/hunspell/bo.dic %{buildroot}%{_datadir}/myspell/bo.dic
mkdir -p %{buildroot}%{_docdir}/myspell-bo
cp -P bo/description.xml %{buildroot}%{_docdir}/myspell-bo/description.xml
cp -P bo/dictionaries.xcu %{buildroot}%{_docdir}/myspell-bo/dictionaries.xcu
cp -P br_FR/br_FR.aff %{buildroot}%{_datadir}/hunspell/br_FR.aff
ln -s %{_datadir}/hunspell/br_FR.aff %{buildroot}%{_datadir}/myspell/br_FR.aff
cp -P br_FR/br_FR.dic %{buildroot}%{_datadir}/hunspell/br_FR.dic
ln -s %{_datadir}/hunspell/br_FR.dic %{buildroot}%{_datadir}/myspell/br_FR.dic
mkdir -p %{buildroot}%{_docdir}/myspell-br_FR
cp -P br_FR/LICENSES-en.txt %{buildroot}%{_docdir}/myspell-br_FR/LICENSES-en.txt
cp -P br_FR/description.xml %{buildroot}%{_docdir}/myspell-br_FR/description.xml
cp -P br_FR/dictionaries.xcu %{buildroot}%{_docdir}/myspell-br_FR/dictionaries.xcu
ln -s %{_datadir}/hunspell/bs_BA.aff %{buildroot}%{_datadir}/hunspell/bs.aff
ln -s %{_datadir}/hunspell/bs.aff %{buildroot}%{_datadir}/myspell/bs.aff
cp -P bs_BA/bs_BA.aff %{buildroot}%{_datadir}/hunspell/bs_BA.aff
ln -s %{_datadir}/hunspell/bs_BA.aff %{buildroot}%{_datadir}/myspell/bs_BA.aff
ln -s %{_datadir}/hunspell/bs_BA.dic %{buildroot}%{_datadir}/hunspell/bs.dic
ln -s %{_datadir}/hunspell/bs.dic %{buildroot}%{_datadir}/myspell/bs.dic
cp -P bs_BA/bs_BA.dic %{buildroot}%{_datadir}/hunspell/bs_BA.dic
ln -s %{_datadir}/hunspell/bs_BA.dic %{buildroot}%{_datadir}/myspell/bs_BA.dic
mkdir -p %{buildroot}%{_docdir}/myspell-bs_BA
cp -P bs_BA/README.txt %{buildroot}%{_docdir}/myspell-bs_BA/README.txt
cp -P bs_BA/description.xml %{buildroot}%{_docdir}/myspell-bs_BA/description.xml
cp -P bs_BA/dictionaries.xcu %{buildroot}%{_docdir}/myspell-bs_BA/dictionaries.xcu
ln -s %{_datadir}/hunspell/ca.aff %{buildroot}%{_datadir}/hunspell/ca_ES.aff
ln -s %{_datadir}/hunspell/ca_ES.aff %{buildroot}%{_datadir}/myspell/ca_ES.aff
ln -s %{_datadir}/hunspell/ca.aff %{buildroot}%{_datadir}/hunspell/ca_AD.aff
ln -s %{_datadir}/hunspell/ca_AD.aff %{buildroot}%{_datadir}/myspell/ca_AD.aff
ln -s %{_datadir}/hunspell/ca.aff %{buildroot}%{_datadir}/hunspell/ca_FR.aff
ln -s %{_datadir}/hunspell/ca_FR.aff %{buildroot}%{_datadir}/myspell/ca_FR.aff
ln -s %{_datadir}/hunspell/ca.aff %{buildroot}%{_datadir}/hunspell/ca_IT.aff
ln -s %{_datadir}/hunspell/ca_IT.aff %{buildroot}%{_datadir}/myspell/ca_IT.aff
cp -P ca/ca.aff %{buildroot}%{_datadir}/hunspell/ca.aff
ln -s %{_datadir}/hunspell/ca.aff %{buildroot}%{_datadir}/myspell/ca.aff
ln -s %{_datadir}/hunspell/ca.dic %{buildroot}%{_datadir}/hunspell/ca_ES.dic
ln -s %{_datadir}/hunspell/ca_ES.dic %{buildroot}%{_datadir}/myspell/ca_ES.dic
ln -s %{_datadir}/hunspell/ca.dic %{buildroot}%{_datadir}/hunspell/ca_AD.dic
ln -s %{_datadir}/hunspell/ca_AD.dic %{buildroot}%{_datadir}/myspell/ca_AD.dic
ln -s %{_datadir}/hunspell/ca.dic %{buildroot}%{_datadir}/hunspell/ca_FR.dic
ln -s %{_datadir}/hunspell/ca_FR.dic %{buildroot}%{_datadir}/myspell/ca_FR.dic
ln -s %{_datadir}/hunspell/ca.dic %{buildroot}%{_datadir}/hunspell/ca_IT.dic
ln -s %{_datadir}/hunspell/ca_IT.dic %{buildroot}%{_datadir}/myspell/ca_IT.dic
cp -P ca/ca.dic %{buildroot}%{_datadir}/hunspell/ca.dic
ln -s %{_datadir}/hunspell/ca.dic %{buildroot}%{_datadir}/myspell/ca.dic
cp -P ca/ca_ES_valencia.aff %{buildroot}%{_datadir}/hunspell/ca_ES_valencia.aff
ln -s %{_datadir}/hunspell/ca_ES_valencia.aff %{buildroot}%{_datadir}/myspell/ca_ES_valencia.aff
cp -P ca/ca_ES_valencia.dic %{buildroot}%{_datadir}/hunspell/ca_ES_valencia.dic
ln -s %{_datadir}/hunspell/ca_ES_valencia.dic %{buildroot}%{_datadir}/myspell/ca_ES_valencia.dic
ln -s %{_datadir}/hyphen/hyph_ca.dic %{buildroot}%{_datadir}/hyphen/hyph_ca_ES.dic
ln -s %{_datadir}/hyphen/hyph_ca_ES.dic %{buildroot}%{_datadir}/myspell/hyph_ca_ES.dic
ln -s %{_datadir}/hyphen/hyph_ca.dic %{buildroot}%{_datadir}/hyphen/hyph_ca_ES_valencia.dic
ln -s %{_datadir}/hyphen/hyph_ca_ES_valencia.dic %{buildroot}%{_datadir}/myspell/hyph_ca_ES_valencia.dic
ln -s %{_datadir}/hyphen/hyph_ca.dic %{buildroot}%{_datadir}/hyphen/hyph_ca_AD.dic
ln -s %{_datadir}/hyphen/hyph_ca_AD.dic %{buildroot}%{_datadir}/myspell/hyph_ca_AD.dic
ln -s %{_datadir}/hyphen/hyph_ca.dic %{buildroot}%{_datadir}/hyphen/hyph_ca_FR.dic
ln -s %{_datadir}/hyphen/hyph_ca_FR.dic %{buildroot}%{_datadir}/myspell/hyph_ca_FR.dic
ln -s %{_datadir}/hyphen/hyph_ca.dic %{buildroot}%{_datadir}/hyphen/hyph_ca_IT.dic
ln -s %{_datadir}/hyphen/hyph_ca_IT.dic %{buildroot}%{_datadir}/myspell/hyph_ca_IT.dic
cp -P ca/hyph_ca.dic %{buildroot}%{_datadir}/hyphen/hyph_ca.dic
ln -s %{_datadir}/hyphen/hyph_ca.dic %{buildroot}%{_datadir}/myspell/hyph_ca.dic
ln -s %{_datadir}/mythes/th_ca_ES_v3.dat %{buildroot}%{_datadir}/mythes/th_ca_ES_v2.dat
ln -s %{_datadir}/mythes/th_ca_ES_v2.dat %{buildroot}%{_datadir}/myspell/th_ca_ES_v2.dat
ln -s %{_datadir}/mythes/th_ca_ES_v3.dat %{buildroot}%{_datadir}/mythes/th_ca_ES_valencia_v2.dat
ln -s %{_datadir}/mythes/th_ca_ES_valencia_v2.dat %{buildroot}%{_datadir}/myspell/th_ca_ES_valencia_v2.dat
ln -s %{_datadir}/mythes/th_ca_ES_v3.dat %{buildroot}%{_datadir}/mythes/th_ca_AD_v2.dat
ln -s %{_datadir}/mythes/th_ca_AD_v2.dat %{buildroot}%{_datadir}/myspell/th_ca_AD_v2.dat
ln -s %{_datadir}/mythes/th_ca_ES_v3.dat %{buildroot}%{_datadir}/mythes/th_ca_FR_v2.dat
ln -s %{_datadir}/mythes/th_ca_FR_v2.dat %{buildroot}%{_datadir}/myspell/th_ca_FR_v2.dat
ln -s %{_datadir}/mythes/th_ca_ES_v3.dat %{buildroot}%{_datadir}/mythes/th_ca_IT_v2.dat
ln -s %{_datadir}/mythes/th_ca_IT_v2.dat %{buildroot}%{_datadir}/myspell/th_ca_IT_v2.dat
cp -P ca/th_ca_ES_v3.dat %{buildroot}%{_datadir}/mythes/th_ca_ES_v3.dat
ln -s %{_datadir}/mythes/th_ca_ES_v3.dat %{buildroot}%{_datadir}/myspell/th_ca_ES_v3.dat
ln -s %{_datadir}/mythes/th_ca_ES_v3.idx %{buildroot}%{_datadir}/mythes/th_ca_ES_v2.idx
ln -s %{_datadir}/mythes/th_ca_ES_v2.idx %{buildroot}%{_datadir}/myspell/th_ca_ES_v2.idx
ln -s %{_datadir}/mythes/th_ca_ES_v3.idx %{buildroot}%{_datadir}/mythes/th_ca_ES_valencia_v2.idx
ln -s %{_datadir}/mythes/th_ca_ES_valencia_v2.idx %{buildroot}%{_datadir}/myspell/th_ca_ES_valencia_v2.idx
ln -s %{_datadir}/mythes/th_ca_ES_v3.idx %{buildroot}%{_datadir}/mythes/th_ca_AD_v2.idx
ln -s %{_datadir}/mythes/th_ca_AD_v2.idx %{buildroot}%{_datadir}/myspell/th_ca_AD_v2.idx
ln -s %{_datadir}/mythes/th_ca_ES_v3.idx %{buildroot}%{_datadir}/mythes/th_ca_FR_v2.idx
ln -s %{_datadir}/mythes/th_ca_FR_v2.idx %{buildroot}%{_datadir}/myspell/th_ca_FR_v2.idx
ln -s %{_datadir}/mythes/th_ca_ES_v3.idx %{buildroot}%{_datadir}/mythes/th_ca_IT_v2.idx
ln -s %{_datadir}/mythes/th_ca_IT_v2.idx %{buildroot}%{_datadir}/myspell/th_ca_IT_v2.idx
cp -P ca/th_ca_ES_v3.idx %{buildroot}%{_datadir}/mythes/th_ca_ES_v3.idx
ln -s %{_datadir}/mythes/th_ca_ES_v3.idx %{buildroot}%{_datadir}/myspell/th_ca_ES_v3.idx
mkdir -p %{buildroot}%{_docdir}/myspell-ca
cp -P ca/LICENSES-en.txt %{buildroot}%{_docdir}/myspell-ca/LICENSES-en.txt
cp -P ca/LLICENCIES-ca.txt %{buildroot}%{_docdir}/myspell-ca/LLICENCIES-ca.txt
cp -P ca/README_ca.txt %{buildroot}%{_docdir}/myspell-ca/README_ca.txt
cp -P ca/README_hyph_ca.txt %{buildroot}%{_docdir}/myspell-ca/README_hyph_ca.txt
cp -P ca/README_thes_ca.txt %{buildroot}%{_docdir}/myspell-ca/README_thes_ca.txt
cp -P ca/description.xml %{buildroot}%{_docdir}/myspell-ca/description.xml
cp -P ca/dictionaries.xcu %{buildroot}%{_docdir}/myspell-ca/dictionaries.xcu
cp -P ca/package-description.txt %{buildroot}%{_docdir}/myspell-ca/package-description.txt
cp -P cs_CZ/cs_CZ.aff %{buildroot}%{_datadir}/hunspell/cs_CZ.aff
ln -s %{_datadir}/hunspell/cs_CZ.aff %{buildroot}%{_datadir}/myspell/cs_CZ.aff
cp -P cs_CZ/cs_CZ.dic %{buildroot}%{_datadir}/hunspell/cs_CZ.dic
ln -s %{_datadir}/hunspell/cs_CZ.dic %{buildroot}%{_datadir}/myspell/cs_CZ.dic
cp -P cs_CZ/hyph_cs_CZ.dic %{buildroot}%{_datadir}/hyphen/hyph_cs_CZ.dic
ln -s %{_datadir}/hyphen/hyph_cs_CZ.dic %{buildroot}%{_datadir}/myspell/hyph_cs_CZ.dic
ln -s %{_datadir}/mythes/thes_cs_CZ.dat %{buildroot}%{_datadir}/mythes/th_cs_CZ_v2.dat
ln -s %{_datadir}/mythes/th_cs_CZ_v2.dat %{buildroot}%{_datadir}/myspell/th_cs_CZ_v2.dat
cp -P cs_CZ/thes_cs_CZ.dat %{buildroot}%{_datadir}/mythes/thes_cs_CZ.dat
ln -s %{_datadir}/mythes/thes_cs_CZ.dat %{buildroot}%{_datadir}/myspell/thes_cs_CZ.dat
ln -s %{_datadir}/mythes/thes_cs_CZ.idx %{buildroot}%{_datadir}/mythes/th_cs_CZ_v2.idx
ln -s %{_datadir}/mythes/th_cs_CZ_v2.idx %{buildroot}%{_datadir}/myspell/th_cs_CZ_v2.idx
cp -P cs_CZ/thes_cs_CZ.idx %{buildroot}%{_datadir}/mythes/thes_cs_CZ.idx
ln -s %{_datadir}/mythes/thes_cs_CZ.idx %{buildroot}%{_datadir}/myspell/thes_cs_CZ.idx
mkdir -p %{buildroot}%{_docdir}/myspell-cs_CZ
cp -P cs_CZ/README_cs.txt %{buildroot}%{_docdir}/myspell-cs_CZ/README_cs.txt
cp -P cs_CZ/README_en.txt %{buildroot}%{_docdir}/myspell-cs_CZ/README_en.txt
cp -P cs_CZ/description.xml %{buildroot}%{_docdir}/myspell-cs_CZ/description.xml
cp -P cs_CZ/dictionaries.xcu %{buildroot}%{_docdir}/myspell-cs_CZ/dictionaries.xcu
cp -P da_DK/da_DK.aff %{buildroot}%{_datadir}/hunspell/da_DK.aff
ln -s %{_datadir}/hunspell/da_DK.aff %{buildroot}%{_datadir}/myspell/da_DK.aff
cp -P da_DK/da_DK.dic %{buildroot}%{_datadir}/hunspell/da_DK.dic
ln -s %{_datadir}/hunspell/da_DK.dic %{buildroot}%{_datadir}/myspell/da_DK.dic
cp -P da_DK/hyph_da_DK.dic %{buildroot}%{_datadir}/hyphen/hyph_da_DK.dic
ln -s %{_datadir}/hyphen/hyph_da_DK.dic %{buildroot}%{_datadir}/myspell/hyph_da_DK.dic
ln -s %{_datadir}/mythes/th_da_DK.dat %{buildroot}%{_datadir}/mythes/th_da_DK_v2.dat
ln -s %{_datadir}/mythes/th_da_DK_v2.dat %{buildroot}%{_datadir}/myspell/th_da_DK_v2.dat
cp -P da_DK/th_da_DK.dat %{buildroot}%{_datadir}/mythes/th_da_DK.dat
ln -s %{_datadir}/mythes/th_da_DK.dat %{buildroot}%{_datadir}/myspell/th_da_DK.dat
ln -s %{_datadir}/mythes/th_da_DK.idx %{buildroot}%{_datadir}/mythes/th_da_DK_v2.idx
ln -s %{_datadir}/mythes/th_da_DK_v2.idx %{buildroot}%{_datadir}/myspell/th_da_DK_v2.idx
cp -P da_DK/th_da_DK.idx %{buildroot}%{_datadir}/mythes/th_da_DK.idx
ln -s %{_datadir}/mythes/th_da_DK.idx %{buildroot}%{_datadir}/myspell/th_da_DK.idx
mkdir -p %{buildroot}%{_docdir}/myspell-da_DK
cp -P da_DK/HYPH_da_DK_README.txt %{buildroot}%{_docdir}/myspell-da_DK/HYPH_da_DK_README.txt
cp -P da_DK/README_da_DK.txt %{buildroot}%{_docdir}/myspell-da_DK/README_da_DK.txt
cp -P da_DK/README_th_da_DK.txt %{buildroot}%{_docdir}/myspell-da_DK/README_th_da_DK.txt
cp -P da_DK/README_th_en-US.txt %{buildroot}%{_docdir}/myspell-da_DK/README_th_en-US.txt
cp -P da_DK/Trold_42x42.png %{buildroot}%{_docdir}/myspell-da_DK/Trold_42x42.png
cp -P da_DK/desc_da_DK.txt %{buildroot}%{_docdir}/myspell-da_DK/desc_da_DK.txt
cp -P da_DK/desc_en_US.txt %{buildroot}%{_docdir}/myspell-da_DK/desc_en_US.txt
cp -P da_DK/description.xml %{buildroot}%{_docdir}/myspell-da_DK/description.xml
cp -P da_DK/dictionaries.xcu %{buildroot}%{_docdir}/myspell-da_DK/dictionaries.xcu
cp -P da_DK/th_desc_da_DK.txt %{buildroot}%{_docdir}/myspell-da_DK/th_desc_da_DK.txt
cp -P da_DK/th_desc_en_US.txt %{buildroot}%{_docdir}/myspell-da_DK/th_desc_en_US.txt
cp -P de/de_AT.aff %{buildroot}%{_datadir}/hunspell/de_AT.aff
ln -s %{_datadir}/hunspell/de_AT.aff %{buildroot}%{_datadir}/myspell/de_AT.aff
cp -P de/de_AT.dic %{buildroot}%{_datadir}/hunspell/de_AT.dic
ln -s %{_datadir}/hunspell/de_AT.dic %{buildroot}%{_datadir}/myspell/de_AT.dic
cp -P de/de_CH.aff %{buildroot}%{_datadir}/hunspell/de_CH.aff
ln -s %{_datadir}/hunspell/de_CH.aff %{buildroot}%{_datadir}/myspell/de_CH.aff
cp -P de/de_CH.dic %{buildroot}%{_datadir}/hunspell/de_CH.dic
ln -s %{_datadir}/hunspell/de_CH.dic %{buildroot}%{_datadir}/myspell/de_CH.dic
cp -P de/de_DE.aff %{buildroot}%{_datadir}/hunspell/de_DE.aff
ln -s %{_datadir}/hunspell/de_DE.aff %{buildroot}%{_datadir}/myspell/de_DE.aff
cp -P de/de_DE.dic %{buildroot}%{_datadir}/hunspell/de_DE.dic
ln -s %{_datadir}/hunspell/de_DE.dic %{buildroot}%{_datadir}/myspell/de_DE.dic
cp -P de/hyph_de_AT.dic %{buildroot}%{_datadir}/hyphen/hyph_de_AT.dic
ln -s %{_datadir}/hyphen/hyph_de_AT.dic %{buildroot}%{_datadir}/myspell/hyph_de_AT.dic
cp -P de/hyph_de_CH.dic %{buildroot}%{_datadir}/hyphen/hyph_de_CH.dic
ln -s %{_datadir}/hyphen/hyph_de_CH.dic %{buildroot}%{_datadir}/myspell/hyph_de_CH.dic
cp -P de/hyph_de_DE.dic %{buildroot}%{_datadir}/hyphen/hyph_de_DE.dic
ln -s %{_datadir}/hyphen/hyph_de_DE.dic %{buildroot}%{_datadir}/myspell/hyph_de_DE.dic
cp -P de/th_de_CH_v2.dat %{buildroot}%{_datadir}/mythes/th_de_CH_v2.dat
ln -s %{_datadir}/mythes/th_de_CH_v2.dat %{buildroot}%{_datadir}/myspell/th_de_CH_v2.dat
cp -P de/th_de_CH_v2.idx %{buildroot}%{_datadir}/mythes/th_de_CH_v2.idx
ln -s %{_datadir}/mythes/th_de_CH_v2.idx %{buildroot}%{_datadir}/myspell/th_de_CH_v2.idx
cp -P de/th_de_DE_v2.dat %{buildroot}%{_datadir}/mythes/th_de_DE_v2.dat
ln -s %{_datadir}/mythes/th_de_DE_v2.dat %{buildroot}%{_datadir}/myspell/th_de_DE_v2.dat
ln -s %{_datadir}/mythes/th_de_DE_v2.dat %{buildroot}%{_datadir}/mythes/th_de_AT_v2.dat
ln -s %{_datadir}/mythes/th_de_AT_v2.dat %{buildroot}%{_datadir}/myspell/th_de_AT_v2.dat
cp -P de/th_de_DE_v2.idx %{buildroot}%{_datadir}/mythes/th_de_DE_v2.idx
ln -s %{_datadir}/mythes/th_de_DE_v2.idx %{buildroot}%{_datadir}/myspell/th_de_DE_v2.idx
ln -s %{_datadir}/mythes/th_de_DE_v2.idx %{buildroot}%{_datadir}/mythes/th_de_AT_v2.idx
ln -s %{_datadir}/mythes/th_de_AT_v2.idx %{buildroot}%{_datadir}/myspell/th_de_AT_v2.idx
mkdir -p %{buildroot}%{_docdir}/myspell-de
cp -P de/COPYING_GPLv2 %{buildroot}%{_docdir}/myspell-de/COPYING_GPLv2
cp -P de/COPYING_GPLv3 %{buildroot}%{_docdir}/myspell-de/COPYING_GPLv3
cp -P de/COPYING_LGPL_v2.0.txt %{buildroot}%{_docdir}/myspell-de/COPYING_LGPL_v2.0.txt
cp -P de/COPYING_LGPL_v2.1.txt %{buildroot}%{_docdir}/myspell-de/COPYING_LGPL_v2.1.txt
cp -P de/COPYING_OASIS.txt %{buildroot}%{_docdir}/myspell-de/COPYING_OASIS.txt
cp -P de/README_de_DE_frami.txt %{buildroot}%{_docdir}/myspell-de/README_de_DE_frami.txt
cp -P de/README_extension_owner.txt %{buildroot}%{_docdir}/myspell-de/README_extension_owner.txt
cp -P de/README_hyph_de.txt %{buildroot}%{_docdir}/myspell-de/README_hyph_de.txt
cp -P de/README_thesaurus.txt %{buildroot}%{_docdir}/myspell-de/README_thesaurus.txt
cp -P de/description.xml %{buildroot}%{_docdir}/myspell-de/description.xml
cp -P de/dictionaries.xcu %{buildroot}%{_docdir}/myspell-de/dictionaries.xcu
cp -P el_GR/el_GR.aff %{buildroot}%{_datadir}/hunspell/el_GR.aff
ln -s %{_datadir}/hunspell/el_GR.aff %{buildroot}%{_datadir}/myspell/el_GR.aff
cp -P el_GR/el_GR.dic %{buildroot}%{_datadir}/hunspell/el_GR.dic
ln -s %{_datadir}/hunspell/el_GR.dic %{buildroot}%{_datadir}/myspell/el_GR.dic
cp -P el_GR/hyph_el_GR.dic %{buildroot}%{_datadir}/hyphen/hyph_el_GR.dic
ln -s %{_datadir}/hyphen/hyph_el_GR.dic %{buildroot}%{_datadir}/myspell/hyph_el_GR.dic
mkdir -p %{buildroot}%{_docdir}/myspell-el_GR
cp -P el_GR/README_el_GR.txt %{buildroot}%{_docdir}/myspell-el_GR/README_el_GR.txt
cp -P el_GR/README_hyph_el_GR.txt %{buildroot}%{_docdir}/myspell-el_GR/README_hyph_el_GR.txt
cp -P el_GR/description.xml %{buildroot}%{_docdir}/myspell-el_GR/description.xml
cp -P el_GR/dictionaries.xcu %{buildroot}%{_docdir}/myspell-el_GR/dictionaries.xcu
cp -P en/en_AU.aff %{buildroot}%{_datadir}/hunspell/en_AU.aff
ln -s %{_datadir}/hunspell/en_AU.aff %{buildroot}%{_datadir}/myspell/en_AU.aff
cp -P en/en_AU.dic %{buildroot}%{_datadir}/hunspell/en_AU.dic
ln -s %{_datadir}/hunspell/en_AU.dic %{buildroot}%{_datadir}/myspell/en_AU.dic
cp -P en/en_CA.aff %{buildroot}%{_datadir}/hunspell/en_CA.aff
ln -s %{_datadir}/hunspell/en_CA.aff %{buildroot}%{_datadir}/myspell/en_CA.aff
cp -P en/en_CA.dic %{buildroot}%{_datadir}/hunspell/en_CA.dic
ln -s %{_datadir}/hunspell/en_CA.dic %{buildroot}%{_datadir}/myspell/en_CA.dic
cp -P en/en_GB.aff %{buildroot}%{_datadir}/hunspell/en_GB.aff
ln -s %{_datadir}/hunspell/en_GB.aff %{buildroot}%{_datadir}/myspell/en_GB.aff
ln -s %{_datadir}/hunspell/en_GB.aff %{buildroot}%{_datadir}/hunspell/en_BS.aff
ln -s %{_datadir}/hunspell/en_BS.aff %{buildroot}%{_datadir}/myspell/en_BS.aff
ln -s %{_datadir}/hunspell/en_GB.aff %{buildroot}%{_datadir}/hunspell/en_BZ.aff
ln -s %{_datadir}/hunspell/en_BZ.aff %{buildroot}%{_datadir}/myspell/en_BZ.aff
ln -s %{_datadir}/hunspell/en_GB.aff %{buildroot}%{_datadir}/hunspell/en_GH.aff
ln -s %{_datadir}/hunspell/en_GH.aff %{buildroot}%{_datadir}/myspell/en_GH.aff
ln -s %{_datadir}/hunspell/en_GB.aff %{buildroot}%{_datadir}/hunspell/en_IE.aff
ln -s %{_datadir}/hunspell/en_IE.aff %{buildroot}%{_datadir}/myspell/en_IE.aff
ln -s %{_datadir}/hunspell/en_GB.aff %{buildroot}%{_datadir}/hunspell/en_IN.aff
ln -s %{_datadir}/hunspell/en_IN.aff %{buildroot}%{_datadir}/myspell/en_IN.aff
ln -s %{_datadir}/hunspell/en_GB.aff %{buildroot}%{_datadir}/hunspell/en_JM.aff
ln -s %{_datadir}/hunspell/en_JM.aff %{buildroot}%{_datadir}/myspell/en_JM.aff
ln -s %{_datadir}/hunspell/en_GB.aff %{buildroot}%{_datadir}/hunspell/en_NZ.aff
ln -s %{_datadir}/hunspell/en_NZ.aff %{buildroot}%{_datadir}/myspell/en_NZ.aff
ln -s %{_datadir}/hunspell/en_GB.aff %{buildroot}%{_datadir}/hunspell/en_TT.aff
ln -s %{_datadir}/hunspell/en_TT.aff %{buildroot}%{_datadir}/myspell/en_TT.aff
cp -P en/en_GB.dic %{buildroot}%{_datadir}/hunspell/en_GB.dic
ln -s %{_datadir}/hunspell/en_GB.dic %{buildroot}%{_datadir}/myspell/en_GB.dic
ln -s %{_datadir}/hunspell/en_GB.dic %{buildroot}%{_datadir}/hunspell/en_BS.dic
ln -s %{_datadir}/hunspell/en_BS.dic %{buildroot}%{_datadir}/myspell/en_BS.dic
ln -s %{_datadir}/hunspell/en_GB.dic %{buildroot}%{_datadir}/hunspell/en_BZ.dic
ln -s %{_datadir}/hunspell/en_BZ.dic %{buildroot}%{_datadir}/myspell/en_BZ.dic
ln -s %{_datadir}/hunspell/en_GB.dic %{buildroot}%{_datadir}/hunspell/en_GH.dic
ln -s %{_datadir}/hunspell/en_GH.dic %{buildroot}%{_datadir}/myspell/en_GH.dic
ln -s %{_datadir}/hunspell/en_GB.dic %{buildroot}%{_datadir}/hunspell/en_IE.dic
ln -s %{_datadir}/hunspell/en_IE.dic %{buildroot}%{_datadir}/myspell/en_IE.dic
ln -s %{_datadir}/hunspell/en_GB.dic %{buildroot}%{_datadir}/hunspell/en_IN.dic
ln -s %{_datadir}/hunspell/en_IN.dic %{buildroot}%{_datadir}/myspell/en_IN.dic
ln -s %{_datadir}/hunspell/en_GB.dic %{buildroot}%{_datadir}/hunspell/en_JM.dic
ln -s %{_datadir}/hunspell/en_JM.dic %{buildroot}%{_datadir}/myspell/en_JM.dic
ln -s %{_datadir}/hunspell/en_GB.dic %{buildroot}%{_datadir}/hunspell/en_NZ.dic
ln -s %{_datadir}/hunspell/en_NZ.dic %{buildroot}%{_datadir}/myspell/en_NZ.dic
ln -s %{_datadir}/hunspell/en_GB.dic %{buildroot}%{_datadir}/hunspell/en_TT.dic
ln -s %{_datadir}/hunspell/en_TT.dic %{buildroot}%{_datadir}/myspell/en_TT.dic
cp -P en/en_US.aff %{buildroot}%{_datadir}/hunspell/en_US.aff
ln -s %{_datadir}/hunspell/en_US.aff %{buildroot}%{_datadir}/myspell/en_US.aff
ln -s %{_datadir}/hunspell/en_US.aff %{buildroot}%{_datadir}/hunspell/en_PH.aff
ln -s %{_datadir}/hunspell/en_PH.aff %{buildroot}%{_datadir}/myspell/en_PH.aff
cp -P en/en_US.dic %{buildroot}%{_datadir}/hunspell/en_US.dic
ln -s %{_datadir}/hunspell/en_US.dic %{buildroot}%{_datadir}/myspell/en_US.dic
ln -s %{_datadir}/hunspell/en_US.dic %{buildroot}%{_datadir}/hunspell/en_PH.dic
ln -s %{_datadir}/hunspell/en_PH.dic %{buildroot}%{_datadir}/myspell/en_PH.dic
cp -P en/en_ZA.aff %{buildroot}%{_datadir}/hunspell/en_ZA.aff
ln -s %{_datadir}/hunspell/en_ZA.aff %{buildroot}%{_datadir}/myspell/en_ZA.aff
ln -s %{_datadir}/hunspell/en_ZA.aff %{buildroot}%{_datadir}/hunspell/en_MW.aff
ln -s %{_datadir}/hunspell/en_MW.aff %{buildroot}%{_datadir}/myspell/en_MW.aff
ln -s %{_datadir}/hunspell/en_ZA.aff %{buildroot}%{_datadir}/hunspell/en_NA.aff
ln -s %{_datadir}/hunspell/en_NA.aff %{buildroot}%{_datadir}/myspell/en_NA.aff
ln -s %{_datadir}/hunspell/en_ZA.aff %{buildroot}%{_datadir}/hunspell/en_ZW.aff
ln -s %{_datadir}/hunspell/en_ZW.aff %{buildroot}%{_datadir}/myspell/en_ZW.aff
cp -P en/en_ZA.dic %{buildroot}%{_datadir}/hunspell/en_ZA.dic
ln -s %{_datadir}/hunspell/en_ZA.dic %{buildroot}%{_datadir}/myspell/en_ZA.dic
ln -s %{_datadir}/hunspell/en_ZA.dic %{buildroot}%{_datadir}/hunspell/en_MW.dic
ln -s %{_datadir}/hunspell/en_MW.dic %{buildroot}%{_datadir}/myspell/en_MW.dic
ln -s %{_datadir}/hunspell/en_ZA.dic %{buildroot}%{_datadir}/hunspell/en_NA.dic
ln -s %{_datadir}/hunspell/en_NA.dic %{buildroot}%{_datadir}/myspell/en_NA.dic
ln -s %{_datadir}/hunspell/en_ZA.dic %{buildroot}%{_datadir}/hunspell/en_ZW.dic
ln -s %{_datadir}/hunspell/en_ZW.dic %{buildroot}%{_datadir}/myspell/en_ZW.dic
cp -P en/hyph_en_GB.dic %{buildroot}%{_datadir}/hyphen/hyph_en_GB.dic
ln -s %{_datadir}/hyphen/hyph_en_GB.dic %{buildroot}%{_datadir}/myspell/hyph_en_GB.dic
ln -s %{_datadir}/hyphen/hyph_en_GB.dic %{buildroot}%{_datadir}/hyphen/hyph_en_ZA.dic
ln -s %{_datadir}/hyphen/hyph_en_ZA.dic %{buildroot}%{_datadir}/myspell/hyph_en_ZA.dic
ln -s %{_datadir}/hyphen/hyph_en_GB.dic %{buildroot}%{_datadir}/hyphen/hyph_en_NA.dic
ln -s %{_datadir}/hyphen/hyph_en_NA.dic %{buildroot}%{_datadir}/myspell/hyph_en_NA.dic
ln -s %{_datadir}/hyphen/hyph_en_GB.dic %{buildroot}%{_datadir}/hyphen/hyph_en_ZW.dic
ln -s %{_datadir}/hyphen/hyph_en_ZW.dic %{buildroot}%{_datadir}/myspell/hyph_en_ZW.dic
ln -s %{_datadir}/hyphen/hyph_en_GB.dic %{buildroot}%{_datadir}/hyphen/hyph_en_AU.dic
ln -s %{_datadir}/hyphen/hyph_en_AU.dic %{buildroot}%{_datadir}/myspell/hyph_en_AU.dic
ln -s %{_datadir}/hyphen/hyph_en_GB.dic %{buildroot}%{_datadir}/hyphen/hyph_en_CA.dic
ln -s %{_datadir}/hyphen/hyph_en_CA.dic %{buildroot}%{_datadir}/myspell/hyph_en_CA.dic
ln -s %{_datadir}/hyphen/hyph_en_GB.dic %{buildroot}%{_datadir}/hyphen/hyph_en_IE.dic
ln -s %{_datadir}/hyphen/hyph_en_IE.dic %{buildroot}%{_datadir}/myspell/hyph_en_IE.dic
ln -s %{_datadir}/hyphen/hyph_en_GB.dic %{buildroot}%{_datadir}/hyphen/hyph_en_IN.dic
ln -s %{_datadir}/hyphen/hyph_en_IN.dic %{buildroot}%{_datadir}/myspell/hyph_en_IN.dic
ln -s %{_datadir}/hyphen/hyph_en_GB.dic %{buildroot}%{_datadir}/hyphen/hyph_en_BZ.dic
ln -s %{_datadir}/hyphen/hyph_en_BZ.dic %{buildroot}%{_datadir}/myspell/hyph_en_BZ.dic
ln -s %{_datadir}/hyphen/hyph_en_GB.dic %{buildroot}%{_datadir}/hyphen/hyph_en_BS.dic
ln -s %{_datadir}/hyphen/hyph_en_BS.dic %{buildroot}%{_datadir}/myspell/hyph_en_BS.dic
ln -s %{_datadir}/hyphen/hyph_en_GB.dic %{buildroot}%{_datadir}/hyphen/hyph_en_GH.dic
ln -s %{_datadir}/hyphen/hyph_en_GH.dic %{buildroot}%{_datadir}/myspell/hyph_en_GH.dic
ln -s %{_datadir}/hyphen/hyph_en_GB.dic %{buildroot}%{_datadir}/hyphen/hyph_en_JM.dic
ln -s %{_datadir}/hyphen/hyph_en_JM.dic %{buildroot}%{_datadir}/myspell/hyph_en_JM.dic
ln -s %{_datadir}/hyphen/hyph_en_GB.dic %{buildroot}%{_datadir}/hyphen/hyph_en_MW.dic
ln -s %{_datadir}/hyphen/hyph_en_MW.dic %{buildroot}%{_datadir}/myspell/hyph_en_MW.dic
ln -s %{_datadir}/hyphen/hyph_en_GB.dic %{buildroot}%{_datadir}/hyphen/hyph_en_NZ.dic
ln -s %{_datadir}/hyphen/hyph_en_NZ.dic %{buildroot}%{_datadir}/myspell/hyph_en_NZ.dic
ln -s %{_datadir}/hyphen/hyph_en_GB.dic %{buildroot}%{_datadir}/hyphen/hyph_en_TT.dic
ln -s %{_datadir}/hyphen/hyph_en_TT.dic %{buildroot}%{_datadir}/myspell/hyph_en_TT.dic
cp -P en/hyph_en_US.dic %{buildroot}%{_datadir}/hyphen/hyph_en_US.dic
ln -s %{_datadir}/hyphen/hyph_en_US.dic %{buildroot}%{_datadir}/myspell/hyph_en_US.dic
ln -s %{_datadir}/hyphen/hyph_en_US.dic %{buildroot}%{_datadir}/hyphen/hyph_en_PH.dic
ln -s %{_datadir}/hyphen/hyph_en_PH.dic %{buildroot}%{_datadir}/myspell/hyph_en_PH.dic
ln -s %{_datadir}/mythes/th_en_US_v2.dat %{buildroot}%{_datadir}/mythes/th_en_GB_v2.dat
ln -s %{_datadir}/mythes/th_en_GB_v2.dat %{buildroot}%{_datadir}/myspell/th_en_GB_v2.dat
cp -P en/th_en_US_v2.dat %{buildroot}%{_datadir}/mythes/th_en_US_v2.dat
ln -s %{_datadir}/mythes/th_en_US_v2.dat %{buildroot}%{_datadir}/myspell/th_en_US_v2.dat
ln -s %{_datadir}/mythes/th_en_US_v2.dat %{buildroot}%{_datadir}/mythes/th_en_PH_v2.dat
ln -s %{_datadir}/mythes/th_en_PH_v2.dat %{buildroot}%{_datadir}/myspell/th_en_PH_v2.dat
ln -s %{_datadir}/mythes/th_en_US_v2.dat %{buildroot}%{_datadir}/mythes/th_en_ZA_v2.dat
ln -s %{_datadir}/mythes/th_en_ZA_v2.dat %{buildroot}%{_datadir}/myspell/th_en_ZA_v2.dat
ln -s %{_datadir}/mythes/th_en_US_v2.dat %{buildroot}%{_datadir}/mythes/th_en_NA_v2.dat
ln -s %{_datadir}/mythes/th_en_NA_v2.dat %{buildroot}%{_datadir}/myspell/th_en_NA_v2.dat
ln -s %{_datadir}/mythes/th_en_US_v2.dat %{buildroot}%{_datadir}/mythes/th_en_ZW_v2.dat
ln -s %{_datadir}/mythes/th_en_ZW_v2.dat %{buildroot}%{_datadir}/myspell/th_en_ZW_v2.dat
ln -s %{_datadir}/mythes/th_en_US_v2.dat %{buildroot}%{_datadir}/mythes/th_en_AU_v2.dat
ln -s %{_datadir}/mythes/th_en_AU_v2.dat %{buildroot}%{_datadir}/myspell/th_en_AU_v2.dat
ln -s %{_datadir}/mythes/th_en_US_v2.dat %{buildroot}%{_datadir}/mythes/th_en_CA_v2.dat
ln -s %{_datadir}/mythes/th_en_CA_v2.dat %{buildroot}%{_datadir}/myspell/th_en_CA_v2.dat
ln -s %{_datadir}/mythes/th_en_US_v2.dat %{buildroot}%{_datadir}/mythes/th_en_IE_v2.dat
ln -s %{_datadir}/mythes/th_en_IE_v2.dat %{buildroot}%{_datadir}/myspell/th_en_IE_v2.dat
ln -s %{_datadir}/mythes/th_en_US_v2.dat %{buildroot}%{_datadir}/mythes/th_en_IN_v2.dat
ln -s %{_datadir}/mythes/th_en_IN_v2.dat %{buildroot}%{_datadir}/myspell/th_en_IN_v2.dat
ln -s %{_datadir}/mythes/th_en_US_v2.dat %{buildroot}%{_datadir}/mythes/th_en_BZ_v2.dat
ln -s %{_datadir}/mythes/th_en_BZ_v2.dat %{buildroot}%{_datadir}/myspell/th_en_BZ_v2.dat
ln -s %{_datadir}/mythes/th_en_US_v2.dat %{buildroot}%{_datadir}/mythes/th_en_BS_v2.dat
ln -s %{_datadir}/mythes/th_en_BS_v2.dat %{buildroot}%{_datadir}/myspell/th_en_BS_v2.dat
ln -s %{_datadir}/mythes/th_en_US_v2.dat %{buildroot}%{_datadir}/mythes/th_en_GH_v2.dat
ln -s %{_datadir}/mythes/th_en_GH_v2.dat %{buildroot}%{_datadir}/myspell/th_en_GH_v2.dat
ln -s %{_datadir}/mythes/th_en_US_v2.dat %{buildroot}%{_datadir}/mythes/th_en_JM_v2.dat
ln -s %{_datadir}/mythes/th_en_JM_v2.dat %{buildroot}%{_datadir}/myspell/th_en_JM_v2.dat
ln -s %{_datadir}/mythes/th_en_US_v2.dat %{buildroot}%{_datadir}/mythes/th_en_MW_v2.dat
ln -s %{_datadir}/mythes/th_en_MW_v2.dat %{buildroot}%{_datadir}/myspell/th_en_MW_v2.dat
ln -s %{_datadir}/mythes/th_en_US_v2.dat %{buildroot}%{_datadir}/mythes/th_en_NZ_v2.dat
ln -s %{_datadir}/mythes/th_en_NZ_v2.dat %{buildroot}%{_datadir}/myspell/th_en_NZ_v2.dat
ln -s %{_datadir}/mythes/th_en_US_v2.dat %{buildroot}%{_datadir}/mythes/th_en_TT_v2.dat
ln -s %{_datadir}/mythes/th_en_TT_v2.dat %{buildroot}%{_datadir}/myspell/th_en_TT_v2.dat
ln -s %{_datadir}/mythes/th_en_US_v2.idx %{buildroot}%{_datadir}/mythes/th_en_GB_v2.idx
ln -s %{_datadir}/mythes/th_en_GB_v2.idx %{buildroot}%{_datadir}/myspell/th_en_GB_v2.idx
cp -P en/th_en_US_v2.idx %{buildroot}%{_datadir}/mythes/th_en_US_v2.idx
ln -s %{_datadir}/mythes/th_en_US_v2.idx %{buildroot}%{_datadir}/myspell/th_en_US_v2.idx
ln -s %{_datadir}/mythes/th_en_US_v2.idx %{buildroot}%{_datadir}/mythes/th_en_PH_v2.idx
ln -s %{_datadir}/mythes/th_en_PH_v2.idx %{buildroot}%{_datadir}/myspell/th_en_PH_v2.idx
ln -s %{_datadir}/mythes/th_en_US_v2.idx %{buildroot}%{_datadir}/mythes/th_en_ZA_v2.idx
ln -s %{_datadir}/mythes/th_en_ZA_v2.idx %{buildroot}%{_datadir}/myspell/th_en_ZA_v2.idx
ln -s %{_datadir}/mythes/th_en_US_v2.idx %{buildroot}%{_datadir}/mythes/th_en_NA_v2.idx
ln -s %{_datadir}/mythes/th_en_NA_v2.idx %{buildroot}%{_datadir}/myspell/th_en_NA_v2.idx
ln -s %{_datadir}/mythes/th_en_US_v2.idx %{buildroot}%{_datadir}/mythes/th_en_ZW_v2.idx
ln -s %{_datadir}/mythes/th_en_ZW_v2.idx %{buildroot}%{_datadir}/myspell/th_en_ZW_v2.idx
ln -s %{_datadir}/mythes/th_en_US_v2.idx %{buildroot}%{_datadir}/mythes/th_en_AU_v2.idx
ln -s %{_datadir}/mythes/th_en_AU_v2.idx %{buildroot}%{_datadir}/myspell/th_en_AU_v2.idx
ln -s %{_datadir}/mythes/th_en_US_v2.idx %{buildroot}%{_datadir}/mythes/th_en_CA_v2.idx
ln -s %{_datadir}/mythes/th_en_CA_v2.idx %{buildroot}%{_datadir}/myspell/th_en_CA_v2.idx
ln -s %{_datadir}/mythes/th_en_US_v2.idx %{buildroot}%{_datadir}/mythes/th_en_IE_v2.idx
ln -s %{_datadir}/mythes/th_en_IE_v2.idx %{buildroot}%{_datadir}/myspell/th_en_IE_v2.idx
ln -s %{_datadir}/mythes/th_en_US_v2.idx %{buildroot}%{_datadir}/mythes/th_en_IN_v2.idx
ln -s %{_datadir}/mythes/th_en_IN_v2.idx %{buildroot}%{_datadir}/myspell/th_en_IN_v2.idx
ln -s %{_datadir}/mythes/th_en_US_v2.idx %{buildroot}%{_datadir}/mythes/th_en_BZ_v2.idx
ln -s %{_datadir}/mythes/th_en_BZ_v2.idx %{buildroot}%{_datadir}/myspell/th_en_BZ_v2.idx
ln -s %{_datadir}/mythes/th_en_US_v2.idx %{buildroot}%{_datadir}/mythes/th_en_BS_v2.idx
ln -s %{_datadir}/mythes/th_en_BS_v2.idx %{buildroot}%{_datadir}/myspell/th_en_BS_v2.idx
ln -s %{_datadir}/mythes/th_en_US_v2.idx %{buildroot}%{_datadir}/mythes/th_en_GH_v2.idx
ln -s %{_datadir}/mythes/th_en_GH_v2.idx %{buildroot}%{_datadir}/myspell/th_en_GH_v2.idx
ln -s %{_datadir}/mythes/th_en_US_v2.idx %{buildroot}%{_datadir}/mythes/th_en_JM_v2.idx
ln -s %{_datadir}/mythes/th_en_JM_v2.idx %{buildroot}%{_datadir}/myspell/th_en_JM_v2.idx
ln -s %{_datadir}/mythes/th_en_US_v2.idx %{buildroot}%{_datadir}/mythes/th_en_MW_v2.idx
ln -s %{_datadir}/mythes/th_en_MW_v2.idx %{buildroot}%{_datadir}/myspell/th_en_MW_v2.idx
ln -s %{_datadir}/mythes/th_en_US_v2.idx %{buildroot}%{_datadir}/mythes/th_en_NZ_v2.idx
ln -s %{_datadir}/mythes/th_en_NZ_v2.idx %{buildroot}%{_datadir}/myspell/th_en_NZ_v2.idx
ln -s %{_datadir}/mythes/th_en_US_v2.idx %{buildroot}%{_datadir}/mythes/th_en_TT_v2.idx
ln -s %{_datadir}/mythes/th_en_TT_v2.idx %{buildroot}%{_datadir}/myspell/th_en_TT_v2.idx
mkdir -p %{buildroot}%{_libdir}/libreoffice/share/extensions/lightproof-en
cp -rP en/Lightproof.components %{buildroot}%{_libdir}/libreoffice/share/extensions/lightproof-en/Lightproof.components
cp -rP en/Lightproof.py %{buildroot}%{_libdir}/libreoffice/share/extensions/lightproof-en/Lightproof.py
cp -rP en/Linguistic.xcu %{buildroot}%{_libdir}/libreoffice/share/extensions/lightproof-en/Linguistic.xcu
cp -rP en/META-INF %{buildroot}%{_libdir}/libreoffice/share/extensions/lightproof-en/META-INF
cp -rP en/description.xml %{buildroot}%{_libdir}/libreoffice/share/extensions/lightproof-en/description.xml
cp -rP en/dialog %{buildroot}%{_libdir}/libreoffice/share/extensions/lightproof-en/dialog
cp -rP en/pythonpath %{buildroot}%{_libdir}/libreoffice/share/extensions/lightproof-en/pythonpath
mkdir -p %{buildroot}%{_docdir}/myspell-en
cp -P en/English.png %{buildroot}%{_docdir}/myspell-en/English.png
cp -P en/Linguistic.xcu %{buildroot}%{_docdir}/myspell-en/Linguistic.xcu
cp -P en/README.txt %{buildroot}%{_docdir}/myspell-en/README.txt
cp -P en/README_en_AU.txt %{buildroot}%{_docdir}/myspell-en/README_en_AU.txt
cp -P en/README_en_CA.txt %{buildroot}%{_docdir}/myspell-en/README_en_CA.txt
cp -P en/README_en_GB.txt %{buildroot}%{_docdir}/myspell-en/README_en_GB.txt
cp -P en/README_en_GB_thes.txt %{buildroot}%{_docdir}/myspell-en/README_en_GB_thes.txt
cp -P en/README_en_US.txt %{buildroot}%{_docdir}/myspell-en/README_en_US.txt
cp -P en/README_en_ZA.txt %{buildroot}%{_docdir}/myspell-en/README_en_ZA.txt
cp -P en/README_hyph_en_GB.txt %{buildroot}%{_docdir}/myspell-en/README_hyph_en_GB.txt
cp -P en/README_hyph_en_US.txt %{buildroot}%{_docdir}/myspell-en/README_hyph_en_US.txt
cp -P en/README_lightproof_en.txt %{buildroot}%{_docdir}/myspell-en/README_lightproof_en.txt
cp -P en/WordNet_license.txt %{buildroot}%{_docdir}/myspell-en/WordNet_license.txt
cp -P en/affDescription.txt %{buildroot}%{_docdir}/myspell-en/affDescription.txt
cp -P en/changelog.txt %{buildroot}%{_docdir}/myspell-en/changelog.txt
cp -P en/description.xml %{buildroot}%{_docdir}/myspell-en/description.xml
cp -P en/dictionaries.xcu %{buildroot}%{_docdir}/myspell-en/dictionaries.xcu
cp -P en/license.txt %{buildroot}%{_docdir}/myspell-en/license.txt
cp -P en/package-description.txt %{buildroot}%{_docdir}/myspell-en/package-description.txt
ln -s %{_datadir}/hunspell/es_ANY.aff %{buildroot}%{_datadir}/hunspell/es_AR.aff
ln -s %{_datadir}/hunspell/es_AR.aff %{buildroot}%{_datadir}/myspell/es_AR.aff
ln -s %{_datadir}/hunspell/es_ANY.aff %{buildroot}%{_datadir}/hunspell/es_BO.aff
ln -s %{_datadir}/hunspell/es_BO.aff %{buildroot}%{_datadir}/myspell/es_BO.aff
ln -s %{_datadir}/hunspell/es_ANY.aff %{buildroot}%{_datadir}/hunspell/es_CL.aff
ln -s %{_datadir}/hunspell/es_CL.aff %{buildroot}%{_datadir}/myspell/es_CL.aff
ln -s %{_datadir}/hunspell/es_ANY.aff %{buildroot}%{_datadir}/hunspell/es_CO.aff
ln -s %{_datadir}/hunspell/es_CO.aff %{buildroot}%{_datadir}/myspell/es_CO.aff
ln -s %{_datadir}/hunspell/es_ANY.aff %{buildroot}%{_datadir}/hunspell/es_CR.aff
ln -s %{_datadir}/hunspell/es_CR.aff %{buildroot}%{_datadir}/myspell/es_CR.aff
ln -s %{_datadir}/hunspell/es_ANY.aff %{buildroot}%{_datadir}/hunspell/es_CU.aff
ln -s %{_datadir}/hunspell/es_CU.aff %{buildroot}%{_datadir}/myspell/es_CU.aff
ln -s %{_datadir}/hunspell/es_ANY.aff %{buildroot}%{_datadir}/hunspell/es_DO.aff
ln -s %{_datadir}/hunspell/es_DO.aff %{buildroot}%{_datadir}/myspell/es_DO.aff
ln -s %{_datadir}/hunspell/es_ANY.aff %{buildroot}%{_datadir}/hunspell/es_EC.aff
ln -s %{_datadir}/hunspell/es_EC.aff %{buildroot}%{_datadir}/myspell/es_EC.aff
ln -s %{_datadir}/hunspell/es_ANY.aff %{buildroot}%{_datadir}/hunspell/es_ES.aff
ln -s %{_datadir}/hunspell/es_ES.aff %{buildroot}%{_datadir}/myspell/es_ES.aff
ln -s %{_datadir}/hunspell/es_ANY.aff %{buildroot}%{_datadir}/hunspell/es_GT.aff
ln -s %{_datadir}/hunspell/es_GT.aff %{buildroot}%{_datadir}/myspell/es_GT.aff
ln -s %{_datadir}/hunspell/es_ANY.aff %{buildroot}%{_datadir}/hunspell/es_HN.aff
ln -s %{_datadir}/hunspell/es_HN.aff %{buildroot}%{_datadir}/myspell/es_HN.aff
ln -s %{_datadir}/hunspell/es_ANY.aff %{buildroot}%{_datadir}/hunspell/es_MX.aff
ln -s %{_datadir}/hunspell/es_MX.aff %{buildroot}%{_datadir}/myspell/es_MX.aff
ln -s %{_datadir}/hunspell/es_ANY.aff %{buildroot}%{_datadir}/hunspell/es_NI.aff
ln -s %{_datadir}/hunspell/es_NI.aff %{buildroot}%{_datadir}/myspell/es_NI.aff
ln -s %{_datadir}/hunspell/es_ANY.aff %{buildroot}%{_datadir}/hunspell/es_PA.aff
ln -s %{_datadir}/hunspell/es_PA.aff %{buildroot}%{_datadir}/myspell/es_PA.aff
ln -s %{_datadir}/hunspell/es_ANY.aff %{buildroot}%{_datadir}/hunspell/es_PE.aff
ln -s %{_datadir}/hunspell/es_PE.aff %{buildroot}%{_datadir}/myspell/es_PE.aff
ln -s %{_datadir}/hunspell/es_ANY.aff %{buildroot}%{_datadir}/hunspell/es_PR.aff
ln -s %{_datadir}/hunspell/es_PR.aff %{buildroot}%{_datadir}/myspell/es_PR.aff
ln -s %{_datadir}/hunspell/es_ANY.aff %{buildroot}%{_datadir}/hunspell/es_PY.aff
ln -s %{_datadir}/hunspell/es_PY.aff %{buildroot}%{_datadir}/myspell/es_PY.aff
ln -s %{_datadir}/hunspell/es_ANY.aff %{buildroot}%{_datadir}/hunspell/es_SV.aff
ln -s %{_datadir}/hunspell/es_SV.aff %{buildroot}%{_datadir}/myspell/es_SV.aff
ln -s %{_datadir}/hunspell/es_ANY.aff %{buildroot}%{_datadir}/hunspell/es_UY.aff
ln -s %{_datadir}/hunspell/es_UY.aff %{buildroot}%{_datadir}/myspell/es_UY.aff
ln -s %{_datadir}/hunspell/es_ANY.aff %{buildroot}%{_datadir}/hunspell/es_VE.aff
ln -s %{_datadir}/hunspell/es_VE.aff %{buildroot}%{_datadir}/myspell/es_VE.aff
cp -P es/es_ANY.aff %{buildroot}%{_datadir}/hunspell/es_ANY.aff
ln -s %{_datadir}/hunspell/es_ANY.aff %{buildroot}%{_datadir}/myspell/es_ANY.aff
ln -s %{_datadir}/hunspell/es_ANY.dic %{buildroot}%{_datadir}/hunspell/es_AR.dic
ln -s %{_datadir}/hunspell/es_AR.dic %{buildroot}%{_datadir}/myspell/es_AR.dic
ln -s %{_datadir}/hunspell/es_ANY.dic %{buildroot}%{_datadir}/hunspell/es_BO.dic
ln -s %{_datadir}/hunspell/es_BO.dic %{buildroot}%{_datadir}/myspell/es_BO.dic
ln -s %{_datadir}/hunspell/es_ANY.dic %{buildroot}%{_datadir}/hunspell/es_CL.dic
ln -s %{_datadir}/hunspell/es_CL.dic %{buildroot}%{_datadir}/myspell/es_CL.dic
ln -s %{_datadir}/hunspell/es_ANY.dic %{buildroot}%{_datadir}/hunspell/es_CO.dic
ln -s %{_datadir}/hunspell/es_CO.dic %{buildroot}%{_datadir}/myspell/es_CO.dic
ln -s %{_datadir}/hunspell/es_ANY.dic %{buildroot}%{_datadir}/hunspell/es_CR.dic
ln -s %{_datadir}/hunspell/es_CR.dic %{buildroot}%{_datadir}/myspell/es_CR.dic
ln -s %{_datadir}/hunspell/es_ANY.dic %{buildroot}%{_datadir}/hunspell/es_CU.dic
ln -s %{_datadir}/hunspell/es_CU.dic %{buildroot}%{_datadir}/myspell/es_CU.dic
ln -s %{_datadir}/hunspell/es_ANY.dic %{buildroot}%{_datadir}/hunspell/es_DO.dic
ln -s %{_datadir}/hunspell/es_DO.dic %{buildroot}%{_datadir}/myspell/es_DO.dic
ln -s %{_datadir}/hunspell/es_ANY.dic %{buildroot}%{_datadir}/hunspell/es_EC.dic
ln -s %{_datadir}/hunspell/es_EC.dic %{buildroot}%{_datadir}/myspell/es_EC.dic
ln -s %{_datadir}/hunspell/es_ANY.dic %{buildroot}%{_datadir}/hunspell/es_ES.dic
ln -s %{_datadir}/hunspell/es_ES.dic %{buildroot}%{_datadir}/myspell/es_ES.dic
ln -s %{_datadir}/hunspell/es_ANY.dic %{buildroot}%{_datadir}/hunspell/es_GT.dic
ln -s %{_datadir}/hunspell/es_GT.dic %{buildroot}%{_datadir}/myspell/es_GT.dic
ln -s %{_datadir}/hunspell/es_ANY.dic %{buildroot}%{_datadir}/hunspell/es_HN.dic
ln -s %{_datadir}/hunspell/es_HN.dic %{buildroot}%{_datadir}/myspell/es_HN.dic
ln -s %{_datadir}/hunspell/es_ANY.dic %{buildroot}%{_datadir}/hunspell/es_MX.dic
ln -s %{_datadir}/hunspell/es_MX.dic %{buildroot}%{_datadir}/myspell/es_MX.dic
ln -s %{_datadir}/hunspell/es_ANY.dic %{buildroot}%{_datadir}/hunspell/es_NI.dic
ln -s %{_datadir}/hunspell/es_NI.dic %{buildroot}%{_datadir}/myspell/es_NI.dic
ln -s %{_datadir}/hunspell/es_ANY.dic %{buildroot}%{_datadir}/hunspell/es_PA.dic
ln -s %{_datadir}/hunspell/es_PA.dic %{buildroot}%{_datadir}/myspell/es_PA.dic
ln -s %{_datadir}/hunspell/es_ANY.dic %{buildroot}%{_datadir}/hunspell/es_PE.dic
ln -s %{_datadir}/hunspell/es_PE.dic %{buildroot}%{_datadir}/myspell/es_PE.dic
ln -s %{_datadir}/hunspell/es_ANY.dic %{buildroot}%{_datadir}/hunspell/es_PR.dic
ln -s %{_datadir}/hunspell/es_PR.dic %{buildroot}%{_datadir}/myspell/es_PR.dic
ln -s %{_datadir}/hunspell/es_ANY.dic %{buildroot}%{_datadir}/hunspell/es_PY.dic
ln -s %{_datadir}/hunspell/es_PY.dic %{buildroot}%{_datadir}/myspell/es_PY.dic
ln -s %{_datadir}/hunspell/es_ANY.dic %{buildroot}%{_datadir}/hunspell/es_SV.dic
ln -s %{_datadir}/hunspell/es_SV.dic %{buildroot}%{_datadir}/myspell/es_SV.dic
ln -s %{_datadir}/hunspell/es_ANY.dic %{buildroot}%{_datadir}/hunspell/es_UY.dic
ln -s %{_datadir}/hunspell/es_UY.dic %{buildroot}%{_datadir}/myspell/es_UY.dic
ln -s %{_datadir}/hunspell/es_ANY.dic %{buildroot}%{_datadir}/hunspell/es_VE.dic
ln -s %{_datadir}/hunspell/es_VE.dic %{buildroot}%{_datadir}/myspell/es_VE.dic
cp -P es/es_ANY.dic %{buildroot}%{_datadir}/hunspell/es_ANY.dic
ln -s %{_datadir}/hunspell/es_ANY.dic %{buildroot}%{_datadir}/myspell/es_ANY.dic
ln -s %{_datadir}/hyphen/hyph_es_ANY.dic %{buildroot}%{_datadir}/hyphen/hyph_es_AR.dic
ln -s %{_datadir}/hyphen/hyph_es_AR.dic %{buildroot}%{_datadir}/myspell/hyph_es_AR.dic
ln -s %{_datadir}/hyphen/hyph_es_ANY.dic %{buildroot}%{_datadir}/hyphen/hyph_es_BO.dic
ln -s %{_datadir}/hyphen/hyph_es_BO.dic %{buildroot}%{_datadir}/myspell/hyph_es_BO.dic
ln -s %{_datadir}/hyphen/hyph_es_ANY.dic %{buildroot}%{_datadir}/hyphen/hyph_es_CL.dic
ln -s %{_datadir}/hyphen/hyph_es_CL.dic %{buildroot}%{_datadir}/myspell/hyph_es_CL.dic
ln -s %{_datadir}/hyphen/hyph_es_ANY.dic %{buildroot}%{_datadir}/hyphen/hyph_es_CO.dic
ln -s %{_datadir}/hyphen/hyph_es_CO.dic %{buildroot}%{_datadir}/myspell/hyph_es_CO.dic
ln -s %{_datadir}/hyphen/hyph_es_ANY.dic %{buildroot}%{_datadir}/hyphen/hyph_es_CR.dic
ln -s %{_datadir}/hyphen/hyph_es_CR.dic %{buildroot}%{_datadir}/myspell/hyph_es_CR.dic
ln -s %{_datadir}/hyphen/hyph_es_ANY.dic %{buildroot}%{_datadir}/hyphen/hyph_es_CU.dic
ln -s %{_datadir}/hyphen/hyph_es_CU.dic %{buildroot}%{_datadir}/myspell/hyph_es_CU.dic
ln -s %{_datadir}/hyphen/hyph_es_ANY.dic %{buildroot}%{_datadir}/hyphen/hyph_es_DO.dic
ln -s %{_datadir}/hyphen/hyph_es_DO.dic %{buildroot}%{_datadir}/myspell/hyph_es_DO.dic
ln -s %{_datadir}/hyphen/hyph_es_ANY.dic %{buildroot}%{_datadir}/hyphen/hyph_es_EC.dic
ln -s %{_datadir}/hyphen/hyph_es_EC.dic %{buildroot}%{_datadir}/myspell/hyph_es_EC.dic
ln -s %{_datadir}/hyphen/hyph_es_ANY.dic %{buildroot}%{_datadir}/hyphen/hyph_es_ES.dic
ln -s %{_datadir}/hyphen/hyph_es_ES.dic %{buildroot}%{_datadir}/myspell/hyph_es_ES.dic
ln -s %{_datadir}/hyphen/hyph_es_ANY.dic %{buildroot}%{_datadir}/hyphen/hyph_es_GT.dic
ln -s %{_datadir}/hyphen/hyph_es_GT.dic %{buildroot}%{_datadir}/myspell/hyph_es_GT.dic
ln -s %{_datadir}/hyphen/hyph_es_ANY.dic %{buildroot}%{_datadir}/hyphen/hyph_es_HN.dic
ln -s %{_datadir}/hyphen/hyph_es_HN.dic %{buildroot}%{_datadir}/myspell/hyph_es_HN.dic
ln -s %{_datadir}/hyphen/hyph_es_ANY.dic %{buildroot}%{_datadir}/hyphen/hyph_es_MX.dic
ln -s %{_datadir}/hyphen/hyph_es_MX.dic %{buildroot}%{_datadir}/myspell/hyph_es_MX.dic
ln -s %{_datadir}/hyphen/hyph_es_ANY.dic %{buildroot}%{_datadir}/hyphen/hyph_es_NI.dic
ln -s %{_datadir}/hyphen/hyph_es_NI.dic %{buildroot}%{_datadir}/myspell/hyph_es_NI.dic
ln -s %{_datadir}/hyphen/hyph_es_ANY.dic %{buildroot}%{_datadir}/hyphen/hyph_es_PA.dic
ln -s %{_datadir}/hyphen/hyph_es_PA.dic %{buildroot}%{_datadir}/myspell/hyph_es_PA.dic
ln -s %{_datadir}/hyphen/hyph_es_ANY.dic %{buildroot}%{_datadir}/hyphen/hyph_es_PE.dic
ln -s %{_datadir}/hyphen/hyph_es_PE.dic %{buildroot}%{_datadir}/myspell/hyph_es_PE.dic
ln -s %{_datadir}/hyphen/hyph_es_ANY.dic %{buildroot}%{_datadir}/hyphen/hyph_es_PR.dic
ln -s %{_datadir}/hyphen/hyph_es_PR.dic %{buildroot}%{_datadir}/myspell/hyph_es_PR.dic
ln -s %{_datadir}/hyphen/hyph_es_ANY.dic %{buildroot}%{_datadir}/hyphen/hyph_es_PY.dic
ln -s %{_datadir}/hyphen/hyph_es_PY.dic %{buildroot}%{_datadir}/myspell/hyph_es_PY.dic
ln -s %{_datadir}/hyphen/hyph_es_ANY.dic %{buildroot}%{_datadir}/hyphen/hyph_es_SV.dic
ln -s %{_datadir}/hyphen/hyph_es_SV.dic %{buildroot}%{_datadir}/myspell/hyph_es_SV.dic
ln -s %{_datadir}/hyphen/hyph_es_ANY.dic %{buildroot}%{_datadir}/hyphen/hyph_es_UY.dic
ln -s %{_datadir}/hyphen/hyph_es_UY.dic %{buildroot}%{_datadir}/myspell/hyph_es_UY.dic
ln -s %{_datadir}/hyphen/hyph_es_ANY.dic %{buildroot}%{_datadir}/hyphen/hyph_es_VE.dic
ln -s %{_datadir}/hyphen/hyph_es_VE.dic %{buildroot}%{_datadir}/myspell/hyph_es_VE.dic
cp -P es/hyph_es_ANY.dic %{buildroot}%{_datadir}/hyphen/hyph_es_ANY.dic
ln -s %{_datadir}/hyphen/hyph_es_ANY.dic %{buildroot}%{_datadir}/myspell/hyph_es_ANY.dic
ln -s %{_datadir}/mythes/th_es_ANY_v2.dat %{buildroot}%{_datadir}/mythes/th_es_AR_v2.dat
ln -s %{_datadir}/mythes/th_es_AR_v2.dat %{buildroot}%{_datadir}/myspell/th_es_AR_v2.dat
ln -s %{_datadir}/mythes/th_es_ANY_v2.dat %{buildroot}%{_datadir}/mythes/th_es_BO_v2.dat
ln -s %{_datadir}/mythes/th_es_BO_v2.dat %{buildroot}%{_datadir}/myspell/th_es_BO_v2.dat
ln -s %{_datadir}/mythes/th_es_ANY_v2.dat %{buildroot}%{_datadir}/mythes/th_es_CL_v2.dat
ln -s %{_datadir}/mythes/th_es_CL_v2.dat %{buildroot}%{_datadir}/myspell/th_es_CL_v2.dat
ln -s %{_datadir}/mythes/th_es_ANY_v2.dat %{buildroot}%{_datadir}/mythes/th_es_CO_v2.dat
ln -s %{_datadir}/mythes/th_es_CO_v2.dat %{buildroot}%{_datadir}/myspell/th_es_CO_v2.dat
ln -s %{_datadir}/mythes/th_es_ANY_v2.dat %{buildroot}%{_datadir}/mythes/th_es_CR_v2.dat
ln -s %{_datadir}/mythes/th_es_CR_v2.dat %{buildroot}%{_datadir}/myspell/th_es_CR_v2.dat
ln -s %{_datadir}/mythes/th_es_ANY_v2.dat %{buildroot}%{_datadir}/mythes/th_es_CU_v2.dat
ln -s %{_datadir}/mythes/th_es_CU_v2.dat %{buildroot}%{_datadir}/myspell/th_es_CU_v2.dat
ln -s %{_datadir}/mythes/th_es_ANY_v2.dat %{buildroot}%{_datadir}/mythes/th_es_DO_v2.dat
ln -s %{_datadir}/mythes/th_es_DO_v2.dat %{buildroot}%{_datadir}/myspell/th_es_DO_v2.dat
ln -s %{_datadir}/mythes/th_es_ANY_v2.dat %{buildroot}%{_datadir}/mythes/th_es_EC_v2.dat
ln -s %{_datadir}/mythes/th_es_EC_v2.dat %{buildroot}%{_datadir}/myspell/th_es_EC_v2.dat
ln -s %{_datadir}/mythes/th_es_ANY_v2.dat %{buildroot}%{_datadir}/mythes/th_es_ES_v2.dat
ln -s %{_datadir}/mythes/th_es_ES_v2.dat %{buildroot}%{_datadir}/myspell/th_es_ES_v2.dat
ln -s %{_datadir}/mythes/th_es_ANY_v2.dat %{buildroot}%{_datadir}/mythes/th_es_GT_v2.dat
ln -s %{_datadir}/mythes/th_es_GT_v2.dat %{buildroot}%{_datadir}/myspell/th_es_GT_v2.dat
ln -s %{_datadir}/mythes/th_es_ANY_v2.dat %{buildroot}%{_datadir}/mythes/th_es_HN_v2.dat
ln -s %{_datadir}/mythes/th_es_HN_v2.dat %{buildroot}%{_datadir}/myspell/th_es_HN_v2.dat
ln -s %{_datadir}/mythes/th_es_ANY_v2.dat %{buildroot}%{_datadir}/mythes/th_es_MX_v2.dat
ln -s %{_datadir}/mythes/th_es_MX_v2.dat %{buildroot}%{_datadir}/myspell/th_es_MX_v2.dat
ln -s %{_datadir}/mythes/th_es_ANY_v2.dat %{buildroot}%{_datadir}/mythes/th_es_NI_v2.dat
ln -s %{_datadir}/mythes/th_es_NI_v2.dat %{buildroot}%{_datadir}/myspell/th_es_NI_v2.dat
ln -s %{_datadir}/mythes/th_es_ANY_v2.dat %{buildroot}%{_datadir}/mythes/th_es_PA_v2.dat
ln -s %{_datadir}/mythes/th_es_PA_v2.dat %{buildroot}%{_datadir}/myspell/th_es_PA_v2.dat
ln -s %{_datadir}/mythes/th_es_ANY_v2.dat %{buildroot}%{_datadir}/mythes/th_es_PE_v2.dat
ln -s %{_datadir}/mythes/th_es_PE_v2.dat %{buildroot}%{_datadir}/myspell/th_es_PE_v2.dat
ln -s %{_datadir}/mythes/th_es_ANY_v2.dat %{buildroot}%{_datadir}/mythes/th_es_PR_v2.dat
ln -s %{_datadir}/mythes/th_es_PR_v2.dat %{buildroot}%{_datadir}/myspell/th_es_PR_v2.dat
ln -s %{_datadir}/mythes/th_es_ANY_v2.dat %{buildroot}%{_datadir}/mythes/th_es_PY_v2.dat
ln -s %{_datadir}/mythes/th_es_PY_v2.dat %{buildroot}%{_datadir}/myspell/th_es_PY_v2.dat
ln -s %{_datadir}/mythes/th_es_ANY_v2.dat %{buildroot}%{_datadir}/mythes/th_es_SV_v2.dat
ln -s %{_datadir}/mythes/th_es_SV_v2.dat %{buildroot}%{_datadir}/myspell/th_es_SV_v2.dat
ln -s %{_datadir}/mythes/th_es_ANY_v2.dat %{buildroot}%{_datadir}/mythes/th_es_UY_v2.dat
ln -s %{_datadir}/mythes/th_es_UY_v2.dat %{buildroot}%{_datadir}/myspell/th_es_UY_v2.dat
ln -s %{_datadir}/mythes/th_es_ANY_v2.dat %{buildroot}%{_datadir}/mythes/th_es_VE_v2.dat
ln -s %{_datadir}/mythes/th_es_VE_v2.dat %{buildroot}%{_datadir}/myspell/th_es_VE_v2.dat
cp -P es/th_es_ANY_v2.dat %{buildroot}%{_datadir}/mythes/th_es_ANY_v2.dat
ln -s %{_datadir}/mythes/th_es_ANY_v2.dat %{buildroot}%{_datadir}/myspell/th_es_ANY_v2.dat
ln -s %{_datadir}/mythes/th_es_ANY_v2.idx %{buildroot}%{_datadir}/mythes/th_es_AR_v2.idx
ln -s %{_datadir}/mythes/th_es_AR_v2.idx %{buildroot}%{_datadir}/myspell/th_es_AR_v2.idx
ln -s %{_datadir}/mythes/th_es_ANY_v2.idx %{buildroot}%{_datadir}/mythes/th_es_BO_v2.idx
ln -s %{_datadir}/mythes/th_es_BO_v2.idx %{buildroot}%{_datadir}/myspell/th_es_BO_v2.idx
ln -s %{_datadir}/mythes/th_es_ANY_v2.idx %{buildroot}%{_datadir}/mythes/th_es_CL_v2.idx
ln -s %{_datadir}/mythes/th_es_CL_v2.idx %{buildroot}%{_datadir}/myspell/th_es_CL_v2.idx
ln -s %{_datadir}/mythes/th_es_ANY_v2.idx %{buildroot}%{_datadir}/mythes/th_es_CO_v2.idx
ln -s %{_datadir}/mythes/th_es_CO_v2.idx %{buildroot}%{_datadir}/myspell/th_es_CO_v2.idx
ln -s %{_datadir}/mythes/th_es_ANY_v2.idx %{buildroot}%{_datadir}/mythes/th_es_CR_v2.idx
ln -s %{_datadir}/mythes/th_es_CR_v2.idx %{buildroot}%{_datadir}/myspell/th_es_CR_v2.idx
ln -s %{_datadir}/mythes/th_es_ANY_v2.idx %{buildroot}%{_datadir}/mythes/th_es_CU_v2.idx
ln -s %{_datadir}/mythes/th_es_CU_v2.idx %{buildroot}%{_datadir}/myspell/th_es_CU_v2.idx
ln -s %{_datadir}/mythes/th_es_ANY_v2.idx %{buildroot}%{_datadir}/mythes/th_es_DO_v2.idx
ln -s %{_datadir}/mythes/th_es_DO_v2.idx %{buildroot}%{_datadir}/myspell/th_es_DO_v2.idx
ln -s %{_datadir}/mythes/th_es_ANY_v2.idx %{buildroot}%{_datadir}/mythes/th_es_EC_v2.idx
ln -s %{_datadir}/mythes/th_es_EC_v2.idx %{buildroot}%{_datadir}/myspell/th_es_EC_v2.idx
ln -s %{_datadir}/mythes/th_es_ANY_v2.idx %{buildroot}%{_datadir}/mythes/th_es_ES_v2.idx
ln -s %{_datadir}/mythes/th_es_ES_v2.idx %{buildroot}%{_datadir}/myspell/th_es_ES_v2.idx
ln -s %{_datadir}/mythes/th_es_ANY_v2.idx %{buildroot}%{_datadir}/mythes/th_es_GT_v2.idx
ln -s %{_datadir}/mythes/th_es_GT_v2.idx %{buildroot}%{_datadir}/myspell/th_es_GT_v2.idx
ln -s %{_datadir}/mythes/th_es_ANY_v2.idx %{buildroot}%{_datadir}/mythes/th_es_HN_v2.idx
ln -s %{_datadir}/mythes/th_es_HN_v2.idx %{buildroot}%{_datadir}/myspell/th_es_HN_v2.idx
ln -s %{_datadir}/mythes/th_es_ANY_v2.idx %{buildroot}%{_datadir}/mythes/th_es_MX_v2.idx
ln -s %{_datadir}/mythes/th_es_MX_v2.idx %{buildroot}%{_datadir}/myspell/th_es_MX_v2.idx
ln -s %{_datadir}/mythes/th_es_ANY_v2.idx %{buildroot}%{_datadir}/mythes/th_es_NI_v2.idx
ln -s %{_datadir}/mythes/th_es_NI_v2.idx %{buildroot}%{_datadir}/myspell/th_es_NI_v2.idx
ln -s %{_datadir}/mythes/th_es_ANY_v2.idx %{buildroot}%{_datadir}/mythes/th_es_PA_v2.idx
ln -s %{_datadir}/mythes/th_es_PA_v2.idx %{buildroot}%{_datadir}/myspell/th_es_PA_v2.idx
ln -s %{_datadir}/mythes/th_es_ANY_v2.idx %{buildroot}%{_datadir}/mythes/th_es_PE_v2.idx
ln -s %{_datadir}/mythes/th_es_PE_v2.idx %{buildroot}%{_datadir}/myspell/th_es_PE_v2.idx
ln -s %{_datadir}/mythes/th_es_ANY_v2.idx %{buildroot}%{_datadir}/mythes/th_es_PR_v2.idx
ln -s %{_datadir}/mythes/th_es_PR_v2.idx %{buildroot}%{_datadir}/myspell/th_es_PR_v2.idx
ln -s %{_datadir}/mythes/th_es_ANY_v2.idx %{buildroot}%{_datadir}/mythes/th_es_PY_v2.idx
ln -s %{_datadir}/mythes/th_es_PY_v2.idx %{buildroot}%{_datadir}/myspell/th_es_PY_v2.idx
ln -s %{_datadir}/mythes/th_es_ANY_v2.idx %{buildroot}%{_datadir}/mythes/th_es_SV_v2.idx
ln -s %{_datadir}/mythes/th_es_SV_v2.idx %{buildroot}%{_datadir}/myspell/th_es_SV_v2.idx
ln -s %{_datadir}/mythes/th_es_ANY_v2.idx %{buildroot}%{_datadir}/mythes/th_es_UY_v2.idx
ln -s %{_datadir}/mythes/th_es_UY_v2.idx %{buildroot}%{_datadir}/myspell/th_es_UY_v2.idx
ln -s %{_datadir}/mythes/th_es_ANY_v2.idx %{buildroot}%{_datadir}/mythes/th_es_VE_v2.idx
ln -s %{_datadir}/mythes/th_es_VE_v2.idx %{buildroot}%{_datadir}/myspell/th_es_VE_v2.idx
cp -P es/th_es_ANY_v2.idx %{buildroot}%{_datadir}/mythes/th_es_ANY_v2.idx
ln -s %{_datadir}/mythes/th_es_ANY_v2.idx %{buildroot}%{_datadir}/myspell/th_es_ANY_v2.idx
mkdir -p %{buildroot}%{_docdir}/myspell-es
cp -P es/README_es_ANY.txt %{buildroot}%{_docdir}/myspell-es/README_es_ANY.txt
cp -P es/README_hyph_es_ANY.txt %{buildroot}%{_docdir}/myspell-es/README_hyph_es_ANY.txt
cp -P es/README_th_es_ANY.txt %{buildroot}%{_docdir}/myspell-es/README_th_es_ANY.txt
cp -P es/description.xml %{buildroot}%{_docdir}/myspell-es/description.xml
cp -P es/dictionaries.xcu %{buildroot}%{_docdir}/myspell-es/dictionaries.xcu
cp -P es/package-description.txt %{buildroot}%{_docdir}/myspell-es/package-description.txt
cp -P et_EE/et_EE.aff %{buildroot}%{_datadir}/hunspell/et_EE.aff
ln -s %{_datadir}/hunspell/et_EE.aff %{buildroot}%{_datadir}/myspell/et_EE.aff
cp -P et_EE/et_EE.dic %{buildroot}%{_datadir}/hunspell/et_EE.dic
ln -s %{_datadir}/hunspell/et_EE.dic %{buildroot}%{_datadir}/myspell/et_EE.dic
cp -P et_EE/hyph_et_EE.dic %{buildroot}%{_datadir}/hyphen/hyph_et_EE.dic
ln -s %{_datadir}/hyphen/hyph_et_EE.dic %{buildroot}%{_datadir}/myspell/hyph_et_EE.dic
mkdir -p %{buildroot}%{_docdir}/myspell-et_EE
cp -P et_EE/README_et_EE.txt %{buildroot}%{_docdir}/myspell-et_EE/README_et_EE.txt
cp -P et_EE/README_hyph_et_EE.txt %{buildroot}%{_docdir}/myspell-et_EE/README_hyph_et_EE.txt
cp -P et_EE/description.xml %{buildroot}%{_docdir}/myspell-et_EE/description.xml
cp -P et_EE/dictionaries.xcu %{buildroot}%{_docdir}/myspell-et_EE/dictionaries.xcu
cp -P et_EE/eehyph.tex %{buildroot}%{_docdir}/myspell-et_EE/eehyph.tex
ln -s %{_datadir}/hunspell/fr.aff %{buildroot}%{_datadir}/hunspell/fr_FR.aff
ln -s %{_datadir}/hunspell/fr_FR.aff %{buildroot}%{_datadir}/myspell/fr_FR.aff
ln -s %{_datadir}/hunspell/fr.aff %{buildroot}%{_datadir}/hunspell/fr_BE.aff
ln -s %{_datadir}/hunspell/fr_BE.aff %{buildroot}%{_datadir}/myspell/fr_BE.aff
ln -s %{_datadir}/hunspell/fr.aff %{buildroot}%{_datadir}/hunspell/fr_CA.aff
ln -s %{_datadir}/hunspell/fr_CA.aff %{buildroot}%{_datadir}/myspell/fr_CA.aff
ln -s %{_datadir}/hunspell/fr.aff %{buildroot}%{_datadir}/hunspell/fr_CH.aff
ln -s %{_datadir}/hunspell/fr_CH.aff %{buildroot}%{_datadir}/myspell/fr_CH.aff
ln -s %{_datadir}/hunspell/fr.aff %{buildroot}%{_datadir}/hunspell/fr_LU.aff
ln -s %{_datadir}/hunspell/fr_LU.aff %{buildroot}%{_datadir}/myspell/fr_LU.aff
ln -s %{_datadir}/hunspell/fr.aff %{buildroot}%{_datadir}/hunspell/fr_MC.aff
ln -s %{_datadir}/hunspell/fr_MC.aff %{buildroot}%{_datadir}/myspell/fr_MC.aff
cp -P fr_FR/fr.aff %{buildroot}%{_datadir}/hunspell/fr.aff
ln -s %{_datadir}/hunspell/fr.aff %{buildroot}%{_datadir}/myspell/fr.aff
ln -s %{_datadir}/hunspell/fr.dic %{buildroot}%{_datadir}/hunspell/fr_FR.dic
ln -s %{_datadir}/hunspell/fr_FR.dic %{buildroot}%{_datadir}/myspell/fr_FR.dic
ln -s %{_datadir}/hunspell/fr.dic %{buildroot}%{_datadir}/hunspell/fr_BE.dic
ln -s %{_datadir}/hunspell/fr_BE.dic %{buildroot}%{_datadir}/myspell/fr_BE.dic
ln -s %{_datadir}/hunspell/fr.dic %{buildroot}%{_datadir}/hunspell/fr_CA.dic
ln -s %{_datadir}/hunspell/fr_CA.dic %{buildroot}%{_datadir}/myspell/fr_CA.dic
ln -s %{_datadir}/hunspell/fr.dic %{buildroot}%{_datadir}/hunspell/fr_CH.dic
ln -s %{_datadir}/hunspell/fr_CH.dic %{buildroot}%{_datadir}/myspell/fr_CH.dic
ln -s %{_datadir}/hunspell/fr.dic %{buildroot}%{_datadir}/hunspell/fr_LU.dic
ln -s %{_datadir}/hunspell/fr_LU.dic %{buildroot}%{_datadir}/myspell/fr_LU.dic
ln -s %{_datadir}/hunspell/fr.dic %{buildroot}%{_datadir}/hunspell/fr_MC.dic
ln -s %{_datadir}/hunspell/fr_MC.dic %{buildroot}%{_datadir}/myspell/fr_MC.dic
cp -P fr_FR/fr.dic %{buildroot}%{_datadir}/hunspell/fr.dic
ln -s %{_datadir}/hunspell/fr.dic %{buildroot}%{_datadir}/myspell/fr.dic
ln -s %{_datadir}/hyphen/hyph_fr.dic %{buildroot}%{_datadir}/hyphen/hyph_fr_FR.dic
ln -s %{_datadir}/hyphen/hyph_fr_FR.dic %{buildroot}%{_datadir}/myspell/hyph_fr_FR.dic
ln -s %{_datadir}/hyphen/hyph_fr.dic %{buildroot}%{_datadir}/hyphen/hyph_fr_BE.dic
ln -s %{_datadir}/hyphen/hyph_fr_BE.dic %{buildroot}%{_datadir}/myspell/hyph_fr_BE.dic
ln -s %{_datadir}/hyphen/hyph_fr.dic %{buildroot}%{_datadir}/hyphen/hyph_fr_CA.dic
ln -s %{_datadir}/hyphen/hyph_fr_CA.dic %{buildroot}%{_datadir}/myspell/hyph_fr_CA.dic
ln -s %{_datadir}/hyphen/hyph_fr.dic %{buildroot}%{_datadir}/hyphen/hyph_fr_CH.dic
ln -s %{_datadir}/hyphen/hyph_fr_CH.dic %{buildroot}%{_datadir}/myspell/hyph_fr_CH.dic
ln -s %{_datadir}/hyphen/hyph_fr.dic %{buildroot}%{_datadir}/hyphen/hyph_fr_MC.dic
ln -s %{_datadir}/hyphen/hyph_fr_MC.dic %{buildroot}%{_datadir}/myspell/hyph_fr_MC.dic
ln -s %{_datadir}/hyphen/hyph_fr.dic %{buildroot}%{_datadir}/hyphen/hyph_fr_LU.dic
ln -s %{_datadir}/hyphen/hyph_fr_LU.dic %{buildroot}%{_datadir}/myspell/hyph_fr_LU.dic
cp -P fr_FR/hyph_fr.dic %{buildroot}%{_datadir}/hyphen/hyph_fr.dic
ln -s %{_datadir}/hyphen/hyph_fr.dic %{buildroot}%{_datadir}/myspell/hyph_fr.dic
ln -s %{_datadir}/mythes/thes_fr.dat %{buildroot}%{_datadir}/mythes/th_fr_FR_v2.dat
ln -s %{_datadir}/mythes/th_fr_FR_v2.dat %{buildroot}%{_datadir}/myspell/th_fr_FR_v2.dat
ln -s %{_datadir}/mythes/thes_fr.dat %{buildroot}%{_datadir}/mythes/th_fr_BE_v2.dat
ln -s %{_datadir}/mythes/th_fr_BE_v2.dat %{buildroot}%{_datadir}/myspell/th_fr_BE_v2.dat
ln -s %{_datadir}/mythes/thes_fr.dat %{buildroot}%{_datadir}/mythes/th_fr_CA_v2.dat
ln -s %{_datadir}/mythes/th_fr_CA_v2.dat %{buildroot}%{_datadir}/myspell/th_fr_CA_v2.dat
ln -s %{_datadir}/mythes/thes_fr.dat %{buildroot}%{_datadir}/mythes/th_fr_CH_v2.dat
ln -s %{_datadir}/mythes/th_fr_CH_v2.dat %{buildroot}%{_datadir}/myspell/th_fr_CH_v2.dat
ln -s %{_datadir}/mythes/thes_fr.dat %{buildroot}%{_datadir}/mythes/th_fr_MC_v2.dat
ln -s %{_datadir}/mythes/th_fr_MC_v2.dat %{buildroot}%{_datadir}/myspell/th_fr_MC_v2.dat
ln -s %{_datadir}/mythes/thes_fr.dat %{buildroot}%{_datadir}/mythes/th_fr_LU_v2.dat
ln -s %{_datadir}/mythes/th_fr_LU_v2.dat %{buildroot}%{_datadir}/myspell/th_fr_LU_v2.dat
cp -P fr_FR/thes_fr.dat %{buildroot}%{_datadir}/mythes/thes_fr.dat
ln -s %{_datadir}/mythes/thes_fr.dat %{buildroot}%{_datadir}/myspell/thes_fr.dat
ln -s %{_datadir}/mythes/thes_fr.idx %{buildroot}%{_datadir}/mythes/th_fr_FR_v2.idx
ln -s %{_datadir}/mythes/th_fr_FR_v2.idx %{buildroot}%{_datadir}/myspell/th_fr_FR_v2.idx
ln -s %{_datadir}/mythes/thes_fr.idx %{buildroot}%{_datadir}/mythes/th_fr_BE_v2.idx
ln -s %{_datadir}/mythes/th_fr_BE_v2.idx %{buildroot}%{_datadir}/myspell/th_fr_BE_v2.idx
ln -s %{_datadir}/mythes/thes_fr.idx %{buildroot}%{_datadir}/mythes/th_fr_CA_v2.idx
ln -s %{_datadir}/mythes/th_fr_CA_v2.idx %{buildroot}%{_datadir}/myspell/th_fr_CA_v2.idx
ln -s %{_datadir}/mythes/thes_fr.idx %{buildroot}%{_datadir}/mythes/th_fr_CH_v2.idx
ln -s %{_datadir}/mythes/th_fr_CH_v2.idx %{buildroot}%{_datadir}/myspell/th_fr_CH_v2.idx
ln -s %{_datadir}/mythes/thes_fr.idx %{buildroot}%{_datadir}/mythes/th_fr_MC_v2.idx
ln -s %{_datadir}/mythes/th_fr_MC_v2.idx %{buildroot}%{_datadir}/myspell/th_fr_MC_v2.idx
ln -s %{_datadir}/mythes/thes_fr.idx %{buildroot}%{_datadir}/mythes/th_fr_LU_v2.idx
ln -s %{_datadir}/mythes/th_fr_LU_v2.idx %{buildroot}%{_datadir}/myspell/th_fr_LU_v2.idx
cp -P fr_FR/thes_fr.idx %{buildroot}%{_datadir}/mythes/thes_fr.idx
ln -s %{_datadir}/mythes/thes_fr.idx %{buildroot}%{_datadir}/myspell/thes_fr.idx
mkdir -p %{buildroot}%{_docdir}/myspell-fr_FR
cp -P fr_FR/README_fr.txt %{buildroot}%{_docdir}/myspell-fr_FR/README_fr.txt
cp -P fr_FR/README_hyph_fr.txt %{buildroot}%{_docdir}/myspell-fr_FR/README_hyph_fr.txt
cp -P fr_FR/README_thes_fr.txt %{buildroot}%{_docdir}/myspell-fr_FR/README_thes_fr.txt
cp -P fr_FR/description.xml %{buildroot}%{_docdir}/myspell-fr_FR/description.xml
cp -P fr_FR/dictionaries.xcu %{buildroot}%{_docdir}/myspell-fr_FR/dictionaries.xcu
cp -P fr_FR/hyph-fr.tex %{buildroot}%{_docdir}/myspell-fr_FR/hyph-fr.tex
cp -P fr_FR/icon.png %{buildroot}%{_docdir}/myspell-fr_FR/icon.png
cp -P fr_FR/package-description.txt %{buildroot}%{_docdir}/myspell-fr_FR/package-description.txt
cp -P gd_GB/gd_GB.aff %{buildroot}%{_datadir}/hunspell/gd_GB.aff
ln -s %{_datadir}/hunspell/gd_GB.aff %{buildroot}%{_datadir}/myspell/gd_GB.aff
cp -P gd_GB/gd_GB.dic %{buildroot}%{_datadir}/hunspell/gd_GB.dic
ln -s %{_datadir}/hunspell/gd_GB.dic %{buildroot}%{_datadir}/myspell/gd_GB.dic
mkdir -p %{buildroot}%{_docdir}/myspell-gd_GB
cp -P gd_GB/LICENSES-en.txt %{buildroot}%{_docdir}/myspell-gd_GB/LICENSES-en.txt
cp -P gd_GB/README_gd_GB.txt %{buildroot}%{_docdir}/myspell-gd_GB/README_gd_GB.txt
cp -P gd_GB/description.xml %{buildroot}%{_docdir}/myspell-gd_GB/description.xml
cp -P gd_GB/dictionaries.xcu %{buildroot}%{_docdir}/myspell-gd_GB/dictionaries.xcu
ln -s %{_datadir}/hunspell/gl.aff %{buildroot}%{_datadir}/hunspell/gl_ES.aff
ln -s %{_datadir}/hunspell/gl_ES.aff %{buildroot}%{_datadir}/myspell/gl_ES.aff
cp -P gl/gl.aff %{buildroot}%{_datadir}/hunspell/gl.aff
ln -s %{_datadir}/hunspell/gl.aff %{buildroot}%{_datadir}/myspell/gl.aff
ln -s %{_datadir}/hunspell/gl.dic %{buildroot}%{_datadir}/hunspell/gl_ES.dic
ln -s %{_datadir}/hunspell/gl_ES.dic %{buildroot}%{_datadir}/myspell/gl_ES.dic
cp -P gl/gl.dic %{buildroot}%{_datadir}/hunspell/gl.dic
ln -s %{_datadir}/hunspell/gl.dic %{buildroot}%{_datadir}/myspell/gl.dic
ln -s %{_datadir}/hyphen/hyph_gl.dic %{buildroot}%{_datadir}/hyphen/hyph_gl_ES.dic
ln -s %{_datadir}/hyphen/hyph_gl_ES.dic %{buildroot}%{_datadir}/myspell/hyph_gl_ES.dic
cp -P gl/hyph_gl.dic %{buildroot}%{_datadir}/hyphen/hyph_gl.dic
ln -s %{_datadir}/hyphen/hyph_gl.dic %{buildroot}%{_datadir}/myspell/hyph_gl.dic
ln -s %{_datadir}/mythes/thesaurus_gl.dat %{buildroot}%{_datadir}/mythes/th_gl_v2.dat
ln -s %{_datadir}/mythes/th_gl_v2.dat %{buildroot}%{_datadir}/myspell/th_gl_v2.dat
ln -s %{_datadir}/mythes/thesaurus_gl.dat %{buildroot}%{_datadir}/mythes/th_gl_ES_v2.dat
ln -s %{_datadir}/mythes/th_gl_ES_v2.dat %{buildroot}%{_datadir}/myspell/th_gl_ES_v2.dat
cp -P gl/thesaurus_gl.dat %{buildroot}%{_datadir}/mythes/thesaurus_gl.dat
ln -s %{_datadir}/mythes/thesaurus_gl.dat %{buildroot}%{_datadir}/myspell/thesaurus_gl.dat
ln -s %{_datadir}/mythes/thesaurus_gl.idx %{buildroot}%{_datadir}/mythes/th_gl_v2.idx
ln -s %{_datadir}/mythes/th_gl_v2.idx %{buildroot}%{_datadir}/myspell/th_gl_v2.idx
ln -s %{_datadir}/mythes/thesaurus_gl.idx %{buildroot}%{_datadir}/mythes/th_gl_ES_v2.idx
ln -s %{_datadir}/mythes/th_gl_ES_v2.idx %{buildroot}%{_datadir}/myspell/th_gl_ES_v2.idx
cp -P gl/thesaurus_gl.idx %{buildroot}%{_datadir}/mythes/thesaurus_gl.idx
ln -s %{_datadir}/mythes/thesaurus_gl.idx %{buildroot}%{_datadir}/myspell/thesaurus_gl.idx
mkdir -p %{buildroot}%{_docdir}/myspell-gl
cp -P gl/COPYING_th_gl %{buildroot}%{_docdir}/myspell-gl/COPYING_th_gl
cp -P gl/Changelog.txt %{buildroot}%{_docdir}/myspell-gl/Changelog.txt
cp -P gl/GPLv3.txt %{buildroot}%{_docdir}/myspell-gl/GPLv3.txt
cp -P gl/ProxectoTrasno.png %{buildroot}%{_docdir}/myspell-gl/ProxectoTrasno.png
cp -P gl/README %{buildroot}%{_docdir}/myspell-gl/README
cp -P gl/README_hyph-gl.txt %{buildroot}%{_docdir}/myspell-gl/README_hyph-gl.txt
cp -P gl/README_th_gl.txt %{buildroot}%{_docdir}/myspell-gl/README_th_gl.txt
cp -P gl/description.xml %{buildroot}%{_docdir}/myspell-gl/description.xml
cp -P gl/dictionaries.xcu %{buildroot}%{_docdir}/myspell-gl/dictionaries.xcu
cp -P gl/package-description.txt %{buildroot}%{_docdir}/myspell-gl/package-description.txt
ln -s %{_datadir}/hunspell/gug.aff %{buildroot}%{_datadir}/hunspell/gug_PY.aff
ln -s %{_datadir}/hunspell/gug_PY.aff %{buildroot}%{_datadir}/myspell/gug_PY.aff
cp -P gug/gug.aff %{buildroot}%{_datadir}/hunspell/gug.aff
ln -s %{_datadir}/hunspell/gug.aff %{buildroot}%{_datadir}/myspell/gug.aff
ln -s %{_datadir}/hunspell/gug.dic %{buildroot}%{_datadir}/hunspell/gug_PY.dic
ln -s %{_datadir}/hunspell/gug_PY.dic %{buildroot}%{_datadir}/myspell/gug_PY.dic
cp -P gug/gug.dic %{buildroot}%{_datadir}/hunspell/gug.dic
ln -s %{_datadir}/hunspell/gug.dic %{buildroot}%{_datadir}/myspell/gug.dic
ln -s %{_datadir}/mythes/th_gug_PY.dat %{buildroot}%{_datadir}/mythes/th_gug_PY_v2.dat
ln -s %{_datadir}/mythes/th_gug_PY_v2.dat %{buildroot}%{_datadir}/myspell/th_gug_PY_v2.dat
cp -P gug/th_gug_PY.dat %{buildroot}%{_datadir}/mythes/th_gug_PY.dat
ln -s %{_datadir}/mythes/th_gug_PY.dat %{buildroot}%{_datadir}/myspell/th_gug_PY.dat
ln -s %{_datadir}/mythes/th_gug_PY.idx %{buildroot}%{_datadir}/mythes/th_gug_PY_v2.idx
ln -s %{_datadir}/mythes/th_gug_PY_v2.idx %{buildroot}%{_datadir}/myspell/th_gug_PY_v2.idx
cp -P gug/th_gug_PY.idx %{buildroot}%{_datadir}/mythes/th_gug_PY.idx
ln -s %{_datadir}/mythes/th_gug_PY.idx %{buildroot}%{_datadir}/myspell/th_gug_PY.idx
mkdir -p %{buildroot}%{_docdir}/myspell-gug
cp -P gug/README_th_gug_PY.txt %{buildroot}%{_docdir}/myspell-gug/README_th_gug_PY.txt
cp -P gug/description.xml %{buildroot}%{_docdir}/myspell-gug/description.xml
cp -P gug/dictionaries.xcu %{buildroot}%{_docdir}/myspell-gug/dictionaries.xcu
cp -P gu_IN/gu_IN.aff %{buildroot}%{_datadir}/hunspell/gu_IN.aff
ln -s %{_datadir}/hunspell/gu_IN.aff %{buildroot}%{_datadir}/myspell/gu_IN.aff
cp -P gu_IN/gu_IN.dic %{buildroot}%{_datadir}/hunspell/gu_IN.dic
ln -s %{_datadir}/hunspell/gu_IN.dic %{buildroot}%{_datadir}/myspell/gu_IN.dic
mkdir -p %{buildroot}%{_docdir}/myspell-gu_IN
cp -P gu_IN/README_gu_IN.txt %{buildroot}%{_docdir}/myspell-gu_IN/README_gu_IN.txt
cp -P gu_IN/description.xml %{buildroot}%{_docdir}/myspell-gu_IN/description.xml
cp -P gu_IN/dictionaries.xcu %{buildroot}%{_docdir}/myspell-gu_IN/dictionaries.xcu
cp -P he_IL/he_IL.aff %{buildroot}%{_datadir}/hunspell/he_IL.aff
ln -s %{_datadir}/hunspell/he_IL.aff %{buildroot}%{_datadir}/myspell/he_IL.aff
cp -P he_IL/he_IL.dic %{buildroot}%{_datadir}/hunspell/he_IL.dic
ln -s %{_datadir}/hunspell/he_IL.dic %{buildroot}%{_datadir}/myspell/he_IL.dic
mkdir -p %{buildroot}%{_docdir}/myspell-he_IL
cp -P he_IL/README_he_IL.txt %{buildroot}%{_docdir}/myspell-he_IL/README_he_IL.txt
cp -P he_IL/alphabet.png %{buildroot}%{_docdir}/myspell-he_IL/alphabet.png
cp -P he_IL/description.xml %{buildroot}%{_docdir}/myspell-he_IL/description.xml
cp -P he_IL/dictionaries.xcu %{buildroot}%{_docdir}/myspell-he_IL/dictionaries.xcu
cp -P hi_IN/hi_IN.aff %{buildroot}%{_datadir}/hunspell/hi_IN.aff
ln -s %{_datadir}/hunspell/hi_IN.aff %{buildroot}%{_datadir}/myspell/hi_IN.aff
cp -P hi_IN/hi_IN.dic %{buildroot}%{_datadir}/hunspell/hi_IN.dic
ln -s %{_datadir}/hunspell/hi_IN.dic %{buildroot}%{_datadir}/myspell/hi_IN.dic
mkdir -p %{buildroot}%{_docdir}/myspell-hi_IN
cp -P hi_IN/COPYING %{buildroot}%{_docdir}/myspell-hi_IN/COPYING
cp -P hi_IN/Copyright %{buildroot}%{_docdir}/myspell-hi_IN/Copyright
cp -P hi_IN/README_hi_IN.txt %{buildroot}%{_docdir}/myspell-hi_IN/README_hi_IN.txt
cp -P hi_IN/description.xml %{buildroot}%{_docdir}/myspell-hi_IN/description.xml
cp -P hi_IN/dictionaries.xcu %{buildroot}%{_docdir}/myspell-hi_IN/dictionaries.xcu
cp -P hr_HR/hr_HR.aff %{buildroot}%{_datadir}/hunspell/hr_HR.aff
ln -s %{_datadir}/hunspell/hr_HR.aff %{buildroot}%{_datadir}/myspell/hr_HR.aff
cp -P hr_HR/hr_HR.dic %{buildroot}%{_datadir}/hunspell/hr_HR.dic
ln -s %{_datadir}/hunspell/hr_HR.dic %{buildroot}%{_datadir}/myspell/hr_HR.dic
cp -P hr_HR/hyph_hr_HR.dic %{buildroot}%{_datadir}/hyphen/hyph_hr_HR.dic
ln -s %{_datadir}/hyphen/hyph_hr_HR.dic %{buildroot}%{_datadir}/myspell/hyph_hr_HR.dic
mkdir -p %{buildroot}%{_docdir}/myspell-hr_HR
cp -P hr_HR/README_hr_HR.txt %{buildroot}%{_docdir}/myspell-hr_HR/README_hr_HR.txt
cp -P hr_HR/README_hyph_hr_HR.txt %{buildroot}%{_docdir}/myspell-hr_HR/README_hyph_hr_HR.txt
cp -P hr_HR/description.xml %{buildroot}%{_docdir}/myspell-hr_HR/description.xml
cp -P hr_HR/dictionaries.xcu %{buildroot}%{_docdir}/myspell-hr_HR/dictionaries.xcu
cp -P hu_HU/hu_HU.aff %{buildroot}%{_datadir}/hunspell/hu_HU.aff
ln -s %{_datadir}/hunspell/hu_HU.aff %{buildroot}%{_datadir}/myspell/hu_HU.aff
cp -P hu_HU/hu_HU.dic %{buildroot}%{_datadir}/hunspell/hu_HU.dic
ln -s %{_datadir}/hunspell/hu_HU.dic %{buildroot}%{_datadir}/myspell/hu_HU.dic
cp -P hu_HU/hyph_hu_HU.dic %{buildroot}%{_datadir}/hyphen/hyph_hu_HU.dic
ln -s %{_datadir}/hyphen/hyph_hu_HU.dic %{buildroot}%{_datadir}/myspell/hyph_hu_HU.dic
cp -P hu_HU/th_hu_HU_v2.dat %{buildroot}%{_datadir}/mythes/th_hu_HU_v2.dat
ln -s %{_datadir}/mythes/th_hu_HU_v2.dat %{buildroot}%{_datadir}/myspell/th_hu_HU_v2.dat
cp -P hu_HU/th_hu_HU_v2.idx %{buildroot}%{_datadir}/mythes/th_hu_HU_v2.idx
ln -s %{_datadir}/mythes/th_hu_HU_v2.idx %{buildroot}%{_datadir}/myspell/th_hu_HU_v2.idx
mkdir -p %{buildroot}%{_libdir}/libreoffice/share/extensions/lightproof-hu_HU
cp -rP hu_HU/Lightproof.components %{buildroot}%{_libdir}/libreoffice/share/extensions/lightproof-hu_HU/Lightproof.components
cp -rP hu_HU/Lightproof.py %{buildroot}%{_libdir}/libreoffice/share/extensions/lightproof-hu_HU/Lightproof.py
cp -rP hu_HU/Linguistic.xcu %{buildroot}%{_libdir}/libreoffice/share/extensions/lightproof-hu_HU/Linguistic.xcu
cp -rP hu_HU/META-INF %{buildroot}%{_libdir}/libreoffice/share/extensions/lightproof-hu_HU/META-INF
cp -rP hu_HU/description.xml %{buildroot}%{_libdir}/libreoffice/share/extensions/lightproof-hu_HU/description.xml
cp -rP hu_HU/dialog %{buildroot}%{_libdir}/libreoffice/share/extensions/lightproof-hu_HU/dialog
cp -rP hu_HU/pythonpath %{buildroot}%{_libdir}/libreoffice/share/extensions/lightproof-hu_HU/pythonpath
mkdir -p %{buildroot}%{_docdir}/myspell-hu_HU
cp -P hu_HU/Linguistic.xcu %{buildroot}%{_docdir}/myspell-hu_HU/Linguistic.xcu
cp -P hu_HU/README_hu_HU.txt %{buildroot}%{_docdir}/myspell-hu_HU/README_hu_HU.txt
cp -P hu_HU/README_hyph_hu_HU.txt %{buildroot}%{_docdir}/myspell-hu_HU/README_hyph_hu_HU.txt
cp -P hu_HU/README_lightproof_hu_HU.txt %{buildroot}%{_docdir}/myspell-hu_HU/README_lightproof_hu_HU.txt
cp -P hu_HU/README_th_hu_HU_v2.txt %{buildroot}%{_docdir}/myspell-hu_HU/README_th_hu_HU_v2.txt
cp -P hu_HU/description.xml %{buildroot}%{_docdir}/myspell-hu_HU/description.xml
cp -P hu_HU/dictionaries.xcu %{buildroot}%{_docdir}/myspell-hu_HU/dictionaries.xcu
cp -P id/hyph_id_ID.dic %{buildroot}%{_datadir}/hyphen/hyph_id_ID.dic
ln -s %{_datadir}/hyphen/hyph_id_ID.dic %{buildroot}%{_datadir}/myspell/hyph_id_ID.dic
cp -P id/id_ID.aff %{buildroot}%{_datadir}/hunspell/id_ID.aff
ln -s %{_datadir}/hunspell/id_ID.aff %{buildroot}%{_datadir}/myspell/id_ID.aff
cp -P id/id_ID.dic %{buildroot}%{_datadir}/hunspell/id_ID.dic
ln -s %{_datadir}/hunspell/id_ID.dic %{buildroot}%{_datadir}/myspell/id_ID.dic
cp -P id/th_id_ID_v2.dat %{buildroot}%{_datadir}/mythes/th_id_ID_v2.dat
ln -s %{_datadir}/mythes/th_id_ID_v2.dat %{buildroot}%{_datadir}/myspell/th_id_ID_v2.dat
cp -P id/th_id_ID_v2.idx %{buildroot}%{_datadir}/mythes/th_id_ID_v2.idx
ln -s %{_datadir}/mythes/th_id_ID_v2.idx %{buildroot}%{_datadir}/myspell/th_id_ID_v2.idx
mkdir -p %{buildroot}%{_docdir}/myspell-id
cp -P id/LICENSE-dict %{buildroot}%{_docdir}/myspell-id/LICENSE-dict
cp -P id/LICENSE-thes %{buildroot}%{_docdir}/myspell-id/LICENSE-thes
cp -P id/README-thes %{buildroot}%{_docdir}/myspell-id/README-thes
cp -P id/description.xml %{buildroot}%{_docdir}/myspell-id/description.xml
cp -P id/dictionaries.xcu %{buildroot}%{_docdir}/myspell-id/dictionaries.xcu
ln -s %{_datadir}/hyphen/hyph_is.dic %{buildroot}%{_datadir}/hyphen/hyph_is_IS.dic
ln -s %{_datadir}/hyphen/hyph_is_IS.dic %{buildroot}%{_datadir}/myspell/hyph_is_IS.dic
cp -P is/hyph_is.dic %{buildroot}%{_datadir}/hyphen/hyph_is.dic
ln -s %{_datadir}/hyphen/hyph_is.dic %{buildroot}%{_datadir}/myspell/hyph_is.dic
ln -s %{_datadir}/hunspell/is.aff %{buildroot}%{_datadir}/hunspell/is_IS.aff
ln -s %{_datadir}/hunspell/is_IS.aff %{buildroot}%{_datadir}/myspell/is_IS.aff
cp -P is/is.aff %{buildroot}%{_datadir}/hunspell/is.aff
ln -s %{_datadir}/hunspell/is.aff %{buildroot}%{_datadir}/myspell/is.aff
ln -s %{_datadir}/hunspell/is.dic %{buildroot}%{_datadir}/hunspell/is_IS.dic
ln -s %{_datadir}/hunspell/is_IS.dic %{buildroot}%{_datadir}/myspell/is_IS.dic
cp -P is/is.dic %{buildroot}%{_datadir}/hunspell/is.dic
ln -s %{_datadir}/hunspell/is.dic %{buildroot}%{_datadir}/myspell/is.dic
ln -s %{_datadir}/mythes/th_is.dat %{buildroot}%{_datadir}/mythes/th_is_v2.dat
ln -s %{_datadir}/mythes/th_is_v2.dat %{buildroot}%{_datadir}/myspell/th_is_v2.dat
ln -s %{_datadir}/mythes/th_is.dat %{buildroot}%{_datadir}/mythes/th_is_IS_v2.dat
ln -s %{_datadir}/mythes/th_is_IS_v2.dat %{buildroot}%{_datadir}/myspell/th_is_IS_v2.dat
cp -P is/th_is.dat %{buildroot}%{_datadir}/mythes/th_is.dat
ln -s %{_datadir}/mythes/th_is.dat %{buildroot}%{_datadir}/myspell/th_is.dat
ln -s %{_datadir}/mythes/th_is.idx %{buildroot}%{_datadir}/mythes/th_is_v2.idx
ln -s %{_datadir}/mythes/th_is_v2.idx %{buildroot}%{_datadir}/myspell/th_is_v2.idx
ln -s %{_datadir}/mythes/th_is.idx %{buildroot}%{_datadir}/mythes/th_is_IS_v2.idx
ln -s %{_datadir}/mythes/th_is_IS_v2.idx %{buildroot}%{_datadir}/myspell/th_is_IS_v2.idx
cp -P is/th_is.idx %{buildroot}%{_datadir}/mythes/th_is.idx
ln -s %{_datadir}/mythes/th_is.idx %{buildroot}%{_datadir}/myspell/th_is.idx
mkdir -p %{buildroot}%{_docdir}/myspell-is
cp -P is/description.xml %{buildroot}%{_docdir}/myspell-is/description.xml
cp -P is/dictionaries.xcu %{buildroot}%{_docdir}/myspell-is/dictionaries.xcu
cp -P is/license.txt %{buildroot}%{_docdir}/myspell-is/license.txt
cp -P it_IT/hyph_it_IT.dic %{buildroot}%{_datadir}/hyphen/hyph_it_IT.dic
ln -s %{_datadir}/hyphen/hyph_it_IT.dic %{buildroot}%{_datadir}/myspell/hyph_it_IT.dic
cp -P it_IT/it_IT.aff %{buildroot}%{_datadir}/hunspell/it_IT.aff
ln -s %{_datadir}/hunspell/it_IT.aff %{buildroot}%{_datadir}/myspell/it_IT.aff
cp -P it_IT/it_IT.dic %{buildroot}%{_datadir}/hunspell/it_IT.dic
ln -s %{_datadir}/hunspell/it_IT.dic %{buildroot}%{_datadir}/myspell/it_IT.dic
cp -P it_IT/th_it_IT_v2.dat %{buildroot}%{_datadir}/mythes/th_it_IT_v2.dat
ln -s %{_datadir}/mythes/th_it_IT_v2.dat %{buildroot}%{_datadir}/myspell/th_it_IT_v2.dat
cp -P it_IT/th_it_IT_v2.idx %{buildroot}%{_datadir}/mythes/th_it_IT_v2.idx
ln -s %{_datadir}/mythes/th_it_IT_v2.idx %{buildroot}%{_datadir}/myspell/th_it_IT_v2.idx
mkdir -p %{buildroot}%{_docdir}/myspell-it_IT
cp -P it_IT/CHANGELOG.txt %{buildroot}%{_docdir}/myspell-it_IT/CHANGELOG.txt
cp -P it_IT/README_hyph_it_IT.txt %{buildroot}%{_docdir}/myspell-it_IT/README_hyph_it_IT.txt
cp -P it_IT/README_it_IT.txt %{buildroot}%{_docdir}/myspell-it_IT/README_it_IT.txt
cp -P it_IT/README_th_it_IT.txt %{buildroot}%{_docdir}/myspell-it_IT/README_th_it_IT.txt
cp -P it_IT/description.xml %{buildroot}%{_docdir}/myspell-it_IT/description.xml
cp -P it_IT/dictionaries.xcu %{buildroot}%{_docdir}/myspell-it_IT/dictionaries.xcu
ln -s %{_datadir}/hunspell/kmr_Latn.aff %{buildroot}%{_datadir}/hunspell/kmr_Latn_TR.aff
ln -s %{_datadir}/hunspell/kmr_Latn_TR.aff %{buildroot}%{_datadir}/myspell/kmr_Latn_TR.aff
ln -s %{_datadir}/hunspell/kmr_Latn.aff %{buildroot}%{_datadir}/hunspell/kmr_Latn_SY.aff
ln -s %{_datadir}/hunspell/kmr_Latn_SY.aff %{buildroot}%{_datadir}/myspell/kmr_Latn_SY.aff
cp -P kmr_Latn/kmr_Latn.aff %{buildroot}%{_datadir}/hunspell/kmr_Latn.aff
ln -s %{_datadir}/hunspell/kmr_Latn.aff %{buildroot}%{_datadir}/myspell/kmr_Latn.aff
ln -s %{_datadir}/hunspell/kmr_Latn.dic %{buildroot}%{_datadir}/hunspell/kmr_Latn_TR.dic
ln -s %{_datadir}/hunspell/kmr_Latn_TR.dic %{buildroot}%{_datadir}/myspell/kmr_Latn_TR.dic
ln -s %{_datadir}/hunspell/kmr_Latn.dic %{buildroot}%{_datadir}/hunspell/kmr_Latn_SY.dic
ln -s %{_datadir}/hunspell/kmr_Latn_SY.dic %{buildroot}%{_datadir}/myspell/kmr_Latn_SY.dic
cp -P kmr_Latn/kmr_Latn.dic %{buildroot}%{_datadir}/hunspell/kmr_Latn.dic
ln -s %{_datadir}/hunspell/kmr_Latn.dic %{buildroot}%{_datadir}/myspell/kmr_Latn.dic
mkdir -p %{buildroot}%{_docdir}/myspell-kmr_Latn
cp -P kmr_Latn/MPL-1.1.txt %{buildroot}%{_docdir}/myspell-kmr_Latn/MPL-1.1.txt
cp -P kmr_Latn/README_kmr_Latn.txt %{buildroot}%{_docdir}/myspell-kmr_Latn/README_kmr_Latn.txt
cp -P kmr_Latn/description.xml %{buildroot}%{_docdir}/myspell-kmr_Latn/description.xml
cp -P kmr_Latn/dictionaries.xcu %{buildroot}%{_docdir}/myspell-kmr_Latn/dictionaries.xcu
cp -P kmr_Latn/ferheng.org.png %{buildroot}%{_docdir}/myspell-kmr_Latn/ferheng.org.png
cp -P kmr_Latn/gpl-3.0.txt %{buildroot}%{_docdir}/myspell-kmr_Latn/gpl-3.0.txt
cp -P kmr_Latn/lgpl-2.1.txt %{buildroot}%{_docdir}/myspell-kmr_Latn/lgpl-2.1.txt
cp -P kmr_Latn/license.txt %{buildroot}%{_docdir}/myspell-kmr_Latn/license.txt
cp -P lo_LA/lo_LA.aff %{buildroot}%{_datadir}/hunspell/lo_LA.aff
ln -s %{_datadir}/hunspell/lo_LA.aff %{buildroot}%{_datadir}/myspell/lo_LA.aff
cp -P lo_LA/lo_LA.dic %{buildroot}%{_datadir}/hunspell/lo_LA.dic
ln -s %{_datadir}/hunspell/lo_LA.dic %{buildroot}%{_datadir}/myspell/lo_LA.dic
mkdir -p %{buildroot}%{_docdir}/myspell-lo_LA
cp -P lo_LA/README_lo_LA.txt %{buildroot}%{_docdir}/myspell-lo_LA/README_lo_LA.txt
cp -P lo_LA/description.xml %{buildroot}%{_docdir}/myspell-lo_LA/description.xml
cp -P lo_LA/dictionaries.xcu %{buildroot}%{_docdir}/myspell-lo_LA/dictionaries.xcu
ln -s %{_datadir}/hyphen/hyph_lt.dic %{buildroot}%{_datadir}/hyphen/hyph_lt_LT.dic
ln -s %{_datadir}/hyphen/hyph_lt_LT.dic %{buildroot}%{_datadir}/myspell/hyph_lt_LT.dic
cp -P lt_LT/hyph_lt.dic %{buildroot}%{_datadir}/hyphen/hyph_lt.dic
ln -s %{_datadir}/hyphen/hyph_lt.dic %{buildroot}%{_datadir}/myspell/hyph_lt.dic
ln -s %{_datadir}/hunspell/lt.aff %{buildroot}%{_datadir}/hunspell/lt_LT.aff
ln -s %{_datadir}/hunspell/lt_LT.aff %{buildroot}%{_datadir}/myspell/lt_LT.aff
cp -P lt_LT/lt.aff %{buildroot}%{_datadir}/hunspell/lt.aff
ln -s %{_datadir}/hunspell/lt.aff %{buildroot}%{_datadir}/myspell/lt.aff
ln -s %{_datadir}/hunspell/lt.dic %{buildroot}%{_datadir}/hunspell/lt_LT.dic
ln -s %{_datadir}/hunspell/lt_LT.dic %{buildroot}%{_datadir}/myspell/lt_LT.dic
cp -P lt_LT/lt.dic %{buildroot}%{_datadir}/hunspell/lt.dic
ln -s %{_datadir}/hunspell/lt.dic %{buildroot}%{_datadir}/myspell/lt.dic
mkdir -p %{buildroot}%{_docdir}/myspell-lt_LT
cp -P lt_LT/AUTHORS %{buildroot}%{_docdir}/myspell-lt_LT/AUTHORS
cp -P lt_LT/COPYING %{buildroot}%{_docdir}/myspell-lt_LT/COPYING
cp -P lt_LT/README %{buildroot}%{_docdir}/myspell-lt_LT/README
cp -P lt_LT/README_hyph %{buildroot}%{_docdir}/myspell-lt_LT/README_hyph
cp -P lt_LT/description.xml %{buildroot}%{_docdir}/myspell-lt_LT/description.xml
cp -P lt_LT/dictionaries.xcu %{buildroot}%{_docdir}/myspell-lt_LT/dictionaries.xcu
cp -P lv_LV/hyph_lv_LV.dic %{buildroot}%{_datadir}/hyphen/hyph_lv_LV.dic
ln -s %{_datadir}/hyphen/hyph_lv_LV.dic %{buildroot}%{_datadir}/myspell/hyph_lv_LV.dic
cp -P lv_LV/lv_LV.aff %{buildroot}%{_datadir}/hunspell/lv_LV.aff
ln -s %{_datadir}/hunspell/lv_LV.aff %{buildroot}%{_datadir}/myspell/lv_LV.aff
cp -P lv_LV/lv_LV.dic %{buildroot}%{_datadir}/hunspell/lv_LV.dic
ln -s %{_datadir}/hunspell/lv_LV.dic %{buildroot}%{_datadir}/myspell/lv_LV.dic
cp -P lv_LV/th_lv_LV_v2.dat %{buildroot}%{_datadir}/mythes/th_lv_LV_v2.dat
ln -s %{_datadir}/mythes/th_lv_LV_v2.dat %{buildroot}%{_datadir}/myspell/th_lv_LV_v2.dat
cp -P lv_LV/th_lv_LV_v2.idx %{buildroot}%{_datadir}/mythes/th_lv_LV_v2.idx
ln -s %{_datadir}/mythes/th_lv_LV_v2.idx %{buildroot}%{_datadir}/myspell/th_lv_LV_v2.idx
mkdir -p %{buildroot}%{_docdir}/myspell-lv_LV
cp -P lv_LV/Changelog.txt %{buildroot}%{_docdir}/myspell-lv_LV/Changelog.txt
cp -P lv_LV/README_hyph_lv_LV.txt %{buildroot}%{_docdir}/myspell-lv_LV/README_hyph_lv_LV.txt
cp -P lv_LV/README_lv_LV.txt %{buildroot}%{_docdir}/myspell-lv_LV/README_lv_LV.txt
cp -P lv_LV/README_th_lv_LV_v2.txt %{buildroot}%{_docdir}/myspell-lv_LV/README_th_lv_LV_v2.txt
cp -P lv_LV/description.xml %{buildroot}%{_docdir}/myspell-lv_LV/description.xml
cp -P lv_LV/dictionaries.xcu %{buildroot}%{_docdir}/myspell-lv_LV/dictionaries.xcu
cp -P lv_LV/license.txt %{buildroot}%{_docdir}/myspell-lv_LV/license.txt
cp -P ne_NP/ne_NP.aff %{buildroot}%{_datadir}/hunspell/ne_NP.aff
ln -s %{_datadir}/hunspell/ne_NP.aff %{buildroot}%{_datadir}/myspell/ne_NP.aff
cp -P ne_NP/ne_NP.dic %{buildroot}%{_datadir}/hunspell/ne_NP.dic
ln -s %{_datadir}/hunspell/ne_NP.dic %{buildroot}%{_datadir}/myspell/ne_NP.dic
cp -P ne_NP/th_ne_NP_v2.dat %{buildroot}%{_datadir}/mythes/th_ne_NP_v2.dat
ln -s %{_datadir}/mythes/th_ne_NP_v2.dat %{buildroot}%{_datadir}/myspell/th_ne_NP_v2.dat
cp -P ne_NP/th_ne_NP_v2.idx %{buildroot}%{_datadir}/mythes/th_ne_NP_v2.idx
ln -s %{_datadir}/mythes/th_ne_NP_v2.idx %{buildroot}%{_datadir}/myspell/th_ne_NP_v2.idx
mkdir -p %{buildroot}%{_docdir}/myspell-ne_NP
cp -P ne_NP/README_ne_NP.txt %{buildroot}%{_docdir}/myspell-ne_NP/README_ne_NP.txt
cp -P ne_NP/README_th_ne_NP_v2.txt %{buildroot}%{_docdir}/myspell-ne_NP/README_th_ne_NP_v2.txt
cp -P ne_NP/description.xml %{buildroot}%{_docdir}/myspell-ne_NP/description.xml
cp -P ne_NP/dictionaries.xcu %{buildroot}%{_docdir}/myspell-ne_NP/dictionaries.xcu
ln -s %{_datadir}/hyphen/hyph_nl_NL.dic %{buildroot}%{_datadir}/hyphen/hyph_nl_BE.dic
ln -s %{_datadir}/hyphen/hyph_nl_BE.dic %{buildroot}%{_datadir}/myspell/hyph_nl_BE.dic
cp -P nl_NL/hyph_nl_NL.dic %{buildroot}%{_datadir}/hyphen/hyph_nl_NL.dic
ln -s %{_datadir}/hyphen/hyph_nl_NL.dic %{buildroot}%{_datadir}/myspell/hyph_nl_NL.dic
ln -s %{_datadir}/hunspell/nl_NL.aff %{buildroot}%{_datadir}/hunspell/nl_BE.aff
ln -s %{_datadir}/hunspell/nl_BE.aff %{buildroot}%{_datadir}/myspell/nl_BE.aff
cp -P nl_NL/nl_NL.aff %{buildroot}%{_datadir}/hunspell/nl_NL.aff
ln -s %{_datadir}/hunspell/nl_NL.aff %{buildroot}%{_datadir}/myspell/nl_NL.aff
ln -s %{_datadir}/hunspell/nl_NL.dic %{buildroot}%{_datadir}/hunspell/nl_BE.dic
ln -s %{_datadir}/hunspell/nl_BE.dic %{buildroot}%{_datadir}/myspell/nl_BE.dic
cp -P nl_NL/nl_NL.dic %{buildroot}%{_datadir}/hunspell/nl_NL.dic
ln -s %{_datadir}/hunspell/nl_NL.dic %{buildroot}%{_datadir}/myspell/nl_NL.dic
mkdir -p %{buildroot}%{_docdir}/myspell-nl_NL
cp -P nl_NL/OpenTaal.png %{buildroot}%{_docdir}/myspell-nl_NL/OpenTaal.png
cp -P nl_NL/README_NL.txt %{buildroot}%{_docdir}/myspell-nl_NL/README_NL.txt
cp -P nl_NL/desc_en_US.txt %{buildroot}%{_docdir}/myspell-nl_NL/desc_en_US.txt
cp -P nl_NL/desc_nl_NL.txt %{buildroot}%{_docdir}/myspell-nl_NL/desc_nl_NL.txt
cp -P nl_NL/description.xml %{buildroot}%{_docdir}/myspell-nl_NL/description.xml
cp -P nl_NL/dictionaries.xcu %{buildroot}%{_docdir}/myspell-nl_NL/dictionaries.xcu
cp -P nl_NL/license_en_EN.txt %{buildroot}%{_docdir}/myspell-nl_NL/license_en_EN.txt
cp -P nl_NL/licentie_nl_NL.txt %{buildroot}%{_docdir}/myspell-nl_NL/licentie_nl_NL.txt
cp -P no/hyph_nb_NO.dic %{buildroot}%{_datadir}/hyphen/hyph_nb_NO.dic
ln -s %{_datadir}/hyphen/hyph_nb_NO.dic %{buildroot}%{_datadir}/myspell/hyph_nb_NO.dic
cp -P no/hyph_nn_NO.dic %{buildroot}%{_datadir}/hyphen/hyph_nn_NO.dic
ln -s %{_datadir}/hyphen/hyph_nn_NO.dic %{buildroot}%{_datadir}/myspell/hyph_nn_NO.dic
cp -P no/nb_NO.aff %{buildroot}%{_datadir}/hunspell/nb_NO.aff
ln -s %{_datadir}/hunspell/nb_NO.aff %{buildroot}%{_datadir}/myspell/nb_NO.aff
cp -P no/nb_NO.dic %{buildroot}%{_datadir}/hunspell/nb_NO.dic
ln -s %{_datadir}/hunspell/nb_NO.dic %{buildroot}%{_datadir}/myspell/nb_NO.dic
cp -P no/nn_NO.aff %{buildroot}%{_datadir}/hunspell/nn_NO.aff
ln -s %{_datadir}/hunspell/nn_NO.aff %{buildroot}%{_datadir}/myspell/nn_NO.aff
cp -P no/nn_NO.dic %{buildroot}%{_datadir}/hunspell/nn_NO.dic
ln -s %{_datadir}/hunspell/nn_NO.dic %{buildroot}%{_datadir}/myspell/nn_NO.dic
cp -P no/th_nb_NO_v2.dat %{buildroot}%{_datadir}/mythes/th_nb_NO_v2.dat
ln -s %{_datadir}/mythes/th_nb_NO_v2.dat %{buildroot}%{_datadir}/myspell/th_nb_NO_v2.dat
cp -P no/th_nb_NO_v2.idx %{buildroot}%{_datadir}/mythes/th_nb_NO_v2.idx
ln -s %{_datadir}/mythes/th_nb_NO_v2.idx %{buildroot}%{_datadir}/myspell/th_nb_NO_v2.idx
cp -P no/th_nn_NO_v2.dat %{buildroot}%{_datadir}/mythes/th_nn_NO_v2.dat
ln -s %{_datadir}/mythes/th_nn_NO_v2.dat %{buildroot}%{_datadir}/myspell/th_nn_NO_v2.dat
cp -P no/th_nn_NO_v2.idx %{buildroot}%{_datadir}/mythes/th_nn_NO_v2.idx
ln -s %{_datadir}/mythes/th_nn_NO_v2.idx %{buildroot}%{_datadir}/myspell/th_nn_NO_v2.idx
mkdir -p %{buildroot}%{_docdir}/myspell-no
cp -P no/COPYING %{buildroot}%{_docdir}/myspell-no/COPYING
cp -P no/README_hyph_NO.txt %{buildroot}%{_docdir}/myspell-no/README_hyph_NO.txt
cp -P no/description.xml %{buildroot}%{_docdir}/myspell-no/description.xml
cp -P no/dictionaries.xcu %{buildroot}%{_docdir}/myspell-no/dictionaries.xcu
cp -P oc_FR/oc_FR.aff %{buildroot}%{_datadir}/hunspell/oc_FR.aff
ln -s %{_datadir}/hunspell/oc_FR.aff %{buildroot}%{_datadir}/myspell/oc_FR.aff
cp -P oc_FR/oc_FR.dic %{buildroot}%{_datadir}/hunspell/oc_FR.dic
ln -s %{_datadir}/hunspell/oc_FR.dic %{buildroot}%{_datadir}/myspell/oc_FR.dic
mkdir -p %{buildroot}%{_docdir}/myspell-oc_FR
cp -P oc_FR/LICENCES-fr.txt %{buildroot}%{_docdir}/myspell-oc_FR/LICENCES-fr.txt
cp -P oc_FR/LICENSES-en.txt %{buildroot}%{_docdir}/myspell-oc_FR/LICENSES-en.txt
cp -P oc_FR/README_oc_FR.txt %{buildroot}%{_docdir}/myspell-oc_FR/README_oc_FR.txt
cp -P oc_FR/description.xml %{buildroot}%{_docdir}/myspell-oc_FR/description.xml
cp -P oc_FR/dictionaries.xcu %{buildroot}%{_docdir}/myspell-oc_FR/dictionaries.xcu
cp -P pl_PL/hyph_pl_PL.dic %{buildroot}%{_datadir}/hyphen/hyph_pl_PL.dic
ln -s %{_datadir}/hyphen/hyph_pl_PL.dic %{buildroot}%{_datadir}/myspell/hyph_pl_PL.dic
cp -P pl_PL/pl_PL.aff %{buildroot}%{_datadir}/hunspell/pl_PL.aff
ln -s %{_datadir}/hunspell/pl_PL.aff %{buildroot}%{_datadir}/myspell/pl_PL.aff
cp -P pl_PL/pl_PL.dic %{buildroot}%{_datadir}/hunspell/pl_PL.dic
ln -s %{_datadir}/hunspell/pl_PL.dic %{buildroot}%{_datadir}/myspell/pl_PL.dic
cp -P pl_PL/th_pl_PL_v2.dat %{buildroot}%{_datadir}/mythes/th_pl_PL_v2.dat
ln -s %{_datadir}/mythes/th_pl_PL_v2.dat %{buildroot}%{_datadir}/myspell/th_pl_PL_v2.dat
cp -P pl_PL/th_pl_PL_v2.idx %{buildroot}%{_datadir}/mythes/th_pl_PL_v2.idx
ln -s %{_datadir}/mythes/th_pl_PL_v2.idx %{buildroot}%{_datadir}/myspell/th_pl_PL_v2.idx
mkdir -p %{buildroot}%{_docdir}/myspell-pl_PL
cp -P pl_PL/README_en.txt %{buildroot}%{_docdir}/myspell-pl_PL/README_en.txt
cp -P pl_PL/README_pl.txt %{buildroot}%{_docdir}/myspell-pl_PL/README_pl.txt
cp -P pl_PL/description.xml %{buildroot}%{_docdir}/myspell-pl_PL/description.xml
cp -P pl_PL/dictionaries.xcu %{buildroot}%{_docdir}/myspell-pl_PL/dictionaries.xcu
cp -P pl_PL/plhyph.tex %{buildroot}%{_docdir}/myspell-pl_PL/plhyph.tex
cp -P pt_BR/hyph_pt_BR.dic %{buildroot}%{_datadir}/hyphen/hyph_pt_BR.dic
ln -s %{_datadir}/hyphen/hyph_pt_BR.dic %{buildroot}%{_datadir}/myspell/hyph_pt_BR.dic
cp -P pt_BR/pt_BR.aff %{buildroot}%{_datadir}/hunspell/pt_BR.aff
ln -s %{_datadir}/hunspell/pt_BR.aff %{buildroot}%{_datadir}/myspell/pt_BR.aff
cp -P pt_BR/pt_BR.dic %{buildroot}%{_datadir}/hunspell/pt_BR.dic
ln -s %{_datadir}/hunspell/pt_BR.dic %{buildroot}%{_datadir}/myspell/pt_BR.dic
mkdir -p %{buildroot}%{_libdir}/libreoffice/share/extensions/lightproof-pt_BR
cp -rP pt_BR/Lightproof.components %{buildroot}%{_libdir}/libreoffice/share/extensions/lightproof-pt_BR/Lightproof.components
cp -rP pt_BR/Lightproof.py %{buildroot}%{_libdir}/libreoffice/share/extensions/lightproof-pt_BR/Lightproof.py
cp -rP pt_BR/Linguistic.xcu %{buildroot}%{_libdir}/libreoffice/share/extensions/lightproof-pt_BR/Linguistic.xcu
cp -rP pt_BR/META-INF %{buildroot}%{_libdir}/libreoffice/share/extensions/lightproof-pt_BR/META-INF
cp -rP pt_BR/description.xml %{buildroot}%{_libdir}/libreoffice/share/extensions/lightproof-pt_BR/description.xml
cp -rP pt_BR/dialog %{buildroot}%{_libdir}/libreoffice/share/extensions/lightproof-pt_BR/dialog
cp -rP pt_BR/icons %{buildroot}%{_libdir}/libreoffice/share/extensions/lightproof-pt_BR/icons
cp -rP pt_BR/pythonpath %{buildroot}%{_libdir}/libreoffice/share/extensions/lightproof-pt_BR/pythonpath
mkdir -p %{buildroot}%{_docdir}/myspell-pt_BR
cp -P pt_BR/Linguistic.xcu %{buildroot}%{_docdir}/myspell-pt_BR/Linguistic.xcu
cp -P pt_BR/README_Lightproof_pt_BR.txt %{buildroot}%{_docdir}/myspell-pt_BR/README_Lightproof_pt_BR.txt
cp -P pt_BR/README_en.txt %{buildroot}%{_docdir}/myspell-pt_BR/README_en.txt
cp -P pt_BR/README_hyph_pt_BR.txt %{buildroot}%{_docdir}/myspell-pt_BR/README_hyph_pt_BR.txt
cp -P pt_BR/README_pt_BR.txt %{buildroot}%{_docdir}/myspell-pt_BR/README_pt_BR.txt
cp -P pt_BR/description.xml %{buildroot}%{_docdir}/myspell-pt_BR/description.xml
cp -P pt_BR/dictionaries.xcu %{buildroot}%{_docdir}/myspell-pt_BR/dictionaries.xcu
cp -P pt_BR/package-description.txt %{buildroot}%{_docdir}/myspell-pt_BR/package-description.txt
ln -s %{_datadir}/hyphen/hyph_pt_PT.dic %{buildroot}%{_datadir}/hyphen/hyph_pt_AO.dic
ln -s %{_datadir}/hyphen/hyph_pt_AO.dic %{buildroot}%{_datadir}/myspell/hyph_pt_AO.dic
cp -P pt_PT/hyph_pt_PT.dic %{buildroot}%{_datadir}/hyphen/hyph_pt_PT.dic
ln -s %{_datadir}/hyphen/hyph_pt_PT.dic %{buildroot}%{_datadir}/myspell/hyph_pt_PT.dic
ln -s %{_datadir}/hunspell/pt_PT.aff %{buildroot}%{_datadir}/hunspell/pt_AO.aff
ln -s %{_datadir}/hunspell/pt_AO.aff %{buildroot}%{_datadir}/myspell/pt_AO.aff
cp -P pt_PT/pt_PT.aff %{buildroot}%{_datadir}/hunspell/pt_PT.aff
ln -s %{_datadir}/hunspell/pt_PT.aff %{buildroot}%{_datadir}/myspell/pt_PT.aff
ln -s %{_datadir}/hunspell/pt_PT.dic %{buildroot}%{_datadir}/hunspell/pt_AO.dic
ln -s %{_datadir}/hunspell/pt_AO.dic %{buildroot}%{_datadir}/myspell/pt_AO.dic
cp -P pt_PT/pt_PT.dic %{buildroot}%{_datadir}/hunspell/pt_PT.dic
ln -s %{_datadir}/hunspell/pt_PT.dic %{buildroot}%{_datadir}/myspell/pt_PT.dic
ln -s %{_datadir}/mythes/th_pt_PT_v2.dat %{buildroot}%{_datadir}/mythes/th_pt_AO_v2.dat
ln -s %{_datadir}/mythes/th_pt_AO_v2.dat %{buildroot}%{_datadir}/myspell/th_pt_AO_v2.dat
cp -P pt_PT/th_pt_PT_v2.dat %{buildroot}%{_datadir}/mythes/th_pt_PT_v2.dat
ln -s %{_datadir}/mythes/th_pt_PT_v2.dat %{buildroot}%{_datadir}/myspell/th_pt_PT_v2.dat
ln -s %{_datadir}/mythes/th_pt_PT_v2.idx %{buildroot}%{_datadir}/mythes/th_pt_AO_v2.idx
ln -s %{_datadir}/mythes/th_pt_AO_v2.idx %{buildroot}%{_datadir}/myspell/th_pt_AO_v2.idx
cp -P pt_PT/th_pt_PT_v2.idx %{buildroot}%{_datadir}/mythes/th_pt_PT_v2.idx
ln -s %{_datadir}/mythes/th_pt_PT_v2.idx %{buildroot}%{_datadir}/myspell/th_pt_PT_v2.idx
mkdir -p %{buildroot}%{_docdir}/myspell-pt_PT
cp -P pt_PT/LICENSES.txt %{buildroot}%{_docdir}/myspell-pt_PT/LICENSES.txt
cp -P pt_PT/README_hyph_pt_PT.txt %{buildroot}%{_docdir}/myspell-pt_PT/README_hyph_pt_PT.txt
cp -P pt_PT/README_pt_PT.txt %{buildroot}%{_docdir}/myspell-pt_PT/README_pt_PT.txt
cp -P pt_PT/README_th_pt_PT_v2.txt %{buildroot}%{_docdir}/myspell-pt_PT/README_th_pt_PT_v2.txt
cp -P pt_PT/description.xml %{buildroot}%{_docdir}/myspell-pt_PT/description.xml
cp -P pt_PT/dictionaries.xcu %{buildroot}%{_docdir}/myspell-pt_PT/dictionaries.xcu
cp -P pt_PT/icon.png %{buildroot}%{_docdir}/myspell-pt_PT/icon.png
cp -P ro/hyph_ro_RO.dic %{buildroot}%{_datadir}/hyphen/hyph_ro_RO.dic
ln -s %{_datadir}/hyphen/hyph_ro_RO.dic %{buildroot}%{_datadir}/myspell/hyph_ro_RO.dic
cp -P ro/ro_RO.aff %{buildroot}%{_datadir}/hunspell/ro_RO.aff
ln -s %{_datadir}/hunspell/ro_RO.aff %{buildroot}%{_datadir}/myspell/ro_RO.aff
cp -P ro/ro_RO.dic %{buildroot}%{_datadir}/hunspell/ro_RO.dic
ln -s %{_datadir}/hunspell/ro_RO.dic %{buildroot}%{_datadir}/myspell/ro_RO.dic
cp -P ro/th_ro_RO_v2.dat %{buildroot}%{_datadir}/mythes/th_ro_RO_v2.dat
ln -s %{_datadir}/mythes/th_ro_RO_v2.dat %{buildroot}%{_datadir}/myspell/th_ro_RO_v2.dat
cp -P ro/th_ro_RO_v2.idx %{buildroot}%{_datadir}/mythes/th_ro_RO_v2.idx
ln -s %{_datadir}/mythes/th_ro_RO_v2.idx %{buildroot}%{_datadir}/myspell/th_ro_RO_v2.idx
mkdir -p %{buildroot}%{_docdir}/myspell-ro
cp -P ro/README_EN.txt %{buildroot}%{_docdir}/myspell-ro/README_EN.txt
cp -P ro/README_RO.txt %{buildroot}%{_docdir}/myspell-ro/README_RO.txt
cp -P ro/description.xml %{buildroot}%{_docdir}/myspell-ro/description.xml
cp -P ro/dictionaries.xcu %{buildroot}%{_docdir}/myspell-ro/dictionaries.xcu
cp -P ru_RU/hyph_ru_RU.dic %{buildroot}%{_datadir}/hyphen/hyph_ru_RU.dic
ln -s %{_datadir}/hyphen/hyph_ru_RU.dic %{buildroot}%{_datadir}/myspell/hyph_ru_RU.dic
cp -P ru_RU/ru_RU.aff %{buildroot}%{_datadir}/hunspell/ru_RU.aff
ln -s %{_datadir}/hunspell/ru_RU.aff %{buildroot}%{_datadir}/myspell/ru_RU.aff
cp -P ru_RU/ru_RU.dic %{buildroot}%{_datadir}/hunspell/ru_RU.dic
ln -s %{_datadir}/hunspell/ru_RU.dic %{buildroot}%{_datadir}/myspell/ru_RU.dic
ln -s %{_datadir}/mythes/th_ru_RU_M_aot_and_v2.dat %{buildroot}%{_datadir}/mythes/th_ru_RU_v2.dat
ln -s %{_datadir}/mythes/th_ru_RU_v2.dat %{buildroot}%{_datadir}/myspell/th_ru_RU_v2.dat
cp -P ru_RU/th_ru_RU_M_aot_and_v2.dat %{buildroot}%{_datadir}/mythes/th_ru_RU_M_aot_and_v2.dat
ln -s %{_datadir}/mythes/th_ru_RU_M_aot_and_v2.dat %{buildroot}%{_datadir}/myspell/th_ru_RU_M_aot_and_v2.dat
ln -s %{_datadir}/mythes/th_ru_RU_M_aot_and_v2.idx %{buildroot}%{_datadir}/mythes/th_ru_RU_v2.idx
ln -s %{_datadir}/mythes/th_ru_RU_v2.idx %{buildroot}%{_datadir}/myspell/th_ru_RU_v2.idx
cp -P ru_RU/th_ru_RU_M_aot_and_v2.idx %{buildroot}%{_datadir}/mythes/th_ru_RU_M_aot_and_v2.idx
ln -s %{_datadir}/mythes/th_ru_RU_M_aot_and_v2.idx %{buildroot}%{_datadir}/myspell/th_ru_RU_M_aot_and_v2.idx
mkdir -p %{buildroot}%{_libdir}/libreoffice/share/extensions/lightproof-ru_RU
cp -rP ru_RU/Lightproof.components %{buildroot}%{_libdir}/libreoffice/share/extensions/lightproof-ru_RU/Lightproof.components
cp -rP ru_RU/Lightproof.py %{buildroot}%{_libdir}/libreoffice/share/extensions/lightproof-ru_RU/Lightproof.py
cp -rP ru_RU/Linguistic.xcu %{buildroot}%{_libdir}/libreoffice/share/extensions/lightproof-ru_RU/Linguistic.xcu
cp -rP ru_RU/META-INF %{buildroot}%{_libdir}/libreoffice/share/extensions/lightproof-ru_RU/META-INF
cp -rP ru_RU/description.xml %{buildroot}%{_libdir}/libreoffice/share/extensions/lightproof-ru_RU/description.xml
cp -rP ru_RU/dialog %{buildroot}%{_libdir}/libreoffice/share/extensions/lightproof-ru_RU/dialog
cp -rP ru_RU/pythonpath %{buildroot}%{_libdir}/libreoffice/share/extensions/lightproof-ru_RU/pythonpath
mkdir -p %{buildroot}%{_docdir}/myspell-ru_RU
cp -P ru_RU/Linguistic.xcu %{buildroot}%{_docdir}/myspell-ru_RU/Linguistic.xcu
cp -P ru_RU/README_Lightproof_ru_RU.txt %{buildroot}%{_docdir}/myspell-ru_RU/README_Lightproof_ru_RU.txt
cp -P ru_RU/README_ru_RU.txt %{buildroot}%{_docdir}/myspell-ru_RU/README_ru_RU.txt
cp -P ru_RU/README_thes_ru_RU_M_aot_and_v2.txt %{buildroot}%{_docdir}/myspell-ru_RU/README_thes_ru_RU_M_aot_and_v2.txt
cp -P ru_RU/description.xml %{buildroot}%{_docdir}/myspell-ru_RU/description.xml
cp -P ru_RU/dictionaries.xcu %{buildroot}%{_docdir}/myspell-ru_RU/dictionaries.xcu
cp -P si_LK/si_LK.aff %{buildroot}%{_datadir}/hunspell/si_LK.aff
ln -s %{_datadir}/hunspell/si_LK.aff %{buildroot}%{_datadir}/myspell/si_LK.aff
cp -P si_LK/si_LK.dic %{buildroot}%{_datadir}/hunspell/si_LK.dic
ln -s %{_datadir}/hunspell/si_LK.dic %{buildroot}%{_datadir}/myspell/si_LK.dic
mkdir -p %{buildroot}%{_docdir}/myspell-si_LK
cp -P si_LK/LICENSES-en.txt %{buildroot}%{_docdir}/myspell-si_LK/LICENSES-en.txt
cp -P si_LK/description.xml %{buildroot}%{_docdir}/myspell-si_LK/description.xml
cp -P si_LK/dictionaries.xcu %{buildroot}%{_docdir}/myspell-si_LK/dictionaries.xcu
cp -P sk_SK/hyph_sk_SK.dic %{buildroot}%{_datadir}/hyphen/hyph_sk_SK.dic
ln -s %{_datadir}/hyphen/hyph_sk_SK.dic %{buildroot}%{_datadir}/myspell/hyph_sk_SK.dic
cp -P sk_SK/sk_SK.aff %{buildroot}%{_datadir}/hunspell/sk_SK.aff
ln -s %{_datadir}/hunspell/sk_SK.aff %{buildroot}%{_datadir}/myspell/sk_SK.aff
cp -P sk_SK/sk_SK.dic %{buildroot}%{_datadir}/hunspell/sk_SK.dic
ln -s %{_datadir}/hunspell/sk_SK.dic %{buildroot}%{_datadir}/myspell/sk_SK.dic
cp -P sk_SK/th_sk_SK_v2.dat %{buildroot}%{_datadir}/mythes/th_sk_SK_v2.dat
ln -s %{_datadir}/mythes/th_sk_SK_v2.dat %{buildroot}%{_datadir}/myspell/th_sk_SK_v2.dat
cp -P sk_SK/th_sk_SK_v2.idx %{buildroot}%{_datadir}/mythes/th_sk_SK_v2.idx
ln -s %{_datadir}/mythes/th_sk_SK_v2.idx %{buildroot}%{_datadir}/myspell/th_sk_SK_v2.idx
mkdir -p %{buildroot}%{_docdir}/myspell-sk_SK
cp -P sk_SK/LICENSE.txt %{buildroot}%{_docdir}/myspell-sk_SK/LICENSE.txt
cp -P sk_SK/README_en.txt %{buildroot}%{_docdir}/myspell-sk_SK/README_en.txt
cp -P sk_SK/README_sk.txt %{buildroot}%{_docdir}/myspell-sk_SK/README_sk.txt
cp -P sk_SK/README_th_sk_SK_v2.txt %{buildroot}%{_docdir}/myspell-sk_SK/README_th_sk_SK_v2.txt
cp -P sk_SK/description.xml %{buildroot}%{_docdir}/myspell-sk_SK/description.xml
cp -P sk_SK/dictionaries.xcu %{buildroot}%{_docdir}/myspell-sk_SK/dictionaries.xcu
cp -P sk_SK/release_en.txt %{buildroot}%{_docdir}/myspell-sk_SK/release_en.txt
cp -P sk_SK/release_sk.txt %{buildroot}%{_docdir}/myspell-sk_SK/release_sk.txt
cp -P sl_SI/hyph_sl_SI.dic %{buildroot}%{_datadir}/hyphen/hyph_sl_SI.dic
ln -s %{_datadir}/hyphen/hyph_sl_SI.dic %{buildroot}%{_datadir}/myspell/hyph_sl_SI.dic
cp -P sl_SI/sl_SI.aff %{buildroot}%{_datadir}/hunspell/sl_SI.aff
ln -s %{_datadir}/hunspell/sl_SI.aff %{buildroot}%{_datadir}/myspell/sl_SI.aff
cp -P sl_SI/sl_SI.dic %{buildroot}%{_datadir}/hunspell/sl_SI.dic
ln -s %{_datadir}/hunspell/sl_SI.dic %{buildroot}%{_datadir}/myspell/sl_SI.dic
cp -P sl_SI/th_sl_SI_v2.dat %{buildroot}%{_datadir}/mythes/th_sl_SI_v2.dat
ln -s %{_datadir}/mythes/th_sl_SI_v2.dat %{buildroot}%{_datadir}/myspell/th_sl_SI_v2.dat
cp -P sl_SI/th_sl_SI_v2.idx %{buildroot}%{_datadir}/mythes/th_sl_SI_v2.idx
ln -s %{_datadir}/mythes/th_sl_SI_v2.idx %{buildroot}%{_datadir}/myspell/th_sl_SI_v2.idx
mkdir -p %{buildroot}%{_docdir}/myspell-sl_SI
cp -P sl_SI/README_hyph_sl_SI.txt %{buildroot}%{_docdir}/myspell-sl_SI/README_hyph_sl_SI.txt
cp -P sl_SI/README_sl_SI.txt %{buildroot}%{_docdir}/myspell-sl_SI/README_sl_SI.txt
cp -P sl_SI/README_th_sl_SI.txt %{buildroot}%{_docdir}/myspell-sl_SI/README_th_sl_SI.txt
cp -P sl_SI/description.xml %{buildroot}%{_docdir}/myspell-sl_SI/description.xml
cp -P sl_SI/dictionaries.xcu %{buildroot}%{_docdir}/myspell-sl_SI/dictionaries.xcu
cp -P sl_SI/icon.png %{buildroot}%{_docdir}/myspell-sl_SI/icon.png
cp -P sl_SI/package-description.txt %{buildroot}%{_docdir}/myspell-sl_SI/package-description.txt
cp -P sq_AL/sq_AL.aff %{buildroot}%{_datadir}/hunspell/sq_AL.aff
ln -s %{_datadir}/hunspell/sq_AL.aff %{buildroot}%{_datadir}/myspell/sq_AL.aff
cp -P sq_AL/sq_AL.dic %{buildroot}%{_datadir}/hunspell/sq_AL.dic
ln -s %{_datadir}/hunspell/sq_AL.dic %{buildroot}%{_datadir}/myspell/sq_AL.dic
mkdir -p %{buildroot}%{_docdir}/myspell-sq_AL
cp -P sq_AL/README.txt %{buildroot}%{_docdir}/myspell-sq_AL/README.txt
cp -P sq_AL/description.xml %{buildroot}%{_docdir}/myspell-sq_AL/description.xml
cp -P sq_AL/dictionaries.xcu %{buildroot}%{_docdir}/myspell-sq_AL/dictionaries.xcu
ln -s %{_datadir}/hyphen/hyph_sr.dic %{buildroot}%{_datadir}/hyphen/hyph_sr_RS.dic
ln -s %{_datadir}/hyphen/hyph_sr_RS.dic %{buildroot}%{_datadir}/myspell/hyph_sr_RS.dic
ln -s %{_datadir}/hyphen/hyph_sr.dic %{buildroot}%{_datadir}/hyphen/hyph_sr_CS.dic
ln -s %{_datadir}/hyphen/hyph_sr_CS.dic %{buildroot}%{_datadir}/myspell/hyph_sr_CS.dic
cp -P sr/hyph_sr.dic %{buildroot}%{_datadir}/hyphen/hyph_sr.dic
ln -s %{_datadir}/hyphen/hyph_sr.dic %{buildroot}%{_datadir}/myspell/hyph_sr.dic
ln -s %{_datadir}/hyphen/hyph_sr-Latn.dic %{buildroot}%{_datadir}/hyphen/hyph_sr_Latn_RS.dic
ln -s %{_datadir}/hyphen/hyph_sr_Latn_RS.dic %{buildroot}%{_datadir}/myspell/hyph_sr_Latn_RS.dic
ln -s %{_datadir}/hyphen/hyph_sr-Latn.dic %{buildroot}%{_datadir}/hyphen/hyph_sr_Latn_CS.dic
ln -s %{_datadir}/hyphen/hyph_sr_Latn_CS.dic %{buildroot}%{_datadir}/myspell/hyph_sr_Latn_CS.dic
cp -P sr/hyph_sr-Latn.dic %{buildroot}%{_datadir}/hyphen/hyph_sr-Latn.dic
ln -s %{_datadir}/hyphen/hyph_sr-Latn.dic %{buildroot}%{_datadir}/myspell/hyph_sr-Latn.dic
ln -s %{_datadir}/hunspell/sr.aff %{buildroot}%{_datadir}/hunspell/sr_RS.aff
ln -s %{_datadir}/hunspell/sr_RS.aff %{buildroot}%{_datadir}/myspell/sr_RS.aff
ln -s %{_datadir}/hunspell/sr.aff %{buildroot}%{_datadir}/hunspell/sr_CS.aff
ln -s %{_datadir}/hunspell/sr_CS.aff %{buildroot}%{_datadir}/myspell/sr_CS.aff
cp -P sr/sr.aff %{buildroot}%{_datadir}/hunspell/sr.aff
ln -s %{_datadir}/hunspell/sr.aff %{buildroot}%{_datadir}/myspell/sr.aff
ln -s %{_datadir}/hunspell/sr.dic %{buildroot}%{_datadir}/hunspell/sr_RS.dic
ln -s %{_datadir}/hunspell/sr_RS.dic %{buildroot}%{_datadir}/myspell/sr_RS.dic
ln -s %{_datadir}/hunspell/sr.dic %{buildroot}%{_datadir}/hunspell/sr_CS.dic
ln -s %{_datadir}/hunspell/sr_CS.dic %{buildroot}%{_datadir}/myspell/sr_CS.dic
cp -P sr/sr.dic %{buildroot}%{_datadir}/hunspell/sr.dic
ln -s %{_datadir}/hunspell/sr.dic %{buildroot}%{_datadir}/myspell/sr.dic
ln -s %{_datadir}/hunspell/sr-Latn.aff %{buildroot}%{_datadir}/hunspell/sr_Latn_RS.aff
ln -s %{_datadir}/hunspell/sr_Latn_RS.aff %{buildroot}%{_datadir}/myspell/sr_Latn_RS.aff
ln -s %{_datadir}/hunspell/sr-Latn.aff %{buildroot}%{_datadir}/hunspell/sr_Latn_CS.aff
ln -s %{_datadir}/hunspell/sr_Latn_CS.aff %{buildroot}%{_datadir}/myspell/sr_Latn_CS.aff
cp -P sr/sr-Latn.aff %{buildroot}%{_datadir}/hunspell/sr-Latn.aff
ln -s %{_datadir}/hunspell/sr-Latn.aff %{buildroot}%{_datadir}/myspell/sr-Latn.aff
ln -s %{_datadir}/hunspell/sr-Latn.dic %{buildroot}%{_datadir}/hunspell/sr_Latn_RS.dic
ln -s %{_datadir}/hunspell/sr_Latn_RS.dic %{buildroot}%{_datadir}/myspell/sr_Latn_RS.dic
ln -s %{_datadir}/hunspell/sr-Latn.dic %{buildroot}%{_datadir}/hunspell/sr_Latn_CS.dic
ln -s %{_datadir}/hunspell/sr_Latn_CS.dic %{buildroot}%{_datadir}/myspell/sr_Latn_CS.dic
cp -P sr/sr-Latn.dic %{buildroot}%{_datadir}/hunspell/sr-Latn.dic
ln -s %{_datadir}/hunspell/sr-Latn.dic %{buildroot}%{_datadir}/myspell/sr-Latn.dic
mkdir -p %{buildroot}%{_docdir}/myspell-sr
cp -P sr/README.txt %{buildroot}%{_docdir}/myspell-sr/README.txt
cp -P sr/description.xml %{buildroot}%{_docdir}/myspell-sr/description.xml
cp -P sr/dictionaries.xcu %{buildroot}%{_docdir}/myspell-sr/dictionaries.xcu
ln -s %{_datadir}/hyphen/hyph_sv.dic %{buildroot}%{_datadir}/hyphen/hyph_sv_SE.dic
ln -s %{_datadir}/hyphen/hyph_sv_SE.dic %{buildroot}%{_datadir}/myspell/hyph_sv_SE.dic
ln -s %{_datadir}/hyphen/hyph_sv.dic %{buildroot}%{_datadir}/hyphen/hyph_sv_FI.dic
ln -s %{_datadir}/hyphen/hyph_sv_FI.dic %{buildroot}%{_datadir}/myspell/hyph_sv_FI.dic
cp -P sv_SE/hyph_sv.dic %{buildroot}%{_datadir}/hyphen/hyph_sv.dic
ln -s %{_datadir}/hyphen/hyph_sv.dic %{buildroot}%{_datadir}/myspell/hyph_sv.dic
cp -P sv_SE/sv_FI.aff %{buildroot}%{_datadir}/hunspell/sv_FI.aff
ln -s %{_datadir}/hunspell/sv_FI.aff %{buildroot}%{_datadir}/myspell/sv_FI.aff
cp -P sv_SE/sv_FI.dic %{buildroot}%{_datadir}/hunspell/sv_FI.dic
ln -s %{_datadir}/hunspell/sv_FI.dic %{buildroot}%{_datadir}/myspell/sv_FI.dic
cp -P sv_SE/sv_SE.aff %{buildroot}%{_datadir}/hunspell/sv_SE.aff
ln -s %{_datadir}/hunspell/sv_SE.aff %{buildroot}%{_datadir}/myspell/sv_SE.aff
cp -P sv_SE/sv_SE.dic %{buildroot}%{_datadir}/hunspell/sv_SE.dic
ln -s %{_datadir}/hunspell/sv_SE.dic %{buildroot}%{_datadir}/myspell/sv_SE.dic
ln -s %{_datadir}/mythes/th_sv_SE.dat %{buildroot}%{_datadir}/mythes/th_sv_SE_v2.dat
ln -s %{_datadir}/mythes/th_sv_SE_v2.dat %{buildroot}%{_datadir}/myspell/th_sv_SE_v2.dat
cp -P sv_SE/th_sv_SE.dat %{buildroot}%{_datadir}/mythes/th_sv_SE.dat
ln -s %{_datadir}/mythes/th_sv_SE.dat %{buildroot}%{_datadir}/myspell/th_sv_SE.dat
ln -s %{_datadir}/mythes/th_sv_SE.idx %{buildroot}%{_datadir}/mythes/th_sv_SE_v2.idx
ln -s %{_datadir}/mythes/th_sv_SE_v2.idx %{buildroot}%{_datadir}/myspell/th_sv_SE_v2.idx
cp -P sv_SE/th_sv_SE.idx %{buildroot}%{_datadir}/mythes/th_sv_SE.idx
ln -s %{_datadir}/mythes/th_sv_SE.idx %{buildroot}%{_datadir}/myspell/th_sv_SE.idx
mkdir -p %{buildroot}%{_docdir}/myspell-sv_SE
cp -P sv_SE/LICENSE_en_US.txt %{buildroot}%{_docdir}/myspell-sv_SE/LICENSE_en_US.txt
cp -P sv_SE/LICENSE_sv_SE.txt %{buildroot}%{_docdir}/myspell-sv_SE/LICENSE_sv_SE.txt
cp -P sv_SE/README_hyph_sv.txt %{buildroot}%{_docdir}/myspell-sv_SE/README_hyph_sv.txt
cp -P sv_SE/README_th_sv_SE.txt %{buildroot}%{_docdir}/myspell-sv_SE/README_th_sv_SE.txt
cp -P sv_SE/description.xml %{buildroot}%{_docdir}/myspell-sv_SE/description.xml
cp -P sv_SE/dictionaries.xcu %{buildroot}%{_docdir}/myspell-sv_SE/dictionaries.xcu
cp -P sw_TZ/sw_TZ.aff %{buildroot}%{_datadir}/hunspell/sw_TZ.aff
ln -s %{_datadir}/hunspell/sw_TZ.aff %{buildroot}%{_datadir}/myspell/sw_TZ.aff
cp -P sw_TZ/sw_TZ.dic %{buildroot}%{_datadir}/hunspell/sw_TZ.dic
ln -s %{_datadir}/hunspell/sw_TZ.dic %{buildroot}%{_datadir}/myspell/sw_TZ.dic
mkdir -p %{buildroot}%{_docdir}/myspell-sw_TZ
cp -P sw_TZ/README_sw_TZ.txt %{buildroot}%{_docdir}/myspell-sw_TZ/README_sw_TZ.txt
cp -P sw_TZ/description.xml %{buildroot}%{_docdir}/myspell-sw_TZ/description.xml
cp -P sw_TZ/dictionaries.xcu %{buildroot}%{_docdir}/myspell-sw_TZ/dictionaries.xcu
ln -s %{_datadir}/hyphen/hyph_te_IN.dic %{buildroot}%{_datadir}/hyphen/hyph_te.dic
ln -s %{_datadir}/hyphen/hyph_te.dic %{buildroot}%{_datadir}/myspell/hyph_te.dic
cp -P te_IN/hyph_te_IN.dic %{buildroot}%{_datadir}/hyphen/hyph_te_IN.dic
ln -s %{_datadir}/hyphen/hyph_te_IN.dic %{buildroot}%{_datadir}/myspell/hyph_te_IN.dic
ln -s %{_datadir}/hunspell/te_IN.aff %{buildroot}%{_datadir}/hunspell/te.aff
ln -s %{_datadir}/hunspell/te.aff %{buildroot}%{_datadir}/myspell/te.aff
cp -P te_IN/te_IN.aff %{buildroot}%{_datadir}/hunspell/te_IN.aff
ln -s %{_datadir}/hunspell/te_IN.aff %{buildroot}%{_datadir}/myspell/te_IN.aff
ln -s %{_datadir}/hunspell/te_IN.dic %{buildroot}%{_datadir}/hunspell/te.dic
ln -s %{_datadir}/hunspell/te.dic %{buildroot}%{_datadir}/myspell/te.dic
cp -P te_IN/te_IN.dic %{buildroot}%{_datadir}/hunspell/te_IN.dic
ln -s %{_datadir}/hunspell/te_IN.dic %{buildroot}%{_datadir}/myspell/te_IN.dic
mkdir -p %{buildroot}%{_docdir}/myspell-te_IN
cp -P te_IN/README_hyph_te_IN.txt %{buildroot}%{_docdir}/myspell-te_IN/README_hyph_te_IN.txt
cp -P te_IN/README_te_IN.txt %{buildroot}%{_docdir}/myspell-te_IN/README_te_IN.txt
cp -P te_IN/description.xml %{buildroot}%{_docdir}/myspell-te_IN/description.xml
cp -P te_IN/dictionaries.xcu %{buildroot}%{_docdir}/myspell-te_IN/dictionaries.xcu
cp -P th_TH/th_TH.aff %{buildroot}%{_datadir}/hunspell/th_TH.aff
ln -s %{_datadir}/hunspell/th_TH.aff %{buildroot}%{_datadir}/myspell/th_TH.aff
cp -P th_TH/th_TH.dic %{buildroot}%{_datadir}/hunspell/th_TH.dic
ln -s %{_datadir}/hunspell/th_TH.dic %{buildroot}%{_datadir}/myspell/th_TH.dic
mkdir -p %{buildroot}%{_docdir}/myspell-th_TH
cp -P th_TH/README_th_TH.txt %{buildroot}%{_docdir}/myspell-th_TH/README_th_TH.txt
cp -P th_TH/description.xml %{buildroot}%{_docdir}/myspell-th_TH/description.xml
cp -P th_TH/dictionaries.xcu %{buildroot}%{_docdir}/myspell-th_TH/dictionaries.xcu
ln -s %{_datadir}/hunspell/tr_TR.aff %{buildroot}%{_datadir}/hunspell/tr.aff
ln -s %{_datadir}/hunspell/tr.aff %{buildroot}%{_datadir}/myspell/tr.aff
cp -P tr_TR/tr_TR.aff %{buildroot}%{_datadir}/hunspell/tr_TR.aff
ln -s %{_datadir}/hunspell/tr_TR.aff %{buildroot}%{_datadir}/myspell/tr_TR.aff
ln -s %{_datadir}/hunspell/tr_TR.dic %{buildroot}%{_datadir}/hunspell/tr.dic
ln -s %{_datadir}/hunspell/tr.dic %{buildroot}%{_datadir}/myspell/tr.dic
cp -P tr_TR/tr_TR.dic %{buildroot}%{_datadir}/hunspell/tr_TR.dic
ln -s %{_datadir}/hunspell/tr_TR.dic %{buildroot}%{_datadir}/myspell/tr_TR.dic
mkdir -p %{buildroot}%{_docdir}/myspell-tr_TR
cp -P tr_TR/LICENSE %{buildroot}%{_docdir}/myspell-tr_TR/LICENSE
cp -P tr_TR/README.txt %{buildroot}%{_docdir}/myspell-tr_TR/README.txt
cp -P tr_TR/description.xml %{buildroot}%{_docdir}/myspell-tr_TR/description.xml
cp -P tr_TR/dictionaries.xcu %{buildroot}%{_docdir}/myspell-tr_TR/dictionaries.xcu
cp -P uk_UA/hyph_uk_UA.dic %{buildroot}%{_datadir}/hyphen/hyph_uk_UA.dic
ln -s %{_datadir}/hyphen/hyph_uk_UA.dic %{buildroot}%{_datadir}/myspell/hyph_uk_UA.dic
ln -s %{_datadir}/mythes/th_uk_UA.dat %{buildroot}%{_datadir}/mythes/th_uk_UA_v2.dat
ln -s %{_datadir}/mythes/th_uk_UA_v2.dat %{buildroot}%{_datadir}/myspell/th_uk_UA_v2.dat
cp -P uk_UA/th_uk_UA.dat %{buildroot}%{_datadir}/mythes/th_uk_UA.dat
ln -s %{_datadir}/mythes/th_uk_UA.dat %{buildroot}%{_datadir}/myspell/th_uk_UA.dat
ln -s %{_datadir}/mythes/th_uk_UA.idx %{buildroot}%{_datadir}/mythes/th_uk_UA_v2.idx
ln -s %{_datadir}/mythes/th_uk_UA_v2.idx %{buildroot}%{_datadir}/myspell/th_uk_UA_v2.idx
cp -P uk_UA/th_uk_UA.idx %{buildroot}%{_datadir}/mythes/th_uk_UA.idx
ln -s %{_datadir}/mythes/th_uk_UA.idx %{buildroot}%{_datadir}/myspell/th_uk_UA.idx
cp -P uk_UA/uk_UA.aff %{buildroot}%{_datadir}/hunspell/uk_UA.aff
ln -s %{_datadir}/hunspell/uk_UA.aff %{buildroot}%{_datadir}/myspell/uk_UA.aff
cp -P uk_UA/uk_UA.dic %{buildroot}%{_datadir}/hunspell/uk_UA.dic
ln -s %{_datadir}/hunspell/uk_UA.dic %{buildroot}%{_datadir}/myspell/uk_UA.dic
mkdir -p %{buildroot}%{_docdir}/myspell-uk_UA
cp -P uk_UA/README_hyph_uk_UA.txt %{buildroot}%{_docdir}/myspell-uk_UA/README_hyph_uk_UA.txt
cp -P uk_UA/README_th_uk_UA.txt %{buildroot}%{_docdir}/myspell-uk_UA/README_th_uk_UA.txt
cp -P uk_UA/README_uk_UA.txt %{buildroot}%{_docdir}/myspell-uk_UA/README_uk_UA.txt
cp -P uk_UA/description.xml %{buildroot}%{_docdir}/myspell-uk_UA/description.xml
cp -P uk_UA/dictionaries.xcu %{buildroot}%{_docdir}/myspell-uk_UA/dictionaries.xcu
cp -P vi/vi_VN.aff %{buildroot}%{_datadir}/hunspell/vi_VN.aff
ln -s %{_datadir}/hunspell/vi_VN.aff %{buildroot}%{_datadir}/myspell/vi_VN.aff
cp -P vi/vi_VN.dic %{buildroot}%{_datadir}/hunspell/vi_VN.dic
ln -s %{_datadir}/hunspell/vi_VN.dic %{buildroot}%{_datadir}/myspell/vi_VN.dic
mkdir -p %{buildroot}%{_docdir}/myspell-vi
cp -P vi/LICENSES-en.txt %{buildroot}%{_docdir}/myspell-vi/LICENSES-en.txt
cp -P vi/LICENSES-vi.txt %{buildroot}%{_docdir}/myspell-vi/LICENSES-vi.txt
cp -P vi/description.xml %{buildroot}%{_docdir}/myspell-vi/description.xml
cp -P vi/dictionaries.xcu %{buildroot}%{_docdir}/myspell-vi/dictionaries.xcu
cp -P zu_ZA/hyph_zu_ZA.dic %{buildroot}%{_datadir}/hyphen/hyph_zu_ZA.dic
ln -s %{_datadir}/hyphen/hyph_zu_ZA.dic %{buildroot}%{_datadir}/myspell/hyph_zu_ZA.dic
mkdir -p %{buildroot}%{_docdir}/myspell-zu_ZA
cp -P zu_ZA/description.xml %{buildroot}%{_docdir}/myspell-zu_ZA/description.xml
cp -P zu_ZA/dictionaries.xcu %{buildroot}%{_docdir}/myspell-zu_ZA/dictionaries.xcu

%files
%dir %{_datadir}/hunspell
%dir %{_datadir}/hyphen
%dir %{_datadir}/mythes
%dir %{_datadir}/myspell
%dir %{_libdir}/libreoffice
%dir %{_libdir}/libreoffice/share
%dir %{_libdir}/libreoffice/share/extensions

%files -n myspell-af_NA
%{_datadir}/hunspell/af_NA.aff
%{_datadir}/myspell/af_NA.aff
%{_datadir}/hunspell/af_NA.dic
%{_datadir}/myspell/af_NA.dic
%{_datadir}/hyphen/hyph_af_NA.dic
%{_datadir}/myspell/hyph_af_NA.dic

%files -n myspell-af_ZA
%{_datadir}/hunspell/af_ZA.aff
%{_datadir}/myspell/af_ZA.aff
%{_datadir}/hunspell/af_ZA.dic
%{_datadir}/myspell/af_ZA.dic
%{_datadir}/hyphen/hyph_af_ZA.dic
%{_datadir}/myspell/hyph_af_ZA.dic
%dir %{_docdir}/myspell-af_ZA
%{_docdir}/myspell-af_ZA/README_af_ZA.txt
%{_docdir}/myspell-af_ZA/description.xml
%{_docdir}/myspell-af_ZA/dictionaries.xcu

%files -n myspell-an
%{_datadir}/hunspell/an.aff
%{_datadir}/myspell/an.aff
%{_datadir}/hunspell/an.dic
%{_datadir}/myspell/an.dic

%files -n myspell-an_ES
%{_datadir}/hunspell/an_ES.aff
%{_datadir}/myspell/an_ES.aff
%{_datadir}/hunspell/an_ES.dic
%{_datadir}/myspell/an_ES.dic
%dir %{_docdir}/myspell-an_ES
%{_docdir}/myspell-an_ES/LICENSES-en.txt
%{_docdir}/myspell-an_ES/description.xml
%{_docdir}/myspell-an_ES/dictionaries.xcu

%files -n myspell-ar_IQ
%{_datadir}/hunspell/ar_IQ.aff
%{_datadir}/myspell/ar_IQ.aff
%{_datadir}/hunspell/ar_IQ.dic
%{_datadir}/myspell/ar_IQ.dic
%{_datadir}/mythes/th_ar_IQ_v2.dat
%{_datadir}/myspell/th_ar_IQ_v2.dat
%{_datadir}/mythes/th_ar_IQ_v2.idx
%{_datadir}/myspell/th_ar_IQ_v2.idx

%files -n myspell-ar_QA
%{_datadir}/hunspell/ar_QA.aff
%{_datadir}/myspell/ar_QA.aff
%{_datadir}/hunspell/ar_QA.dic
%{_datadir}/myspell/ar_QA.dic
%{_datadir}/mythes/th_ar_QA_v2.dat
%{_datadir}/myspell/th_ar_QA_v2.dat
%{_datadir}/mythes/th_ar_QA_v2.idx
%{_datadir}/myspell/th_ar_QA_v2.idx

%files -n myspell-ar_EG
%{_datadir}/hunspell/ar_EG.aff
%{_datadir}/myspell/ar_EG.aff
%{_datadir}/hunspell/ar_EG.dic
%{_datadir}/myspell/ar_EG.dic
%{_datadir}/mythes/th_ar_EG_v2.dat
%{_datadir}/myspell/th_ar_EG_v2.dat
%{_datadir}/mythes/th_ar_EG_v2.idx
%{_datadir}/myspell/th_ar_EG_v2.idx

%files -n myspell-ar
%{_datadir}/hunspell/ar.aff
%{_datadir}/myspell/ar.aff
%{_datadir}/hunspell/ar.dic
%{_datadir}/myspell/ar.dic
%{_datadir}/mythes/th_ar.dat
%{_datadir}/myspell/th_ar.dat
%{_datadir}/mythes/th_ar.idx
%{_datadir}/myspell/th_ar.idx
%dir %{_docdir}/myspell-ar
%{_docdir}/myspell-ar/AUTHORS.txt
%{_docdir}/myspell-ar/COPYING.txt
%{_docdir}/myspell-ar/README_ar.txt
%{_docdir}/myspell-ar/description.xml
%{_docdir}/myspell-ar/dictionaries.xcu

%files -n myspell-ar_DZ
%{_datadir}/hunspell/ar_DZ.aff
%{_datadir}/myspell/ar_DZ.aff
%{_datadir}/hunspell/ar_DZ.dic
%{_datadir}/myspell/ar_DZ.dic
%{_datadir}/mythes/th_ar_DZ_v2.dat
%{_datadir}/myspell/th_ar_DZ_v2.dat
%{_datadir}/mythes/th_ar_DZ_v2.idx
%{_datadir}/myspell/th_ar_DZ_v2.idx

%files -n myspell-ar_BH
%{_datadir}/hunspell/ar_BH.aff
%{_datadir}/myspell/ar_BH.aff
%{_datadir}/hunspell/ar_BH.dic
%{_datadir}/myspell/ar_BH.dic
%{_datadir}/mythes/th_ar_BH_v2.dat
%{_datadir}/myspell/th_ar_BH_v2.dat
%{_datadir}/mythes/th_ar_BH_v2.idx
%{_datadir}/myspell/th_ar_BH_v2.idx

%files -n myspell-ar_YE
%{_datadir}/hunspell/ar_YE.aff
%{_datadir}/myspell/ar_YE.aff
%{_datadir}/hunspell/ar_YE.dic
%{_datadir}/myspell/ar_YE.dic
%{_datadir}/mythes/th_ar_YE_v2.dat
%{_datadir}/myspell/th_ar_YE_v2.dat
%{_datadir}/mythes/th_ar_YE_v2.idx
%{_datadir}/myspell/th_ar_YE_v2.idx

%files -n myspell-ar_JO
%{_datadir}/hunspell/ar_JO.aff
%{_datadir}/myspell/ar_JO.aff
%{_datadir}/hunspell/ar_JO.dic
%{_datadir}/myspell/ar_JO.dic
%{_datadir}/mythes/th_ar_JO_v2.dat
%{_datadir}/myspell/th_ar_JO_v2.dat
%{_datadir}/mythes/th_ar_JO_v2.idx
%{_datadir}/myspell/th_ar_JO_v2.idx

%files -n myspell-ar_MA
%{_datadir}/hunspell/ar_MA.aff
%{_datadir}/myspell/ar_MA.aff
%{_datadir}/hunspell/ar_MA.dic
%{_datadir}/myspell/ar_MA.dic
%{_datadir}/mythes/th_ar_MA_v2.dat
%{_datadir}/myspell/th_ar_MA_v2.dat
%{_datadir}/mythes/th_ar_MA_v2.idx
%{_datadir}/myspell/th_ar_MA_v2.idx

%files -n myspell-ar_KW
%{_datadir}/hunspell/ar_KW.aff
%{_datadir}/myspell/ar_KW.aff
%{_datadir}/hunspell/ar_KW.dic
%{_datadir}/myspell/ar_KW.dic
%{_datadir}/mythes/th_ar_KW_v2.dat
%{_datadir}/myspell/th_ar_KW_v2.dat
%{_datadir}/mythes/th_ar_KW_v2.idx
%{_datadir}/myspell/th_ar_KW_v2.idx

%files -n myspell-ar_SA
%{_datadir}/hunspell/ar_SA.aff
%{_datadir}/myspell/ar_SA.aff
%{_datadir}/hunspell/ar_SA.dic
%{_datadir}/myspell/ar_SA.dic
%{_datadir}/mythes/th_ar_SA_v2.dat
%{_datadir}/myspell/th_ar_SA_v2.dat
%{_datadir}/mythes/th_ar_SA_v2.idx
%{_datadir}/myspell/th_ar_SA_v2.idx

%files -n myspell-ar_SD
%{_datadir}/hunspell/ar_SD.aff
%{_datadir}/myspell/ar_SD.aff
%{_datadir}/hunspell/ar_SD.dic
%{_datadir}/myspell/ar_SD.dic
%{_datadir}/mythes/th_ar_SD_v2.dat
%{_datadir}/myspell/th_ar_SD_v2.dat
%{_datadir}/mythes/th_ar_SD_v2.idx
%{_datadir}/myspell/th_ar_SD_v2.idx

%files -n myspell-ar_LB
%{_datadir}/hunspell/ar_LB.aff
%{_datadir}/myspell/ar_LB.aff
%{_datadir}/hunspell/ar_LB.dic
%{_datadir}/myspell/ar_LB.dic
%{_datadir}/mythes/th_ar_LB_v2.dat
%{_datadir}/myspell/th_ar_LB_v2.dat
%{_datadir}/mythes/th_ar_LB_v2.idx
%{_datadir}/myspell/th_ar_LB_v2.idx

%files -n myspell-ar_LY
%{_datadir}/hunspell/ar_LY.aff
%{_datadir}/myspell/ar_LY.aff
%{_datadir}/hunspell/ar_LY.dic
%{_datadir}/myspell/ar_LY.dic
%{_datadir}/mythes/th_ar_LY_v2.dat
%{_datadir}/myspell/th_ar_LY_v2.dat
%{_datadir}/mythes/th_ar_LY_v2.idx
%{_datadir}/myspell/th_ar_LY_v2.idx

%files -n myspell-ar_OM
%{_datadir}/hunspell/ar_OM.aff
%{_datadir}/myspell/ar_OM.aff
%{_datadir}/hunspell/ar_OM.dic
%{_datadir}/myspell/ar_OM.dic
%{_datadir}/mythes/th_ar_OM_v2.dat
%{_datadir}/myspell/th_ar_OM_v2.dat
%{_datadir}/mythes/th_ar_OM_v2.idx
%{_datadir}/myspell/th_ar_OM_v2.idx

%files -n myspell-ar_SY
%{_datadir}/hunspell/ar_SY.aff
%{_datadir}/myspell/ar_SY.aff
%{_datadir}/hunspell/ar_SY.dic
%{_datadir}/myspell/ar_SY.dic
%{_datadir}/mythes/th_ar_SY_v2.dat
%{_datadir}/myspell/th_ar_SY_v2.dat
%{_datadir}/mythes/th_ar_SY_v2.idx
%{_datadir}/myspell/th_ar_SY_v2.idx

%files -n myspell-ar_AE
%{_datadir}/hunspell/ar_AE.aff
%{_datadir}/myspell/ar_AE.aff
%{_datadir}/hunspell/ar_AE.dic
%{_datadir}/myspell/ar_AE.dic
%{_datadir}/mythes/th_ar_AE_v2.dat
%{_datadir}/myspell/th_ar_AE_v2.dat
%{_datadir}/mythes/th_ar_AE_v2.idx
%{_datadir}/myspell/th_ar_AE_v2.idx

%files -n myspell-ar_TN
%{_datadir}/hunspell/ar_TN.aff
%{_datadir}/myspell/ar_TN.aff
%{_datadir}/hunspell/ar_TN.dic
%{_datadir}/myspell/ar_TN.dic
%{_datadir}/mythes/th_ar_TN_v2.dat
%{_datadir}/myspell/th_ar_TN_v2.dat
%{_datadir}/mythes/th_ar_TN_v2.idx
%{_datadir}/myspell/th_ar_TN_v2.idx

%files -n myspell-be_BY
%{_datadir}/hunspell/be_BY.aff
%{_datadir}/myspell/be_BY.aff
%{_datadir}/hunspell/be_BY.dic
%{_datadir}/myspell/be_BY.dic
%{_datadir}/hyphen/hyph_be_BY.dic
%{_datadir}/myspell/hyph_be_BY.dic
%dir %{_docdir}/myspell-be_BY
%{_docdir}/myspell-be_BY/README_be_BY.txt
%{_docdir}/myspell-be_BY/description.xml
%{_docdir}/myspell-be_BY/dictionaries.xcu

%files -n myspell-bg_BG
%{_datadir}/hunspell/bg_BG.aff
%{_datadir}/myspell/bg_BG.aff
%{_datadir}/hunspell/bg_BG.dic
%{_datadir}/myspell/bg_BG.dic
%{_datadir}/hyphen/hyph_bg_BG.dic
%{_datadir}/myspell/hyph_bg_BG.dic
%{_datadir}/mythes/th_bg_BG_v2.dat
%{_datadir}/myspell/th_bg_BG_v2.dat
%{_datadir}/mythes/th_bg_BG_v2.idx
%{_datadir}/myspell/th_bg_BG_v2.idx
%dir %{_docdir}/myspell-bg_BG
%{_docdir}/myspell-bg_BG/COPYING
%{_docdir}/myspell-bg_BG/README_hyph_bg_BG.txt
%{_docdir}/myspell-bg_BG/README_th_bg_BG_v2.txt
%{_docdir}/myspell-bg_BG/description.xml
%{_docdir}/myspell-bg_BG/dictionaries.xcu

%files -n myspell-bn_BD
%{_datadir}/hunspell/bn_BD.aff
%{_datadir}/myspell/bn_BD.aff
%{_datadir}/hunspell/bn_BD.dic
%{_datadir}/myspell/bn_BD.dic
%dir %{_docdir}/myspell-bn_BD
%{_docdir}/myspell-bn_BD/COPYING
%{_docdir}/myspell-bn_BD/description.xml
%{_docdir}/myspell-bn_BD/dictionaries.xcu

%files -n myspell-bn_IN
%{_datadir}/hunspell/bn_IN.aff
%{_datadir}/myspell/bn_IN.aff
%{_datadir}/hunspell/bn_IN.dic
%{_datadir}/myspell/bn_IN.dic

%files -n myspell-bo_IN
%{_datadir}/hunspell/bo_IN.aff
%{_datadir}/myspell/bo_IN.aff
%{_datadir}/hunspell/bo_IN.dic
%{_datadir}/myspell/bo_IN.dic

%files -n myspell-bo_CN
%{_datadir}/hunspell/bo_CN.aff
%{_datadir}/myspell/bo_CN.aff
%{_datadir}/hunspell/bo_CN.dic
%{_datadir}/myspell/bo_CN.dic

%files -n myspell-bo
%{_datadir}/hunspell/bo.aff
%{_datadir}/myspell/bo.aff
%{_datadir}/hunspell/bo.dic
%{_datadir}/myspell/bo.dic
%dir %{_docdir}/myspell-bo
%{_docdir}/myspell-bo/description.xml
%{_docdir}/myspell-bo/dictionaries.xcu

%files -n myspell-br_FR
%{_datadir}/hunspell/br_FR.aff
%{_datadir}/myspell/br_FR.aff
%{_datadir}/hunspell/br_FR.dic
%{_datadir}/myspell/br_FR.dic
%dir %{_docdir}/myspell-br_FR
%{_docdir}/myspell-br_FR/LICENSES-en.txt
%{_docdir}/myspell-br_FR/description.xml
%{_docdir}/myspell-br_FR/dictionaries.xcu

%files -n myspell-bs
%{_datadir}/hunspell/bs.aff
%{_datadir}/myspell/bs.aff
%{_datadir}/hunspell/bs.dic
%{_datadir}/myspell/bs.dic

%files -n myspell-bs_BA
%{_datadir}/hunspell/bs_BA.aff
%{_datadir}/myspell/bs_BA.aff
%{_datadir}/hunspell/bs_BA.dic
%{_datadir}/myspell/bs_BA.dic
%dir %{_docdir}/myspell-bs_BA
%{_docdir}/myspell-bs_BA/README.txt
%{_docdir}/myspell-bs_BA/description.xml
%{_docdir}/myspell-bs_BA/dictionaries.xcu

%files -n myspell-ca_FR
%{_datadir}/hunspell/ca_FR.aff
%{_datadir}/myspell/ca_FR.aff
%{_datadir}/hunspell/ca_FR.dic
%{_datadir}/myspell/ca_FR.dic
%{_datadir}/hyphen/hyph_ca_FR.dic
%{_datadir}/myspell/hyph_ca_FR.dic
%{_datadir}/mythes/th_ca_FR_v2.dat
%{_datadir}/myspell/th_ca_FR_v2.dat
%{_datadir}/mythes/th_ca_FR_v2.idx
%{_datadir}/myspell/th_ca_FR_v2.idx

%files -n myspell-ca_AD
%{_datadir}/hunspell/ca_AD.aff
%{_datadir}/myspell/ca_AD.aff
%{_datadir}/hunspell/ca_AD.dic
%{_datadir}/myspell/ca_AD.dic
%{_datadir}/hyphen/hyph_ca_AD.dic
%{_datadir}/myspell/hyph_ca_AD.dic
%{_datadir}/mythes/th_ca_AD_v2.dat
%{_datadir}/myspell/th_ca_AD_v2.dat
%{_datadir}/mythes/th_ca_AD_v2.idx
%{_datadir}/myspell/th_ca_AD_v2.idx

%files -n myspell-ca_IT
%{_datadir}/hunspell/ca_IT.aff
%{_datadir}/myspell/ca_IT.aff
%{_datadir}/hunspell/ca_IT.dic
%{_datadir}/myspell/ca_IT.dic
%{_datadir}/hyphen/hyph_ca_IT.dic
%{_datadir}/myspell/hyph_ca_IT.dic
%{_datadir}/mythes/th_ca_IT_v2.dat
%{_datadir}/myspell/th_ca_IT_v2.dat
%{_datadir}/mythes/th_ca_IT_v2.idx
%{_datadir}/myspell/th_ca_IT_v2.idx

%files -n myspell-ca_ES_valencia
%{_datadir}/hunspell/ca_ES_valencia.aff
%{_datadir}/myspell/ca_ES_valencia.aff
%{_datadir}/hunspell/ca_ES_valencia.dic
%{_datadir}/myspell/ca_ES_valencia.dic
%{_datadir}/hyphen/hyph_ca_ES_valencia.dic
%{_datadir}/myspell/hyph_ca_ES_valencia.dic
%{_datadir}/mythes/th_ca_ES_valencia_v2.dat
%{_datadir}/myspell/th_ca_ES_valencia_v2.dat
%{_datadir}/mythes/th_ca_ES_valencia_v2.idx
%{_datadir}/myspell/th_ca_ES_valencia_v2.idx

%files -n myspell-ca
%{_datadir}/hunspell/ca.aff
%{_datadir}/myspell/ca.aff
%{_datadir}/hunspell/ca.dic
%{_datadir}/myspell/ca.dic
%{_datadir}/hyphen/hyph_ca.dic
%{_datadir}/myspell/hyph_ca.dic
%{_datadir}/mythes/th_ca_ES_v3.dat
%{_datadir}/myspell/th_ca_ES_v3.dat
%{_datadir}/mythes/th_ca_ES_v3.idx
%{_datadir}/myspell/th_ca_ES_v3.idx
%dir %{_docdir}/myspell-ca
%{_docdir}/myspell-ca/LICENSES-en.txt
%{_docdir}/myspell-ca/LLICENCIES-ca.txt
%{_docdir}/myspell-ca/README_ca.txt
%{_docdir}/myspell-ca/README_hyph_ca.txt
%{_docdir}/myspell-ca/README_thes_ca.txt
%{_docdir}/myspell-ca/description.xml
%{_docdir}/myspell-ca/dictionaries.xcu
%{_docdir}/myspell-ca/package-description.txt

%files -n myspell-ca_ES
%{_datadir}/hunspell/ca_ES.aff
%{_datadir}/myspell/ca_ES.aff
%{_datadir}/hunspell/ca_ES.dic
%{_datadir}/myspell/ca_ES.dic
%{_datadir}/hyphen/hyph_ca_ES.dic
%{_datadir}/myspell/hyph_ca_ES.dic
%{_datadir}/mythes/th_ca_ES_v2.dat
%{_datadir}/myspell/th_ca_ES_v2.dat
%{_datadir}/mythes/th_ca_ES_v2.idx
%{_datadir}/myspell/th_ca_ES_v2.idx

%files -n myspell-cs_CZ
%{_datadir}/hunspell/cs_CZ.aff
%{_datadir}/myspell/cs_CZ.aff
%{_datadir}/hunspell/cs_CZ.dic
%{_datadir}/myspell/cs_CZ.dic
%{_datadir}/hyphen/hyph_cs_CZ.dic
%{_datadir}/myspell/hyph_cs_CZ.dic
%{_datadir}/mythes/th_cs_CZ_v2.dat
%{_datadir}/myspell/th_cs_CZ_v2.dat
%{_datadir}/mythes/thes_cs_CZ.dat
%{_datadir}/myspell/thes_cs_CZ.dat
%{_datadir}/mythes/th_cs_CZ_v2.idx
%{_datadir}/myspell/th_cs_CZ_v2.idx
%{_datadir}/mythes/thes_cs_CZ.idx
%{_datadir}/myspell/thes_cs_CZ.idx
%dir %{_docdir}/myspell-cs_CZ
%{_docdir}/myspell-cs_CZ/README_cs.txt
%{_docdir}/myspell-cs_CZ/README_en.txt
%{_docdir}/myspell-cs_CZ/description.xml
%{_docdir}/myspell-cs_CZ/dictionaries.xcu

%files -n myspell-da_DK
%{_datadir}/hunspell/da_DK.aff
%{_datadir}/myspell/da_DK.aff
%{_datadir}/hunspell/da_DK.dic
%{_datadir}/myspell/da_DK.dic
%{_datadir}/hyphen/hyph_da_DK.dic
%{_datadir}/myspell/hyph_da_DK.dic
%{_datadir}/mythes/th_da_DK_v2.dat
%{_datadir}/myspell/th_da_DK_v2.dat
%{_datadir}/mythes/th_da_DK.dat
%{_datadir}/myspell/th_da_DK.dat
%{_datadir}/mythes/th_da_DK_v2.idx
%{_datadir}/myspell/th_da_DK_v2.idx
%{_datadir}/mythes/th_da_DK.idx
%{_datadir}/myspell/th_da_DK.idx
%dir %{_docdir}/myspell-da_DK
%{_docdir}/myspell-da_DK/HYPH_da_DK_README.txt
%{_docdir}/myspell-da_DK/README_da_DK.txt
%{_docdir}/myspell-da_DK/README_th_da_DK.txt
%{_docdir}/myspell-da_DK/README_th_en-US.txt
%{_docdir}/myspell-da_DK/Trold_42x42.png
%{_docdir}/myspell-da_DK/desc_da_DK.txt
%{_docdir}/myspell-da_DK/desc_en_US.txt
%{_docdir}/myspell-da_DK/description.xml
%{_docdir}/myspell-da_DK/dictionaries.xcu
%{_docdir}/myspell-da_DK/th_desc_da_DK.txt
%{_docdir}/myspell-da_DK/th_desc_en_US.txt

%files -n myspell-de_CH
%{_datadir}/hunspell/de_CH.aff
%{_datadir}/myspell/de_CH.aff
%{_datadir}/hunspell/de_CH.dic
%{_datadir}/myspell/de_CH.dic
%{_datadir}/hyphen/hyph_de_CH.dic
%{_datadir}/myspell/hyph_de_CH.dic
%{_datadir}/mythes/th_de_CH_v2.dat
%{_datadir}/myspell/th_de_CH_v2.dat
%{_datadir}/mythes/th_de_CH_v2.idx
%{_datadir}/myspell/th_de_CH_v2.idx

%files -n myspell-de
%dir %{_docdir}/myspell-de
%{_docdir}/myspell-de/COPYING_GPLv2
%{_docdir}/myspell-de/COPYING_GPLv3
%{_docdir}/myspell-de/COPYING_LGPL_v2.0.txt
%{_docdir}/myspell-de/COPYING_LGPL_v2.1.txt
%{_docdir}/myspell-de/COPYING_OASIS.txt
%{_docdir}/myspell-de/README_de_DE_frami.txt
%{_docdir}/myspell-de/README_extension_owner.txt
%{_docdir}/myspell-de/README_hyph_de.txt
%{_docdir}/myspell-de/README_thesaurus.txt
%{_docdir}/myspell-de/description.xml
%{_docdir}/myspell-de/dictionaries.xcu

%files -n myspell-de_DE
%{_datadir}/hunspell/de_DE.aff
%{_datadir}/myspell/de_DE.aff
%{_datadir}/hunspell/de_DE.dic
%{_datadir}/myspell/de_DE.dic
%{_datadir}/hyphen/hyph_de_DE.dic
%{_datadir}/myspell/hyph_de_DE.dic
%{_datadir}/mythes/th_de_DE_v2.dat
%{_datadir}/myspell/th_de_DE_v2.dat
%{_datadir}/mythes/th_de_DE_v2.idx
%{_datadir}/myspell/th_de_DE_v2.idx

%files -n myspell-de_AT
%{_datadir}/hunspell/de_AT.aff
%{_datadir}/myspell/de_AT.aff
%{_datadir}/hunspell/de_AT.dic
%{_datadir}/myspell/de_AT.dic
%{_datadir}/hyphen/hyph_de_AT.dic
%{_datadir}/myspell/hyph_de_AT.dic
%{_datadir}/mythes/th_de_AT_v2.dat
%{_datadir}/myspell/th_de_AT_v2.dat
%{_datadir}/mythes/th_de_AT_v2.idx
%{_datadir}/myspell/th_de_AT_v2.idx

%files -n myspell-el_GR
%{_datadir}/hunspell/el_GR.aff
%{_datadir}/myspell/el_GR.aff
%{_datadir}/hunspell/el_GR.dic
%{_datadir}/myspell/el_GR.dic
%{_datadir}/hyphen/hyph_el_GR.dic
%{_datadir}/myspell/hyph_el_GR.dic
%dir %{_docdir}/myspell-el_GR
%{_docdir}/myspell-el_GR/README_el_GR.txt
%{_docdir}/myspell-el_GR/README_hyph_el_GR.txt
%{_docdir}/myspell-el_GR/description.xml
%{_docdir}/myspell-el_GR/dictionaries.xcu

%files -n myspell-en_AU
%{_datadir}/hunspell/en_AU.aff
%{_datadir}/myspell/en_AU.aff
%{_datadir}/hunspell/en_AU.dic
%{_datadir}/myspell/en_AU.dic
%{_datadir}/hyphen/hyph_en_AU.dic
%{_datadir}/myspell/hyph_en_AU.dic
%{_datadir}/mythes/th_en_AU_v2.dat
%{_datadir}/myspell/th_en_AU_v2.dat
%{_datadir}/mythes/th_en_AU_v2.idx
%{_datadir}/myspell/th_en_AU_v2.idx

%files -n myspell-en_BZ
%{_datadir}/hunspell/en_BZ.aff
%{_datadir}/myspell/en_BZ.aff
%{_datadir}/hunspell/en_BZ.dic
%{_datadir}/myspell/en_BZ.dic
%{_datadir}/hyphen/hyph_en_BZ.dic
%{_datadir}/myspell/hyph_en_BZ.dic
%{_datadir}/mythes/th_en_BZ_v2.dat
%{_datadir}/myspell/th_en_BZ_v2.dat
%{_datadir}/mythes/th_en_BZ_v2.idx
%{_datadir}/myspell/th_en_BZ_v2.idx

%files -n myspell-en_JM
%{_datadir}/hunspell/en_JM.aff
%{_datadir}/myspell/en_JM.aff
%{_datadir}/hunspell/en_JM.dic
%{_datadir}/myspell/en_JM.dic
%{_datadir}/hyphen/hyph_en_JM.dic
%{_datadir}/myspell/hyph_en_JM.dic
%{_datadir}/mythes/th_en_JM_v2.dat
%{_datadir}/myspell/th_en_JM_v2.dat
%{_datadir}/mythes/th_en_JM_v2.idx
%{_datadir}/myspell/th_en_JM_v2.idx

%files -n myspell-en_CA
%{_datadir}/hunspell/en_CA.aff
%{_datadir}/myspell/en_CA.aff
%{_datadir}/hunspell/en_CA.dic
%{_datadir}/myspell/en_CA.dic
%{_datadir}/hyphen/hyph_en_CA.dic
%{_datadir}/myspell/hyph_en_CA.dic
%{_datadir}/mythes/th_en_CA_v2.dat
%{_datadir}/myspell/th_en_CA_v2.dat
%{_datadir}/mythes/th_en_CA_v2.idx
%{_datadir}/myspell/th_en_CA_v2.idx

%files -n myspell-en_BS
%{_datadir}/hunspell/en_BS.aff
%{_datadir}/myspell/en_BS.aff
%{_datadir}/hunspell/en_BS.dic
%{_datadir}/myspell/en_BS.dic
%{_datadir}/hyphen/hyph_en_BS.dic
%{_datadir}/myspell/hyph_en_BS.dic
%{_datadir}/mythes/th_en_BS_v2.dat
%{_datadir}/myspell/th_en_BS_v2.dat
%{_datadir}/mythes/th_en_BS_v2.idx
%{_datadir}/myspell/th_en_BS_v2.idx

%files -n myspell-en_MW
%{_datadir}/hunspell/en_MW.aff
%{_datadir}/myspell/en_MW.aff
%{_datadir}/hunspell/en_MW.dic
%{_datadir}/myspell/en_MW.dic
%{_datadir}/hyphen/hyph_en_MW.dic
%{_datadir}/myspell/hyph_en_MW.dic
%{_datadir}/mythes/th_en_MW_v2.dat
%{_datadir}/myspell/th_en_MW_v2.dat
%{_datadir}/mythes/th_en_MW_v2.idx
%{_datadir}/myspell/th_en_MW_v2.idx

%files -n myspell-en_ZW
%{_datadir}/hunspell/en_ZW.aff
%{_datadir}/myspell/en_ZW.aff
%{_datadir}/hunspell/en_ZW.dic
%{_datadir}/myspell/en_ZW.dic
%{_datadir}/hyphen/hyph_en_ZW.dic
%{_datadir}/myspell/hyph_en_ZW.dic
%{_datadir}/mythes/th_en_ZW_v2.dat
%{_datadir}/myspell/th_en_ZW_v2.dat
%{_datadir}/mythes/th_en_ZW_v2.idx
%{_datadir}/myspell/th_en_ZW_v2.idx

%files -n myspell-en_NZ
%{_datadir}/hunspell/en_NZ.aff
%{_datadir}/myspell/en_NZ.aff
%{_datadir}/hunspell/en_NZ.dic
%{_datadir}/myspell/en_NZ.dic
%{_datadir}/hyphen/hyph_en_NZ.dic
%{_datadir}/myspell/hyph_en_NZ.dic
%{_datadir}/mythes/th_en_NZ_v2.dat
%{_datadir}/myspell/th_en_NZ_v2.dat
%{_datadir}/mythes/th_en_NZ_v2.idx
%{_datadir}/myspell/th_en_NZ_v2.idx

%files -n myspell-en_PH
%{_datadir}/hunspell/en_PH.aff
%{_datadir}/myspell/en_PH.aff
%{_datadir}/hunspell/en_PH.dic
%{_datadir}/myspell/en_PH.dic
%{_datadir}/hyphen/hyph_en_PH.dic
%{_datadir}/myspell/hyph_en_PH.dic
%{_datadir}/mythes/th_en_PH_v2.dat
%{_datadir}/myspell/th_en_PH_v2.dat
%{_datadir}/mythes/th_en_PH_v2.idx
%{_datadir}/myspell/th_en_PH_v2.idx

%files -n myspell-en_ZA
%{_datadir}/hunspell/en_ZA.aff
%{_datadir}/myspell/en_ZA.aff
%{_datadir}/hunspell/en_ZA.dic
%{_datadir}/myspell/en_ZA.dic
%{_datadir}/hyphen/hyph_en_ZA.dic
%{_datadir}/myspell/hyph_en_ZA.dic
%{_datadir}/mythes/th_en_ZA_v2.dat
%{_datadir}/myspell/th_en_ZA_v2.dat
%{_datadir}/mythes/th_en_ZA_v2.idx
%{_datadir}/myspell/th_en_ZA_v2.idx

%files -n myspell-en_GH
%{_datadir}/hunspell/en_GH.aff
%{_datadir}/myspell/en_GH.aff
%{_datadir}/hunspell/en_GH.dic
%{_datadir}/myspell/en_GH.dic
%{_datadir}/hyphen/hyph_en_GH.dic
%{_datadir}/myspell/hyph_en_GH.dic
%{_datadir}/mythes/th_en_GH_v2.dat
%{_datadir}/myspell/th_en_GH_v2.dat
%{_datadir}/mythes/th_en_GH_v2.idx
%{_datadir}/myspell/th_en_GH_v2.idx

%files -n myspell-en_NA
%{_datadir}/hunspell/en_NA.aff
%{_datadir}/myspell/en_NA.aff
%{_datadir}/hunspell/en_NA.dic
%{_datadir}/myspell/en_NA.dic
%{_datadir}/hyphen/hyph_en_NA.dic
%{_datadir}/myspell/hyph_en_NA.dic
%{_datadir}/mythes/th_en_NA_v2.dat
%{_datadir}/myspell/th_en_NA_v2.dat
%{_datadir}/mythes/th_en_NA_v2.idx
%{_datadir}/myspell/th_en_NA_v2.idx

%files -n myspell-en_GB
%{_datadir}/hunspell/en_GB.aff
%{_datadir}/myspell/en_GB.aff
%{_datadir}/hunspell/en_GB.dic
%{_datadir}/myspell/en_GB.dic
%{_datadir}/hyphen/hyph_en_GB.dic
%{_datadir}/myspell/hyph_en_GB.dic
%{_datadir}/mythes/th_en_GB_v2.dat
%{_datadir}/myspell/th_en_GB_v2.dat
%{_datadir}/mythes/th_en_GB_v2.idx
%{_datadir}/myspell/th_en_GB_v2.idx

%files -n myspell-en
%dir %{_docdir}/myspell-en
%{_docdir}/myspell-en/English.png
%{_docdir}/myspell-en/Linguistic.xcu
%{_docdir}/myspell-en/README.txt
%{_docdir}/myspell-en/README_en_AU.txt
%{_docdir}/myspell-en/README_en_CA.txt
%{_docdir}/myspell-en/README_en_GB.txt
%{_docdir}/myspell-en/README_en_GB_thes.txt
%{_docdir}/myspell-en/README_en_US.txt
%{_docdir}/myspell-en/README_en_ZA.txt
%{_docdir}/myspell-en/README_hyph_en_GB.txt
%{_docdir}/myspell-en/README_hyph_en_US.txt
%{_docdir}/myspell-en/README_lightproof_en.txt
%{_docdir}/myspell-en/WordNet_license.txt
%{_docdir}/myspell-en/affDescription.txt
%{_docdir}/myspell-en/changelog.txt
%{_docdir}/myspell-en/description.xml
%{_docdir}/myspell-en/dictionaries.xcu
%{_docdir}/myspell-en/license.txt
%{_docdir}/myspell-en/package-description.txt

%files -n myspell-en_IN
%{_datadir}/hunspell/en_IN.aff
%{_datadir}/myspell/en_IN.aff
%{_datadir}/hunspell/en_IN.dic
%{_datadir}/myspell/en_IN.dic
%{_datadir}/hyphen/hyph_en_IN.dic
%{_datadir}/myspell/hyph_en_IN.dic
%{_datadir}/mythes/th_en_IN_v2.dat
%{_datadir}/myspell/th_en_IN_v2.dat
%{_datadir}/mythes/th_en_IN_v2.idx
%{_datadir}/myspell/th_en_IN_v2.idx

%files -n myspell-en_IE
%{_datadir}/hunspell/en_IE.aff
%{_datadir}/myspell/en_IE.aff
%{_datadir}/hunspell/en_IE.dic
%{_datadir}/myspell/en_IE.dic
%{_datadir}/hyphen/hyph_en_IE.dic
%{_datadir}/myspell/hyph_en_IE.dic
%{_datadir}/mythes/th_en_IE_v2.dat
%{_datadir}/myspell/th_en_IE_v2.dat
%{_datadir}/mythes/th_en_IE_v2.idx
%{_datadir}/myspell/th_en_IE_v2.idx

%files -n myspell-en_TT
%{_datadir}/hunspell/en_TT.aff
%{_datadir}/myspell/en_TT.aff
%{_datadir}/hunspell/en_TT.dic
%{_datadir}/myspell/en_TT.dic
%{_datadir}/hyphen/hyph_en_TT.dic
%{_datadir}/myspell/hyph_en_TT.dic
%{_datadir}/mythes/th_en_TT_v2.dat
%{_datadir}/myspell/th_en_TT_v2.dat
%{_datadir}/mythes/th_en_TT_v2.idx
%{_datadir}/myspell/th_en_TT_v2.idx

%files -n myspell-en_US
%{_datadir}/hunspell/en_US.aff
%{_datadir}/myspell/en_US.aff
%{_datadir}/hunspell/en_US.dic
%{_datadir}/myspell/en_US.dic
%{_datadir}/hyphen/hyph_en_US.dic
%{_datadir}/myspell/hyph_en_US.dic
%{_datadir}/mythes/th_en_US_v2.dat
%{_datadir}/myspell/th_en_US_v2.dat
%{_datadir}/mythes/th_en_US_v2.idx
%{_datadir}/myspell/th_en_US_v2.idx

%files -n myspell-lightproof-en
%dir %{_libdir}/libreoffice/share/extensions/lightproof-en
%{_libdir}/libreoffice/share/extensions/lightproof-en/Lightproof.components
%{_libdir}/libreoffice/share/extensions/lightproof-en/Lightproof.py
%{_libdir}/libreoffice/share/extensions/lightproof-en/Linguistic.xcu
%{_libdir}/libreoffice/share/extensions/lightproof-en/META-INF
%{_libdir}/libreoffice/share/extensions/lightproof-en/description.xml
%{_libdir}/libreoffice/share/extensions/lightproof-en/dialog
%{_libdir}/libreoffice/share/extensions/lightproof-en/pythonpath

%files -n myspell-es_CR
%{_datadir}/hunspell/es_CR.aff
%{_datadir}/myspell/es_CR.aff
%{_datadir}/hunspell/es_CR.dic
%{_datadir}/myspell/es_CR.dic
%{_datadir}/hyphen/hyph_es_CR.dic
%{_datadir}/myspell/hyph_es_CR.dic
%{_datadir}/mythes/th_es_CR_v2.dat
%{_datadir}/myspell/th_es_CR_v2.dat
%{_datadir}/mythes/th_es_CR_v2.idx
%{_datadir}/myspell/th_es_CR_v2.idx

%files -n myspell-es_CU
%{_datadir}/hunspell/es_CU.aff
%{_datadir}/myspell/es_CU.aff
%{_datadir}/hunspell/es_CU.dic
%{_datadir}/myspell/es_CU.dic
%{_datadir}/hyphen/hyph_es_CU.dic
%{_datadir}/myspell/hyph_es_CU.dic
%{_datadir}/mythes/th_es_CU_v2.dat
%{_datadir}/myspell/th_es_CU_v2.dat
%{_datadir}/mythes/th_es_CU_v2.idx
%{_datadir}/myspell/th_es_CU_v2.idx

%files -n myspell-es_MX
%{_datadir}/hunspell/es_MX.aff
%{_datadir}/myspell/es_MX.aff
%{_datadir}/hunspell/es_MX.dic
%{_datadir}/myspell/es_MX.dic
%{_datadir}/hyphen/hyph_es_MX.dic
%{_datadir}/myspell/hyph_es_MX.dic
%{_datadir}/mythes/th_es_MX_v2.dat
%{_datadir}/myspell/th_es_MX_v2.dat
%{_datadir}/mythes/th_es_MX_v2.idx
%{_datadir}/myspell/th_es_MX_v2.idx

%files -n myspell-es_PA
%{_datadir}/hunspell/es_PA.aff
%{_datadir}/myspell/es_PA.aff
%{_datadir}/hunspell/es_PA.dic
%{_datadir}/myspell/es_PA.dic
%{_datadir}/hyphen/hyph_es_PA.dic
%{_datadir}/myspell/hyph_es_PA.dic
%{_datadir}/mythes/th_es_PA_v2.dat
%{_datadir}/myspell/th_es_PA_v2.dat
%{_datadir}/mythes/th_es_PA_v2.idx
%{_datadir}/myspell/th_es_PA_v2.idx

%files -n myspell-es_PE
%{_datadir}/hunspell/es_PE.aff
%{_datadir}/myspell/es_PE.aff
%{_datadir}/hunspell/es_PE.dic
%{_datadir}/myspell/es_PE.dic
%{_datadir}/hyphen/hyph_es_PE.dic
%{_datadir}/myspell/hyph_es_PE.dic
%{_datadir}/mythes/th_es_PE_v2.dat
%{_datadir}/myspell/th_es_PE_v2.dat
%{_datadir}/mythes/th_es_PE_v2.idx
%{_datadir}/myspell/th_es_PE_v2.idx

%files -n myspell-es_PY
%{_datadir}/hunspell/es_PY.aff
%{_datadir}/myspell/es_PY.aff
%{_datadir}/hunspell/es_PY.dic
%{_datadir}/myspell/es_PY.dic
%{_datadir}/hyphen/hyph_es_PY.dic
%{_datadir}/myspell/hyph_es_PY.dic
%{_datadir}/mythes/th_es_PY_v2.dat
%{_datadir}/myspell/th_es_PY_v2.dat
%{_datadir}/mythes/th_es_PY_v2.idx
%{_datadir}/myspell/th_es_PY_v2.idx

%files -n myspell-es_PR
%{_datadir}/hunspell/es_PR.aff
%{_datadir}/myspell/es_PR.aff
%{_datadir}/hunspell/es_PR.dic
%{_datadir}/myspell/es_PR.dic
%{_datadir}/hyphen/hyph_es_PR.dic
%{_datadir}/myspell/hyph_es_PR.dic
%{_datadir}/mythes/th_es_PR_v2.dat
%{_datadir}/myspell/th_es_PR_v2.dat
%{_datadir}/mythes/th_es_PR_v2.idx
%{_datadir}/myspell/th_es_PR_v2.idx

%files -n myspell-es_CL
%{_datadir}/hunspell/es_CL.aff
%{_datadir}/myspell/es_CL.aff
%{_datadir}/hunspell/es_CL.dic
%{_datadir}/myspell/es_CL.dic
%{_datadir}/hyphen/hyph_es_CL.dic
%{_datadir}/myspell/hyph_es_CL.dic
%{_datadir}/mythes/th_es_CL_v2.dat
%{_datadir}/myspell/th_es_CL_v2.dat
%{_datadir}/mythes/th_es_CL_v2.idx
%{_datadir}/myspell/th_es_CL_v2.idx

%files -n myspell-es_CO
%{_datadir}/hunspell/es_CO.aff
%{_datadir}/myspell/es_CO.aff
%{_datadir}/hunspell/es_CO.dic
%{_datadir}/myspell/es_CO.dic
%{_datadir}/hyphen/hyph_es_CO.dic
%{_datadir}/myspell/hyph_es_CO.dic
%{_datadir}/mythes/th_es_CO_v2.dat
%{_datadir}/myspell/th_es_CO_v2.dat
%{_datadir}/mythes/th_es_CO_v2.idx
%{_datadir}/myspell/th_es_CO_v2.idx

%files -n myspell-es_ES
%{_datadir}/hunspell/es_ES.aff
%{_datadir}/myspell/es_ES.aff
%{_datadir}/hunspell/es_ES.dic
%{_datadir}/myspell/es_ES.dic
%{_datadir}/hyphen/hyph_es_ES.dic
%{_datadir}/myspell/hyph_es_ES.dic
%{_datadir}/mythes/th_es_ES_v2.dat
%{_datadir}/myspell/th_es_ES_v2.dat
%{_datadir}/mythes/th_es_ES_v2.idx
%{_datadir}/myspell/th_es_ES_v2.idx

%files -n myspell-es_DO
%{_datadir}/hunspell/es_DO.aff
%{_datadir}/myspell/es_DO.aff
%{_datadir}/hunspell/es_DO.dic
%{_datadir}/myspell/es_DO.dic
%{_datadir}/hyphen/hyph_es_DO.dic
%{_datadir}/myspell/hyph_es_DO.dic
%{_datadir}/mythes/th_es_DO_v2.dat
%{_datadir}/myspell/th_es_DO_v2.dat
%{_datadir}/mythes/th_es_DO_v2.idx
%{_datadir}/myspell/th_es_DO_v2.idx

%files -n myspell-es_EC
%{_datadir}/hunspell/es_EC.aff
%{_datadir}/myspell/es_EC.aff
%{_datadir}/hunspell/es_EC.dic
%{_datadir}/myspell/es_EC.dic
%{_datadir}/hyphen/hyph_es_EC.dic
%{_datadir}/myspell/hyph_es_EC.dic
%{_datadir}/mythes/th_es_EC_v2.dat
%{_datadir}/myspell/th_es_EC_v2.dat
%{_datadir}/mythes/th_es_EC_v2.idx
%{_datadir}/myspell/th_es_EC_v2.idx

%files -n myspell-es_NI
%{_datadir}/hunspell/es_NI.aff
%{_datadir}/myspell/es_NI.aff
%{_datadir}/hunspell/es_NI.dic
%{_datadir}/myspell/es_NI.dic
%{_datadir}/hyphen/hyph_es_NI.dic
%{_datadir}/myspell/hyph_es_NI.dic
%{_datadir}/mythes/th_es_NI_v2.dat
%{_datadir}/myspell/th_es_NI_v2.dat
%{_datadir}/mythes/th_es_NI_v2.idx
%{_datadir}/myspell/th_es_NI_v2.idx

%files -n myspell-es_GT
%{_datadir}/hunspell/es_GT.aff
%{_datadir}/myspell/es_GT.aff
%{_datadir}/hunspell/es_GT.dic
%{_datadir}/myspell/es_GT.dic
%{_datadir}/hyphen/hyph_es_GT.dic
%{_datadir}/myspell/hyph_es_GT.dic
%{_datadir}/mythes/th_es_GT_v2.dat
%{_datadir}/myspell/th_es_GT_v2.dat
%{_datadir}/mythes/th_es_GT_v2.idx
%{_datadir}/myspell/th_es_GT_v2.idx

%files -n myspell-es_HN
%{_datadir}/hunspell/es_HN.aff
%{_datadir}/myspell/es_HN.aff
%{_datadir}/hunspell/es_HN.dic
%{_datadir}/myspell/es_HN.dic
%{_datadir}/hyphen/hyph_es_HN.dic
%{_datadir}/myspell/hyph_es_HN.dic
%{_datadir}/mythes/th_es_HN_v2.dat
%{_datadir}/myspell/th_es_HN_v2.dat
%{_datadir}/mythes/th_es_HN_v2.idx
%{_datadir}/myspell/th_es_HN_v2.idx

%files -n myspell-es_SV
%{_datadir}/hunspell/es_SV.aff
%{_datadir}/myspell/es_SV.aff
%{_datadir}/hunspell/es_SV.dic
%{_datadir}/myspell/es_SV.dic
%{_datadir}/hyphen/hyph_es_SV.dic
%{_datadir}/myspell/hyph_es_SV.dic
%{_datadir}/mythes/th_es_SV_v2.dat
%{_datadir}/myspell/th_es_SV_v2.dat
%{_datadir}/mythes/th_es_SV_v2.idx
%{_datadir}/myspell/th_es_SV_v2.idx

%files -n myspell-es_BO
%{_datadir}/hunspell/es_BO.aff
%{_datadir}/myspell/es_BO.aff
%{_datadir}/hunspell/es_BO.dic
%{_datadir}/myspell/es_BO.dic
%{_datadir}/hyphen/hyph_es_BO.dic
%{_datadir}/myspell/hyph_es_BO.dic
%{_datadir}/mythes/th_es_BO_v2.dat
%{_datadir}/myspell/th_es_BO_v2.dat
%{_datadir}/mythes/th_es_BO_v2.idx
%{_datadir}/myspell/th_es_BO_v2.idx

%files -n myspell-es_AR
%{_datadir}/hunspell/es_AR.aff
%{_datadir}/myspell/es_AR.aff
%{_datadir}/hunspell/es_AR.dic
%{_datadir}/myspell/es_AR.dic
%{_datadir}/hyphen/hyph_es_AR.dic
%{_datadir}/myspell/hyph_es_AR.dic
%{_datadir}/mythes/th_es_AR_v2.dat
%{_datadir}/myspell/th_es_AR_v2.dat
%{_datadir}/mythes/th_es_AR_v2.idx
%{_datadir}/myspell/th_es_AR_v2.idx

%files -n myspell-es
%{_datadir}/hunspell/es_ANY.aff
%{_datadir}/myspell/es_ANY.aff
%{_datadir}/hunspell/es_ANY.dic
%{_datadir}/myspell/es_ANY.dic
%{_datadir}/hyphen/hyph_es_ANY.dic
%{_datadir}/myspell/hyph_es_ANY.dic
%{_datadir}/mythes/th_es_ANY_v2.dat
%{_datadir}/myspell/th_es_ANY_v2.dat
%{_datadir}/mythes/th_es_ANY_v2.idx
%{_datadir}/myspell/th_es_ANY_v2.idx
%dir %{_docdir}/myspell-es
%{_docdir}/myspell-es/README_es_ANY.txt
%{_docdir}/myspell-es/README_hyph_es_ANY.txt
%{_docdir}/myspell-es/README_th_es_ANY.txt
%{_docdir}/myspell-es/description.xml
%{_docdir}/myspell-es/dictionaries.xcu
%{_docdir}/myspell-es/package-description.txt

%files -n myspell-es_UY
%{_datadir}/hunspell/es_UY.aff
%{_datadir}/myspell/es_UY.aff
%{_datadir}/hunspell/es_UY.dic
%{_datadir}/myspell/es_UY.dic
%{_datadir}/hyphen/hyph_es_UY.dic
%{_datadir}/myspell/hyph_es_UY.dic
%{_datadir}/mythes/th_es_UY_v2.dat
%{_datadir}/myspell/th_es_UY_v2.dat
%{_datadir}/mythes/th_es_UY_v2.idx
%{_datadir}/myspell/th_es_UY_v2.idx

%files -n myspell-es_VE
%{_datadir}/hunspell/es_VE.aff
%{_datadir}/myspell/es_VE.aff
%{_datadir}/hunspell/es_VE.dic
%{_datadir}/myspell/es_VE.dic
%{_datadir}/hyphen/hyph_es_VE.dic
%{_datadir}/myspell/hyph_es_VE.dic
%{_datadir}/mythes/th_es_VE_v2.dat
%{_datadir}/myspell/th_es_VE_v2.dat
%{_datadir}/mythes/th_es_VE_v2.idx
%{_datadir}/myspell/th_es_VE_v2.idx

%files -n myspell-et_EE
%{_datadir}/hunspell/et_EE.aff
%{_datadir}/myspell/et_EE.aff
%{_datadir}/hunspell/et_EE.dic
%{_datadir}/myspell/et_EE.dic
%{_datadir}/hyphen/hyph_et_EE.dic
%{_datadir}/myspell/hyph_et_EE.dic
%dir %{_docdir}/myspell-et_EE
%{_docdir}/myspell-et_EE/README_et_EE.txt
%{_docdir}/myspell-et_EE/README_hyph_et_EE.txt
%{_docdir}/myspell-et_EE/description.xml
%{_docdir}/myspell-et_EE/dictionaries.xcu
%{_docdir}/myspell-et_EE/eehyph.tex

%files -n myspell-fr_LU
%{_datadir}/hunspell/fr_LU.aff
%{_datadir}/myspell/fr_LU.aff
%{_datadir}/hunspell/fr_LU.dic
%{_datadir}/myspell/fr_LU.dic
%{_datadir}/hyphen/hyph_fr_LU.dic
%{_datadir}/myspell/hyph_fr_LU.dic
%{_datadir}/mythes/th_fr_LU_v2.dat
%{_datadir}/myspell/th_fr_LU_v2.dat
%{_datadir}/mythes/th_fr_LU_v2.idx
%{_datadir}/myspell/th_fr_LU_v2.idx

%files -n myspell-fr_BE
%{_datadir}/hunspell/fr_BE.aff
%{_datadir}/myspell/fr_BE.aff
%{_datadir}/hunspell/fr_BE.dic
%{_datadir}/myspell/fr_BE.dic
%{_datadir}/hyphen/hyph_fr_BE.dic
%{_datadir}/myspell/hyph_fr_BE.dic
%{_datadir}/mythes/th_fr_BE_v2.dat
%{_datadir}/myspell/th_fr_BE_v2.dat
%{_datadir}/mythes/th_fr_BE_v2.idx
%{_datadir}/myspell/th_fr_BE_v2.idx

%files -n myspell-fr_MC
%{_datadir}/hunspell/fr_MC.aff
%{_datadir}/myspell/fr_MC.aff
%{_datadir}/hunspell/fr_MC.dic
%{_datadir}/myspell/fr_MC.dic
%{_datadir}/hyphen/hyph_fr_MC.dic
%{_datadir}/myspell/hyph_fr_MC.dic
%{_datadir}/mythes/th_fr_MC_v2.dat
%{_datadir}/myspell/th_fr_MC_v2.dat
%{_datadir}/mythes/th_fr_MC_v2.idx
%{_datadir}/myspell/th_fr_MC_v2.idx

%files -n myspell-fr_CH
%{_datadir}/hunspell/fr_CH.aff
%{_datadir}/myspell/fr_CH.aff
%{_datadir}/hunspell/fr_CH.dic
%{_datadir}/myspell/fr_CH.dic
%{_datadir}/hyphen/hyph_fr_CH.dic
%{_datadir}/myspell/hyph_fr_CH.dic
%{_datadir}/mythes/th_fr_CH_v2.dat
%{_datadir}/myspell/th_fr_CH_v2.dat
%{_datadir}/mythes/th_fr_CH_v2.idx
%{_datadir}/myspell/th_fr_CH_v2.idx

%files -n myspell-fr_CA
%{_datadir}/hunspell/fr_CA.aff
%{_datadir}/myspell/fr_CA.aff
%{_datadir}/hunspell/fr_CA.dic
%{_datadir}/myspell/fr_CA.dic
%{_datadir}/hyphen/hyph_fr_CA.dic
%{_datadir}/myspell/hyph_fr_CA.dic
%{_datadir}/mythes/th_fr_CA_v2.dat
%{_datadir}/myspell/th_fr_CA_v2.dat
%{_datadir}/mythes/th_fr_CA_v2.idx
%{_datadir}/myspell/th_fr_CA_v2.idx

%files -n myspell-fr_FR
%{_datadir}/hunspell/fr_FR.aff
%{_datadir}/myspell/fr_FR.aff
%{_datadir}/hunspell/fr.aff
%{_datadir}/myspell/fr.aff
%{_datadir}/hunspell/fr_FR.dic
%{_datadir}/myspell/fr_FR.dic
%{_datadir}/hunspell/fr.dic
%{_datadir}/myspell/fr.dic
%{_datadir}/hyphen/hyph_fr_FR.dic
%{_datadir}/myspell/hyph_fr_FR.dic
%{_datadir}/hyphen/hyph_fr.dic
%{_datadir}/myspell/hyph_fr.dic
%{_datadir}/mythes/th_fr_FR_v2.dat
%{_datadir}/myspell/th_fr_FR_v2.dat
%{_datadir}/mythes/thes_fr.dat
%{_datadir}/myspell/thes_fr.dat
%{_datadir}/mythes/th_fr_FR_v2.idx
%{_datadir}/myspell/th_fr_FR_v2.idx
%{_datadir}/mythes/thes_fr.idx
%{_datadir}/myspell/thes_fr.idx
%dir %{_docdir}/myspell-fr_FR
%{_docdir}/myspell-fr_FR/README_fr.txt
%{_docdir}/myspell-fr_FR/README_hyph_fr.txt
%{_docdir}/myspell-fr_FR/README_thes_fr.txt
%{_docdir}/myspell-fr_FR/description.xml
%{_docdir}/myspell-fr_FR/dictionaries.xcu
%{_docdir}/myspell-fr_FR/hyph-fr.tex
%{_docdir}/myspell-fr_FR/icon.png
%{_docdir}/myspell-fr_FR/package-description.txt

%files -n myspell-gd_GB
%{_datadir}/hunspell/gd_GB.aff
%{_datadir}/myspell/gd_GB.aff
%{_datadir}/hunspell/gd_GB.dic
%{_datadir}/myspell/gd_GB.dic
%dir %{_docdir}/myspell-gd_GB
%{_docdir}/myspell-gd_GB/LICENSES-en.txt
%{_docdir}/myspell-gd_GB/README_gd_GB.txt
%{_docdir}/myspell-gd_GB/description.xml
%{_docdir}/myspell-gd_GB/dictionaries.xcu

%files -n myspell-gl
%{_datadir}/hunspell/gl.aff
%{_datadir}/myspell/gl.aff
%{_datadir}/hunspell/gl.dic
%{_datadir}/myspell/gl.dic
%{_datadir}/hyphen/hyph_gl.dic
%{_datadir}/myspell/hyph_gl.dic
%{_datadir}/mythes/th_gl_v2.dat
%{_datadir}/myspell/th_gl_v2.dat
%{_datadir}/mythes/thesaurus_gl.dat
%{_datadir}/myspell/thesaurus_gl.dat
%{_datadir}/mythes/th_gl_v2.idx
%{_datadir}/myspell/th_gl_v2.idx
%{_datadir}/mythes/thesaurus_gl.idx
%{_datadir}/myspell/thesaurus_gl.idx
%dir %{_docdir}/myspell-gl
%{_docdir}/myspell-gl/COPYING_th_gl
%{_docdir}/myspell-gl/Changelog.txt
%{_docdir}/myspell-gl/GPLv3.txt
%{_docdir}/myspell-gl/ProxectoTrasno.png
%{_docdir}/myspell-gl/README
%{_docdir}/myspell-gl/README_hyph-gl.txt
%{_docdir}/myspell-gl/README_th_gl.txt
%{_docdir}/myspell-gl/description.xml
%{_docdir}/myspell-gl/dictionaries.xcu
%{_docdir}/myspell-gl/package-description.txt

%files -n myspell-gl_ES
%{_datadir}/hunspell/gl_ES.aff
%{_datadir}/myspell/gl_ES.aff
%{_datadir}/hunspell/gl_ES.dic
%{_datadir}/myspell/gl_ES.dic
%{_datadir}/hyphen/hyph_gl_ES.dic
%{_datadir}/myspell/hyph_gl_ES.dic
%{_datadir}/mythes/th_gl_ES_v2.dat
%{_datadir}/myspell/th_gl_ES_v2.dat
%{_datadir}/mythes/th_gl_ES_v2.idx
%{_datadir}/myspell/th_gl_ES_v2.idx

%files -n myspell-gug
%{_datadir}/hunspell/gug.aff
%{_datadir}/myspell/gug.aff
%{_datadir}/hunspell/gug.dic
%{_datadir}/myspell/gug.dic
%{_datadir}/mythes/th_gug_PY.dat
%{_datadir}/myspell/th_gug_PY.dat
%{_datadir}/mythes/th_gug_PY.idx
%{_datadir}/myspell/th_gug_PY.idx
%dir %{_docdir}/myspell-gug
%{_docdir}/myspell-gug/README_th_gug_PY.txt
%{_docdir}/myspell-gug/description.xml
%{_docdir}/myspell-gug/dictionaries.xcu

%files -n myspell-gug_PY
%{_datadir}/hunspell/gug_PY.aff
%{_datadir}/myspell/gug_PY.aff
%{_datadir}/hunspell/gug_PY.dic
%{_datadir}/myspell/gug_PY.dic
%{_datadir}/mythes/th_gug_PY_v2.dat
%{_datadir}/myspell/th_gug_PY_v2.dat
%{_datadir}/mythes/th_gug_PY_v2.idx
%{_datadir}/myspell/th_gug_PY_v2.idx

%files -n myspell-gu_IN
%{_datadir}/hunspell/gu_IN.aff
%{_datadir}/myspell/gu_IN.aff
%{_datadir}/hunspell/gu_IN.dic
%{_datadir}/myspell/gu_IN.dic
%dir %{_docdir}/myspell-gu_IN
%{_docdir}/myspell-gu_IN/README_gu_IN.txt
%{_docdir}/myspell-gu_IN/description.xml
%{_docdir}/myspell-gu_IN/dictionaries.xcu

%files -n myspell-he_IL
%{_datadir}/hunspell/he_IL.aff
%{_datadir}/myspell/he_IL.aff
%{_datadir}/hunspell/he_IL.dic
%{_datadir}/myspell/he_IL.dic
%dir %{_docdir}/myspell-he_IL
%{_docdir}/myspell-he_IL/README_he_IL.txt
%{_docdir}/myspell-he_IL/alphabet.png
%{_docdir}/myspell-he_IL/description.xml
%{_docdir}/myspell-he_IL/dictionaries.xcu

%files -n myspell-hi_IN
%{_datadir}/hunspell/hi_IN.aff
%{_datadir}/myspell/hi_IN.aff
%{_datadir}/hunspell/hi_IN.dic
%{_datadir}/myspell/hi_IN.dic
%dir %{_docdir}/myspell-hi_IN
%{_docdir}/myspell-hi_IN/COPYING
%{_docdir}/myspell-hi_IN/Copyright
%{_docdir}/myspell-hi_IN/README_hi_IN.txt
%{_docdir}/myspell-hi_IN/description.xml
%{_docdir}/myspell-hi_IN/dictionaries.xcu

%files -n myspell-hr_HR
%{_datadir}/hunspell/hr_HR.aff
%{_datadir}/myspell/hr_HR.aff
%{_datadir}/hunspell/hr_HR.dic
%{_datadir}/myspell/hr_HR.dic
%{_datadir}/hyphen/hyph_hr_HR.dic
%{_datadir}/myspell/hyph_hr_HR.dic
%dir %{_docdir}/myspell-hr_HR
%{_docdir}/myspell-hr_HR/README_hr_HR.txt
%{_docdir}/myspell-hr_HR/README_hyph_hr_HR.txt
%{_docdir}/myspell-hr_HR/description.xml
%{_docdir}/myspell-hr_HR/dictionaries.xcu

%files -n myspell-hu_HU
%{_datadir}/hunspell/hu_HU.aff
%{_datadir}/myspell/hu_HU.aff
%{_datadir}/hunspell/hu_HU.dic
%{_datadir}/myspell/hu_HU.dic
%{_datadir}/hyphen/hyph_hu_HU.dic
%{_datadir}/myspell/hyph_hu_HU.dic
%{_datadir}/mythes/th_hu_HU_v2.dat
%{_datadir}/myspell/th_hu_HU_v2.dat
%{_datadir}/mythes/th_hu_HU_v2.idx
%{_datadir}/myspell/th_hu_HU_v2.idx
%dir %{_docdir}/myspell-hu_HU
%{_docdir}/myspell-hu_HU/Linguistic.xcu
%{_docdir}/myspell-hu_HU/README_hu_HU.txt
%{_docdir}/myspell-hu_HU/README_hyph_hu_HU.txt
%{_docdir}/myspell-hu_HU/README_lightproof_hu_HU.txt
%{_docdir}/myspell-hu_HU/README_th_hu_HU_v2.txt
%{_docdir}/myspell-hu_HU/description.xml
%{_docdir}/myspell-hu_HU/dictionaries.xcu

%files -n myspell-lightproof-hu_HU
%dir %{_libdir}/libreoffice/share/extensions/lightproof-hu_HU
%{_libdir}/libreoffice/share/extensions/lightproof-hu_HU/Lightproof.components
%{_libdir}/libreoffice/share/extensions/lightproof-hu_HU/Lightproof.py
%{_libdir}/libreoffice/share/extensions/lightproof-hu_HU/Linguistic.xcu
%{_libdir}/libreoffice/share/extensions/lightproof-hu_HU/META-INF
%{_libdir}/libreoffice/share/extensions/lightproof-hu_HU/description.xml
%{_libdir}/libreoffice/share/extensions/lightproof-hu_HU/dialog
%{_libdir}/libreoffice/share/extensions/lightproof-hu_HU/pythonpath

%files -n myspell-id
%dir %{_docdir}/myspell-id
%{_docdir}/myspell-id/LICENSE-dict
%{_docdir}/myspell-id/LICENSE-thes
%{_docdir}/myspell-id/README-thes
%{_docdir}/myspell-id/description.xml
%{_docdir}/myspell-id/dictionaries.xcu

%files -n myspell-id_ID
%{_datadir}/hyphen/hyph_id_ID.dic
%{_datadir}/myspell/hyph_id_ID.dic
%{_datadir}/hunspell/id_ID.aff
%{_datadir}/myspell/id_ID.aff
%{_datadir}/hunspell/id_ID.dic
%{_datadir}/myspell/id_ID.dic
%{_datadir}/mythes/th_id_ID_v2.dat
%{_datadir}/myspell/th_id_ID_v2.dat
%{_datadir}/mythes/th_id_ID_v2.idx
%{_datadir}/myspell/th_id_ID_v2.idx

%files -n myspell-is_IS
%{_datadir}/hyphen/hyph_is_IS.dic
%{_datadir}/myspell/hyph_is_IS.dic
%{_datadir}/hunspell/is_IS.aff
%{_datadir}/myspell/is_IS.aff
%{_datadir}/hunspell/is_IS.dic
%{_datadir}/myspell/is_IS.dic
%{_datadir}/mythes/th_is_IS_v2.dat
%{_datadir}/myspell/th_is_IS_v2.dat
%{_datadir}/mythes/th_is_IS_v2.idx
%{_datadir}/myspell/th_is_IS_v2.idx

%files -n myspell-is
%{_datadir}/hyphen/hyph_is.dic
%{_datadir}/myspell/hyph_is.dic
%{_datadir}/hunspell/is.aff
%{_datadir}/myspell/is.aff
%{_datadir}/hunspell/is.dic
%{_datadir}/myspell/is.dic
%{_datadir}/mythes/th_is_v2.dat
%{_datadir}/myspell/th_is_v2.dat
%{_datadir}/mythes/th_is.dat
%{_datadir}/myspell/th_is.dat
%{_datadir}/mythes/th_is_v2.idx
%{_datadir}/myspell/th_is_v2.idx
%{_datadir}/mythes/th_is.idx
%{_datadir}/myspell/th_is.idx
%dir %{_docdir}/myspell-is
%{_docdir}/myspell-is/description.xml
%{_docdir}/myspell-is/dictionaries.xcu
%{_docdir}/myspell-is/license.txt

%files -n myspell-it_IT
%{_datadir}/hyphen/hyph_it_IT.dic
%{_datadir}/myspell/hyph_it_IT.dic
%{_datadir}/hunspell/it_IT.aff
%{_datadir}/myspell/it_IT.aff
%{_datadir}/hunspell/it_IT.dic
%{_datadir}/myspell/it_IT.dic
%{_datadir}/mythes/th_it_IT_v2.dat
%{_datadir}/myspell/th_it_IT_v2.dat
%{_datadir}/mythes/th_it_IT_v2.idx
%{_datadir}/myspell/th_it_IT_v2.idx
%dir %{_docdir}/myspell-it_IT
%{_docdir}/myspell-it_IT/CHANGELOG.txt
%{_docdir}/myspell-it_IT/README_hyph_it_IT.txt
%{_docdir}/myspell-it_IT/README_it_IT.txt
%{_docdir}/myspell-it_IT/README_th_it_IT.txt
%{_docdir}/myspell-it_IT/description.xml
%{_docdir}/myspell-it_IT/dictionaries.xcu

%files -n myspell-kmr_Latn_TR
%{_datadir}/hunspell/kmr_Latn_TR.aff
%{_datadir}/myspell/kmr_Latn_TR.aff
%{_datadir}/hunspell/kmr_Latn_TR.dic
%{_datadir}/myspell/kmr_Latn_TR.dic

%files -n myspell-kmr_Latn
%{_datadir}/hunspell/kmr_Latn.aff
%{_datadir}/myspell/kmr_Latn.aff
%{_datadir}/hunspell/kmr_Latn.dic
%{_datadir}/myspell/kmr_Latn.dic
%dir %{_docdir}/myspell-kmr_Latn
%{_docdir}/myspell-kmr_Latn/MPL-1.1.txt
%{_docdir}/myspell-kmr_Latn/README_kmr_Latn.txt
%{_docdir}/myspell-kmr_Latn/description.xml
%{_docdir}/myspell-kmr_Latn/dictionaries.xcu
%{_docdir}/myspell-kmr_Latn/ferheng.org.png
%{_docdir}/myspell-kmr_Latn/gpl-3.0.txt
%{_docdir}/myspell-kmr_Latn/lgpl-2.1.txt
%{_docdir}/myspell-kmr_Latn/license.txt

%files -n myspell-kmr_Latn_SY
%{_datadir}/hunspell/kmr_Latn_SY.aff
%{_datadir}/myspell/kmr_Latn_SY.aff
%{_datadir}/hunspell/kmr_Latn_SY.dic
%{_datadir}/myspell/kmr_Latn_SY.dic

%files -n myspell-lo_LA
%{_datadir}/hunspell/lo_LA.aff
%{_datadir}/myspell/lo_LA.aff
%{_datadir}/hunspell/lo_LA.dic
%{_datadir}/myspell/lo_LA.dic
%dir %{_docdir}/myspell-lo_LA
%{_docdir}/myspell-lo_LA/README_lo_LA.txt
%{_docdir}/myspell-lo_LA/description.xml
%{_docdir}/myspell-lo_LA/dictionaries.xcu

%files -n myspell-lt_LT
%{_datadir}/hyphen/hyph_lt_LT.dic
%{_datadir}/myspell/hyph_lt_LT.dic
%{_datadir}/hyphen/hyph_lt.dic
%{_datadir}/myspell/hyph_lt.dic
%{_datadir}/hunspell/lt_LT.aff
%{_datadir}/myspell/lt_LT.aff
%{_datadir}/hunspell/lt.aff
%{_datadir}/myspell/lt.aff
%{_datadir}/hunspell/lt_LT.dic
%{_datadir}/myspell/lt_LT.dic
%{_datadir}/hunspell/lt.dic
%{_datadir}/myspell/lt.dic
%dir %{_docdir}/myspell-lt_LT
%{_docdir}/myspell-lt_LT/AUTHORS
%{_docdir}/myspell-lt_LT/COPYING
%{_docdir}/myspell-lt_LT/README
%{_docdir}/myspell-lt_LT/README_hyph
%{_docdir}/myspell-lt_LT/description.xml
%{_docdir}/myspell-lt_LT/dictionaries.xcu

%files -n myspell-lv_LV
%{_datadir}/hyphen/hyph_lv_LV.dic
%{_datadir}/myspell/hyph_lv_LV.dic
%{_datadir}/hunspell/lv_LV.aff
%{_datadir}/myspell/lv_LV.aff
%{_datadir}/hunspell/lv_LV.dic
%{_datadir}/myspell/lv_LV.dic
%{_datadir}/mythes/th_lv_LV_v2.dat
%{_datadir}/myspell/th_lv_LV_v2.dat
%{_datadir}/mythes/th_lv_LV_v2.idx
%{_datadir}/myspell/th_lv_LV_v2.idx
%dir %{_docdir}/myspell-lv_LV
%{_docdir}/myspell-lv_LV/Changelog.txt
%{_docdir}/myspell-lv_LV/README_hyph_lv_LV.txt
%{_docdir}/myspell-lv_LV/README_lv_LV.txt
%{_docdir}/myspell-lv_LV/README_th_lv_LV_v2.txt
%{_docdir}/myspell-lv_LV/description.xml
%{_docdir}/myspell-lv_LV/dictionaries.xcu
%{_docdir}/myspell-lv_LV/license.txt

%files -n myspell-ne_NP
%{_datadir}/hunspell/ne_NP.aff
%{_datadir}/myspell/ne_NP.aff
%{_datadir}/hunspell/ne_NP.dic
%{_datadir}/myspell/ne_NP.dic
%{_datadir}/mythes/th_ne_NP_v2.dat
%{_datadir}/myspell/th_ne_NP_v2.dat
%{_datadir}/mythes/th_ne_NP_v2.idx
%{_datadir}/myspell/th_ne_NP_v2.idx
%dir %{_docdir}/myspell-ne_NP
%{_docdir}/myspell-ne_NP/README_ne_NP.txt
%{_docdir}/myspell-ne_NP/README_th_ne_NP_v2.txt
%{_docdir}/myspell-ne_NP/description.xml
%{_docdir}/myspell-ne_NP/dictionaries.xcu

%files -n myspell-nl_NL
%{_datadir}/hyphen/hyph_nl_NL.dic
%{_datadir}/myspell/hyph_nl_NL.dic
%{_datadir}/hunspell/nl_NL.aff
%{_datadir}/myspell/nl_NL.aff
%{_datadir}/hunspell/nl_NL.dic
%{_datadir}/myspell/nl_NL.dic
%dir %{_docdir}/myspell-nl_NL
%{_docdir}/myspell-nl_NL/OpenTaal.png
%{_docdir}/myspell-nl_NL/README_NL.txt
%{_docdir}/myspell-nl_NL/desc_en_US.txt
%{_docdir}/myspell-nl_NL/desc_nl_NL.txt
%{_docdir}/myspell-nl_NL/description.xml
%{_docdir}/myspell-nl_NL/dictionaries.xcu
%{_docdir}/myspell-nl_NL/license_en_EN.txt
%{_docdir}/myspell-nl_NL/licentie_nl_NL.txt

%files -n myspell-nl_BE
%{_datadir}/hyphen/hyph_nl_BE.dic
%{_datadir}/myspell/hyph_nl_BE.dic
%{_datadir}/hunspell/nl_BE.aff
%{_datadir}/myspell/nl_BE.aff
%{_datadir}/hunspell/nl_BE.dic
%{_datadir}/myspell/nl_BE.dic

%files -n myspell-no
%dir %{_docdir}/myspell-no
%{_docdir}/myspell-no/COPYING
%{_docdir}/myspell-no/README_hyph_NO.txt
%{_docdir}/myspell-no/description.xml
%{_docdir}/myspell-no/dictionaries.xcu

%files -n myspell-nb_NO
%{_datadir}/hyphen/hyph_nb_NO.dic
%{_datadir}/myspell/hyph_nb_NO.dic
%{_datadir}/hunspell/nb_NO.aff
%{_datadir}/myspell/nb_NO.aff
%{_datadir}/hunspell/nb_NO.dic
%{_datadir}/myspell/nb_NO.dic
%{_datadir}/mythes/th_nb_NO_v2.dat
%{_datadir}/myspell/th_nb_NO_v2.dat
%{_datadir}/mythes/th_nb_NO_v2.idx
%{_datadir}/myspell/th_nb_NO_v2.idx

%files -n myspell-nn_NO
%{_datadir}/hyphen/hyph_nn_NO.dic
%{_datadir}/myspell/hyph_nn_NO.dic
%{_datadir}/hunspell/nn_NO.aff
%{_datadir}/myspell/nn_NO.aff
%{_datadir}/hunspell/nn_NO.dic
%{_datadir}/myspell/nn_NO.dic
%{_datadir}/mythes/th_nn_NO_v2.dat
%{_datadir}/myspell/th_nn_NO_v2.dat
%{_datadir}/mythes/th_nn_NO_v2.idx
%{_datadir}/myspell/th_nn_NO_v2.idx

%files -n myspell-oc_FR
%{_datadir}/hunspell/oc_FR.aff
%{_datadir}/myspell/oc_FR.aff
%{_datadir}/hunspell/oc_FR.dic
%{_datadir}/myspell/oc_FR.dic
%dir %{_docdir}/myspell-oc_FR
%{_docdir}/myspell-oc_FR/LICENCES-fr.txt
%{_docdir}/myspell-oc_FR/LICENSES-en.txt
%{_docdir}/myspell-oc_FR/README_oc_FR.txt
%{_docdir}/myspell-oc_FR/description.xml
%{_docdir}/myspell-oc_FR/dictionaries.xcu

%files -n myspell-pl_PL
%{_datadir}/hyphen/hyph_pl_PL.dic
%{_datadir}/myspell/hyph_pl_PL.dic
%{_datadir}/hunspell/pl_PL.aff
%{_datadir}/myspell/pl_PL.aff
%{_datadir}/hunspell/pl_PL.dic
%{_datadir}/myspell/pl_PL.dic
%{_datadir}/mythes/th_pl_PL_v2.dat
%{_datadir}/myspell/th_pl_PL_v2.dat
%{_datadir}/mythes/th_pl_PL_v2.idx
%{_datadir}/myspell/th_pl_PL_v2.idx
%dir %{_docdir}/myspell-pl_PL
%{_docdir}/myspell-pl_PL/README_en.txt
%{_docdir}/myspell-pl_PL/README_pl.txt
%{_docdir}/myspell-pl_PL/description.xml
%{_docdir}/myspell-pl_PL/dictionaries.xcu
%{_docdir}/myspell-pl_PL/plhyph.tex

%files -n myspell-pt_BR
%{_datadir}/hyphen/hyph_pt_BR.dic
%{_datadir}/myspell/hyph_pt_BR.dic
%{_datadir}/hunspell/pt_BR.aff
%{_datadir}/myspell/pt_BR.aff
%{_datadir}/hunspell/pt_BR.dic
%{_datadir}/myspell/pt_BR.dic
%dir %{_docdir}/myspell-pt_BR
%{_docdir}/myspell-pt_BR/Linguistic.xcu
%{_docdir}/myspell-pt_BR/README_Lightproof_pt_BR.txt
%{_docdir}/myspell-pt_BR/README_en.txt
%{_docdir}/myspell-pt_BR/README_hyph_pt_BR.txt
%{_docdir}/myspell-pt_BR/README_pt_BR.txt
%{_docdir}/myspell-pt_BR/description.xml
%{_docdir}/myspell-pt_BR/dictionaries.xcu
%{_docdir}/myspell-pt_BR/package-description.txt

%files -n myspell-lightproof-pt_BR
%dir %{_libdir}/libreoffice/share/extensions/lightproof-pt_BR
%{_libdir}/libreoffice/share/extensions/lightproof-pt_BR/Lightproof.components
%{_libdir}/libreoffice/share/extensions/lightproof-pt_BR/Lightproof.py
%{_libdir}/libreoffice/share/extensions/lightproof-pt_BR/Linguistic.xcu
%{_libdir}/libreoffice/share/extensions/lightproof-pt_BR/META-INF
%{_libdir}/libreoffice/share/extensions/lightproof-pt_BR/description.xml
%{_libdir}/libreoffice/share/extensions/lightproof-pt_BR/dialog
%{_libdir}/libreoffice/share/extensions/lightproof-pt_BR/icons
%{_libdir}/libreoffice/share/extensions/lightproof-pt_BR/pythonpath

%files -n myspell-pt_PT
%{_datadir}/hyphen/hyph_pt_PT.dic
%{_datadir}/myspell/hyph_pt_PT.dic
%{_datadir}/hunspell/pt_PT.aff
%{_datadir}/myspell/pt_PT.aff
%{_datadir}/hunspell/pt_PT.dic
%{_datadir}/myspell/pt_PT.dic
%{_datadir}/mythes/th_pt_PT_v2.dat
%{_datadir}/myspell/th_pt_PT_v2.dat
%{_datadir}/mythes/th_pt_PT_v2.idx
%{_datadir}/myspell/th_pt_PT_v2.idx
%dir %{_docdir}/myspell-pt_PT
%{_docdir}/myspell-pt_PT/LICENSES.txt
%{_docdir}/myspell-pt_PT/README_hyph_pt_PT.txt
%{_docdir}/myspell-pt_PT/README_pt_PT.txt
%{_docdir}/myspell-pt_PT/README_th_pt_PT_v2.txt
%{_docdir}/myspell-pt_PT/description.xml
%{_docdir}/myspell-pt_PT/dictionaries.xcu
%{_docdir}/myspell-pt_PT/icon.png

%files -n myspell-pt_AO
%{_datadir}/hyphen/hyph_pt_AO.dic
%{_datadir}/myspell/hyph_pt_AO.dic
%{_datadir}/hunspell/pt_AO.aff
%{_datadir}/myspell/pt_AO.aff
%{_datadir}/hunspell/pt_AO.dic
%{_datadir}/myspell/pt_AO.dic
%{_datadir}/mythes/th_pt_AO_v2.dat
%{_datadir}/myspell/th_pt_AO_v2.dat
%{_datadir}/mythes/th_pt_AO_v2.idx
%{_datadir}/myspell/th_pt_AO_v2.idx

%files -n myspell-ro_RO
%{_datadir}/hyphen/hyph_ro_RO.dic
%{_datadir}/myspell/hyph_ro_RO.dic
%{_datadir}/hunspell/ro_RO.aff
%{_datadir}/myspell/ro_RO.aff
%{_datadir}/hunspell/ro_RO.dic
%{_datadir}/myspell/ro_RO.dic
%{_datadir}/mythes/th_ro_RO_v2.dat
%{_datadir}/myspell/th_ro_RO_v2.dat
%{_datadir}/mythes/th_ro_RO_v2.idx
%{_datadir}/myspell/th_ro_RO_v2.idx

%files -n myspell-ro
%dir %{_docdir}/myspell-ro
%{_docdir}/myspell-ro/README_EN.txt
%{_docdir}/myspell-ro/README_RO.txt
%{_docdir}/myspell-ro/description.xml
%{_docdir}/myspell-ro/dictionaries.xcu

%files -n myspell-ru_RU
%{_datadir}/hyphen/hyph_ru_RU.dic
%{_datadir}/myspell/hyph_ru_RU.dic
%{_datadir}/hunspell/ru_RU.aff
%{_datadir}/myspell/ru_RU.aff
%{_datadir}/hunspell/ru_RU.dic
%{_datadir}/myspell/ru_RU.dic
%{_datadir}/mythes/th_ru_RU_v2.dat
%{_datadir}/myspell/th_ru_RU_v2.dat
%{_datadir}/mythes/th_ru_RU_M_aot_and_v2.dat
%{_datadir}/myspell/th_ru_RU_M_aot_and_v2.dat
%{_datadir}/mythes/th_ru_RU_v2.idx
%{_datadir}/myspell/th_ru_RU_v2.idx
%{_datadir}/mythes/th_ru_RU_M_aot_and_v2.idx
%{_datadir}/myspell/th_ru_RU_M_aot_and_v2.idx
%dir %{_docdir}/myspell-ru_RU
%{_docdir}/myspell-ru_RU/Linguistic.xcu
%{_docdir}/myspell-ru_RU/README_Lightproof_ru_RU.txt
%{_docdir}/myspell-ru_RU/README_ru_RU.txt
%{_docdir}/myspell-ru_RU/README_thes_ru_RU_M_aot_and_v2.txt
%{_docdir}/myspell-ru_RU/description.xml
%{_docdir}/myspell-ru_RU/dictionaries.xcu

%files -n myspell-lightproof-ru_RU
%dir %{_libdir}/libreoffice/share/extensions/lightproof-ru_RU
%{_libdir}/libreoffice/share/extensions/lightproof-ru_RU/Lightproof.components
%{_libdir}/libreoffice/share/extensions/lightproof-ru_RU/Lightproof.py
%{_libdir}/libreoffice/share/extensions/lightproof-ru_RU/Linguistic.xcu
%{_libdir}/libreoffice/share/extensions/lightproof-ru_RU/META-INF
%{_libdir}/libreoffice/share/extensions/lightproof-ru_RU/description.xml
%{_libdir}/libreoffice/share/extensions/lightproof-ru_RU/dialog
%{_libdir}/libreoffice/share/extensions/lightproof-ru_RU/pythonpath

%files -n myspell-si_LK
%{_datadir}/hunspell/si_LK.aff
%{_datadir}/myspell/si_LK.aff
%{_datadir}/hunspell/si_LK.dic
%{_datadir}/myspell/si_LK.dic
%dir %{_docdir}/myspell-si_LK
%{_docdir}/myspell-si_LK/LICENSES-en.txt
%{_docdir}/myspell-si_LK/description.xml
%{_docdir}/myspell-si_LK/dictionaries.xcu

%files -n myspell-sk_SK
%{_datadir}/hyphen/hyph_sk_SK.dic
%{_datadir}/myspell/hyph_sk_SK.dic
%{_datadir}/hunspell/sk_SK.aff
%{_datadir}/myspell/sk_SK.aff
%{_datadir}/hunspell/sk_SK.dic
%{_datadir}/myspell/sk_SK.dic
%{_datadir}/mythes/th_sk_SK_v2.dat
%{_datadir}/myspell/th_sk_SK_v2.dat
%{_datadir}/mythes/th_sk_SK_v2.idx
%{_datadir}/myspell/th_sk_SK_v2.idx
%dir %{_docdir}/myspell-sk_SK
%{_docdir}/myspell-sk_SK/LICENSE.txt
%{_docdir}/myspell-sk_SK/README_en.txt
%{_docdir}/myspell-sk_SK/README_sk.txt
%{_docdir}/myspell-sk_SK/README_th_sk_SK_v2.txt
%{_docdir}/myspell-sk_SK/description.xml
%{_docdir}/myspell-sk_SK/dictionaries.xcu
%{_docdir}/myspell-sk_SK/release_en.txt
%{_docdir}/myspell-sk_SK/release_sk.txt

%files -n myspell-sl_SI
%{_datadir}/hyphen/hyph_sl_SI.dic
%{_datadir}/myspell/hyph_sl_SI.dic
%{_datadir}/hunspell/sl_SI.aff
%{_datadir}/myspell/sl_SI.aff
%{_datadir}/hunspell/sl_SI.dic
%{_datadir}/myspell/sl_SI.dic
%{_datadir}/mythes/th_sl_SI_v2.dat
%{_datadir}/myspell/th_sl_SI_v2.dat
%{_datadir}/mythes/th_sl_SI_v2.idx
%{_datadir}/myspell/th_sl_SI_v2.idx
%dir %{_docdir}/myspell-sl_SI
%{_docdir}/myspell-sl_SI/README_hyph_sl_SI.txt
%{_docdir}/myspell-sl_SI/README_sl_SI.txt
%{_docdir}/myspell-sl_SI/README_th_sl_SI.txt
%{_docdir}/myspell-sl_SI/description.xml
%{_docdir}/myspell-sl_SI/dictionaries.xcu
%{_docdir}/myspell-sl_SI/icon.png
%{_docdir}/myspell-sl_SI/package-description.txt

%files -n myspell-sq_AL
%{_datadir}/hunspell/sq_AL.aff
%{_datadir}/myspell/sq_AL.aff
%{_datadir}/hunspell/sq_AL.dic
%{_datadir}/myspell/sq_AL.dic
%dir %{_docdir}/myspell-sq_AL
%{_docdir}/myspell-sq_AL/README.txt
%{_docdir}/myspell-sq_AL/description.xml
%{_docdir}/myspell-sq_AL/dictionaries.xcu

%files -n myspell-sr_Latn_CS
%{_datadir}/hyphen/hyph_sr_Latn_CS.dic
%{_datadir}/myspell/hyph_sr_Latn_CS.dic
%{_datadir}/hunspell/sr_Latn_CS.aff
%{_datadir}/myspell/sr_Latn_CS.aff
%{_datadir}/hunspell/sr_Latn_CS.dic
%{_datadir}/myspell/sr_Latn_CS.dic

%files -n myspell-sr_CS
%{_datadir}/hyphen/hyph_sr_CS.dic
%{_datadir}/myspell/hyph_sr_CS.dic
%{_datadir}/hunspell/sr_CS.aff
%{_datadir}/myspell/sr_CS.aff
%{_datadir}/hunspell/sr_CS.dic
%{_datadir}/myspell/sr_CS.dic

%files -n myspell-sr
%{_datadir}/hyphen/hyph_sr.dic
%{_datadir}/myspell/hyph_sr.dic
%{_datadir}/hyphen/hyph_sr-Latn.dic
%{_datadir}/myspell/hyph_sr-Latn.dic
%{_datadir}/hunspell/sr.aff
%{_datadir}/myspell/sr.aff
%{_datadir}/hunspell/sr.dic
%{_datadir}/myspell/sr.dic
%{_datadir}/hunspell/sr-Latn.aff
%{_datadir}/myspell/sr-Latn.aff
%{_datadir}/hunspell/sr-Latn.dic
%{_datadir}/myspell/sr-Latn.dic
%dir %{_docdir}/myspell-sr
%{_docdir}/myspell-sr/README.txt
%{_docdir}/myspell-sr/description.xml
%{_docdir}/myspell-sr/dictionaries.xcu

%files -n myspell-sr_Latn_RS
%{_datadir}/hyphen/hyph_sr_Latn_RS.dic
%{_datadir}/myspell/hyph_sr_Latn_RS.dic
%{_datadir}/hunspell/sr_Latn_RS.aff
%{_datadir}/myspell/sr_Latn_RS.aff
%{_datadir}/hunspell/sr_Latn_RS.dic
%{_datadir}/myspell/sr_Latn_RS.dic

%files -n myspell-sr_RS
%{_datadir}/hyphen/hyph_sr_RS.dic
%{_datadir}/myspell/hyph_sr_RS.dic
%{_datadir}/hunspell/sr_RS.aff
%{_datadir}/myspell/sr_RS.aff
%{_datadir}/hunspell/sr_RS.dic
%{_datadir}/myspell/sr_RS.dic

%files -n myspell-sv_SE
%{_datadir}/hyphen/hyph_sv_SE.dic
%{_datadir}/myspell/hyph_sv_SE.dic
%{_datadir}/hyphen/hyph_sv.dic
%{_datadir}/myspell/hyph_sv.dic
%{_datadir}/hunspell/sv_SE.aff
%{_datadir}/myspell/sv_SE.aff
%{_datadir}/hunspell/sv_SE.dic
%{_datadir}/myspell/sv_SE.dic
%{_datadir}/mythes/th_sv_SE_v2.dat
%{_datadir}/myspell/th_sv_SE_v2.dat
%{_datadir}/mythes/th_sv_SE.dat
%{_datadir}/myspell/th_sv_SE.dat
%{_datadir}/mythes/th_sv_SE_v2.idx
%{_datadir}/myspell/th_sv_SE_v2.idx
%{_datadir}/mythes/th_sv_SE.idx
%{_datadir}/myspell/th_sv_SE.idx
%dir %{_docdir}/myspell-sv_SE
%{_docdir}/myspell-sv_SE/LICENSE_en_US.txt
%{_docdir}/myspell-sv_SE/LICENSE_sv_SE.txt
%{_docdir}/myspell-sv_SE/README_hyph_sv.txt
%{_docdir}/myspell-sv_SE/README_th_sv_SE.txt
%{_docdir}/myspell-sv_SE/description.xml
%{_docdir}/myspell-sv_SE/dictionaries.xcu

%files -n myspell-sv_FI
%{_datadir}/hyphen/hyph_sv_FI.dic
%{_datadir}/myspell/hyph_sv_FI.dic
%{_datadir}/hunspell/sv_FI.aff
%{_datadir}/myspell/sv_FI.aff
%{_datadir}/hunspell/sv_FI.dic
%{_datadir}/myspell/sv_FI.dic

%files -n myspell-sw_TZ
%{_datadir}/hunspell/sw_TZ.aff
%{_datadir}/myspell/sw_TZ.aff
%{_datadir}/hunspell/sw_TZ.dic
%{_datadir}/myspell/sw_TZ.dic
%dir %{_docdir}/myspell-sw_TZ
%{_docdir}/myspell-sw_TZ/README_sw_TZ.txt
%{_docdir}/myspell-sw_TZ/description.xml
%{_docdir}/myspell-sw_TZ/dictionaries.xcu

%files -n myspell-te
%{_datadir}/hyphen/hyph_te.dic
%{_datadir}/myspell/hyph_te.dic
%{_datadir}/hunspell/te.aff
%{_datadir}/myspell/te.aff
%{_datadir}/hunspell/te.dic
%{_datadir}/myspell/te.dic

%files -n myspell-te_IN
%{_datadir}/hyphen/hyph_te_IN.dic
%{_datadir}/myspell/hyph_te_IN.dic
%{_datadir}/hunspell/te_IN.aff
%{_datadir}/myspell/te_IN.aff
%{_datadir}/hunspell/te_IN.dic
%{_datadir}/myspell/te_IN.dic
%dir %{_docdir}/myspell-te_IN
%{_docdir}/myspell-te_IN/README_hyph_te_IN.txt
%{_docdir}/myspell-te_IN/README_te_IN.txt
%{_docdir}/myspell-te_IN/description.xml
%{_docdir}/myspell-te_IN/dictionaries.xcu

%files -n myspell-th_TH
%{_datadir}/hunspell/th_TH.aff
%{_datadir}/myspell/th_TH.aff
%{_datadir}/hunspell/th_TH.dic
%{_datadir}/myspell/th_TH.dic
%dir %{_docdir}/myspell-th_TH
%{_docdir}/myspell-th_TH/README_th_TH.txt
%{_docdir}/myspell-th_TH/description.xml
%{_docdir}/myspell-th_TH/dictionaries.xcu

%files -n myspell-tr
%{_datadir}/hunspell/tr.aff
%{_datadir}/myspell/tr.aff
%{_datadir}/hunspell/tr.dic
%{_datadir}/myspell/tr.dic

%files -n myspell-tr_TR
%{_datadir}/hunspell/tr_TR.aff
%{_datadir}/myspell/tr_TR.aff
%{_datadir}/hunspell/tr_TR.dic
%{_datadir}/myspell/tr_TR.dic
%dir %{_docdir}/myspell-tr_TR
%{_docdir}/myspell-tr_TR/LICENSE
%{_docdir}/myspell-tr_TR/README.txt
%{_docdir}/myspell-tr_TR/description.xml
%{_docdir}/myspell-tr_TR/dictionaries.xcu

%files -n myspell-uk_UA
%{_datadir}/hyphen/hyph_uk_UA.dic
%{_datadir}/myspell/hyph_uk_UA.dic
%{_datadir}/mythes/th_uk_UA_v2.dat
%{_datadir}/myspell/th_uk_UA_v2.dat
%{_datadir}/mythes/th_uk_UA.dat
%{_datadir}/myspell/th_uk_UA.dat
%{_datadir}/mythes/th_uk_UA_v2.idx
%{_datadir}/myspell/th_uk_UA_v2.idx
%{_datadir}/mythes/th_uk_UA.idx
%{_datadir}/myspell/th_uk_UA.idx
%{_datadir}/hunspell/uk_UA.aff
%{_datadir}/myspell/uk_UA.aff
%{_datadir}/hunspell/uk_UA.dic
%{_datadir}/myspell/uk_UA.dic
%dir %{_docdir}/myspell-uk_UA
%{_docdir}/myspell-uk_UA/README_hyph_uk_UA.txt
%{_docdir}/myspell-uk_UA/README_th_uk_UA.txt
%{_docdir}/myspell-uk_UA/README_uk_UA.txt
%{_docdir}/myspell-uk_UA/description.xml
%{_docdir}/myspell-uk_UA/dictionaries.xcu

%files -n myspell-vi
%dir %{_docdir}/myspell-vi
%{_docdir}/myspell-vi/LICENSES-en.txt
%{_docdir}/myspell-vi/LICENSES-vi.txt
%{_docdir}/myspell-vi/description.xml
%{_docdir}/myspell-vi/dictionaries.xcu

%files -n myspell-vi_VN
%{_datadir}/hunspell/vi_VN.aff
%{_datadir}/myspell/vi_VN.aff
%{_datadir}/hunspell/vi_VN.dic
%{_datadir}/myspell/vi_VN.dic

%files -n myspell-zu_ZA
%{_datadir}/hyphen/hyph_zu_ZA.dic
%{_datadir}/myspell/hyph_zu_ZA.dic
%dir %{_docdir}/myspell-zu_ZA
%{_docdir}/myspell-zu_ZA/description.xml
%{_docdir}/myspell-zu_ZA/dictionaries.xcu

%changelog
