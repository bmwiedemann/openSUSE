#
# spec file for package google-noto-fonts
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define hyear     2017
%define hmonth    09
%define hday      19
%define src_name  NotoFonts

# DO NOT EDIT THIS SPECFILE DIRECTLY, edit google-noto-fonts.spec.in and run generate-specfile.sh script

Name:           google-noto-fonts
Version:        %{hyear}%{hmonth}%{hday}
Release:        0
Summary:        Noto Font Families
License:        OFL-1.1
Group:          System/X11/Fonts
Url:            https://github.com/googlei18n/noto-fonts
Source0:        https://noto-website-2.storage.googleapis.com/pkgs/Noto-hinted.zip
Source1:        generate-specfile.sh
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Noto's design goal is to achieve visual harmonization (e.g., compatible heights and stroke 
thicknesses) across languages. 

%package doc
Summary:        Noto Font Families License
Group:          Documentation/Other

%description doc
License for Google's Noto fonts.

%package -n noto-kufiarabic-fonts
Summary:        Noto Kufi Arabic Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-kufiarabic
Provides:       noto-kufiarabic
%reconfigure_fonts_prereq

%description -n noto-kufiarabic-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
KufiArabic font, hinted.

%package -n noto-mono-fonts
Summary:        Noto Mono Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-mono
Provides:       noto-mono
%reconfigure_fonts_prereq

%description -n noto-mono-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Mono font, hinted.

%package -n noto-naskharabic-fonts
Summary:        Noto Naskh Arabic Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-naskharabic
Provides:       noto-naskharabic
%reconfigure_fonts_prereq

%description -n noto-naskharabic-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
NaskhArabic font, hinted.

%package -n noto-naskharabic-ui-fonts
Summary:        Noto Naskh Arabic Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-naskharabic-ui
Provides:       noto-naskharabic-ui
%reconfigure_fonts_prereq

%description -n noto-naskharabic-ui-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
NaskhArabic font, hinted.

%package -n noto-nastaliqurdu-fonts
Summary:        Noto Nastaliq Urdu Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-nastaliqurdu
Provides:       noto-nastaliqurdu
%reconfigure_fonts_prereq

%description -n noto-nastaliqurdu-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
NastaliqUrdu font, hinted.

%package -n noto-sans-fonts
Summary:        Noto Sans Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans
Provides:       noto-sans
%reconfigure_fonts_prereq

%description -n noto-sans-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Sans font, hinted.

%package -n noto-sans-adlam-fonts
Summary:        Noto Adlam Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-adlam
Provides:       noto-sans-adlam
%reconfigure_fonts_prereq

%description -n noto-sans-adlam-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Adlam Sans Serif font, hinted.

%package -n noto-sans-adlamunjoined-fonts
Summary:        Noto Adlam Unjoined Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-adlamunjoined
Provides:       noto-sans-adlamunjoined
%reconfigure_fonts_prereq

%description -n noto-sans-adlamunjoined-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
AdlamUnjoined Sans Serif font, hinted.

%package -n noto-sans-anatolianhieroglyphs-fonts
Summary:        Noto Anatolian Hieroglyphs Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-anatolianhieroglyphs
Provides:       noto-sans-anatolianhieroglyphs
%reconfigure_fonts_prereq

%description -n noto-sans-anatolianhieroglyphs-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
AnatolianHieroglyphs Sans Serif font, hinted.

%package -n noto-sans-arabic-fonts
Summary:        Noto Arabic Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-arabic
Provides:       noto-sans-arabic
%reconfigure_fonts_prereq

%description -n noto-sans-arabic-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Arabic Sans Serif font, hinted.

%package -n noto-sans-arabic-ui-fonts
Summary:        Noto Arabic Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-arabic-ui
Provides:       noto-sans-arabic-ui
%reconfigure_fonts_prereq

%description -n noto-sans-arabic-ui-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Arabic Sans Serif font, hinted.

%package -n noto-sans-armenian-fonts
Summary:        Noto Armenian Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-armenian
Provides:       noto-sans-armenian
%reconfigure_fonts_prereq

%description -n noto-sans-armenian-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Armenian Sans Serif font, hinted.

%package -n noto-sans-avestan-fonts
Summary:        Noto Avestan Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-avestan
Provides:       noto-sans-avestan
%reconfigure_fonts_prereq

%description -n noto-sans-avestan-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Avestan Sans Serif font, hinted.

%package -n noto-sans-balinese-fonts
Summary:        Noto Balinese Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-balinese
Provides:       noto-sans-balinese
%reconfigure_fonts_prereq

%description -n noto-sans-balinese-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Balinese Sans Serif font, hinted.

%package -n noto-sans-bamum-fonts
Summary:        Noto Bamum Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-bamum
Provides:       noto-sans-bamum
%reconfigure_fonts_prereq

%description -n noto-sans-bamum-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Bamum Sans Serif font, hinted.

%package -n noto-sans-batak-fonts
Summary:        Noto Batak Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-batak
Provides:       noto-sans-batak
%reconfigure_fonts_prereq

%description -n noto-sans-batak-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Batak Sans Serif font, hinted.

%package -n noto-sans-bengali-fonts
Summary:        Noto Bengali Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-bengali
Provides:       noto-sans-bengali
%reconfigure_fonts_prereq

%description -n noto-sans-bengali-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Bengali Sans Serif font, hinted.

%package -n noto-sans-bengali-ui-fonts
Summary:        Noto Bengali Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-bengali-ui
Provides:       noto-sans-bengali-ui
%reconfigure_fonts_prereq

%description -n noto-sans-bengali-ui-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Bengali Sans Serif font, hinted.

%package -n noto-sans-brahmi-fonts
Summary:        Noto Brahmi Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-brahmi
Provides:       noto-sans-brahmi
%reconfigure_fonts_prereq

%description -n noto-sans-brahmi-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Brahmi Sans Serif font, hinted.

%package -n noto-sans-buginese-fonts
Summary:        Noto Buginese Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-buginese
Provides:       noto-sans-buginese
%reconfigure_fonts_prereq

%description -n noto-sans-buginese-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Buginese Sans Serif font, hinted.

%package -n noto-sans-buhid-fonts
Summary:        Noto Buhid Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-buhid
Provides:       noto-sans-buhid
%reconfigure_fonts_prereq

%description -n noto-sans-buhid-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Buhid Sans Serif font, hinted.

%package -n noto-sans-canadianaboriginal-fonts
Summary:        Noto Canadian Aboriginal Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-canadianaboriginal
Provides:       noto-sans-canadianaboriginal
%reconfigure_fonts_prereq

%description -n noto-sans-canadianaboriginal-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
CanadianAboriginal Sans Serif font, hinted.

%package -n noto-sans-carian-fonts
Summary:        Noto Carian Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-carian
Provides:       noto-sans-carian
%reconfigure_fonts_prereq

%description -n noto-sans-carian-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Carian Sans Serif font, hinted.

%package -n noto-sans-chakma-fonts
Summary:        Noto Chakma Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-chakma
Provides:       noto-sans-chakma
%reconfigure_fonts_prereq

%description -n noto-sans-chakma-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Chakma Sans Serif font, hinted.

