#
# spec file for package tesseract-ocr-traineddata
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           tesseract-ocr-traineddata
Version:        4.1.0+git.20240801.8741641
Release:        0
Summary:        Tesseract Traineddata for Various Languages
License:        Apache-2.0
URL:            https://github.com/tesseract-ocr
Source0:        tessdata_fast-%{version}.tar.xz
BuildRequires:  python3-packaging
BuildArch:      noarch

%description
This package contains fast integer versions of trained models for the Tesseract
Open Source OCR Engine.

These models only work with the LSTM OCR engine of Tesseract 4.

%package        doc
Summary:        Documentation for %{name}

%description    doc
The %{name}-doc package contains the documentation for %{name}.

%package        osd
Summary:        Orientation & Script Detection Data for tesseract
Requires:       tesseract-ocr >= %{version}
Provides:       tesseract-ocr-traineddata-orientation_and_script_detection = %{version}
Obsoletes:      tesseract-ocr-traineddata-orientation_and_script_detection < 4
Obsoletes:      tesseract-traineddata-orientation_and_script_detection <= 3.02
BuildArch:      noarch

%description    osd
Orientation & Script Detection data for the Tesseract Open Source OCR Engine.

%package        equ
Summary:        Orientation & Script Detection Data for tesseract
Requires:       tesseract-ocr >= %{version}
Provides:       tesseract-ocr-traineddata-math_equation = %{version}
Obsoletes:      tesseract-ocr-traineddata-math_equation < 4
Obsoletes:      tesseract-traineddata-math_equation <= 3.02
BuildArch:      noarch

