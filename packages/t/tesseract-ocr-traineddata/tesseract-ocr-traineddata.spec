#
# spec file for package tesseract-ocr-traineddata
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           tesseract-ocr-traineddata
Version:        3.04.00
Release:        0
Summary:        Tesseract Traineddata for Various Languages
License:        Apache-2.0
Group:          Productivity/Graphics/Other
Url:            http://code.google.com/p/tesseract-ocr/
Source0:        https://github.com/tesseract-ocr/tessdata/archive/%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
A commercial quality OCR engine originally developed at HP between 1985 and
1995. In 1995, this engine was among the top 3 evaluated by UNLV. It was
open-sourced by HP and UNLV in 2005. From 2007 it is developed by Google.

%package afrikaans
Summary:        Afrikaans Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}
Obsoletes:      tesseract-traineddata-afrikaans <= 3.02

%description afrikaans
The Afrikaans traineddata for Tesseract.

%package albanian
Summary:        Albanian Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}
Obsoletes:      tesseract-traineddata-albanian <= 3.02

%description albanian
The Albanian traineddata for Tesseract.

%package amharic
Summary:        Amharic Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}

%description amharic
The Amharic traineddata for Tesseract.

%package arabic
Summary:        Arabic Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}
Obsoletes:      tesseract-traineddata-arabic <= 3.02

%description arabic
The Arabic traineddata for Tesseract.

%package assamese
Summary:        Assamese Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}

%description assamese
The Assamese traineddata for Tesseract.

%package azerbaijani
Summary:        Azerbaijani Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}
Obsoletes:      tesseract-traineddata-azerbaijani <= 3.02

%description azerbaijani
The Azerbaijani traineddata for Tesseract.

%package azerbaijani_cyrillic
Summary:        Azerbaijani (Cyrillic) Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}

%description azerbaijani_cyrillic
The Azerbaijani (Cyrillic) traineddata for Tesseract.

%package basque
Summary:        Basque Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}
Obsoletes:      tesseract-traineddata-basque <= 3.02

%description basque
The Basque traineddata for Tesseract.

%package belarusian
Summary:        Belarusian Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}
Obsoletes:      tesseract-traineddata-belarusian <= 3.02

%description belarusian
The Belarusian traineddata for Tesseract.

%package bengali
Summary:        Bengali Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}
Obsoletes:      tesseract-traineddata-bengali <= 3.02

%description bengali
The Bengali traineddata for Tesseract.

%package bosnian
Summary:        Bosnian Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}

%description bosnian
The Bosnian traineddata for Tesseract.

%package bulgarian
Summary:        Bulgarian Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}
Provides:       tesseract-traineddata-bul = 3.02
Obsoletes:      tesseract-traineddata-bul <= 3.00
Obsoletes:      tesseract-traineddata-bulgarian <= 3.02

%description bulgarian
The Bulgarian traineddata for Tesseract.

%package burmese
Summary:        Burmese Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}

%description burmese
The Burmese traineddata for Tesseract.

%package catalan
Summary:        Catalan Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}
Provides:       tesseract-traineddata-cat = 3.02
Obsoletes:      tesseract-traineddata-cat <= 3.00
Obsoletes:      tesseract-traineddata-catalan <= 3.02

%description catalan
The Catalan traineddata for Tesseract.

%package cebuano
Summary:        Cebuano Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}

%description cebuano
The Cebuano traineddata for Tesseract.

%package cherokee
Summary:        Cherokee Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}
Obsoletes:      tesseract-traineddata-cherokee <= 3.02

%description cherokee
The Cherokee traineddata for Tesseract.

%package chinese_simplified
Summary:        Chinese (Simplified) Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}
Provides:       tesseract-traineddata-chi_sim = 3.02
Obsoletes:      tesseract-traineddata-chi_sim <= 3.00
Obsoletes:      tesseract-traineddata-chinese_simplified <= 3.02

%description chinese_simplified
The Chinese (Simplified) traineddata for Tesseract.

%package chinese_traditional
Summary:        Chinese (Traditional) Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}
Provides:       tesseract-traineddata-chi_tra = 3.02
Obsoletes:      tesseract-traineddata-chi_tra <= 3.00
Obsoletes:      tesseract-traineddata-chinese_traditional <= 3.02

%description chinese_traditional
The Chinese (Traditional) traineddata for Tesseract.

%package croatian
Summary:        Croatian Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}
Obsoletes:      tesseract-traineddata-croatian <= 3.02