%package -n noto-sans-cham-fonts
Summary:        Noto Cham Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-cham
Provides:       noto-sans-cham
%reconfigure_fonts_prereq

%description -n noto-sans-cham-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Cham Sans Serif font, hinted.

%package -n noto-sans-cherokee-fonts
Summary:        Noto Cherokee Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-cherokee
Provides:       noto-sans-cherokee
%reconfigure_fonts_prereq

%description -n noto-sans-cherokee-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Cherokee Sans Serif font, hinted.

%package -n noto-sans-coptic-fonts
Summary:        Noto Coptic Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-coptic
Provides:       noto-sans-coptic
%reconfigure_fonts_prereq

%description -n noto-sans-coptic-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Coptic Sans Serif font, hinted.

%package -n noto-sans-cuneiform-fonts
Summary:        Noto Cuneiform Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-cuneiform
Provides:       noto-sans-cuneiform
%reconfigure_fonts_prereq

%description -n noto-sans-cuneiform-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Cuneiform Sans Serif font, hinted.

%package -n noto-sans-cypriot-fonts
Summary:        Noto Cypriot Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-cypriot
Provides:       noto-sans-cypriot
%reconfigure_fonts_prereq

%description -n noto-sans-cypriot-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Cypriot Sans Serif font, hinted.

%package -n noto-sans-deseret-fonts
Summary:        Noto Deseret Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-deseret
Provides:       noto-sans-deseret
%reconfigure_fonts_prereq

%description -n noto-sans-deseret-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Deseret Sans Serif font, hinted.

%package -n noto-sans-devanagari-fonts
Summary:        Noto Devanagari Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-devanagari
Provides:       noto-sans-devanagari
%reconfigure_fonts_prereq

%description -n noto-sans-devanagari-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Devanagari Sans Serif font, hinted.

%package -n noto-sans-devanagari-ui-fonts
Summary:        Noto Devanagari Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-devanagari-ui
Provides:       noto-sans-devanagari-ui
%reconfigure_fonts_prereq

%description -n noto-sans-devanagari-ui-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Devanagari Sans Serif font, hinted.

%package -n noto-sans-display-fonts
Summary:        Noto Display Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-display
Provides:       noto-sans-display
%reconfigure_fonts_prereq

%description -n noto-sans-display-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Display Sans Serif font, hinted.

%package -n noto-sans-egyptianhieroglyphs-fonts
Summary:        Noto Egyptian Hieroglyphs Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-egyptianhieroglyphs
Provides:       noto-sans-egyptianhieroglyphs
%reconfigure_fonts_prereq

%description -n noto-sans-egyptianhieroglyphs-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
EgyptianHieroglyphs Sans Serif font, hinted.

%package -n noto-sans-ethiopic-fonts
Summary:        Noto Ethiopic Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-ethiopic
Provides:       noto-sans-ethiopic
%reconfigure_fonts_prereq

%description -n noto-sans-ethiopic-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Ethiopic Sans Serif font, hinted.

%package -n noto-sans-georgian-fonts
Summary:        Noto Georgian Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-georgian
Provides:       noto-sans-georgian
%reconfigure_fonts_prereq

%description -n noto-sans-georgian-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Georgian Sans Serif font, hinted.

%package -n noto-sans-glagolitic-fonts
Summary:        Noto Glagolitic Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-glagolitic
Provides:       noto-sans-glagolitic
%reconfigure_fonts_prereq

%description -n noto-sans-glagolitic-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Glagolitic Sans Serif font, hinted.

%package -n noto-sans-gothic-fonts
Summary:        Noto Gothic Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-gothic
Provides:       noto-sans-gothic
%reconfigure_fonts_prereq

%description -n noto-sans-gothic-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Gothic Sans Serif font, hinted.

%package -n noto-sans-gujarati-fonts
Summary:        Noto Gujarati Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-gujarati
Provides:       noto-sans-gujarati
%reconfigure_fonts_prereq

%description -n noto-sans-gujarati-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Gujarati Sans Serif font, hinted.

%package -n noto-sans-gujarati-ui-fonts
Summary:        Noto Gujarati Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-gujarati-ui
Provides:       noto-sans-gujarati-ui
%reconfigure_fonts_prereq

%description -n noto-sans-gujarati-ui-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Gujarati Sans Serif font, hinted.

%package -n noto-sans-gurmukhi-fonts
Summary:        Noto Gurmukhi Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-gurmukhi
Provides:       noto-sans-gurmukhi
%reconfigure_fonts_prereq

%description -n noto-sans-gurmukhi-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Gurmukhi Sans Serif font, hinted.

%package -n noto-sans-gurmukhi-ui-fonts
Summary:        Noto Gurmukhi Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-gurmukhi-ui
Provides:       noto-sans-gurmukhi-ui
%reconfigure_fonts_prereq

%description -n noto-sans-gurmukhi-ui-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Gurmukhi Sans Serif font, hinted.

%package -n noto-sans-hanunoo-fonts
Summary:        Noto Hanunoo Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-hanunoo
Provides:       noto-sans-hanunoo
%reconfigure_fonts_prereq

%description -n noto-sans-hanunoo-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Hanunoo Sans Serif font, hinted.

%package -n noto-sans-hebrew-fonts
Summary:        Noto Hebrew Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-hebrew
Provides:       noto-sans-hebrew
%reconfigure_fonts_prereq

%description -n noto-sans-hebrew-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Hebrew Sans Serif font, hinted.

%package -n noto-sans-imperialaramaic-fonts
Summary:        Noto Imperial Aramaic Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-imperialaramaic
Provides:       noto-sans-imperialaramaic
%reconfigure_fonts_prereq

%description -n noto-sans-imperialaramaic-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
ImperialAramaic Sans Serif font, hinted.

%package -n noto-sans-inscriptionalpahlavi-fonts
Summary:        Noto Inscriptional Pahlavi Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-inscriptionalpahlavi
Provides:       noto-sans-inscriptionalpahlavi
%reconfigure_fonts_prereq

%description -n noto-sans-inscriptionalpahlavi-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
InscriptionalPahlavi Sans Serif font, hinted.

%package -n noto-sans-inscriptionalparthian-fonts
Summary:        Noto Inscriptional Parthian Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-inscriptionalparthian
Provides:       noto-sans-inscriptionalparthian
%reconfigure_fonts_prereq

%description -n noto-sans-inscriptionalparthian-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
InscriptionalParthian Sans Serif font, hinted.

%package -n noto-sans-javanese-fonts
Summary:        Noto Javanese Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-javanese
Provides:       noto-sans-javanese
%reconfigure_fonts_prereq

%description -n noto-sans-javanese-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Javanese Sans Serif font, hinted.

%package -n noto-sans-kaithi-fonts
Summary:        Noto Kaithi Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-kaithi
Provides:       noto-sans-kaithi
%reconfigure_fonts_prereq

%description -n noto-sans-kaithi-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Kaithi Sans Serif font, hinted.

%package -n noto-sans-kannada-fonts
Summary:        Noto Kannada Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-kannada
Provides:       noto-sans-kannada
%reconfigure_fonts_prereq

%description -n noto-sans-kannada-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Kannada Sans Serif font, hinted.