%description   equ
Math equation data for the Tesseract Open Source OCR Engine.
# define lang_subpkg macro
# m: 3 letter macrolanguage code
# l: langcode used in Provides and Supplements tags
# n: language name
# o: old language name
# -m and -n is needed for subpackages
#
%define lang_subpkg(m:l:n:o:) \
%define macrolang %{-m:%{-m*}}%{!-m:%{error:3 letter Language code not defined}} \
%define langcode %{-l:%{-l*}} \
%define langname %{-n:%{-n*}}%{!-n:%{error:Language name not defined}} \
%define oldlangname %{-o:%{-o*}} \
\
%package       %{macrolang}\
Summary:       %{langname} language data for %{name}\
BuildArch:     noarch\
Requires:      (tesseract-ocr >= %{version} or libtesseract5 >= %{version})\
Provides:      tesseract-ocr-traineddata-%{oldlangname} = %{version} \
Provides:      tesseract-ocr-traineddata-provider = %{version} \
Provides:      tesseract-traineddata-%{oldlangname} = %{version} \
Obsoletes:     tesseract-ocr-traineddata-%{oldlangname} < 4\
Obsoletes:     tesseract-traineddata-%{oldlangname} <= 3.02\
%if "%{?langcode:%{langcode}}" != ""\
Provides:      locale(tesseract-ocr-common:%{langcode})\
%endif\
\
%description   %{macrolang}\
This package contains the fast integer version of the %{langname} language \
trained models for the Tesseract Open Source OCR Engine.\
\
%files %{macrolang}\
%dir %{_datadir}/tessdata\
%{_datadir}/tessdata/%{macrolang}.*
# define script_subpkg macro
# s: script name
# n: package name
#
%define script_subpkg(s:n:) \
%define scriptname %{-s:%{-s*}}%{!-s:%{error:Script name defined}} \
%define filename %{-n:%{-n*}}%{!-n:%{error:Package name not defined}} \
%define pkgname %(echo %{filename} | tr '[:upper:]' '[:lower:]') \
\
%package       script-%{pkgname}\
Summary:       %{scriptname} script data for %{name}\
BuildArch:     noarch\
Requires:      tesseract-ocr >= %{version}\
\
%description   script-%{pkgname}\
This package contains the fast integer version of the %{scriptname} script \
trained models for the Tesseract Open Source OCR Engine.\
\
%files script-%{pkgname}\
%dir %{_datadir}/tessdata/\
%dir %{_datadir}/tessdata/script/\
%{_datadir}/tessdata/script/%{filename}.*
# see https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
# and https://en.wikipedia.org/wiki/List_of_ISO_639-2_codes
%lang_subpkg -m afr -l af -n Afrikaans -o afrikaans
%lang_subpkg -m amh -l an -n Amharic -o amharic
%lang_subpkg -m ara -l ar -n Arabic -o arabic
%lang_subpkg -m asm -l as -n Assamese -o assamese
%lang_subpkg -m aze -l az -n Azerbaijani -o azerbaijani
%lang_subpkg -m aze_cyrl -n %{quote:Azerbaijani (Cyrillic)} -o azerbaijani_cyrillic
%lang_subpkg -m bel -l bel -n Belarusian -o belarusian
%lang_subpkg -m ben -l bn -n Bengali -o bengali
%lang_subpkg -m bod -l bo -n %{quote:Tibetan (Standard)} -o tibetan_standard
%lang_subpkg -m bos -l bs -n Bosnian -o bosnian
%lang_subpkg -m bre -l br -n Breton -o breton
%lang_subpkg -m bul -l bg -n Bulgarian -o bulgarian
%lang_subpkg -m cat -l ca -n Catalan -o catalan
%lang_subpkg -m ceb -n Cebuano -o cebuano
%lang_subpkg -m ces -l cs -n Czech -o czech
%lang_subpkg -m chi_sim -l zh_CN -n %{quote:Chinese (Simplified)} -o chinese_simplified
%lang_subpkg -m chi_sim_vert -l zh_CN -n %{quote:Chinese (Simplified, Vertical)} -o chinese_simplified_vertical
%lang_subpkg -m chi_tra -l zh_TW -n %{quote:Chinese (Traditional)} -o chinese_traditional
%lang_subpkg -m chi_tra_vert -l zh_TW -n %{quote:Chinese (Traditional, Vertical)} -o chinese_traditional_vertical
%lang_subpkg -m chr -n Cherokee -o cherokee
%lang_subpkg -m cos -l co -n Corsican -o corsican
%lang_subpkg -m cym -l cy -n Welsh -o welsh
%lang_subpkg -m dan -l da -n Danish -o danish
%lang_subpkg -m deu -l de -n German -o german
%lang_subpkg -m div -l dv -n %{quote:Dhivehi; Maldivian} -o dhivehi
%lang_subpkg -m dzo -n Dzongkha -o dzongkha
%lang_subpkg -m ell -l el -n Greek -o greek
%lang_subpkg -m eng -n English -o english
%lang_subpkg -m enm -n %{quote:Middle English (1100-1500)} -o english_middle
%lang_subpkg -m epo -l eo -n Esperanto -o esperanto
%lang_subpkg -m est -l et -n Estonian -o estonian
%lang_subpkg -m eus -l eu -n Basque -o basque
%lang_subpkg -m fao -l fo -n %{quote:Faroese} -o faroese
%lang_subpkg -m fas -l fa -n %{quote:Persian (Farsi)} -o persian
%lang_subpkg -m fil -n %{quote:Filipino; Pilipino} -o filipino
%lang_subpkg -m fin -l fi -n Finnish -o finnish
%lang_subpkg -m fra -l fr -n French -o french
%lang_subpkg -m deu_latf -n Fraktur -o frankish
%lang_subpkg -m frk -n Fraktur -o frankish
%lang_subpkg -m frm -n %{quote:Middle French (ca. 1400-1600)} -o french_middle
%lang_subpkg -m fry -l fy -n %{quote:Western Frisian} -o frisian
%lang_subpkg -m gla -l gd -n %{quote:Gaelic; Scottish Gaelic} -o gaelic
%lang_subpkg -m gle -l ga -n Irish -o irish
%lang_subpkg -m glg -l gl -n Galician -o galician
%lang_subpkg -m grc -n %{quote:Ancient Greek} -o greek_ancient
%lang_subpkg -m guj -l gu -n Gujarati -o gujarati
%lang_subpkg -m hat -l ht -n Haitian -o haitian
%lang_subpkg -m heb -l he -n Hebrew -o hebrew
%lang_subpkg -m hin -l hi -n Hindi -o hindi
%lang_subpkg -m hrv -l hr -n Croatian -o croatian
%lang_subpkg -m hun -l hu -n Hungarian -o hungarian
%lang_subpkg -m hye -l hy -n Armenian -o armenian
%lang_subpkg -m iku -l iu -n Inuktitut -o inuktitut
%lang_subpkg -m ind -l id -n Indonesian -o indonese
%lang_subpkg -m isl -l is -n Icelandic -o icelandic
%lang_subpkg -m ita -l it -n Italian -o italian
%lang_subpkg -m ita_old -n %{quote:Italian (Old)} -o italian_old
%lang_subpkg -m jav -l jav -n Javanese -o javanese
%lang_subpkg -m jpn -l ja -n Japanese -o japanese
%lang_subpkg -m jpn_vert -l ja -n "Japanese (Vertical)" -o japanese_vertical
%lang_subpkg -m kan -l kn -n Kannada -o kannada
%lang_subpkg -m kat -l ka -n Georgian -o georgian
%lang_subpkg -m kat_old -n %{quote:Georgian (Old)} -o georgian_old
%lang_subpkg -m kaz -l kk -n Kazakh -o kazakh
%lang_subpkg -m khm -l km -n Khmer -o khmer
%lang_subpkg -m kir -l ky -n Kyrgyz -o kyrgyz
%lang_subpkg -m kor -l ko -n Korean -o korean
%lang_subpkg -m kor_vert -l ko -n "Korean (Vertical)" -o korean_vertical
%lang_subpkg -m kmr -l ku -n Kurmanji -o kurmanji
%lang_subpkg -m lao -l lo -n Lao -o lao
%lang_subpkg -m lat -l lat -n Latin -o latin
%lang_subpkg -m lav -l lv -n Latvian -o latvian
%lang_subpkg -m lit -l lt -n Lithuanian -o lithuanian
%lang_subpkg -m ltz -l lb -n Luxembourgish -o luxembourgish
%lang_subpkg -m mal -l ml -n Malayalam -o malayalam
%lang_subpkg -m mar -l mr -n Marathi -o marathi
%lang_subpkg -m mkd -l mk -n Macedonian -o macedonian
%lang_subpkg -m mlt -l mt -n Maltese -o maltese
%lang_subpkg -m mon -l mn -n Mongolian -o mongolian
%lang_subpkg -m mri -l mi -n Maori -o maori
%lang_subpkg -m msa -l ms -n Malay -o malay
%lang_subpkg -m mya -l my -n Burmese -o burmese
%lang_subpkg -m nep -l ne -n Nepali -o nepali
%lang_subpkg -m nld -l nl -n Dutch -o dutch
%lang_subpkg -m nor -l no -n Norwegian -o norwegian
%lang_subpkg -m oci -l oc -n Occitan -o occitan
%lang_subpkg -m ori -l or -n Oriya -o oriya
%lang_subpkg -m pan -l pa -n Panjabi -o punjabi
%lang_subpkg -m pol -l pl -n Polish -o polish
%lang_subpkg -m por -l pt -n Portuguese -o portuguese
%lang_subpkg -m pus -l ps -n Pashto -o pashto
%lang_subpkg -m que -l qu -n Quechuan -o quechuan
%lang_subpkg -m ron -l ro -n Romanian -o romanian
%lang_subpkg -m rus -l ru -n Russian -o russian
%lang_subpkg -m san -l sa -n Sanskrit -o sanskrit
%lang_subpkg -m sin -l si -n Sinhala -o sinhala
%lang_subpkg -m slk -l sk -n Slovakian -o slovak
%lang_subpkg -m slv -l sl -n Slovenian -o slovenian
%lang_subpkg -m snd -l sd -n Sindhi -o sindhi
%lang_subpkg -m spa -l es -n Spanish -o spanish
%lang_subpkg -m spa_old -n %{quote:Spanish (Old)} -o spanish_old
%lang_subpkg -m sqi -l sq -n Albanian -o albanian
%lang_subpkg -m srp -l sr -n Serbian -o serbian
%lang_subpkg -m srp_latn -n %{quote:Serbian (Latin)} -o serbian_latin
%lang_subpkg -m sun -l su -n Sundanese -o sundanese
%lang_subpkg -m swa -l sw -n Swahili -o swahili
%lang_subpkg -m swe -l sv -n Swedish -o swedish
%lang_subpkg -m syr -l ar_SY -n Syriac -o syriac
%lang_subpkg -m tam -l ta -n Tamil -o tamil
%lang_subpkg -m tat -l tt -n Tatar -o tatar
%lang_subpkg -m tel -l te -n Telugu -o telugu
%lang_subpkg -m tgk -l tg -n Tajik -o tajik
%lang_subpkg -m tha -l th -n Thai -o thai
%lang_subpkg -m tir -l ti -n Tigrinya -o tigrinya
%lang_subpkg -m ton -l to -n Tongan -o tongan
%lang_subpkg -m tur -l tr -n Turkish -o turkish
%lang_subpkg -m uig -l ug -n Uyghur -o uyghur
%lang_subpkg -m ukr -l uk -n Ukrainian -o ukrainian
%lang_subpkg -m urd -l ur -n Urdu -o urdu
%lang_subpkg -m uzb -l uz -n Uzbek -o uzbek
%lang_subpkg -m uzb_cyrl -n %{quote:Uzbek (Cyrillic)} -o uzbek_cyrillic
%lang_subpkg -m vie -l vi -n Vietnamese -o vietnamese
%lang_subpkg -m yid -l yi -n Yiddish -o yiddish
%lang_subpkg -m yor -l yo -n Yoruba -o yoruba
%script_subpkg -n Arabic -s Arabic
%script_subpkg -n Armenian -s Armenian
%script_subpkg -n Bengali -s Bengali
%script_subpkg -n Canadian_Aboriginal -s %{quote:Canadian (Aboriginal)}
%script_subpkg -n Cherokee -s Cherokee
%script_subpkg -n Cyrillic -s Cyrillic
%script_subpkg -n Devanagari -s Devanagari
%script_subpkg -n Ethiopic -s Ethiopic
%script_subpkg -n Fraktur -s Fraktur
%script_subpkg -n Georgian -s Georgian
%script_subpkg -n Greek -s Greek
%script_subpkg -n Gujarati -s Gujarati
%script_subpkg -n Gurmukhi -s Gurmukhi
%script_subpkg -n HanS -s %{quote:Han (Simplified)}
%script_subpkg -n HanS_vert -s %{quote:Han (Simplified, Vertical)}
%script_subpkg -n HanT -s %{quote:Han (Traditional)}
%script_subpkg -n HanT_vert -s %{quote:Han (Traditional, Vertical)}
%script_subpkg -n Hangul -s Hangul
%script_subpkg -n Hangul_vert -s %{quote:Hangul (Vertical)}
%script_subpkg -n Hebrew -s Hebrew
%script_subpkg -n Japanese -s Japanese
%script_subpkg -n Japanese_vert -s %{quote:Japanese (Vertical)}
%script_subpkg -n Kannada -s Kannada
%script_subpkg -n Khmer -s Khmer
%script_subpkg -n Lao -s Lao
%script_subpkg -n Latin -s Latin
%script_subpkg -n Malayalam -s Malayalam
%script_subpkg -n Myanmar -s Myanmar
%script_subpkg -n Oriya -s Oriya
%script_subpkg -n Sinhala -s Sinhala
%script_subpkg -n Syriac -s Syriac
%script_subpkg -n Tamil -s Tamil
%script_subpkg -n Telugu -s Telugu
%script_subpkg -n Thaana -s Thaana
%script_subpkg -n Thai -s Thai
%script_subpkg -n Tibetan -s Tibetan
%script_subpkg -n Vietnamese -s Vietnamese

%prep
%autosetup -n tessdata_fast-%{version}

%build

%install
mkdir -p %{buildroot}/%{_datadir}/tessdata/
cp -a *.traineddata %{buildroot}/%{_datadir}/tessdata/
cp -r script %{buildroot}/%{_datadir}/tessdata

%files doc
%license LICENSE
%doc README.md

%files equ
%{_datadir}/tessdata/equ.traineddata

%files osd
%{_datadir}/tessdata/osd.traineddata

%changelog