%description croatian
The Croatian traineddata for Tesseract.

%package czech
Summary:        Czech Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}
Provides:       tesseract-traineddata-ces = 3.02
Obsoletes:      tesseract-traineddata-ces <= 3.00
Obsoletes:      tesseract-traineddata-czech <= 3.02

%description czech
The Czech traineddata for Tesseract.

%package danish
Summary:        Danish and Danish (Fraktur) Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}
Provides:       tesseract-traineddata-dan = 3.02
Obsoletes:      tesseract-traineddata-dan <= 3.00
Provides:       tesseract-traineddata-danish_fraktur = 3.02
Obsoletes:      tesseract-traineddata-danish <= 3.02
Obsoletes:      tesseract-traineddata-danish_fraktur <= 3.00

%description danish
The Danish and Danish (Fraktur) traineddata for Tesseract.

%package dutch
Summary:        Dutch Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}
Provides:       tesseract-traineddata-nld = 3.02
Obsoletes:      tesseract-traineddata-dutch <= 3.02
Obsoletes:      tesseract-traineddata-nld <= 3.00

%description dutch
The Dutch traineddata for Tesseract.

%package dzongkha
Summary:        Dzongkha Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}

%description dzongkha
The Dzongkha traineddata for Tesseract.

%package english
Summary:        English Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}
Provides:       tesseract-traineddata-eng = 3.02
Obsoletes:      tesseract-ocr-traineddata-american <= 3.02
Obsoletes:      tesseract-traineddata-american <= 3.02
Obsoletes:      tesseract-traineddata-eng < 3.01

%description english
The English traineddata for Tesseract.

%package english_middle
Summary:        Middle English (1100-1500) Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}
Obsoletes:      tesseract-ocr-traineddata-english_middle_1100_to_1500 <= 3.02
Obsoletes:      tesseract-traineddata-english_middle_1100_to_1500 <= 3.02

%description english_middle
The Middle English (1100-1500) traineddata for Tesseract.

%package esperanto
Summary:        Esperanto Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}
Obsoletes:      tesseract-traineddata-esperanto <= 3.02

%description esperanto
The Esperanto traineddata for Tesseract.

%package estonian
Summary:        Estonian Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}
Obsoletes:      tesseract-traineddata-estonian <= 3.02

%description estonian
The Estonian traineddata for Tesseract.

%package finnish
Summary:        Finnish Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}
Provides:       tesseract-traineddata-fin = 3.02
Obsoletes:      tesseract-traineddata-fin <= 3.00
Obsoletes:      tesseract-traineddata-finnish <= 3.02

%description finnish
The Finnish traineddata for Tesseract.

%package frankish
Summary:        Frankish Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}
Obsoletes:      tesseract-traineddata-frankish <= 3.02

%description frankish
The Frankish traineddata for Tesseract.

%package french
Summary:        French Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}
Provides:       tesseract-traineddata-fra = 3.02
Obsoletes:      tesseract-traineddata-fra <= 3.00
Obsoletes:      tesseract-traineddata-french <= 3.02

%description french
The French traineddata for Tesseract.

%package french_middle
Summary:        Middle French (ca. 1400-1600) Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}
Obsoletes:      tesseract-ocr-traineddata-french_middle_1400_to_1600 <= 3.02
Obsoletes:      tesseract-traineddata-french_middle_1400_to_1600 <= 3.02

%description french_middle
The Middle French (ca. 1400-1600) traineddata for Tesseract.

%package galician
Summary:        Galician Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}
Obsoletes:      tesseract-traineddata-galician <= 3.02

%description galician
The Galician traineddata for Tesseract.

%package georgian
Summary:        Georgian Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}

%description georgian
The Georgian traineddata for Tesseract.

%package georgian_old
Summary:        Georgian (Old) Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}

%description georgian_old
The Georgian (Old) traineddata for Tesseract.

%package german
Summary:        German and German (Fraktur) Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}
Provides:       tesseract-traineddata-deu = 3.02
Obsoletes:      tesseract-traineddata-deu <= 3.00
Provides:       tesseract-traineddata-german_fraktur = 3.02
Obsoletes:      tesseract-traineddata-german <= 3.02
Obsoletes:      tesseract-traineddata-german_fraktur <= 3.00

%description german
The German and German (Fraktur) traineddata for Tesseract.