%package -n noto-sans-kannada-ui-fonts
Summary:        Noto Kannada Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-kannada-ui
Provides:       noto-sans-kannada-ui
%reconfigure_fonts_prereq

%description -n noto-sans-kannada-ui-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Kannada Sans Serif font, hinted.

%package -n noto-sans-kayahli-fonts
Summary:        Noto Kayah Li Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-kayahli
Provides:       noto-sans-kayahli
%reconfigure_fonts_prereq

%description -n noto-sans-kayahli-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
KayahLi Sans Serif font, hinted.

%package -n noto-sans-kharoshthi-fonts
Summary:        Noto Kharoshthi Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-kharoshthi
Provides:       noto-sans-kharoshthi
%reconfigure_fonts_prereq

%description -n noto-sans-kharoshthi-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Kharoshthi Sans Serif font, hinted.

%package -n noto-sans-khmer-fonts
Summary:        Noto Khmer Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-khmer
Provides:       noto-sans-khmer
%reconfigure_fonts_prereq

%description -n noto-sans-khmer-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Khmer Sans Serif font, hinted.

%package -n noto-sans-khmer-ui-fonts
Summary:        Noto Khmer Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-khmer-ui
Provides:       noto-sans-khmer-ui
%reconfigure_fonts_prereq

%description -n noto-sans-khmer-ui-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Khmer Sans Serif font, hinted.

%package -n noto-sans-lao-fonts
Summary:        Noto Lao Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-lao
Provides:       noto-sans-lao
%reconfigure_fonts_prereq

%description -n noto-sans-lao-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Lao Sans Serif font, hinted.

%package -n noto-sans-lao-ui-fonts
Summary:        Noto Lao Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-lao-ui
Provides:       noto-sans-lao-ui
%reconfigure_fonts_prereq

%description -n noto-sans-lao-ui-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Lao Sans Serif font, hinted.

%package -n noto-sans-lepcha-fonts
Summary:        Noto Lepcha Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-lepcha
Provides:       noto-sans-lepcha
%reconfigure_fonts_prereq

%description -n noto-sans-lepcha-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Lepcha Sans Serif font, hinted.

%package -n noto-sans-limbu-fonts
Summary:        Noto Limbu Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-limbu
Provides:       noto-sans-limbu
%reconfigure_fonts_prereq

%description -n noto-sans-limbu-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Limbu Sans Serif font, hinted.

%package -n noto-sans-linearb-fonts
Summary:        Noto Linear B Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-linearb
Provides:       noto-sans-linearb
%reconfigure_fonts_prereq

%description -n noto-sans-linearb-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
LinearB Sans Serif font, hinted.

%package -n noto-sans-lisu-fonts
Summary:        Noto Lisu Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-lisu
Provides:       noto-sans-lisu
%reconfigure_fonts_prereq

%description -n noto-sans-lisu-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Lisu Sans Serif font, hinted.

%package -n noto-sans-lycian-fonts
Summary:        Noto Lycian Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-lycian
Provides:       noto-sans-lycian
%reconfigure_fonts_prereq

%description -n noto-sans-lycian-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Lycian Sans Serif font, hinted.

%package -n noto-sans-lydian-fonts
Summary:        Noto Lydian Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-lydian
Provides:       noto-sans-lydian
%reconfigure_fonts_prereq

%description -n noto-sans-lydian-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Lydian Sans Serif font, hinted.

%package -n noto-sans-malayalam-fonts
Summary:        Noto Malayalam Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-malayalam
Provides:       noto-sans-malayalam
%reconfigure_fonts_prereq

%description -n noto-sans-malayalam-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Malayalam Sans Serif font, hinted.

%package -n noto-sans-malayalam-ui-fonts
Summary:        Noto Malayalam Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-malayalam-ui
Provides:       noto-sans-malayalam-ui
%reconfigure_fonts_prereq

%description -n noto-sans-malayalam-ui-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Malayalam Sans Serif font, hinted.

%package -n noto-sans-mandaic-fonts
Summary:        Noto Mandaic Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-mandaic
Provides:       noto-sans-mandaic
%reconfigure_fonts_prereq

%description -n noto-sans-mandaic-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Mandaic Sans Serif font, hinted.

%package -n noto-sans-meeteimayek-fonts
Summary:        Noto Meetei Mayek Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-meeteimayek
Provides:       noto-sans-meeteimayek
%reconfigure_fonts_prereq

%description -n noto-sans-meeteimayek-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
MeeteiMayek Sans Serif font, hinted.

%package -n noto-sans-mongolian-fonts
Summary:        Noto Mongolian Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-mongolian
Provides:       noto-sans-mongolian
%reconfigure_fonts_prereq

%description -n noto-sans-mongolian-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Mongolian Sans Serif font, hinted.

%package -n noto-sans-mono-fonts
Summary:        Noto Mono Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-mono
Provides:       noto-sans-mono
%reconfigure_fonts_prereq

%description -n noto-sans-mono-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Mono Sans Serif font, hinted.

%package -n noto-sans-myanmar-fonts
Summary:        Noto Myanmar Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-myanmar
Provides:       noto-sans-myanmar
%reconfigure_fonts_prereq

%description -n noto-sans-myanmar-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Myanmar Sans Serif font, hinted.

%package -n noto-sans-myanmar-ui-fonts
Summary:        Noto Myanmar Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-myanmar-ui
Provides:       noto-sans-myanmar-ui
%reconfigure_fonts_prereq

%description -n noto-sans-myanmar-ui-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Myanmar Sans Serif font, hinted.

%package -n noto-sans-newtailue-fonts
Summary:        Noto New Tai Lue Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-newtailue
Provides:       noto-sans-newtailue
%reconfigure_fonts_prereq

%description -n noto-sans-newtailue-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
NewTaiLue Sans Serif font, hinted.

%package -n noto-sans-nko-fonts
Summary:        Noto NKo Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-nko
Provides:       noto-sans-nko
%reconfigure_fonts_prereq

%description -n noto-sans-nko-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
NKo Sans Serif font, hinted.

%package -n noto-sans-ogham-fonts
Summary:        Noto Ogham Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-ogham
Provides:       noto-sans-ogham
%reconfigure_fonts_prereq

%description -n noto-sans-ogham-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Ogham Sans Serif font, hinted.

%package -n noto-sans-olchiki-fonts
Summary:        Noto Ol Chiki Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-olchiki
Provides:       noto-sans-olchiki
%reconfigure_fonts_prereq

%description -n noto-sans-olchiki-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
OlChiki Sans Serif font, hinted.

%package -n noto-sans-olditalic-fonts
Summary:        Noto Old Italic Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-olditalic
Provides:       noto-sans-olditalic
%reconfigure_fonts_prereq

%description -n noto-sans-olditalic-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
OldItalic Sans Serif font, hinted.

%package -n noto-sans-oldpersian-fonts
Summary:        Noto Old Persian Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-oldpersian
Provides:       noto-sans-oldpersian
%reconfigure_fonts_prereq

%description -n noto-sans-oldpersian-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
OldPersian Sans Serif font, hinted.

%package -n noto-sans-oldsoutharabian-fonts
Summary:        Noto Old South Arabian Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-oldsoutharabian
Provides:       noto-sans-oldsoutharabian
%reconfigure_fonts_prereq