%package greek
Summary:        Greek Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}
Provides:       tesseract-traineddata-ell = 3.02
Obsoletes:      tesseract-traineddata-ell <= 3.00
Obsoletes:      tesseract-traineddata-greek <= 3.02

%description greek
The Greek traineddata for Tesseract.

%package greek_ancient
Summary:        Ancient Greek Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}
Obsoletes:      tesseract-traineddata-greek_ancient <= 3.02

%description greek_ancient
The Ancient Greek traineddata for Tesseract.

%package gujarati
Summary:        Gujarati Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}

%description gujarati
The Gujarati traineddata for Tesseract.

%package haitian
Summary:        Haitian Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}

%description haitian
The Haitian traineddata for Tesseract.

%package hebrew
Summary:        Hebrew Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}
Obsoletes:      tesseract-traineddata-hebrew <= 3.02

%description hebrew
The Hebrew traineddata for Tesseract.

%package hindi
Summary:        Hindi Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}
Obsoletes:      tesseract-traineddata-hindi <= 3.02

%description hindi
The Hindi traineddata for Tesseract.

%package hungarian
Summary:        Hungarian Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}
Provides:       tesseract-traineddata-hun = 3.02
Obsoletes:      tesseract-traineddata-hun <= 3.00
Obsoletes:      tesseract-traineddata-hungarian <= 3.02

%description hungarian
The Hungarian traineddata for Tesseract.

%package icelandic
Summary:        Icelandic Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}
Obsoletes:      tesseract-traineddata-icelandic <= 3.02

%description icelandic
The Icelandic traineddata for Tesseract.

%package indonese
Summary:        Indonese Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}
Provides:       tesseract-traineddata-ind = 3.02
Obsoletes:      tesseract-traineddata-ind <= 3.00
Obsoletes:      tesseract-traineddata-indonese <= 3.02

%description indonese
The Indonese traineddata for Tesseract.

%package inuktitut
Summary:        Inuktitut Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}

%description inuktitut
The Inuktitut traineddata for Tesseract.

%package irish
Summary:        Irish Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}

%description irish
The Irish traineddata for Tesseract.

%package italian
Summary:        Italian Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}
Provides:       tesseract-traineddata-ita = 3.02
Obsoletes:      tesseract-traineddata-ita <= 3.00
Obsoletes:      tesseract-traineddata-italian <= 3.02

%description italian
The Italian traineddata for Tesseract.

%package italian_old
Summary:        Italian (Old) Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}
Obsoletes:      tesseract-traineddata-italian_old <= 3.02

%description italian_old
The Italian (Old) traineddata for Tesseract.

%package japanese
Summary:        Japanese Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}
Provides:       tesseract-traineddata-jpn = 3.02
Obsoletes:      tesseract-traineddata-japanese <= 3.02
Obsoletes:      tesseract-traineddata-jpn <= 3.00

%description japanese
The Japanese traineddata for Tesseract.

%package javanese
Summary:        Javanese Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}

%description javanese
The Javanese traineddata for Tesseract.

%package kannada
Summary:        Kannada Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}
Obsoletes:      tesseract-traineddata-kannada <= 3.02

%description kannada
The Kannada traineddata for Tesseract.

%package kazakh
Summary:        Kazakh Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}

%description kazakh
The Kazakh traineddata for Tesseract.

%package khmer
Summary:        Khmer Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}

%description khmer
The Khmer traineddata for Tesseract.

%package korean
Summary:        Korean Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}
Provides:       tesseract-traineddata-kor = 3.02
Obsoletes:      tesseract-traineddata-kor <= 3.00
Obsoletes:      tesseract-traineddata-korean <= 3.02

%description korean
The Korean traineddata for Tesseract.

%package kurdish
Summary:        Kurdish Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}

%description kurdish
The Kurdish traineddata for Tesseract.

%package kyrgyz
Summary:        Kyrgyz Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}

%description kyrgyz
The Kyrgyz traineddata for Tesseract.

%package lao
Summary:        Lao Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}

%description lao
The Lao traineddata for Tesseract.

%package latin
Summary:        Latin Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}

%description latin
The Latin traineddata for Tesseract.

%package latvian
Summary:        Latvian Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}
Provides:       tesseract-traineddata-lav = 3.02
Obsoletes:      tesseract-traineddata-latvian <= 3.02
Obsoletes:      tesseract-traineddata-lav <= 3.00

%description latvian
The Latvian traineddata for Tesseract.

%package lithuanian
Summary:        Lithuanian Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}
Provides:       tesseract-traineddata-lit = 3.02
Obsoletes:      tesseract-traineddata-lit <= 3.00
Obsoletes:      tesseract-traineddata-lithuanian <= 3.02