%description -n noto-sans-oldsoutharabian-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
OldSouthArabian Sans Serif font, hinted.

%package -n noto-sans-oldturkic-fonts
Summary:        Noto Old Turkic Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-oldturkic
Provides:       noto-sans-oldturkic
%reconfigure_fonts_prereq

%description -n noto-sans-oldturkic-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
OldTurkic Sans Serif font, hinted.

%package -n noto-sans-oriya-fonts
Summary:        Noto Oriya Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-oriya
Provides:       noto-sans-oriya
%reconfigure_fonts_prereq

%description -n noto-sans-oriya-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Oriya Sans Serif font, hinted.

%package -n noto-sans-oriya-ui-fonts
Summary:        Noto Oriya Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-oriya-ui
Provides:       noto-sans-oriya-ui
%reconfigure_fonts_prereq

%description -n noto-sans-oriya-ui-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Oriya Sans Serif font, hinted.

%package -n noto-sans-osage-fonts
Summary:        Noto Osage Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-osage
Provides:       noto-sans-osage
%reconfigure_fonts_prereq

%description -n noto-sans-osage-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Osage Sans Serif font, hinted.

%package -n noto-sans-osmanya-fonts
Summary:        Noto Osmanya Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-osmanya
Provides:       noto-sans-osmanya
%reconfigure_fonts_prereq

%description -n noto-sans-osmanya-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Osmanya Sans Serif font, hinted.

%package -n noto-sans-phagspa-fonts
Summary:        Noto Phags Pa Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-phagspa
Provides:       noto-sans-phagspa
%reconfigure_fonts_prereq

%description -n noto-sans-phagspa-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
PhagsPa Sans Serif font, hinted.

%package -n noto-sans-phoenician-fonts
Summary:        Noto Phoenician Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-phoenician
Provides:       noto-sans-phoenician
%reconfigure_fonts_prereq

%description -n noto-sans-phoenician-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Phoenician Sans Serif font, hinted.

%package -n noto-sans-rejang-fonts
Summary:        Noto Rejang Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-rejang
Provides:       noto-sans-rejang
%reconfigure_fonts_prereq

%description -n noto-sans-rejang-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Rejang Sans Serif font, hinted.

%package -n noto-sans-runic-fonts
Summary:        Noto Runic Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-runic
Provides:       noto-sans-runic
%reconfigure_fonts_prereq

%description -n noto-sans-runic-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Runic Sans Serif font, hinted.

%package -n noto-sans-samaritan-fonts
Summary:        Noto Samaritan Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-samaritan
Provides:       noto-sans-samaritan
%reconfigure_fonts_prereq

%description -n noto-sans-samaritan-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Samaritan Sans Serif font, hinted.

%package -n noto-sans-saurashtra-fonts
Summary:        Noto Saurashtra Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-saurashtra
Provides:       noto-sans-saurashtra
%reconfigure_fonts_prereq

%description -n noto-sans-saurashtra-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Saurashtra Sans Serif font, hinted.

%package -n noto-sans-shavian-fonts
Summary:        Noto Shavian Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-shavian
Provides:       noto-sans-shavian
%reconfigure_fonts_prereq

%description -n noto-sans-shavian-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Shavian Sans Serif font, hinted.

%package -n noto-sans-sinhala-fonts
Summary:        Noto Sinhala Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-sinhala
Provides:       noto-sans-sinhala
%reconfigure_fonts_prereq

%description -n noto-sans-sinhala-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Sinhala Sans Serif font, hinted.

%package -n noto-sans-sinhala-ui-fonts
Summary:        Noto Sinhala Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-sinhala-ui
Provides:       noto-sans-sinhala-ui
%reconfigure_fonts_prereq

%description -n noto-sans-sinhala-ui-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Sinhala Sans Serif font, hinted.

%package -n noto-sans-sundanese-fonts
Summary:        Noto Sundanese Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-sundanese
Provides:       noto-sans-sundanese
%reconfigure_fonts_prereq

%description -n noto-sans-sundanese-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Sundanese Sans Serif font, hinted.

%package -n noto-sans-sylotinagri-fonts
Summary:        Noto Syloti Nagri Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-sylotinagri
Provides:       noto-sans-sylotinagri
%reconfigure_fonts_prereq

%description -n noto-sans-sylotinagri-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
SylotiNagri Sans Serif font, hinted.

%package -n noto-sans-symbols-fonts
Summary:        Noto Symbols Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-symbols
Provides:       noto-sans-symbols
%reconfigure_fonts_prereq

%description -n noto-sans-symbols-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Symbols Sans Serif font, hinted.

%package -n noto-sans-symbols2-fonts
Summary:        Noto Symbols2 Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-symbols2
Provides:       noto-sans-symbols2
%reconfigure_fonts_prereq

%description -n noto-sans-symbols2-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Symbols2 Sans Serif font, hinted.

%package -n noto-sans-syriaceastern-fonts
Summary:        Noto Syriac Eastern Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-syriaceastern
Provides:       noto-sans-syriaceastern
%reconfigure_fonts_prereq

%description -n noto-sans-syriaceastern-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
SyriacEastern Sans Serif font, hinted.

%package -n noto-sans-syriacestrangela-fonts
Summary:        Noto Syriac Estrangela Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-syriacestrangela
Provides:       noto-sans-syriacestrangela
%reconfigure_fonts_prereq

%description -n noto-sans-syriacestrangela-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
SyriacEstrangela Sans Serif font, hinted.

%package -n noto-sans-syriacwestern-fonts
Summary:        Noto Syriac Western Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-syriacwestern
Provides:       noto-sans-syriacwestern
%reconfigure_fonts_prereq

%description -n noto-sans-syriacwestern-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
SyriacWestern Sans Serif font, hinted.

%package -n noto-sans-tagalog-fonts
Summary:        Noto Tagalog Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-tagalog
Provides:       noto-sans-tagalog
%reconfigure_fonts_prereq

%description -n noto-sans-tagalog-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Tagalog Sans Serif font, hinted.

%package -n noto-sans-tagbanwa-fonts
Summary:        Noto Tagbanwa Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-tagbanwa
Provides:       noto-sans-tagbanwa
%reconfigure_fonts_prereq

%description -n noto-sans-tagbanwa-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Tagbanwa Sans Serif font, hinted.

%package -n noto-sans-taile-fonts
Summary:        Noto Tai Le Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-taile
Provides:       noto-sans-taile
%reconfigure_fonts_prereq

%description -n noto-sans-taile-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
TaiLe Sans Serif font, hinted.

%package -n noto-sans-taitham-fonts
Summary:        Noto Tai Tham Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-taitham
Provides:       noto-sans-taitham
%reconfigure_fonts_prereq

%description -n noto-sans-taitham-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
TaiTham Sans Serif font, hinted.

%package -n noto-sans-taiviet-fonts
Summary:        Noto Tai Viet Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-taiviet
Provides:       noto-sans-taiviet
%reconfigure_fonts_prereq

%description -n noto-sans-taiviet-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
TaiViet Sans Serif font, hinted.

%package -n noto-sans-tamil-fonts
Summary:        Noto Tamil Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-tamil
Provides:       noto-sans-tamil
%reconfigure_fonts_prereq