%description lithuanian
The Lithuanian traineddata for Tesseract.

%package macedonian
Summary:        Macedonian Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}
Obsoletes:      tesseract-traineddata-macedonian <= 3.02

%description macedonian
The Macedonian traineddata for Tesseract.

%package malay
Summary:        Malay Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}
Obsoletes:      tesseract-traineddata-malay <= 3.02

%description malay
The Malay traineddata for Tesseract.

%package malayalam
Summary:        Malayalam Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}
Obsoletes:      tesseract-traineddata-malayalam <= 3.02

%description malayalam
The Malayalam traineddata for Tesseract.

%package maltese
Summary:        Maltese Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}
Obsoletes:      tesseract-traineddata-maltese <= 3.02

%description maltese
The Maltese traineddata for Tesseract.

%package marathi
Summary:        Marathi Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}

%description marathi
The Marathi traineddata for Tesseract.

%package math_equation
Summary:        Math / Equation Detection Module Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}
Obsoletes:      tesseract-traineddata-math_equation <= 3.02

%description math_equation
The Math / Equation Detection Module traineddata for Tesseract.

%package nepali
Summary:        Nepali Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}

%description nepali
The Nepali traineddata for Tesseract.

%package norwegian
Summary:        Norwegian Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}
Provides:       tesseract-traineddata-nor = 3.02
Obsoletes:      tesseract-traineddata-nor <= 3.00
Obsoletes:      tesseract-traineddata-norwegian <= 3.02

%description norwegian
The Norwegian traineddata for Tesseract.

%package orientation_and_script_detection
Summary:        Orientation & Script Detection Enabler Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}
Obsoletes:      tesseract-traineddata-orientation_and_script_detection <= 3.01

%description orientation_and_script_detection
The Orientation & Script Detection Enabler traineddata for Tesseract.

%package oriya
Summary:        Oriya Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}

%description oriya
The Oriya traineddata for Tesseract.

%package pashto
Summary:        Pashto Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}

%description pashto
The Pashto traineddata for Tesseract.

%package persian
Summary:        Persian Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}

%description persian
The Persian traineddata for Tesseract.

%package polish
Summary:        Polish Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}
Provides:       tesseract-traineddata-pol = 3.02
Obsoletes:      tesseract-traineddata-pol <= 3.00
Obsoletes:      tesseract-traineddata-polish <= 3.02

%description polish
The Polish traineddata for Tesseract.

%package portuguese
Summary:        Portuguese Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}
Provides:       tesseract-traineddata-por = 3.02
Obsoletes:      tesseract-traineddata-por <= 3.00
Obsoletes:      tesseract-traineddata-portuguese <= 3.02

%description portuguese
The Portuguese traineddata for Tesseract.

%package punjabi
Summary:        Punjabi Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}

%description punjabi
The Punjabi traineddata for Tesseract.

%package romanian
Summary:        Romanian Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}
Provides:       tesseract-traineddata-ron = 3.02
Obsoletes:      tesseract-traineddata-romanian <= 3.02
Obsoletes:      tesseract-traineddata-ron <= 3.00

%description romanian
The Romanian traineddata for Tesseract.

%package russian
Summary:        Russian Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}
Provides:       tesseract-traineddata-rus = 3.02
Obsoletes:      tesseract-traineddata-rus <= 3.00
Obsoletes:      tesseract-traineddata-russian <= 3.02

%description russian
The Russian traineddata for Tesseract.

%package sanskrit
Summary:        Sanskrit Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}

%description sanskrit
The Sanskrit traineddata for Tesseract.

%package serbian
Summary:        Serbian Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}
Provides:       tesseract-traineddata-srp = 3.02
Obsoletes:      tesseract-traineddata-srp <= 3.00

%description serbian
The Serbian traineddata for Tesseract.

%package serbian_latin
Summary:        Serbian (Latin) Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}
Obsoletes:      tesseract-traineddata-serbian_latin <= 3.02

%description serbian_latin
The Serbian (Latin) traineddata for Tesseract.

%package sinhala
Summary:        Sinhala Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}

%description sinhala
The Sinhala traineddata for Tesseract.