%description -n noto-sans-tamil-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Tamil Sans Serif font, hinted.

%package -n noto-sans-tamil-ui-fonts
Summary:        Noto Tamil Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-tamil-ui
Provides:       noto-sans-tamil-ui
%reconfigure_fonts_prereq

%description -n noto-sans-tamil-ui-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Tamil Sans Serif font, hinted.

%package -n noto-sans-telugu-fonts
Summary:        Noto Telugu Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-telugu
Provides:       noto-sans-telugu
%reconfigure_fonts_prereq

%description -n noto-sans-telugu-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Telugu Sans Serif font, hinted.

%package -n noto-sans-telugu-ui-fonts
Summary:        Noto Telugu Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-telugu-ui
Provides:       noto-sans-telugu-ui
%reconfigure_fonts_prereq

%description -n noto-sans-telugu-ui-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Telugu Sans Serif font, hinted.

%package -n noto-sans-thaana-fonts
Summary:        Noto Thaana Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-thaana
Provides:       noto-sans-thaana
%reconfigure_fonts_prereq

%description -n noto-sans-thaana-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Thaana Sans Serif font, hinted.

%package -n noto-sans-thai-fonts
Summary:        Noto Thai Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-thai
Provides:       noto-sans-thai
%reconfigure_fonts_prereq

%description -n noto-sans-thai-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Thai Sans Serif font, hinted.

%package -n noto-sans-thai-ui-fonts
Summary:        Noto Thai Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-thai-ui
Provides:       noto-sans-thai-ui
%reconfigure_fonts_prereq

%description -n noto-sans-thai-ui-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Thai Sans Serif font, hinted.

%package -n noto-sans-tibetan-fonts
Summary:        Noto Tibetan Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-tibetan
Provides:       noto-sans-tibetan
%reconfigure_fonts_prereq

%description -n noto-sans-tibetan-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Tibetan Sans Serif font, hinted.

%package -n noto-sans-tifinagh-fonts
Summary:        Noto Tifinagh Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-tifinagh
Provides:       noto-sans-tifinagh
%reconfigure_fonts_prereq

%description -n noto-sans-tifinagh-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Tifinagh Sans Serif font, hinted.

%package -n noto-sans-ugaritic-fonts
Summary:        Noto Ugaritic Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-ugaritic
Provides:       noto-sans-ugaritic
%reconfigure_fonts_prereq

%description -n noto-sans-ugaritic-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Ugaritic Sans Serif font, hinted.

%package -n noto-sans-vai-fonts
Summary:        Noto Vai Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-vai
Provides:       noto-sans-vai
%reconfigure_fonts_prereq

%description -n noto-sans-vai-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Vai Sans Serif font, hinted.

%package -n noto-sans-yi-fonts
Summary:        Noto Yi Sans Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-sans-yi
Provides:       noto-sans-yi
%reconfigure_fonts_prereq

%description -n noto-sans-yi-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Yi Sans Serif font, hinted.

%package -n noto-serif-fonts
Summary:        Noto Serif Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-serif
Provides:       noto-serif
%reconfigure_fonts_prereq

%description -n noto-serif-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Serif font, hinted.

%package -n noto-serif-armenian-fonts
Summary:        Noto Armenian Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-serif-armenian
Provides:       noto-serif-armenian
%reconfigure_fonts_prereq

%description -n noto-serif-armenian-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Armenian font, hinted.

%package -n noto-serif-bengali-fonts
Summary:        Noto Bengali Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-serif-bengali
Provides:       noto-serif-bengali
%reconfigure_fonts_prereq

%description -n noto-serif-bengali-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Bengali font, hinted.

%package -n noto-serif-devanagari-fonts
Summary:        Noto Devanagari Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-serif-devanagari
Provides:       noto-serif-devanagari
%reconfigure_fonts_prereq

%description -n noto-serif-devanagari-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Devanagari font, hinted.

%package -n noto-serif-display-fonts
Summary:        Noto Display Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-serif-display
Provides:       noto-serif-display
%reconfigure_fonts_prereq

%description -n noto-serif-display-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Display font, hinted.

%package -n noto-serif-ethiopic-fonts
Summary:        Noto Ethiopic Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-serif-ethiopic
Provides:       noto-serif-ethiopic
%reconfigure_fonts_prereq

%description -n noto-serif-ethiopic-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Ethiopic font, hinted.

%package -n noto-serif-georgian-fonts
Summary:        Noto Georgian Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-serif-georgian
Provides:       noto-serif-georgian
%reconfigure_fonts_prereq

%description -n noto-serif-georgian-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Georgian font, hinted.

%package -n noto-serif-gujarati-fonts
Summary:        Noto Gujarati Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-serif-gujarati
Provides:       noto-serif-gujarati
%reconfigure_fonts_prereq

%description -n noto-serif-gujarati-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Gujarati font, hinted.

%package -n noto-serif-hebrew-fonts
Summary:        Noto Hebrew Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-serif-hebrew
Provides:       noto-serif-hebrew
%reconfigure_fonts_prereq

%description -n noto-serif-hebrew-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Hebrew font, hinted.

%package -n noto-serif-kannada-fonts
Summary:        Noto Kannada Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-serif-kannada
Provides:       noto-serif-kannada
%reconfigure_fonts_prereq

%description -n noto-serif-kannada-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Kannada font, hinted.

%package -n noto-serif-khmer-fonts
Summary:        Noto Khmer Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-serif-khmer
Provides:       noto-serif-khmer
%reconfigure_fonts_prereq

%description -n noto-serif-khmer-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Khmer font, hinted.

%package -n noto-serif-lao-fonts
Summary:        Noto Lao Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-serif-lao
Provides:       noto-serif-lao
%reconfigure_fonts_prereq

%description -n noto-serif-lao-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Lao font, hinted.

%package -n noto-serif-malayalam-fonts
Summary:        Noto Malayalam Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-serif-malayalam
Provides:       noto-serif-malayalam
%reconfigure_fonts_prereq

%description -n noto-serif-malayalam-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Malayalam font, hinted.

%package -n noto-serif-myanmar-fonts
Summary:        Noto Myanmar Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-serif-myanmar
Provides:       noto-serif-myanmar
%reconfigure_fonts_prereq

%description -n noto-serif-myanmar-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Myanmar font, hinted.

%package -n noto-serif-sinhala-fonts
Summary:        Noto Sinhala Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-serif-sinhala
Provides:       noto-serif-sinhala
%reconfigure_fonts_prereq

%description -n noto-serif-sinhala-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Sinhala font, hinted.

%package -n noto-serif-tamil-fonts
Summary:        Noto Tamil Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-serif-tamil
Provides:       noto-serif-tamil
%reconfigure_fonts_prereq

%description -n noto-serif-tamil-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Tamil font, hinted.

%package -n noto-serif-telugu-fonts
Summary:        Noto Telugu Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-serif-telugu
Provides:       noto-serif-telugu
%reconfigure_fonts_prereq

%description -n noto-serif-telugu-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Telugu font, hinted.

%package -n noto-serif-thai-fonts
Summary:        Noto Thai Font
Group:          System/X11/Fonts
Recommends:     google-noto-fonts-doc
Obsoletes:      noto-serif-thai
Provides:       noto-serif-thai
%reconfigure_fonts_prereq

%description -n noto-serif-thai-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Thai font, hinted.



%prep
%setup -q -c -n %{name}-%{version}
# remove cjk
rm -rf *CJK*.?tf
# remove emoji
rm -rf *Emoji*.ttf

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}
cp *.?tf   %{buildroot}%{_ttfontsdir}/

%reconfigure_fonts_scriptlets -n noto-kufiarabic-fonts

%reconfigure_fonts_scriptlets -n noto-mono-fonts

%reconfigure_fonts_scriptlets -n noto-naskharabic-fonts

%reconfigure_fonts_scriptlets -n noto-naskharabic-ui-fonts

%reconfigure_fonts_scriptlets -n noto-nastaliqurdu-fonts

%reconfigure_fonts_scriptlets -n noto-sans-fonts

%reconfigure_fonts_scriptlets -n noto-sans-adlam-fonts

%reconfigure_fonts_scriptlets -n noto-sans-adlamunjoined-fonts

%reconfigure_fonts_scriptlets -n noto-sans-anatolianhieroglyphs-fonts

%reconfigure_fonts_scriptlets -n noto-sans-arabic-fonts

%reconfigure_fonts_scriptlets -n noto-sans-arabic-ui-fonts

%reconfigure_fonts_scriptlets -n noto-sans-armenian-fonts

%reconfigure_fonts_scriptlets -n noto-sans-avestan-fonts

%reconfigure_fonts_scriptlets -n noto-sans-balinese-fonts

%reconfigure_fonts_scriptlets -n noto-sans-bamum-fonts

%reconfigure_fonts_scriptlets -n noto-sans-batak-fonts

%reconfigure_fonts_scriptlets -n noto-sans-bengali-fonts

%reconfigure_fonts_scriptlets -n noto-sans-bengali-ui-fonts

%reconfigure_fonts_scriptlets -n noto-sans-brahmi-fonts

%reconfigure_fonts_scriptlets -n noto-sans-buginese-fonts

%reconfigure_fonts_scriptlets -n noto-sans-buhid-fonts

%reconfigure_fonts_scriptlets -n noto-sans-canadianaboriginal-fonts

%reconfigure_fonts_scriptlets -n noto-sans-carian-fonts

%reconfigure_fonts_scriptlets -n noto-sans-chakma-fonts

%reconfigure_fonts_scriptlets -n noto-sans-cham-fonts

%reconfigure_fonts_scriptlets -n noto-sans-cherokee-fonts

%reconfigure_fonts_scriptlets -n noto-sans-coptic-fonts

%reconfigure_fonts_scriptlets -n noto-sans-cuneiform-fonts

%reconfigure_fonts_scriptlets -n noto-sans-cypriot-fonts

%reconfigure_fonts_scriptlets -n noto-sans-deseret-fonts

%reconfigure_fonts_scriptlets -n noto-sans-devanagari-fonts

%reconfigure_fonts_scriptlets -n noto-sans-devanagari-ui-fonts

%reconfigure_fonts_scriptlets -n noto-sans-display-fonts

%reconfigure_fonts_scriptlets -n noto-sans-egyptianhieroglyphs-fonts

%reconfigure_fonts_scriptlets -n noto-sans-ethiopic-fonts

%reconfigure_fonts_scriptlets -n noto-sans-georgian-fonts

%reconfigure_fonts_scriptlets -n noto-sans-glagolitic-fonts

%reconfigure_fonts_scriptlets -n noto-sans-gothic-fonts

%reconfigure_fonts_scriptlets -n noto-sans-gujarati-fonts

%reconfigure_fonts_scriptlets -n noto-sans-gujarati-ui-fonts

%reconfigure_fonts_scriptlets -n noto-sans-gurmukhi-fonts

%reconfigure_fonts_scriptlets -n noto-sans-gurmukhi-ui-fonts

%reconfigure_fonts_scriptlets -n noto-sans-hanunoo-fonts

%reconfigure_fonts_scriptlets -n noto-sans-hebrew-fonts

%reconfigure_fonts_scriptlets -n noto-sans-imperialaramaic-fonts

%reconfigure_fonts_scriptlets -n noto-sans-inscriptionalpahlavi-fonts

%reconfigure_fonts_scriptlets -n noto-sans-inscriptionalparthian-fonts

%reconfigure_fonts_scriptlets -n noto-sans-javanese-fonts

%reconfigure_fonts_scriptlets -n noto-sans-kaithi-fonts

%reconfigure_fonts_scriptlets -n noto-sans-kannada-fonts

%reconfigure_fonts_scriptlets -n noto-sans-kannada-ui-fonts

%reconfigure_fonts_scriptlets -n noto-sans-kayahli-fonts

%reconfigure_fonts_scriptlets -n noto-sans-kharoshthi-fonts

%reconfigure_fonts_scriptlets -n noto-sans-khmer-fonts

%reconfigure_fonts_scriptlets -n noto-sans-khmer-ui-fonts

%reconfigure_fonts_scriptlets -n noto-sans-lao-fonts

%reconfigure_fonts_scriptlets -n noto-sans-lao-ui-fonts

%reconfigure_fonts_scriptlets -n noto-sans-lepcha-fonts

%reconfigure_fonts_scriptlets -n noto-sans-limbu-fonts

%reconfigure_fonts_scriptlets -n noto-sans-linearb-fonts

%reconfigure_fonts_scriptlets -n noto-sans-lisu-fonts

%reconfigure_fonts_scriptlets -n noto-sans-lycian-fonts

%reconfigure_fonts_scriptlets -n noto-sans-lydian-fonts

%reconfigure_fonts_scriptlets -n noto-sans-malayalam-fonts

%reconfigure_fonts_scriptlets -n noto-sans-malayalam-ui-fonts

%reconfigure_fonts_scriptlets -n noto-sans-mandaic-fonts

%reconfigure_fonts_scriptlets -n noto-sans-meeteimayek-fonts

%reconfigure_fonts_scriptlets -n noto-sans-mongolian-fonts

%reconfigure_fonts_scriptlets -n noto-sans-mono-fonts

%reconfigure_fonts_scriptlets -n noto-sans-myanmar-fonts

%reconfigure_fonts_scriptlets -n noto-sans-myanmar-ui-fonts

%reconfigure_fonts_scriptlets -n noto-sans-newtailue-fonts

%reconfigure_fonts_scriptlets -n noto-sans-nko-fonts

%reconfigure_fonts_scriptlets -n noto-sans-ogham-fonts

%reconfigure_fonts_scriptlets -n noto-sans-olchiki-fonts

%reconfigure_fonts_scriptlets -n noto-sans-olditalic-fonts

%reconfigure_fonts_scriptlets -n noto-sans-oldpersian-fonts

%reconfigure_fonts_scriptlets -n noto-sans-oldsoutharabian-fonts

%reconfigure_fonts_scriptlets -n noto-sans-oldturkic-fonts

%reconfigure_fonts_scriptlets -n noto-sans-oriya-fonts

%reconfigure_fonts_scriptlets -n noto-sans-oriya-ui-fonts

%reconfigure_fonts_scriptlets -n noto-sans-osage-fonts