%package slovak
Summary:        Slovak and Slovak (Fraktur) Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}
Provides:       tesseract-traineddata-slk = 3.02
Obsoletes:      tesseract-traineddata-slk <= 3.00
Provides:       tesseract-traineddata-slovak_fraktur = 3.02
Obsoletes:      tesseract-traineddata-slovak <= 3.02
Obsoletes:      tesseract-traineddata-slovak_fraktur <= 3.01

%description slovak
The Slovak and Slovak (Fraktur) traineddata for Tesseract.

%package slovenian
Summary:        Slovenian Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}
Provides:       tesseract-traineddata-slv = 3.02
Obsoletes:      tesseract-traineddata-slovenian <= 3.02
Obsoletes:      tesseract-traineddata-slv <= 3.00

%description slovenian
The Slovenian traineddata for Tesseract.

%package spanish
Summary:        Spanish Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}
Provides:       tesseract-traineddata-spa = 3.02
Obsoletes:      tesseract-traineddata-spa <= 3.00
Obsoletes:      tesseract-traineddata-spanish <= 3.02

%description spanish
The Spanish traineddata for Tesseract.

%package spanish_old
Summary:        Spanish (Old) Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}
Obsoletes:      tesseract-traineddata-spanish_old <= 3.02

%description spanish_old
The Spanish (Old) traineddata for Tesseract.

%package swahili
Summary:        Swahili Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}
Obsoletes:      tesseract-traineddata-swahili <= 3.02

%description swahili
The Swahili traineddata for Tesseract.

%package swedish
Summary:        Swedish Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}
Provides:       tesseract-traineddata-swe = 3.02
Obsoletes:      tesseract-traineddata-swe <= 3.00
Obsoletes:      tesseract-traineddata-swedish <= 3.02

%description swedish
The Swedish traineddata for Tesseract.

%package syriac
Summary:        Syriac Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}

%description syriac
The Syriac traineddata for Tesseract.

%package tagalog
Summary:        Tagalog Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}
Provides:       tesseract-traineddata-tgl = 3.02
Obsoletes:      tesseract-traineddata-tagalog <= 3.02
Obsoletes:      tesseract-traineddata-tgl <= 3.00

%description tagalog
The Tagalog traineddata for Tesseract.

%package tajik
Summary:        Tajik Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}

%description tajik
The Tajik traineddata for Tesseract.

%package tamil
Summary:        Tamil Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}
Obsoletes:      tesseract-traineddata-tamil <= 3.02

%description tamil
The Tamil traineddata for Tesseract.

%package telugu
Summary:        Telugu Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}
Obsoletes:      tesseract-traineddata-telugu <= 3.02

%description telugu
The Telugu traineddata for Tesseract.

%package thai
Summary:        Thai Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}
Obsoletes:      tesseract-traineddata-thai <= 3.02

%description thai
The Thai traineddata for Tesseract.

%package tibetan_standard
Summary:        Tibetan Standard Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}

%description tibetan_standard
The Tibetan Standard traineddata for Tesseract.

%package tigrinya
Summary:        Tigrinya Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}

%description tigrinya
The Tigrinya traineddata for Tesseract.

%package turkish
Summary:        Turkish Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}
Provides:       tesseract-traineddata-tur = 3.02
Obsoletes:      tesseract-traineddata-tur <= 3.00
Obsoletes:      tesseract-traineddata-turkish <= 3.02

%description turkish
The Turkish traineddata for Tesseract.

%package ukrainian
Summary:        Ukrainian Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}
Provides:       tesseract-traineddata-ukr = 3.02
Obsoletes:      tesseract-traineddata-ukr <= 3.00
Obsoletes:      tesseract-traineddata-ukrainian <= 3.02

%description ukrainian
The Ukrainian traineddata for Tesseract.

%package urdu
Summary:        Urdu Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}

%description urdu
The Urdu traineddata for Tesseract.

%package uyghur
Summary:        Uyghur Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}

%description uyghur
The Uyghur traineddata for Tesseract.

%package uzbek
Summary:        Uzbek Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}

%description uzbek
The Uzbek traineddata for Tesseract.

%package uzbek_cyrillic
Summary:        Uzbek (Cyrillic) Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}

%description uzbek_cyrillic
The Uzbek (Cyrillic) traineddata for Tesseract.

%package vietnamese
Summary:        Vietnamese Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}
Provides:       tesseract-traineddata-vie = 3.02
Obsoletes:      tesseract-traineddata-vie <= 3.00
Obsoletes:      tesseract-traineddata-vietnamese <= 3.02

%description vietnamese
The Vietnamese traineddata for Tesseract.

%package welsh
Summary:        Welsh Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}