%reconfigure_fonts_scriptlets -n noto-sans-osmanya-fonts

%reconfigure_fonts_scriptlets -n noto-sans-phagspa-fonts

%reconfigure_fonts_scriptlets -n noto-sans-phoenician-fonts

%reconfigure_fonts_scriptlets -n noto-sans-rejang-fonts

%reconfigure_fonts_scriptlets -n noto-sans-runic-fonts

%reconfigure_fonts_scriptlets -n noto-sans-samaritan-fonts

%reconfigure_fonts_scriptlets -n noto-sans-saurashtra-fonts

%reconfigure_fonts_scriptlets -n noto-sans-shavian-fonts

%reconfigure_fonts_scriptlets -n noto-sans-sinhala-fonts

%reconfigure_fonts_scriptlets -n noto-sans-sinhala-ui-fonts

%reconfigure_fonts_scriptlets -n noto-sans-sundanese-fonts

%reconfigure_fonts_scriptlets -n noto-sans-sylotinagri-fonts

%reconfigure_fonts_scriptlets -n noto-sans-symbols-fonts

%reconfigure_fonts_scriptlets -n noto-sans-symbols2-fonts

%reconfigure_fonts_scriptlets -n noto-sans-syriaceastern-fonts

%reconfigure_fonts_scriptlets -n noto-sans-syriacestrangela-fonts

%reconfigure_fonts_scriptlets -n noto-sans-syriacwestern-fonts

%reconfigure_fonts_scriptlets -n noto-sans-tagalog-fonts

%reconfigure_fonts_scriptlets -n noto-sans-tagbanwa-fonts

%reconfigure_fonts_scriptlets -n noto-sans-taile-fonts

%reconfigure_fonts_scriptlets -n noto-sans-taitham-fonts

%reconfigure_fonts_scriptlets -n noto-sans-taiviet-fonts

%reconfigure_fonts_scriptlets -n noto-sans-tamil-fonts

%reconfigure_fonts_scriptlets -n noto-sans-tamil-ui-fonts

%reconfigure_fonts_scriptlets -n noto-sans-telugu-fonts

%reconfigure_fonts_scriptlets -n noto-sans-telugu-ui-fonts

%reconfigure_fonts_scriptlets -n noto-sans-thaana-fonts

%reconfigure_fonts_scriptlets -n noto-sans-thai-fonts

%reconfigure_fonts_scriptlets -n noto-sans-thai-ui-fonts

%reconfigure_fonts_scriptlets -n noto-sans-tibetan-fonts

%reconfigure_fonts_scriptlets -n noto-sans-tifinagh-fonts

%reconfigure_fonts_scriptlets -n noto-sans-ugaritic-fonts

%reconfigure_fonts_scriptlets -n noto-sans-vai-fonts

%reconfigure_fonts_scriptlets -n noto-sans-yi-fonts

%reconfigure_fonts_scriptlets -n noto-serif-fonts

%reconfigure_fonts_scriptlets -n noto-serif-armenian-fonts

%reconfigure_fonts_scriptlets -n noto-serif-bengali-fonts

%reconfigure_fonts_scriptlets -n noto-serif-devanagari-fonts

%reconfigure_fonts_scriptlets -n noto-serif-display-fonts

%reconfigure_fonts_scriptlets -n noto-serif-ethiopic-fonts

%reconfigure_fonts_scriptlets -n noto-serif-georgian-fonts

%reconfigure_fonts_scriptlets -n noto-serif-gujarati-fonts

%reconfigure_fonts_scriptlets -n noto-serif-hebrew-fonts

%reconfigure_fonts_scriptlets -n noto-serif-kannada-fonts

%reconfigure_fonts_scriptlets -n noto-serif-khmer-fonts

%reconfigure_fonts_scriptlets -n noto-serif-lao-fonts

%reconfigure_fonts_scriptlets -n noto-serif-malayalam-fonts

%reconfigure_fonts_scriptlets -n noto-serif-myanmar-fonts

%reconfigure_fonts_scriptlets -n noto-serif-sinhala-fonts

%reconfigure_fonts_scriptlets -n noto-serif-tamil-fonts

%reconfigure_fonts_scriptlets -n noto-serif-telugu-fonts

%reconfigure_fonts_scriptlets -n noto-serif-thai-fonts

%files doc
%defattr(0644,root,root,755)
%doc LICENSE*.txt

%files -n noto-kufiarabic-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoKufiArabic-*.?tf

%files -n noto-mono-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoMono-*.?tf

%files -n noto-naskharabic-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoNaskhArabic-*.?tf

%files -n noto-naskharabic-ui-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoNaskhArabicUI-*.?tf

%files -n noto-nastaliqurdu-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoNastaliqUrdu-*.?tf

%files -n noto-sans-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSans-*.?tf

%files -n noto-sans-adlam-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansAdlam-*.?tf

%files -n noto-sans-adlamunjoined-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansAdlamUnjoined-*.?tf

%files -n noto-sans-anatolianhieroglyphs-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansAnatolianHieroglyphs-*.?tf

%files -n noto-sans-arabic-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansArabic-*.?tf

%files -n noto-sans-arabic-ui-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansArabicUI-*.?tf

%files -n noto-sans-armenian-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansArmenian-*.?tf

%files -n noto-sans-avestan-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansAvestan-*.?tf

%files -n noto-sans-balinese-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansBalinese-*.?tf

%files -n noto-sans-bamum-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansBamum-*.?tf

%files -n noto-sans-batak-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansBatak-*.?tf

%files -n noto-sans-bengali-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansBengali-*.?tf

%files -n noto-sans-bengali-ui-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansBengaliUI-*.?tf

%files -n noto-sans-brahmi-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansBrahmi-*.?tf

%files -n noto-sans-buginese-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansBuginese-*.?tf

%files -n noto-sans-buhid-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansBuhid-*.?tf

%files -n noto-sans-canadianaboriginal-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansCanadianAboriginal-*.?tf

%files -n noto-sans-carian-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansCarian-*.?tf

%files -n noto-sans-chakma-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansChakma-*.?tf

%files -n noto-sans-cham-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansCham-*.?tf

%files -n noto-sans-cherokee-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansCherokee-*.?tf

%files -n noto-sans-coptic-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansCoptic-*.?tf

%files -n noto-sans-cuneiform-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansCuneiform-*.?tf

%files -n noto-sans-cypriot-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansCypriot-*.?tf

%files -n noto-sans-deseret-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansDeseret-*.?tf

%files -n noto-sans-devanagari-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansDevanagari-*.?tf

%files -n noto-sans-devanagari-ui-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansDevanagariUI-*.?tf

%files -n noto-sans-display-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansDisplay-*.?tf

%files -n noto-sans-egyptianhieroglyphs-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansEgyptianHieroglyphs-*.?tf

%files -n noto-sans-ethiopic-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansEthiopic-*.?tf

%files -n noto-sans-georgian-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansGeorgian-*.?tf

%files -n noto-sans-glagolitic-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansGlagolitic-*.?tf

%files -n noto-sans-gothic-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansGothic-*.?tf