%description welsh
The Welsh traineddata for Tesseract.

%package yiddish
Summary:        Yiddish Traineddata for Tesseract
Group:          Productivity/Graphics/Other
Requires:       tesseract-ocr >= %{version}

%description yiddish
The Yiddish traineddata for Tesseract.

%prep
%setup -q -n tessdata-%{version}

%build

%install
install -pm 0755 -d %{buildroot}%{_datadir}/tessdata/
install -pm 0644 * %{buildroot}%{_datadir}/tessdata/

%files afrikaans
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/afr.*

%files albanian
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/sqi.*

%files amharic
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/amh.*

%files arabic
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/ara.*

%files assamese
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/asm.*

%files azerbaijani
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/aze.*

%files azerbaijani_cyrillic
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/aze_cyrl.*

%files basque
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/eus.*

%files belarusian
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/bel.*

%files bengali
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/ben.*

%files bosnian
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/bos.*

%files bulgarian
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/bul.*

%files burmese
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/mya.*

%files catalan
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/cat.*

%files cebuano
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/ceb.*

%files cherokee
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/chr.*

%files chinese_simplified
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/chi_sim.*

%files chinese_traditional
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/chi_tra.*

%files croatian
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/hrv.*

%files czech
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/ces.*

%files danish
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/dan.*
%{_datadir}/tessdata/dan_frak.*

%files dutch
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/nld.*

%files dzongkha
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/dzo.*

%files english
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/eng.*

%files english_middle
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/enm.*

%files esperanto
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/epo.*

%files estonian
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/est.*

%files finnish
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/fin.*

%files frankish
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/frk.*

%files french
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/fra.*

%files french_middle
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/frm.*

%files galician
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/glg.*

%files georgian
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/kat.*

%files georgian_old
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/kat_old.*

%files german
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/deu.*
%{_datadir}/tessdata/deu_frak.*

%files greek
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/ell.*

%files greek_ancient
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/grc.*

%files gujarati
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/guj.*

%files haitian
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/hat.*

%files hebrew
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/heb.*

%files hindi
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/hin.*

%files hungarian
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/hun.*

%files icelandic
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/isl.*

%files indonese
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/ind.*

%files inuktitut
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/iku.*

%files irish
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/gle.*

%files italian
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/ita.*

%files italian_old
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/ita_old.*

%files japanese
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/jpn.*

%files javanese
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/jav.*

%files kannada
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/kan.*

%files kazakh
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/kaz.*

%files khmer
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/khm.*

%files korean
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/kor.*

%files kurdish
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/kur.*

%files kyrgyz
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/kir.*

%files lao
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/lao.*

%files latin
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/lat.*

%files latvian
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/lav.*

%files lithuanian
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/lit.*

%files macedonian
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/mkd.*

%files malay
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/msa.*

%files malayalam
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/mal.*

%files maltese
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/mlt.*

%files marathi
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/mar.*

%files math_equation
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/equ.*

%files nepali
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/nep.*

%files norwegian
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/nor.*

%files orientation_and_script_detection
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/osd.*

%files oriya
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/ori.*

%files pashto
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/pus.*

%files persian
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/fas.*

%files polish
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/pol.*

%files portuguese
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/por.*

%files punjabi
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/pan.*

%files romanian
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/ron.*

%files russian
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/rus.*

%files sanskrit
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/san.*

%files serbian
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/srp.*

%files serbian_latin
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/srp_latn.*

%files sinhala
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/sin.*

%files slovak
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/slk.*
%{_datadir}/tessdata/slk_frak.*

%files slovenian
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/slv.*

%files spanish
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/spa.*

%files spanish_old
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/spa_old.*

%files swahili
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/swa.*

%files swedish
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/swe.*

%files syriac
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/syr.*

%files tagalog
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/tgl.*

%files tajik
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/tgk.*

%files tamil
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/tam.*

%files telugu
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/tel.*

%files thai
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/tha.*

%files tibetan_standard
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/bod.*

%files tigrinya
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/tir.*

%files turkish
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/tur.*

%files ukrainian
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/ukr.*

%files urdu
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/urd.*

%files uyghur
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/uig.*

%files uzbek
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/uzb.*

%files uzbek_cyrillic
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/uzb_cyrl.*

%files vietnamese
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/vie.*

%files welsh
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/cym.*

%files yiddish
%defattr(-,root,root,-)
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/yid.*

%changelog