%files -n noto-sans-gujarati-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansGujarati-*.?tf

%files -n noto-sans-gujarati-ui-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansGujaratiUI-*.?tf

%files -n noto-sans-gurmukhi-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansGurmukhi-*.?tf

%files -n noto-sans-gurmukhi-ui-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansGurmukhiUI-*.?tf

%files -n noto-sans-hanunoo-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansHanunoo-*.?tf

%files -n noto-sans-hebrew-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansHebrew-*.?tf

%files -n noto-sans-imperialaramaic-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansImperialAramaic-*.?tf

%files -n noto-sans-inscriptionalpahlavi-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansInscriptionalPahlavi-*.?tf

%files -n noto-sans-inscriptionalparthian-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansInscriptionalParthian-*.?tf

%files -n noto-sans-javanese-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansJavanese-*.?tf

%files -n noto-sans-kaithi-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansKaithi-*.?tf

%files -n noto-sans-kannada-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansKannada-*.?tf

%files -n noto-sans-kannada-ui-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansKannadaUI-*.?tf

%files -n noto-sans-kayahli-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansKayahLi-*.?tf

%files -n noto-sans-kharoshthi-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansKharoshthi-*.?tf

%files -n noto-sans-khmer-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansKhmer-*.?tf

%files -n noto-sans-khmer-ui-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansKhmerUI-*.?tf

%files -n noto-sans-lao-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansLao-*.?tf

%files -n noto-sans-lao-ui-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansLaoUI-*.?tf

%files -n noto-sans-lepcha-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansLepcha-*.?tf

%files -n noto-sans-limbu-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansLimbu-*.?tf

%files -n noto-sans-linearb-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansLinearB-*.?tf

%files -n noto-sans-lisu-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansLisu-*.?tf

%files -n noto-sans-lycian-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansLycian-*.?tf

%files -n noto-sans-lydian-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansLydian-*.?tf

%files -n noto-sans-malayalam-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansMalayalam-*.?tf

%files -n noto-sans-malayalam-ui-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansMalayalamUI-*.?tf

%files -n noto-sans-mandaic-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansMandaic-*.?tf

%files -n noto-sans-meeteimayek-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansMeeteiMayek-*.?tf

%files -n noto-sans-mongolian-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansMongolian-*.?tf

%files -n noto-sans-mono-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansMono-*.?tf

%files -n noto-sans-myanmar-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansMyanmar-*.?tf

%files -n noto-sans-myanmar-ui-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansMyanmarUI-*.?tf

%files -n noto-sans-newtailue-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansNewTaiLue-*.?tf

%files -n noto-sans-nko-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansNKo-*.?tf

%files -n noto-sans-ogham-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansOgham-*.?tf

%files -n noto-sans-olchiki-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansOlChiki-*.?tf

%files -n noto-sans-olditalic-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansOldItalic-*.?tf

%files -n noto-sans-oldpersian-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansOldPersian-*.?tf

%files -n noto-sans-oldsoutharabian-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansOldSouthArabian-*.?tf

%files -n noto-sans-oldturkic-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansOldTurkic-*.?tf

%files -n noto-sans-oriya-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansOriya-*.?tf

%files -n noto-sans-oriya-ui-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansOriyaUI-*.?tf

%files -n noto-sans-osage-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansOsage-*.?tf

%files -n noto-sans-osmanya-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansOsmanya-*.?tf

%files -n noto-sans-phagspa-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansPhagsPa-*.?tf

%files -n noto-sans-phoenician-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansPhoenician-*.?tf

%files -n noto-sans-rejang-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansRejang-*.?tf

%files -n noto-sans-runic-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansRunic-*.?tf

%files -n noto-sans-samaritan-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansSamaritan-*.?tf

%files -n noto-sans-saurashtra-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansSaurashtra-*.?tf

%files -n noto-sans-shavian-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansShavian-*.?tf

%files -n noto-sans-sinhala-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansSinhala-*.?tf

%files -n noto-sans-sinhala-ui-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansSinhalaUI-*.?tf

%files -n noto-sans-sundanese-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansSundanese-*.?tf

%files -n noto-sans-sylotinagri-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansSylotiNagri-*.?tf

%files -n noto-sans-symbols-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansSymbols-*.?tf

%files -n noto-sans-symbols2-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansSymbols2-*.?tf

%files -n noto-sans-syriaceastern-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansSyriacEastern-*.?tf

%files -n noto-sans-syriacestrangela-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansSyriacEstrangela-*.?tf

%files -n noto-sans-syriacwestern-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansSyriacWestern-*.?tf

%files -n noto-sans-tagalog-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansTagalog-*.?tf

%files -n noto-sans-tagbanwa-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansTagbanwa-*.?tf

%files -n noto-sans-taile-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansTaiLe-*.?tf

%files -n noto-sans-taitham-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansTaiTham-*.?tf

%files -n noto-sans-taiviet-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansTaiViet-*.?tf

%files -n noto-sans-tamil-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansTamil-*.?tf

%files -n noto-sans-tamil-ui-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansTamilUI-*.?tf

%files -n noto-sans-telugu-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansTelugu-*.?tf

%files -n noto-sans-telugu-ui-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansTeluguUI-*.?tf

%files -n noto-sans-thaana-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansThaana-*.?tf

%files -n noto-sans-thai-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansThai-*.?tf

%files -n noto-sans-thai-ui-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansThaiUI-*.?tf

%files -n noto-sans-tibetan-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansTibetan-*.?tf

%files -n noto-sans-tifinagh-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansTifinagh-*.?tf

%files -n noto-sans-ugaritic-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansUgaritic-*.?tf

%files -n noto-sans-vai-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansVai-*.?tf

%files -n noto-sans-yi-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansYi-*.?tf

%files -n noto-serif-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerif-*.?tf

%files -n noto-serif-armenian-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifArmenian-*.?tf

%files -n noto-serif-bengali-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifBengali-*.?tf

%files -n noto-serif-devanagari-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifDevanagari-*.?tf

%files -n noto-serif-display-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifDisplay-*.?tf

%files -n noto-serif-ethiopic-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifEthiopic-*.?tf

%files -n noto-serif-georgian-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifGeorgian-*.?tf

%files -n noto-serif-gujarati-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifGujarati-*.?tf

%files -n noto-serif-hebrew-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifHebrew-*.?tf

%files -n noto-serif-kannada-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifKannada-*.?tf

%files -n noto-serif-khmer-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifKhmer-*.?tf

%files -n noto-serif-lao-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifLao-*.?tf

%files -n noto-serif-malayalam-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifMalayalam-*.?tf

%files -n noto-serif-myanmar-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifMyanmar-*.?tf

%files -n noto-serif-sinhala-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifSinhala-*.?tf

%files -n noto-serif-tamil-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifTamil-*.?tf

%files -n noto-serif-telugu-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifTelugu-*.?tf

%files -n noto-serif-thai-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifThai-*.?tf

%changelog
